
"""
Rain simulation

Simulates rain drops on a surface by animating the scale and opacity
of 50 scatter points.

Author: Nicolas P. Rougier
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys, getopt
from LED import LED
import colorsys as cs
import serial
from struct import *
from threading import Thread, Lock


class Globals(object):
    colors = []

    def __init__(self):
        return


NUM_LEDS = 181
COLOR_BYTES = 3
BOARDS = 12

leds   = []
window = []

globals = Globals()

i = 0
while (i < NUM_LEDS):
    globals.colors.append(cs.hsv_to_rgb(0 / 255, 1.0, 1.0))
    i += 1


ser = serial.Serial(
    port='/dev/ttyS1',
    baudrate=9600,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS,
    rtscts=True,
    dsrdtr=True
)

# mutex = Lock()
# last_received = ''
# def receiving(ser, colors):
#     global last_received
#     buffer = []
#
#     while True:
#         while ser.inWaiting() > 0:
#             # line = ser.readline()
#             #
#             # string = line.decode()
#             #
#             # hexStrArray = string.strip().split(" ")
#
#             mutex.acquire()
#
#             colors.colors = ser.read(NUM_LEDS * COLOR_BYTES)
#
#             mutex.release()



def parse(infilePath, outfilePath, scale):
    with open(infilePath) as infile:
        lines = infile.readlines()

    w, h = lines[1].strip().split("\t")
    window.append(float(w) * ((BOARDS / 2) if (BOARDS > 1) else 1))
    window.append(float(h) * (2 if (BOARDS > 1) else 1))

    lls  = lines[3:len(lines)]
    for ll in lls:
        x, y, rho, phi = ll.strip().split("\t")
        leds.append(LED(x, y, rho, phi))

    i = 1
    while(i < BOARDS):
        j = 0
        while(j < NUM_LEDS):
            led = leds[j]

            if (i < BOARDS / 2):
                x_off = float(w) * i

                leds.append(LED(led.x + x_off, led.y, led.rho, led.phi))

            else:
                x_off = float(w) * (i - (BOARDS / 2))
                y_off = (2 * float(h))

                leds.append(LED(led.x + x_off, y_off - led.y, led.rho, led.phi))

            j+=1
        i+=1

    return



def main(argv):
    inputfile = ''
    outputfile = ''
    scale = 1000

    try:
        opts, args = getopt.getopt(argv,"hi:o:s:",["ifile=","ofile=","scale="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile> -s <scale>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile> -s <scale>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-s", "--scale"): # horizontal scale
            scale = float(arg)

    print('Input file is :', inputfile)
    print('Output file is :', outputfile)
    print('Scale is :', scale)

    parse(inputfile, outputfile, scale)




if __name__ == "__main__":
    main(sys.argv[1:])

    # ser = serial.Serial(
    #     port='/dev/ttyS1',
    #     baudrate=9600,
    #     stopbits=serial.STOPBITS_TWO,
    #     bytesize=serial.EIGHTBITS,
    #     rtscts=True,
    #     dsrdtr=True
    # )

    # Thread(target=receiving, args=(ser, colors, )).start()



# Create new Figure and an Axes which fills it.
#fig = plt.figure(figsize=(window[0], window[1]))
# ax = fig.add_axes([0, 0, window[0], window[0]], frameon=True)

fig, ax = plt.subplots()  #create figure and axes

#fig(figsize=(window[0], window[1]))
ax.set_aspect('equal')
ax.set_xlim(0, window[0])# if (window[0] > window[1]) else window[1])
ax.set_ylim(0, window[1])# if (window[0] > window[1]) else window[1])
# ax = fig.add_axes([0, 0, 1, 1], frameon=True)
# ax.set_xlim(0, 1), ax.set_xticks([])
# ax.set_ylim(0, 1), ax.set_yticks([])


# Create rain data
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth',   float, 1),
                                      ('color',    float, 4)])

# Initialize the raindrops in random positions and with
# random growth rates.
rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

x_data = [led.x for led in leds]
y_data = [led.y for led in leds]
area   = [led.area for led in leds]


# Construct the scatter which we will update during animation
# as the raindrops develop.
scat = ax.scatter(x_data, y_data,
                  s=area, alpha=1.0)#, lw=0.5,
                  #facecolors=colors)
# scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
#                   s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
#                   facecolors='none')

printStrs = ["r: ", "g: ", "b: ", "a: "]

def update(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % len(leds)

    # startingHue = frame_number % 255
    # colors = []
    #
    # i = 0
    # while (i < len(leds)):
    #     hue = startingHue if startingHue < 255 else startingHue - 255
    #     # r,g,b = cs.hsv_to_rgb(hue / 255)
    #     # rgba = [r, g, b, 1.0]
    #     colors.append(cs.hsv_to_rgb(hue / 255, 1.0, 1.0))
    #     startingHue += 1
    #     i += 1

    print("Frame: " + str(frame_number))

    # # Make all colors more transparent as time progresses.
    # rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    # rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)
    #
    # # Make all circles bigger.
    # rain_drops['size'] += rain_drops['growth']
    #
    # # Pick a new position for oldest rain drop, resetting its size,
    # # color and growth factor.
    # rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    # rain_drops['size'][current_index] = 5
    # rain_drops['color'][current_index] = (0, 0, 0, 1)
    # rain_drops['growth'][current_index] = np.random.uniform(50, 200)
    #
    # # Update the scatter collection, with the new colors, sizes and positions.
    # scat.set_edgecolors(rain_drops['color'])
    # scat.set_sizes(rain_drops['size'])
    # scat.set_offsets(rain_drops['position'])

    # colors = np.random.rand(len(leds))

    # mutex.acquire()

    # while True:
    inWaiting = ser.inWaiting

    if ser.inWaiting() > 0:
        print("We have stuff!!")
        buffer = ser.read(NUM_LEDS * BOARDS * COLOR_BYTES)

        ser.flush()

        l = len(buffer)
        arr = unpack(str(l) + 'c', buffer)

        print("length: " + str(l))

        i = 0
        while (i < COLOR_BYTES):
            byte = int.from_bytes(arr[i], byteorder='big')

            print(printStrs[i%COLOR_BYTES] + str(byte))

            i += 1

        globals.colors.clear()

        i = 0
        while (i < NUM_LEDS * BOARDS * COLOR_BYTES):
            j = 0
            tuple = []
            while (j < COLOR_BYTES):
                tuple.append(int.from_bytes(arr[i+j], byteorder='big') / 255)
                j += 1

            globals.colors.append(tuple)
            i += COLOR_BYTES

    else:
        print("We don't have stuff. :-(")

    #scat.set_facecolors(colors)
    scat.set_facecolors(globals.colors)

    # mutex.release()





# Construct the animation, using the update function as the animation
# director.
animation = FuncAnimation(fig, update, interval=10)
plt.show()
