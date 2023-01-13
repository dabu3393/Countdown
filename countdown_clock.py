import datetime
import time

target_date_str = input("Enter the target date in the format of YYYY-MM-DD: ")
target_time_str = input("Enter the target time in the format of HH:MM:SS: ")

# Convert the input strings to datetime objects
target_date = datetime.datetime.strptime(target_date_str + ' ' + target_time_str, "%Y-%m-%d %H:%M:%S")

while True:
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Calculate the time remaining until the target date and time
    time_remaining = target_date - current_time

    # Print the time remaining in days, hours, minutes, and seconds
    print(time_remaining)

    if time_remaining.total_seconds() <= 0:
        print("Time's up!")
        break

    # Pause for 1 second before updating the countdown (Comment out for the Website)
    time.sleep(1)
