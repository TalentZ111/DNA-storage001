def graph(strs):
    group = 0
    while group < 600:
        strsr = strs[group:group+20]
        interval = strsr.count('G')+strsr.count('C')
        print(group+20,interval/20)
        group = group+20

with open("bin_data/encode_base.txt") as f:
    origin_bin = f.read().strip()
    origin_bin = origin_bin.replace(" ", "").replace("\n", "")
graph(origin_bin)
