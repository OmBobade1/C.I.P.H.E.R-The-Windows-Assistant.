import os
import speech_recognition as sr
import pyttsx3
import shutil

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text using text-to-speech engine."""
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    """Listen for a voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
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

def get_folder_path(location):
    """Return the absolute path of known locations or user-specified paths."""
    home = os.path.expanduser("~")  # Get user home directory

    known_paths = {
        "desktop": os.path.join(home, "Desktop"),
        "downloads": os.path.join(home, "Downloads"),
        "documents": os.path.join(home, "Documents"),
        "pictures": os.path.join(home, "Pictures"),
        "music": os.path.join(home, "Music"),
        "videos": os.path.join(home, "Videos"),
        "c drive": "C:\\",
        "d drive": "D:\\",
        "e drive": "E:\\",
        "f drive": "F:\\"
    }

    return known_paths.get(location, location)  # Return known path or assume it's a user-defined path

def create_file_or_folder(command):
    """Create a file or folder in the specified location."""
    words = command.split()
    if "folder" in words:
        item_type = "folder"
    elif "file" in words:
        item_type = "file"
    else:
        speak("Please specify whether to create a file or folder.")
        return

    # Extract file/folder name and location
    name = words[words.index(item_type) + 1] if item_type in words else None
    
    # Detect whether the user said "on Desktop" or "in [location]"
    if " on " in command:
        location_words = command.split(" on ")
    elif " in " in command:
        location_words = command.split(" in ")
    else:
        speak("Please specify the location for the file or folder.")
        return

    location = location_words[1].strip()
    target_path = get_folder_path(location)
    
    if not os.path.exists(target_path):
        speak("The specified location does not exist. Please check and try again.")
        return

    full_path = os.path.join(target_path, name)

    try:
        if item_type == "folder":
            os.makedirs(full_path, exist_ok=True)
        else:
            with open(full_path, "w") as f:
                f.write("")

        location_word = "on" if "desktop" in location.lower() else "in"
        speak(f"{item_type.capitalize()} '{name}' has been created {location_word} {location}.")
        print(f"{item_type.capitalize()} '{name}' created at {full_path}.")

    except Exception as e:
        speak(f"Error creating {item_type}: {e}")
        print(f"Error creating {item_type}: {e}")

def delete_file_or_folder(command):
    """Delete a specified file or folder from the given location."""
    words = command.split()
    if "folder" in words:
        item_type = "folder"
    elif "file" in words:
        item_type = "file"
    else:
        speak("Please specify whether to delete a file or folder.")
        return

    location_words = command.split(" from ")

    if len(location_words) > 1:
        location = location_words[1].strip()
    else:
        speak("Please specify the location of the file or folder.")
        return

    target_path = get_folder_path(location)
    
    if not os.path.exists(target_path):
        speak("The specified location does not exist. Please check and try again.")
        return

    name = words[words.index(item_type) + 1] if item_type in words else None
    full_path = os.path.join(target_path, name)

    try:
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)  # Delete folder and contents
        elif os.path.isfile(full_path):
            os.remove(full_path)  # Delete file
        else:
            speak(f"{item_type.capitalize()} '{name}' not found in {location}.")
            return

        speak(f"{item_type.capitalize()} '{name}' has been deleted from {location}.")
        print(f"{item_type.capitalize()} '{name}' deleted at {full_path}.")

    except Exception as e:
        speak(f"Error deleting {item_type}: {e}")
        print(f"Error deleting {item_type}: {e}")

# Main function to listen for commands
def main():
    speak("File and folder manager activated. Say 'create file', 'create folder', 'delete file from', or 'delete folder from' followed by location.")
    
    while True:
        command = listen_for_command()
        if command:
            if "create" in command:
                create_file_or_folder(command)
            elif "delete" in command:
                delete_file_or_folder(command)
            elif "exit" in command or "quit" in command:
                speak("Exiting file manager.")
                break
            else:
                speak("Unknown command. Please specify 'create' or 'delete' followed by 'file' or 'folder' and a location.")


