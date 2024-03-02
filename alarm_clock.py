# Import necessary modules
from playsound import playsound
import time

# CLEAR = '\033[2J'
# CLEAR_AND_RETURN = '\033[H'
# print(CLEAR, CLEAR_AND_RETURN)

# Function to set an alarm for a specified duration


def alarm(sec):
    time_elapsed = 0

    # Loop until the specified time duration is reached
    while time_elapsed < sec:
        time.sleep(1)
        time_elapsed += 1
        time_left = sec - time_elapsed

        # Convert remaining time to hours, minutes, and seconds
        hours, mins = divmod(time_left, 3600)
        mins, secs = divmod(mins, 60)
        timer = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)

        # Display the countdown timer in the same line
        print(f'Alarm will sound in: {timer}', end='\r')

    # Play the alarm sound
    playsound('alarm.wav')


# Get user input for minutes and seconds
minutes = int(input('Enter the minutes: '))
seconds = int(input('Enter the seconds: '))
total_seconds = minutes * 60 + seconds

# Set the alarm for the specified duration
alarm(total_seconds)
