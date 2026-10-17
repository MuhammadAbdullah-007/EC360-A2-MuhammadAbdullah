import hashlib

def register_user(email, password):
    return {"email": email, "hash": hashlib.sha256(password.encode()).hexdigest()}
