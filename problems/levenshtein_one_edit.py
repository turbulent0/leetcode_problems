s = "ab"
t = "ba"


    
def isOneEditDistance( s: str, t: str) -> bool:
    temp1 = s if len(s) < len(t) else t
    temp2  = s if len(s) >=len(t) else t
    for i, _ in enumerate(temp1):
        if temp1[i] != temp2[i]:
            if len(temp1) == len(temp2):
                return temp1[i+1:] == temp2[i+1:]
            elif len(temp2) - len(temp1) == 1:
                return temp1[i:]==temp2[i+1:]
            else:
                return False
    # if there is no diffs     
    return len(temp1)+1 == len(temp2)

print(isOneEditDistance(s,t))


            
            