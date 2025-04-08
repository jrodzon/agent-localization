import matplotlib.pyplot as plt
import numpy as np

from argparse import ArgumentParser
from argparse import BooleanOptionalAction
from mpl_toolkits.axes_grid1 import ImageGrid

def get_image_list(name: str, algorithm: str, extension='.png', annotation=''):
    day = plt.imread('./output/' + name + annotation + '/' + algorithm + '/' + name + '_Day' + extension)
    day_depth = plt.imread('./output/' + name + annotation + '/' + algorithm + '/' + name + '_Day_dep.png')
    night = plt.imread('./output/' + name + annotation + '/' + algorithm + '/' + name + '_Night' + extension)
    night_depth = plt.imread('./output/' + name + annotation + '/' + algorithm + '/' + name + '_Night_dep.png')
    return [day_depth, day, night, night_depth]

def get_original_images(name: str):
    day = plt.imread('./resized/' + name + '_Day.jpg')
    night = plt.imread('./resized/' + name + '_Night.jpg')
    return [day, night]

def prepare_scene(name: str, annotation: str, vertical: bool):

    original_images = get_original_images(name)
    h, w, c = original_images[0].shape
    blank_image = 255 * np.ones(shape=(h, w, c), dtype=np.uint8)

    first_row_list = [blank_image] + original_images + [blank_image]
    planercnn_list = get_image_list(name, 'planercnn', annotation=annotation)
    plane_rec_net_list = get_image_list(name, 'PlaneRecNet', extension='.jpg', annotation=annotation)

    fig = plt.figure(figsize=(20., 15.))
    grid = ImageGrid(fig, 111,  # similar to subplot(111)
                    nrows_ncols=(3, 4),  # creates 2x4 grid of Axes
                    axes_pad=0.04,  # pad between Axes in inch.
                    share_all=True, # to disable ticks on axes only once
                    )
    
    # Disable ticks on axes
    grid[0].get_yaxis().set_ticks([])
    grid[0].get_xaxis().set_ticks([])

    # Remove borders on skipped blank images
    grid[0].spines['top'].set_visible(False)
    grid[0].spines['right'].set_visible(False)
    grid[0].spines['bottom'].set_visible(False)
    grid[0].spines['left'].set_visible(False)

    grid[3].spines['top'].set_visible(False)
    grid[3].spines['right'].set_visible(False)
    grid[3].spines['bottom'].set_visible(False)
    grid[3].spines['left'].set_visible(False)

    for ax, im in zip(grid, first_row_list + planercnn_list + plane_rec_net_list):
        # Iterating over the grid returns the Axes.
        ax.imshow(im)

    grid[0].grid(False)
    grid[3].grid(False)

    title_font_size = 30

    if vertical:
        grid[9].set_title("Original", rotation=90, x=-0.08, y=2.35, fontsize=title_font_size)
        grid[5].set_title("PlaneRCNN", rotation=90, x=-1.08, y=0.2, fontsize=title_font_size)
        grid[8].set_title("PlaneRecNet", rotation=90, x=-0.07, y=0.15, fontsize=title_font_size)
    else:
        grid[9].set_title("Original", rotation=90, x=-0.06, y=2.25, fontsize=title_font_size)
        grid[5].set_title("PlaneRCNN", rotation=90, x=-1.07, y=0.1, fontsize=title_font_size)
        grid[8].set_title("PlaneRecNet", rotation=90, x=-0.060, y=0.05, fontsize=title_font_size)
    grid[1].set_title("Day", fontsize=title_font_size)
    grid[2].set_title("Night", fontsize=title_font_size)
    grid[4].set_title("Day Depth", fontsize=title_font_size)
    grid[7].set_title("Night Depth", fontsize=title_font_size)

    plt.savefig('./results/' + name + ".png",bbox_inches='tight')


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-n", "--name")
    parser.add_argument("-a", "--annotation", default='')
    parser.add_argument("-v", "--vertical", action=BooleanOptionalAction)

    args = parser.parse_args()
    prepare_scene(args.name, args.annotation, args.vertical)
