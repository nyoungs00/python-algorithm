# 뒤집힌 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 05. 20:32:39

def solution(my_string):
    st = []
    for s in my_string:
        st.insert(0,s)
    answer = ''.join(st)
    return answer