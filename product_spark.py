from pyspark import SparkContext
from operator import mul

if __name__=='__main__':
    sc = SparkContext("local", "product")
    nums = sc.parallelize(range(1,1001))# Create an RDD from 1 to 1000
    result = nums.fold(1, mul)#set up default with 1,computing product via fold
    print(result)#print
