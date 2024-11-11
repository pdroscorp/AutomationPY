from cryptography.fernet import Fernet

# Cargar la clave desde el archivo
with open("../JenkinsReport/secret.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Tu clave secreta
secret_key_user = "jppg".encode()
secret_key_pass = "11e67565bc99312d54d08ab262ab229280".encode()

# Encriptar la clave
encrypted_key_user = cipher_suite.encrypt(secret_key_user)
encrypted_key_pass = cipher_suite.encrypt(secret_key_pass)

# Imprimir o guardar la clave encriptada para usarla más tarde
print(f"User encrypt: {encrypted_key_user.decode()} Pass encrypt: {encrypted_key_pass.decode()}")
