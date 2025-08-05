# calendar_ui.py

import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime
from reminder_manager import ReminderManager

class CalendarApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calendar and Reminder App")
        self.reminder_mgr = ReminderManager()

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        self.create_widgets()
        self.show_calendar()

    def create_widgets(self):
        self.month_year_label = tk.Label(self.root, font=("Arial", 16))
        self.month_year_label.pack(pady=10)

        self.calendar_text = tk.Text(self.root, width=20, height=8, font=("Courier", 12))
        self.calendar_text.pack()

        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack(pady=5)
        self.date_entry.insert(0, "DD-MM-YYYY")

        self.reminder_entry = tk.Entry(self.root, width=40)
        self.reminder_entry.pack(pady=5)
        self.reminder_entry.insert(0, "Reminder text")

        tk.Button(self.root, text="Add Reminder", command=self.add_reminder).pack(pady=2)
        tk.Button(self.root, text="View Reminder", command=self.view_reminder).pack(pady=2)

    def show_calendar(self):
        cal = calendar.month(self.current_year, self.current_month)
        self.month_year_label.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")
        self.calendar_text.delete("1.0", tk.END)
        self.calendar_text.insert(tk.END, cal)

    def add_reminder(self):
        date = self.date_entry.get()
        reminder = self.reminder_entry.get()
        success = self.reminder_mgr.add_reminder(date, reminder)
        if success:
            messagebox.showinfo("Success", "Reminder added!")
        else:
            messagebox.showerror("Error", "Invalid date format. Use DD-MM-YYYY.")

    def view_reminder(self):
        date = self.date_entry.get()
        reminders = self.reminder_mgr.get_reminders(date)
        if reminders:
            messagebox.showinfo("Reminders", "\n".join(reminders))
        else:
            messagebox.showinfo("Reminders", "No reminders found.")

    def run(self):
        self.root.mainloop()
