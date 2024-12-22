from datetime import datetime

class Habit:
    def __init__(self, task, periodicity, creation_date=None, completion_dates=None):
        self.task = task
        self.periodicity = periodicity
        self.creation_date = creation_date or datetime.now()
        self.completion_dates = completion_dates or []
        self.streak = self.calculate_streak()  # calculate the initial streak if there are completion dates

    def complete_task(self, date):
        """Marks the habit as completed and updates the streak."""
        if self.completion_dates:
            last_completion = self.completion_dates[-1]
            # Check if the task was completed in the correct period
            if self.is_within_period(last_completion, date):
                self.streak += 1
            else:
                self.streak = 1  # Restart streak if not completed on time
        else:
            self.streak = 1  # First time the habit is complete
        self.completion_dates.append(date)

    def is_within_period(self, last_date, current_date):
        """Checks if the habit is completed within its defined periodicity."""
        if self.periodicity == "daily":
            return (current_date - last_date).days <= 1
        elif self.periodicity == "weekly":
            return (current_date - last_date).days <= 7
        return False

    def calculate_streak(self):
        """Calculates the current streak based on completion dates."""
        if not self.completion_dates:
            return 0

        streak = 1
        for i in range(len(self.completion_dates) - 1, 0, -1):
            if self.is_within_period(self.completion_dates[i - 1], self.completion_dates[i]):
                streak += 1
            else:
                break
        return streak

    def __repr__(self):
        return f"Habit(task={self.task}, periodicity={self.periodicity}, streak={self.streak})"

