#list comprehension

a = list(map(lambda x : x+10, [1,2,3]))
print(a)

b= [n*2 for n in range(1,10+1) if n%2 == 1]
c= [n+1 for n in range(1,10+1) if n%2 == 1]
print(b)
print(c)

"""
dic_a = {}

for key, value in original.items():
    a[key] = value;

dic_a = {key:value for key,value in original.items()}

"""
