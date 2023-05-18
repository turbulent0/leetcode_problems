def findStrobogrammatic( n: int) -> list[str]:
    # we can cash to faster calculation
    if n == 1:
        return ["0","1","8"]
    res = [''] if n%2 == 0 else ["0", "1", "8"]
    while n > 1:
        val_strob_nums = ["0", "1", "8", '6', '9'] if n > 3 else [ "1", "8", '6', '9']
        next_level = []
        for number in res:
            for j in val_strob_nums:
                if j == '6':
                    j_pair = '9'
                elif j == '9':
                    j_pair = '6'
                else:
                    j_pair = j
                next_level.append(j + number + j_pair)
        res= next_level
        n -= 2
    return res
    
print(findStrobogrammatic(4))