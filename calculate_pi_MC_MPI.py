from mpi4py import MPI
import argparse
from random import random
from math import pi

parser = argparse.ArgumentParser(description="Calculate pi using Monte Carlo")
parser.add_argument('-s', dest='samples', default=1000, type=int, help='Number of MC samples to use')
samples = parser.parse_args().samples



comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

passed = 0

for i in range(int(samples/size)):
    x, y = random(), random()
    if(x*x + y*y < 1):
        passed +=1


passed = comm.reduce(passed, MPI.SUM, 0)

if rank == 0:
    print('Python\'s pi: %.6f\t'% (pi))
    print('Estimate is: %.6f\t'% (passed*4/samples))
