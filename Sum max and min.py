arr = list(map(int, input().rstrip().split()))  # Getting input from the user as a list 
x = sorted(arr)                                 # Sorting the array in ascending order
maxi = max(x)                                   # Finding maximum and minimum element in array
mini = min(x)                                      
sum = maxi + mini                               # Sum of maximum amd minimum element
print(sum) 
