# code for greeting user as per the current time using time module and if else statement

import time

h = int(time.strftime('%H'))

if h < 12:
    print("Good Morning!")
elif 12 <= h < 16:
    print("Good Afternoon!")
elif 16 <= h < 20:
    print("Good Evening!")
else:
    print("Good Night!")


