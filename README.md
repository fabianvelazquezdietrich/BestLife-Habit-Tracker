# BestLife-Habit-Tracker
A Python CLI application to track habits

## Overview
Hey there! We created the BestLife to help you explore, create, manage, and analyze your habits. It's a command-line application, so it's a bit different from other habit trackers out there. But we think you'll love it! This handy little app helps you keep track of your daily and weekly habits, so you can monitor your progress, build streaks, and reflect on how consistent you've been.

---

## Features

- **Addition of Habits:** We've made it really easy for you to create new habits with weekly or daily periodicity.
- Loading your favorites: Our users can mark a habit as completed for the current day or week, depending on what they want.
- **Delete Habits:** Our customers can easily remove their habits from the tracker if they need to.
- Display Habits: Here's where you can see all the habits you're tracking right now.
- Analyze Habits:
- View habits or goals by periodicity (weekly or daily) to get a better idea of what's going on!
  Our customers can search here for the longest streak of all their habits to see how they're doing!
  We're happy to say that with our application, you can easily find the longest streak for a specific habit in this section of the menu!
- **Data Persistence:** We've made sure that everything you do in our application is saved and loaded automatically using a JSON file, so you don't have to worry about a thing!

---

## Installation instructions

### Prerequisites to execute BestLife
- **Python**: We just ask that users have version 3.7 or later.
1. You'll also need a terminal or command prompt to run the application on your device.
Here's how to install it:
2. Clone the repository or download the project files on your device.
3. Navigate to the project folder in your terminal:
bash
cd habit_tracker


## Usage

To get started, just run the application using:
```bash
python main.py
```

### Menu Options
Once the costumers started the application, they will see the main menu:

```
Habit Tracker Menu:
1. Add a new habit
2. Complete a habit
3. Display all habits
4. Save and Exit
5. Delete a habit
6. Analysis Menu
```

#### Example Flows

1. **Add a New Habit**:  
   - If the costumers are ready to add a new habit, just select option `1` from the menu.
   - Then they have to enter the habit name (e.g., "Morning Run").
   - And to finish they need to specify the periodicity (`daily` or `weekly`)of the selected habit.

2. **Complete a Habit**:  
   - To mark as finished or completed a habit just select option `2` from the menu.
   - The they need to choose the habit to mark as completed by its corresponding number.

3. **Delete a Habit**:
   - Select option `5` from the menu.
   - Choose the habit to delete by its corresponding number.

4. **Analysis Menu**:
   - The users must select option `6` if they want to analyze their habits.
   - Then they will have to choose from the sub-options to view habits by periodicity, the longest streak, or the longest streak for a specific habit.

---

## File Structure

```
habit_tracker/
|-- habit.py               # This file contains the Habit class definition.
|-- habit_tracker.py       # You'll find the HabitTracker class and related methods here.
|-- utils.py               # This file is full of handy utility functions for data persistence and menu operations.
|-- main.py                # It's time to dive into the heart of BestLife, this file serves as our entry point to the application.
|-- habits.json            # JSON file for saving and loading all the habit data that the application generates.
|-- README.md              # This is a handy little documentation file.
```

---

## Data Persistence
Habits are stored in a JSON file named `habits.json`. Each habit is saved with the following attributes:

```json
{
    "task": "Morning reading",
    "periodicity": "daily",
    "creation_date": "2024-12-13T17:24:59.395286",
    "completion_dates": ["2024-12-14T09:54:54.782729"],
    "streak": 1
}
```

### Notes:
- The JSON file is updated automatically when habits are added, completed, or deleted.
- If the file does not exist, it will be created when the program runs.

---

## Reflection
It illustrates the use of Python OOP and functional programming paradigms. Implementation of features like data persistence and interaction with the user using a CLI menu demonstrates the practical aspects of programming in great depth.

---

## Future Enhancements
- **SQLite Database Integration**: Remove the JSON file and add a relational database; this will help in scaling.
- **Enhanced Analytics**: Such features as streak history and habit performance trends.
- **User Authentication**: Allow different users to track their habits.
- **GUI Development**: Build a graphical interface using frameworks such as Tkinter or PyQt.

---

## License
The code in these notebooks is licensed under the MIT License. See the LICENSE file for details.
