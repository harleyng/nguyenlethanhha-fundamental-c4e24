from turtle import *

speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
canh = 2
goc = 0

for index, colour in enumerate(colors):
    color(colour)
    canh += 1
    goc = (1 - 2/canh)*180

    for _ in range(canh):
        forward(100)
        left(180 - goc)



mainloop()
