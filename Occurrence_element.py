#occurrence of element in List/Array
a=[1,2,2,3,4,3,4,6,7,9,11,12,12,13,15,'a','a','a','a','a','a','a']

def dict_creation(a):
    c=remove_duplicates(a)
    print(c)
    occ={}
    for i in range(len(c)):
        n=a.count(c[i])
        occ[c[i]]=n
    print(occ)
def remove_duplicates(a):
    new_array=[]
    for i in a:
        if i not in new_array:
            new_array.append(i)
    return new_array
dict_creation(a)
