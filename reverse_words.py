
# 
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(id(s))
def reverse(s, start=0, end=len(s)):
    for i in range((end - start)//2):
        s[start + i], s[end-i-1] = s[end-i-1], s[start + i]
    return s

reverse(s) # reverse all string

start = 0
for i in range(len(s)+ 1):
    if i == len(s) or s[i]==' ':
        end = i
        reverse(s, start, end)                  
        start = end + 1
print(id(s)) 
print(s)

