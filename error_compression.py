def graph(strs):
    group = 0
    while group < 2000:
        strsr = strs[group:group+30]
        interval = strsr.count('TAT')+strsr.count('TCT')+strsr.count('AGA')+strsr.count('ATA')\
                   +strsr.count('GAC')+strsr.count('GCG')+strsr.count('TGC')+strsr.count('GTC')\
                   +strsr.count('CAC')+strsr.count('ACT')+strsr.count('CGC')+strsr.count('GTG')
        print(group+30,interval)
        group = group+30
with open("bin_data/encode_base.txt") as f:
    origin_bin = f.read().strip()
    origin_bin = origin_bin.replace(" ", "").replace("\n", "")
graph(origin_bin)