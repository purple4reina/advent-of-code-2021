def day01_1(depths):
    inc = 0
    for i in range(1, len(depths)):
        if depths[i-1] < depths[i]:
            inc += 1
    return inc

def day01_2(depths):
    inc = 0
    for i in range(0, len(depths)-3):
        if sum(depths[i:i+3]) < sum(depths[i+1:i+4]):
            inc += 1
    return inc

if __name__ == '__main__':
    with open('input.txt') as f:
        depths = list(map(int, f.read().split()))
        print(day01_2(depths))
