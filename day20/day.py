import numpy as np

def part1(inputs):
    enhancer, input_image = inputs

    def enlarged_view():
        shapex, shapey = input_image.shape
        img = np.concatenate((np.zeros((20, shapey)), input_image), axis=0)
        img = np.concatenate((img, np.zeros((shapex + 20, 20))), axis=1)
        img = np.concatenate((img, np.zeros((20, shapey + 20))), axis=0)
        img = np.concatenate((np.zeros((shapey + 40, 20)), img), axis=1)
        return img

    def translate_image_at(i, j):
        num = 0
        for row in surrounding_block(i, j):
            for val in row:
                num <<= 1
                num += int(val)
        return num

    def surrounding_block(i, j):
        return input_image[i-1:i+2,j-1:j+2]

    print(f'input_image:\n{printable_image(input_image)}')
    input_image = enlarged_view()
    for _ in range(2):
        shapex, shapey = input_image.shape
        output_image = np.zeros((shapex, shapey))

        for i in range(1, shapex - 1):
            for j in range(1, shapey - 1):
                enhancer_key = translate_image_at(i, j)
                output_image[i,j] = enhancer[enhancer_key]

        input_image = output_image
        print(f'input_image:\n{printable_image(input_image)}')

    return int(output_image[2:-2,2:-2].sum())

def part2(inputs):
    enhancer, input_image = inputs

    def enlarged_view():
        big = 275
        shapex, shapey = input_image.shape
        img = np.concatenate((np.zeros((big, shapey)), input_image), axis=0)
        img = np.concatenate((img, np.zeros((shapex + big, big))), axis=1)
        img = np.concatenate((img, np.zeros((big, shapey + big))), axis=0)
        img = np.concatenate((np.zeros((shapey + big*2, big)), img), axis=1)
        return img

    def translate_image_at(i, j):
        num = 0
        for row in surrounding_block(i, j):
            for val in row:
                num <<= 1
                num += int(val)
        return num

    def surrounding_block(i, j):
        return input_image[i-1:i+2,j-1:j+2]

    print(f'input_image:\n{printable_image(input_image)}')
    input_image = enlarged_view()
    for i in range(50):
        print('i: ', i)
        shapex, shapey = input_image.shape
        output_image = np.zeros((shapex, shapey))

        for i in range(1, shapex - 1):
            for j in range(1, shapey - 1):
                enhancer_key = translate_image_at(i, j)
                output_image[i,j] = enhancer[enhancer_key]

        input_image = output_image
        print(f'input_image:\n{printable_image(input_image)}')

    return int(output_image[50:-50,50:-50].sum())

def printable_image(image):
    return '\n'.join([''.join(['#' if i else '.' for i in row]) for row in image])

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    enhancer, enh_done = [], False
    input_image = []
    for line in raw.split('\n'):
        if not line:
            enh_done = True
        elif enh_done:
            input_image.append([(0 if i == '.' else 1) for i in line])
        else:
            enhancer.extend([(0 if i == '.' else 1) for i in line])
    return np.array(enhancer), np.array(input_image)

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
