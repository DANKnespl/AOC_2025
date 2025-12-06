import re

def load_data(path, p2=False):
    f = open(path)
    lines = f.readlines()
    f.close()
    ll = lines.copy()  

    if p2:
        un = set()
        for l,line in enumerate(ll):
            spaces = set([m.start(0) for m in re.finditer(" ",line)])
            if len(un)==0:
                un = un.union(spaces)
            else:
                un = un.intersection(spaces)
        
        for l,line in enumerate(lines[:-1]):
            ll = line.replace(" ","x")
            for i in un:
                ll = ll[:i] + ";" + ll[i + 1:]
            ll = ll.replace(";"," ")
            lines[l] = ll


    for l,line in enumerate(lines):
        lines[l] = line.strip().split()
    


    

    expresions = []
    for x in range(len(lines[0])):
        exp = []
        for y,_ in enumerate(lines):
            exp.append(lines[y][x])
        expresions.append(exp)


    if p2:
        fin = []
        for exp in expresions:
            new_exp = []
            for i,_ in enumerate(exp[:-1]):
                try:
                    new_val = "".join([val[i] for val in exp[:-1]]).rstrip("x").replace("x","0")
                    new_exp.append(new_val)
                except:
                    continue
            new_exp.append(exp[-1])
            fin.append(new_exp)
        expresions = fin

    for y,line in enumerate(expresions):
        for x in range(0,len(line)-1):
            expresions[y][x] = int(expresions[y][x])
        expresions[y] = Group(expresions[y][:-1],expresions[y][-1])
    
    return expresions

def mult(a,b):
    return a * b

def sums(a,b):
    return a+b

class Group():
    def __init__(self, operands, operator):
        if operator == "+":
            self.operation = sums
            self.neutral = 0
        if operator == "*":
            self.operation = mult
            self.neutral = 1
        self.operands = operands   
    
    def batch(self):
        out = self.neutral
        for b in self.operands:
            out = self.operation(out,b)
        return out




if __name__ == "__main__":
    grps = load_data("data/day06.txt", True)
    outs = []
    for grp in grps:
        outs.append(grp.batch())
    print(Group(outs,"+").batch())

