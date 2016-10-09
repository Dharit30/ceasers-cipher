a = input()
d = int(input())
s = ""
for i in a:
    if ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90:
        m = ord(i) + d
        if ord(i)<=90:
            if m>90:
                m = m - 26
        if ord(i)>=97:
            if m>122:
                m = m - 26
        s = s+ chr(m)
print(s)
            
            
        
        
