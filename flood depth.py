'''
Problem - 4

https://app.codility.com/programmers/trainings/1/flood_depth/


'''
# Solution:
'''Idea:
1. There should be two taller blocks to make the rainwater stay
2. find each position's tallest block from left and right
3. Then find the 2nd tallest block among the left and right (which will be floor level of water) (min(left tallest, right tallest))
4. calculate each posiition's depth using min(left tallest, right tallest) - current positon's height

'''

def solution(A):
    if len(A) < 3:
        return 0

    N = len(A)
    
    left_max = [0] * N
    right_max = [0] * N

    left_max[0] = A[0]
    for i in range(1, N):
        left_max[i] = max(left_max[i - 1], A[i])

    right_max[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], A[i])

    max_depth = 0
    for i in range(N):
        # Water depth at position i (is calculaed by the minimum of left_max and right_max minus the current height)
        depth = min(left_max[i], right_max[i]) - A[i]
        if depth > max_depth:
            max_depth = depth

    return max_depth

        
print(solution([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))
print(solution([1, 3]))
print(solution([1, 3, 8, 12, 1, 5, 11, 0, 16, 1]))