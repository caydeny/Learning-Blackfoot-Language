import pygame

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

def main():
    user_selection = 0
    while user_selection != 4:
        print("MAIN MENU")
        print("1. Learn - Word Flashcards")
        print("2. Play - Seek and Find Game")
        print("3. Settings")
        print("4. Exit")

        user_selection = int(input("Choose an Option: "))

        if user_selection == 1:
            learn()
        elif user_selection == 2:
            play()
        elif user_selection == 3:
            settings()
        else:
            print("Please enter a number between 1-3")

def learn():
    file = open("blackfoot.csv")
    for line in file:
        datalist = line.split(",")

def play():


def settings():
    

main()