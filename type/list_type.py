odd = [1, 3, 5, 7, 9]

print(odd)

arr = [1, 2, ['string']]
arr2 = list()

print(arr)
print(arr2)

# arr2[0] = 3; -> IndexError: list assignment index out of range

print(arr[-1][0])

print(odd[0:len(odd)])

print(arr[:2])

arr.append(3)

print(arr)

arr.extend([4, 5])

print(arr)

arr.reverse()

print(arr)

arr = [7, 6] + arr

print(arr, len(arr))

print(str(arr[0]) + str(arr[1]))

del(arr[1:])

print(arr)

indexOfSeven = arr.index(7)

print(indexOfSeven)

arr.insert(1, 6)

print(arr)

arr.remove(7)

print(arr)

print(arr.count(6))

test = [1, 2, 3]

copied1 = test
copied2 = test[:]

print(id(test) == id(copied1)) # True
print(id(test) == id(copied2)) # True
