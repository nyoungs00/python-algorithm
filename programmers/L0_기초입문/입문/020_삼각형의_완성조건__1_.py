# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 06. 20:52:06

def solution(sides):
    tri = sorted(sides,reverse=True)
    if tri[0]<tri[1]+tri[2]:
        answer = 1
    else:
        answer = 2
    return answer