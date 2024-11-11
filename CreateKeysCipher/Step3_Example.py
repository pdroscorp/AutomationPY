from cryptography.fernet import Fernet
def get_credential ():
    # Cargar la clave desde el archivo
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)

    # Esta es tu clave encriptada (usa el valor que generaste antes)
    user_encrypted_key = b"gAAAAABm_qqPC8rR_L0SH3VXB236zhQqKPm4rOjyNxTr0lfNXkqgaE-WQ3tsTPnJ-ykP58Y1MSQyVQxRGvmJT23zRz5IBkNTUQ=="  # Reemplaza con tu clave encriptada
    pass_encrypted_key = b"gAAAAABm_qqPymDV9uLlzN080PBfD_c8Ef4Tipb8qyPkzdErbwcKV7IUJcMcWntJNGcQQnRS9E5OVzcfAp7i-UjNZryAnPOfAH5M3QPKFAqqlV2sKh271AloWJMseGPxfD2kgXgWzktK"  # Reemplaza con tu clave encriptada

    #USER:  gAAAAABm_qqPC8rR_L0SH3VXB236zhQqKPm4rOjyNxTr0lfNXkqgaE-WQ3tsTPnJ-ykP58Y1MSQyVQxRGvmJT23zRz5IBkNTUQ==
    #PASS:  gAAAAABm_qqPymDV9uLlzN080PBfD_c8Ef4Tipb8qyPkzdErbwcKV7IUJcMcWntJNGcQQnRS9E5OVzcfAp7i-UjNZryAnPOfAH5M3QPKFAqqlV2sKh271AloWJMseGPxfD2kgXgWzktK


    # Desencriptar la clave
    decrypted_key_user = cipher_suite.decrypt(user_encrypted_key)
    decrypted_key_pass = cipher_suite.decrypt(pass_encrypted_key)

    print(f"User desencriptada: {decrypted_key_user.decode()}")
    print(f"Pass desencriptada: {decrypted_key_pass.decode()}")

    # Aquí puedes hacer tus consultas usando `decrypted_key`
    # Ejemplo de uso en una consulta
def realizar_consulta(conexion, clave):
 # Aquí iría tu lógica de consulta, usando `clave`
 print(f"Realizando consulta con la clave: {get_credential('USR'), get_credential('PASS')}")

# Supongamos que tienes una conexión a tu base de datos
# conexion = obtener_conexion_a_base_de_datos()
# realizar_consulta(conexion, decrypted_key.decode())
