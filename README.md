# UserManagement-SaltedHash
Windows application for user management with passwords stored as SaltedHash in MySQL database. Uses SHA-256 hashing with random salt. Built with Python & Tkinter.

## Description
This university project implements a user management system with secure password storage using SaltedHash. Passwords are never stored as plaintext — only SHA-256 hash and random salt are saved in the database.

## How It Works
- **Register:** Generates random salt → SHA256(password + salt) → saves to DB
- **Login:** Fetches salt from DB → SHA256(password + salt) → compares with stored hash
- **Dashboard:** Shows all registered users after successful login

## Security
- **Salt:** 16 random bytes encoded in Base64 — unique for every user
- **Hash:** SHA-256(password + salt) — irreversible
- Without salt: SHA256("password") is always the same → vulnerable
- With salt: SHA256("password" + "xK9#...") is unique per user → secure

## Project Structure
- `login.py` – Main UI (Register + Login)
- `dashboard.py` – Dashboard with user list
- `database.py` – MySQL connection and table creation
- `security.py` – Salt generation and password hashing

## Team Members
- **Alba Jashanica** – Register UI (login.py) + Security (security.py)
- **Albina Haliti** – Database (database.py)
- **Albion Hoxha** – Login UI (login.py)
- **Fatbardha Gashi** – Dashboard (dashboard.py)

## Requirements
- Python 3.x
- MySQL / MariaDB
- mysql-connector-python

## Installation
pip install mysql-connector-python

## Running the Project
python login.py