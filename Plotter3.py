import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os

n = 25 ## nr of agents
x,y = 10, 10 ## matrix of x by y dimension
dataX, dataY, binaryRaster = [],[],[]

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self):
        global n
        self.numpoints = n
        self.stream = self.data_stream()
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("My first Agent Based Model (ABM)",fontsize=14)
        self.ax.grid(True,linestyle='-',color='0.75')
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100, 
                                           init_func=self.setup_plot, blit=False,
                                           repeat=False)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        global x,y
        dataX,dataY = next(self.stream)
        self.scat = self.ax.scatter(dataY, dataX, c="tomato", s=20, animated=True)
        self.ax.axis([0, y, x, 0])
        return self.scat,

    def data_stream(self):
        """Generate a random walk (brownian motion). Data is scaled to produce
        a soft "flickering" effect."""
        global x,y, n

        dataX,dataY = self.createRandomData()

        #printing results to ascii for validation
        lines = []
        binaryData = np.zeros((x,y), dtype=np.int)
        for i in range(n):
            binaryData[dataX,dataY] =1
        for i in range(x):
            line = ""
            for j in range(y):
                line += str(binaryData[i,j])+ ","
            line= line[:-1]+ "\n"
            lines.append(line)
        lines.append("\n")

        yx = np.array([dataY,dataX])
        cnt = 0
        while cnt < 10:
            dataX,dataY = self.createRandomData()
            yx = np.array([dataY,dataX])

            #printing results to ascii for validation
            binaryData = np.zeros((x,y), dtype=np.int)
            for i in range(n):
                binaryData[dataX,dataY] =1
            for i in range(x):
                line = ""
                for j in range(y):
                    line += str(binaryData[i,j])+ ","
                line= line[:-1]+ "\n"
                lines.append(line)
            lines.append("\n")

            cnt+=1
            yield yx

        #printing results to ascii for validation

        outNm = os.getcwd()+"\\ScatterValidation.txt"
        outfile = open(outNm, "w")
        outfile.writelines(lines)
        outfile.close()
        return

    def update(self, i):
        """Update the scatter plot."""
        dataX, dataY = next(self.stream)
        self.scat = self.ax.scatter(dataX, dataY, c="tomato", s=20, animated=True)
        return self.scat,

    def show(self):
        plt.show()

    def createRandomData(self):
        """Positions n agents randomly on a raster of x by y cells.
        Each cell can only hold a single agent."""

        global x,y,n
        binaryData = np.zeros((x,y), dtype=np.int)
        newAgents = 0
        dataX,dataY = [],[]
        while newAgents < n:
            row = np.random.randint(0,x,1)[0]
            col = np.random.randint(0,y,1)[0]
            if binaryData[row][col] != 1:
                binaryData[row][col] = 1
                newAgents+=1

        for row in range(x):
            for col in range(y):
                if binaryData[row][col] == 1:
                    dataX.append(row)
                    dataY.append(col)
        return dataX, dataY

def main():
    global n, x, y, dataX, dataY, binaryRaster
    a = AnimatedScatter()
    a.show()
    return

if __name__ ==  "__main__":
    main()
