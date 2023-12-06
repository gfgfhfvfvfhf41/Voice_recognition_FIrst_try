from googlesearch import search
from termcolor import colored
import speech_recognition
import wikipediaapi
import random
import webbrowser
import traceback
import os
import pyttsx3
from datetime import datetime
import datetime
import requests
from bs4 import BeautifulSoup as BS

def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()
def record_and_recognize_audio(*args: tuple):
    with microphone:
        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=1)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            pass
            return

        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru-RU").lower()


        except speech_recognition.UnknownValueError:
            pass  # play_voice_assistant_speech("What did you say again?")

        except speech_recognition.RequestError:
            print(colored("Trying to use offline recognition...", "cyan"))
        #if "джарвис" in recognized_data:
            #recognized_data = recognized_data.replace("джарвис", "").strip()
        return recognized_data
        # else:
        #     return
        #return recognized_data
def search_for_term_on_google(*args: tuple):

    if not args[0]: return
    search_term = " ".join(args[0])

    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)

    search_results = []
    try:
        for _ in search(search_term,
                        tld="com",
                        lang="ru",
                        num=1,
                        start=0,
                        stop=1,
                        pause=1.0,
                        ):
            search_results.append(_)
            webbrowser.get().open(_)

    except:
        traceback.print_exc()
        return
    print(search_results)
def search_for_video_on_youtube(*args: tuple):
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
def search_for_definition_on_wikipedia(*args: tuple):
    if not args[0]: return

    search_term = " ".join(args[0])

    url = "https://google.com/search?q=" + search_term

    wiki = wikipediaapi.Wikipedia("ru")

    wiki_page = wiki.page(search_term)
    try:
        if wiki_page.exists():
            webbrowser.get().open(wiki_page.fullurl)
        else:
            webbrowser.get().open(url)

    except:
        traceback.print_exc()
        return
def run_person_through_social_nets_databases(*args: tuple):

    if not args[0]: return

    google_search_term = " ".join(args[0])
    vk_search_term = "_".join(args[0])
    fb_search_term = "-".join(args[0])

    url = "https://google.com/search?q=" + google_search_term + " site: vk.com"
    webbrowser.get().open(url)

    url = "https://google.com/search?q=" + google_search_term + " site: facebook.com"
    webbrowser.get().open(url)

    vk_url = "https://vk.com/people/" + vk_search_term
    webbrowser.get().open(vk_url)

    fb_url = "https://www.facebook.com/public/" + fb_search_term
    webbrowser.get().open(fb_url)
def toss_coin(*args: tuple):
    flips_count, heads, tails = 3, 0, 0

    for flip in range(flips_count):
        if random.randint(0, 1) == 0:
            heads += 1

    tails = flips_count - heads
    winner = "Tails" if tails > heads else "Heads"
    print(winner)
def execute_command_with_name(command_name: str, *args: list):
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass  # print("Command not found")
def vk(*args: tuple):
    webbrowser.open('https://vk.com/')
def chrome1(*args: tuple):
    os.system("taskkill /im chrome.exe")
def steam(*args: tuple):
    os.startfile('C:\Program Files (x86)\Steam\steam.exe')
def steam1(*args: tuple):
    os.system("taskkill /im steam.exe")
def tg(*args: tuple):
    webbrowser.open('https://web.telegram.org/k/')
def time(*args: tuple):
    now = datetime.datetime.now()
    speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
def kino(*args: tuple):
    if not args[0]: return
    search_term = " ".join(args[0])
    urlk = "https://e1.zona.plus/search/" + search_term
    #webbrowser.get().open(urlk)

    r = requests.get("https://e1.zona.plus/search/" + search_term)
    html = BS(r.text, 'lxml')

    b = {}

    bg = html.findAll("a", class_="results-item", itemprop="url")
    for n in bg:
        gh = n.get('title').lower()
        if  search_term in gh:
            b[gh] = "https://e1.zona.plus" + n.get("href")




    for key,value in b.items():
        print(key + "\n" + value + "\n")
        webbrowser.open(value)




commands = {
    ("search", "google", "find", "найди"): search_for_term_on_google,
    ("video", "youtube", "watch", "видео"): search_for_video_on_youtube,
    ("wikipedia", "definition", "about", "определение", "википедия"): search_for_definition_on_wikipedia,
    ("facebook", "person", "run", "пробей", "контакт"): run_person_through_social_nets_databases,
    ("toss", "coin", "монета", "подбрось"): toss_coin,
    ('открой вконтакте', 'включи вконтакте', 'открой вк', 'вконтакте'): vk,
    ('steam'): steam,
    ('закрой steam'): steam1,
    ('закрой chrome'): chrome1,
    ('открой telegram', 'telegram'): tg,
    ('сколько время'): time,
    ('фильм', 'кино'): kino
}

if __name__ == "__main__":

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    speak_engine = pyttsx3.init()
    speak("приветствую, сер")
    while True:
        voice_input = record_and_recognize_audio()
        print(colored(voice_input, "blue"))

        if voice_input is None:
            print('xуй там плавал')
            record_and_recognize_audio()
        else:
            voice_input = voice_input.split(" ")
            command = voice_input[0]
            command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
            execute_command_with_name(command, command_options)
