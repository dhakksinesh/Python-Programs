def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
random_list_of_nums = [4, 15, 9, 10, 26]
selection_sort(random_list_of_nums)
print(random_list_of_nums)