#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys, getopt
import numpy as np
from LED import LED

def parse(infilePath, outfilePath, scale):
    with open(infilePath) as infile:
        lines = infile.readlines()

    w, h = lines[1].strip().split("\t")
    lls  = lines[3:len(lines)]
    leds = []

    for ll in lls:
        x, y, rho, phi = ll.strip().split("\t")
        leds.append(LED(x, y, rho, phi))

    for led in leds:
        print(led.to_string())


    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    x1 = [led.x for led in leds]
    y1 = [led.y for led in leds]
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

    plt.scatter(x1, y1)
    # plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()



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

