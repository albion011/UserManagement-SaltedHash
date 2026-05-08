import tkinter as tk

def open_dashboard():
    app = tk.Tk()
    app.title("Dashboard")
    app.geometry("400x300")

    listbox = tk.Listbox(app, width=50, height=15)
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    app.mainloop()