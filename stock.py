'''
You are given an array of stock prices for a company for some period of time
(in the code below the array is stock_prices). Write a function that calculates
the time to buy and sell stock so that the profit is maximal.  Some rules that
you need to obey:
* You are permitted to perform only one buy and one sell.
* You must buy before you sell.
* Please mind your coding style.
* DO NOT copy/paste anything from the internet
* Comment all your code
'''

import matplotlib.pyplot as plt
import numpy as np

# the code below generates the stock prices, you may uncomment the plot call to
# see the graph

T = 2
mu = 0.1
sigma = 0.1
S0 = 20
dt = 0.01
N = round(T/dt)
t = np.linspace(0, T, N)
W = np.random.standard_normal(size=N)
W = np.cumsum(W)*np.sqrt(dt)
X = (mu-0.5*sigma**2)*t + sigma*W
stock_prices = S0*np.exp(X)

# plt.plot(t, stock_prices)
# plt.show()


def get_deal1(prices):
    ''' get_deal1 should return a tuple of 2 indices for the prices array, the 
    first one when to buy and the 2nd when to sell. Make it as efficient as you
    can.'''
    return (i1, i2)


def get_deal2(prices):
    ''' get_deal2 function must return exactly the same result as get_deal1, but
    it is allowed to be less efficient.'''
    return (i1, i2)
