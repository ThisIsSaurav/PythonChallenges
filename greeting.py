import time

time_in_sec  = time.time()

result = time.localtime(time_in_sec)

if(result.tm_hour < 12 ):
    print("Good Morning")
elif(result.tm_hour >= 12 and result.tm_hour <= 16):
    print("Good AfterNoon")
else:
    print("Good Evening")