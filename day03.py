import itertools

def max_jolt(bank,length):
    def generate_seq(bank,length):
        return list(set(itertools.combinations(bank, length)))
    potentials = generate_seq(bank,length)
    potentials = [int("".join(i)) for i in potentials]
    potentials.sort(reverse=True)
    return potentials[0]

def max_joltage(bank):
    tmp_ind = -1
    highest_pot_ind = -1
    for val in range(9,-1,-1):
        indices = [i for i, x in enumerate(bank) if x == f"{val}"]
        if len(indices)==1:
            if tmp_ind == -1:
                tmp_ind = indices[0]
            else:
                if indices[0] > tmp_ind:
                    return int(f"{bank[min(tmp_ind,indices[0])]}{bank[max(tmp_ind,indices[0])]}")
                if highest_pot_ind == -1:
                    highest_pot_ind = indices[0]
                
        
        if len(indices)>1:
            if tmp_ind == -1:
                return int(f"{bank[indices[0]]}{bank[indices[1]]}")
            else:
                for index in indices:
                    if index > tmp_ind:
                        return int(f"{bank[tmp_ind]}{bank[index]}")
                if highest_pot_ind == -1:
                    highest_pot_ind = indices[0]
                
                
    return int(f"{bank[highest_pot_ind]}{bank[tmp_ind]}")
                

def max_j(bank,length):
    result = []
    min_index = 0
    
    l_bank = list(bank)
    l_bank = [int(i) for i in l_bank]
    for padding in range(length-1, -1, -1):
        p = l_bank[min_index:-padding]
        if padding !=0:
            max_val = max(l_bank[min_index:-padding])
        else:
            max_val = max(l_bank[min_index:])
        min_index = min_index + l_bank[min_index:].index(max_val)+1
        result.append(max_val)
    
    result = [str(i) for i in result]
    res = int("".join(result))
    return res

if __name__=="__main__":
    f = open("data/day03.txt")
    banks = f.readlines()
    f.close()
    
    
    
    
    
    
    bank_sum = (0,0)
    print("len: "+ str(len(banks[0])))
    for bank in banks:
        val1 = max_j(bank.strip(),2)
        val2 = max_j(bank.strip(),12)
        
        bank_sum = (bank_sum[0]+val1,bank_sum[1]+val2)
        print(bank_sum)