import sys

from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.colors import ListedColormap
import matplotlib
import pandas as pd
import numpy as np
import sys


class SensorViz:
    def __init__(self,data=None,filename="quiver"):
        self.data=data
        # 2 dim arrays for x and y. These are the static locations of the arrows on the plot.
        # mgrid takes the format: np.mgrid[x_range_low:x_range_high:num_spots,y_range_low:y_range_high:num_spots]
        X, Y = np.mgrid[:10:3j,:10:3j]
        # U and V are grids where each corresponding spot has x and y values that define the arrows.
        U = self.data[0][0]
        V = self.data[0][1]
        # Single color values for every spot. This would be the z value.
        C = self.data[0][2]

        # Initialize the quiver
        fig, ax = plt.subplots(1,1)
        # C argument can be used for the colors.
        # See all the cmaps at: https://matplotlib.org/stable/tutorials/colors/colormaps.html
        norm = matplotlib.colors.Normalize(vmin=0, vmax=6) # This sets the range for the colors.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html
        # Q = ax.quiver(X, Y, U, V, C, pivot='mid', units='inches', norm=norm, cmap='plasma')
        Q = ax.quiver(X, Y, U, V, C, pivot='mid', units='inches', norm=norm, cmap='coolwarm',width = .05, scale=1 / 0.5)
        ax.set_xlim(-3, 13)
        ax.set_ylim(-3, 13)

        # You need to set blit=False, or the first set of arrows never gets cleared on subsequent frames.
        # https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.animation.FuncAnimation.html
        hz = 500
        anim = animation.FuncAnimation(fig, self.update_quiver, fargs=(Q,), interval=1000 / hz, blit=False,save_count=sys.maxsize)
        anim.save('testing.mp4')
        fig.tight_layout()
        plt.show()

    def update_quiver(self,i, Q):
        """updates the horizontal and vertical vector components by a
        fixed increment on each frame
        """
        U = self.data[i][0]
        V = self.data[i][1]
        C = self.data[i][2]

        Q.set_UVC(U,V,C)

        return Q,

def data_prep():
    frames = []
    # 1st dim == frame num, 2nd dim == xforce grid(0), yforce grid(1), zforce grid(2)
    # Each grid is 2 dim array. 1st dim is row, 2nd dim is column of pillars.
    name_of_csv_file_written = 'hub_0-sensor_0.csv'
    dataframe = pd.read_csv(name_of_csv_file_written)
    data = dataframe.to_numpy()
    for sample in data:
        pillar_data = sample[6]
        pillar_data = pillar_data.strip('[]')
        pillar_data = pillar_data.split(',')
        xgrid, ygrid, zgrid = get_grids(pillar_data)
        frames.append([xgrid, ygrid, zgrid])
    return frames

def get_grids(pillar_data):
    xgrid = np.empty(0)
    ygrid = np.empty(0)
    zgrid = np.empty(0)
    for i, pillar in enumerate(pillar_data):
        pillar_list = pillar.split('\r\n')
        fx = pillar_list[10].split(':')
        fx = float(fx[1])
        fy = pillar_list[11].split(':')
        fy = float(fy[1])
        fz = pillar_list[12].split(':')
        fz = float(fz[1])
        xgrid = np.append(xgrid, fx)
        ygrid = np.append(ygrid, fy)
        zgrid = np.append(zgrid, fz)
    xgrid = list(xgrid.reshape(3, 3))
    ygrid = list(ygrid.reshape(3, 3))
    zgrid = list(zgrid.reshape(3, 3))
    return xgrid, ygrid, zgrid

if __name__ == "__main__":
    data=data_prep()
    _ = SensorViz(data=data,filename="quiver_test")