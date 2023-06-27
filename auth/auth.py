import jwt
from flask import current_app as app

def generate_token(payload):
    return jwt.encode(payload, app.secret_key, algorithm="HS256")

def decode_token(token):
    try:
        decoded = jwt.decode(token, app.secret_key, options={"verify_signature": False})
        return decoded
    except jwt.ExpiredSignatureError:
        # Manejar el error de token expirado
        return None
    except jwt.InvalidTokenError:
        # Manejar el error de token inválido
        return None
