import jwt
from app import app

app.secret_key = "secret"

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
