import argparse
from random import random
from math import pi

parser = argparse.ArgumentParser(description="Calculate pi using Monte Carlo")
parser.add_argument('-s', dest='samples', default=1000, type=int, help='Number of MC samples to use')
samples = parser.parse_args().samples


passed = 0

for i in range(samples):
    x, y = random(), random()
    if(x*x + y*y < 1):
        passed +=1

print('Python\'s pi: %.6f\t'% (pi))
print('Estimate is: %.6f\t'% (passed*4/samples))
