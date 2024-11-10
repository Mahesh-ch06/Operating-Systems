from tabulate import tabulate

class Process:
    def __init__(self, name, arrival_time, priority, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.priority = priority
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.completion_time = None

def schedule_processes(processes):
    time = 0
    context_switch_time = 1
    completed_processes = 0
    num_processes = len(processes)

    processes.sort(key=lambda p: (p.arrival_time, p.priority))

    while completed_processes < num_processes:
        available_processes = [p for p in processes if p.arrival_time <= time and p.remaining_time > 0]

        if not available_processes:
            time += 1
            continue

        current_process = min(available_processes, key=lambda p: p.priority)

        if current_process.start_time is None:
            current_process.start_time = time

        current_process.remaining_time -= 1
        time += 1

        if current_process.remaining_time == 0:
            current_process.completion_time = time
            completed_processes += 1

            if completed_processes < num_processes:
                time += context_switch_time

    table_data = []
    for p in processes:
        table_data.append([p.name, p.arrival_time, p.priority, p.burst_time, p.start_time, p.completion_time])

    headers = ["Process", "Arrival Time", "Priority", "Burst Time", "Start Time", "Completion Time"]

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    total_completion_time = max(p.completion_time for p in processes)
    print(f"Total Completion Time: {total_completion_time} units")

def get_process_input():
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    
    for i in range(num_processes):
        name = input(f"Enter name for Process {i+1}: ")
        arrival_time = int(input(f"Enter arrival time for {name}: "))
        priority = int(input(f"Enter priority for {name} (lower number = higher priority): "))
        burst_time = int(input(f"Enter burst time for {name}: "))
        
        process = Process(name, arrival_time, priority, burst_time)
        processes.append(process)
    
    return processes

processes = get_process_input()
schedule_processes(processes)
