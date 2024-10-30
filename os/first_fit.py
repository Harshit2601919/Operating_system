def first_fit():
    num_process=int(input("enter the  umber of process"))
    num_blocks=int(input("enter the number of blocks"))

    process=[]
    blocks=[]
    for i in range(num_blocks):
        blocks.append(int(input(f"enter the {i+1 } block")))

    for i in range(num_process):
        process.append(int(input(f"enter the {i+1} process")))

    allocation=[-1]*num_process

    for i in range(num_process):
        for j in range(num_blocks):
            if blocks[j]>process[i]:
                allocation[i]=j
                blocks[j]-=process[i]
                break

    print("process\tprocess size\tblock no")
    for i in range(num_process):
        print(i+1,"\t",process[i],"\t\t",allocation[i]+1)

first_fit()