# 배열 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120821
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 04. 20:50:46

def solution(num_list):
    new_list = []
    for n in num_list:
        new_list.insert(0,n)
    answer = new_list
    return answer