#making some sort of digital clock with time module
import time    #a module
x = int(input("Input seconds: "))

for i in range(x):
    time.sleep(1)   # time.sleep from time module (pauses for 1 second)
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600) % 24
    days = x // 86400

    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}", end="\r")  #\r overwrites the previous output
    x -= 1    # -1 seconds per iteration
print("time's up!")