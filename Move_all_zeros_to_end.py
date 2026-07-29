def moveZeros(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j +=1
    return arr
arr=[0,6,6,3,4,4,99,00,0]
print(moveZeros(arr))         

                            # Time Complexity: O(n) (only one pass through the array)
                            # Space Complexity: O(1) (no extra array is used)