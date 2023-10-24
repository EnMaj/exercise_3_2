from turtle import *

def soleil(n):
    color('red', 'yellow')
    while True:
        forward(n)
        left(190)
        if abs(pos())<1:
            break
def fan(n):
    color('green', 'yellow')
    for i in range(4):
        left(20)
        for j in range(4):
            forward(n)
            left(90)

def square(n):
    for i in range(4):
        forward(n)
        left(90)

begin_fill()
fan(100)
end_fill()