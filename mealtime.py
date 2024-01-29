from datetime import datetime

def get_meal_time(time_str):
    # Try parsing as 24-hour format first, then 12-hour format
    try:
        time_obj = datetime.strptime(time_str, '%H:%M')
    except ValueError:
        time_obj = datetime.strptime(time_str, '%I:%M %p')

    # Convert to 24-hour time for comparison
    hour = time_obj.hour

    # Determine meal time
    if 6 <= hour < 10:
        return "Breakfast"
    elif 12 <= hour < 14:
        return "Lunch"
    elif 18 <= hour < 21:
        return "Dinner"
    else:
        return "It's not a meal time"

# Example usage
user_input = input("Enter the time (HH:MM or HH:MM AM/PM): ")
meal = get_meal_time(user_input)
print(meal)