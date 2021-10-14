my_list = [1,3,5,6,45,6,7,7,88,9,0]

def  binary_search(list,item):
  low=0 #pastki chegara
  high = len(list)-1  # tepa chegara

  while low <=high:
    mid = (low+high)//2
    g = list[mid]

    if g == item:
      return mid
    if g > item:
      return mid -1
    else:
      low=mid+1  
  return None

print(binary_search(my_list,88))


