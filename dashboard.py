import tkinter as tk
from database import get_connection

def open_dashboard():
    app = tk.Tk()
    app.title("Dashboard")
    app.geometry("400x300")

    listbox = tk.Listbox(app, width=50, height=15)
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users")

    for user in cursor.fetchall():
        listbox.insert(tk.END, user[0])

    conn.close()

    app.mainloop()