
def load_data(path):
    f = open(path)
    intervals = []
    while 1:
        line = f.readline().strip()
        if line == "":
            break

        interval = line.split("-")
        interval = [int(interval[0]), int(interval[1])]
        intervals.append(interval)
    ids  = f.readlines()
    ids = [int(id.strip()) for id in ids]
    f.close()
    return intervals,ids

def is_fresh(id, intervals):
    for interval in intervals:
        if id in range(interval[0],interval[1]+1):
            return True
    return False

def fresh_ids(intervals):
    def merge(intervals,lmbd = lambda x: x):
        sets_len = -1
        ints = intervals.copy()
        ints.sort(key=lmbd)
        sets = []
        finished = []
        while sets_len != len(sets):
            sets_len = len(sets)
            sets = []
            for i,interval1 in enumerate(ints):
                merged = False
                for interval2 in ints[i+1:]:
                    if interval1[1] + 1 < interval2[0]:
                        break
                    if interval1[1] <= interval2[1]:
                        sets.append([min(interval1[0],interval2[0]),max(interval1[1],interval2[1])])
                        merged = True
                        break
                if not merged:
                    finished.append(interval1)
            ints = sets.copy()
            ints.sort(key = lmbd)
        return finished

    front = merge(intervals)
    finished = merge(front,lambda x: x[1])

    dct = dict()
    for interval in finished:
        if interval[1] not in dct.keys():
            dct[interval[1]] = []
        dct[interval[1]].append(interval[0])
    
    fin = []
    
    for key in dct.keys():
        fin.append([min(dct.get(key)),key])
    return fin

if __name__ == "__main__":
    intervals,ids = load_data("data/day05.txt")
    cnt = 0
    for id in ids:
        if is_fresh(id,intervals):
            cnt +=1
    cnt2 = 0
    for interval in fresh_ids(intervals):
        cnt2 += len(range(interval[0],interval[1]+1))
    print(cnt,cnt2)