import datetime
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# File paths
ACTIVITY_LOG_FILE = "activity_log.txt"
REMINDERS_FILE = "reminders.txt"

# 1. Log Past Activities and Commands
def log_activity(command):
    """Logs every voice command with a timestamp."""
    with open(ACTIVITY_LOG_FILE, 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()}: {command}\n")

# 2. Retrieve Past Activities
def read_past_activities(count=5):
    """Reads out the last few recorded activities."""
    try:
        with open(ACTIVITY_LOG_FILE, 'r') as log_file:
            activities = log_file.readlines()
        if activities:
            speak("Here are your recent activities:")
            for activity in activities[-count:]:
                speak(activity.strip())
        else:
            speak("You have no recorded activities.")
    except FileNotFoundError:
        speak("No activities have been recorded yet.")

# 3. Remember Reminders
def remember_reminder(reminder):
    """Saves a reminder to the file."""
    with open(REMINDERS_FILE, 'a') as reminder_file:
        reminder_file.write(f"{reminder}\n")
    speak("Reminder saved.")

def list_reminders():
    """Lists all saved reminders."""
    try:
        with open(REMINDERS_FILE, 'r') as reminder_file:
            reminders = reminder_file.readlines()
        if reminders:
            speak("Here are your reminders:")
            for reminder in reminders:
                speak(reminder.strip())
        else:
            speak("You have no reminders.")
    except FileNotFoundError:
        speak("You have no reminders.")

def delete_reminders():
    """Deletes all saved reminders."""
    open(REMINDERS_FILE, 'w').close()
    speak("All reminders have been deleted.")
