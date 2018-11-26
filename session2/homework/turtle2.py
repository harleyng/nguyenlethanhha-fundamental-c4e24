from turtle import *

speed(0)

canh = 2
goc = 0

for i in range (4):
    canh += 1
    goc = (1 - 2/canh)*180
    
    if canh % 2 == 1 :      #color: xanh lẻ
        color("blue")       #       đỏ chẵn
    else:
        color("red")

    for j in range(canh):
        forward(100)
        left(180 - goc)



mainloop()
