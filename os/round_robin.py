def round_robin_scheduling():
    n = int(input("Enter the number of processes: "))
    time_quantum = int(input("Enter the time quantum: "))

    processes = []
    arrival_time = []
    burst_time = []

    for i in range(n):
        processes.append(i + 1)
        arrival_time.append(int(input(f"Enter arrival time for process {i + 1}: ")))
        burst_time.append(int(input(f"Enter burst time for process {i + 1}: ")))

    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    current_time = 0
    index = 0

    # Gantt chart data
    gantt_chart = []

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > time_quantum:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum
                    gantt_chart.append((processes[i], current_time)) 
                else:
                    current_time += remaining_time[i]
                    waiting_time[i] = current_time - arrival_time[i] - burst_time[i]
                    remaining_time[i] = 0
                    completion_time[i] = current_time
                    gantt_chart.append((processes[i], current_time)) 
        if done:
            break

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Calculate average waiting and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print table
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t"
              f"{turnaround_time[i]}\t\t{completion_time[i]}")

    # Gantt Chart
    print("\nGantt Chart:")
    print("-" * 50)
    for i in range(len(gantt_chart)):
        print(f"| P{gantt_chart[i][0]}", end="")
    print("|")
    print("-" * 50)
    print(0, end="")
    for i in range(len(gantt_chart)):
        print(" " * 3, gantt_chart[i][1], end="")
    print()


# Call the function
round_robin_scheduling()
