import math
import itertools

def euclidian_distance_3D(p,q):
    x_diff = pow(p[0]-q[0],2)
    y_diff = pow(p[1]-q[1],2)
    z_diff = pow(p[2]-q[2],2)
    return math.sqrt(x_diff+y_diff+z_diff)

def merge_pairs(pair1,pair2):
    if len((pair1.intersection(pair2)))!=0:
        return pair1.union(pair2)
    return pair1


def generate_pairs(coords):
    pairs = list(set(itertools.combinations(range(len(coords)), 2)))
    pairs = [list(pair) for pair in pairs]
    [pair.sort() for pair in pairs]
    pairs = [tuple(pair) for pair in pairs]
    
    
    pairs = list(set(tuple(pairs)))
    pairs = [tuple([pair[0],pair[1],euclidian_distance_3D(coords[pair[0]],coords[pair[1]])]) for pair in pairs]
    
    pairs.sort(key=lambda x:x[2])
    return pairs

def merger(pairs):
    #pairs = [(pair[0],pair[1]) for pair in pairs]
    sets = list(pairs)
    sets.sort()
    merged_trans = []
    j = 0
    while len(sets)!=0:
        merged = [j]
        used_set = sets[j]
        m_len = -1
        merg=[]
        while m_len == -1 or len(merg)!=m_len:
            m_len = len(merg)
            for bj, pair2 in enumerate(sets[j+1:]):
                merg = list(merge_pairs(set(used_set),set(pair2)))
                merg.sort()
                merg = tuple(merg)
                if len(set(pair2).intersection(set(used_set)))>0:
                    merged.append(bj+1+j)
                used_set = merg

        
        merged_trans.append(used_set)
        merged = sorted(set(merged), reverse=True)
        for id in merged:
            sets.pop(id)
        sets.sort()
    
    
    merged_trans = sorted(set(merged_trans))
    return merged_trans






    
def load_data(path):
    f = open(path)
    coords = f.readlines()
    f.close()
    coords = [coord.strip().split(",") for coord in coords]
    coords = [(int(coord[0]),int(coord[1]),int(coord[2])) for coord in coords]
    return coords

def solver(path, edges_of_interest):
    coords = load_data(path)
    pairs_dist = generate_pairs(coords)
    smalest_pairs = pairs_dist[:edges_of_interest]
    smalest_pairs = [(pair[0], pair[1]) for pair in smalest_pairs]
    cycles = merger(smalest_pairs)
    
    
    cycles = []
    full_cycle_id = -1
    partial_cycle_edges = 1
    for i in range(0,len(pairs_dist),1):
        cycles.append((pairs_dist[i][0],pairs_dist[i][1]))
        cycles = merger(cycles)
        cycles_lengths = [len(cycle) for cycle in cycles]
        cycles_lengths.sort(reverse=True)
        print(f"closest {i} pairs used, found cycles: {len(cycles)}, longest cycle: {cycles_lengths[0]}/{len(coords)}")
        if i==edges_of_interest-1:
            for cycle in cycles_lengths[:3]:
                partial_cycle_edges *= cycle
        if len(cycles) == 1 and len(cycles[0])== len(coords) and full_cycle_id==-1:
            full_cycle_id = i
        if full_cycle_id != -1 and i >= edges_of_interest:
            break
    print((partial_cycle_edges,coords[pairs_dist[full_cycle_id][0]][0]*coords[pairs_dist[full_cycle_id][1]][0]))


if __name__=="__main__":
    #solver("data/day08T.txt",10)
    solver("data/day08.txt",1000)    
