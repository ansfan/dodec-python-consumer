#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from LED import LED

def plot_cartesian(leds, colors, w=100, h=100):

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    x1 = [led.x for led in leds]
    y1 = [led.y for led in leds]
    colors = np.random.rand(N)
    colors1 = np.random.rand(181)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
    area1 = [led.area for led in leds]

    fig, ax = plt.subplots()  #create figure and axes
    ax.set_aspect('equal')
    ax.set_xlim(0, float(w))
    ax.set_ylim(0, float(w))

    ax.scatter(x1, y1, c=colors1, s=area1)

    plt.show()

    return



def plot_polar(leds, colors, w=100, h=100):

    fig, ax = plt.subplots()  #create figure and axes
    ax.set_aspect('equal')
    ax.set_xlim(0, float(w))
    ax.set_ylim(0, float(w))

    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    r1 = [led.rho for led in leds]
    theta1 = [led.phi for led in leds]
    area = 200 * r**2 * np.random.rand(N)
    colors = theta

    ax = plt.subplot(111, projection='polar')
    #c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.hsv)
    c = plt.scatter(theta1, r1, cmap=plt.cm.hsv)
    c.set_alpha(0.75)

    plt.show()

    return
