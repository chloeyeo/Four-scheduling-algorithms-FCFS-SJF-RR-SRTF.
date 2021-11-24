# Four-scheduling-algorithms-FCFS-SJF-RR-SRTF.
Uses and extends a simple discrete event simulator written in Python, by creating classes that simulate the scheduling and dispatching of processes performed by four scheduling algorithms: First-Come-First-Served (FCFS), Shortest-Job-First (SJF), Round-Robin (RR) and Shortest-Remaining-Time-First (SRTF). 

To execute the program with the command-line, add the arguments -S 851898649 where 851898649 would be the seed number.

Making use of object oriented programming in Python, this program implements the following
four scheduling algorithms:

• FCFS/FIFO (first-come-first-serve/first-in-first-out) (non-pre-emptive, i.e. process 
cannot be interrupted in the middle):Processes should be executed in the order in
which they arrived at the system. Conceptually, when a process arrives at the
system, it is added to a queue. The scheduling algorithm will always pick the
first process in the queue and will execute it to completion. It will then proceed
with the next process in the queue, and so on.

• SJF (shortest-job-first) (non-pre-emptive): Processes are prioritised based on their service time.
Conceptually, on arrival, processes are added to a priority queue, which is
sorted in ascending order of service time. The scheduling algorithm will then
always pick the first process in the queue and will execute it to completion. It
will then proceed with the next process in the queue, and so on.

• RR (round-robin) (pre-emptive, i.e. process can be interrupted in the
middle): On arrival, processes are added to a queue. Conceptually,
the algorithm will pick the first process in the queue, execute it for a specified
amount of time (also known as a time-slice or quantum), and if the process
needs more time it will then be added to the end of the queue.

• SRTF (shortest-remaining-time-first) (pre-emptive): This is a pre-emptive version of the SJF algorithm above.
Conceptually, whenever a change occurs in the system (i.e., a new process
arrives, a running process terminates, etc.), the scheduler is called to select the
process among those in the READY state with the minimum remaining
execution time. This process will then be pre-empted when a new change
occurs that results in some other process having a lower remaining execution
time than the currently executing one.
