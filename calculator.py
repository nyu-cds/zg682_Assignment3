# -----------------------------------------------------------------------------
# calculator.py
'''
Original code's analysis line by line: 
Timer unit: 3.77581e-07 s

Total time: 3.43848 s
File: <ipython-input-2-b142caa8fdc3>
Function: hypotenuse at line 42

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    42                                           def hypotenuse(x,y):
    43                                               """
    44                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    45                                               x and y must be two-dimensional arrays of the same shape.
    46                                               """
    47         1      2910330 2910330.0     32.0      xx = multiply(x,x)
    48         1      2221276 2221276.0     24.4      yy = multiply(y,y)
    49         1      2217171 2217171.0     24.3      zz = add(xx, yy)
    50         1      1757835 1757835.0     19.3      return sqrt(zz)

    16                                           def multiply(x,y):
    17                                               """
    18                                               Multiply two arrays using a Python loop.
    19                                               x and y must be two-dimensional arrays of the same shape.
    20                                               """
    21         1           41     41.0      0.0      m,n = x.shape
    22         1          395    395.0      0.0      z = np.zeros((m,n))
    23      1001         1114      1.1      0.0      for i in range(m):
    24   1001000      1058265      1.1     27.6          for j in range(n):
    25   1000000      2777927      2.8     72.4              z[i,j] = x[i,j] * y[i,j]
    26         1            1      1.0      0.0      return z

    16                                           def multiply(x,y):
    17                                               """
    18                                               Multiply two arrays using a Python loop.
    19                                               x and y must be two-dimensional arrays of the same shape.
    20                                               """
    21         1           43     43.0      0.0      m,n = x.shape
    22         1          292    292.0      0.0      z = np.zeros((m,n))
    23      1001         1396      1.4      0.0      for i in range(m):
    24   1001000      1138236      1.1     27.7          for j in range(n):
    25   1000000      2975259      3.0     72.3              z[i,j] = x[i,j] * y[i,j]
    26         1            5      5.0      0.0      return z

     3                                           def add(x,y):
     4                                               """
     5                                               Add two arrays using a Python loop.
     6                                               x and y must be two-dimensional arrays of the same shape.
     7                                               """
     8         1           37     37.0      0.0      m,n = x.shape
     9         1          255    255.0      0.0      z = np.zeros((m,n))
    10      1001         1095      1.1      0.0      for i in range(m):
    11   1001000       926709      0.9     26.6          for j in range(n):
    12   1000000      2560964      2.6     73.4              z[i,j] = x[i,j] + y[i,j]
    13         1            3      3.0      0.0      return z

    29                                           def sqrt(x):
    30                                               """
    31                                               Take the square root of the elements of an arrays using a Python loop.
    32                                               """
    33         1           71     71.0      0.0      from math import sqrt
    34         1           28     28.0      0.0      m,n = x.shape
    35         1          359    359.0      0.0      z = np.zeros((m,n))
    36      1001         1189      1.2      0.0      for i in range(m):
    37   1001000      1020236      1.0     32.5          for j in range(n):
    38   1000000      2113635      2.1     67.4              z[i,j] = sqrt(x[i,j])
    39         1            2      2.0      0.0      return z

    I think what really matter are the nested loops in add, multiplied and sqrt
    function. We can solve that by calling the functions in Numpy.

    After the modification，
    
Total time: 0.0204917 s
File: <ipython-input-1-ad5fefa7a592>
Function: hypotenuse at line 28

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    28                                           def hypotenuse(x,y):
    29                                               """
    30                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    31                                               x and y must be two-dimensional arrays of the same shape.
    32                                               """
    33         1        13295  13295.0     24.5      xx = multiply(x,x)
    34         1        20165  20165.0     37.2      yy = multiply(y,y)
    35         1        10199  10199.0     18.8      zz = add(xx, yy)
    36         1        10612  10612.0     19.6      return sqrt(zz)

The improvement is 167.79 times
''' 
# ----------------------------------------------------------------------------- 
import numpy as np

def add(x,y):
 
    return np.add(x,y)


def multiply(x,y):

    return np.multiply(x,y)


def sqrt(x):

    return np.sqrt(x)


def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)
