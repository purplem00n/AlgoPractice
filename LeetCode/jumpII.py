def jump(nums) -> int:

    i = 0
    n = len(nums)
    # the number of jumps we make to get to the end
    num_jumps = 0

    if n <= 2:
        return n - 1

    while i < (n - 1):
        # the size of the jump, to keep track of max jump possible
        max_jump = 0
        # to keep track of the length of the jump (the amount of indexes moved)
        jump_size = 0
        # iterate through the possible destinations (value at nums[i])
        j = nums[i]
        # if the greatest possible jump is larger than the length of the array,
        # we will take the jump to the end (add 1) and return num jumps
        if i + j >= (n - 1):
            return num_jumps + 1

        for k in range(1, j + 1):
            # keep track of the largest jump - the furthest we can get from where we're at:
                # the amount of indexes forward plus the value at that index: k + nums[i+k]
            # if the value at each possible iteration is greater than max_jump, 
            # set max jump to that value and keep track of the amount of indexes moved

            # max_jump = max(max_jump, k + nums[i+k]) doesn't work
            # jump_size = nums[::1].index(max_jump) doesn't work
            if k + nums[i+k] >= max_jump:
                max_jump = k + nums[i+k]
                jump_size = k
        # increment i by the amount of indexes moved to get to the largest jump value.
        i += jump_size   
        # we know we'll jump one time per iteration of the while loop
        num_jumps += 1
        # if we are sitting exactly at the last element, exit
        if i == (n - 1):
            break

    return num_jumps

print(jump([2,3,1,1,4]))
