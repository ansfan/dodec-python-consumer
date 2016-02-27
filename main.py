#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys, getopt
import numpy as np
from LED import LED
import plotter as plotter


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

    plotter.plot_cartesian(leds, [], float(w), float(h))
    plotter.plot_polar(leds, [], float(w), float(h))

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

