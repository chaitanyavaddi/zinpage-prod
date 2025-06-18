
import base64



def encode_password(str_password: str):
    pass_bytes = str_password.encode("ascii")
    encoded_bytes = base64.b64encode(pass_bytes)
    encrypted_password = encoded_bytes.decode("ascii")
    return encrypted_password