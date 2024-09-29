size=int(input("Lug'atgalarga hajmilarini kiriting: "))
dict1=dict()
print()
for key in range(size):
    value=int(input("Kalit soniga int formatida qiymat kiriting: "))
    dict1[key+1]=value
start=key
dict2=dict()
print()
for key in range(start+1,size*2):
    value=int(input("Kalit soniga int formatida qiymat kiriting: "))
    dict2[key+1]=value
start=key
dict3=dict()
print()
for key in range(start+1,size*3):
    value=int(input("Kalit soniga int formatida qiymat kiriting: "))
    dict3[key+1]=value     
        
print()
print(dict1)
print(dict2)
print(dict3)
dict4={**dict1, **dict2, **dict3}
print(dict4)