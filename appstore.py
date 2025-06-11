import os
import subprocess
import webbrowser
import shutil
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Speak the given text using text-to-speech engine."""
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    """Listen for a command from the user via the microphone and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Listen for audio input
    
    try:
        command = recognizer.recognize_google(audio).lower()  # Recognize the speech and convert to text
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that. Please try again.")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech service.")
        speak("Sorry, there was an issue with the speech service.")
        return None

def get_uwp_app_path(app_name):
    """Retrieve the UWP app path using PowerShell."""
    try:
        command = f'powershell "(Get-StartApps | Where-Object {{ $_.Name -like \'*{app_name}*\' }}).AppID"'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        return result.stdout.strip() or None
    except Exception as e:
        print(f"Error fetching UWP app path: {e}")
        return None

def open_uwp_app(app_name):
    """Attempt to open a UWP app using its AppID."""
    app_id = get_uwp_app_path(app_name)
    if app_id:
        try:
            app_command = f"explorer shell:AppsFolder\\{app_id}"
            subprocess.Popen(app_command, shell=True)
            speak(f"Opened {app_name}.")
        except Exception as e:
            print(f"Error launching {app_name}: {e}")
            speak(f"Failed to open {app_name}.")
    else:
        speak(f"{app_name} is not installed on your system.")
        open_microsoft_store(app_name)

def open_microsoft_store(app_name):
    """Search for the app in the Microsoft Store."""
    try:
        app_name = app_name.replace(" ", "+")
        subprocess.Popen(f"start ms-windows-store://search/?query={app_name}", shell=True)
        speak(f"Searching the Microsoft Store for {app_name}.")
    except Exception as e:
        print(f"Error opening Microsoft Store: {e}")
        speak("Could not open the Microsoft Store.")

def open_specific_application(app_name):
    """Open specific applications based on predefined paths."""
    app_paths = {
        'calculator': 'C:\\Windows\\System32\\calc.exe',
        'paint': 'C:\\Windows\\System32\\mspaint.exe',
        'notepad': 'C:\\Windows\\System32\\notepad.exe',
        'discord': '..\\..\\Discord.exe',
      
        'online classes': 'https://teams.microsoft.com/',
       
        'lt spice': "..\\..\\XVIIx64.exe",
        'steam': "..\\..\\steam.exe",
        'media player': "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
        'wordpad': "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
        'powerpoint': "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
        'excel': "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
        'wi-fi': 'ms-settings:network-wifi',
        'bluetooth': 'ms-settings:bluetooth',
        'flipkart': 'https://www.flipkart.com/',
        'amazon': 'https://www.amazon.in/',
         'gmail': 'https://mail.google.com/mail/',  # Gmail
    'maps': 'https://www.google.co.in/maps/',  # Google Maps
    'news': 'https://news.google.com/',  # Google News
    'calendar': 'https://calendar.google.com/calendar/',  # Google Calendar
    'photos': 'https://photos.google.com/',  # Google Photos
    'documents': 'https://docs.google.com/document/',  # Google Docs
    'spreadsheet': 'https://docs.google.com/spreadsheets',  # Google Sheets
    'drive': 'https://drive.google.com/drive/my-drive',  # Google Drive
    'hangouts': 'https://hangouts.google.com/',  # Google Hangouts
    'meet': 'https://meet.google.com/',  # Google Meet
    'slides': 'https://docs.google.com/presentation/',  # Google Slides
    'keep': 'https://keep.google.com/',  # Google Keep
    'google': 'https://www.google.com/',  # Google Search
    'github': 'https://github.com/',
    'gitlab' : 'https://gitlab.com/-/profile',
    'stackoverflow': 'https://stackoverflow.com/',
    
   ## 'linkedin': 'https://www.linkedin.com/',
    'zoom': 'https://zoom.us/',
    'skype': 'https://www.skype.com/',
    #'#whatsapp': 'https://web.whatsapp.com/',
    #'telegram': 'https://web.telegram.org/',
    'signal': 'https://signal.org/',
    'viber': 'https://www.viber.com/',
   # 'facebook': 'https://www.facebook.com/',
    'twitter': 'https://twitter.com/',
   
    
    # Shopping websites
    'flipkart': 'https://www.flipkart.com/',
    'amazon': 'https://www.amazon.in/',
    'meesho': 'https://www.meesho.com/',
    }
    
    app_name = app_name.lower()
    for key in app_paths:
        if key in app_name:
            # Before using the predefined path, check if it's a UWP app
            app_id = get_uwp_app_path(key)
            if app_id:  # If a UWP app is found, open it
                open_uwp_app(key)
                return True
            
            # Fall back to the predefined path (e.g., URL or executable)
            app_path = app_paths[key]
            if app_path.startswith('http') or app_path.startswith('ms-settings:'):
                # For URLs or Windows settings
                webbrowser.open(app_path)
            else:
                try:
                    os.startfile(app_path)
                except Exception as e:
                    print(f"Error opening {key}: {e}")
                    speak(f"Failed to open {key}.")
            speak(f"Opened {key}.")
            return True
    return False

def open_application(app_name):
    """Open an application."""
    if open_specific_application(app_name):
        return
    app_id = get_uwp_app_path(app_name)
    if app_id:
        open_uwp_app(app_name)
        return
    app_path = shutil.which(app_name)
    if app_path:
        subprocess.Popen(app_path)
        speak(f"Opened {app_name}.")
    else:
        speak(f"{app_name} is not installed.")
        open_microsoft_store(app_name)
