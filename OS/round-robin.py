from collections import deque


class Process:

    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


def round_robin_scheduling(processes, quantum):
    processes.sort(key=lambda x: x.arrival_time)
    ready_queue = deque()
    current_time = 0
    completed = 0
    n = len(processes)
    in_queue = [False] * n

    # Initialize queue with the first arriving process
    ready_queue.append(0)
    in_queue[0] = True

    print("\n--- Execution Timeline ---")
    while completed < n:
        if not ready_queue:
            # Handle idle CPU state
            next_arrival = min(
                [p.arrival_time for p in processes if p.remaining_time > 0]
            )
            current_time = max(current_time, next_arrival)
            for i in range(n):
                if (
                    processes[i].arrival_time <= current_time
                    and not in_queue[i]
                    and processes[i].remaining_time > 0
                ):
                    ready_queue.append(i)
                    in_queue[i] = True

        idx = ready_queue.popleft()
        p = processes[idx]

        # Execute for quantum or remaining time
        execution_time = min(p.remaining_time, quantum)
        print(
            f"Time {current_time}: Process P{p.pid} executes for {execution_time} units."
        )
        current_time += execution_time
        p.remaining_time -= execution_time

        # Add newly arrived processes to queue during this time step
        for i in range(n):
            if (
                processes[i].arrival_time <= current_time
                and not in_queue[i]
                and processes[i].remaining_time > 0
            ):
                ready_queue.append(i)
                in_queue[i] = True

        # Re-queue unfinished process or record stats if completed
        if p.remaining_time > 0:
            ready_queue.append(idx)
        else:
            p.completion_time = current_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed += 1

    # Print Results Table
    print("\n" + "=" * 65)
    print(
        f"{'PID':<6}{'Arrival':<10}{'Burst':<8}{'Complete':<10}{'Turnaround':<12}{'Waiting':<8}"
    )
    print("=" * 65)

    total_tat = sum(p.turnaround_time for p in processes)
    total_wt = sum(p.waiting_time for p in processes)

    for p in sorted(processes, key=lambda x: x.pid):
        print(
            f"P{p.pid:<5}{p.arrival_time:<10}{p.burst_time:<8}"
            f"{p.completion_time:<10}{p.turnaround_time:<12}{p.waiting_time:<8}"
        )
    print("=" * 65)
    print(f"Average Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Waiting Time   : {total_wt / n:.2f}")


def main():
    # Sample data: Process(PID, Arrival, Burst)
    process_list = [
        Process(1, 0, 5),
        Process(2, 1, 4),
        Process(3, 2, 2),
        Process(4, 4, 1),
    ]
    time_quantum = 2

    round_robin_scheduling(process_list, quantum=time_quantum)


if __name__ == "__main__":
    main()