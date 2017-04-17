import numpy
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank() #setup rank
size=comm.Get_size() #setup size

datal= numpy.zeros(1)

if rank ==0: #when rank is 0, input the data
    data=101 #initialize the data
    while (data>=100) : #until data is less than 100, we stop the loop
        try:            #check if data is an interger
            data = input('input an integer less than 100: ')
            data =int(data) 
        except :
            print("not an int, try again")
            continue

    datal[0]=data
    comm.Send(datal, dest=1 )#send the number to rank 1
    comm.Recv(datal,source=size-1)#receive the number from the last rank 
    print(datal[0])

elif rank<size-1:                    #if the rank is not the last rank
    comm.Recv( datal,source=rank-1 )# receive the data from the previous rank
    datal =datal*(rank+1) # multiply the data by its rank
    comm.Send(datal,(rank+1)) #send the data to the next rank
else:                                 #if the rank is the last one
    comm.Recv( datal,source=rank-1 )
    comm.Send(datal,dest=0)                #send the data to the rank 0
