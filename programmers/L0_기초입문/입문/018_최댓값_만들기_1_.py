# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 06. 20:42:57

def solution(numbers):
    s_numbers = sorted(numbers,reverse=True)
    answer = int(s_numbers[0])*int(s_numbers[1])
    return answer