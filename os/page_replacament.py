def fifo(page_references, num_frames):
    page_faults = 0
    frames = []
    for page in page_references:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
        print("Current Frames:", frames)
    return page_faults

def optimal(page_references, num_frames):
    page_faults = 0
    frames = []
    for page in page_references:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                index_list = []
                for frame in frames:
                    index_list.append(page_references.index(frame, page_references.index(page) + 1))
                frames[index_list.index(max(index_list))] = page
            page_faults += 1
        print("Current Frames:", frames)
    return page_faults


def lru(page_references, num_frames):
    page_faults = 0
    frames = []
    indexes = {}
    for i, page in enumerate(page_references):
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                lru_page = min(indexes, key=indexes.get)
                frames[frames.index(lru_page)] = page
                del indexes[lru_page]
            page_faults += 1
        indexes[page] = i
        print("Current Frames:", frames)
    return page_faults


def main():
    n=int(input("input number of pages"))
    page_reference=[]

    for i in range(n):
        page_reference.append(int(input(("enter the frames"))))

    num_frames=int(input("enter the fraframes"))
    page_faults=fifo(page_reference,num_frames)
    print("page faults",page_faults)
   
    page_faults=optimal(page_reference,num_frames)
    print("page faults",page_faults)
    page_faults=lru(page_reference,num_frames)
    print("page faults",page_faults)

if __name__ == "__main__":
    main()


