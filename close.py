import os
import subprocess
import psutil
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def close_predefined_application(app_name):
    """Close a predefined application based on known process names."""
    app_name = app_name.lower()
    app_paths = {
        'calculator': 'calc.exe',
        'paint': 'mspaint.exe',
        'notepad': 'notepad.exe',
        'discord': 'Discord.exe',
        'spotify': 'Spotify.exe',  # Both UWP and traditional
        'telegram': 'Telegram.exe',  # Both UWP and traditional
        'steam': 'steam.exe',
        'media player': 'vlc.exe',
        'wordpad': 'WINWORD.EXE',
        'powerpoint': 'POWERPNT.EXE',
        'excel': 'EXCEL.EXE',
        'edge': 'msedge.exe'
    }

    for key, process_name in app_paths.items():
        if key in app_name:
            try:
                subprocess.run(f"taskkill /IM {process_name} /F", shell=True, check=True)
                speak(f"Closed {key}.")
                return True
            except subprocess.CalledProcessError as e:
                print(f"Error closing {key}: {e}")
                speak(f"Failed to close {key}.")
                return False

    return False

def close_uwp_app(app_name):
    """Close a UWP (Microsoft Store) app."""
    try:
        # Enhanced PowerShell to locate and terminate UWP processes
        command = (
            f'powershell "Get-Process | '
            f'Where-Object {{$_.Name -like \'*{app_name}*\' -or $_.MainWindowTitle -like \'*{app_name}*\'}} | '
            f'Stop-Process -Force"'
        )
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            speak(f"Closed {app_name}.")
            return True
        else:
            print(f"PowerShell error: {result.stderr}")
    except Exception as e:
        print(f"Error closing UWP app {app_name}: {e}")

    return False

def close_traditional_app(app_name):
    """Close traditional apps by matching running processes."""
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if app_name in proc.info['name'].lower():
                os.kill(proc.info['pid'], 9)  # Kill the process
                speak(f"Closed {app_name}.")
                return True
    except Exception as e:
        print(f"Error closing {app_name}: {e}")

    return False

def close_application(app_name):
    """Close an application, checking predefined, UWP, and traditional apps."""
    if close_predefined_application(app_name):
        return

    if close_uwp_app(app_name):
        return

    if close_traditional_app(app_name):
        return

    speak(f"Unable to find or close {app_name}.")

# Example usage

