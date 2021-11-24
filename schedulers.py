from des import SchedulerDES
from event import Event, EventTypes
from process import Process, ProcessStates

class FCFS(SchedulerDES):
    def scheduler_func(self, cur_event):
        for process in self.processes:
            if cur_event.process_id == process.process_id:
                return process

    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        cur_process.run_for(cur_process.service_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        # we can only know the departure time of process once the process terminates!!
        timeWhenProcessEnds = cur_process.departure_time # this is the same as: self.time + cur_process.service_time
        event = Event(process_id = cur_process.process_id, event_type = EventTypes.PROC_CPU_DONE, event_time = timeWhenProcessEnds)
        return event

class SJF(SchedulerDES):
    def scheduler_func(self, cur_event):
        # lambda in Python = stream in Java
        self.processes.sort(key=lambda processes: processes.service_time, reverse=False) # reverse=False will sort in ascending order.
        for process in self.processes:
            if process.process_state == ProcessStates.READY:
                return process            

    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        cur_process.run_for(cur_process.service_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        # we can only know the departure time of process once the process terminates!!
        timeWhenProcessEnds = cur_process.departure_time # this is the same as: self.time + cur_process.service_time
        event = Event(process_id = cur_process.process_id, event_type = EventTypes.PROC_CPU_DONE, event_time = timeWhenProcessEnds)
        return event

class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        for process in self.processes:
            if cur_event.process_id == process.process_id:
                return process

    def dispatcher_func(self, cur_process):
        ''' cur_process will always not be terminated to start with, 
            i.e. will always be either new or ready, since insort() in des won't add a done event,
            i.e. event with a terminated process, to the queue, so cur_event should always be not done. '''
        cur_process.process_state = ProcessStates.RUNNING
        # (start_time = self.time)
        # (original_remaining_time = cur_process.remaining_time)
        timeAfterTimeQuantum = self.time + self.quantum
        cur_process.run_for(self.quantum, self.time)
        if cur_process.remaining_time != 0:
           cur_process.process_state = ProcessStates.READY
           event = Event(process_id = cur_process.process_id, event_type = EventTypes.PROC_CPU_REQ, event_time = timeAfterTimeQuantum)
        elif cur_process.remaining_time == 0:
           cur_process.process_state = ProcessStates.TERMINATED
           
           # cur_process.departure_time is the same as: start_time + original_remaining_time.
           event = Event(process_id = cur_process.process_id, event_type = EventTypes.PROC_CPU_DONE, event_time = cur_process.departure_time)
        return event


class SRTF(SchedulerDES):
    def scheduler_func(self, cur_event):
        # lambda in Python = stream in Java
        self.processes.sort(key=lambda processes: processes.remaining_time, reverse=False) # reverse=False will sort in ascending order.
        for process in self.processes:
            if process.process_state == ProcessStates.READY:
                return process  
                
    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        startTime = self.time
        nextEventStartTime = self.next_event_time()
        cur_process.run_for(nextEventStartTime-startTime, self.time)
        if cur_process.remaining_time != 0:
            cur_process.process_state = ProcessStates.READY
            event = Event(process_id = cur_process.process_id, event_type = EventTypes.PROC_CPU_REQ, event_time = nextEventStartTime)
        elif cur_process.remaining_time == 0:
            cur_process.process_state = ProcessStates.TERMINATED
            event = Event(process_id = cur_process.process_id, event_type = EventTypes.PROC_CPU_DONE, event_time = cur_process.departure_time)
        return event