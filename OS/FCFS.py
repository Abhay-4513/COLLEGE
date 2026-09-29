def fcfs_scheduling(burst_time):
    n = len(burst_time)

    # Initialize arrays for waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate Waiting Time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Calculate Turnaround Time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Calculate Averages
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    # Display Results Table
    print("\nFCFS Scheduling Results")
    print("-" * 55)
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    print("-" * 55)
    for i in range(n):
        print(
            f"P{i + 1}\t"
            f"{burst_time[i]}\t\t"
            f"{waiting_time[i]}\t\t"
            f"{turnaround_time[i]}"
        )
    print("-" * 55)
    print(f"Average Waiting Time    : {avg_wt:.2f}")
    print(f"Average Turnaround Time : {avg_tat:.2f}")

    # Display Gantt Chart
    print("\nGantt Chart:")
    current_time = 0
    print("0", end="")
    for i in range(n):
        current_time += burst_time[i]
        print(f" -- P{i + 1} -- {current_time}", end="")
    print()


def main():
    n = int(input("Enter the number of processes: "))
    burst_time = []

    for i in range(n):
        bt = int(input(f"Enter Burst Time for Process P{i + 1}: "))
        burst_time.append(bt)

    fcfs_scheduling(burst_time)


if __name__ == "__main__":
    main()