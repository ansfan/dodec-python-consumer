#!/usr/bin/env python

class LED(object):
    x   = 0.0
    y   = 0.0
    rho = 0.0
    phi = 0.0
    color = 0.0
    area  = 300.0

    # The class "constructor" - It's actually an initializer
    def __init__(self, x, y, rho, phi):
        self.x   = float(x)
        self.y   = float(y)
        self.rho = float(rho)
        self.phi = float(phi)


    def to_string(self):
        return str(self.x) + "\t" + str(self.y) + "\t" + str(self.rho)+ "\t" + str(self.phi) + "\n"

