import math

def range_check(rng):
    ids = rng.split("-")
    invalids2 = 0
    invalids = 0
    for id in range(int(ids[0]),int(ids[1])+1):
        id = str(id)
        ln = len(id)
#        print(id[:ln//2],id[ln//2:])
            
        if len(id)%2 == 0 and id[:ln//2]==id[ln//2:]:
            invalids += int(id)
        if not rep_check(id):
            invalids2 += int(id)
    return invalids, invalids2

def rep_check(id):
    for i in range(1,len(id)//2+1):
        block = id[:i]
        pseudo_id = (block * len(id))[:len(id)]
        if pseudo_id == id and len(id)%len(block)==0:
            print(id, block)
            return False
    return True




if __name__=="__main__":
    
    f = open("data/day02.txt")
    ranges = f.readline().split(",")

    f.close()
    #ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(",")
    invalids = (0,0)
    for rng in ranges:
        print("\n" + rng.strip() + "\n" + "-"*10)
        invs = range_check(rng)
        invalids = (invalids[0]+invs[0],invalids[1]+invs[1])
    print(invalids, invalids[0]+invalids[1])
