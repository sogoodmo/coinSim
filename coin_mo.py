import os 
import random 
import json
import math
import matplotlib.pyplot as plt


'''
https://www.youtube.com/watch?v=rwvIGNXY21Y&ab_channel=singingbanana

This youtube video of someone trying to flip 'CONSECUTIVE_COUNT' (Originally 10) Heads in a row peaked my interest and was 
a great source of procrastniation while I was revising for my final second year exam.

So I thought it'd be a great idea to try to simulate it myself using some python.

Since this was a whim 'CONSECUTIVE_COUNT':00am small coding idea the variable naming isn't the best, 
but if you'd like to play around with it.

ITR => The number of simulations 
TRUE_RANDOM => If True -> Uses `os.urandom` to provide a better notion of 'Random'. Otherwise it uses the pseudorandom `random.randint(0,1)`
TARGET => The number of times each simulation is trying to achieve 'CONSECUTIVE_COUNT' Heads in a row 
DEBUG => Show analytics of each simulation 

What is interesting is I found that the avg attempts actually tends towards 2000ish (A bit more than what you'd expect with the 1024).
I thought because maybe I was using random.randint, and that isn't truly random. So I tried again using os.urandom - and I get similar results

That's either kinda cool, or I've made a very big logical error. More likley the latter :P

Maybe in the future I'll try to re-write this in C and add some vectorisation / multi-threading to calculate very large numbers.
'''


'''
'Flipping a coin' untill I get 'Heads' (1) 'CONSECUTIVE_COUNT' times in a row.
'''
def runTest():
    count = 0
    attempt = 0
    while (count != CONSECUTIVE_COUNT):
        if TRUE_RANDOM:
            count = 0 if round(int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)) == 0 else count + 1
        else:
            count = 0 if random.randint(0, 1) == 0 else count + 1
        attempt += 1
    return attempt 

'''
Trying to get 10Heads in a row "TARGET" amount of times 
'''
def flipCoin(simCount, TARGET):
    tries = [runTest() for _ in range(TARGET)]
    if DEBUG:
        print(f'\nSimulation: {simCount} | Target {CONSECUTIVE_COUNT}Head Count: {TARGET}\n\
        \nAttempts = {tries}\n\
        \nAvg attempts = {sum(tries)/len(tries)} \
        \nFastest Attempt = {min(tries)} \
        \nSlowest Attempt = {max(tries)} \
        \nMedian = {sorted(tries)[len(tries)//2]} \
        \nMode = {max(tries, key=tries.count)}')
    return sum(tries)/len(tries)


'''
Running the simulation "ITR" amount of times
'''
def runSimulation():
    avgCount = 0
    for simCount in range(ITR+1):
        avgCount += flipCoin(simCount, TARGET)
    print(f'\n\nTesting {ITR} simulations each trying to get {CONSECUTIVE_COUNT} Heads in a row 100 Times. \nAverage attempts to get {CONSECUTIVE_COUNT} heads in a row = {round(avgCount/ITR, 2)}\nUsing: {"os.urandom" if TRUE_RANDOM else "random.randint"}')
    return (CONSECUTIVE_COUNT, round(avgCount/ITR, 2))
TRUE_RANDOM = True
ITR = 100
TARGET = 100 
DEBUG = False
MAX_CONSEC = 10

'''
Find the average amount of heads from 1 -> "MAX_CONSEC" and output this data as a json.
'''
def main():
    global CONSECUTIVE_COUNT
    CONSECUTIVE_COUNT = 1
    avgDict = dict()
    for _ in range(MAX_CONSEC):
        target, avg = runSimulation()
        CONSECUTIVE_COUNT += 1
        avgDict[target] = math.log(avg)
        
    with open("out.json", "w") as f:
        f.write(json.dumps(avgDict))
        
    print(list(avgDict.values()))
    plt.xlabel("Target consectuive heads")
    plt.ylabel("Average amount of tosses (Log Scale)")
    plt.bar(list(avgDict.keys()), list(avgDict.values()))
    plt.show()
    

if __name__ == "__main__":
    main()