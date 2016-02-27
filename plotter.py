#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from LED import LED

class Plotter(object):
    fig, ax = plt.subplots()  #create figure and axes
    leds = []
    w = 0.0
    h = 0.0

    def __init__(self, leds, w=100, h=100):
        self.leds = leds
        self.w = w
        self.h = h

        self.ax.set_aspect('equal')
        self.ax.set_xlim(0, float(self.w))
        self.ax.set_ylim(0, float(self.w))

        self.x = [led.x for led in self.leds]
        self.y = [led.y for led in self.leds]
        self.area = [led.area for led in self.leds]

        self.scatter = self.ax.scatter(self.x, self.y, s=self.area)

        plt.show()

        return


    def update_plot(self, colors):
        self.scatter.set_facecolors(colors)

        # self.ax.scatter(self.x, self.y, c=colors, s=self.area)
        plt.draw()

        return


    # def plot_animate(self, i):
    #     colors1 = np.random.rand(181)
    #     # self.line.set_ydata(c=colors1)  # update the data
    #     x1 = [led.x for led in self.leds]
    #     y1 = [led.y for led in self.leds]
    #     area1 = [led.area for led in self.leds]
    #     self.line, = self.ax.scatter(x1, y1, c=colors1, s=area1)
    #     return self.line,
    #
    #
    # # Init only required for blitting to give a clean slate.
    # def init(self):
    #     self.ax.set_aspect('equal')
    #     self.ax.set_xlim(0, float(self.w))
    #     self.ax.set_ylim(0, float(self.w))
    #     x1 = [led.x for led in self.leds]
    #     y1 = [led.y for led in self.leds]
    #     area1 = [led.area for led in self.leds]
    #     colors1 = np.random.rand(181)
    #     self.line, = self.ax.scatter(x1, y1, c=colors1, s=area1)
    #
    #
    # def start(self):
    #     self.ani = animation.FuncAnimation(self.fig, self.plot_animate, np.arange(1, 200), init_func=self.init,
    #                                   interval=25, blit=True)
    #     plt.show()



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

    def plot_animate():
        x = np.arange(6)
        y = np.arange(5)
        z = x * y[:, np.newaxis]

        for i in range(5):
            if i == 0:
                p = plt.imshow(z)
                fig = plt.gcf()
                plt.clim()   # clamp the color limits
                plt.title("Boring slide show")
            else:
                z = z + 2
                p.set_data(z)

            print("step", i)
            plt.pause(0.5)
