import math

def FCFS(num_requests, cylinder, head_movement, starting_cylinder):
    total_head_movement = 0.0
    for i in range(1, num_requests):
        head_movement[i] = abs(cylinder[i - 1] - cylinder[i])
        total_head_movement += head_movement[i]
    average_seek_time = total_head_movement / num_requests

    print("\n-------------------------------------")
    print("| I/O REQUEST\t\t| TOTAL HEAD MOVEMENT |")
    print("-------------------------------------")
    for i in range(1, num_requests):
        print(f"| {cylinder[i]}\t\t\t\t| {head_movement[i]} |")
    print("-------------------------------------")
    print(f"| AVERAGE SEEK TIME IS : {average_seek_time} |")

def SSTF(num_requests, cylinder, head_movement, starting_cylinder):
    total_head_movement = 0.0
    for i in range(1, num_requests):
        for j in range(1, num_requests):
            if abs(cylinder[j] - starting_cylinder) > abs(cylinder[j + 1] - starting_cylinder):
                cylinder[j], cylinder[j + 1] = cylinder[j + 1], cylinder[j]
    for i in range(1, num_requests):
        head_movement[i] = abs(cylinder[i - 1] - cylinder[i])
        total_head_movement += head_movement[i]
    average_seek_time = total_head_movement / num_requests

    print("\n-------------------------------------")
    print("| I/O REQUEST\t\t| TOTAL HEAD MOVEMENT |")
    print("-------------------------------------")
    for i in range(1, num_requests):
        print(f"| {cylinder[i]}\t\t\t\t| {head_movement[i]} |")
    print("-------------------------------------")
    print(f"| AVERAGE SEEK TIME IS : {average_seek_time} |")

def SCAN(num_requests, cylinder, head_movement, starting_cylinder, max_cylinder):
    left_cylinder = []
    right_cylinder = []
    sum_head_movement = 0
    for i in range(1, num_requests):
        if cylinder[i] <= starting_cylinder:
            left_cylinder.append(cylinder[i])
        else:
            right_cylinder.append(cylinder[i])
    left_cylinder.append(0)
    right_cylinder.append(max_cylinder)
    left_cylinder.sort(reverse=True)
    right_cylinder.sort()
    disk_cylinder = left_cylinder + right_cylinder

    for i in range(1, num_requests):
        if i == 0:
            head_movement.append(abs(starting_cylinder - disk_cylinder[i]))
        else:
            head_movement.append(abs(disk_cylinder[i - 1] - disk_cylinder[i]))
        sum_head_movement += head_movement[i]

    print("\n-------------------------------------")
    print("| I/O REQUEST\t\t| TOTAL HEAD MOVEMENT |")
    print("-------------------------------------")
    for i in range(1, num_requests):
        print(f"| {disk_cylinder[i]}\t\t\t\t| {head_movement[i]} |")
    print("-------------------------------------")
    average_seek_time = sum_head_movement / num_requests
    print(f"| AVERAGE SEEK TIME IS : {average_seek_time} |")

if __name__ == "__main__":
    num_requests = int(input("Enter the Number of IO Request \n"))
    cylinder = [0] * 20
    head_movement = [0] * 20

    print("Enter the Cylinder No")
    for i in range(1, num_requests + 1):
        cylinder[i] = int(input())

    starting_cylinder = int(input("Enter the Starting Cylinder \n"))
    max_cylinder = int(input("Enter the Maximum Cylinder \n"))
    cylinder[0] = starting_cylinder

    print("FCFS")
    FCFS(num_requests, cylinder, head_movement, starting_cylinder)

    print("\nSSTF")
    SSTF(num_requests, cylinder, head_movement, starting_cylinder)

    print("\nSCAN")
    SCAN(num_requests, cylinder, head_movement, starting_cylinder, max_cylinder)
