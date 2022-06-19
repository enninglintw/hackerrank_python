if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_scores = list(set(arr))
    runner_up_score = sorted(unique_scores)[-2]
    print(runner_up_score)
