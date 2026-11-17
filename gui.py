import tkinter as tk
from tkinter import messagebox, ttk
import storage
import analytics


class ModernExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Expense Tracker")
        self.root.geometry("680x620")
        self.root.resizable(True, True)
        self.root.state("zoomed")

        # Color Palette
        self.BG_MAIN = "#F1F5F9"
        self.BG_CARD = "#FFFFFF"
        self.PRIMARY = "#4F46E5"
        self.PRIMARY_HOVER = "#4338CA"
        self.SUCCESS = "#10B981"
        self.DANGER = "#EF4444"
        self.DANGER_HOVER = "#DC2626"
        self.TEXT_DARK = "#0F172A"
        self.TEXT_MUTED = "#64748B"
        self.BORDER = "#CBD5E1"

        self.root.configure(bg=self.BG_MAIN)
        self.expenses = storage.load_expenses()
        self.monthly_limit = 5000.0

        self.setup_styles()
        self.build_ui()
        self.refresh_all()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Modern.Treeview",
            background=self.BG_CARD,
            foreground=self.TEXT_DARK,
            fieldbackground=self.BG_CARD,
            rowheight=32,
            font=("Segoe UI", 10),
            borderwidth=0,
        )
        style.configure(
            "Modern.Treeview.Heading",
            background="#E2E8F0",
            foreground=self.TEXT_DARK,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padding=6,
        )
        style.map(
            "Modern.Treeview",
            background=[("selected", "#E0E7FF")],
            foreground=[("selected", self.PRIMARY)],
        )

    def build_ui(self):
        # Top Header Bar
        header = tk.Frame(self.root, bg=self.PRIMARY, height=64)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(
            header,
            text="Student Expense Tracker",
            font=("Segoe UI", 16, "bold"),
            bg=self.PRIMARY,
            fg="white",
        ).pack(side=tk.LEFT, padx=24)

        tk.Label(
            header,
            text="Personal Budget & Analytics",
            font=("Segoe UI", 10),
            bg=self.PRIMARY,
            fg="#C7D2FE",
        ).pack(side=tk.RIGHT, padx=24)

        # Main Container
        container = tk.Frame(self.root, bg=self.BG_MAIN, padx=24, pady=18)
        container.pack(fill=tk.BOTH, expand=True)

        # Summary Metric Cards
        cards_frame = tk.Frame(container, bg=self.BG_MAIN)
        cards_frame.pack(fill=tk.X, pady=(0, 16))

        self.total_val_lbl = self.create_metric_card(
            cards_frame, "TOTAL SPENT", "Rs. 0.00", self.PRIMARY, 0
        )
        self.limit_val_lbl = self.create_metric_card(
            cards_frame, "MONTHLY LIMIT", f"Rs. {self.monthly_limit:,.2f}", self.TEXT_DARK, 1
        )
        self.rem_val_lbl = self.create_metric_card(
            cards_frame, "REMAINING", f"Rs. {self.monthly_limit:,.2f}", self.SUCCESS, 2
        )

        # Add Expense Input Card
        input_card = tk.Frame(
            container,
            bg=self.BG_CARD,
            highlightbackground=self.BORDER,
            highlightthickness=1,
            padx=16,
            pady=14,
        )
        input_card.pack(fill=tk.X, pady=(0, 16))

        tk.Label(
            input_card,
            text="Amount (Rs.)",
            font=("Segoe UI", 9, "bold"),
            bg=self.BG_CARD,
            fg=self.TEXT_MUTED,
        ).grid(row=0, column=0, sticky="w")

        self.amount_entry = tk.Entry(
            input_card,
            width=16,
            font=("Segoe UI", 11),
            bg="#F8FAFC",
            fg=self.TEXT_DARK,
            relief="flat",
            highlightbackground=self.BORDER,
            highlightthickness=1,
        )
        self.amount_entry.grid(row=1, column=0, padx=(0, 14), ipady=5)
        self.amount_entry.bind("<Return>", lambda event: self.add_expense())

        tk.Label(
            input_card,
            text="Category",
            font=("Segoe UI", 9, "bold"),
            bg=self.BG_CARD,
            fg=self.TEXT_MUTED,
        ).grid(row=0, column=1, sticky="w")

        self.category_var = tk.StringVar(value="Food")
        self.category_box = ttk.Combobox(
            input_card,
            textvariable=self.category_var,
            values=["Food", "Books", "Travel", "Stationery", "Entertainment", "Other"],
            width=16,
            state="readonly",
            font=("Segoe UI", 10),
        )
        self.category_box.grid(row=1, column=1, padx=(0, 14), ipady=4)

        add_btn = tk.Button(
            input_card,
            text="+ Add Expense",
            command=self.add_expense,
            bg=self.PRIMARY,
            fg="white",
            activebackground=self.PRIMARY_HOVER,
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=16,
            pady=6,
        )
        add_btn.grid(row=1, column=2, sticky="e")

        # Filter & Action Toolbar
        toolbar = tk.Frame(container, bg=self.BG_MAIN)
        toolbar.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            toolbar,
            text="Expense History",
            font=("Segoe UI", 12, "bold"),
            bg=self.BG_MAIN,
            fg=self.TEXT_DARK,
        ).pack(side=tk.LEFT)

        del_btn = tk.Button(
            toolbar,
            text="Delete Selected",
            command=self.delete_selected,
            bg=self.DANGER,
            fg="white",
            activebackground=self.DANGER_HOVER,
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=4,
        )
        del_btn.pack(side=tk.RIGHT, padx=(6, 0))

        filter_btn = tk.Button(
            toolbar,
            text="Filter Category",
            command=self.filter_category,
            bg="#E0E7FF",
            fg=self.PRIMARY,
            activebackground="#C7D2FE",
            activeforeground=self.PRIMARY,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=4,
        )
        filter_btn.pack(side=tk.RIGHT, padx=6)

        all_btn = tk.Button(
            toolbar,
            text="Show All",
            command=self.refresh_all,
            bg=self.BG_CARD,
            fg=self.TEXT_DARK,
            activebackground="#E2E8F0",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=4,
            highlightbackground=self.BORDER,
            highlightthickness=1,
        )
        all_btn.pack(side=tk.RIGHT, padx=6)

        # Expense Table Card
        table_card = tk.Frame(
            container,
            bg=self.BG_CARD,
            highlightbackground=self.BORDER,
            highlightthickness=1,
        )
        table_card.pack(fill=tk.BOTH, expand=True, pady=(0, 14))

        self.tree = ttk.Treeview(
            table_card,
            columns=("ID", "Category", "Amount"),
            show="headings",
            style="Modern.Treeview",
            height=7,
        )
        self.tree.heading("ID", text="#")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount (Rs.)")
        self.tree.column("ID", width=70, anchor="center")
        self.tree.column("Category", width=310, anchor="w")
        self.tree.column("Amount", width=210, anchor="e")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.tag_configure("oddrow", background="#F8FAFC")
        self.tree.tag_configure("evenrow", background="#FFFFFF")

        # Status Alert Banner
        self.alert_frame = tk.Frame(
            container,
            bg="#ECFDF5",
            highlightbackground="#A7F3D0",
            highlightthickness=1,
            pady=10,
            padx=14,
        )
        self.alert_frame.pack(fill=tk.X)

        self.status_label = tk.Label(
            self.alert_frame,
            text="",
            font=("Segoe UI", 10, "bold"),
            bg="#ECFDF5",
            fg="#065F46",
        )
        self.status_label.pack()

    def create_metric_card(self, parent, title, initial_val, accent_color, col_idx):
        card = tk.Frame(
            parent,
            bg=self.BG_CARD,
            highlightbackground=self.BORDER,
            highlightthickness=1,
            padx=14,
            pady=10,
        )
        pad_right = 10 if col_idx < 2 else 0
        card.grid(row=0, column=col_idx, sticky="ew", padx=(0, pad_right))
        parent.grid_columnconfigure(col_idx, weight=1)

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 8, "bold"),
            bg=self.BG_CARD,
            fg=self.TEXT_MUTED,
        ).pack(anchor="w")

        val_lbl = tk.Label(
            card,
            text=initial_val,
            font=("Segoe UI", 14, "bold"),
            bg=self.BG_CARD,
            fg=accent_color,
        )
        val_lbl.pack(anchor="w", pady=(2, 0))
        return val_lbl

    def add_expense(self):
        raw_amount = self.amount_entry.get().strip()
        try:
            amount = float(raw_amount)
            if amount <= 0:
                raise ValueError
            category = self.category_var.get()
            self.expenses.append({"amount": amount, "category": category})
            storage.save_expenses(self.expenses)
            self.amount_entry.delete(0, tk.END)
            self.refresh_all()
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid positive number.")


    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Click an expense row in the table first.")
            return
        row_values = self.tree.item(selected[0])["values"]
        index = int(row_values[0])
        if storage.delete_expense(self.expenses, index):
            self.refresh_all()

    def filter_category(self):
        cat = self.category_var.get()
        filtered = analytics.filter_by_category(self.expenses, cat)
        self.populate_table(filtered)

    def refresh_all(self):
        self.populate_table(self.expenses)
        self.update_dashboard()

    def populate_table(self, data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for idx, exp in enumerate(data):
            tag = "evenrow" if idx % 2 == 0 else "oddrow"
            self.tree.insert(
                "",
                tk.END,
                values=(idx, f"  {exp['category']}", f"Rs. {float(exp['amount']):,.2f}  "),
                tags=(tag,),
            )

    def update_dashboard(self):
        total = analytics.calculate_total(self.expenses)
        remaining = self.monthly_limit - total

        self.total_val_lbl.config(text=f"Rs. {total:,.2f}")
        self.rem_val_lbl.config(
            text=f"Rs. {remaining:,.2f}",
            fg=self.DANGER if remaining < 0 else self.SUCCESS,
        )

        if total > self.monthly_limit:
            self.alert_frame.config(bg="#FEF2F2", highlightbackground="#FECACA")
            self.status_label.config(
                text=f"WARNING: Budget Exceeded! You spent Rs. {total:,.2f} (Over limit by Rs. {abs(remaining):,.2f})",
                bg="#FEF2F2",
                fg="#991B1B",
            )
        else:
            self.alert_frame.config(bg="#ECFDF5", highlightbackground="#A7F3D0")
            self.status_label.config(
                text=f"Budget On Track - Rs. {remaining:,.2f} remaining out of Rs. {self.monthly_limit:,.2f}",
                bg="#ECFDF5",
                fg="#065F46",
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernExpenseTracker(root)
    root.mainloop()
