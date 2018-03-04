## Running MPI on an AWS Server


**AWS**
- Create an Instance with 4 vCPUs


**Install MPI**

*Local*
- Download [latest version of mpi](https://www.open-mpi.org/software/ompi/v3.0/)
- I downloaded the tar file
- `scp openmpi-3.0.0.tar.gz ec2@...:`

*On EC2*
- `sudo yum install gcc`
- `sudo yum install gcc-c++`
- Unzip: `tar zxvf openmpi-3.0.0.tar.gz`
- `cd openmpi-3.0.0`
- Configure with `./configure --prefix=/usr/local`
  - or in a directory of your choice
- Make with `make all`
  - takes awhile
- `sudo make install`


**Python**

- `sudo yum install python34`
- `sudo yum install python34-pip`
- `python34 -m pip install --user mpi4py`

