import time
t=input("Enter number of seconds: ")

def countdowwn(s):
    s=int(s)
    i=s
    while i>=0:
        minutes,seconds=divmod(i,60)
        timeformat="{:02}:{:02}".format(int(minutes),int(seconds))
        print(timeformat,end="\r")
        time.sleep(1)
        i-=1
    print("Fire in the hole!!!!!!")

countdowwn(t)