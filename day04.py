

def find_adj_free_count(grid,x,y):
    xs = 0
    
    height = len(grid)
    width = len(grid[0])
    
    for i in range(-1,2):
        for j in range(-1,2):
            
            if y+i >= 0 and y+i < height and x+j >= 0 and x+j < width:
                if grid[y+i][x+j] == ".":
                    xs +=1
            else:
                xs +=1
    
    if xs > 4:
        return 1
    return 0

def do_the(grid):
    num = 0
    g = grid.copy()
    for y,line in enumerate(grid):
        for x,point in enumerate(line):
            
            if point == "@":
                val = find_adj_free_count(grid,x,y)
                num += val
                if val == 1:
                    g[y][x] = "."
    return num,g



if __name__ == "__main__":
    f = open("data/day04.txt") 
    grid = f.readlines()
    f.close()
    
    for i,line in enumerate(grid):
        grid[i] = line.strip()
    
    num = 0
    old_num = -1
    
    new_grid = grid.copy()
    new_grid = grid.copy()
    for o,l in enumerate(new_grid):
        new_grid[o] = list(l)
    
    
    while old_num!=num:
        N,new_grid = do_the(new_grid)
        old_num = num
        num += N
    
    print(new_grid)
    print(num)