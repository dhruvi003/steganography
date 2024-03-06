from PIL import Image

def generate_data(pixels, data):
    data_in_binary = []

    for value in data:
        binary_data = format(ord(value),'08b')
        data_in_binary.append(binary_data)

    length_of_data = len(data_in_binary)
    pixel_value = iter(pixels)

    for item in range(length_of_data):
        pixels = [val for val in pixel_value.__next__()[:3] + pixel_value.__next__()[:3] + pixel_value.__next__()[:3]]

        for b in range(8):
            if(data_in_binary[item][b] == '1') and (pixels[b] % 2 != 0):
                pixels[b] -= 1
            elif(data_in_binary[item][b] == '0') and (pixels[b] % 2 == 0):
                if pixels[b] == 0:
                    pixels[b] += 1
                pixels[b] -= 1

        if(length_of_data-1) == item:
            if pixels[-1] %2 == 0:
                if pixels[-1] == 0:
                    pixels[-1] += 1
                else:
                    pixels[-1] -= 1

        pixels = tuple(pixels)

        yield pixels[:3]
        yield pixels[3:6]
        yield pixels[6:9]

