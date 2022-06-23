def build_set():
    return set(map(int, input().split(' ')))

def is_a_strict_superset(superset, subset):
    return (superset | subset == superset) and (len(superset - subset) > 0)

set_a = build_set()
other_sets_count = int(input())
booleans = [is_a_strict_superset(set_a, build_set()) for i in range(other_sets_count)]

print(all(booleans))
