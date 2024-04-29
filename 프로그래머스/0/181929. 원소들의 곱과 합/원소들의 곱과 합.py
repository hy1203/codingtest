def solution(num_list):
    result_sum = 0
    result_multi = 1
    for num in num_list:
        result_sum += num
        result_multi *= num
    if result_multi < result_sum**2:
        return 1
    else:
        return 0