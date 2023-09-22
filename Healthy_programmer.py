from datetime import datetime
import time
from pygame import mixer


def musicloop(file, s):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == s:
            mixer.music.stop()
            break
def log_now(msg):
    with open("log.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n\n")

if __name__ == '__main__':
    t = time.localtime()
    c_time = time.strftime("%H:%M:%S", t)
    def officetime(time_off):
        init_water = time.time()
        init_eyes = time.time()
        init_exercise = time.time()
        watersec = 18
        excsec = 3000
        eyesec = 2400

        if time_off > '09:00:00' and time_off < '17:00:01':
            while True:
                if time.time() - init_water > watersec:
                    print("Enter Drank to stop alarm : ")
                    musicloop("Clock-sound-effect.mp3", "drank")
                    init_water = time.time()
                    log_now("Drank Water at :")
                if time.time() - init_eyes > eyesec:
                    print("Enter done1 to stop alarm for eye exercise : ")
                    musicloop("Rain-gutter-noise-relaxing-sound-of-water.mp3", "done1")
                    init_eyes = time.time()
                    log_now("Eyes relaxed at :")
                if time.time() - init_exercise > excsec:
                    print("Enter done2 to stop alarm for exercise : ")
                    musicloop("Rain-gutter-noise-relaxing-sound-of-water.mp3", "done2")
                    init_exercise = time.time()
                    log_now("Exercised at:")
        else:
            print("Not in office time")
    officetime(c_time)
