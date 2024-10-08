from collections import Counter

ls = [input().strip() for _ in range(int(input()))]
ls_dict = Counter(ls)
sorted_dict = sorted(ls_dict.items(), key = lambda x : ((-1) * x[1], x[0])) #책 등장 횟수가 큰 순, 알파벳은 빠른 순
print(sorted_dict[0][0])


##강의 풀이
#map(dictionary) 이용
d = dict()
for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

#d.keys()
#d.valeus()
#d.items()

m = max(d.values())
candidate = []
for k, v in d.items():
    if v == m:
        candidate.append(k)
candidate.sort()
print(candidate[0])