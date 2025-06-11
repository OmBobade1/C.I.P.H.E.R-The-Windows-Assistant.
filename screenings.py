#import datetime
#from PIL import ImageGrab
#import numpy as np
#import cv2
#import pyaudio
#import wave
#import subprocess
#import pyautogui
#import os
#import msvcrt  # Windows-specific library

#def Recordings(option):
    #try:
        # Setup file paths with timestamp
    #    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
   #     base_dir = "C:\\Users\user\\Videos"
  #      video_dir = os.path.join(base_dir, "Screen")
 #       audio_dir = os.path.join(base_dir, "Audio")
#        output_dir = os.path.join(base_dir, "SCREENRECORDED")

        #os.makedirs(video_dir, exist_ok=True)
        #os.makedirs(audio_dir, exist_ok=True)
        #os.makedirs(output_dir, exist_ok=True)

        #VideoFile_name = os.path.join(video_dir, f"VideoFile-{time_stamp}.mp4")
        #AudioFile_name = os.path.join(audio_dir, f"AudioFile-{time_stamp}.wav")
        #OutputFileName = os.path.join(output_dir, f"VideoFile-{time_stamp}.mp4")

        # Initialize audio
        #audio = pyaudio.PyAudio()
        #frames = []
        #stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

       # if "screen recording" in option.lower():
      #      ScreenRecording(audio, VideoFile_name, AudioFile_name, OutputFileName, frames, stream)
     #   elif "voice recording" in option.lower():
    #        VoiceRecording(stream, frames, AudioFile_name, audio)
   #     else:
  #          print("Invalid option. Please choose 'screen recording' or 'voice recording'.")
 #   except Exception as e:
 #       print(f"An error occurred: {e}")

#def ScreenRecording(audio, VideoFile_name, AudioFile_name, OutputFileName, frames, stream):
    #try:
        #print("Screen Recording has been started.")
        #print("Press the key 'q' to stop screen recording.")

        #width, height = pyautogui.size()
        #fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        #captured_video = cv2.VideoWriter(VideoFile_name, fourcc, 20.0, (width, height))

        #while True:
            #img = ImageGrab.grab(bbox=(0, 0, width, height))
            #image_np = np.array(img)
            #final_img = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
           # captured_video.write(final_img)

            # Exit condition
          #  if msvcrt.kbhit() and ord(msvcrt.getch()) == ord('q'):
         #       break

        #stream.stop_stream()
        #stream.close()
        #audio.terminate()
       # VoiceEnd(AudioFile_name, audio, frames)
      #  captured_video.release()

        # Merge video and audio using ffmpeg
     #   cmd = f'ffmpeg -y -i "{VideoFile_name}" -i "{AudioFile_name}" -c:v copy -c:a aac "{OutputFileName}"'
    #    subprocess.call(cmd, shell=True)
   #     print(f"Screen Recording has ended. Saved as {OutputFileName}")

  #  except Exception as e:
 #       print(f"An error occurred during screen recording: {e}")

#def VoiceCapture(stream, frames):
    #ry:
    #    data = stream.read(1024)
   #     frames.append(data)
  #  except Exception as e:
 #       print(f"An error occurred while capturing voice: {e}")

#def VoiceEnd(AudioFile_name, audio, frames):
    #try:
        #with wave.open(AudioFile_name, "wb") as sound_file:
       #     sound_file.setnchannels(1)
      #      sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
     #       sound_file.setframerate(44100)
    #        sound_file.writeframes(b''.join(frames))
   #     print(f"Audio saved as {AudioFile_name}")
  #  except Exception as e:
 #       print(f"An error occurred while saving audio: {e}")

#def VoiceRecording(stream, frames, AudioFile_name, audio):
    #try:
        #print("Voice Recording has been started.")
        #print("Press the key 'q' to stop voice recording.")
        
        #while True:
           # VoiceCapture(stream, frames)

          #  if msvcrt.kbhit() and ord(msvcrt.getch()) == ord('q'):
         #       break

        #stream.stop_stream()
        #stream.close()
       # audio.terminate()
      #  VoiceEnd(AudioFile_name, audio, frames)
     #   print("Voice Recording has ended.")
    #except Exception as e:
       # print(f"An error occurred during voice recording: {e}")


import datetime
import cv2
import numpy as np
import pyaudio
import wave
import subprocess
import pyautogui
import os
import keyboard
from PIL import ImageGrab
import threading
import time

def RecordScreen(output_video, stop_event, start_time):
    width, height = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    captured_video = cv2.VideoWriter(output_video, fourcc, 20.0, (width, height))

    print("Screen Recording started. Press 'escape' to stop.")
    
    while not stop_event.is_set():
        current_time = time.time()
        if current_time >= start_time:
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            frame = np.array(img)
            final_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            captured_video.write(final_frame)
    
    captured_video.release()
    print(f"Screen recording saved as {output_video}")

def RecordAudio(output_audio, stop_event, start_time):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []
    
    print("Audio Recording started. Press 'escape' to stop.")
    
    while not stop_event.is_set():
        current_time = time.time()
        if current_time >= start_time:
            data = stream.read(1024)
            frames.append(data)
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    with wave.open(output_audio, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
    
    print(f"Audio recording saved as {output_audio}")

def StartRecording(option):
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    base_dir = os.path.join(os.path.expanduser("~"), "Videos")

    video_dir = os.path.join(base_dir, "Screen")
    audio_dir = os.path.join(base_dir, "Audio")
    output_dir = os.path.join(base_dir, "SCREENRECORDED")
    
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    video_file = os.path.join(video_dir, f"VideoFile-{time_stamp}.mp4")
    audio_file = os.path.join(audio_dir, f"AudioFile-{time_stamp}.wav")
    output_file = os.path.join(output_dir, f"VideoFile-{time_stamp}.mp4")
    
    stop_event = threading.Event()
    start_time = time.time() + 0.5  # Ensure both audio and video start at the same time
    
    if "screen recording" in option.lower():
        video_thread = threading.Thread(target=RecordScreen, args=(video_file, stop_event, start_time))
        audio_thread = threading.Thread(target=RecordAudio, args=(audio_file, stop_event, start_time))
        
        video_thread.start()
        audio_thread.start()
        
        keyboard.wait('escape')  # Wait for 'escape' key press
        stop_event.set()
        
        video_thread.join()
        audio_thread.join()
        
        # Merge video and audio using ffmpeg with sync adjustment
        cmd = f'ffmpeg -y -itsoffset 0.5 -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac "{output_file}"'
        subprocess.call(cmd, shell=True)
        print(f"Screen recording saved as {output_file}")
    
    elif "voice recording" in option.lower():
        audio_thread = threading.Thread(target=RecordAudio, args=(audio_file, stop_event, start_time))
        
        audio_thread.start()
        keyboard.wait('escape')  # Wait for 'escape' key press
        stop_event.set()
        
        audio_thread.join()
    
    else:
        print("Invalid option. Choose 'screen recording' or 'voice recording'.")

