'''
assignment 11 parallel sorting the data
author:GJgao
'''
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def inputNumSize():
        size_=input("input the size of the array")
        range_=input("input the range of the array")
        return (int(size_),int(range_))
        
def parallel_sorter():
        data=[]#initialize the data
        if rank == 0:
                (size_,range_)=inputNumSize()
                input_ = np.random.randint(0,range_,size_)
                #get the minimum number
                min_=min(input_)
                #get the max number
                max_=max(input_)
                #create bins
                bins = np.linspace(min_, max_, size)
                #checking which group each element in the data is placed 
                group= np.digitize(input_, bins) 
                for i in range(len(bins)):
                        data.append(input_[group==i])
        else:
                data = None

        #scatter the data to all the processors part by part
        data=comm.scatter(data, root=0)
        #sort the data in each processor
        data = np.sort(data)
        #gather the data back to the rank 0
        data= comm.gather(data, root=0)
        if rank == 0:
                #print the whole data out
                print(np.concatenate(data))
                return np.concatenate(data)

if __name__ == '__main__':
        parallel_sorter()


