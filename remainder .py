import win32com.client
import schedule
import time

# Initialize the text-to-speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def water_reminder():
    message = "Hey! It's time to drink water. Stay hydrated!"
    print(message)
    speaker.Speak(message)

# Schedule the reminder every 1 hour (you can change it)
schedule.every(1).minutes.do(water_reminder)

# Optional: Also remind immediately at start
water_reminder()

# Keep running the scheduler
while True:
    schedule.run_pending()
    time.sleep(5)
