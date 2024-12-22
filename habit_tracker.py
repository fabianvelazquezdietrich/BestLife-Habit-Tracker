import json
from datetime import datetime
from habit import Habit  # Import Habit from habit.py

class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def remove_habit(self, habit_name):
        self.habits = [habit for habit in self.habits if habit.task != habit_name]

    def get_all_habits(self):
        return self.habits

    def get_habits_by_periodicity(self, periodicity):
        return [h for h in self.habits if h.periodicity == periodicity]

    def get_longest_streak(self):
        return max(h.get_streak() for h in self.habits) if self.habits else 0

    def get_longest_streak_for_habit(self, task):
        for h in self.habits:
            if h.task == task:
                return h.get_streak()
        raise ValueError(f"Habit '{task}' does not exist.")

def save_habits(tracker, filename="habits.json"):
    """Saves the habits to a JSON file."""
    data = []
    for habit in tracker.get_all_habits():
        data.append({
            "task": habit.task,
            "periodicity": habit.periodicity,
            "creation_date": habit.creation_date.isoformat(),
            "completion_dates": [date.isoformat() for date in habit.completion_dates],
            "streak": habit.streak  # Safe the streak
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"DEBUG: Habits saved to {filename}. Total habits: {len(data)}")

def load_habits(tracker, filename="habits.json"):
    """Loads habits from a JSON file.

    Args:
        tracker (HabitTracker): The HabitTracker instance to load the habits into.
        filename (str): The name of the file to load the data from.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)

            for item in data:
                habit = Habit(
                    task=item["task"],
                    periodicity=item["periodicity"],
                    creation_date=datetime.fromisoformat(item["creation_date"])
                )
                habit.completion_dates = [
                    datetime.fromisoformat(date) for date in item["completion_dates"]
                ]
                tracker.add_habit(habit)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty tracker
        print(f"No data file found ({filename}). Starting with an empty tracker.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while loading habits: {e}")

