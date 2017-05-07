from pyspark import SparkContext
from operator import add
from math import sqrt

if __name__ == '__main__':
    sc = SparkContext("local", "squareroot")    
    # Create an RDD of numbers from 1 to 1,000 and map 
    sqrts = sc.parallelize(range(1, 1001)).map(sqrt)
    # Compute the average of the square roots
    avg = sqrts.fold(0, add)/sqrts.count()
    print(avg)
