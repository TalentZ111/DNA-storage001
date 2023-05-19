def graph(strs):
    group = 0
    while group < 600:
        strsr = strs[group:group+7]
        interval = strsr.count('G')+strsr.count('C')
        #interval = strsr.count('G')
        print(group+7,interval/7)
        group = group+7

graph('')