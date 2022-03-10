import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.colors import ListedColormap
import matplotlib


class SensorViz:
    def __init__(self,data=None,filename="quiver"):
        self.data=data
        # 2 dim arrays for x and y. These are the static locations of the arrows on the plot.
        # mgrid takes the format: np.mgrid[x_range_low:x_range_high:num_spots,y_range_low:y_range_high:num_spots]
        X, Y = np.mgrid[:2*np.pi:10j,:2*np.pi:5j]
        # U and V are grids where each corresponding spot has x and y values that define the arrows.
        U = np.cos(X)
        V = np.sin(Y)
        # Single color values for every spot. This would be the z value.
        C = np.hypot(U, V)

        # Initialize the quiver
        fig, ax = plt.subplots(1,1)
        # C argument can be used for the colors.
        # See all the cmaps at: https://matplotlib.org/stable/tutorials/colors/colormaps.html
        norm = matplotlib.colors.Normalize(vmin=0, vmax=1.5) # This sets the range for the colors.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html
        Q = ax.quiver(X, Y, U, V, C, pivot='mid', units='inches', norm=norm, cmap='inferno')
        ax.set_xlim(-1, 7)
        ax.set_ylim(-1, 7)

        # You need to set blit=False, or the first set of arrows never gets cleared on subsequent frames.
        # https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.animation.FuncAnimation.html
        hz = 20
        anim = animation.FuncAnimation(fig, self.update_quiver, fargs=(Q, X, Y), interval=1000 / hz, blit=False)
        fig.tight_layout()
        plt.show()

    def update_quiver(self,i, Q, X, Y):
        """updates the horizontal and vertical vector components by a
        fixed increment on each frame
        """
        U = np.cos(X + i*0.1)
        V = np.sin(Y + i*0.1)
        C = np.hypot(U, V)

        Q.set_UVC(U,V,C)

        return Q,

if __name__ == "__main__":
    _ = SensorViz(data=None,filename="quiver")