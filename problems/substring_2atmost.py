s = 'eceba'
left = 0
right = 0
length = 0
i = 0
d = {}
while i < len(s):
    if len(s) < 3:
        length = len(s) 
    d[s[i]] = i
    i += 1    
    if i == len(s):
        max_index = i
    if len(d) == 3:
        del_index = min(d.values())
        max_index = max(d.values())
        key = [i for i in d if d[i]==del_index]
        del d[key[0]]
        length = max(length, max_index - left)
        left = del_index + 1
length = max(length, max_index - left)
print(length)