
import tkinter as tk
from tkinter import ttk
from database import create_reservation

class BookingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f0f4f8")
        self.pack(fill='both', expand=True)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=("Arial", 12), padding=10)
        style.configure("TLabel", font=("Arial", 10), background="#f0f4f8")

        container = tk.Frame(self, bg="#f0f4f8")
        container.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(container, text="✈️ Book New Flight", font=("Arial", 20, "bold"), bg="#f0f4f8", fg="#2d3e50")
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.entries = {}
        self.placeholders = {
            "Name": "e.g., John Doe",
            "Flight Number": "e.g., AA123",
            "Departure": "e.g., New York",
            "Destination": "e.g., London",
            "Date": "YYYY-MM-DD",
            "Seat Number": "e.g., 12A"
        }
        fields = list(self.placeholders.keys())
        for idx, field in enumerate(fields):
            ttk.Label(container, text=field+":").grid(row=idx+1, column=0, sticky="e", padx=(0,10), pady=5)
            entry = ttk.Entry(container, width=25, foreground="grey")
            entry.insert(0, self.placeholders[field])
            entry.bind("<FocusIn>", lambda e, f=field: self._clear_placeholder(e, f))
            entry.bind("<FocusOut>", lambda e, f=field: self._add_placeholder(e, f))
            entry.grid(row=idx+1, column=1, pady=5, sticky="w")
            self.entries[field] = entry

        btn_frame = tk.Frame(container, bg="#f0f4f8")
        btn_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=(20,0))
        ttk.Button(btn_frame, text="✅ Book Flight", width=18, command=self.submit).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🗑️ Clear Form", width=18, command=self.clear_form).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🏠 Back to Home", width=18, command=self.go_back).pack(side="left", padx=5)

        self.msg = tk.Label(container, text="", fg="green", bg="#f0f4f8", font=("Arial", 10))
        self.msg.grid(row=len(fields)+2, column=0, columnspan=2, pady=(10,0))

        # Instructions panel
        instr_frame = tk.LabelFrame(container, text="Instructions", font=("Arial", 9, "bold"), bg="#f0f4f8")
        instr_frame.grid(row=len(fields)+3, column=0, columnspan=2, pady=(20,0), sticky="ew")
        instr = (
            "- All fields are required.\n"
            "- Flight Number: Use format like AA123.\n"
            "- Date: Use YYYY-MM-DD.\n"
            "- Seat Number: Use format like 12A."
        )
        tk.Label(instr_frame, text=instr, justify="left", bg="#f0f4f8", font=("Arial", 9)).pack(anchor="w", padx=10, pady=5)

    def _clear_placeholder(self, event, field):
        entry = self.entries[field]
        if entry.get() == self.placeholders[field]:
            entry.delete(0, tk.END)
            entry.config(foreground="black")

    def _add_placeholder(self, event, field):
        entry = self.entries[field]
        if not entry.get():
            entry.insert(0, self.placeholders[field])
            entry.config(foreground="grey")

    def clear_form(self):
        for field, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, self.placeholders[field])
            entry.config(foreground="grey")




    def submit(self):
        data = [self.entries[field].get() for field in self.entries]
        if all(data):
            create_reservation(*data)
            self.msg.config(text="Reservation Added!", fg="green")
            for entry in self.entries.values():
                entry.delete(0, tk.END)
        else:
            self.msg.config(text="Fill all fields!", fg="red")

    def go_back(self):
        from home import HomePage
        self.pack_forget()
        HomePage(self.master)