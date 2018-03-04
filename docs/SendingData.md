## Sending Data

Now look at [send_data.py](../send_data.py) which should ideally be run with 2 processes (`mpiexec -n 2 python send_data.py`)

**Setup**
- Each rank/process initialises an array with values relating to its rank to distinguish them
- They each print their array
  - Note when printing, the string to be printed is assembled before any printing. If not, each value
    would print when ready, the processes would overlap and the print would be a mess.
- Then to sync up the prints, a barrier is thrown up with `comm.barrier()`. This forces all processes to
    wait until the last process reaches this stage
- Now rank 0 sends its array to rank 1 AND rank 1 receives this data overwriting its existing array

**Sending**
- Rank 0 calls the send() function
- `comm.send(array, destination, tag)`
  - `comm`: what communicator to send over
  - `array`: signifies the data to send
  - `destination`: what rank to send to
  - `tag`: a tag to distinguish sends
- This function should only be called by the sending process, hence the `if` statement
  - It is a blocking function(in most cases) meaning the code will wait until the corresponding `destination` process has received. Therefore if, say, all processes called `send()` first, the program will stall as they are all waiting for someone else to receive
  - It won't be a blocking function in this case as it is sending a small enough amount of data. But if this were to scale up, the data would need to be separated into smaller buffers and each buffer waits for the previous buffer to be received. In this case only one buffer would be used and the program could continue straight away (creating a false positive that the program works)

**Receiving**
- Rank 1 calls the corresponding receive function
- `comm.recv(array, source, tag)`
- This function has a source instead of a destination

**Successful Communication**
- In order for one process to send to another:
  - The Send's `destination` must be the Recv's rank
  - The Recv's `source` must be the Send's rank
  - The `tag` of both functions must match
  - They must both be using the same `comm`

**Results**

After the send, when both ranks print their array, we see they both have the values from rank 0
