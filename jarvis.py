import os
from time import strftime
import requests
from subprocess import Popen, PIPE
import sys
import tkinter
import threading
from tkinter import *
from PIL import Image
import PIL.Image
import datetime
import random
import webbrowser
import os
import pyttsx3
import speech_recognition as sr
import subprocess
import pyjokes
import datetime
import random
from tkinter import Image
import webbrowser
import os
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import pyjokes
import requests
import subprocess
import ctypes
from decouple import config
from email.message import EmailMessage
import time
import ecapture as ec
from pywikihow import WikiHow, search_wikihow
import pywhatkit
import pyaudio
from vosk import Model, KaldiRecognizer
import sys
import PyPDF2
import json
from urllib.request import urlopen
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
x = random.randint(0, 1)
# print(voices[x].id)
# print(x)
engine.setProperty("voice", voices[x].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening! sir")
        print("Computer: Good Evening! sir")
    if x == 0:
        speak(f"I am your assistant Jarvis. How can i help you?\n")
    elif x == 1:
        speak("I am your assistant Zira. How can i help you?\n")
    else:
        speak("I am your assistant Zira. How can i help you?\n")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)

    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language="en-in")
        print(f"User said: {query1}\n")

    except Exception as er:
        print(er)
        print("Sorry I can't hear that.")
        return "None"
    return query1

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is", "")
    query = query.replace("how to", "")
    query = query.replace("what do you mean by", "")
    query = query.replace("who is the", "")
    

    Query = str(term)
    pywhatkit.search(Query)

    if "how to" in Query:
        m_res = 1
        how_to_func = search_wikihow(query=Query,max_results=m_res)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        speak(how_to_func[0].summary)
        # print(how_to_func[0].summary)

    
    else:
        search = wikipedia.summary(Query, 2)
        speak(f": According to Your Search : {search}")
        print(f": According to Your Search : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    webbrowser.open(result)
    
    speak("This is what i found for you in the search")
    
    pywhatkit.playonyt(term)

    speak("This may also help you.")

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

def pdf_rer():
    try:
        book = open("C:\\Users\\sonas\\Documents\\SIST_BE_40731100_SMI SHAMSHUDDIN.pdf","rb")
        pR = PyPDF2.PdfFileReader(book)
        p = pR.numPages
        speak(f"Total Number of pages in this book is {p}")
        print(f"Total Number of pages in this book is {p}")
        speak("sir please say the page number i have to read")
        pg = int(takeCommand())
        pa = pR.getPage(pg)
        text = pa.extractText()
        speak(text)
        print(text)
    except Exception as e:
        return None

def audiototext():
    model = Model(r"F:\PyCharm Community Edition 2021.1.3\pyprog\vosk-model-en-in-0.5")
    rec = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while 1:
        data = stream.read(4096)

        if rec.AcceptWaveform(data):
            text = rec.Result()
            p = text[14:-3]
            print(p)

            if p == 'exit':
                break

def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        
        return day_of_the_week 

def condition():
        usage = str(psutil.cpu_percent())
        speak("CPU is at"+usage+" percentage")
        print("CPU is at"+usage+" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        speak(f"our system have {percentage} percentage Battery")
        print(f"our system have {percentage} percentage Battery")
        if percentage >=75:
            speak(f"we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            speak(f"we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            speak(f"we don't have enough power to work, please connect to charging")
        else:
            speak(f"we have very low power, please connect to charging otherwise the system will shutdown very soon")

class redirect():
    def __init__(self,widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll
    
    def write(self,text):
        self.widget.insert('end',text)
        if self.autoscroll:
            self.widget.see('end')
    
    def flush(self):
        pass

def run():
    threading.Thread(target=Task).start()

def Task():
    clear = lambda: os.system('cls')
    clear()
    wish_me()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia: ")
            print(results)
            speak(results)

        elif "search google" in query:
            # query = query.replace("search google","")
            GoogleSearch(query)

        elif "youtube search" in query:
            YouTubeSearch(query)
        
        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org//v1//articles?source=the-times-of-india&sortBy=top&apiKey=e9a27aa4e76c49d4850fd9b38f071350''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== THE NEWS ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
            

        # elif "open google" in query:
        #     webbrowser.open("www.google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open duckduckgo" in query:
            webbrowser.open("www.duckduckgo.com")

        # elif "quran" in query:
        #     webbrowser.open("https://www.youtube.com/playlist?list=PLuM8gIEBe3i6iGPwZyFDu7ElEHWmyGm-v")

        elif "audio to text" in query:
            audiototext()

        elif "play music" in query:
            music_direc = "C:\\Users\\91950\\Music\\music_direc"
            songs = os.listdir(music_direc)
            print(songs)
            y = random.randint(0, len(songs) - 1)
            # print(y)
            os.startfile(os.path.join(music_direc, songs[y]))

        elif "play video" in query:
            vid_dir = "C:\\Users\\sonas\\Videos\\Video"
            vid = os.listdir(vid_dir)
            print(vid)
            z = random.randint(0, len(vid) - 1)
            # print(y)
            os.startfile(os.path.join(vid_dir, vid[z]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir the time is {strTime}")
        
        elif "day" in query:
            Cal_day()

        elif "open code" in query:
            codePath = "D:\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif "open whatsapp" in query:
            whatsPath = "C:\\Users\\91950\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsPath)

        elif "open tor" in query:
            torPath = "D:\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(torPath)
        
        # elif "my location" or " where am i" in query:
            # from Features import my_location
            # my_location()

        elif "where is" in query:
            from Features import GoogleMaps
            place = query.replace("where is","")
            GoogleMaps(place)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif "read the book" in query:
            pdf_rer()
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        
        # elif "take screenshot" or "take a screenshot" in query:
        #     speak("By what name do you want to save the screenshot?")
        #     name = takeCommand()
        #     speak("Alright, taking screenshot")
        #     img = pyautogui.screenshot()
        #     name = f"{name}.png"
        #     img.save(name)
        #     speak("screenshot hasbeen successfully captured")
        
        # elif "show me the screenshot" in query:
        #     img = Image.open()
        #     img.show(img)
        #     speak("Here it is")
        #     time.sleep(2)
        
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
            speak("Background changed successfully")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "send email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            print("On what email address do I send sir? Please enter in the console:")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            print("What should be the subject sir?")
            subject = takeCommand().capitalize()
            speak("What is the message sir?")
            message = takeCommand().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
                print("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail.")
                print("Something went wrong while I was sending the mail")
        
        elif "quit" in query:
            sys.exit()

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'a')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now()
                a = str(strTime)
                file.write(a)
                file.write(" :- ")
                file.write(note)
                file.write("\n")
            else:
                file.write(note)
                file.write("\n")

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "sleep" in query:
            speak("Okay sir!, I am going to sleep you can call me anytime")
            print("Okay sir!, I am going to sleep you can call me anytime")
            break

def guide_task():
    print(" ")
    print("Hey! There I am Jarvis")
    print("I can help you with variety of tasks")
    print(" ")

def guide_run():
    threading.Thread(target=guide_task).start()

screen_main = tkinter.Tk()
screen_main.configure(background='black')
# screen_main.attributes("-fullscreen",True)
# screen_main.iconbitmap("C:\\Users\\sonas\\Pictures\\jarvisUI5re.gif")

def color_changer():
    color = ['Green','Gold','silver','cyan','blue','magenta']
    act_color = random.choice(color)
    label.configure(foreground=act_color)
    label.after(1000,color_changer)

label = tkinter.Label(screen_main,font=('space age',30),background='black',text="Done by sona")
color_changer()
label.place(x=1550,y=40)

def time():
    stri = strftime("%H:%M:%S %p")
    label.config(text=stri)
    label.after(1000,time)
    min = strftime("%M")

label = Label(screen_main,font=('futura bold', 35),background="black",border="0",foreground="cyan")
label.place(x=10,y=40)
time()

file=r"C:\Users\sonas\Desktop\jarvispin2.gif"
info = PIL.Image.open(file)
frames = info.n_frames
im = [tkinter.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = screen_main.after(30,lambda :animation(count))

def stop_animation():
    screen_main.after_cancel(anim)

gif_label = tkinter.Label(screen_main,image="")
gif_label.configure(height=350,width=300,border="0",background='black')
gif_label.place(x=800,y=320)

def batt():
    label1 = Label(screen_main,text="Current Power Level at:",font=('arial',20),foreground="cyan",border='0',background="black")
    label1.place(x=1450,y=650)

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    per = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"

    str_bat = battery #
    str_per = per,"%"
    label2 = Label(screen_main,font=('arial',20),border='0',foreground="blue",background='black')
    label2.config(text=str_per)
    label2.place(x=1790,y=650)
    label2.after(10000,batt)
batt()

terminal = tkinter.Text(screen_main)
terminal.configure(background='black')
terminal.configure(width=60, height=30)
terminal.configure(font=('arial',10),fg='white')
terminal.place(x=0,y=200)
scrollbar = tkinter.Scrollbar(screen_main)
scrollbar.pack(side='right', fill='y')
terminal['yscrollcommand'] = scrollbar.set
scrollbar['command'] = terminal.yview
guide_run()
old_stdout = sys.stdout
sys.stdout = redirect(terminal)

initiate_btn = tkinter.Button(screen_main,font=("arial",25),foreground="cyan",background='black',text="Initiate",command=run)
initiate_btn.place(x=1490,y=900)
start = tkinter.Button(screen_main,font=("arial",25),foreground="cyan",background="black",text="start",command=lambda :animation(count))
start.place(x=1660,y=900)
# start.place(x=1200,y=800)
# stop = tkinter.Button(screen_main,text="stop",command=stop_animation)
# stop.pack()
screen_main.mainloop()
sys.stdout = old_stdout
