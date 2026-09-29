def srtf_scheduling(n, process, arrival, burst):
    # Copy burst time to track remaining execution time
    remaining = burst[:]
    completion = [0] * n
    time = 0
    completed = 0
    gantt = []

    # SRTF Scheduling Loop
    while completed < n:
        idx = -1
        minimum = float("inf")

        # Find process with shortest remaining time among arrived processes
        for i in range(n):
            if arrival[i] <= time and remaining[i] > 0:
                if remaining[i] < minimum:
                    minimum = remaining[i]
                    idx = i

        # If no process has arrived yet, CPU stays Idle
        if idx == -1:
            gantt.append("Idle")
            time += 1
            continue

        # Execute selected process for 1 time unit
        gantt.append(process[idx])
        remaining[idx] -= 1
        time += 1

        # Check if process completed execution
        if remaining[idx] == 0:
            completion[idx] = time
            completed += 1

    # Calculate Turnaround Time (TAT) and Waiting Time (WT)
    turnaround = []
    waiting = []
    total_tat = 0
    total_wt = 0

    for i in range(n):
        tat = completion[i] - arrival[i]
        wt = tat - burst[i]
        turnaround.append(tat)
        waiting.append(wt)
        total_tat += tat
        total_wt += wt

    # Calculate Averages
    avg_tat = total_tat / n
    avg_wt = total_wt / n

    # Display Results Table
    print("\n" + "=" * 50)
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    print("=" * 50)
    for i in range(n):
        print(
            f"{process[i]}\t"
            f"{arrival[i]}\t"
            f"{burst[i]}\t"
            f"{completion[i]}\t"
            f"{turnaround[i]}\t"
            f"{waiting[i]}"
        )
    print("=" * 50)

    # Display Averages
    print(f"Average Turnaround Time = {avg_tat:.2f}")
    print(f"Average Waiting Time    = {avg_wt:.2f}")

    # Display Gantt Chart
    print("\nGantt Chart:")
    print("-" * (len(gantt) * 6))
    for p in gantt:
        print(f"| {p:<4}", end="")
    print("|")
    print("-" * (len(gantt) * 6))

    print("0", end="")
    for i in range(1, len(gantt) + 1):
        print(f"{i:>6}", end="")
    print()


def main():
    n = int(input("Enter number of processes: "))
    process = []
    arrival = []
    burst = []

    for i in range(n):
        print(f"\nProcess P{i + 1}")
        arrival.append(int(input("Arrival Time: ")))
        burst.append(int(input("Burst Time: ")))
        process.append(f"P{i + 1}")

    srtf_scheduling(n, process, arrival, burst)


if __name__ == "__main__":
    main()