def day01(depths):
    inc = 0
    for i in range(1, len(depths)):
        if depths[i-1] < depths[i]:
            inc += 1
    return inc

if __name__ == '__main__':
    with open('input.txt') as f:
        depths = list(map(int, f.read().split()))
        print(day01(depths))
