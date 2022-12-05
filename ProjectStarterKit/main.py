# Final Project
# Clifton Tan and Cayden Yoo
# Dec 5th, 2022

import pygame
import cmpt120image
import draw
import random

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################


file = open("blackfoot.csv")
lst = []
for line in file:
    lst.append(line.strip("\n"))

def main(number_of_words):
    user_selection = 0
    while user_selection != 4:
        print("MAIN MENU")
        print("1. Learn - Word Flashcards")
        print("2. Play - Seek and Find Game")
        print("3. Settings")
        print("4. Exit")

        user_selection = str(input("Choose an Option: "))
        options = ['1','2','3','4']
        if user_selection == options[0]:
            learn(number_of_words)
        elif user_selection == options[1]:
            play(number_of_words)
        elif user_selection == options[2]:
            number_of_words = settings()
        elif user_selection == options[3]:
            break
        else:
            print("Please enter a number between 1-4\n")

def learn(number_of_words):
    print("\nLEARN")
    for i in range(number_of_words):
        canvas = cmpt120image.getWhiteImage(400,300)
        item = cmpt120image.getImage("images/" + (lst[i])+".png")
        img = draw.distributeItems(canvas, item, 1)
        cmpt120image.showImage(img)
        playSound(lst[i], ENV)
        input("Click enter to continue.")
    img = cmpt120image.getWhiteImage(400,300)
    cmpt120image.showImage(img)
    print("")

def play(number_of_words):
    yes_or_no = ["yes", "no"]

    print("\nPLAY")
    while True:
        num_of_rounds = input("How many rounds would you like to play? ")
        if num_of_rounds.isdigit():
            num_of_rounds = int(num_of_rounds)
            break
        else:
            print("Please enter a number.")
            
    for i in range(num_of_rounds):
        words_to_shuffle = []
        canvas = cmpt120image.getWhiteImage(400,300)

        for j in range(number_of_words):
            words_to_shuffle.append(lst[j])

        random.shuffle(words_to_shuffle)
        for x in range(3):
            word = words_to_shuffle[x]
            img = cmpt120image.getImage("images/" + words_to_shuffle[x]+".png")
            number_of_imgs = random.randint(1,4)

            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)

            rgb = [r,g,b]

            img = draw.recolorImage(img,rgb)

            if word == words_to_shuffle[x]:
                answer = number_of_imgs

            minify = random.choice(yes_or_no)
            mirror = random.choice(yes_or_no)

            if minify == "yes":
                img = draw.minify(img)
            if mirror == "yes":
                img = draw.mirror(img)
            
            canvas = draw.distributeItems(canvas,img,number_of_imgs)
        
        cmpt120image.showImage(canvas)
        playSound(word, ENV)
        
        isTrue = True
        while isTrue:
            user_guess = input("Listen to the word. How many of them can you find? ")
            if user_guess.isdigit():
                if int(user_guess) == answer:
                    input("Right! Click enter to continue.")
                    isTrue = False
                else:
                    input("Wrong! Click enter to continue.\n") 
                    isTrue = False
            else:
                print("Please input a number.") 

def settings():
    print("\nOPTIONS")
    while True:
        question = input("How many words do you want to learn? ")
        if question.isdigit():
            if int(question) >= 3 and int(question) <= 12:
                number_of_words = int(question)
                return number_of_words
            else:
                print("Please enter a number between 3-13\n")
        else:
            print("Please enter a number between 3-12\n")

main(3)