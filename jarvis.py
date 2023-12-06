import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3 as p
from datetime import datetime
import time
import datetime
import random
import pyglet
from pydub import AudioSegment
from pydub.playback import play

def talk2():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\41.wav')
    play(song)
def talk():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\42.wav')
    play(song)
def radio():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\radio.wav')
    play(song)
def radio1():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\da.wav')
    play(song)
def da2():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\da2.wav')
    play(song)

from pydub import AudioSegment
from pydub.playback import play
import json
from hello import a, b
from fuzzywuzzy import fuzz
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime



opts = {
    "alias": ('привет'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds": {
        "ctime": ('текущее время','сейчас времени','который час', 'время'),
        "radio": ('включи музыку','воспроизведи радио','включи радио'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),
        "stop": ('останови', 'стоп'),
        "y": ('включи youtube'),
        "v": ('открой вконтакте')
        
        
    }
}
author = 'Bot'
text = 'Привет! Чем я могу вам помочь?'

print("Bot: "+ text)

def command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('Bot: ...')
        #Удаление шума
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    try:
        text = rec.recognize_google(audio, language="ru-RU").lower()
        #Вывод текста
        print('Вы:  ' + text[0].upper() + text[1:])
    #Если не распознался тест
    except sr.UnknownValueError:
        text = 'Не понимаю. Повторите.'
        print('Bot: ' + text)
        #заново
        text = command()
    return (text)





def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
    elif cmd == 'y':  
        webbrowser.open("https://youtube.com")
        da2()
    elif cmd == 'м':  
        webbrowser.open("https://vk.com/feed")
        da2() 
    else:
        print('Команда не распознана, повторите!')



def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC

  
def callback(text):
    if text.startswith(opts["alias"]):
        # обращаются 
        cmd = text
 
        for x in opts['alias']:
            cmd = cmd.replace(x, "").strip()
            
        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()
            
        # распознаем и выполняем команд

        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])





def talk2():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\41.wav')
    play(song)
def talk():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\42.wav')
    play(song)
def radio():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\radio.wav')
    play(song)
def radio1():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\da.wav')
    play(song)
def da2():
    song = AudioSegment.from_wav('D:\\JARVIS\\voice\\da2.wav')
    play(song)




while True:
    callback(command())
