import subprocess
import pkg_resources

required = [
    'pyttsx3',
    'SpeechRecognition',
    'pywhatkit',
    'wikipedia',
    'pyjokes',
    'requests',
    'beautifulsoup4',
    'nltk',
    'opencv-python',
    'pyaudio',
    'PyPDF2',
    'pytube',
    'pyautogui',
    'psutil',
    'instaloader',
    'speedtest-cli',
    'PyQt5',
    'pillow',
    'numpy',
    'fuzzywuzzy',
    'openai',
    'folium',
    'phonenumbers',
    'opencage',
    'pygetwindow',
    'pywin32',
    'keyboard'
]

installed = {pkg.key for pkg in pkg_resources.working_set}
missing = [pkg for pkg in required if pkg.lower() not in installed]

if missing:
    print(f"Installing missing libraries: {missing}")
    subprocess.check_call(["pip", "install", *missing])
else:
    print("✅ All required libraries are already installed.")
