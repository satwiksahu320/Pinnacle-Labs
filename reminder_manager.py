# reminder_manager.py

from datetime import datetime

class ReminderManager:
    def __init__(self):
        self.reminders = {}

    def add_reminder(self, date_str, text):
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            return False

        if date_str not in self.reminders:
            self.reminders[date_str] = []
        self.reminders[date_str].append(text)
        return True

    def get_reminders(self, date_str):
        return self.reminders.get(date_str, [])
