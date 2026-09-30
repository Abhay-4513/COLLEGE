def priority_scheduling(processes):
    n = len(processes)
    completed = []
    current_time = 0
    ready_queue = []

    # Keep a copy of the processes to track remaining tasks
    remaining_processes = processes.copy()

    while len(completed) < n:
        # 1. Fetch all processes that have arrived by the current time
        arrived = [
            p for p in remaining_processes if p["arrival"] <= current_time
        ]
        for p in arrived:
            ready_queue.append(p)
            remaining_processes.remove(p)

        # 2. Handle CPU idle state if no processes have arrived yet
        if not ready_queue:
            if remaining_processes:
                current_time = min(p["arrival"] for p in remaining_processes)
                continue

        # 3. Sort ready queue by priority (Ascending: lower number = higher priority)
        # If priorities match, fall back to Arrival Time (FCFS rule)
        ready_queue.sort(key=lambda x: (x["priority"], x["arrival"]))

        # 4. Pick and execute the highest priority process
        current_process = ready_queue.pop(0)
        start_time = current_time
        completion_time = start_time + current_process["burst"]
        turnaround_time = completion_time - current_process["arrival"]
        waiting_time = turnaround_time - current_process["burst"]

        completed.append(
            {
                "id": current_process["id"],
                "arrival": current_process["arrival"],
                "burst": current_process["burst"],
                "priority": current_process["priority"],
                "completion": completion_time,
                "turnaround": turnaround_time,
                "waiting": waiting_time,
            }
        )

        # Update system clock
        current_time = completion_time

    # Display scheduling data
    print(
        f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}"
        f"{'Exit':<10}{'Turnaround':<12}{'Waiting':<8}"
    )
    print("-" * 70)

    total_tat, total_wt = 0, 0
    for p in completed:
        print(
            f"{p['id']:<10}{p['arrival']:<10}{p['burst']:<10}{p['priority']:<10}"
            f"{p['completion']:<10}{p['turnaround']:<12}{p['waiting']:<8}"
        )
        total_tat += p["turnaround"]
        total_wt += p["waiting"]

    print("-" * 70)
    print(f"Average Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Waiting Time   : {total_wt / n:.2f}")


def main():
    # Example Dataset: (Process ID, Arrival Time, Burst Time, Priority)
    example_processes = [
        {"id": "P1", "arrival": 0, "burst": 4, "priority": 2},
        {"id": "P2", "arrival": 1, "burst": 3, "priority": 1},
        {"id": "P3", "arrival": 2, "burst": 1, "priority": 4},
        {"id": "P4", "arrival": 3, "burst": 5, "priority": 3},
    ]

    priority_scheduling(example_processes)


if __name__ == "__main__":
    main()