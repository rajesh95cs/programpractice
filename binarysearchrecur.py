a = [3,5,7,8,9,15,17,29]

b = 9

def binsearch(low,high,b,a):
     mid = (low + high)/2
     mid = int(mid)
     if(a[mid] == b):
         print("element found at")
         return mid + 1
     elif(low >= high):
         print("element not found")
         return -1
     else:
         if(a[mid] < b):
             low = mid + 1
             return binsearch(low,high,b,a)
         else:
             high = mid - 1
             return binsearch(low,high,b,a)
low = 0
high = len(a) - 1
print(binsearch(low,high,b,a))
