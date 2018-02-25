
## Install MPICC

Adapted from: [Installation Guide](https://wiki.helsinki.fi/display/HUGG/Open+MPI+install+on+Mac+OS+X)

**Download**
- Download [latest version of mpi](https://www.open-mpi.org/software/ompi/v3.0/)
- I downloaded the tar file
- Unzip: `tar zxvf openmpi-3.0.0.tar.gz`

**Install**
- `cd openmpi-3.0.0`
- Configure with `./configure --prefix=/usr/local`
  - or in a directory of your choice
- Make with `make all`
  - takes awhile
- `sudo make install`

## Hello World

**Run Test Program**
- See the test [helloworld.c](./helloworld.c) written in C
- Compile using `mpicc helloworld.c`
- Run using `mpirun ./a.out`
  - To specify say 4 processes: `mpirun -n 4 ./a.out`
  - To run more processes than cores `mpirun -n 4 --oversubscribe ./a.out`

**Explanation**

When this program is `mpirun -n 4`, it is run 4 times in parallel.
Each instance sees and executes the exact same code.

To distinguish the different processes, they can each request their ID known as their `rank` via `MPI_Comm_rank`.
These ranks are zero indexed.
They can also request the total number of processes being run using `MPI_Comm_size`.

Both of these functions take a communicator, `MPI_COMM_WORLD`, as an argument.
By default all processes communicate via this communicator.
You can set up custom communicators in the program which only specific processes use.

[helloworld.c](./helloworld.c) simply asks each process to print our their ID.
You may notice order is not guaranteed as each process will execute as and when it reaches the print command.
