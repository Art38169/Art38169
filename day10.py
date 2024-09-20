print("P'Ve so handsome lah.")
# *list (list extractor)
l = [1, 2.3, True, "Vetit", None]
print(*l) # To remove the brackets
# List can be added and multiply
# map
m = [0, 1, 0.0]
# print(list(map(int, input().split())))
# Tuple
# Same as list but 1. Immutable(Members cannot change)
# empty_tuple = () OR tuple()
# one_element_tuple = (2,)
"""num = int(input())
l = list(map(int, input().split()))
l.sort()
count = 0
for i in range(len(l)):
    if i == 0:
        count +=1
    elif l[i] != l[i-1]:
        count += 1
print(count)
"""
