import array

def create_image_ppm(image:array, width, height, filename = "image.ppm"):
    """ Creates a binary ppm file based on the given image 
    
    Parameters:
    image (array): Binary array of length 3 * width * height (e.g., array.array('B', [0,0,0] * width * height))
    width (int): Width of image
    height (int): Height of image
    filnemae (str): Name of produced ppm image
    """
    header = "P6 {} {} 255\n".format(width, height);

    print("Create image...")

    with open('image.ppm', 'wb') as f:
        f.write(bytearray(header, 'ascii'))
        image.tofile(f)


