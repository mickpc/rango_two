#!/usr/bin/python

"""
Demo of the histogram (hist) function with a few features.

In addition to the basic histogram, this demo shows a few optional features:

    * Setting the number of data bins
    * The ``normed`` flag, which normalizes bin heights so that the integral of
      the histogram is 1. The resulting histogram is a probability density.
    * Setting the face color of the bars
    * Setting the opacity (alpha value).

"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random



# example data
#mu = 100 # mean of distribution
#	sigma = 15 # standard deviation of distribution
#	x = mu + sigma * np.random.randn(10000)

#	num_bins = 50
	# the histogram of the data
#	n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
	# add a 'best fit' line
#	y = mlab.normpdf(bins, mu, sigma)
x = [1,2,3,4,5,6,7,8,9,10]
y = [random.randint(1,10) for _ in range(10)]
plt.plot(x, y, 'r--')
plt.xlabel('Time (hours)')
plt.ylabel('Power')
plt.title(r'Power produced by the Solar Plant')
	
# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.plot()
plt.savefig('myfig')
	
