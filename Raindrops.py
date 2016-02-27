
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


leds = []
window = []

def parse(infilePath, outfilePath, scale):
    with open(infilePath) as infile:
        lines = infile.readlines()

    w, h = lines[1].strip().split("\t")
    window.append(float(w))
    window.append(float(h))

    lls  = lines[3:len(lines)]
    for ll in lls:
        x, y, rho, phi = ll.strip().split("\t")
        leds.append(LED(x, y, rho, phi))

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




# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, window[0], window[0]], frameon=False)
ax.set_xlim(0, window[0]), ax.set_xticks([])
ax.set_ylim(0, window[0]), ax.set_yticks([])


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

# Construct the scatter which we will update during animation
# as the raindrops develop.
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')


def update(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_drops

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Make all circles bigger.
    rain_drops['size'] += rain_drops['growth']

    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (0, 0, 0, 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])








# Construct the animation, using the update function as the animation
# director.
animation = FuncAnimation(fig, update, interval=10)
plt.show()
