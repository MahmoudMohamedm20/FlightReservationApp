import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f0f4f8")
        self.pack(fill='both', expand=True)

        container = tk.Frame(self, bg="#f0f4f8")
        container.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(container, text="Welcome to Flight Reservation System", font=("Segoe UI", 20, "bold"), bg="#f0f4f8", fg="#2d3e50")
        title.pack(pady=(0, 30))

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 12), padding=10)

        book_btn = ttk.Button(container, text="Book Flight", width=20, command=self.go_to_booking)
        book_btn.pack(pady=10)
        view_btn = ttk.Button(container, text="View Reservations", width=20, command=self.go_to_reservations)
        view_btn.pack(pady=10)

    def go_to_booking(self):
        from booking import BookingPage
        self.pack_forget()
        BookingPage(self.master)

    def go_to_reservations(self):
        from reservations import ReservationsPage
        self.pack_forget()
        ReservationsPage(self.master)