nums = []
for x in range(int(input())):
    nums.append(int(input()))

best_list = []
for x in range(len(nums)):
    thing = nums[0]
    nums.remove(nums[0])
    nums.insert(len(nums), thing)
    curr=0
    for v in range(len(nums)):
        curr += v*nums[v]
    best_list.append(curr)
    
print(min(best_list))