
import tkinter as tk
from tkinter import ttk
from database import get_all_reservations, delete_reservation

class ReservationsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f0f4f8")
        self.pack(fill='both', expand=True)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=("Arial", 12), padding=10)
        style.configure("TLabel", font=("Arial", 10), background="#f0f4f8")

        container = tk.Frame(self, bg="#f0f4f8")
        container.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(container, text="📋 All Reservations", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#2d3e50")
        title.grid(row=0, column=0, columnspan=4, pady=(0, 10))

        # Search bar
        search_frame = tk.Frame(container, bg="#f0f4f8")
        search_frame.grid(row=1, column=0, columnspan=4, pady=(0, 10), sticky="ew")
        tk.Label(search_frame, text="🔍 Search:", font=("Arial", 10), bg="#f0f4f8").pack(side="left")
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.refresh_table).pack(side="left", padx=2)
        ttk.Button(search_frame, text="Clear", command=self.clear_search).pack(side="left", padx=2)

        # Table
        columns = ("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat")
        self.tree = ttk.Treeview(container, columns=columns, show="headings", height=8)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        self.tree.grid(row=2, column=0, columnspan=4, pady=5)

        # Scrollbars
        vsb = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        vsb.grid(row=2, column=4, sticky='ns')
        self.tree.configure(yscrollcommand=vsb.set)

        # Action buttons
        btn_frame = tk.Frame(container, bg="#f0f4f8")
        btn_frame.grid(row=3, column=0, columnspan=4, pady=(10,0))
        ttk.Button(btn_frame, text="✏️ Edit Selected", width=18, command=self.edit_selected).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🗑️ Delete Selected", width=18, command=self.delete_selected).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🔄 Refresh", width=18, command=self.refresh_table).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🏠 Back to Home", width=18, command=self.go_back).pack(side="left", padx=5)

        # Status bar
        self.status = tk.Label(container, text="", font=("Arial", 9), bg="#f0f4f8", anchor="w")
        self.status.grid(row=4, column=0, columnspan=4, sticky="ew", pady=(10,0))

        self.refresh_table()

    def refresh_table(self):
        search = self.search_var.get().lower() if hasattr(self, 'search_var') else ""
        for row in self.tree.get_children():
            self.tree.delete(row)
        reservations = get_all_reservations()
        filtered = [r for r in reservations if search in " ".join(map(str, r)).lower()]
        for row in filtered:
            self.tree.insert("", "end", values=row[:7])
        self.status.config(text=f"Showing {len(filtered)} of {len(reservations)} reservations.")

    def clear_search(self):
        self.search_var.set("")
        self.refresh_table()

    def edit_selected(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], 'values')
            from edit_reservation import EditReservationPage
            self.pack_forget()
            EditReservationPage(self.master, values)

    def delete_selected(self):
        selected = self.tree.selection()
        if selected:
            res_id = self.tree.item(selected[0], 'values')[0]
            delete_reservation(res_id)
            self.refresh_table()

    def go_back(self):
        from home import HomePage
        self.pack_forget()
        HomePage(self.master)