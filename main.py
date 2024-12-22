from utils import (
    load_and_initialize_tracker,
    display_habits,
    delete_habit,
    complete_habit,
    get_habits_by_periodicity,
    get_longest_streak,
    get_longest_streak_for_habit,
)
from habit_tracker import save_habits
from habit import Habit
from datetime import datetime

def add_habit(tracker):
    """Prompts the user to add a new habit."""
    task = input("Enter the name of the habit: ").strip()
    periodicity = input("Enter the periodicity (daily/weekly): ").strip().lower()

    if periodicity not in ["daily", "weekly"]:
        print("Invalid periodicity. Please enter 'daily' or 'weekly'.")
        return

    new_habit = Habit(task, periodicity)
    tracker.add_habit(new_habit)
    print(f"New habit added: {new_habit.task} ({new_habit.periodicity})")

    # Save changes to file
    save_habits(tracker)
    print("Habits saved successfully.")

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
            tracker.habits[choice - 1].complete_task(datetime.now())
            print(f"Habit '{tracker.habits[choice - 1].task}' marked as completed!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

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

def analysis_menu(tracker):
    """Displays the analysis menu and handles user input for analysis options."""
    if not tracker.habits:
        print("No habits available for analysis. Please add some habits first.")
        return

    print("\nAnalysis Menu:")
    print("1. View habits by periodicity")
    print("2. View longest streak of all habits")
    print("3. View longest streak for a specific habit")
    
    sub_choice = input("Choose an option: ").strip()
    if sub_choice == "1":
        periodicity = input("Enter periodicity (daily/weekly): ").strip().lower()
        habits = get_habits_by_periodicity(tracker, periodicity)
        if habits:
            print(f"\nHabits with periodicity '{periodicity}':")
            for habit in habits:
                print(f"- {habit.task} ({habit.periodicity})")
        else:
            print(f"No habits found with periodicity '{periodicity}'.")
    elif sub_choice == "2":
        habit_name, streak = get_longest_streak(tracker)
        if habit_name:
            print(f"The longest streak is '{streak}' days, achieved by the habit: '{habit_name}'.")
        else:
            print("No habits available to analyze streaks.")
    elif sub_choice == "3":
        task = input("Enter the name of the habit: ").strip()
        longest_streak = get_longest_streak_for_habit(tracker, task)
        print(f"Longest streak for '{task}': {longest_streak}")
    else:
        print("Invalid choice. Returning to the main menu.")

def main_menu():
    """Displays the main menu and handles user input."""
    tracker = load_and_initialize_tracker()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add a new habit")
        print("2. Complete a habit")
        print("3. Display all habits")
        print("4. Save and Exit")
        print("5. Delete a habit")
        print("6. Analysis Menu")  

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_habit(tracker)
        elif choice == "2":
            complete_habit(tracker)
        elif choice == "3":
            display_habits(tracker)
        elif choice == "4":
            save_habits(tracker)
            print("Habits saved. Exiting...")
            break
        elif choice == "5":
            delete_habit(tracker)
        elif choice == "6":
            analysis_menu(tracker)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
