import collections


def solution(nums):
    answer = 0

    N = len(nums) / 2

    if len(collections.Counter(nums)) > N:
        answer += N
    else:
        answer += len(collections.Counter(nums))

    return answer