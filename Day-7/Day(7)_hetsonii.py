it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of \"it_companies\" set: {}".format(len(it_companies)))
print("A union B: {}".format(A.union(B)))
print("A intersection B: {}".format(A.intersection(B)))

if(len(set(age))>len(age)):
    print("Set is bigger than the List")
elif(len(set(age))<len(age)):
    print("List is bigger than the Set")
else:
    print("List and Set both have equal size.")