def lru(page_reference,num_frames):
    frames=[]
    indexes={}
    page_fault=0
    for i,page in enumerate(page_reference):
        if page not in frames:
            if len(frames)<num_frames:
                frames.append(page)
            else:
                lru_page=min(indexes,key=indexes.get)
                frames[frames.index(lru_page)]=page
                del indexes[lru_page]
            page_fault+=1
        indexes[page]=i
        print("current frames",frames)
    return page_fault