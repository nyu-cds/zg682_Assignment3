from numba import cuda
import numpy as np
from pylab import imshow, show

@cuda.jit(device=True)
def mandel(x, y, max_iters):
    '''
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the 
    Mandelbrot set given a fixed number of iterations.
    '''
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if ((z.real*z.real + z.imag*z.imag)>=4):
            return i

    return max_iters

@cuda.jit
def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
    """
    Set up the threads and compute.
    every thread is expressed as (ori_x+grdthread_x*i,ori_y+grdthread_y*j)
    where ori_x and ori_y are the start point
    """

    ori_y,ori_x=cuda.grid(2)#original point 
    height = image.shape[0]
    width = image.shape[1]
    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    grdthread_x,grdthread_y=blockdim[1]*griddim[1],blockdim[0]*griddim[0]
    range_x=round(width/grdthread_x)+1 #the number of points on axis x
    range_y=round(height/grdthread_y)+1#the number of points on axis y
    
    for i in range(range_x):
        x=ori_x+grdthread_x*i
        real = min_x + x * pixel_size_x#real part 
        for j in range(range_y):
            y=ori_y+grdthread_y*j
            if ((x<width) & (y<height)):
                imag = min_y + y * pixel_size_y#imagine part
                image[y, x] = mandel(real, imag, iters)



if __name__ == '__main__':
	image = np.zeros((1024, 1536), dtype = np.uint8)
	blockdim = (32, 8)
	griddim = (32, 16)
	
	image_global_mem = cuda.to_device(image)
	compute_mandel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, image_global_mem, 20) 
	image_global_mem.copy_to_host()
	imshow(image)
	show()
