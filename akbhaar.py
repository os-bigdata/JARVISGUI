from win32com.client import Dispatch
# import request

import json
import requests
# parsed = json.loads(s.text)

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Today's news... begins")
    s = requests.get("https://newsapi.org/v2/everything?q=apple&from=2021-08-01&to=2021-08-01&sortBy=popularity&apiKey=75678af080f141cbbfbefb0cf8c8cb36").text
    str = json.loads(s)
    # speak(str)
    print(str["articles"])
    arts = str["articles"]
    for article in arts:
        speak(article["title"])
        speak("Moving on to next news")

