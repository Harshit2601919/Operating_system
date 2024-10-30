def best_fit_allocation():
    num_blocks = int(input("Enter the number of memory blocks: "))
    num_processes = int(input("Enter the number of processes: "))

    blocks = []
    processes = []

    for i in range(num_blocks):
        blocks.append(int(input(f"Enter size of memory block {i + 1}: ")))

    for i in range(num_processes):
        processes.append(int(input(f"Enter size of process {i + 1}: ")))

    allocation = [-1] * num_processes

    for i in range(num_processes):
        best_fit_index = -1
        for j in range(num_blocks):
            if blocks[j] >= processes[i]:
                if best_fit_index == -1:
                    best_fit_index = j
                elif blocks[j] < blocks[best_fit_index]:
                    best_fit_index = j
        if best_fit_index != -1:
            allocation[i] = best_fit_index
            blocks[best_fit_index] -= processes[i]

    print("\nProcess No.\tProcess Size\tBlock No.")
    for i in range(num_processes):
        print(f"{i + 1}\t\t{processes[i]}\t\t{allocation[i] + 1 if allocation[i] != -1 else 'Not Allocated'}")

best_fit_allocation()