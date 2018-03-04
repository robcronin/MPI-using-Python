
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

**MPI4PY Package**
- Install with `pip install mpi4py`
- Run a test program `mpiexec pyton -m mpi4py.bench helloworld`