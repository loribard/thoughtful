
# hrt4rj -> Hrt4rj, hrt4RJ, HRT4RJ, HrT4rj
# hash_in_db(HRT4RJ) -> True/False

def all_possibilities(stringa):
    if stringa[0].isdigit():
        all_poss = [stringa[0]]
    else:
        all_poss = [stringa[0],stringa[0].upper()]
    stringa = stringa[1:]
    while stringa:
        char = stringa[0]
        if char.isdigit():
            for i in range(len(all_poss)):
                all_poss[i] += char
        else:
            all_poss_before = all_poss[:]
            for i in range(len(all_poss)):
                all_poss_before[i] += char
            for i in range(len(all_poss)):
                all_poss[i] += char.upper()
            all_poss.extend(all_poss_before)                 
        stringa = stringa[1:]
    return all_poss
                    
                    



print all_possibilities("h43ab6q")