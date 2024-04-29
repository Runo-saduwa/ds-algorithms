# Out of place solution
def removeDuplicatesOutOfPlace(nums):
  newList = sorted(set(nums));
  print(newList)


removeDuplicatesOutOfPlace([1,1,2])

# The function `removeDuplicates(nums)` you've provided removes duplicates from the list `nums` and then prints the sorted list without duplicates. Let's analyze its space and time complexity and determine whether it's in-place or out-of-place:

### Time Complexity

# 1. **Converting List to Set**:
#    - This operation removes duplicates and involves iterating over all elements in the list to add them to the set. The average time complexity for inserting an element into a set is \(O(1)\).
#    - Therefore, for \(n\) elements, this operation has an average time complexity of \(O(n)\).

# 2. **Sorting the Set**:
#    - After converting the list to a set, the `sorted()` function is used to sort the elements. The number of elements in the set is at most \(n\) (if all elements were unique), but could be less if there were duplicates.
#    - The best sorting algorithms have a time complexity of \(O(m \log m)\), where \(m\) is the number of elements in the set. In the worst case, \(m = n\).

# Combining these, the overall time complexity of the function is \(O(n + n \log n)\), which simplifies to \(O(n \log n)\).

# ### Space Complexity

# 1. **Set Storage**:
#    - The set will use space proportional to the number of unique elements it holds, which is at most \(n\).

# 2. **New List for Sorted Elements**:
#    - The `sorted()` function creates a new list containing the sorted elements from the set. The size of this list will be the same as the number of elements in the set, again at most \(n\).

# Thus, the space complexity is \(O(n)\), where \(n\) is the number of elements in the original list, due to the additional storage needed for the set and the sorted list.

# ### In-Place or Out-of-Place

# - **Out-of-Place**:
#   - The function does not modify the original list `nums` but instead creates a new set and a new sorted list. Therefore, the operations are performed out-of-place.

# In summary, the function `removeDuplicates(nums)` operates with a time complexity of \(O(n \log n)\) and a space complexity of \(O(n)\). It performs its operations out-of-place by utilizing additional data structures (set and list) to store the unique and sorted elements.

# the function removeDuplicatesOutOfPlace(nums) operates with a time complexity of 
# 𝑂(𝑛log𝑛) and a space complexity of 𝑂(𝑛). It performs its operations out-of-place by utilizing additional data structures (set and list) to store the unique and sorted elements





# In place algorithm

# def removeDuplicatesInPlace(nums):

#     l = 1

#     for r in range(1, len(nums)):
#        if nums[r] != nums[r - 1]:
#           nums[l] = nums[r]
#           l += 1

#     return l
   




def removeDuplicates2(nums):
    l = 1
    for r in range(1, len(nums)):
       
        if nums[r] != nums[r-1]:
           nums[l] = nums[r]
           l += 1;
 
   