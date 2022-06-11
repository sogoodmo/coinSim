import os 
import random 

TRUE_RANDOM = True
ITR = 100
TARGET = 100 
DEBUG = False



'''
https://www.youtube.com/watch?v=rwvIGNXY21Y&ab_channel=singingbanana

This youtube video of someone trying to flip 10 Heads in a row peaked my interest and was 
a great source of procrastniation while I was revising for my final second year exam.

So I thought it'd be a great idea to try to simulate it myself using some python.

Since this was a whim 10:00am small coding idea the variable naming isn't the best, 
but if you'd like to play around with it.

ITR => The number of simulations 
TRUE_RANDOM => If True -> Uses `os.urandom` to provide a better notion of 'Random'. Otherwise it uses the pseudorandom `random.randint(0,1)`
TARGET => The number of times each simulation is trying to achieve 10 Heads in a row 
DEBUG => Show analytics of each simulation 

What is interesting is I found that the avg attempts actually tends towards 2000ish (A bit more than what you'd expect with the 1024).
I thought because maybe I was using random.randint, and that isn't truly random. So I tried again using os.urandom - and I get similar results

That's either kinda cool, or I've made a very big logical error. More likley the latter :P

Maybe in the future I'll try to re-write this in C and add some vectorisation / multi-threading to calculate very large numbers.
'''


def runTest():
    count = 1
    attempt = 0
    while (count != 10):
        if TRUE_RANDOM:
            count = 0 if round(int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)) == 0 else count + 1
        else:
            count = 0 if random.randint(0, 1) == 0 else count + 1
        attempt += 1
    return attempt 

def flipCoin(simCount, TARGET):
    tries = [runTest() for _ in range(TARGET)]
    if DEBUG:
        print(f'\nSimulation: {simCount} | Target 10Head Count: {TARGET}\n\
        \nAttempts = {tries}\n\
        \nAvg attempts = {sum(tries)/len(tries)} \
        \nFastest Attempt = {min(tries)} \
        \nSlowest Attempt = {max(tries)} \
        \nMedian = {sorted(tries)[len(tries)//2]} \
        \nMode = {max(tries, key=tries.count)}')
    return sum(tries)/len(tries)


avgCount = 0
for simCount in range(ITR+1):
    avgCount += flipCoin(simCount, TARGET)
print(f'\n\nTesting {ITR} simulations each trying to get 10 Heads in a row 100 Times. \n\nAverage attempts to get 10 heads in a row = {round(avgCount/ITR, 2)}\nUsing: {"os.urandom" if TRUE_RANDOM else "random.randint"}')