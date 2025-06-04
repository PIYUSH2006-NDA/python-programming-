import time

hour = int(time.strftime('%H'))  # get current hour as integer

if 0 <= hour < 12:
    print("Good morning")
elif 12 <= hour < 17:
    print("Good afternoon")
else:
    print("Good night")
