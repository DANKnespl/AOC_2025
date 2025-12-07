


def load(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]
    return lines

def update_line(line,pointer,letter = "|",spliting = True):
    if spliting:
        new_line = line[:pointer-1] + letter + line[pointer] + letter + line[pointer+2:]
        
    else:
        new_line = line[:pointer] + letter + line[pointer+1:]
    return new_line


def get_past(used_splitters,pointer,lines):
    cc = [0,0]
    for c in range(lines-2,1,-2):
        for u, used in enumerate(used_splitters[c]):
            if used[0]==pointer-1 and  used_splitters[c][u][2][0]:
                cc[0] += used[1]
                used_splitters[c][u][2][0] = False
            if used[0]==pointer+1 and used_splitters[c][u][2][1]:
                cc[1] += used[1]
                used_splitters[c][u][2][1] = False
    if sum(cc)==0:
        return 1
    return sum(cc)

def simulate(lines):
    used_splitters = {}
    for y_coord,line in enumerate(lines[::2]):
        y_coord_simplified = y_coord*2
        for x_coord,point in enumerate(line):
            if point =="S":
                lines[1] = update_line(lines[1],x_coord,spliting=False)
            if lines[y_coord_simplified-1][x_coord] == "|":
                if point == "^":
                    if y_coord_simplified not in used_splitters.keys():
                        used_splitters[y_coord_simplified] = []
                    
                    used_splitters[y_coord_simplified].append((x_coord,get_past(used_splitters,x_coord,y_coord_simplified),[True,True]))

                    lines[y_coord_simplified] = update_line(lines[y_coord_simplified],x_coord)
                    lines[y_coord_simplified+1] = update_line(lines[y_coord_simplified+1],x_coord)
                if point == ".":
                    lines[y_coord_simplified] = update_line(lines[y_coord_simplified],x_coord, spliting=False)
                    lines[y_coord_simplified+1] = update_line(lines[y_coord_simplified+1],x_coord, spliting=False)
            elif lines[y_coord_simplified][x_coord] == "^":
                lines[y_coord_simplified] = update_line(lines[y_coord_simplified],x_coord,"@",False)

    for line in lines[::1]:
        print(line)
    return  used_splitters

def parse_sim(used_splitters):
    used_splitters_l = []
    
    lst = [spl[1] for spl in used_splitters.items()]
    [used_splitters_l.extend(line) for line in lst]

    timelines = sum([splitter[1]*splitter[2].count(True) for splitter in used_splitters_l])
    splittings = len(used_splitters_l)

    print(splittings, timelines)



if __name__ == "__main__":
    parse_sim(simulate(load("data/day07.txt")))
