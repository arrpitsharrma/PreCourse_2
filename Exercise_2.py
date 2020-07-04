# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  pIndex = low
  pivot = arr[high]

  for i in range(low, high):
    if arr[i] < pivot:
      temp = arr[pIndex]
      arr[pIndex] = arr[i]
      arr[i] = temp
      pIndex += 1
  temp = arr[high]
  arr[high] = arr[pIndex]
  arr[pIndex] = temp
  return pIndex

# Function to do Quick sort 
def quickSort(arr,low,high):
  if low < high:
    pIndex = partition(arr, low, high)
    quickSort(arr, low, pIndex-1)
    quickSort(arr, pIndex+1, high)
  
# Driver code to test above 
arr = [37,4,1,10,14,68,42] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  

 
