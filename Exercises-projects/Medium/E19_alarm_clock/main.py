# Alarm Clock

import time, datetime, pygame
from pathlib import Path



def set_alarm(alarm_time): # input format > HH:MM:SS
    Base = Path(__file__).resolve().parent
    alarm_sound = Base/"alarm.mp3"

    is_running = True
    
    while is_running:

        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("Wake up! 🫨")
            pygame.mixer.init() #This will initialize mixer
            pygame.mixer.music.load(alarm_sound) # this will load our input music
            pygame.mixer.music.play()   # this will start playing music ( for 1-2 sed)
            #But to continue it playing, we add loop
            user_break = ""

            user_break = input("Enter value to stop alarm: ")
            pygame.mixer.music.stop()
                

            

            is_running = False
        elif current_time > alarm_time:
            print("Time already passed!")
            is_running = False
        
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter time to set alarm(HH:MM:SS): ")

    set_alarm(alarm_time)