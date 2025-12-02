import math

def state(dir, mag, previous):
    zeros = mag//100
    match dir:
        case "L":
            if previous!= 0 and (previous - mag%100)<=0:
                zeros += 1
            return (previous - mag)%100, zeros 
        case "R":
            if previous!= 0 and (previous + mag%100)>=100:
                zeros += 1
            
            return (previous + mag)%100, zeros
        


if __name__=="__main__":
    
    f = open("data/day01.txt")
    lines = f.readlines()
    f.close()
    zeros_count = 0
    zeros_count2 = 0
    st = 50
    #lines = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82","L2033"]
    for line in lines:
        st,cn = state(line[0],int(line[1:]),st)
        zeros_count2 += cn
        if st == 0:
            zeros_count += 1
    print(zeros_count, zeros_count2, st)