n=int(input("enter the number of process"))
process=[]
finish_time=[]
burst_time=[]
arrivial_time=[]
turn_ariund_time=[]
waiting_time=[]
avg_turn_around_time=0
avg_waiting_time=0

for i in range(0,n):
    process.append(input("enter the process name"))
    burst_time.append(int(input(f"enter the burst time of {process[i]}:")))
    arrivial_time.append(int(input(f"enter the arrivial time of {process[i]}")))

finish_time.append(burst_time[0])
for i in range(1,n):
    finish_time.append(finish_time[i-1]+burst_time[i])



for i in range(0,n):
    turn_ariund_time.append(finish_time[i]-arrivial_time[i])

for i in range(0,n):
    avg_turn_around_time+=(turn_ariund_time[i]/n)


for i in range(0,n):
    waiting_time.append(turn_ariund_time[i]-burst_time[i])

for i in range(0,n):
    avg_waiting_time+=(waiting_time[i]/n)


print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format("process","arrival","bursttime","finish time","turnaround","waiting time"))
for i in range(0,n):
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(str(process[i]),str(arrivial_time[i]),str(burst_time[i]),str(finish_time[i]),str(turn_ariund_time[i]),str(waiting_time[i])))
print(f"avgerage turnaorund time :{avg_turn_around_time} \n average waiting time :{avg_waiting_time}")



print("\nGantt Chart:")
print("-" * 50)
print("|", end="")
for i in range(n):
    print("  ", process[i], " " * (burst_time[i] - len(process[i])), "|", end="")
print("\n" + "-" * 50)
print(0, end="")
for i in range(n):
    print(" " * (burst_time[i] + 2), finish_time[i], end="")
print()

    