# [PCCE 모의고사] 4번
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/240609
# 작성자: 조현영
# 작성일: 2026. 07. 23. 14:24:51

start = int(input())
step = int(input())
end = int(input())

for i in range(start, end-1, -step):
    print(i)