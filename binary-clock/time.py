from datetime import datetime

def get_current_time_12_hour():
    # Get the current time
    now = datetime.now()
    
    # Extract hours, minutes, and seconds
    hour = now.hour
    minute = now.minute
    second = now.second
    
    # Convert to 12-hour format
    am_pm = 'AM' if hour < 12 else 'PM'
    hour_12 = hour % 12
    hour_12 = 12 if hour_12 == 0 else hour_12  # Handle midnight case

    return hour_12, minute, second, am_pm

def main():
    hour, minute, second, am_pm = get_current_time_12_hour()
    print(f"Current Time: {hour:02}:{minute:02}:{second:02} {am_pm}")
    print((hour))

if __name__ == "__main__":
    main()