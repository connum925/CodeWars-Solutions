def filter_list(l):
    List=[]
    for element in l:
        if isinstance(element,(int,float)):
            List.append(element)
    return List