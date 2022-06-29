# Project jarvis 4.0.1
# developed by @itzzzyashu
# Update 4.0.1



# Packages
#   speech_recognition as sr 
#   datetime
#   wikipedia
#   pyttsx3
#   webbrowser
#   random
#   os



# Importing packages and config variables

import os
import html
import time
# import pyjokes
import random
# import pyttsx3
# import wikipedia
import webbrowser
# import speech_recognition as sr 
from datetime import datetime, date
from config import NAME, CLASS, AGE, TFT, CNT
from config import jarvis_path, music_dir, pics_dir, video_dir, hidden_dir, xsearch


# Late Night is now dependent on user's age
if AGE >= 13:
    LATE_NIGHT = "True"
else:
    LATE_NIGHT = "False"

# Time Importing
hour = int(datetime.now().hour)
minute = int(datetime.now().minute)
second = int(datetime.now().second)

if TFT == 24:
    tym = '{}:{}:{}'.format(hour, minute, second)
elif TFT == 12:
    if hour > 12:
        hrs = hour-12
        tym = "{}:{}:{} PM {}".format(hrs, minute, second, CNT)
    elif hour < 12:
        tym = "{}:{}:{} AM {}".format(hour, minute, second, CNT)
    else:
        tym = "ERROR IN 12 HOUR FORMAT"
else:
    tym = "ERROR IN 24 HOUR FORMAT"
# time = f'{hour} : {minute} : {second}'


# Date Importing
if CNT == 'UTC':
    date = "%d %m %Y, %A UTC"
    date_fmt = datetime.utcnow().strftime(date)
elif CNT == 'IST':
    date = date.today()
    date_fmt = date.strftime("%d %b %Y, %A IST")
else:
    print("ERROR IN COUNTRY DATE")

def repeat():
    print('INITIALIZING Jarvis 4.0.1 IN 3 SECONDS...')
    time.sleep(3)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')
    time.sleep(0.2)
    print('[==================================] [==================================]')

# repeat()

dttm=f'''\n
||=============Date & Time=============||
   Date: {date_fmt}
   Time: {tym}
||=====================================||
'''
# Wishing message :)
print("\n# || =============== Started Jarvis AI 4.0.1 =============== || #")
if hour >= 0 and hour<12:
    print(dttm)
    print(f"\nGood Morning {NAME}, how are you? :)")
elif hour>=12 and hour<16:
    print(dttm)
    print(f"\nGood Afternoon {NAME}, how are you? :)")
elif hour>=16 and hour<22:
    print(dttm)
    print(f"\nGood Evening {NAME}, how are you? :)")
elif hour>=22:
    if LATE_NIGHT == "False":
        print(dttm)
        print(f"Time is {tym} yet, you should sleep now.")
        if CLASS<10:
            print("also you have to study for your exams.")
        exit()
    elif LATE_NIGHT == "True":
        print(dttm)
        print(f"\nGood Night {NAME}, how are you? :)")

# Logs
def jarvis():
    search = input("Enter : ")
    if search == "help":
        help_section='''
I can help you with these commands


0. google/assistance/x - Open Google.

1. github/git/coding - Open GitHub.

2. heroku - Open Heroku website.

3. youtube/yt/online videos - Open YouTube.

4. pip install - Install a python module.

5. prompt/cmd - Open Command Prompt.

6. shutdown/turn off - Shutdown device with different functions.

7. musics/audio - Play Musics saved in directory of 'music_dir'.

8. videos/vids/video - Play Videos saved in directory of 'video_dir'.

9. photos/pics/photographs/images - Open photographs saved in directory of 'pics_dir'.

10. goodbye/bye/tata - End the Program.

11. Random Search - Gives you result at Google.

12. date/time - date or time respectively.

13. insta/instagram - Open Instagram.

14. fb/facebook/meta - Open Facebook/Meta.

15. tweet/twitter - Open Twitter.

16. path/directory - Opens given path/directory.

17. hidden - Open help related to hidden files.

18. 
'''
        print(help_section)

    elif "google" in search or 'assistance' in search :
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "insta" in search or 'instagram' in search or 'ig' in search :
        print("Opening Instagram...")
        webbrowser.open("https://www.instagram.com")

    elif 'fb' in search or 'facebook' in search or 'meta' in search :
        print("Opening Meta/Facebook...")
        webbrowser.open("https://www.facebook.com")

    elif 'tweet' in search or 'twitter' in search:
        print("Opening Twitter...")
        webbrowser.open("https://www.twitter.com")
    
    elif "github" in search or 'git' in search or 'coding' in search :
        print("Opening Github...")
        webbrowser.open("https://www.github.com")
    
    elif 'youtube' in search or 'yt' in search or 'online videos' in search :
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif 'time' in search :
        print("Time is {}".format(tym))

    elif 'date' in search :
        print("Date is "+date_fmt)

    elif "pip install" in search :
        input("Enter python module name that you wanna install : ")
        os.system("pip install {}".format(search))
    
    elif "prompt" in search or 'cmd' in search or 'shell' in search :
        prompt_cmd=input("Enter prompt command : ")
        if prompt_cmd == "shutdown":
            print("You should enter `shutdown` directly")
        else:
            print("'"+prompt_cmd+"' command executed")
            os.system(prompt_cmd)
        
    elif "shutdown" in search or 'turn off' in search :
        print("Please choose which type of Shutdown you want :-"
          "\nShutdown",
          "\n.......................................................... : s"
          "\nRestart",
          "\n.......................................................... : r"
          "\nLog off",
          "\n.......................................................... : l"
          "\nRestart after Reboot",
          "\n.......................................................... : g"
         "\nShutdown without any warning",
          "\n.......................................................... : p"
         "\nSleep / Hibernate",
          "\n.......................................................... : h"
          "\n\nYou can Abort shutdown once if you selected 'No'.")
        sdt = input("Enter the symbol : ")
        confirmation_text = """ # ================ Confirmation ================= #
\nPlease confirm by entering:
 'Yes' : I want to shutdown.
 'No'   : I don't want to shutdown or maybe I had mistaken."""
        print(confirmation_text)
        confirm_s = input("\nEnter : ")
        if confirm_s == "Yes":
            print(f"OK! shutting down with `shutdown /{sdt}` command"
                  "Shutdown Process : SD CODE ACCEPTED"
                  "Attempting Shutdown by Jarvis AI 4.0.1")
            
            os.system(f'shutdown -{sdt}')
        if confirm_s == "No":
            print(f"OK! Aborted Shutdown, please be sure next time :)")
            os.system(f'shutdown /a')
            os.system("Desktop\Jarvis-4.0.1\jarvis.py")
        if confirm_s != "No" or "Yes":
            print("Wrong choice\nPlease Enter 'Yes' or 'No'")

    elif "what\'s up" in search or 'how are you' in search :
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you?']
        ans_q = random.choice(stMsgs)
        print(ans_q)
        ans_take_from_user_how_are_you = input()
        if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
            print('okey... Any command for me?')
        elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
            print("oh I'm sorry...")

    elif 'make you' in search or 'made you' in search or 'created you' in search or 'developed you' in search :
        ans_m = """
For your information,
I was developed by @itzzzyashu
Lot of Thanks to Him.

you can contact him by
Instagram - @itzzzyashu
Telegram - @itzzzyashu
Gmail - rajnisrdevs@gmail.com

He's most active on Telegram
for thier Programming projects as
Userbots, bots, AI bots, Group Management bots
I'm an AI python program for basic lifestyles made by
https://telegram.me/SanatanRakshaNetwork.
that's all I knew about my sexy developer.
"""
        print(ans_m)

    elif "who are you" in search or "about you" in search or "your details" in search :
        about = '''
        I am Jarvis an AI based python program
        but i can help you lot like a your close friend !
        send help to know about my commands!
        like playing music or video from your directory
        I can also play video and song from web or online !
        I can also entain you i so think you Understand me ! ok Lets Start...'''
        print(about)

    elif 'goodbye' in search or 'bye' in search or 'tata' in search :
        stMsgs = ['byeee cutie!',
              "Goodbye {}! ".format(NAME),
              "Ok {}! we'll talk later.. ".format(NAME),
              "it's Nice to meet you {}! ".format(NAME),
              "Have a Good day {}! ".format(NAME)]
        ans_bye = random.choice(stMsgs)
        print(ans_bye)
        print(exit())

    elif 'hidden' in search or 'secret' in search :
        os.system('Desktop\Jarvis-4.0.1\config.py')
        print('Enter any keyword that is in `xsearch` keywords in `config.py` file\n this will open your directory that is saved in `hidden_dir`',
              'Example enter `movu` if it is in `xsearch` keyword collection!')

    elif 'hello' in search or 'hi' in search or 'hii' in search or 'hola' in search or 'halo' in search :
        hello_Msgs = ['Hii cutie!',
              "Umm I was thinking about you.. {}! ".format(NAME),
              "Hii {}".format(NAME),
              "Hey {}! Any command for me? ".format(NAME),
              "it's Nice to meet you {}! ".format(NAME),
              "So {}, tell me what I've to do now! ".format(NAME)]
    # https://www.kuki-api.tk/api/apikey=XXXXXX/jarvis/@itzzzyashu/message=
        kuki_msg=(''+search)
        ans_hello = random.choice(hello_Msgs)
        print(ans_hello)
    
    elif 'photo' in search or 'photograph' in search or 'images' in search or 'pics' in search :
        print("opening pictures...")
        pics = os.listdir(pics_dir)
        os.startfile(os.path.join(pics_dir, pics[0]))

    elif 'music' in search or 'audio' in search :
        print("ok i am playing music...")
        musics = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, musics[0]))

    elif 'path' in search or 'directory' in search :
        path_i=input('Enter directory path : ')
        print("finding given path...")
        time.sleep(1)
        os.system(path_i)

    elif 'restarts' in search:
        print("Restarting...")
        time.sleep(1)
        os.system('Desktop\Jarvis-4.0.1\jarvis.py')
    
    elif 'vids' in search or 'video' in search :
        print("ok i am playing videos...")
        videos = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir, videos[0]))

    elif search in xsearch :
        print("ok playing hidden media! xD")
        hidden = os.listdir(hidden_dir)
        os.startfile(os.path.join(hidden_dir,hidden[0]))

        
    else:
        print(f"Sorry {NAME}, I'm still learning and I don't have any correct answer for your query.....",
              f"\nPlease press ENTER if you want me to search `{search}` on browser.")
        ggl_it=input()
        if ggl_it == '':
            print("Pushing your search to Web browser",
                  f"\nShowing you the results for `{search}`.")
            webbrowser.open('https://www.google.com/search?q='+search)
        else:
            print('starting again')
            
            
while True:
    jarvis()


# Update 4.0.1
