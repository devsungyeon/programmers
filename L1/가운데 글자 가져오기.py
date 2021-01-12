a = input()
l = len(a)
print(a[l//2 - (1 if l%2 == 0 else 0):l//2+1])