from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank() #setup rank
size=comm.Get_size() #setup size


if rank ==0: #when rank is 0, input the data
    data=101 #initialize the data
    while (data>=100) : #until data is less than 100, we stop the loop
        try:            #check if data is an interger
            data = input('input an integer less than 100: ')
            data =int(data) 
        except :
            print("not an int, try again")
            continue

    comm.send(data, dest=1 )#send the number to rank 1
    data = comm.recv(source=size-1)#receive the number from the last rank 
    print(data)

elif rank<size-1:                    #if the rank is not the last rank
    data = comm.recv( source=rank-1 )# receive the data from the previous rank
    data =data*rank # multiply the data by its rank
    comm.send(data,(rank+1)) #send the data to the next rank
else:                                 #if the rank is the last one
    data = comm.recv( source=rank-1 )
    data =data*rank
    comm.send(data,0)                #send the data to the rank 0
