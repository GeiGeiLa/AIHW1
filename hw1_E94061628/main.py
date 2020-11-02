import os
import sys
from random import randint, random
from functions import func
from math import exp
maxf = sys.float_info.max
path = os.path.dirname(__file__)
def brute_force(xl,xh, yl, yh):
    minval = maxf
    gx, gy = (0,0)
    for x in range(xl, xh + 1) :
        for y in range(yl, yh + 1) :
            ret = func(x,y)
            if ret < minval:
                minval = ret
                (gx, gy) = (x,y)
    return (gx,gy, minval)

def simulated_annealing(xl, xh, yl, yh, temp , rate):
    li = [-1,1]
    # max temperature
    (ox, oy) = (randint(xl, xh+1) ,  randint(yl, yh+1) )
    
    ###
    old = sys.float_info.max
    ###
    while temp > 0.05:
        x_or_y = randint(0,1)
        offset = li[randint(0,1)]
        ###
        (nx, ny) =  ( ox + (1-x_or_y) * offset, oy + x_or_y * offset )
        if nx < xl or nx > xh:
            nx = ox
        if ny < yl or ny > yh:
            ny = oy
        new = func(nx, ny)
        ###

        de = new - old
        if de <= 0:
            (old, ox, oy) = (new, nx, ny)
        else:
            if exp(-1*de / temp) > random():
                (old, ox, oy) = (new, nx, ny)
        temp = rate * temp
    return (ox, oy,old)

def main():
    with open(path+'/input.txt') as file:
        xl, xh = ( int(s) for s in ( next(file) ).split(",") )
        yl, yh = ( int(s) for s in ( next(file) ).split(",") )
        (gx, gy, minval) = brute_force(xl, xh, yl, yh)
        print(gx,gy,format(minval,".3f") ,sep="\n")
        (temp, rate) = ( 900, 0.99992 )
        (gx, gy, minval) = simulated_annealing(xl, xh, yl, yh, temp, rate)
        print(gx,gy,format(minval,".3f") ,sep="\n")

if __name__ == "__main__":
    main()
