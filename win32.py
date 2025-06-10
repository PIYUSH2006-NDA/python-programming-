import win32com.client

# Initialize speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Input number of students
no = ["piyush"]
for i in no:
    sentence = f"The shoutout give to  {i}"
    print(sentence)
    speaker.Speak(sentence)
k="nice everyone you have done the great job."
print(f"nice everyone you have done the great job.")
speaker.speak(k)
