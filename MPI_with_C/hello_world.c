#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]){

    // vars to store process ID(rank) and number of total processes(size)
    int rank, size;

    // starts up MPI for the processes running
    MPI_Init(&argc, &argv);

    // populates rank and size for processes on MPI_COMM_WORLD (default)
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    // each process prints their ID
    printf("Hello World, I am rank %d of %d\n", rank, size);

    // finished MPI
    MPI_Finalize();
    
	return 0;
}