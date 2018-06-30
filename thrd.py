# Q1
'''from threading import *
import time
def message():
    time.sleep(5)
    print("This Is Your Message.. After Sleeping for 5Sec....")

t=Thread(target=message)
t.start()'''

# Q2
'''from threading import *
import time
def num():
    for i in range(1,11):
        print(i)
        time.sleep(1)

t=Thread(target=num)
t.start()'''

# Q3
'''from threading import *
import time
def list():
    list=[1,2,3,4,5]
    for i in range(len(list)):
        print(list[i])
        x=2*list[i]
        time.sleep(x)

t=Thread(target=list)
t.start()'''

# Q4
'''from threading import *
def factorial(num):

    if num == 1:
         return 1
    else:
         return (num * factorial(num-1))
    return 1 if num == 1 else (num * factorial(num-1))


num = int(input("Enter Number to be factorial:"))
print('Factorial of {} is {}'.format(num, factorial(num)))

t=Thread(target=factorial,args=(num,))
t.start()'''