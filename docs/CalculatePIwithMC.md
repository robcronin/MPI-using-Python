## Calculating π with Monte Carlo

**Commands**

- `python calculate_pi_MC.py -s [num_samples]`
- `mpiexec -n [procs] python calculate_pi_MC_MPI.py -s [num_samples]`


**Method**

- One of the simplest methods of calculating π is by using Monte Carlo(MC)
- Imagine you throw darts at a square of length 2 (area 4), completely randomly
- The circle inside the square, will have a radius of 1 and hence an area of π
- The proportion of darts inside the circle will hence be π/4
- If you multiply the proportion by 4 you will have an estimate of π


**Serial Method**

- The serial method implements this in [calculate\_pi\_MC.py](../calculate_pi_MC.py)
- It throws a dart by randomly generating an x and y coordiante in [-1, 1]\*[-1, 1]
- To see if the dart would be inside the circle, check if its distance is less than 1
  - i.e. x\*x + y\*y < 1^2 = 1
  - Due to squaring of x and y, you only have to generate x and y in [0, 1]\*[0, 1]
- Multiplying the proportion of darts passing this criteria by 4 will give you an estimate of π


**Parallel Method**

- This type of problem is the easiest and most efficient method to implement in parallel
- As each sample is computed independantly it doesn't matter which machine generates it, as long as the total proportion is computed
- [calculate\_pi\_MC\_MPI.py](../calculate_pi_MC_MPI.py) has each process run *samples/num_procs* simulations
  - Then rank 0 gathers and sums the number of passing samples
  - Rank 0 can then assume *samples* number of simulations have run, despite only running a fraction of this
  - It can then estimate π as before


**MPI Reduce**

- After all processes have run their simulations, one could make non rank 0's  `comm.send()` their values to rank 0 and have rank 0 loop through each process with a `comm.recv`
- However, their exists an MPI Reduce function that accounts for this situation
- `comm.reduce(data, operation, root)`:
  - `data`: data to be sent
  - `operation`: reduce operation to be carried out on all data (`MPI.SUM`, `MPI.PROD`, `MPI.MAX`, etc.)
  - `root`: rank which carries out this reduce operation and stores the result


**Similar Operations**

- See [tutorial](https://mpi4py.readthedocs.io/en/stable/tutorial.html#collective-communication)
  - MPI Bcast: Send data from one rank to all others
  - MPI Scatter: Break an array into chunks and send a chunk to each other process
  - MPI Gather: Gather chunks from each process into one array on given root process

