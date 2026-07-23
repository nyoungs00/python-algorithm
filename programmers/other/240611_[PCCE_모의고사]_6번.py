# [PCCE 모의고사] 6번
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/240611
# 작성자: 조현영
# 작성일: 2026. 07. 23. 16:32:47

def solution(matrix_A, matrix_B):
    answer = []
    for i in range(len(matrix_A)):
        row = []
        for j in range(len(matrix_A[i])):
            row.append(matrix_A[i][j]+matrix_B[i][j])
        answer.append(row)            
    return answer