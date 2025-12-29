
import time
mytime = int(input("Enter time in seconds: "))

for x in range(mytime,0,-1):

    secs = x % 60
    mins = (int)(x / 60) % 60
    hours = (int)(x/3600)
    time.sleep(1)
    print(f"{hours:02}:{mins:02}:{secs:02}")

print("Time's up!")