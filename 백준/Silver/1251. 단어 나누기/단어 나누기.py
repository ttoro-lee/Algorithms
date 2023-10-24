from itertools import combinations

string = input()

ranges = list(range(len(string)-1))

strings = set()

for combi in combinations(ranges, 2):
    first, second = combi
    f = string[:first+1][::-1]
    s = string[first+1:second+1][::-1]
    t = string[second+1:][::-1]

    strings.add(f+s+t)


print(sorted(strings)[0])