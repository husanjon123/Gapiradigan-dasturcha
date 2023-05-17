# MANBA Paydev youtube canalidan olindi 
# Paydev youtube canaliga raxmat



#import pyttsx3

#gap = pyttsx3.init()
#gap.say(" asalomu alaykum! hammangizga ")
#gap.say("meneg ismim jarvins 2..0")
#gap.runAndWait()



#gap = pyttsx3.init()
#gap.say(input("kimligingiz haqida malumot bering"))
#gap.runAndWait()
#print(gap)


Yuklash uchun manzillar

# https://pypi.org/project/1OS/                          os
# https://pypi.org/project/adhan-time/                   time
# https://pypi.org/project/speech2speech/                speech_recognition
# https://pypi.org/project/rapidfuzz/                    fuzzywuzzy
# https://pypi.org/project/pyttsx4/                      pyttsx3
# https://pypi.org/project/DateTime/                     datetime

🇺🇿  #   u yerda kutub xonalarni yuklash va ishlatish haqida tuliq malumot larni olishingiz mumkin va versiyalar bilan tanishasiz
ru  #   там можно получить полную информацию о скачивании и использовании библиотек и проверить версии
🇺🇸  #   there you can download libraries and get complete information about their usage and check versions

# Ovozli yordamchi Jarvis
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime


# barcha so`zlar jamlanmasi
opts = {
    "alias": ('jarvis', 'jarvis', 'jar', 'jorvis', 'jarviz', 'jorviz',
              'yarvis', '', 'jorvez', 'jarvez', 'jarves', 'husanjon', 'husan', 'husan','xusan'),
    "tbr": ('aytginchi', 'ko`rsatchi', 'korsat', 'necha', 'aytchi'),
    "cmds": {
        "ctime": ('xozirgi vaqt', 'soat necha', 'xozirgi soat','vaqtni kursat'),
        "radio": ('muzikani qo`y', 'radioni yoq', 'radiyoni qo`sh'),
        "stupid1": ('latifa aytib ber', 'meni kuldir', 'Latifa aytishni bilasanmi')
    }
}


# Funcsiyalar
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="uz-UZ").lower()
        print("[log] Aytildi: " + voice)

        if voice.startswith(opts["alias"]):
            # Jarvisga murojat
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # Tekshiramiz va ishlatamiz
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Tushunarsiz gap!")
    except sr.RequestError as e:
        print("[log] Tushunarsiz gap!, Internetni tekshiring!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        # vaqtni ko`rsat
        now = datetime.datetime.now()
        speak("Hozirgi vaqt " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':
        # Radioni yoqish
        os.system("D:\\Music\\Кожура - ZAPOMNI.m4a")

    elif cmd == 'stupid1':
        # Yemagan xazil
        speak("Bitta afandi PyDev kanaliga obuna bo`lmagan ekan! "
              "praektlari o`chib ketibdi! xa xa xa")

    else:
        print('Tushunarsiz gap!')


# ovoz
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Faqatgina biz yozgan ovozlarni!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)

# forced cmd test

speak("Salom Internet")
speak("Videoga layk bosing va kanalga obuna boling")

stop_listening = r.listen_in_background(m, callback)
while True:
    time.sleep(0.1)











