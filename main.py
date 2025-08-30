import tkinter as tk
from database import init_db
from home import HomePage

def main():
    init_db()
    root = tk.Tk()
    root.title("Flight Reservation System")
    root.geometry("600x400")
    app = HomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main()