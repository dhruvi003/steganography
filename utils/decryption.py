from PIL import Image

def main_decryption(img, start_var):

    image = Image.open(img, 'r')
    data = ''
    image_data = iter(image.getdata())
    decoding = True

    while decoding:
        pixels = [value for value in image_data.__next__()[:3] + image_data.__next__()[:3]+ image_data.__next__()[:3]]

        binary_string = ''

        for i in pixels[:8]:
            if i%2 == 0:
                binary_string += '0'
            else:
                binary_string += '1'

        data += chr(int(binary_string,2))

        if pixels[-1] % 2 != 0:
            start_var.set(data)





