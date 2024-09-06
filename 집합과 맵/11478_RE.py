def power_set(s):
    result = [[]]
    for elem in s:
        new_subsets = [subset + [elem] for subset in result]
        result.extend(new_subsets)
    return [set(subset) for subset in result]


def powerSet2(s):
    uniqueElements = list(set(s))
    result = [[]]
    for elem in uniqueElements:
        newSubsets = [subset + [elem] for subset in result]
        result.extend(newSubsets)
    return [set(subset) for subset in result]


def count_unique_substrings(s):
    substrings = set()
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])

    return len(substrings)


s = input().strip()
# print(count_unique_substrings(s))
print(sorted(powerSet2(s)))
