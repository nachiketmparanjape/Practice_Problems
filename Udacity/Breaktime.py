import webbrowser
import time

i = 1
print "This program Started on" + time.ctime()
while i < 4:
    time.sleep(10)
    webbrowser.open("https://www.google.com/?gws_rd=ssl")
    i += 1