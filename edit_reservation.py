
import tkinter as tk
from tkinter import ttk
from database import update_reservation

class EditReservationPage(tk.Frame):
    def __init__(self, master, reservation):
        super().__init__(master, bg="#f0f4f8")
        self.pack(fill='both', expand=True)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=("Arial", 12), padding=10)
        style.configure("TLabel", font=("Arial", 10), background="#f0f4f8")

        container = tk.Frame(self, bg="#f0f4f8")
        container.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(container, text=f"✏️ Edit Reservation #{reservation[0]}", font=("Arial", 20, "bold"), bg="#f0f4f8", fg="#2d3e50")
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.res_id = reservation[0]
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}
        for idx, field in enumerate(fields):
            ttk.Label(container, text=field+":").grid(row=idx+1, column=0, sticky="e", padx=(0,10), pady=5)
            entry = ttk.Entry(container, width=25)
            entry.insert(0, reservation[idx+1])
            entry.grid(row=idx+1, column=1, pady=5, sticky="w")
            self.entries[field] = entry

        btn_frame = tk.Frame(container, bg="#f0f4f8")
        btn_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=(20,0))
        ttk.Button(btn_frame, text="💾 Update Reservation", width=18, command=self.update).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🗑️ Delete Reservation", width=18, command=self.delete_reservation).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="❌ Cancel", width=18, command=self.go_back).pack(side="left", padx=5)

        self.msg = tk.Label(container, text="", fg="green", bg="#f0f4f8", font=("Arial", 10))
        self.msg.grid(row=len(fields)+2, column=0, columnspan=2, pady=(10,0))

        # Instructions panel
        instr_frame = tk.LabelFrame(container, text="Instructions", font=("Arial", 9, "bold"), bg="#f0f4f8")
        instr_frame.grid(row=len(fields)+3, column=0, columnspan=2, pady=(20,0), sticky="ew")
        instr = (
            "- Edit any field and click 'Update Reservation'.\n"
            "- To delete, click 'Delete Reservation'.\n"
            "- Date: Use YYYY-MM-DD.\n"
            "- Seat Number: Use format like 12A."
        )
        tk.Label(instr_frame, text=instr, justify="left", bg="#f0f4f8", font=("Arial", 9)).pack(anchor="w", padx=10, pady=5)

    def update(self):
        data = [self.entries[field].get() for field in self.entries]
        if all(data):
            update_reservation(self.res_id, *data)
            self.msg.config(text="Updated!", fg="green")
        else:
            self.msg.config(text="Fill all fields!", fg="red")

    def delete_reservation(self):
        # This should be connected to a delete function if desired
        self.msg.config(text="Delete functionality not implemented.", fg="red")

    def go_back(self):
        from reservations import ReservationsPage
        self.pack_forget()
        ReservationsPage(self.master)

    def update(self):
        data = [self.entries[field].get() for field in self.entries]
        if all(data):
            update_reservation(self.res_id, *data)
            self.msg.config(text="Updated!", fg="green")
        else:
            self.msg.config(text="Fill all fields!", fg="red")

    def go_back(self):
        from reservations import ReservationsPage
        self.pack_forget()
        ReservationsPage(self.master)