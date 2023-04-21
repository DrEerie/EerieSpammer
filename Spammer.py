#!/usr/bin/env python3

import pyautogui as eerie
import time as t
import sys
from colorama import *
from tqdm import tqdm
from termcolor import colored
# Create a function for typing animation
# Added this new feature i.e print_animation on Friday, April 21, 2023
# I got idea of this feature from team De-Technocrats repo blogvis at: github.com/De-Technocrats/blogvis .
def print_animation(text, color):
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        t.sleep(0.25)
    print()


# coded on Friday, April 7, 2023
print(Fore.CYAN + """
 _____          _      _____
|  ___|        (_)    /  ___|
| |__  ___ _ __ _  ___\ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __
|  __|/ _ \ '__| |/ _ \`--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
| |__|  __/ |  | |  __/\__/ / |_) | (_| | | | | | | | | | | |  __/ |
\____/\___|_|  |_|\___\____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|
                            | |
                            |_|
                    𝕱𝖔𝖗 𝖊𝖉𝖚𝖈𝖆𝖙𝖎𝖔𝖓 𝖕𝖚𝖗𝖕𝖔𝖘𝖊𝖘 𝖔𝖓𝖑𝖄.
        𝕯𝖔𝖓'𝖙 𝖋𝖔𝖗𝖌𝖊𝖙 𝖙𝖔 𝖌𝖎𝖛𝖊 𝖒𝖊 𝖘𝖙𝖆𝖗 𝖔𝖓 𝖌𝖎𝖙𝖍𝖚𝖇 𝖆𝖓𝖉  𝖋𝖔𝖑𝖑𝖔𝖜 𝖒𝖄 𝖈𝖗𝖊𝖆𝖙𝖔𝖗
                        𝖈𝖗𝖊𝖆𝖙𝖔𝖗 : 𝕯𝖗.𝕰𝖊𝖗𝖎𝖊

More TOOls:""" + Fore.CYAN + """ https://github.com/De-Technocrats
Telegram channel:""" + Fore.CYAN + """ https://t.me/DeTechnocrats
Youtube channel:""" + Fore.CYAN + """ https://www.youtube.com/@DeTechnocrats
""")
t.sleep(2)
print_animation("Vist THE ABOVE LINKS TO LEARN HACKING....","yellow")
t.sleep(2)
print_animation('Starting in 5 seconds....','green')
t.sleep(5)

while True:
    try:
        Bombcount = int(input(Fore.GREEN + "How many times you wanna Spam message: "))
        break
    except ValueError:
        print_animation("You have entered a non-numeric input. Please enter a number.", 'red')
        continue

Bombmessage = str(input(Fore.YELLOW + "Type your message that you wanna spam: "))  # accept numbers as well
t.sleep(1)
print("")
print_animation(
    "YOU HAVE TO ENTER AMOUNT OF TIME IN SECOND AS THE INPUT. YOU COULD ENTER TIME IN FRACTION SECOND AS WELL VIA USING DECIMAL POINT. ENTER ZERO FOR NULL","red")
t.sleep(1)
print("")
t.sleep(1)
while True:
    try:
        MsgGapTime = int(input(Fore.LIGHTMAGENTA_EX + "Enter time that you me to take gap between each message: "))
        break
    except ValueError:
        print_animation("You have entered a non-numeric input. Please enter a number.", 'red')
        continue

while True:
    try:
        autostart = int(input(Fore.LIGHTMAGENTA_EX + "Enter time that you wanna wait me before spamming: "))
        break
    except ValueError:
        print_animation("You have entered a non-numeric input. Please enter a number.", 'red')
        continue

#  your entered time would be considered in second.
print(
    Fore.RED + f"Make sure to click at the chat-box of your victim where you wanna spam messages after {autostart} seconds   \n𝔈𝔢𝔯𝔦𝔢𝔖𝔭𝔞𝔪𝔪𝔢𝔯 will start spamming after {autostart} seconds.... ")
t.sleep(autostart)

with tqdm(total=Bombcount) as pbar:
    for i in range(Bombcount):
        eerie.typewrite(Bombmessage)
        eerie.press('enter')
        pbar.update(1)
        t.sleep(MsgGapTime)  # Add a short delay between each message to avoid detection by anti-spam measures
