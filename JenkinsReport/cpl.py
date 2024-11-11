import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import json
from tabulate import tabulate
import os
# import datetime
from datetime import datetime
import colorama
import sys
# from cryptography.fernet import Fernet
import argparse
import getpass

# MARICADAS ===========================================================================
def color_environment(env,color=None):
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[33m"  # \033[93m
    RESET = "\033[0m"   #\033[1m
    txt = str(env).strip()
    colorama.init()
    if color=="Green":
        return f"{GREEN}{txt}{RESET}"
    elif color=="Red":
        return f"{RED}{txt}{RESET}"
    else:
        if txt == "SUCCESS":
            return f"{GREEN}{txt}{RESET}"
        elif txt == "None":
            return f"{YELLOW}{txt}{RESET}"
        else:
            return f"{RED}{txt}{RESET}"
    # return env  # Sin color para otros entornos

def get_credential():
    credenciales = {}
    try:
        ruta = r"C:/Cave/token.key"
        if os.path.exists(ruta):
            with open(ruta, 'r') as f:
                for linea in f:
                    clave, valor = linea.strip().split(': ')
                    credenciales[clave] = valor
            return credenciales
        else:
            login()
    except FileNotFoundError:
        # (f"El archivo token.key no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def save_credentials(Username, password):
    try:
        directory = r"C:/Cave"
        file_path = os.path.join(directory, 'token.key')
        if os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(f"User: {Username}\n")
                f.write(f"Pass: {password}\n")
            sys.exit()
        else:
            print(f"Ruta '{file_path}, no existe'")
    except:
        print(f"Error al crear token.key en '{directory}'")
        sys.exit(1)


def login():
    credenciales = {}
    url = 'http://172.20.10.55:8080/api/json'
    # Credenciales
    print(f"Authentication required for {url} (Jenkins)")
    username = input("Username: ")
    password = getpass.getpass("Pass/Token: ")
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    if response.ok:
        print("Credentials will be saved")
        save_credentials(username, password)
        # return credenciales
    else:
        print(f"Login failed ({response.status_code})")
        print("Verify you have provided correct credentials.")
        sys.exit()
# ======================================================================================
def consulta(perfil):
    credenciales = get_credential()
    if credenciales is None:
        sys.exit()
    response1 = requests.get("http://172.20.10.55:8080/api/json",
                             auth=(credenciales.get('User'), credenciales.get('Pass')))

    if response1.status_code == 200:
        data = response1.json()
        jobs = data.get('jobs', [])
        if perfil:
            filtered_jobs = [job for job in jobs if job['name'].endswith("CERT")]  ## USANDO FILTRO
            tabla = [[job['name'], job['url']] for job in filtered_jobs]  ## UTILIZANDO FILTRO
        else:
            tabla = [[item['name'], item['url']] for item in jobs]  ## SIN FILTRO
            # tabla = [[i + 1, job['name'], job['url']] for i, job in enumerate(filtered_jobs)]## ENUMEADO CON FILTRO

        # Imprimiendo la tabla tabulada
        # print(tabulate(tabla, headers=["ID","Nombre", "Valor"], tablefmt="grid"))
        print(tabulate(tabla, headers=["JOB", "URL"], tablefmt='psql', showindex=False))

        # Imprimiendo matriz dataframe
        # df = pd.DataFrame(tabla, columns=["Nombre", "URL"])
        # print(df)
    else:
        print(f"Error en la solicitud: {response1.status_code}")

# ======================================================================================
def previousBuild(url):
    credenciales = get_credential()
    if credenciales is None:
        sys.exit()
    # http://172.20.10.55:8080/job/BOX-CERT/job/box-bus/24/
    if url is None:
        return {'pBranch': "-", 'pUser': "-", 'pTime': "-", 'pResult': "-"}  # Devuelve un diccionario
    try:
        USR = credenciales.get('User')
        PASS = credenciales.get('Pass')
        pbranch = ""
        puserName = ""
        response = requests.get(url + "/api/json", auth=(USR, PASS))
        if response.status_code == 200:
            data = response.json()
            puserName = str(data['actions'][1]['causes'][0]['userId']).upper()  # str(userName).upper()
            pbranch = data['actions'][0]['parameters'][0]['value']
            timestamp = (data.get("timestamp") / 1000)  # fechahora.strftime("%Y-%m-%d %H:%M:%S")
            pfechahora = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
            presult = color_environment(data.get("result"))
            return {'pBranch': pbranch, 'pUser': puserName, 'pTime': pfechahora,
                    'pResult': presult}  # Devuelve un diccionario
    except FileNotFoundError:
        return {'pBranch': "-", 'pUser': "-", 'pTime': "-", 'pResult': "-"}  # Devuelve un diccionario
# ======================================================================================
def consultaTotal(JOB, filter = None):
    credenciales = get_credential()
    if credenciales is None:
        sys.exit()
    USR = credenciales.get('User')
    PASS = credenciales.get('Pass')
    response = requests.get(f"http://172.20.10.55:8080/job/{JOB}/api/json", auth=(USR, PASS))
    if response.status_code == 200:
        data = response.json()
        jobs = data.get('jobs', [])
        params = []
        for job in jobs:
            if job['name'][-6:] =="devops" and filter:
               continue
            subResponse = requests.get(f"http://172.20.10.55:8080/job/{JOB}/job/{job['name']}/lastBuild/api/json",auth=(USR, PASS))
            if subResponse.status_code == 200:
                dataX = subResponse.json()
                fullDisplayName = dataX.get("fullDisplayName")
                for action in dataX["actions"]:
                    if "_class" in action and action["_class"] == "hudson.model.ParametersAction":
                        for param in action["parameters"]:
                            branch = param.get("value")
                            # params.append({"Value": value})
                    if "_class" in action and action["_class"] == "hudson.model.CauseAction":
                        for param in action["causes"]:
                            # userName = param.get("userName")
                            userName = param.get("userId")
                timestamp = dataX.get("timestamp") / 1000
                fechahora = datetime.fromtimestamp(timestamp)
                result = dataX.get("result")

                previousUrl = dataX.get("previousBuild", {}).get("url") if dataX.get("previousBuild") else None
                previous = previousBuild(previousUrl)

                params.append({"FullName": fullDisplayName,
                               "LastBuild": branch,
                               "User": str(userName).upper(),
                               "DateTime": fechahora.strftime("%Y-%m-%d %H:%M:%S"),
                               "Result": color_environment(result),

                               "PreviousBuild": previous['pBranch'],
                               "PrevUser": previous['pUser'],
                               "PrevDateTime": previous['pTime'],
                               "PrevResult": previous['pResult'],
                               })
            else:
                print(f"{subResponse.status_code}.Pipeline no desplegado: {job['name']}.")

        df3 = pd.DataFrame(params)
        df3['DateTime'] = pd.to_datetime(df3['DateTime'])
        df3 = df3.sort_values(by='DateTime', ascending=False)
        print(tabulate(df3, headers='keys', tablefmt='psql', showindex=False))

    else:
        print(f"{response.status_code}-Error en la solicitud [{JOB}]")

    # FIN
def deploy(JOB, BRANCH):
    credenciales = get_credential()
    if credenciales is None:
        sys.exit()
    try:
        USR = credenciales.get('User')
        PASS = credenciales.get('Pass')
        PROJECT_JOB = JOB[:3].upper()
        #print(f"http://172.20.10.55:8080/job/{PROJECT_JOB}-CERT/job/{JOB}/buildWithParameters?DEPLOY_BRANCH={BRANCH}")
        response = requests.post(f"http://172.20.10.55:8080/job/{PROJECT_JOB}-CERT/job/{JOB}/buildWithParameters?DEPLOY_BRANCH={BRANCH}", auth=(USR, PASS))
        if response.status_code == 201:
            print(f"Se ejecutó el Pipeline:{color_environment(JOB,'Green')} \tRama:{color_environment(BRANCH,'Green')}.")
            print(f"Verificar:http://172.20.10.55:8080/job/{PROJECT_JOB}-CERT/job/{JOB}")
        else:
            print(f"Error al realizar el despliegue:{response.status_code}")

    except FileNotFoundError:
        print(f"Error en la solicitud: {response.status_code}")

# LLAMADA DEL CMD=======================================================================
def main():
    parser = argparse.ArgumentParser(description="Aplicativo para procesar comandos.")
    parser.add_argument('job', help='Nombre del Pipeline') # type=str,
    parser.add_argument('branch',nargs='?', help='La rama de despliegue', default='master')
    parser.add_argument('-d', '--deploy', action='store_true', help='Indica que se realizará un despliegue')
    args = parser.parse_args()
    JOB = str(args.job).strip()
    DEPLOY = args.deploy
    BRANCH = str(args.branch).strip()
    if args.deploy and args.branch and args.job:
        deploy(JOB,BRANCH)
        return
    if args.job:
        if len(JOB) >= 1:
            if JOB == "?":
                consulta(1)  # 1 QA
            elif JOB == "??":
                consulta(0)  # 0 DEV
            elif len(JOB) == 3:
                JOB = JOB + "-CERT"
                consultaTotal(JOB,True)
            elif JOB == "LOGIN":
                login()
            else:
                consultaTotal(JOB)
        sys.exit(1)
    else:
        print("Error: Se debe especificar la rama para realizar el despliegue.")
        return
if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit(1)


# pyinstaller --onefile --icon=cpl.ico cpl.py
# pyinstaller --onefile cpl.py
