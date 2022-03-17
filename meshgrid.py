## Import standard library function
import numpy as np

def get_meshgrid_points(x_range=(-1,1), y_range=(-1,1), x_res=3, y_res=5):
    ## Get co-ordinates
    x_cords = np.linspace(x_range[0], x_range[1], x_res)
    y_cords = np.linspace(y_range[0], y_range[1], y_res)

    ## xv and yv meshgrid
    xv, yv = np.meshgrid(x_cords, y_cords)

    return np.c_[xv.ravel(), yv.ravel()]


if __name__ == '__main__':
    print(get_meshgrid_points())
