import matplotlib.pyplot as plt
import numpy as np

from argparse import ArgumentParser
from mpl_toolkits.axes_grid1 import ImageGrid

def get_image_list(name: str, algorithm: str, extension='.png'):
    day = plt.imread('./output/' + name + '/' + algorithm + '/' + name + '_Day' + extension)
    day_depth = plt.imread('./output/' + name + '/' + algorithm + '/' + name + '_Day_dep.png')
    night = plt.imread('./output/' + name + '/' + algorithm + '/' + name + '_Night' + extension)
    night_depth = plt.imread('./output/' + name + '/' + algorithm + '/' + name + '_Night_dep.png')
    return [day, day_depth, night, night_depth]

def prepare_scene(name: str):
    
    planercnn_list = get_image_list(name, 'planercnn')
    plane_rec_net_list = get_image_list(name, 'PlaneRecNet', '.jpg')

    fig = plt.figure(figsize=(10., 10.))
    grid = ImageGrid(fig, 111,  # similar to subplot(111)
                    nrows_ncols=(2, 4),  # creates 2x4 grid of Axes
                    axes_pad=0.1,  # pad between Axes in inch.
                    share_all=True, # to disable ticks on axes only once
                    )
    
    # Disable ticks on axes
    grid[0].get_yaxis().set_ticks([])
    grid[0].get_xaxis().set_ticks([])

    for ax, im in zip(grid, planercnn_list + plane_rec_net_list):
        # Iterating over the grid returns the Axes.
        ax.imshow(im)
    
    # Version for one algorithm only
    # grid[0].set_ylabel("Day", rotation=90)
    # grid[2].set_ylabel("Night", rotation=90)
    # grid[2].set_xlabel("Plane detection")
    # grid[3].set_xlabel("Depth")

    grid[0].set_ylabel("PlaneRCNN", rotation=90)
    grid[4].set_ylabel("PlaneRecNet", rotation=90)
    grid[0].set_title("Day")
    grid[2].set_title("Night")
    grid[1].set_title("Day Depth")
    grid[3].set_title("Night Depth")

    plt.show()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-n", "--name")

    args = parser.parse_args()
    prepare_scene(args.name)
