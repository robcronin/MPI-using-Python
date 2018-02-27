from mpi4py import MPI

# populates rank and size for processes on MPI.COMM_WORLD (default)
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print('Hello World I am rank: ' + str(rank) + ' of ' + str(size))
