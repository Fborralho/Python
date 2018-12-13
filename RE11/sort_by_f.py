def sort_by_f(l):
    result = []
    final = []
    f = lambda x: 5 - x if x >= 5 else x
    for i in range(len(l)):
        result.append([f(l[i]), [l[i]]])
    result.sort()
    
    for i in range(len(result)):
        final.append(*(result[i][1]))
    return final


