## Hello World

**Run Test Program**
- See the test [hello_world.py](../hello_world.py)
- Run using `mpiexec python helloworld.py`
  - To specify say 4 processes: `mpiexec -n 4 python helloworld.py`
  - To run more processes than you have cores `mpiexec -n 4 --oversubscribe python helloworld.py`

**Explanation**

When this program is `mpirun -n 4`, it is run 4 times in parallel.
Each instance sees and executes the exact same code.

To distinguish the different processes, they can each request their ID known as their `rank` via `Get_rank()`.
These ranks are zero indexed.
They can also request the total number of processes being run using `Get_size()`.

Both of these are methods of a communicator, `MPI.COMM_WORLD`, as an argument.
By default all processes communicate via this communicator.
You can set up custom communicators in the program which only specific processes use.

[hello_world.py](../hello_world.py) simply asks each process to print our their ID.
You may notice order is not guaranteed as each process will execute as and when it reaches the print command.
