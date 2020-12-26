######Code Developed By Siddhesh D.Munagekar for building smart Assist######
##### Date:14-Dec-2020 ################

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import socket
import os
import datetime
import requests
import data_analysis
import shopping_list

#from lsHotword import ls

listener =sr.Recognizer()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',178)
def checkInternetConnection():
    try:
        socket.gethostbyname('www.google.com')
        print('Connected to Internet')
    except:
        print('No Internet connection Bye')
        os.system('No Internet connection Bye')
        exit(0)

checkInternetConnection()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def greetings():
    hour= int(datetime.datetime.now().hour)
    talk('Welcome back Sir')
    if hour >=0 and hour<12:
        talk('Good Morning !')
    elif hour >=12 and hour <18:
        talk('Good Afternoon !')
    else:
        talk('Good Evening !')
    talk('My name is Alexa how can I help you Today')

greetings()

def take_command():

    try:
        with sr.Microphone() as source:

            print('listening....')
            listener.pause_threshold=1


            voice = listener.listen(source)
            ###converting speech to text#########
            command= listener.recognize_google(voice)
            command=command.lower()

            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)



    except sr.UnknownValueError:
        talk('Sorry! I did not get that! Try typing the command ')
        command=str(input('Command: '))
        command=command.lower()
        #pass

    return command


def run_alexa():

    command=take_command()

    ####Play Youtube Video####
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' +song)

        pywhatkit.playonyt(song)

    ####Get time ####
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Sir the current time is'+time)

    ####get wikipedia information####
    elif 'information' in command:
        person=command.replace('information','')
        info=wikipedia.summary(person,1)        #Summary in just one line
        print(info)

        talk(info)

    ####simple conversation####
    elif 'how are you' in command:
        talk('I am good, How are you doing today?')
        command=take_command()
        print(command)
        if 'thank you' in command:
            talk('You Are Welcome. Have a good Day')

    #####Tell Joke###
    elif 'joke' in command:
        joke= pyjokes.get_jokes()

        talk(joke)

    ####Google Search####
    elif 'search' in command:
        command=command.replace('search','')
        talk('searching'+command)
        pywhatkit.search(command)

    ####Open Calculator####
    elif 'calculator' in command:
        talk('Opening Calculator')
        os.system("calc")


    elif 'grocery' in command:
        print('Select a number for the action that you would like to do')
        talk('Select a number for the action that you would like to do')
        print('1. View shopping list')
        talk('1. View shopping list')
        print('2. Add item to your shopping list')
        talk('2. Add item to your shopping list')
        print('3. Remove items from your shopping list')
        talk('3. Remove items from your shopping list')
        print('4. Check if items is in your shopping list')
        talk('4. Check if items is in your shopping list')
        action_item=int(input('Enter number from the above action list :'))
        shopping_list.shopping_list(action_item)



    #### weather details####2
    elif  'weather' in command:
        city=command.replace('what is the weather in','')
        weather_details(city)
    #### Performing Data Analysis #####
    elif 'data analysis' in command:
        #type=command.replace('perform classification data analysis','classification')
        test_acc,train_score=data_analysis.classification()
        talk("Performed classification Data analysis using CatBoost classifier and received Test accuracy of  {:.2f} %".format(test_acc*100))
        talk("and train accuracy of {:.2f} % with low variance and bias".format(train_score*100))
    else:
        talk('Can you please repeat.I did not understand what you say')
        #command = str(input('Command: '))
        command = command.lower()

    #ls.lsHotword_loop()
    return command


#run_alexa()
def weather_details(city):
    #print("City ",city)
    user_api = os.environ['current_weather']
    location=city

    complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()

    if api_data['cod'] == '404':
        print("Invalid City: {},Please Check your city name ".format(location))
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        humidity = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']

        print(city+" current temperature is",round(temp_city),"degree Celsius"+
             " with "+weather_desc+" possessing humidity as",humidity,"percent"
             " and wind blowing with the speed of",wind_speed,"kilometer per hour")

        climate=(city+" current temperature is",round(temp_city),"degree Celsius"+
             " with "+weather_desc+" possessing humidity as",humidity,"percent"
             " and wind blowing with the speed of",wind_speed,"kilometer per hour")

        talk(climate)



while 1:
    command=run_alexa()
    if 'bye' in command:
        talk('Thank you Good Bye')
        break



