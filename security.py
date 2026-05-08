import hashlib
import os
import base64

def generate_salt():
    return base64.b64encode(os.urandom(16)).decode('utf-8')

def hash_password(password, salt):
    combined = password + salt
    return hashlib.sha256(combined.encode()).hexdigest()
