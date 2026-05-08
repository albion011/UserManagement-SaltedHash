import tkinter as tk
from tkinter import messagebox
from database import get_connection
from security import generate_salt, hash_password
from dashboard import open_dashboard
from database import init_db
init_db()

def register_user():
    
    conn.close()