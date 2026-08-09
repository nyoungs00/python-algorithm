# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 09. 12:18:11

def solution(n):
    for i in range (0,n):
        if n !=i*i:
            answer = 2
            continue
        else :
            answer = 1
            break
    return answer