import tkinter as tk
from tkinter import messagebox
from database import get_connection
from security import generate_salt, hash_password
from dashboard import open_dashboard
from database import init_db
init_db()

def register_user():
    username = entry_user.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showwarning("Warning", "Plotëso të gjitha fushat!")
        return

    salt = generate_salt()
    hashed = hash_password(password, salt)

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)", (username, hashed, salt))
        conn.commit()
        messagebox.showinfo("Success", "User u krijua!")
    except:
        messagebox.showerror("Error", "Username ekziston!")
    finally:
        conn.close()