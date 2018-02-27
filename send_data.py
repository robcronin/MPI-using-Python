from mpi4py import MPI

n = 10

# prints a rank's array (prints in one go)
def print_array(array, rank):
    print_string = 'Rank ' + str(rank)+': '
    for i in range(10):
        print_string += str(array[i]) + '  '
    print(print_string)


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# initialises array and fills with rank specific values
array = []
for i in range(n):
    array.append(rank*100+i)

print_array(array, rank)

# Barrier that forces all processes to wait until they sync back up
comm.barrier()
print('Rank ' + str(rank) + ' through barrier')

# rank 0 sends its array to rank 1
if rank == 0:
    comm.send(array, dest=1, tag=0)
elif rank == 1:
    array = comm.recv(source=0, tag=0)


print_array(array, rank)
