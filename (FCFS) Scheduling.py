from tabulate import tabulate

def get_processes_input():
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    
    for i in range(num_processes):
        process_name = input(f"Enter name for Process {i+1}: ")
        arrival_time = int(input(f"Enter Arrival Time (AT) for {process_name}: "))
        burst_time = int(input(f"Enter Burst Time (BT) for {process_name}: "))
        
        processes.append({"process": process_name, "AT": arrival_time, "BT": burst_time})
    
    return processes

def calculate_times(processes):
    processes.sort(key=lambda x: x["AT"])
    current_time = 0
    completion_times = []

    for process in processes:
        if current_time < process["AT"]:
            current_time = process["AT"]

        CT = current_time + process["BT"]
        TAT = CT - process["AT"]
        WT = TAT - process["BT"]
        completion_times.append({
            "process": process["process"],
            "AT": process["AT"],
            "BT": process["BT"],
            "CT": CT,
            "TAT": TAT,
            "WT": WT
        })

        current_time = CT
    
    return completion_times


def display_results(completion_times):
    table_data = [
        [item['process'], item['AT'], item['BT'], item['CT'], item['TAT'], item['WT']]
        for item in completion_times
    ]

    headers = ["Process", "Arrival Time (AT)", "Burst Time (BT)", "Completion Time (CT)", 
               "Turnaround Time (TAT)", "Waiting Time (WT)"]

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    avg_waiting_time = sum(item["WT"] for item in completion_times) / len(completion_times)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")

processes = get_processes_input()
completion_times = calculate_times(processes)
display_results(completion_times)
