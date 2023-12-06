from  playsound  import playsound as g
import time


g("41.wav", block = True)
        sound.play()
                pyglet.app.run()
pyglet.media.load('41.wav', streaming=False)
        sound = pyglet.media.load('D:\\JARVIS\\41.wav', streaming=False)
        sound.play()
        pyglet.app.run()
        rec.pause_threshold = 1
rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('Bot: ...')
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    try:
        text = rec.recognize_google(audio, language="ru-RU").lower()
        print('Вы:  ' + text[0].upper() + text[1:])
        log_me('User', text, audio)
    except sr.UnknownValueError:
        text = 'Не понимаю. Повторите.'
        print('Bot: ' + text)
        text = command()
        log_me('Bot', text, Null)
    makeSomething(text)
    
