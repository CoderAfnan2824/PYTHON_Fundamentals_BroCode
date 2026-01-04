'''
MultiThreading: It is used to perform multiple tasks concurrently
It's good for I/O bound tasks like reading file or fetching data from APIs

A thread is a lightweight unit of execution


'''

import threading, time

def walk_dog():
    print("Take dog for walk")
    time.sleep(3)

def remove_trash():
    print("Throw trash")
    time.sleep(0.002)

def get_mail():
    print("You get a mail")
    time.sleep(4)

#method with argument
def drive(car):
    print(f"I drove {car}")
    time.sleep(3)

#When you run all 3 methods one after another, it takes 8+2+4 secs, meanings they are 
# being run in same thread
walk_dog()
remove_trash()
get_mail()

#three threads are created for 3 tasks
thread1 = threading.Thread(target=walk_dog)
thread2 = threading.Thread(target=remove_trash)
thread3 = threading.Thread(target=get_mail)

#we give arguments as tuple; if we skip comma, we get error as interpretor think we are
#   passing string in parenthesis
thread4 = threading.Thread(target=drive,args=("car",))


#Now 3 tasks are started concurrently
thread1.start()
thread3.start()
thread2.start()
thread4.start()


#Main thread keeps waiting until 3 threads are finished. if we don't code below lines,
#   main print line is printed before end of the threads
thread3.join()
thread1.join()
thread2.join()
print("End of main thread")


