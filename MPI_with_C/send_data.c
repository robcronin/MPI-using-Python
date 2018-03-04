#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int i, j;
int n = 10;

// prints a rank's array (no newline until the end)
void print_array(int *array, int rank){
    printf("Rank %d's array: ", rank);
    for(i=0; i < n; i++){
        printf("%3d  ", array[i]);
    }
    printf("\n");
}


int main(int argc, char *argv[]){

    int rank, size;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    // initialises array and fills with rank specific values
    int *array = malloc(n*sizeof(int));
    for(i=0; i < n; i++){
        array[i] = rank*100 + i;
    }

    print_array(array, rank);

    // Barrier that forces all processes to wait until they sync back up
    MPI_Barrier(MPI_COMM_WORLD);
    printf("Rank %d through the barrier\n", rank);

    // rank 0 sends its array to rank 1
    if(rank == 0){
        MPI_Send(array, n, MPI_INT, 1, 0, MPI_COMM_WORLD);
    }
    else if(rank == 1){
        MPI_Recv(array, n, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
    }

    print_array(array, rank);

    MPI_Finalize();
    
	return 0;
}