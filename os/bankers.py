def banker_algorithm(num_processes, num_resources, allocation, max_need, available):
    # Initialize variables
    need = [[0] * num_resources for _ in range(num_processes)]
    finish = [False] * num_processes
    safe_sequence = []
    total_resources = list(available)

    # Calculate the need matrix
    for i in range(num_processes):
        for j in range(num_resources):
            need[i][j] = max_need[i][j] - allocation[i][j]

    # Check if a process can be allocated resources
    def can_allocate(process):
        for i in range(num_resources):
            if need[process][i] > available[i]:
                return False
        return True

    # Try to find a safe sequence
    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and can_allocate(i):
                for j in range(num_resources):
                    available[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True

        if not found:
            break

    # Check if all processes are finished
    if all(finish):
        # Calculate total resources
        for i in range(num_resources):
            total_resources[i] += sum(allocation[j][i] for j in range(num_processes))
        return need, safe_sequence, total_resources
    else:
        return None

# Example usage
def main():
    num_processes = int(input("Enter number of processes: "))
    num_resources = int(input("Enter number of resources: "))

    allocation = []
    max_need = []
    available = []

    print("Enter allocation matrix:")
    for _ in range(num_processes):
        allocation.append(list(map(int, input().split())))

    print("Enter max need matrix:")
    for _ in range(num_processes):
        max_need.append(list(map(int, input().split())))

    print("Enter available resources:")
    available = list(map(int, input().split()))

    # Run Banker's algorithm
    result = banker_algorithm(num_processes, num_resources, allocation, max_need, available)

    if result:
        need, safe_sequence, total_resources = result
        print("\nNeed Matrix:")
        for row in need:
            print(row)
        print("\nSafe sequence:", safe_sequence)
        print("\nTotal resources:", total_resources)
    else:
        print("Unsafe state. Deadlock detected.")

if __name__ == "__main__":
    main()
