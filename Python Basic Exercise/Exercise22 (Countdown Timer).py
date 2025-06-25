""" Create a simple countdown timer using a while loop. """
# Write a code to create a simple countdown timer of 5 seconds using a while loop.
# Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.

# 1. Import time module and use time.sleep() function inside a while loop.
# 2. You’ll need a variable to keep track of the remaining time (initially set to the total countdown duration).
#    The while loop should continue as long as this remaining time is greater than zero. Inside the loop, you’ll want to:
#     1. Display the current remaining time to the user.
#     2. Pause the program for one second using time module’s sleep() function to create the countdown effect.
#     3. Decrease the remaining time by one second. Once the loop finishes (when the remaining time reaches zero),
#        you can print a “Time’s up!” message.

import time
# simple code
total_sec = 5
while total_sec > 0:
    print("Time remaining: ", total_sec)
    time.sleep(1)
    total_sec -= 1
print("Time’s up!")

# Using Function :-

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time’s up!")

duration = 5
countdown_timer(duration)

