from datetime import datetime, timedelta
from habit import Habit

# Prueba 1: Crear un nuevo hábito
habit = Habit("Morning Reading", "daily")
print(habit)  # Debería mostrar: Habit(task=Morning Reading, periodicity=daily, streak=0)

# Prueba 2: Completar el hábito y verificar la racha
habit.complete_task(datetime.now())
print(habit)  # Debería mostrar: Habit(task=Morning Reading, periodicity=daily, streak=1)

# Completar nuevamente dentro del período
habit.complete_task(datetime.now() + timedelta(days=1))
print(habit)  # Debería mostrar: Habit(task=Morning Reading, periodicity=daily, streak=2)

# Prueba 3: Crear un hábito con fechas preexistentes
habit_with_dates = Habit(
    task="Yoga",
    periodicity="daily",
    completion_dates=[
        datetime(2024, 12, 12),
        datetime(2024, 12, 13),
        datetime(2024, 12, 14),
    ]
)
print(habit_with_dates)  # Debería mostrar: Habit(task=Yoga, periodicity=daily, streak=3)
