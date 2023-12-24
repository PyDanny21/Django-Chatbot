#weapp
import sys
import tkinter
from pynput.keyboard import Key,Listener
import logging
import ctypes
from tkinter import *
import turtle
import pyautogui
from PIL import ImageTk, Image
import datetime
import playsound
import threading
from datetime import datetime
import json
import time
import webbrowser
from playsound import playsound
import pprint
import getpass
#import vosk
import pyaudio
import subprocess as sp
import wikipedia
# import speech_recognition as sr
from pytube import YouTube
import requests
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector
import math
import pyttsx3
# import pywhatkit as kit
import random
from sketchpy import library as lib
import calendar
import os
from pandas.io import clipboard
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
from PIL import ImageGrab
import numpy as np
import openai

#normal conversation
#solve mathematics
#news
#weather
#temperature
#face recognition
#web scrapping
#yt downloads
#play alarm
#make call
#send message sms
#email
#jokes
#advice
#speech recognition
#chempy
#GUI
#face recognition


def speak(text):
    pass

opening_text=['on it,sir','okay sir,i am working on it','a moment sir','getting it done, sir']


my_dictionary={
    'hello':'Hi sir, how are you?',
    'hi':'Hello sir, how are you?',
    'how are you':'I am as fit as fiddle and you',
    'how are you doing':'I am as fit as fiddle and you',
    'howdy':'I am as fit as fiddle and you',
    'how are you doing':'I am as fit as fiddle, and you?',
    'let talk business':'Okay sir,ready for business',
    'how dare you':'Sorry sir, I didnt mean offensive',
    'i am good':'Thank God',
    'can you':'Yes I can',
    'i love you':'I love you too',
    'good': 'I\'m also doing great sir',
    'fine': 'I\'m also doing great sir',
    'great':'Thank God',
    'fine and you': 'I\'m also doing great sir',
    'hey': 'How may I help you,Sir',
    'good and you': 'I am doing great',
    'whats up':'Nothing much sir',
    'well done':'Thank you',
    'thanks': 'No thanks sir, after all you created me',
    'thank you': 'Welcome Sir, please I will be available for any other tasks',
    'who are you': 'My name is Inertia',
    'what is your name': 'My name is Inertia',
    'who created you': 'I was created by PyDanny whose real name is Daniel Quansah',
    'i am fine and you':'I am also doing great sir!!',
    'how old are you':'I am nearly a year old',
    'who is pydanny':'PyDanny is a young, multi-talented, self taught python developer, web developer and many more, who has aimed to achieve something great in future, thus to be the greatest inventor ever.',
    'what can you do':'I can open and close programs and softwares, search for anything from google, youtube, wikipedia, stackoverflow, etc. Play music, movies, make note, create keylogger, give you random advice and jokes, and many more.',
    'how can you help me': 'I can open and close programs and softwares, search for anything from google, youtube, wikipedia, stackoverflow, etc.Play music, movies,make note,create keylogger,give you random advice and jokes.',
    'whats on':'Nothing much, sir!',
    'how was your day':'It was cool, sir and yours',
    'how was your night':'It was cool, sir and yours',
    'i am sad':'Oooh sir, please what happened!',
    'tell me more about yourself':'I am Inertia, a personal assistant program programmed by my creator PyDanny in pure Python and Javascript',
    'tell me about yourself':'I am Inertia, a personal assistant program programmed by my creator PyDanny in pure Python',
    'will you marry me':'No sir, I am only programmed to help you with some tasks',
    'can you marry me': 'No sir, I am only programmed to help you with some tasks',
    'sleep':'Ok sir, you can wake me up anytime you want',
    'wake up':'Hello sir, welcome!'
}

advice = ['Have the courage to live a life true to yourself, not the life others expect of you.',
          'Never attribute to malice that which can be adequately explained by stupidity.',
          '“There is nothing noble in being superior to your fellow man; true nobility is being superior to your former self.” Ernest Hemingway',
          'Don’t make decisions when you’re angry. Don’t make promises when you’re happy.',
          '“Never argue with a stupid person, they’ll drag you down to their level and beat you with experience.” Mark twain',
          'Only pack what you can carry yourself.',
          'Remember you’ll always regret what you didn’t do rather than what you did.',
          '“You’d worry less about what people think about you if you knew how seldom they do.” David Foster Wallace',
          'If you blame it on someone else, don’t expect it to get better.',
          '“You can be the ripest, juiciest peach in the world, but there will always be someone who hates peaches.” Dita von Teese',
          'If the grass is greener on the other side, there’s probably more manure there.',
          'Don’t give up what you want most for what you want now.',
          'With regards to the opposite sex: If you look hungry, you’ll starve.',
          '“Never let your sense of morals prevent you from doing what is right.” Isaac Asimov',
          'Strive to be the man you want your daughter to marry.',
          '“Remember only enemies speak the truth. Friends and lovers lie endlessly, caught in the web of duty.” Stephen King',
          'Never forget your car keys will change your car from one tonne of inert metal into one of the most deadly killing machines that has been invented.',
          'Wait 24 hours before getting mad and reacting about anything. If it doesn’t bother you in 24 hours time, it probably isn’t important enough to get mad over.',
          'Never make someone a priority who only makes you an option.',
          'Try not to take anything personally. No one thinks about you as much as you do.',
          '“If you want to know what a man’s like, take a good look at how he treats his inferiors, not his equals.” Sirius Black',
          'Figure out what you love to do, and then figure out how to get someone to pay you to do it.',
          'If you treat a woman like a queen, and she treats you like a jester, your princess is in another castle.',
          'Whenever something happens that makes you sad, ask yourself whether you’d still care about it when you’re ninety.',
          'Be persistent. When knowledge and ability aren’t enough, be persistent.',
          '“Life is scary. Get used to it. There are no magical fixes. It’s all up to you. So get up off your keister, get out of here, and go start doin’ the work. Nothing in this world that’s worth having comes easy.” Bob Kelso'
          'Smart girls like to hear they’re pretty, pretty girls like to hear that they’re smart.',
          'Happiness is a choice and everything else is a matter of perspective.']

quote=['Youth has no age.',
       'The young do not know enough to be prudent, and therefore they attempt the impossible, and achieve it, generation after generation.',
       'Youth is not a question of years: one is young or old from birth.',
       'Use your youth so that you may have comfort to remember it when it has forsaken you, and not sigh and grieve at the account thereof.',
       'Youth is the season made for joys, love is then our duty.'
       'Never tell a young person that anything cannot be done.',
       'Your life, time, and brain should belong to you, not to an institution.',
       'How wonderful it is that nobody need wait a single moment before starting to improve the world.',
       'Aspire to inspire before we expire.',
       'Goodness is the only investment that never fails.',
       'Whatever you do, do it well.',
       'Winners never quit and quitters never win.',
       'You can\’t depend on your eyes when your imagination is out of focus.',
       'You have to grow from the inside out.',
       'Logic will get you from A to B. Imagination will take you everywhere.',
       'After a while, you learn to ignore the names people call you and just trust who you are.',
       'The world belongs to the energetic.',
       'We are all pretty bizarre. Some of us are just better at hiding it.',
       'Do, or do not. There is no try.',
       'I just wanna let them know that they didnt break me.',
       'Oh yes, the past can hurt. But you can either run from it, or learn from it.',
       'I feel infinite.',
       'High school is like the training wheels for the bicycle of real life.',
       'Youth is a gift of nature but age is a work of art.',
       'I define being the best as competing against the best there is out there and beating them.',
       'We are who we choose to be.',
       'Make each day your masterpiece.',
       'There was no respect for youth when I was young, and now that I am old, there is no respect for age, I missed it coming and going.',
       'This is what is missing in the youth today. This being able to dream and to change the world.',
       'In relative youth, we assume we will remember everything. Someone should urge the young to think otherwise.',
       'You are here to continually push forward and move forward. That is where I am at - I just want to always surprise people.',
       'But once we live all careless free; No cross to mar our love-lit bower.',
       'Life is like a box of chocolates, you never know what you\’re gonna get.',
       'I dont regret the things I\’ve done, but those I did not do.',
       'Me, I still believe in paradise. But now at least I know it\’s not some place you can look for because its not where you go.',
       'Life moves pretty fast. If you dont stop and look around once in a while, you could miss it.',
       'Enjoy the power of your beauty and your youth.',
       'The most lively young people become the best old people, not those who pretend to be as wise as grandfathers while they are still in school.',
       'Age is foolish and forgetful when it underestimates youth.',
       'Sometimes you face difficulties you are doing something wrong, but because you are doing something right.',
       'There is a fountain of youth: it is your mind, your talents, the creativity you bring to your life and the lives of the people you love.',
       'A smart man makes a mistake, learns from it, and never makes that mistake again.',
       'Its not what happens to you, but how you react to it that matters.',
       'It takes a very long time to become young.',
       'Only to children children sing, Only to youth will spring be spring.',
       'Youth is wasted on the young.',
       'The only person you should try to be better than, is the person you were yesterday.',
       'My grandfather once told me that there were two kinds of people: those who do the work and those who take the credit. He told me to try to be in the first group; there was much less competition.',
       'Joy of youth, dream of youth, blood of youth, mood of youth, clothe the world with colors golden, singing songs that never olden.',
       'Youth is that period when a young boy knows everything but how to make a living.',
       'Youth is the best time to be rich, and the best time to be poor.',
       'Youth is a blunder; manhood a struggle, 0ld age a regret.',
       'You are as old as your doubt, your fear, your despair.',
       'It always seems impossible until its done.',
       'Youth is something very new: twenty years ago, no one mentioned it.',
       'We would accomplish many more things if we did not think of them as impossible.',
       'One must learn by doing the thing; for though you think you know it, you have no certainty, until you try.',
       'You are only young once, and if you work it right, once is enough.',
       'The world is the great gymnasium where we come to make ourselves strong.',
       'When you reach the end of your rope, tie a knot in it and hang on.',
       'Cherish your visions and your dreams, as they are the children of your soul, the blueprints of your ultimate achievements.',
       'When you replace why is this happening to me with what is this trying to teach me? Everything shifts.',
       'The world’s biggest power is the youth and beauty of a woman.',
       'Everything started as nothing.',
       'It is better to be a young June-bug than an old bird of paradise.',
       'You always pass failure on the way to success.',
       'Young people need models, not critics.',
       'It is never too late to be what you might have been.',
       'Dont downgrade your dream just to fit your reality. Upgrade your conviction to match your destiny.',
       'Youth is the season of receptivity, and should be devoted to acquirement; and manhood of power--that demands an earnest application. Old age is for revision.',
       'Yesterday you said tomorrow. Just do it.',
       'Build yourself up to stand out and be recognized in a crowd.',
       'The secret of growing younger is counting blessings, not birthdays.',
       'It is the juvenile period of life when friendships are formed, and habits established, that will stick by one.',
       'A leader is a dealer in hope.',
       'In youth we learn; in age we understand.',
       'You don\’t have to hold a position in order to be a leader.',
       'Old minds have the power to create history, young minds have the power to change the history.',
       'To have long term success as a coach or in any position of leadership, you have to be obsessed in some way.',
       'Leaders are never satisfied; they continually strive to be better.',
       'The way to keep young is to keep your faith young. Keep your self-confidence young. Keep your hope young.',
       'The passions of the young are vices in the old.',
       'The young, free to act on their initiative, can lead their elders in the direction of the unknown.',
       'Unless someone like you cares a whole awful lot, nothing is going to get better.  Its not.',
       'Mans own youth is the worlds youth.',
       'We all know we\'re young. We\'re just trying to stay positive. We\'re making young mistakes.',
       'The young are not afraid of telling the truth.',
       'There is always some specific moment when we become aware that our youth is gone; but, years after, we know it was much later.',
       'Youth comes but once in a lifetime.',
       'It is time for parents to teach young people early on that in diversity there is beauty and there is strength.',
       'There is no doubt that creativity is the most important human resource of all.',
       'When you are young, everything feels like the end of the world, but its not; its just the beginning.',
       'Anyone who stops learning is old, whether at twenty or eighty. Anyone who keeps learning stays young.',
       'Youthfulness is about how you live, not when you were born.',
       'Life is not about waiting for the storms to pass... its about learning to dance in the rain.'
       ]


# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def generate_response(prompt):
    # Specify the OpenAI GPT-3.5 engine and make a request
    response = openai.completions.create(
        engine="text-davinci-003",  # You can change the engine based on your preference
        prompt=prompt,
        max_tokens=150,  # You can adjust the maximum number of tokens in the response
        temperature=0.7,  # You can adjust the temperature parameter for randomness
        n=1,  # Number of completions to generate
        stop=None  # You can specify a stop sequence to limit the response
    )

    return response.choices[0].text.strip()

def nlp_Prompt(query):
    prompt=f"Process the following natural language query : '{query}'"
    response=generate_response(prompt)
    return response
    

paths = {
    'notepad': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_notepad():
    os.startfile(paths['notepad'])

def open_calculator():
    os.startfile(paths['calculator'])

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_cmd():
    os.system('start cmd')
    
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=4)
    print(results)
    # speak(results)
    return results

def facedetector():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    aa = FaceDetector()
    while (True):
        success, img = cap.read()
        imag = aa.findFaces(img)
        cv2.imshow('image', img)
        c = cv2.waitKey(1)
        if c == ord('q'):
            break

def handdetector():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.8, maxHands=2)
    while True:
        # Get image frame
        success, img = cap.read()
        # Find the hand and its landmarks
        hands, img = detector.findHands(img)  # with draw
        # hands = detector.findHands(img, draw=False)  # without draw

        if hands:
            # Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points
            bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
            centerPoint1 = hand1['center']  # center of the hand cx,cy
            handType1 = hand1["type"]  # Handtype Left or Right

            fingers1 = detector.fingersUp(hand1)

            if len(hands) == 2:
                # Hand 2
                hand2 = hands[1]
                lmList2 = hand2["lmList"]  # List of 21 Landmark points
                bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
                centerPoint2 = hand2['center']  # center of the hand cx,cy
                handType2 = hand2["type"]  # Hand Type "Left" or "Right"

                fingers2 = detector.fingersUp(hand2)

                # Find Distance between two Landmarks. Could be same hand or different hands
                length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)  # with draw
                #length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
        # Display
        cv2.imshow("Image", img)
        if cv2.waitKey(1)==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def alldetector():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    detector = HandDetector(detectionCon=0.8, maxHands=2)
    face = FaceDetector(minDetectionCon=2)

    def main():
        while True:
            # Get image frame
            success, img = cap.read()
            # Find the hand and its landmarks
            hands, img = detector.findHands(img)
            faces = face.findFaces(img)
            # with draw
            # hands = detector.findHands(img, draw=False)  # without draw

            if hands:
                # Hand 1
                hand1 = hands[0]
                lmList1 = hand1["lmList"]  # List of 21 Landmark points
                bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
                centerPoint1 = hand1['center']  # center of the hand cx,cy
                handType1 = hand1["type"]  # Handtype Left or Right

                fingers1 = detector.fingersUp(hand1)

                if len(hands) == 2:
                    # Hand 2
                    hand2 = hands[1]
                    lmList2 = hand2["lmList"]  # List of 21 Landmark points
                    bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
                    centerPoint2 = hand2['center']  # center of the hand cx,cy
                    handType2 = hand2["type"]  # Hand Type "Left" or "Right"

                    fingers2 = detector.fingersUp(hand2)

                    # Find Distance between two Landmarks. Could be same hand or different hands
                    length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)  # with draw
                    # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
            # Display
            cv2.imshow("Image", img)
            c = cv2.waitKey(1)
            if c == ord('q'):
                break

def cartooning(img):
    import pyautogui as pg
    image=cv2.imread(img)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray, 5)
    edges=cv2.adaptiveThreshold(gray,255,
                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY,9,9)

    #CARTONATION
    color=cv2.bilateralFilter(image,9,250,250)
    cartoon=cv2.bitwise_and(color,color,mask=edges)

    cv2.imshow('image',image)
    cv2.imshow('edges',edges)
    cv2.imshow('cartoon',cartoon)
    c = cv2.waitKey(0)
    cv2.destroyAllWindows()

    while(True):
        a=pg.confirm('Are you sure about cartooning your picture', buttons=['Yes', 'No'])
        if a=='Yes':
            cartooning(img)
            break
        else:
            break

def format_response(weather):

    for i in range(10):

        dt_txt = weather['list'][i]['dt']
        date = (datetime.fromtimestamp(dt_txt)).strftime('%d-%b-%Y %H:%M:%S')

        desc = weather['list'][i]['weather'][0]['description']

        temp_min = weather['list'][i]['main']['temp_min']

        temp_max = weather['list'][i]['main']['temp_max']

        final_str = 'Date: %s \nConditions: %s \nMin.Temperature(Celsius): %s\nMax.Temperature(Celsius): %s' %(date, desc, temp_min, temp_max)

        return(final_str)

def get_weather(city):
    api_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

def get_latest_news():
    NEWS_API_KEY = "17872d9bca7343e4866348761f3d3476"
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
        print(article, sep='\n')
    # return article['title']
    return news_headlines[:5]

# def note():
#     speak('sir,please what should i write')
#     nn = input(':')
#     speak('sir,please should i include date and time?')
#     datetimer = input(':')
#     with open('log.txt', 'a') as file:
#         time = datetime.now().strftime('%H:%M')
#         date = datetime.now().date()
#         if 'yes' in datetimer:
#             file.write(f'on {date} at {time},you made a note saying {nn}')
#             pyautogui.press('enter')
#         elif 'no' in datetimer:
#             file.write(f'you made a note saying {nn}')
#             pyautogui.press('enter')
#         speak('Note made successfully!')

# def open_note():
#     os.startfile('W:\\Projects\\Projects\\py\\log.txt')

# def play_englishsong():
#     music_dir = 'D:\\English songs\\'
#     songs = os.listdir(music_dir)
#     #print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def next_englishsong():
#     music_dir = 'D:\\English songs\\'
#     songs = os.listdir(music_dir)
#     #print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def play_hilife():
#     music_dir = 'D:\\HI-LIFE\\'
#     songs = os.listdir(music_dir)
#     #print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def next_hilife():
#     music_dir = 'W:\\HI-LIFE\\'
#     songs = os.listdir(music_dir)
#     #print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def play_gospel():
#     music_dir = 'D:\\GOSPELS\\'
#     songs = os.listdir(music_dir)
#     #print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def next_gospel():
#     music_dir = 'W:\\GOSPELS\\'
#     songs = os.listdir(music_dir)
#     #print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def play_worship():
#     music_dir = 'W:\\Worship\\'
#     songs = os.listdir(music_dir)
#     # print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def next_worship():
#     music_dir = 'W:\\Worship\\'
#     songs = os.listdir(music_dir)
#     # print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def Cools():
#     music_dir = 'W:\\2015-05-05 COOLS.mp3'
#     speak(f'Playing coools')
#     title = os.startfile(music_dir )

def play_music():
    music_dir = 'C:\\Users\\Daniel\\Desktop\\SUNDAY\\Jarvis\\Project\\tracks\\'
    songs = os.listdir(music_dir)
    # print(len(songs))
    song = random.choice(songs)
    title = os.startfile(music_dir + song)
    return f'Playing {song}'

def next_music():
    music_dir = 'C:\\Users\\Daniel\\Desktop\\SUNDAY\\Jarvis\\Project\\tracks'
    songs = os.listdir(music_dir)
    # print(len(songs))
    song = random.choice(songs)
    title = os.startfile(music_dir + song)
    return f'Playing {song}'

# def next_music():
#     music_dir = 'D:\\tracks\\'
#     songs = os.listdir(music_dir)
#     # print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def play_music1():
#     music_dir = 'W:\\Afro-Dancehall\\'
#     songs = os.listdir(music_dir)
#     # print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def next_music1():
#     music_dir = 'W:\\Afro-Dancehall\\'
#     songs = os.listdir(music_dir)
#     # print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def play_reggae():
#     music_dir = 'W:\\Reggae\\'
#     songs = os.listdir(music_dir)
#     # print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

# def next_reggae():
#     music_dir = 'W:\\Reggae\\'
#     songs = os.listdir(music_dir)
#     # print(len(songs))
#     song = random.choice(songs)
#     speak(f'Playing {song}')
#     title = os.startfile(music_dir + song)

def play_movie():
    movies_dir = 'D:\\Movies\\'
    movies = os.listdir(movies_dir)
    # print(len(movies))
    mov = movies[random.randint(0, len(movies)-1 )]
    speak(f'Playing {mov}')
    os.startfile(movies_dir + mov)

def next_movie():
    movies_dir = 'W:\\Movies\\'
    movies = os.listdir(movies_dir)
    # print(len(movies))
    mov = movies[random.randint(0, len(movies)-1 )]
    speak(f'Playing {mov}')
    os.startfile(movies_dir + mov)

def show_movie():
    os.startfile('W:\\Movies')


# def speak_note():
#     with open('W:\\Projects\\Projects\\py\\log.txt', 'r') as ff:
#         a = ff.read()
#         speak(a)

# def game():
#     path='C:\\Beach Buggy Racing.lnk'
#     os.startfile(path)

# def football():
#     path='C:\\Users\\Daniel\\Desktop\\Winning Eleven 9.lnk'
#     os.startfile(path)

def screenshot():
    time.sleep(1)
    pyautogui.hotkey('win','prtsc')

def minimize_windows():
    time.sleep(1)
    pyautogui.hotkey('win','m')
    return 'all windows minimized'

def keylogger():
    log_dir = ''
    logging.basicConfig(filename=(log_dir + 'keylogs.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        logging.info(str(key))

    def on_release(key):
        if key == Key.esc:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def maximize():
    time.sleep(1)
    pyautogui.hotkey('win','shift','m')
    return 'all windows maximized'

def draw():
    a=lib.rdj()
    a.draw()

# def barchart(index,labels,sizes):
#     import matplotlib.pyplot as plot
#     # set up the data
#     labels = ('Python', 'C#', 'Java', 'PHP', 'Ruby')
#     index = (1, 2, 3, 4, 5)
#     sizes = 90, 20, 54, 76, 18
#     # setting up bar chart
#     plot.bar(index, sizes, tick_label=labels)
#     plot.ylabel('Usage')
#     plot.xlabel('Programming Language')


# def calculate(a):
#         time.sleep(5)
#         pyautogui.click(x=352, y=149, clicks=1, interval=0, button='left')
#         pyautogui.write(a, 0.5)
#         pyautogui.press('enter')
#         pyautogui.hotkey('ctrl', 'a')
#         pyautogui.hotkey('ctrl','c')
#         speak(f'{a} equals ' + clipboard.paste())
        
        

def hackmyphone(ip_address):
    capture = cv2.VideoCapture(f"http:{ip_address}:8080/video")
    while True:
        success, frame = capture.read()
        cv2.imshow('Phone Camera', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

# def alarm():
#     #taking input from user
#     speak('Sir, please take time to fill the alarm details')
#     alarmDY=int(input('Year>>>'))
#     alarmDM=int(input('Month>>>'))
#     alarmDD=int(input('Day>>>'))
#     alarmH = int(input('Hour>>>'))
#     alarmM = int(input('Minute>>>'))
#     amPm = str(input('am/pm>>>'))
#     mission=str(input('Task>>'))

#     print(f"Waiting for the alarm @ {alarmH}:{alarmM}{amPm}")
#     if (amPm == "pm"):
#         alarmH = alarmH + 12

#     #Current Date Time
#     now = datetime.now()

#     alarmDate=alarmDY,alarmDM,alarmDD
#     #desired alarm time
#     later = datetime(alarmDate,alarmH,alarmM,0)

#     #calculating the difference between two time
#     difference = (later - now)

#     #difference in seconds
#     total_sec=difference.total_seconds() 

#     def alarm_func():
#         for i in range(30):
#             playsound('W:\\Projects\\Projects\\py\\beep-09.wav', True)
#             speak(f'Sir, please it is time to {mission}')
        

#     timer = threading.Timer(total_sec, alarm_func)
#     timer.start()

def loc(place):
    webbrowser.open("http://www.google.com/maps/place/" + place + "")
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails=True)
    target_latlng = location.latitude, location.longitude
    location = location.raw['address']
    target_loc = {'city': location.get('city', ''),
                   'state': location.get('state', ''),
                   'country': location.get('country', '')}
    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng

    distance = str(great_circle(current_latlng, target_latlng))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance), 2)

    return current_loc, target_loc, distance

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    #print(city,state,country)
    return city, state,country

def record_screen():
    #Obtain image dimensions
    #Screen capture 
    image = ImageGrab.grab()
    #Convert the object to numpy array
    img_np_arr = np.array(image)
    #Extract and print shape of array
    shape = img_np_arr.shape
    print(shape)

    #Create a video writer
    screen_cap_writer = cv2.VideoWriter('screen_recorded.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 50, (shape[1], shape[0]))

    #To View the screen recording in a separate window (OPTIONAL)
    #This is optional. Use the aspect ratio scaling if you wish to view the screen recording simultaneously
    #Low scale_by_percent implies smaller window
    scale_by_percent = 50 
    width = int(shape[1] * scale_by_percent / 100)
    height = int(shape[0] * scale_by_percent / 100)
    new_dim = (width, height)
    #Record the screen
    #Condition to keep recording as a video
    while True:
        #Capture screen
        image = ImageGrab.grab()
        #Convert to array
        img_np_arr = np.array(image)
        #OpenCV follows BGR and not RGB, hence we convert
        final_img = cv2.cvtColor(img_np_arr, cv2.COLOR_RGB2BGR)
        #Write to video 
        screen_cap_writer.write(final_img)
        #OPTIONAL: To view your screen recording in a separate window, resize and use imshow()
        '''
            If you choose to view the screen recording simultaneously,
            It will be displayed and also recorded in your video. 
        '''
        image = cv2.resize(final_img, (new_dim))
        cv2.imshow("image", image)
        #Stop and exit screen recoding if user presses 'e' (You can put any letter)
        if cv2.waitKey(1) == ord('q'):
            break
        
        
    #Release the created the objects
    screen_cap_writer.release()
    cv2.destroyAllWindows()

def command(query):
    #query=input('\t\t\t\t\t\t\t\t\t\tBoss:').lower() or take_command().lower()
    #query=ques.get() or take_command.lower()
    if query in my_dictionary:
        return my_dictionary[query]
    
    elif 'morning' in query:
        hr=int(datetime.now().hour)
        if hr>=16 and hr<24:
            greet='Good morning sir!'
        elif hr>=12 and hr<16:
            greet='Good Afternoon sir!'
        else:
            greet='Good evening sir!'
        return greet
        
    elif 'afternoon' in query:
        hr=int(datetime.now().hour)
        if hr>=16 and hr<24:
            greet='Good morning sir!'
        elif hr>=12 and hr<16:
            greet='Good Afternoon sir!'
        else:
            greet='Good evening sir!'
        return greet
         
    elif 'evening' in query:
        hr=int(datetime.now().hour)
        if hr>=16 and hr<24:
            greet='Good morning sir!'
        elif hr>=12 and hr<16:
            greet='Good Afternoon sir!'
        else:
            greet='Good evening sir!'
        return greet
    
    elif 'minimize' in query:
        minimize_windows()

    elif 'maximize' in query:
        maximize()
    
    elif 'are you from' in query:
        return 'I am Proudly from Ghana'
        # import ghanaflag

  
    elif 'open settings' in query:
        pyautogui.hotkey('win','i')

    elif 'open notepad' in query:
        open_notepad()
        return random.choice(opening_text)

    elif 'close notepad' in  query:
        os.system('taskkill /f /im notepad.exe')

    elif 'open cmd' in  query:
        open_cmd()

    elif 'close cmd' in  query:
        os.system('taskkill /f /im cmd.exe')

    elif 'keylogger' in query:
        keylogger()
        return 'keylogger started!!!'

    elif 'hand detector' in query:
        handdetector()

    elif 'face detector' in query:
        facedetector()


    elif 'detect all' in query:
        alldetector()

    elif 'open camera' in  query:
        open_camera()

    elif 'word' in query:
        pyautogui.hotkey('win', 'r')
        pyautogui.write('winword',0.2)
        pyautogui.press('enter')
        return 'launching Microsoft Word 2019'
    
    elif 'excel' in query:
        pyautogui.hotkey('win', 'r')
        pyautogui.write('excel',0.2)
        pyautogui.press('enter')
        return 'launching Microsoft Excel 2019'

    elif 'powerpoint' in query:
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk')
        return 'launching Microsoft Powerpoint 2019'

    elif 'close camera' in  query:
        os.system('taskkill /f /im camera.exe')
        return random.choice(opening_text)

    elif 'date' in query:
        date=datetime.now().date()
        return date
    elif 'open calculator' in  query:
        open_calculator()

    # elif  in query:
    #     return eval(query)

    elif 'close calculator' in  query:
        os.system('taskkill /f /im calculator.exe')

    elif 'screenshot' in  query:
        screenshot()

    elif 'switch window' in  query:
        pyautogui.hotkey('alt','tab')
        return 'window switched'

    elif 'shutdown' in  query:
        os.system('shutdown /s')

    elif 'refresh screen' in query:
        pyautogui.hotkey('win', 'm')
        pyautogui.rightClick(300, 300)
        pyautogui.press('Down')
        pyautogui.press('Down')
        pyautogui.press('Down')
        pyautogui.press('enter')
        pyautogui.hotkey('win', 'shift', 'm')

    elif 'restart' in  query:
        os.system('shutdown /r')
        return 'Restarting system'

    elif 'lock screen' in  query:
        os.system('shutdown /l')
        return 'locking screen'

    elif 'quote' in query:
        quotes=quote[random.randint(0,len(quote)-1)]
        return quotes

    elif 'advice' in query:
        ad=advice[random.randint(0,len(advice)-1)]
        return ad

    elif 'open youtube' in  query:
        speak(random.choice(opening_text))
        sp.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'www.youtube.com'])

    elif 'download video' in query:
        link=query.replace('download video','')
        yt=YouTube(link)
        try:
            yd=yt.streams.get_highest_resolution()
            yd.download('D:\\','downloads by Py.mp4')          
            return 'video downloaded succesfully'
        except:
            return 'couldnt download video, please try again!'

    elif 'open google' in  query:
        speak(random.choice(opening_text))
        sp.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'www.google.com'])

    elif 'time' in query:
        return f'The current time is {datetime.now().strftime("%H:%M:%S")}'
    elif 'read' in query:
        text=clipboard.paste()
        return text

    elif 'type' in query:
        speak(random.choice(opening_text))
        text=clipboard.paste()
        pyautogui.typewrite(text)
        speak('Done typing, Sir!!')

    elif 'weather' in query:
        ip_address = find_my_ip()
        city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
        weather, temperature, feels_like = get_weather(city)
        # speak(f"Getting weather report for your city {city}")
        return f"The weather report for {city} is {weather}.\nThe current temperature is {temperature}, but it feels like {feels_like}"
        # speak(f"Also, the weather report talks about {weather}")
        # speak("For your convenience, I am printing it on the screen sir.")
        # print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

    elif "news" in query:
        try:
            news_res = get_latest_news()
            # speak('Source: The Times Of Ghana')
            for index, articles in enumerate(news_res):
                # pprint.pprint(articles['title'])
                if index == len(news_res)-2:
                    break
                return ('Todays Headlines are '+ articles['title'])
        except:
            return 'Sir, please make sure you have internet connection'


    elif 'visit' in  query:
        web =  query.replace('visit', '')
        webbrowser.open(f'{web}')
        return 'On it Sir'

    elif 'open stackoverflow' in  query:
        webbrowser.open('www.stackoverflow.com')
        return 'On it Sir'

    elif 'open wikipedia' in  query:
        webbrowser.open('www.wikipedia.com')
        return 'On it Sir'

    elif 'search wikipedia' in  query:
        query =  query.replace('search wikipedia', '')
        result= search_on_wikipedia(query)
        return f'{result}'

    elif 'draw' in  query:
        draw()
        return 'On it Sir'


    elif 'search' in  query:
        a =  query.replace('search', '')
        # speak(f'searching for {a} from google')
        sp.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
                  f'https://www.google.com/search?client=chrome-b-d&q={a}'])

    # elif 'make note' in  query:
    #     speak(random.choice(opening_text))
    #     note()

    # elif 'show note' in  query:
    #     speak(random.choice(opening_text))
    #     open_note()

    # elif 'speak note' in  query:
    #     speak(random.choice(opening_text))
    #     speak_note()

    elif 'play music' in  query:
        play_music()
        return 'On it Sir'


    elif 'next music' in  query:
        next_music()
        return 'On it Sir'


    # elif 'play english' in  query:
    #     speak(random.choice(opening_text))
    #     play_englishsong()

    # elif 'next english' in  query:
    #     speak(random.choice(opening_text))
    #     next_englishsong()

    # elif 'play hilife' in  query:
    #     speak(random.choice(opening_text))
    #     play_hilife()

    # elif 'next hilife' in  query:
    #     speak(random.choice(opening_text))
    #     next_hilife()

    elif 'harddisk' in query:
        speak('opening hard disk W')
        os.startfile('D:\\')

    # elif 'play afromusic' in  query:
    #     speak(random.choice(opening_text))
    #     play_music1()

    # elif 'next afromusic' in  query:
    #     speak(random.choice(opening_text))
    #     next_music1()

    # elif 'play reggae' in  query:
    #     speak(random.choice(opening_text))
    #     play_music1()

    # elif 'next reggae' in  query:
    #     speak(random.choice(opening_text))
    #     next_music1()

    elif 'stop music' in query:
        os.system('taskkill /f /im vlc.exe')

    elif 'stop movie' in query:
        os.system('taskkill /f /im vlc.exe')


    elif 'play movie' in  query:
        speak(random.choice(opening_text))
        play_movie()

    elif 'next movie' in  query:
        speak(random.choice(opening_text))
        next_movie()

    elif 'show movies' in  query:
        speak(random.choice(opening_text))
        show_movie()

    # elif 'plot' in  query:
    #     speak(random.choice(opening_text))
    #     barchart()


    # elif 'reminder' in query:
    #     speak('Please, how many minutes')
    #     time=input('>>')
    #     seconds=int(time)*60
    #     speak('Countdown started')
    #     pyautogui.countdown(seconds)
    #     print('Time Up')
        #os.system('cls')
        # for i in range(4):
        #     # import playing_sound
        #     #playsound.playsound('W:\\Projects\\Projects\\py\\beep-09.wav')
        # speak('Time up, Sir. Time to get to work.')

    # elif 'play game' in query:
    #     speak(random.choice(opening_text))
    #     game()

    # elif 'football' in query:
    #     speak(random.choice(opening_text))
    #     football()

    elif 'close game' in query:
        os.system('taskkill /f /im Beach Buggy Racing.lnk')

    elif 'music studio' in  query:
        sp.Popen(['C:\\Program Files\\Image-Line\\FL Studio 20\\FL64.exe'])

    elif 'volume up' in query:
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        

    elif 'ip address' in query:
        try:
            find_my_ip()
        except:
            return 'an error occured, please make sure  you are connected to the internet.'

    elif 'volume down' in query:
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')

    elif 'mute' in query:
        pyautogui.press('volumemute')

    elif 'unmute' in query:
        pyautogui.press('volumemute')

    elif 'task manager' in query:
        pyautogui.hotkey('ctrl','shift','esc')

    elif 'obs studio' in  query:
        speak(random.choice(opening_text))
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OBS Studio\\OBS Studio (64bit).lnk')

    elif 'hack ' in query:
        ipaddress=query.replace('hack ','')
        hackmyphone(ipaddress)


    elif 'system info' in query:
        pyautogui.press('win')
        pyautogui.typewrite('system', 1)
        pyautogui.press('enter')
        #time.sleep(2)
        with open('D:\\Projects\\Projects\\system.txt', 'r') as file:
            a=file.read()
            speak(a)

    elif 'close obs studio' in  query:
        os.system('taskkill /f /im OBS Studio (64bit).lnk')

    elif 'my picture' in query:
        os.startfile('mypic.JPG')
        return 'Here is PyDanny, the person wo created me'
    
    elif 'his picture' in query:
        speak('On it sir')
        os.startfile('mypic.JPG')
        speak('Here is PyDanny, the person wo created me')

    elif "where is" in query:
            place = query.split('where is ', 1)[1]
            current_loc, target_loc, distance =loc(place)
            city = target_loc.get('city', '')
            state = target_loc.get('state', '')
            country = target_loc.get('country', '')
            time.sleep(1)
            try:

                if city:
                    res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                    #print(res)
                    return res

                else:
                    res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                    #print(res)
                    return res

            except:
                res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                #print(res)
                return res

    elif "current location" in query or "where am i" in query:
        try:
            city, state, country = my_location()
            print(city, state, country)
            return f"You are currently in {city} city which is in {state} state and country {country}"
        except Exception as e:
            print(e)
            return "Sorry sir, I coundn't fetch your current location. Please try again"

    elif 'screen recorder' in query:
        record_screen()
        return 'Starting screen recorder'

    elif 'record screen' in query:
        record_screen()
        return 'Starting screen recorder'

    elif 'instagram' in query:
        speak('opening your instagram, sir')
        webbrowser.open('www.instagram.com/pydanny21')

    elif 'telegram' in query:
        speak('opening your telegram, sir')
        webbrowser.open('https://t.me/pydanny21')

    elif 'github' in query:
        speak('opening your gitub, sir')
        webbrowser.open('www.github.com/pydanny21')

    elif 'facebook' in query:
        webbrowser.open('www.facebook.com')

    elif 'Portfolio' in query:
        webbrowser.open('pydanny21.github.io/Portfolio/')
        
    elif 'search youtube' in query:
        video=query.replace('search youtube','')
        try:
            kit.playonyt(video)
        except:
            return 'Sir, please make sure you have a stable internet connection'

    elif 'play on youtube' in query:
        video=query.replace('play on youtube','')
        try:
            kit.playonyt(video)
        except:
            return 'Sir, please make sure you have a stable internet connection'

    # elif 'send whatsapp message to' in query:
    #     speak('Sir,please what should I say')
    #     message=input('>>>')
    #     number=int(query.replace('send whatsapp message to',''))
    #     try:
    #         kit.sendwhatmsg_instantly(number,message)
    #     except:
    #         speak('Sir, please make sure you have a stable internet connection')

    else:
        nlp_Prompt(query)