# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 04. 20:44:23

def solution(n, k):
    answer = 12000*n + 2000*(k-n//10)
    return answer