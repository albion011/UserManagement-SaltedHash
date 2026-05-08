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
        cursor.execute(
            "INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)",
            (username, hashed, salt),
        )
        conn.commit()
        messagebox.showinfo("Success", "User u krijua!")
    except:
        messagebox.showerror("Error", "Username ekziston!")
    finally:
        conn.close()


def login():
    username = entry_user.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showwarning("Warning", "Plotëso të gjitha fushat!")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash, salt FROM users WHERE username=%s", (username,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        db_hash, salt = result
        if hash_password(password, salt) == db_hash:
            app.destroy()
            open_dashboard()
        else:
            messagebox.showerror("Error", "Password gabim!")
    else:
        messagebox.showerror("Error", "User nuk ekziston!")

app = tk.Tk()
app.title("User Management")
app.geometry("350x250")

tk.Label(app, text="Username").pack()
entry_user = tk.Entry(app)
entry_user.pack()

tk.Label(app, text="Password").pack()
entry_pass = tk.Entry(app, show="*")
entry_pass.pack()

tk.Button(app, text="Register", command=register_user).pack(pady=5)
tk.Button(app, text="Login", command=login).pack(pady=5)

app.mainloop()