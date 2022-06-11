import matplotlib.pyplot as plt
import numpy as np

def coin_flip_geo( f = lambda : np.random.randint(low = 0, high=2,size=10)):
  flips = 0
  while True:
    c = f()
    flips += 1
    if sum(c) == 10:
      return flips

def coin_flip_markov( f = lambda : np.random.randint(low = 0, high=2)):
  count = 0
  flips = 0
  while True:
    if count >= 10:
      return flips
    c = f()
    flips += 1
    count = count + 1 if c else 0

outcomes_geo = [coin_flip_geo() for _ in range(200)]
print("Flipping 10 coin at once and stopping when all 10 coins are heads. This experiment is repeated 100 times.")
print("Average number of throws: ", np.mean(outcomes_geo))
print("Using np.random.randint\n")

outcomes_markov = [coin_flip_markov() for _ in range(200)]
print("Flipping 10 coin and stopping when there are 10 in a row. This experiment is repeated 100 times.")
print("Average number of throws: ", np.mean(outcomes_markov))
print("Using np.random.randint\n")

axs = plt.subplots(1,2,sharex=False,sharey=True)
axs[1][0].hist(outcomes_geo, bins = 50)
axs[1][0].set(xlabel = "Flipping 10 coins at once")
axs[1][1].hist(outcomes_markov, bins = 50)
axs[1][1].set(xlabel = "Flipping until 10 heads in row")
plt.show()