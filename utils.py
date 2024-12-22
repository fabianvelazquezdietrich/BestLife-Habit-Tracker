from habit_tracker import HabitTracker
from habit import Habit
from datetime import datetime  #Import datetime to manage dates
from habit_tracker import save_habits
import json

def load_and_initialize_tracker(filename="habits.json"):
    """Loads habits from a file or initializes an empty tracker."""
    tracker = HabitTracker()
    load_habits(tracker, filename)
    return tracker

def load_habits(tracker, filename="habits.json"):
    """Loads habits from a JSON file into the tracker."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print("DEBUG: Loaded data from JSON:", data)
            for habit_data in data:
                habit = Habit(
                    task=habit_data["task"],
                    periodicity=habit_data["periodicity"],
                    creation_date=datetime.fromisoformat(habit_data["creation_date"]),
                    completion_dates=[datetime.fromisoformat(date) for date in habit_data["completion_dates"]]
                )
                habit.streak = habit_data.get("streak", 0)  # Assign streak (default, 0)
                tracker.add_habit(habit)
    except FileNotFoundError:
        print(f"DEBUG: File '{filename}' not found. Initializing empty tracker.")
    except json.JSONDecodeError as e:
        print(f"DEBUG: Error decoding JSON: {e}")

def display_habits(tracker):
    """Displays all the habits in the tracker."""
    if not tracker.habits:
        print("No habits found.")
    else:
        print("\nList of Habits:")
        for habit in tracker.get_all_habits():
            print(f"- {habit.task} ({habit.periodicity})")

def delete_habit(tracker):
    """Prompts the user to delete a habit."""
    if not tracker.habits:
        print("No habits to delete.")
        return

    print("\nAvailable Habits:")
    for idx, habit in enumerate(tracker.get_all_habits(), start=1):
        print(f"{idx}. {habit.task} ({habit.periodicity})")

    try:
        choice = int(input("Select a habit to delete (by number): "))
        if 1 <= choice <= len(tracker.habits):
            removed_habit = tracker.habits[choice - 1].task
            tracker.remove_habit(removed_habit)
            print(f"Habit '{removed_habit}' has been deleted.")

            # Save changes to file
            save_habits(tracker)
            print("Habits saved successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")
        
def complete_habit(tracker):
    """Prompts the user to complete a habit."""
    if not tracker.habits:
        print("No habits to complete.")
        return

    print("\nAvailable Habits:")
    for idx, habit in enumerate(tracker.get_all_habits(), start=1):
        print(f"{idx}. {habit.task} ({habit.periodicity})")

    try:
        choice = int(input("Select a habit to complete (by number): "))
        if 1 <= choice <= len(tracker.habits):
            habit = tracker.habits[choice - 1]
            habit.complete_task(datetime.now())
            print(f"Habit '{habit.task}' marked as completed!")
            save_habits(tracker)  # Save changes automatically
            print("Habits saved successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def get_habits_by_periodicity(tracker, periodicity):
    """Returns habits filtered by periodicity."""
    return [habit for habit in tracker.get_all_habits() if habit.periodicity == periodicity]

def get_longest_streak(tracker):
    """Returns the longest streak of all habits and the corresponding habit name."""
    if not tracker.habits:
        return None, 0  # There´s no available

    # Find the longest streak
    longest_streak_habit = max(tracker.get_all_habits(), key=lambda habit: habit.streak, default=None)

    if longest_streak_habit:
        return longest_streak_habit.task, longest_streak_habit.streak
    return None, 0

def get_longest_streak_for_habit(tracker, task):
    """Returns the longest streak for a specific habit."""
    for habit in tracker.get_all_habits():
        if habit.task == task:
            return habit.streak
    return 0  # If the habit is not found
