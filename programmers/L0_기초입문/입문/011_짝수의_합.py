# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 04. 20:46:17

def solution(n):
    sum = 0
    for n in range(1,n+1):
        if n%2 == 0 :
            sum += n
    answer = sum
    return answer