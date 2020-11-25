array = [1,12,13,14,2,4,5,9,7]

def even_num(array):
    even = []
    for x in array:
        if x % 2 == 0:
            even.append(x)
    return even
    
print(even_num(array))