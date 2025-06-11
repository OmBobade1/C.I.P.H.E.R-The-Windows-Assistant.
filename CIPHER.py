#_____________________________________________________C.I.P.H.E.R________________________________________________________
#Python modules used for this programm
import sys
import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time
import subprocess
import os
import cv2
import random
from requests import get
import smtplib
import psutil
import instaloader
import pyautogui
import PyPDF2
#from screenings import Recordings
from PIL import ImageGrab
import pyaudio
import wave
import numpy as np 
from locationtracker import tracker
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from CipherUi import Ui_chipherUI
import memory_manager
from screenings import StartRecording
from territories import states
from pywikihow import search_wikihow
import speedtest
from pytube import YouTube
import qrcode
from PyQt5.QtWidgets import QApplication
#from app import search_and_open, speak
import re
from appstore import open_application
from close import close_application
from window_manager import maximize_window, minimise_window 
from file_manager import create_file_or_folder, delete_file_or_folder
from ppt_manager import start_ppt_manager
#from notepad import main
from PyQt5 import QtWidgets
import openai
#from file_utilities import universal_file_manager
import nltk
import inspect
import pyautogui
from nltk.tokenize import word_tokenize
from fuzzywuzzy import process
from PyQt5.QtGui import QMovie
nltk.download('punkt')


import os, sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller .exe"""
    if getattr(sys, 'frozen', False):  # running as .exe
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)










# Using SAPI5, Microsoft's Speech Application Programming Interface, 
# the Pyttsx3 engine will handle text-to-speech conversion in Python.
# We will utilize this setup for text-to-speech functionality.

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #index '0' for 'David'(male) voice index '1' for 'zira'(female) voice
#def wikipedia_to_notepad():
 #   # Paste the entire program logic inside this function.
  #  pass




#import json  # Already imported, but ensure it's there
#import requests  # Missing import

# Replace with your actual API key
#DEEPSEEK_API_KEY = ""
#def ask_ai(question):
 #   """Send a user query to the DeepSeek AI API and return the response."""
  #  if not DEEPSEEK_API_KEY:
   #     return "Error: API key is missing."
#
 #   url = "https://api.deepseek.com/v1/chat/completions"
  #  headers = {
   #     "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    #    "Content-Type": "application/json"
    #}
    #data = {
     #   "model": "deepseek-chat",
      #  "messages": [
       #     {"role": "system", "content": "You are an AI assistant integrated into a virtual assistant."},
        #    {"role": "user", "content": question}
        #],
        #"temperature": 0.7
    #}
#
 #   try:
  #      response = requests.post(url, headers=headers, json=data)
   #     response.raise_for_status()  # Raise an error for HTTP issues
    #    return response.json().get('choices', [{}])[0].get('message', {}).get('content', "No response received.")
    #except requests.exceptions.RequestException as e:
    #    return f"API request failed: {e}"

# Example usage
# print(ask_ai("What is AI?"))
import nltk

import nltk
nltk.download('punkt_tab')


import inspect  # 🔹 Ensure inspect is imported!

#  Function ko class ke bahar rakho
def get_all_functions(obj):
    """Extracts all functions from the given class object"""
    return {name: func for name, func in inspect.getmembers(obj, inspect.ismethod)}

#Main classs where all the functiona are present
class MainThread(QThread):
    
    #Talk 
    def talk(self, text):
        print(text)  # This will redirect to QTextBrowser via StreamRedirector
        engine.say(text)
        engine.runAndWait()


    def process_command(self, user_input):
     words = word_tokenize(user_input.lower())
     extracted_command = " ".join(words)

    #  Handle IP address
     if "ip" in extracted_command and "address" in extracted_command:
         self.my_ip_address()
         return

    #  Handle contact creation
     elif any(phrase in extracted_command for phrase in ["add new contact", "create new", "new contact", "register contact", "add contact"]):
         if hasattr(self, "AddContact"):
             self.AddContact()
        # elif hasattr(self, "registernewContact"):
         #    self.registernewContact()
         else:
             self.talk("Boss, I can't find the contact creation function.")
         return

    #  Show/display contacts
     elif "show all contacts" in extracted_command or "display all contacts" in extracted_command:
         if hasattr(self, "show"):
             self.show()
         elif hasattr(self, "Display"):
             self.Display()
         else:
             self.talk("Boss, I can't find the function to show contacts.")
         return

    #  Check internet speed
     elif "internet" in extracted_command and "speed" in extracted_command:
         self.InternetSpeed()
         return

    #  News
     elif "news" in extracted_command and len(extracted_command.split()) <= 5:
         self.news()
         return

    #  Arithmetic commands
     elif re.search(r'\b(add|plus|subtract|minus|multiply|times|divide)\b', extracted_command):
         self.perform_task(user_input)
         return

     
     #  Handle stop before play to avoid misfires
     elif any(op in extracted_command for op in ["stop playing", "stop music", "stop video", "pause", "stop"]):
         self.talk("Pausing.")
         pyautogui.press("playpause")
         return  # Stop further processing

     # Specific match first
     elif any(phrase in extracted_command for phrase in ["play a song", "play the song", "play song"]):
         self.yt(extracted_command)  # Opens YouTube
         return

# General media toggle (play/pause)
     elif extracted_command.strip() == "start playing":
         self.talk("Playing.")
         pyautogui.press("playpause")
         return
     
     elif any(phrase in extracted_command for phrase in ["search contact by number", "find contact number", "get contact by number", "lookup number"]):
      self.NameIntheContDataBase(user_input)
      return

     
     elif "send a message" in extracted_command:
      self.whatsapp(user_input)
      return



     

     

    #  Fallback to fuzzy match
     commands_dict = get_all_functions(self)
     best_match, score = process.extractOne(extracted_command, commands_dict.keys())

     if score > 65:
         print(f"Executing: {best_match}")
         func = commands_dict[best_match]
         if func.__code__.co_argcount == 1:
             func()
         elif func.__code__.co_argcount == 2:
             func(user_input)
         else:
             print(f"Cannot automatically call {best_match}, needs special handling.")
    # else:
     #    self.talk("Sorry, I didn't understand that command.")





    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Intro()
    
    #function that will take the commands  to convert voice into text
    def listen_Command(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:

                print('Listening....')
                listener.pause_threshold = 1
                voice = listener.listen(source,timeout=4,phrase_time_limit=7)
                print("Recognizing...")
                command1 = listener.recognize_google(voice,language='en-in')
                command1 = command1.lower()  
                if 'cipher' in command1: 
                    command1 = command1.replace('cipher','')
                
            return command1
        except:
            return 'None'
        
    #cipher commands controller 
    def run_cipher(self):
        self.wish()
        self.talk('Hello boss I am Cipher your assistant. please tell me how can I help you')
        while True:
            self.command = self.listen_Command()  # Har baar naya command le raha hai
            print(self.command)

        # 🛠 **Replace this with the smart processing function**
            self.process_command(self.command)  # Yeh automatically function detect karega


            # Handle "open" command
            if "open" in self.command:
                app_name = self.command.replace("open", "").strip()
                if app_name:
                    self.talk(f"Opening {app_name}")
                    open_application(app_name)  # Call your open_application function here
                else:
                    self.talk("Please specify the application name.")

             #Handle "close" command
            elif "close" in self.command:
                app_name = self.command.replace("close", "").strip()
                if app_name:
                    self.talk(f"Closing {app_name}")
                    close_application(app_name)  # Call your close_application function here
                else:
                    self.talk("Please specify the application name.")
                
            if "minimise" in self.command:
                    app_name = self.command.replace("minimise", "").strip()
                    self.talk(f"Minimizing {app_name}")
                    minimise_window(app_name)
                    

            elif "maximize" in self.command:
                    app_name = self.command.replace("maximize", "").strip()
                    self.talk(f"Maximizing {app_name}")
                    maximize_window(app_name)
            
            if "create file" in self.command or "create folder" in self.command:
                    self.talk("Creating requested file or folder.")
                    create_file_or_folder(self.command)

            elif "delete file" in self.command or "delete folder" in self.command:
                     self.talk("Deleting requested file or folder.")
                     delete_file_or_folder(self.command)
          #  elif "powerpoint mode" in self.command:
           ##          start_ppt_manager(self) # Pass cipher instance so PowerPoint commands don't interfere
         #   elif "ai" in self.command or "chatbot" in self.command or "ask" in self.command:
          #           self.talk("What would you like to ask the AI?")
           #          user_input = self.listen_Command()  # Get user input
    #
     #       if user_input not in [None, "None", ""]:  # Better input validation
      #                  ai_response = ask_ai(user_input)  # Call the DeepSeek AI function
       # 
        #    if ai_response:  # Ensure the response isn't empty or an error
         #             self.talk(ai_response)  # Speak out the response
          #  else:
           #           self.talk("I couldn't get a response from the AI. Please try again.")

          
          #  elif "wikipedia note" in self.command:
           #           self.talk("Fetching Wikipedia data and writing it to Notepad.")
            #          wikipedia_to_notepad()          

            
                  # Handle "maximize" command for any application         
            #if ('play a song' in self.command) or ('youtube' in self.command) or ("download a song" in self.command) or ("download song" in self.command) : 
                #commands for opening youtube, playing a song in youtube, and download a song in youtube
             #   self.yt(self.command) #function is from line 555
            #Interaction commands with CIPHER
            #elif ('your age' in self.command) or ('are you single'in self.command) or ('are you there' in self.command) or ('tell me something' in self.command) or ('thank you' in self.command) or ('in your free time' in self.command) or ('i love you' in self.command) or ('can you hear me' in self.command) or ('do you ever get tired' in self.command):
             #   self.Fun(self.command)
            #elif 'time' in self.command : 
             #   self.Clock_time(self.command)
            #elif (('hi' in self.command) and len(self.command)==2) or ((('hai' in self.command) or ('hey' in self.command)) and len(self.command)==3) or (('hello' in self.command) and len(self.command)==5):
             #   self.comum(self.command)
                
            #elif ('what can you do' in self.command) or ('your name' in self.command) or ('my name' in self.command) or ('university name' in self.command):
             #   self.Fun(self.command)
            #elif ('joke'in self.command) or ('date' in self.command):
             #   self.Fun(self.command)
            #schedule commands for remembering you what is the planns of the day
            #elif ("college time table" in self.command) or ("schedule" in self.command):
             #   self.shedule() #function is present from 407
            #It will tell the day Eg : Today is wednesday
            #elif ("today" in self.command):
               # day = self.Cal_day()
              #  self.talk("Today is "+day)
              
            # Check for greeting commands
            if self.command in ['hi', 'hai', 'hey', 'hello']:
              self.comum(self.command)

# Check for time-related queries
            elif 'current time' in self.command:
             self.Clock_time(self.command)

# Check for general interaction commands with CIPHER
            elif any(keyword in self.command for keyword in ['your age', 'are you single', 'are you there', 'tell me something', 
                                                 'thank you', 'in your free time', 'i love you', 'can you hear me', 
                                                 'do you ever get tired']):
             self.Fun(self.command)

# Check for functional queries about capabilities and user information
            elif any(keyword in self.command for keyword in ['what can you do', 'your name', 'my name', 'university name']):
             self.Fun(self.command)

# Check for humor-related queries
            elif any(keyword in self.command for keyword in ['joke', 'will you go with me on date']):
             self.Fun(self.command)

# Check for schedule-related commands
            elif any(keyword in self.command for keyword in ['college time table', 'schedule']):
              self.shedule()  # Function defined at line 407

# Check for day-related queries
            elif "today's day" in self.command:
             day = self.Cal_day()
             self.talk(f"Today is {day}")

# Check for media-related commands (YouTube play/download)
           # elif any(keyword in self.command for keyword in ['play a song','play the song','play song', 'youtube', 'download a song', 'download song']):
            # self.yt(self.command)  # Function defined at line 555

    
            #commad for opening any weekly meeting links
            #Eg: I have kept a meeting my amFOSS club 
            #Note: the given link is fake!!
           # elif ("meeting" in self.command):
            #    self.talk("Ok sir opening meeet")
             #   webbrowser.open("https://meeting/")
            #command if you don't want the CHIPHER to spack until for a certain time
            #Note: I can be silent for max of 10mins
            # Eg: chipher keep quiet for 5 minutes 
            #elif ('silence' in self.command) or ('silent' in self.command) or ('keep quiet' in self.command) or ('wait for' in self.command) :
             #   self.silenceTime(self.command)
            #elif ('where i am' in self.command) or ('where we are' in self.command):
             #   self.locaiton()    
            #Command for opening your social media accounts in webrowser
            #Eg : chipher open facebook (or) chipher open social media facebook 
           # elif ('facebook' in self.command) or ('whatsapp' in self.command) or ('instagram' in self.command) or ('twitter' in self.command) or ('discord' in self.command) or ('social media' in self.command):
            #    self.social(self.command)
            #command for opening your OTT platform accounts
            #Eg: open hotstart
            #elif ('hotstar' in self.command) or ('prime' in self.command) or ('netflix' in self.command):
             #   self.OTT(self.command)
            #Command for opening your online classes links
            #elif ('online classes'in self.command):
             #   self.OnlineClasses(self.command)
            #command for opeing college websites
            #elif ('teams'in self.command) or ('stream'in self.command) or ('sharepoint'in self.command) or('outlook'in self.command)or('amrita portal'in self.command)or('octave'in self.command):
             #   self.college(self.command)
           # elif ('add' in self.command) or ('subtract' in self.command):# or ('multiply' in self.command) or ('divide' in self.command):
            #    self.perform_task(self.command)    
            #command to search for something in wikipedia
            #Eg: what is meant by python in wikipedia (or) search for "_something_" in wikipedia
            elif ('what is meant by' in self.command)  or ('who is' in self.command):
                self.B_S(self.command)
            #command for opening your browsers and search for information in google
            #lif ('search'in self.command) or (' microsoft edge'in self.command) :
             #   self.brows(self.command)
            #command to open your google applications
           # elif (' gmail'in self.command) or('maps'in self.command) or('documents'in self.command )or('spreadsheet'in self.command) or('photos'in self.command) or(' drive'in self.command) or('news' in self.command):
            #    self.Google_Apps(self.command)
            #command to open your open-source accounts
            #you can add other if you have
            #elif (' github'in self.command) or ('gitlab'in self.command) :
             #   self.open_source(self.command)
            #commands to open presentaion makeing tools like CANVA and GOOGLE SLIDES
            #elif ('slides'in self.command) or (' canva'in self.command) :
             #   self.edit(self.command)
            #Command to open desktop applications
            #It can open : caliculator, notepad,paint, teams(aka online classes), discord, spotify, ltspice,vscode(aka editor), steam, VLC media player
            #elif  (' online classes' in self.command) or ('discord' in self.command) or ('ltspice' in self.command):
              #   self.OpenApp(self.command)
           # elif ('add' in self.command) or ('subtract' in self.command) or ('multiply' in self.command) or ('divide' in self.command):
            #     self.perform_task(self.command)
# Command to close desktop applications
 #It can close: calculator, notepad, paint, discord, spotify, ltspice, vscode(aka editor), steam, VLC media player
            #elif ('close calculator' in self.command) or ('close notepad' in self.command) or ('close paint' in self.command) or ('close discord' in self.command) or ('close ltspice' in self.command) or ('close editor' in self.command) or ('close spotify' in self.command) or ('close steam' in self.command) or ('close media player' in self.command) or ('close wordpad' in self.command) or ('close powerpoint' in self.command) or ('close excel' in self.command) or ('close wifi' in self.command) or ('close bluetooth' in self.command):
             #    self.CloseApp(self.command)
            #command for opening shopping websites 
            #NOTE: you can add as many websites
            #elif ('flipkart'in self.command) or ('amazon'in self.command) or ('meesho'in self.command):
             #  self.shopping(self.command)
            #command for asking your current location
            #elif ('where am i' in self.command) or ('where are we' in self.command):
             #   self.locaiton()
            #command for opening command prompt 
            #Eg: chipher open command prompt
           # elif ('command prompt'in self.command) :
            ##   os.system('start cmd')
            #Command for opening an instagram profile and downloading the profile pictures of the profile
            #Eg: chipher open a profile on instagram 
            #elif ('instagram profile' in self.command) or("profile on instagram" in self.command):
             #   self.Instagram_Pro()
            #Command for opening taking screenshot
            #Eg: chipher take a screenshot
            #elif ('take screenshot' in self.command)or ('screenshot' in self.command) or("take a screenshot" in self.command):
             #   self.scshot()
            #Command for reading PDF
            #EG: chipher read pdf
            #elif ("read pdf" in self.command) or ("pdf" in self.command):
             #   self.pdf_reader()
            #command for searching for a procedure how to do something
            #Eg:chipher activate mod
            #   chipher How to make a cake (or) chipher how to convert int to string in programming 
           # elif "activate how to mod" in self.command:
            #    self.How()
            #command for increaing the volume in the system
            #Eg: chipher increase volume
            #elif ("volume up" in self.command) or ("increase volume" in self.command):
             #   pyautogui.press("volumeup")
              #  self.talk('volume increased')
            #command for decreaseing the volume in the system
            #Eg: chipher decrease volume
            #elif ("volume down" in self.command) or ("decrease volume" in self.command):
             #   pyautogui.press("volumedown")
              #  self.talk('volume decreased')
            #Command to mute the system sound
            #Eg: chipher mute the sound
            #elif ("volume mute" in self.command) or ("mute the sound" in self.command) :
             #   pyautogui.press("volumemute")
              #  self.talk('volume muted')
            #command for opening your mobile camera the description for using this is in the README file
            #Eg: chipher open mobile camera
            #elif ("mobile cam" in self.command):
             #   self.Mobilecamra()
            #command for opening your webcamera
            #Eg: chipher open webcamera
            #elif ('web cam'in self.command) :
             #   self.webCam()
            #Command for creating a new contact
           # elif("register the contact" in self.command):
            #    self.AddContact()
            #Command for searching for a contact
            #elif("number in contacts" in self.command):
             #   self.NameIntheContDataBase(self.command)
            #Command for displaying all contacts
            #elif("display all the contacts" in self.command):
             #   self.Display()
            #Command for checking covid status in India
            #Eg: chipher check covid (or) corona status
            #elif ("covid" in self.command) or  ("corona" in self.command):
             #   self.talk("Boss which state covid 19 status do you want to check")
              #  s = self.take_Command()
               # self.Covid(s)
                        # Command to mute chipher for a specific duration
            elif ('keep quiet' in self.command) or ('be silent' in self.command) or ('stay quiet' in self.command):
                self.silenceTime(self.command)

            # Command to open meeting link
           # elif ('meetings' in self.command) or ('join meeting' in self.command) or ('start meeting' in self.command) or ('meeting' in self.command):
            #    self.talk("Opening the meeting link now.")
             #   webbrowser.open("https://meeting/")

            # Command to ask for current location
            elif ('where am i' in self.command) or ('current location' in self.command):
                self.locaiton()

            # Open popular streaming services like Hotstar, Netflix, Prime Video
          #  elif ('hotstar' in self.command) or ('prime video' in self.command) or ('netflix' in self.command):
           #     self.OTT(self.command)

            # Command to attend online classes
            #elif ('join class' in self.command) or ('online class' in self.command) or ('join classes' in self.command):
             #   self.OnlineClasses(self.command)

            # Open college-related services like Teams, SharePoint, etc.
           # elif ('teams' in self.command) or ('stream' in self.command) or ('sharepoint' in self.command):
            #    self.college(self.command)

            # Command for simple arithmetic operations
           # elif ('multiply' in self.command) or ('divide' in self.command): #or ('add' in self.command) or ('subtract' in self.command):
            #    self.perform_task(self.command)

            # Command to search or inquire on Wikipedia
            elif ('what is' in self.command) or ('tell me about' in self.command) or ('what is the' in self.command):
                self.B_S(self.command)

            # Command to search something on Google
            elif ('search on google' in self.command) or ('open microsoft edge' in self.command):
                self.brows(self.command)

            # Command to open GitHub or GitLab repositories
            #elif ('github' in self.command) or ('gitlab' in self.command):
             #   self.open_source(self.command)

            # Command to edit presentations using tools like Google Slides or Canva
            elif ('create slides' in self.command) or ('design presentation' in self.command):
                self.edit(self.command)

            # Command to launch desktop applications (Discord, Teams, LTSpice)
          #  elif ('open discord' in self.command) or ('launch ltspice' in self.command) or ('start online class' in self.command):
           #     self.OpenApp(self.command)

            # Command to open or download Instagram profiles
            elif ('view instagram profile' in self.command) or ('download instagram picture' in self.command):
                self.Instagram_Pro()

            # Command to capture a screenshot
            elif ('take screenshot' in self.command) or ('capture screen' in self.command):
                self.scshot()

            # Command to read PDF documents
          #  elif ('read pdf' in self.command) or ('open pdf file' in self.command):
           #     self.pdf_reader()

            # Command to activate special modes or features
           # elif "how to" in self.command:
            #    self.How()

            # Command to increase the system volume
            elif ('volume up' in self.command) or ('increase volume' in self.command):
                pyautogui.press("volumeup")
                self.talk('Volume increased')

            # Command to decrease the system volume
            elif ('volume down' in self.command) or ('decrease volume' in self.command):
                pyautogui.press("volumedown")
                self.talk('Volume decreased')

            # Command to mute/unmute system sound
            elif ('mute sound' in self.command) or ('unmute sound' in self.command) or ('unmute volume' in self.command) or ('unmute volume' in self.command):
                pyautogui.press("volumemute")
                self.talk('Sound muted')

            # Command to open mobile camera
            elif ("open mobile camera" in self.command) or ('start mobile camera' in self.command):
                self.Mobilecamra()

            # Command to open web camera
            elif ('start web camera' in self.command) or ('open webcam' in self.command):
                self.webCam()

            # Command to add a new contact
           # elif ("add new contact" in self.command) or ("create contact" in self.command):
            #    self.AddContact()

            # Command to find a contact by phone number
           # elif ("search contact by number" in self.command) or ("find contact number" in self.command):
            #    self.NameIntheContDataBase(self.command)

            # Command to show all saved contacts
        #    elif ("display all contacts" in self.command) or ("show contacts" in self.command):
         #       self.Display()

            # Command to check COVID-19 status
          #  elif ("check covid status" in self.command) or ("corona status" in self.command):
           #     self.talk("Which state's COVID-19 status would you like to know?")
            #    state = self.listen_Command()
             #   self.Covid(state)
    
            #Command for screenRecording
            #Eg: chipher start Screen recording
            elif ("recording" in self.command) or ("screen recording" in self.command) or ("voice recording" in self.command):
                try:
                    self.talk("Boss press escape key to stop recordings")
                    option = self.command
                    StartRecording(option=option)
                    self.talk("Boss recording is being saved")
                except:
                    self.talk("Boss an unexpected error occured couldn't start screen recording")
            #Command for phone number tracker
            elif ("track mobile number" in self.command) or ("track phone number" in self.command) or ("track a phone number" in self.command):
                self.talk("Boss, please enter the mobile number with country code (e.g., +14158586273)")

                location, service_provider, lat, lng = tracker()

                if location:
                    self.talk(f"Boss, the mobile number is from {location}, and the service provider is {service_provider}.")

                    if lat and lng:
                        self.talk(f"The latitude is {lat} and the longitude is {lng}.")
                        self.talk("Boss, the location of the mobile number has been saved in Maps.")
                    else:
                        self.talk("Location coordinates were not available, but the basic details were found.")

                    print(f"Location: {location}, Service Provider: {service_provider}")
                    print(f"Latitude: {lat}, Longitude: {lng}")
                else:
                    self.talk("Boss, I couldn't track the mobile number. Please make sure it's correct.")

#  Now start a completely separate block for music
            elif 'music' in self.command:
                try:
         # 🔄 Dynamically get the user's Music directory
                    music_dir = os.path.join(os.path.expanduser("~"), "Music")
         
                    if not os.path.exists(music_dir):
                        self.talk("Boss, I couldn't find your Music folder.")
                        return

                    songs = os.listdir(music_dir)
                    for song in songs:
                        if song.endswith('.mp3'):
                           os.startfile(os.path.join(music_dir, song))
                           break  # Play only the first song
                    else:
                        self.talk("Boss, no music files found in your Music folder.")
                except Exception as e:
                    self.talk(f"Boss, an unexpected error occurred: {e}")


            #command for knowing your system IP address
            #Eg: chipher check my ip address
           # elif 'my ip' in self.command:
            #    ip = get('https://api.ipify.org').text
             #  # print(f"your IP address is {ip}")
              #  self.talk(f"your IP is {ip}")
            #command for seading a whatsapp group and individual message
            #Individual => Eg: send a message to sujith
            #group => Eg: send a message to school group NOTE: mention the name "group" otherwise chipher cannot detect the name

           # elif ('send a message' in self.command):
            #    self.whatsapp(self.command)
            #command for sending an email 
            #Eg: chipher send email
            elif 'send email' in self.command:
                self.verifyMail()
            #command for checking the temperature in surroundings
            #chipher check the surroundings temperature
            elif ("weather" in self.command):
                self.temperature()
            #Command to generate the qr codes
            elif "generate a qr code" in self.command:
                self.generate_qr_code()
            #command for checking internet speed
            #Eg: chipher check my internet speed
         #   elif "internet speed" in self.command:
          #      self.InternetSpeed()
            #command to make the chipher sleep
            #Eg: chipher you can sleep now
            elif ("you can sleep" in self.command) or ("sleep now" in self.command):
                self.talk("Okay boss, I am going to sleep you can call me anytime.")
                break
            #command for waking the chipher from sleep
            #chipher wake up
            elif ("wake up" in self.command) or ("get up" in self.command):
                self.talk("boss, I am not sleeping, I am in online, what can I do for u")
            #command for exiting chipher from the program
            #Eg: chipher goodbyes
            elif ("goodbye" in self.command) or ("get lost" in self.command):
                self.talk("Thanks for using me boss, have a good day")
                QtWidgets.QApplication.instance().quit()
              


            #command for knowing about your system condition
            #Eg: chipher what is the system condition
           # elif ('system condition' in self.command) or ('condition of the system' in self.command):
            #    self.talk("checking the system condition")
             #   self.condition()
            #command for knowing the latest news
            #Eg: chipher tell me the news
           # elif ('tell me news' in self.command) or ("the news" in self.command) or ("todays news" in self.command):
            #    self.talk("Please wait boss, featching the latest news")
             #   self.news()
            #command for shutting down the system
            #Eg: chipher shutdown the system
            elif ('shutdown the system' in self.command) or ('down the system' in self.command):
                self.talk("Boss shutting down the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 5")
            #command for restarting the system
            #Eg: chipher restart the system
            elif 'restart the system' in self.command:
                self.talk("Boss restarting the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 5")
            #command for make the system sleep
            #Eg: chipher sleep the system
            elif 'sleep the system' in self.command:
                self.talk("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
                        # Voice Control Commands
            elif any(keyword in self.command for keyword in ["type", "press", "select", "copy", "paste", "cut", "undo", "redo"]):
                self.voice_control(self.command)
                        # Remember and Retrieve Past Activities
            elif "what did i do" in self.command or "past activities" in self.command:
                memory_manager.read_past_activities()
            
            elif "remember this" in self.command:
                task = self.command.replace("remember this", "").strip()
                memory_manager.remember_reminder(task)
            
            elif "what are my reminders" in self.command or "list reminders" in self.command:
                memory_manager.list_reminders()
            
            elif "clear all reminders" in self.command or "delete reminders" in self.command:
                memory_manager.delete_reminders()

            # Log every recognized command
                memory_manager.log_activity(self.command)

            # Music and Video Controls
            elif any(keyword in self.command for keyword in ["play", "pause", "next", "previous", "stop", "mute", "unmute", "volume up", "volume down", "loop", "shuffle", "subtitles", "change audio "]):
               self.media_control(self.command)
            elif any(keyword in self.command for keyword in ["scroll up", "scroll down", "scroll left", "scroll right"]):
               self.scroll_control(self.command)
            elif any(keyword in self.command for keyword in ["bold", "italic", "underline", "increase font", "decrease font", "copy", "cut", "paste", "undo", "redo"]):
                self.text_formatting(self.command)
            elif any(keyword in self.command for keyword in ["insert a slide", "delete a slide", "insert a page", "delete a page", "insert a line", "delete a line"]):
              self.slide_page_control(self.command)
          #  elif any(keyword in self.command for keyword in ["search for", "move", "copy", "rename", "delete", "open", "compress", "extract"]):
           #       universal_file_manager(self)


  
    
    def slide_page_control(self, command):
     """
     Control slide and page management for PowerPoint, Word, WordPad, Notepad, and other editors.
     """
    # Insert Slide (PowerPoint)
     if "insert slide" in command:
        self.talk("Inserting a new slide.")
        pyautogui.hotkey("ctrl", "m")

    # Delete Slide (PowerPoint)
     elif "delete slide" in command:
        self.talk("Deleting the current slide.")
        pyautogui.hotkey("ctrl", "shift", "d")  # Duplicate Slide (to avoid data loss)
        pyautogui.press("delete")               # Then Delete

    # Insert Page or Line (Word, WordPad, Notepad)
     elif "insert page" in command or "insert line" in command:
        self.talk("Inserting a new page or line.")
        if "page" in command:
            pyautogui.hotkey("ctrl", "enter")   # New Page in Word or WordPad
        else:
            pyautogui.press("enter")            # New Line in any editor

    # Delete Page or Line (Word, WordPad, Notepad)
     elif "delete page" in command or "delete line" in command:
        self.talk("Deleting the current page or line.")
        pyautogui.press("backspace")            # Delete the line or page break

   
    
                
    def media_control(self, command):
     """
     Universal media control: Works across any media app using keyboard shortcuts.
     """
     command = command.lower()

    # Handle STOP first to prevent 'play' from triggering
    # if any(kw in command for kw in ["stop playing", "stop music", "stop video", "stop the"]):
     #    self.talk("Stopping playback.")
      #   pyautogui.press("stop")

    # elif "pause" in command and "play" not in command:
     #    self.talk("Pausing.")
      #   pyautogui.press("playpause")

     #elif "stop" in command and "play" not in command and "pause" not in command:
      #   self.talk("Stopping playback.")
       #  pyautogui.press("stop")

   #  elif "play" in command and not any(kw in command for kw in ["stop", "pause", "stop playing", "stop music"]):
    #     self.talk("Playing.")
     #    pyautogui.press("playpause")

     if "next" in command:
         self.talk("Skipping to the next track.")
         pyautogui.press("nexttrack")

     elif "previous" in command:
         self.talk("Going back to the previous track.")
         pyautogui.press("prevtrack")

   #  elif "mute" in command:
    #     self.talk("Toggling mute.")
     #    pyautogui.press("volumemute")

    # elif "volume up" in command:
     #    self.talk("Increasing volume.")
      #   pyautogui.press("volumeup")

     #elif "volume down" in command:
      #   self.talk("Decreasing volume.")
       #  pyautogui.press("volumedown")

     elif "loop" in command:
         self.talk("Toggling loop mode.")
         pyautogui.hotkey("ctrl", "l")

     elif "shuffle" in command:
         self.talk("Toggling shuffle mode.")
         pyautogui.hotkey("ctrl", "s")

     elif "subtitles" in command:
         self.talk("Toggling subtitles.")
         pyautogui.press("v")

     elif "change audio" in command or "audio track" in command:
         self.talk("Changing audio track.")
         pyautogui.press("b")




    def scroll_control(self, command):
     """
    Control scrolling in any Windows application using mouse scroll actions.
    """
    # Scroll Up
     if "scroll up" in command:
          self.talk("Scrolling up.")
          pyautogui.scroll(300)  # Scroll up by 300 units

    # Scroll Down
     elif "scroll down" in command:
        self.talk("Scrolling down.")
        pyautogui.scroll(-300)  # Scroll down by 300 units

    # Scroll Left (Horizontal Scroll)
     elif "scroll left" in command:
        self.talk("Scrolling left.")
        pyautogui.hscroll(-100)  # Scroll left by 100 units

    # Scroll Right (Horizontal Scroll)
     elif "scroll right" in command:
        self.talk("Scrolling right.")
        pyautogui.hscroll(100)  # Scroll right by 100 units
     elif any(keyword in self.command for keyword in ["bold", "italic", "underline", "increase font", "decrease font", "copy", "cut", "paste", "undo", "redo"]):
        self.text_formatting(self.command)
    
    def text_formatting(self, command):
     """
     Control text formatting in any Windows application using keyboard shortcuts.
     """
    # Bold Text
     if "bold" in command:
        self.talk("Making text bold.")
        pyautogui.hotkey("ctrl", "b")

    # Italic Text
     elif "italic" in command:
        self.talk("Italicizing text.")
        pyautogui.hotkey("ctrl", "i")

    # Underline Text
     elif "underline" in command:
        self.talk("Underlining text.")
        pyautogui.hotkey("ctrl", "u")

    # Increase Font Size
     elif "increase font" in command or "make text bigger" in command:
        self.talk("Increasing font size.")
        pyautogui.hotkey("ctrl", "shift", ">")

    # Decrease Font Size
     elif "decrease font" in command or "make text smaller" in command:
        self.talk("Decreasing font size.")
        pyautogui.hotkey("ctrl", "shift", "<")

    # Copy
     elif "copy" in command:
        self.talk("Copying selected text.")
        pyautogui.hotkey("ctrl", "c")

    # Cut
     elif "cut" in command:
        self.talk("Cutting selected text.")
        pyautogui.hotkey("ctrl", "x")

    # Paste
     elif "paste" in command:
        self.talk("Pasting from clipboard.")
        pyautogui.hotkey("ctrl", "v")

    # Undo
     elif "undo" in command:
        self.talk("Undoing last action.")
        pyautogui.hotkey("ctrl", "z")

    # Redo
     elif "redo" in command:
        self.talk("Redoing last action.")
        pyautogui.hotkey("ctrl", "y")

                
        # Voice-Controlled Text Interaction
    def voice_control(self, command):
        # Text Input
        if "type" in command:
            text_to_type = command.replace("type", "").strip()
            self.talk(f"Typing: {text_to_type}")
            pyautogui.write(text_to_type)

        # Keyboard Shortcuts
        elif "press enter" in command:
            self.talk("Pressing Enter.")
            pyautogui.press("enter")
        elif "press tab" in command:
            self.talk("Pressing Tab.")
            pyautogui.press("tab")
        elif "press escape" in command:
            self.talk("Pressing Escape.")
            pyautogui.press("esc")
        elif "press backspace" in command:
            self.talk("Pressing Backspace.")
            pyautogui.press("backspace")
        elif "press delete" in command:
            self.talk("Pressing Delete.")
            pyautogui.press("delete")

        # Text Selection
        elif "select all" in command:
            self.talk("Selecting all text.")
            pyautogui.hotkey('ctrl', 'a')
        elif "select up" in command:
            self.talk("Selecting text up.")
            pyautogui.hotkey('shift', 'up')
        elif "select down" in command:
            self.talk("Selecting text down.")
            pyautogui.hotkey('shift', 'down')
        elif "select left" in command:
            self.talk("Selecting text to the left.")
            pyautogui.hotkey('shift', 'left')
        elif "select right" in command:
            self.talk("Selecting text to the right.")
            pyautogui.hotkey('shift', 'right')

        # Copy, Paste, Cut, Undo, Redo
        elif "copy" in command:
            self.talk("Copying selection.")
            pyautogui.hotkey('ctrl', 'c')
        elif "paste" in command:
            self.talk("Pasting from clipboard.")
            pyautogui.hotkey('ctrl', 'v')
        elif "cut" in command:
            self.talk("Cutting selection.")
            pyautogui.hotkey('ctrl', 'x')
        elif "undo" in command:
            self.talk("Undoing last action.")
            pyautogui.hotkey('ctrl', 'z')
        elif "redo" in command:
            self.talk("Redoing last action.")
            pyautogui.hotkey('ctrl', 'y')


   #calculator
    def extract_numbers(self, command):
        """Extract numbers from the user's voice command, supporting decimals."""
        numbers = re.findall(r'\d+\.?\d*', command)  # Match integers and decimals
        return list(map(float, numbers))  # Convert to floats

    def format_number(self, num):
        """Format a number to avoid decimal points for whole numbers."""
        if num.is_integer():
            return int(num)  # Return as an integer
        return round(num, 2)  # Return as a rounded decimal (2 decimal places)

    def perform_task(self, command):
         """Perform mathematical operations directly."""
         if not command:
             self.talk("No command detected.")
             return

         # Open the Windows Calculator
         self.talk("Performing calculation.")
         os.system("start calc.exe")
         time.sleep(2)  # Wait for the calculator to open

         # Extract numbers and operation
         numbers = self.extract_numbers(command)
         if len(numbers) < 2:
             self.talk("Please provide two numbers.")
             return

         num1, num2 = numbers[0], numbers[1]

        #  Identify the operation
         if 'add' in command or 'plus' in command:
             operation = '+'
             result = num1 + num2
         elif 'subtract' in command or 'minus' in command:
             operation = '-'
             result = num1 - num2
         elif 'multiply' in command or 'times' in command:
             operation = '*'
             result = num1 * num2
         elif 'divide' in command or 'by' in command:
             operation = '/'
             if num2 != 0:
                 result = num1 / num2
             else:
                 self.talk("Division by zero is not allowed.")
                 return
         else:
             self.talk("Sorry, I didn't understand the operation.")
             return

        # Format the result
         formatted_result = self.format_number(result)

        # Speak the result
         self.talk(f"The result of {self.format_number(num1)} {operation} {self.format_number(num2)} is {formatted_result}.")

        # Enter numbers and operation into the calculator using pyautogui
         pyautogui.typewrite(str(self.format_number(num1)))  # Enter the first number
         pyautogui.press(operation)  # Press the operator
         pyautogui.typewrite(str(self.format_number(num2)))  # Enter the second number
         pyautogui.press('enter')  # Press Enter to calculate

        # Print the result to the terminal for debugging purposes
        # print(f"The result of {self.format_number(num1)} {operation} {self.format_number(num2)} is {formatted_result}.")

  

    #Intro msg
    def Intro(self):
        while True:
            self.permission = self.listen_Command()
            print(self.permission)
            if ("hey cypher" in self.permission) or ("wake up" in self.permission):# or ("cypher" in self.permission):
                self.run_cipher()
            elif ("goodbye" in self.permission) or ("get lost" in self.permission):
                self.talk("Thanks for using me boss, have a good day")
                sys.exit()
                
    

    #Wish
   # def wish(self):
    #    hour = int(datetime.datetime.now().hour)
     #   t = time.strftime("%I:%M %p")
      #  day = self.Cal_day()
       # print(t)
        #if (hour>=0) and (hour <=12) and ('AM' in t):
         #   self.talk(f'Good morning boss, its {day} and the time is {t}')
        #elif (hour >= 12) and (hour <= 16) and ('PM' in t):
         #   self.talk(f"good afternoon boss, its {day} and the time is {t}")
        #else:
         #   self.talk(f"good evening boss, its {day} and the time is {t}")
    def wish(self):
        hour = int(datetime.datetime.now().hour)
        t = time.strftime("%I:%M %p")
        day = self.Cal_day()
        print(t)
    
        if 0 <= hour <= 12 and 'AM' in t:
           self.talk(f"Good morning, master! Today is {day}, and the time is {t}.")
        elif 12 <= hour <= 16 and 'PM' in t:
           self.talk(f"Good afternoon, master! It's {day}, and the time is {t}.")
        else:
            self.talk(f"Good evening, master! The date is {day}, and the time is {t}.")
        

    #Weather forecast
    def temperature(self):
     try:
        # Get user's IP address and location
        ip_url = 'https://api.ipify.org'
        IP_Address = requests.get(ip_url).text
        
        geo_url = f'https://get.geojs.io/v1/ip/geo/{IP_Address}.json'
        geo_request = requests.get(geo_url)
        geo_data = geo_request.json()
        
        city = geo_data.get('city', 'unknown location')
        
        # Use OpenWeatherMap API for temperature
        api_key = ""  # Replace with your API key
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        if weather_data.get('cod') != 200:
            self.talk(f"Sorry boss, I couldn't fetch the temperature for {city}.")
            return
        
        temp = weather_data['main']['temp']
        self.talk(f"Boss, the current temperature in {city} is {temp} degrees Celsius.")
    
     except Exception as e:
        self.talk(f"An error occurred: {e}")

    
    #qrCodeGenerator
    #def qrCodeGenerator(self):
        #self.talk(f"Boss enter the text/link that you want to keep in the qr code")
        #input_Text_link = input("Enter the Text/Link : ")
        #qr = qrcode.QRCode(
        #    version=1,
        #    error_correction=qrcode.constants.ERROR_CORRECT_L,
        #    box_size=15,
        #    border=4,
        #)
        #QRfile_name = (str(datetime.datetime.now())).replace(" ","-")
        #QRfile_name = QRfile_name.replace(":","-")
        #QRfile_name = QRfile_name.replace(".","-")
        #QRfile_name = QRfile_name+"-QR.png"
        #qr.add_data(input_Text_link)
        #qr.make(fit=True)

        #img = qr.make_image(fill_color="black", back_color="white")
        #img.save(f"QRCodes\{QRfile_name}")
        #self.talk(f"Boss the qr code has been generated")

    def generate_qr_code(self):
        self.talk("Master, please provide the text or link for the QR code.")
        input_text_link = input("Enter the Text/Link: ")

        # Prepare the QR code generator
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4
        )

        # Create a unique file name based on the current date and time
        qr_file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + "-QR.png"

        # Add the input data to the QR code
        qr.add_data(input_text_link)
        qr.make(fit=True)

        # Create the QR code image
        img = qr.make_image(fill='black', back_color='white')

        # Save the generated QR code
        img.save(f"QRCodes/{qr_file_name}")

        # Notify the user
        self.talk("Master, the QR code has been successfully generated.")

    #Mobile camera
    def Mobilecamra(self):
        import urllib.request
        import numpy as np
        try:
            self.talk(f"Boss openinging mobile camera")
            URL = "http://_IP_Webcam_IP_address_/shot.jpg" #Discription for this is available in the README file
            while True:
                imag_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(imag_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    self.talk(f"Boss closing mobile camera")
                    break
            cv2.destroyAllWindows()
        except Exception as e:
            print("Some error occured")

    #Web camera
    #NOTE to exit from the web camera press "ESC" key 
    def webCam(self):    
        self.talk('Opening camera')
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('web camera',img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    
    #covid 
    #def Covid(self,s):
        #try:
            #from covid_india import states
            #details = states.getdata()
            #if "check in" in s:
              #  s = s.replace("check in","").strip()
             #   print(s)
            #elif "check" in s:
             #   s = s.replace("check","").strip()
            #    print(s)
            #elif "tech" in s:
            #    s = s.replace("tech","").strip()
            #s = states[s]
            #ss = details[s]
            #Total = ss["Total"]
            #Active = ss["Active"]
            #Cured = ss["Cured"]
            #Death = ss["Death"]
            #print(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            #self.talk(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            #time.sleep(5)
            #self.talk("Boss do you want any information of other states")
            #I = self.listen_Command()
            #print(I)
            #if ("check" in I):
            #    self.Covid(I)
           # elif("no" in I):
           #     self.talk("Okay boss stay home stay safe")
          #  else:
         #       self.talk("Okay boss stay home stay safe")
        #except:
            #self.talk("Boss some error occured, please try again")
            #self.talk("Boss do you want any information of other states")
            #I = self.listen_Command()
            #if("yes" in I):
               # self.talk("boss, Which state covid status do u want to check")
              #  Sta = self.listen_Command_Command()
             #   self.Covid(Sta)
            #elif("no" in I):
             #   self.talk("Okay boss stay home stay safe")
            #else:
           #     self.talk("Okay boss stay home stay safe")

    def Covid(self, s):
     try:
        from territories import states
        details = states.getdata()
        
        # Process the command input
        if "check in" in s:
            s = s.replace("check in", "").strip()
            print(s)
        elif "check" in s:
            s = s.replace("check", "").strip()
            print(s)
        elif "tech" in s:
            s = s.replace("tech", "").strip()
        
        # Fetch state data
        s = states.get(s, None)
        if not s:
            raise ValueError(f"State '{s}' not found.")
        
        ss = details.get(s, None)
        if not ss:
            raise ValueError(f"Details for state '{s}' not found.")
        
        Total = ss["Total"]
        Active = ss["Active"]
        Cured = ss["Cured"]
        Death = ss["Death"]
        
        # Display the results
        print(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
        self.talk(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
        time.sleep(5)
        
        # Ask if the user wants information on other states
        self.talk("Boss do you want any information of other states?")
        I = self.listen_Command()
        print(I)
        
        if "check" in I:
            self.Covid(I)
        elif "no" in I:
            self.talk("Okay boss, stay home, stay safe.")
        else:
            self.talk("Okay boss, stay home, stay safe.")
    
     except ValueError as ve:
        self.talk(f"Boss, there was an error: {str(ve)}. Please try again.")
        self.talk("Boss do you want any information of other states?")
        I = self.listen_Command()
        
        if "yes" in I:
            self.talk("Boss, which state COVID status do you want to check?")
            Sta = self.listen_Command()
            self.Covid(Sta)
        elif "no" in I:
            self.talk("Okay boss, stay home, stay safe.")
        else:
            self.talk("Okay boss, stay home, stay safe.")
    
     except Exception as e:
        self.talk("Boss, some error occurred. Please try again.")
        self.talk("Boss do you want any information of other states?")
        I = self.listen_Command()
        
        if "yes" in I:
            self.talk("Boss, which state COVID status do you want to check?")
            Sta = self.listen_Command()
            self.Covid(Sta)
        elif "no" in I:
            self.talk("Okay boss, stay home, stay safe.")
        else:
            self.talk("Okay boss, stay home, stay safe.")

                

    #Whatsapp
    def whatsapp(self, command):
     try:
         command = command.replace('send a message to', '').strip()
         
          # Search for contact info
         name, numberID, F = self.SearchCont(command)
        
         if F:  # Contact found
             print(numberID)
             self.talk(f'Boss, what message do you want to send to {name}?')
             message = self.listen_Command()
             hour = int(datetime.datetime.now().hour)
             minute = int(datetime.datetime.now().minute)
             print(hour, minute)
 
             # Ensure minute does not go beyond 59
             if minute == 59:
                 minute = 0
                 hour += 1
             
             # Send message based on whether it's a group or direct contact
             if "group" in command.lower():
                 kit.sendwhatmsg_to_group(numberID, message, hour, minute + 1)
             else:
                 kit.sendwhatmsg(numberID, message, hour, minute + 1)
             self.talk("Boss, the message has been sent.")
        
         else:  # Contact not found
             self.talk(f'Boss, the name is not found in our database. Shall I add the contact?')
             AddOrNot = self.listen_Command().strip().lower()
             
             if not AddOrNot:  # If no response or unclear response
                  self.talk("I didn't get your answer, boss. Cancelling the message.")
                  return
 
            # Process add contact decision
             add_positive_responses = ["yes", "add", "yeah", "yah", "yes add contact"]
             add_negative_responses = ["no", "do not", "don't do it"]
             
             if any(yes in AddOrNot for yes in add_positive_responses):
                 self.AddContact()  # Assuming AddContact method is defined
             elif any(no in AddOrNot for no in add_negative_responses):
                 self.talk('Ok, boss.')
             else:
                  self.talk('Sorry, I did not understand. Cancelling the action.')

     except Exception as e:
         print(f"Error occurred: {str(e)}. Please try again.")
         self.talk("An error occurred while processing the command, please try again.")


            

    
    #Add contacts
    def AddContact(self):
        self.talk(f'Boss, Enter the contact details')
        name = input("Enter the name :").lower()
        number = input("Enter the number :")
        NumberFormat = f'"{name}":"+91{number}"'
        ContFile = open("Contacts.txt", "a") 
        ContFile.write(f"{NumberFormat}\n")
        ContFile.close()
        self.talk(f'Boss, contact saved Successfully')

    #Search Contact
    def SearchCont(self,name):
        with open("Contacts.txt","r") as ContactsFile:
            for line in ContactsFile:
                if name in line:
                    print("Name Match Found")
                    s = line.split("\"")
                    return s[1],s[3],True
        return 0,0,False
    
    #Display all contacts
    def show(self):
     ContactsFile = open("Contacts.txt", "r")
     lines = ContactsFile.readlines()
     count = len([line for line in lines if line.strip()])  # Count non-empty lines
     ContactsFile.close()

     self.talk(f"Boss showing the {count} contacts stored in our database")

     ContactsFile = open("Contacts.txt", "r")
     for line in ContactsFile:
         s = line.strip().split("\"")
         if len(s) >= 4:  # Ensure there are enough parts
             print("Name: " + s[1])
             print("Number: " + s[3])
         else:
             print(f" {line.strip()}")
     ContactsFile.close()


    #search contact
    def NameIntheContDataBase(self,command):
        line = command
        line = line.split("number in contacts")[0]
        if("tell me" in line):
            name = line.split("tell me")[1]
            name = name.strip()
        else:
            name= line.strip()
        name,number,bo = self.SearchCont(name)
        if bo:
            print(f"Contact Match Found in our data base with {name} and the mboile number is {number}")
            self.talk(f"Boss Contact Match Found in our data base with {name} and the mboile number is {number}")
        else:
            self.talk("Boss the name not found in our data base, shall I add the contact")
            AddOrNot = self.listen_Command()
            print(AddOrNot)
            if ("yes add it" in AddOrNot)or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                self.AddContact()
                self.talk(f'Boss, Contact registered Successfully')
            elif("no" in AddOrNot) or ("don't register" in AddOrNot):
                self.talk('Ok Boss')

    #Internet spped
    def InternetSpeed(self):
     try:
        self.talk("Wait a few seconds, boss, checking your internet speed")
        st = speedtest.Speedtest()
        
        # Measure download and upload speeds
        dl = st.download() * 8 / 1000000  # Convert to Mbps
        up = st.upload() * 8 / 1000000  # Convert to Mbps
        
        # Round speeds to two decimal places
        dl = round(dl, 2)
        up = round(up, 2)
        
        print(f"Download: {dl} Mbps, Upload: {up} Mbps")
        self.talk(f"Boss, we have {dl} megabits per second downloading speed and {up} megabits per second uploading speed")
     except Exception as e:
        print(f"Error: {e}")
        self.talk("Sorry boss, I couldn't check the internet speed. Please check your connection or try again later.")

   
    #Search for a process how to do
    def How(self):
        self.talk("How to do mode is is activated")
        while True:
            self.talk("Please tell me what you want to know")
            how = self.listen_Command()
            try:
                if ("exit" in how) or("close" in how):
                    self.talk("Ok sir how to mode is closed")
                    break
                else:
                    max_result=1
                    how_to = search_wikihow(how,max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    self.talk(how_to[0].summary)
            except Exception as e:
                self.talk("Sorry sir, I am not able to find this")

    #Communication commands
    def comum(self,command):
        print(command)
        if ('hi'in command) or('hai'in command) or ('hey'in command) or ('hello' in command) :
            self.talk("Hello boss what can I help for u")
        else :
            self.No_result_found()

    #Fun commands to interact with chipher
    def Fun(self,command):
        #print(command)
        if 'your name' in command:
            self.talk("My name is cypher")
        elif 'my name' in command:
            self.talk("your name is om")
        elif 'university name' in command:
            self.talk("you are studing in Pro.Ram Meghe College Of Engineering And Management, with batchelor in Computer Science and Engineering") 
        elif 'what can you do' in command:
            self.talk("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
        elif 'your age' in command:
            self.talk("I am very young that u")
        elif 'date' in command:
            self.talk('Sorry not intreseted, I am having headache, we will catch up some other time')
        elif 'are you single' in command:
            self.talk('No, I am in a relationship with wifi')
        elif 'joke' in command:
            self.talk(pyjokes.get_joke())
        elif 'are you there' in command:
            self.talk('Yes boss I am here')
        elif 'tell me something' in command:
            self.talk('boss, I don\'t have much to say, you only tell me someting i will give you the company')
        elif 'thank you' in command:
            self.talk('boss, I am here to help you..., your welcome')
        elif 'in your free time' in self.command:
            self.talk('boss, I will be listening to all your words')
        elif 'i love you' in command:
            self.talk('I love you too boss')
        elif 'can you hear me' in command:
            self.talk('Yes Boss, I can hear you')
        elif 'do you ever get tired' in command:
            self.talk('It would be impossible to tire of our conversation')
        else :
            self.No_result_found()

    #Social media accounts commands
   # def social(self,command):
    #    print(command)
     #   if 'facebook' in command:
      #      self.talk('opening your facebook')
       #     webbrowser.open('https://www.facebook.com/')
        #elif 'whatsapp' in command:
         #   self.talk('opening your whatsapp')
          #  webbrowser.open('https://web.whatsapp.com/')
        #elif 'instagram' in command:
         #   self.talk('opening your instagram')
         #   webbrowser.open('https://www.instagram.com/')
        #elif 'twitter' in command:
         #   self.talk('opening your twitter')
          #  webbrowser.open('https://twitter.com/Suj8_116')
        #elif 'discord' in command:
         #   self.talk('opening your discord')
          #  webbrowser.open('https://discord.com/channels/@me')
        #else :
         #   self.No_result_found()
        
    #clock commands
    def Clock_time(self,command):
        #print(command)
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        self.talk("Current time is "+time)
    
    #calender day
    def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        
        return day_of_the_week
    
    def my_ip_address(self):
     ip = get('https://api.ipify.org').text
     self.talk(f"Your IP address is {ip}")


    #shedule function for remembering todays plans
    #NOTE For example I have declared my college timetable you can declare anything you want
    def shedule(self):
        day = self.Cal_day().lower()
        self.talk("Boss today's shedule is")
        Week = {"monday" : "Boss from 9:00 to 9:50 you have Cultural class, from 10:00 to 11:50 you have mechanics class, from 12:00 to 2:00 you have brake, and today you have sensors lab from 2:00",
        "tuesday" : "Boss from 9:00 to 9:50 you have English class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have ELectrical class, from 1:00 to 2:00 you have brake, and today you have biology lab from 2:00",
        "wednesday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have mechanics class, from 12:00 to 12:50 you have cultural class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00",
        "thrusday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Maths class, from 11:00 to 12:50 you have sensors class, from 1:00 to 2:00 you have brake, and today you have english lab from 2:00",
        "friday" : "Boss today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have computer lab from 2:00",
        "saturday" : "Boss today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00",
        "sunday":"Boss today is holiday but we can't say anything when they will bomb with any assisgnments"}
        if day in Week.keys():
            self.talk(Week[day])

    #college resources commands
   # #NOTE Below are some dummy links replace with your college website links
    #def college(self,command):
     #   print(command)
      #  if 'teams' in command:
       #     self.talk('opening your microsoft teams')
        #    webbrowser.open('https://teams.microsoft.com/')
        #elif 'stream' in command:
         #   self.talk('opening your microsoft stream')
          #  webbrowser.open('https://web.microsoftstream.com/')
        #elif 'outlook' in command:
         #   self.talk('opening your microsoft school outlook')
          #  webbrowser.open('https://outlook.office.com/mail/')
       # elif 'amrita portal' in command:
        #    self.talk('opening your amrita university management system')
         #   webbrowser.open('https://aumsam.amrita.edu/')
       # elif 'octave' in command:
        #    self.talk('opening Octave online')
         #   webbrowser.open('https://octave-online.net/')
        #else :
         #   self.No_result_found()
    
    #Online classes
    #def OnlineClasses(self,command):
     #   print(command)
      #  #Keep as many "elif" statemets based on your subject Eg: I have kept a dummy links for JAVA and mechanics classes link of MS Teams
       # if("java" in command):
        #    self.talk('opening DSA class in teams')
         #   webbrowser.open("https://teams.microsoft.com/java")
        #elif("python" in command):
         #   self.talk('opening mechanics class in teams')
          #  webbrowser.open("https://teams.microsoft.com/mechanics")
        #elif 'online classes' in command:
         #   self.talk('opening your microsoft teams')
          #  webbrowser.open('https://teams.microsoft.com/')

    #Brower Search commands
    def B_S(self,command):
       # print(command)
        try:
            # ('what is meant by' in self.command) or ('tell me about' in self.command) or ('who the heck is' in self.command)
            if ('wikipedia' in command):
                target1 = command.replace('search for','')
                target1 = target1.replace('in wikipedia','')
            elif('what is' in command):
                target1 = command.replace("what is meant by"," ")
            elif('tell me about' in command):
                target1 = command.replace("tell me about"," ")
            elif('who the heck is' in command):
                target1 = command.replace("who is"," ")
            elif('search'in command):
             target1 = command.replace('in wikipedia','')    
             print("searching....")
            elif('search for'in command):
             target1 = command.replace('in wikipedia','')    
             print("searching....")
            info = wikipedia.summary(target1,5)
            print(info)
            self.talk("according to wikipedia "+info)
        except :
            self.No_result_found()
        
    #Browser
    def brows(self, command):
        print(f"Command received: {command}")

        if 'google' in command.lower():
            self.talk("Boss, what should I search on Google?")
            search_query = self.listen_Command()  # Take user input for the search query
            if search_query.strip():  # Ensure input is not empty
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                self.talk("You didn't specify anything to search.")
        elif 'edge' in command.lower():
            self.talk("Opening Microsoft Edge for you...")
            try:
                # Replace the path with the actual path to your Edge executable
                os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            except FileNotFoundError:
                self.talk("Sorry, I couldn't find Microsoft Edge on your system.")
        else:
            self.No_result_found()

    #google applications selection
    #if there is any wrong with the URL's replace them with your browsers URL's
    #def Google_Apps(self,command):
     #   print(command)
      #  if 'gmail' in command:
       #     self.talk('opening your google gmail')
        #    webbrowser.open('https://mail.google.com/mail/')
        #elif 'maps' in command:
         #   self.talk('opening google maps')
          #  webbrowser.open('https://www.google.co.in/maps/')
        #elif 'news' in command:
         #   self.talk('opening google news')
          #  webbrowser.open('https://news.google.com/')
        #elif 'calendar' in command:
         #   self.talk('opening google calendar')
          #  webbrowser.open('https://calendar.google.com/calendar/')
        #elif 'photos' in command:
         #   self.talk('opening your google photos')
          #  webbrowser.open('https://photos.google.com/')
        #elif 'documents' in command:
         #   self.talk('opening your google documents')
          #  webbrowser.open('https://docs.google.com/document/')
        #elif 'spreadsheet' in command:
         #   self.talk('opening your google spreadsheet')
          #  webbrowser.open('https://docs.google.com/spreadsheets')
        #elif 'drive' in command:
         #   self.talk('opening your google drive')
          #  webbrowser.open('https://drive.google.com/drive/my-drive')  
        #elif 'sharepoint' in command:
         #   self.talk('opening your sharepoint')
          #  webbrowser.open('https://www.microsoft.com/en-in/microsoft-365/sharepoint/')      
        #else :
         #   self.No_result_found()
            
    #youtube
    def yt(self,command):
        print(command)
        if 'play' in command:
            self.talk("Boss can you please say the name of the song")
            song = self.listen_Command()
            if "play" in song:
                song = song.replace("play","")
            self.talk('playing '+song)
           # print(f'playing {song}')
            pywhatkit.playonyt(song)
            print('playing')
        elif "download" in command:
            self.talk("Boss please enter the youtube video link which you want to download")
            link = input("Enter the YOUTUBE video link: ")
            yt=YouTube(link)
            yt.streams.get_highest_resolution().download()
            self.talk(f"Boss downloaded {yt.title} from the link you given into the main folder")
        elif 'youtube' in command:
            self.talk('opening your youtube')
            webbrowser.open('https://www.youtube.com/')
        else :
            self.No_result_found()
        
    #Opensource accounts
  #  def open_source(self,command):
   #     print(command)
    #    if 'github' in command:
     #       self.talk('opening your github')
      #      webbrowser.open('https://github.com/ombobade1')
       # elif 'gitlab' in command:
        #    self.talk('opening your gitlab')
         #   webbrowser.open('https://gitlab.com/-/profile')
        #else :
         #   self.No_result_found()

    #Photo shops
    def edit(self,command):
        print(command)
        if 'slides' in command:
            self.talk('opening your google slides')
            webbrowser.open('https://docs.google.com/presentation/')
        elif 'canva' in command:
            self.talk('opening your canva')
            webbrowser.open('https://www.canva.com/')
        else :
            self.No_result_found()

    #OTT 
    def OTT(self,command):
        print(command)
        if 'hotstar' in command:
            self.talk('opening your disney plus hotstar')
            webbrowser.open('https://www.hotstar.com/in')
        elif 'prime' in command:
            self.talk('opening your amazon prime videos')
            webbrowser.open('https://www.primevideo.com/')
        elif 'netflix' in command:
            self.talk('opening Netflix videos')
            webbrowser.open('https://www.netflix.com/')
        else :
            self.No_result_found()

    #PC allications
    #NOTE: place the correct path for the applications from your PC there may be some path errors so please check the applications places
    #if you don't have any mentioned applications delete the codes for that
    #I have placed applications path based on my PC path check while using which OS you are using and change according to it
    #def OpenApp(self,command):
        #print(command)
        #if ('calculator'in command) :
          #  self.talk('Opening calculator')
         #   os.startfile('C:\\Windows\\System32\\calc.exe')
        #elif ('paint'in command) :
          #  self.talk('Opening msPaint')
         #   os.startfile('c:\\Windows\\System32\\mspaint.exe')
        #elif ('notepad'in command) :
          #  self.talk('Opening notepad')
         #   os.startfile('c:\\Windows\\System32\\notepad.exe')
        #elif ('discord'in command) :
          #  self.talk('Opening discord')
         #   os.startfile('..\\..\\Discord.exe')
        #elif 'editor' in command:
          #  self.talk('Opening your Visual Studio Code')
         #   os.startfile("C:/Users/ASUS/Desktop/Visual Studio Code.lnk")
        #elif ('online classes'in command) :
          #  self.talk('Opening your Microsoft teams')
         #   webbrowser.open('https://teams.microsoft.com/')
        #elif ('spotify'in command) :
          #  self.talk('Opening spotify')
         #   os.startfile("C:\\Users\\ASUS\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe")
            
        #elif ('lt spice'in command) :
          #  self.talk('Opening lt spice')
         #   os.startfile("..\\..\\XVIIx64.exe")
        #elif ('steam'in command) :
          #  self.talk('Opening steam')
         #   os.startfile("..\\..\\steam.exe")
        #elif ('media player'in command) :
          #  self.talk('Opening VLC media player')
         #   os.startfile("C:\Program Files\VideoLAN\VLC\vlc.exe")
        #elif ('wordpad' in command):
          #   self.talk('Opening WordPad')
         #    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        #elif ('powerpoint' in command):
          #    self.talk('Opening Microsoft PowerPoint')
         #     os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")  # Replace XX with your Office version
        #elif ('excel' in command):
          #   self.talk('Opening Microsoft Excel')
         #    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")  # Replace XX with your Office version
        #elif ('wifi' in command):
          #   self.talk('Opening Wi-Fi settings')
         #    os.startfile('control.exe /name Microsoft.NetworkAndSharingCenter')
        #elif ('bluetooth' in command):
          #   self.talk('Opening Bluetooth settings')
         #    os.startfile('ms-settings:bluetooth') 
        #else :
          #  self.No_result_found()
            
    #closeapplications function
    #def CloseApp(self,command):
        #print(command)
        #if ('calculator'in command) :
          #  self.talk("okay boss, closeing calculator")
         #   os.system("taskkill /f /im calc.exe")
        #elif ('paint'in command) :
          #  self.talk("okay boss, closeing mspaint")
         #   os.system("taskkill /f /im mspaint.exe")
        #elif ('notepad'in command) :
          #  self.talk("okay boss, closeing notepad")
         #   os.system("taskkill /f /im notepad.exe")
        #elif ('discord'in command) :
          #  self.talk("okay boss, closeing discord")
         #   os.system("taskkill /f /im Discord.exe")
        #elif ('editor'in command) :
          #  self.talk("okay boss, closeing vs code")
         #   os.system("taskkill /f /im Code.exe")
        #elif ('spotify'in command) :
          #  self.talk("okay boss, closeing spotify")
         #   subprocess.run(["taskkill", "/f", "/im", "Spotify.exe"], check=True)
        #elif ('lt spice'in command) :
          #  self.talk("okay boss, closeing lt spice")
         #   os.system("taskkill /f /im XVIIx64.exe")
        #elif ('steam'in command) :
          #  self.talk("okay boss, closeing steam")
         #   os.system("taskkill /f /im steam.exe")
        #elif ('media player'in command) :
          #  self.talk("okay boss, closeing media player")
         #   os.system("taskkill /f /im vlc.exe")
        #elif ('wordpad' in command):
          #  self.talk("Okay boss, closing WordPad")
         #   os.system("taskkill /f /im WINWORD.EXE")
        #elif ('powerpoint' in command):
          #  self.talk("Okay boss, closing PowerPoint")
         #   os.system("taskkill /f /im POWERPNT.EXE")
        #elif ('excel' in command):
          #  self.talk("Okay boss, closing Excel")
         #   os.system("taskkill /f /im EXCEL.EXE")
        #elif ('wifi' in command):
         #   self.talk("Boss, Wi-Fi settings cannot be closed directly as it is a control panel setting.")
        #elif ('bluetooth' in command):
          #  self.talk("Okay boss, turning off Bluetooth")
         #   os.system('powershell -Command "Start-Process powershell -ArgumentList \'-Command Disable-Bluetooth\' -Verb runAs"')    
        #else :
          #  self.No_result_found()

    #Shopping links
    #def shopping(self,command):
     #   print(command)
      #  if 'flipkart' in command:
       #     self.talk('Opening flipkart online shopping website')
        #    webbrowser.open("https://www.flipkart.com/")
        #elif 'amazon' in command:
         #   self.talk('Opening amazon online shopping website')
          #  webbrowser.open("https://www.amazon.in/")
        #elif 'meesho' in command:
         #   self.talk('Opening meesho online shopping website')
          #  webbrowser.open("https://www.meesho.com/")    
        #else :
         #   self.No_result_found()

    #PDF reader
    def pdf_reader(self):
     try:
        self.talk("Boss, enter the name or path of the book you want me to read.")
        n = input("Enter the book name or full path (with or without .pdf): ").strip()
        
        # Ensure the file has a .pdf extension
        if not n.lower().endswith(".pdf"):
            n += ".pdf"
        
        # Check if the file exists
        if not os.path.exists(n):
            self.talk("Sorry boss, I couldn't find the book. Please check the name or path and try again.")
            return
        
        # Open the PDF file
        with open(n, 'rb') as book_n:
            pdfReader = PyPDF2.PdfReader(book_n)
            pages = len(pdfReader.pages)
            
            self.talk(f"Boss, there are a total of {pages} pages in this book.")
            print(f"Total Pages: {pages}")
            
            self.talk("Please enter the page number you want me to read.")
            num = int(input("Enter the page number: "))
            
            if num < 1 or num > pages:
                self.talk("Sorry boss, the page number is out of range. Please try again.")
                return
            
            # Extract and read the page content
            page = pdfReader.pages[num - 1]  # Page numbers are 0-based
            text = page.extract_text()
            
            if not text.strip():
                self.talk("Boss, the page appears to be empty or contains non-readable text.")
            else:
                print(text)
                self.talk(text)
     except FileNotFoundError:
        self.talk("Sorry boss, I couldn't find the book. Please check the file name and try again.")
     except ValueError:
        self.talk("Invalid input. Please enter a valid page number.")
     except Exception as e:
        self.talk(f"An error occurred: {e}")


    #Time caliculating algorithm
    def silenceTime(self,command):
       # print(command)
        x=0
        #caliculating the given time to seconds from the speech commnd string
        if ('10' in command) or ('ten' in command):x=600
        elif '1' in command or ('one' in command):x=60
        elif '2' in command or ('two' in command):x=120
        elif '3' in command or ('three' in command):x=180
        elif '4' in command or ('four' in command):x=240
        elif '5' in command or ('five' in command):x=300
        elif '6' in command or ('six' in command):x=360
        elif '7' in command or ('seven' in command):x=420
        elif '8' in command or ('eight' in command):x=480
        elif '9' in command or ('nine' in command):x=540
        self.silence(x)
        
    #Silence
    def silence(self,k):
        t = k
        s = "Ok boss I will be silent for "+str(t/60)+" minutes"
        self.talk(s)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.talk("Boss "+str(k/60)+" minutes over")

    #Mail verification
    import smtplib

    def verifyMail(self):
     try:
         self.talk("What should I say in the email?")
         content = self.listen_Command()
 
         self.talk("To whom do you want to send the email? Please provide the email address.")
         to = self.listen_Command()  # fixed typo
 
         self.SendEmail(to, content)
         self.talk("Email has been sent to " + str(to))
 
     except Exception as e:
         print("Email Error:", e)
         self.talk("Sorry boss, I am not able to send the email.")

    def SendEmail(self, to, content):
     sender_email = "ombobade11@gmail.com"
     sender_password = "OMbobade1234567890@#"  # Use app password, not regular password!

     try:
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.ehlo()
         server.starttls()
         server.login(sender_email, sender_password)
         server.sendmail(sender_email, to, content)
         server.quit()
         print("Email sent to:", to)
     except Exception as e:
         print("SMTP Error:", e)
         raise

    #location
    def locaiton(self):
        self.talk("Wait boss, let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            self.talk(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
            self.talk(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            self.talk("Sorry boss, due to network issue i am not able to find where we are.")
            pass

    #Instagram profile
    def Instagram_Pro(self):
        self.talk("Boss please enter the user name of Instagram: ")
        name = input("Enter username here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        time.sleep(5)
        self.talk("Boss would you like to download the profile picture of this account.")
        cond = self.listen_Command()
        if('download' in cond):
            mod = instaloader.Instaloader()
            mod.download_profile(name,profile_pic_only=True)
            self.talk("I am done boss, profile picture is saved in your main folder. ")
        else:
            pass

    #ScreenShot
    def scshot(self):
      try:
         # Ask for the file name
         self.talk("Boss, please tell me the name for this screenshot file.")
         name = self.listen_Command().strip()

        
         if not name:
             self.talk("Sorry boss, I didn't get a name. Using 'screenshot' as default.")
             name = "screenshot"
        
         # Specify the folder to save screenshots
         save_folder = "Screenshots"
         if not os.path.exists(save_folder):
             os.makedirs(save_folder)
         
         # Confirm the action and take the screenshot
         self.talk("Please hold the screen for a few seconds, boss. I am taking the screenshot.")
         time.sleep(3)
         img = pyautogui.screenshot()
        
         # Save the screenshot
         file_path = os.path.join(save_folder, f"{name}.png")
         img.save(file_path)
        
         self.talk(f"I am done, boss. The screenshot is saved as {file_path}.")
         print(f"Screenshot saved at: {file_path}")
    
      except Exception as e:
         self.talk(f"Sorry boss, I couldn't take the screenshot. Error: {e}")


    #News
    def news(self):
        MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="#need your api keys
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth'] #If you need more than ten you can extend it in the list
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
           # print(f"todays {seq[i]} news is: {headings[i]}")
            self.talk(f"todays {seq[i]} news is: {headings[i]}")
        self.talk("Boss I am done, I have read most of the latest news")

    #System condition
    def condition(self):
        usage = str(psutil.cpu_percent())
        self.talk("CPU is at"+usage+" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        self.talk(f"Boss our system have {percentage} percentage Battery")
        if percentage >=75:
            self.talk(f"Boss we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            self.talk(f"Boss we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            self.talk(f"Boss we don't have enough power to work, please connect to charging")
        else:
            self.talk(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")

            
            
        
    #no result found
    def No_result_found(self):
        self.talk('Boss I couldn\'t understand, could you please say it again.')    

startExecution = MainThread()

def resource_path(relative_path):
    """ Get path to resource (image, gif, etc.), works for dev and PyInstaller .exe """
    if getattr(sys, 'frozen', False):  # Running in a PyInstaller bundle
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Main(QMainWindow):
    cpath =""
    def __init__(self,path):
        self.cpath = path
        super().__init__()
        self.ui = Ui_chipherUI(path=current_path)
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)

        
    
    #NOTE make sure to place a correct path where you are keeping this gifs
    def startTask(self):
#        self.label.setPixmap(QtGui.QPixmap(resource_path("UI/bg2.gif")))
        self.ui.label.setPixmap(QtGui.QPixmap(resource_path("UI/bg2.gif")))
        self.ui.movie = QMovie(resource_path("UI/bg2.gif"))

# Set the movie on the label
        self.ui.label.setMovie(self.ui.movie)

# Start the animation
        self.ui.movie.start()

       # self.ui.label.setMovie(self.ui.movie)
        #self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ringJar.mp4")
        #self.ui.label_3.setMovie(self.ui.movie)
        #self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\circle.gif")
        #self.ui.label_4.setMovie(self.ui.movie)
        #self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\lines1.gif")
        #self.ui.label_7.setMovie(self.ui.movie)
        #self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman3.gif")
        #self.ui.label_8.setMovie(self.ui.movie)
        #self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\circle.gif")
        #self.ui.label_9.setMovie(self.ui.movie)
        #self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\powersource.gif")
        #self.ui.label_12.setMovie(self.ui.movie)
        #self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\powersource.gif")
        #self.ui.label_13.setMovie(self.ui.movie)
        #self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman3_flipped.gif")
       # self.ui.label_16.setMovie(self.ui.movie)
        #self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

current_path = os.getcwd()
app = QApplication(sys.argv)
chipher = Main(path=current_path)
chipher.show()
QtWidgets.QApplication.instance().quit
sys.exit(app.exec_())









#python -m PyInstaller --onefile CIPHER.py

# pyinstaller --onefile CIPHER.py
#pyinstaller --onefile --add-data "Ui;Ui" CIPHER.py
