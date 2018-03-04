
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



## Sending Data

Now look at [send_data.c](./send_data.c) which should ideally be run with 2 processes (`mpirun -n 2`)

**Setup**
- Each rank/process initialises an array with values relating to its rank to distinguish them
- They each print their array
  - Note when printing a newline isn't inserted until the end so that the whole array is put in a single print buffer. If not, each value would print when ready, the processes would overlap and the print would be a mess.
- Then to sync up the prints, a barrier is thrown up with `MPI_Barrier`. This forces all processes to wait until the last process reaches this stage
- Now rank 0 sends its array to rank 1 AND rank 1 receives this data overwriting its existing array

**Sending**
- Rank 0 calls the send function
- `MPI_Send(array pointer, number of values, value type, destination, tag, communicator)`
  - `array pointer`: signifies the start of the array in memory
  - `number of values`: the amount of values to send from that point in memory
  - `value type`: the type of the value (i.e. how many bytes each value uses)
  - `destination`: what rank to send to
  - `tag`: a tag to distinguish sends
  - `communicator`: what communicator to send over
- This function should only be called by the sending process, hence the `if` statement
  - It is a blocking function(in most cases) meaning the code will wait until the corresponding `destination` process has received. Therefore if, say, all processes called `MPI_Send` first, the program will stall as they are all waiting for someone else to receive
  - It won't be a blocking function in this case as it is sending a small enough amount of data. But if this were to scale up, the data would need to be separated into smaller buffers and each buffer waits for the previous buffer to be received. In this case only one buffer would be used and the program could continue straight away (creating a false positive that the program works)

**Receiving**
- Rank 1 calls the corresponding receive function
- `MPI_Recv(array pointer, number of values, value type, source, tag, communicator, status)`
- This function has a source instead of a destination as well as an additional status argument(which can be ignored for now)

**Successful Communication**
- In order for one process to send to another:
  - The Send's `destination` must be the Recv's rank
  - The Recv's `source` must be the Send's rank
  - The `tag` of both functions must match
  - They must both be using the same `communicator`

**Results**

After the send when both ranks print their array, we see they both have the values from rank 0
