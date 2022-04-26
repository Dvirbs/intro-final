#################################################################
# FILE : cartoonify.py
# WRITER : Dvir , Dvirbs , 204270243
# EXERCISE : intro2cs2 ex5 2020
# DESCRIPTION: image processing
# STUDENTS I DISCUSSED THE EXERCISE WITH: Ben Moyel
# WEB PAGES I USED:
# NOTES:
#################################################################


import copy
from typing import List
import math
import sys
import ex5_helper


def separate_channels_pattern(image: List):
    """
    creating separate channels pattern
    :param image: List of raws x columns x channels
    :return: pattern of channels x raws x columns with values of -1
    """
    row_num: int = len(image)
    column_num: int = len(image[0])
    channels_num: int = len(image[0][0])
    columns: List = [-1 for k in range(column_num)]
    rows: List = [copy.deepcopy(columns) for j in range(row_num)]
    separate_channel_pattern: List = [copy.deepcopy(rows) for i in range(channels_num)]
    return separate_channel_pattern


def separate_channels(image: List):
    """
    Function which receives an image of a three-dimensional list such as rows X columns X colors_num
    and returns a three-dimensional list changed  ->>>  colors_num X rows X columns
    :param image: list of the image data  ->>>  colors_num X rows X columns
    :return: three-dimensional list
    """
    separate_channels_image = separate_channels_pattern(image)
    for row_i, row in enumerate(image):
        for column_i, column in enumerate(row):
            for channel_i, channel in enumerate(column):
                separate_channels_image[channel_i][row_i][column_i] = channel
    return separate_channels_image


def combine_channels_pattern(channels: List):
    """
    creating combine channels pattern
    :param channels: List of channels x raws x columns with values
    :return: pattern  List of raws x columns x channels with vlaues of -1
    """
    channels_num = len(channels)
    rows_num = len(channels[0])
    columns_num = len(channels[0][0])
    column: List = [-1 for k in range(channels_num)]
    row: List = [copy.deepcopy(column) for j in range(columns_num)]
    image: List = [copy.deepcopy(row) for i in range(rows_num)]
    return image


def combine_channels(channels: List):
    """
    getting image of saperate channels and conbine it togther
    :param channels: ist of channel lengths of 2D images Which consists of individual color channels
    :return: single color image whose dimensions are rows X columns X channels
    """
    image = combine_channels_pattern(channels)
    for channel_i, channel in enumerate(channels):
        for row_i, row in enumerate(channel):
            for columns_i, column in enumerate(row):
                image[row_i][columns_i][channel_i] = column
    return image


def RGB2grayscale_pattern(colored_image: List):
    """
    function the create pattern of 2D image
    :param colored_image: RGB image
    :return: gray scale image
    """
    grayscale_pattern = list()
    for i in range(len(colored_image)):
        grayscale_pattern.append(list())
        for j in range(len(colored_image[0])):
            grayscale_pattern[i].append(-1)
    return grayscale_pattern


def RGB_averaging(red, green, blue):
    return round(red * 0.299 + green * 0.587 + blue * 0.114)


def RGB2grayscale(colored_image):
    """
    The function converting color image to image in black and white
    :param colored_image: color image
    :return: image in black and white
    """
    grayscale_image = RGB2grayscale_pattern(colored_image)
    for row_i, row in enumerate(colored_image):
        for column_i, column in enumerate(row):
            gray_value = RGB_averaging(column[0], column[1], column[2])
            grayscale_image[row_i][column_i] = gray_value
    return grayscale_image


def blur_kernel(size: int):
    """
    creating blur kernel
    :param size: determine the value of the kernel
    :return: Returns a size X size smoothing kernel as a list of lists.
    """
    row = [1 / (size ** 2) for column in range(size)]
    kernel = [copy.deepcopy(row) for row_i in range(size)]
    return kernel


def coordinates_system_transformation(prev_pix_cord, new_cor_pix_x, new_cor_pix_y, prev_cord_point_x,
                                      prev_cord_point_y) -> List:
    x_transfer_value = new_cor_pix_x - prev_pix_cord  # 4-2=2
    y_transfer_value = new_cor_pix_y - prev_pix_cord  # 3-2=1
    new_point_x = prev_cord_point_x + x_transfer_value  # 2+2 =4
    new_point_y = prev_cord_point_y + y_transfer_value  # 1+1 = 2
    return [new_point_x, new_point_y]


def pixel_matrix_pattern(kernel_len: int, pixel_value: int):
    """
    creating pattern of matrix with len k
    :param pixel_value: the pixel value
    :param kernel_len: An odd natural number!!!
    :return: matrix k x k
    """
    matrix_pattern = list()
    for i in range(kernel_len):
        matrix_pattern.append(list())
        for j in range(kernel_len):
            matrix_pattern[i].append(pixel_value)
    return matrix_pattern


def pixel_matrix(image: List, kernel_len: int, p_row: int, p_col: int):
    """
    creating pixel matrix with k rows and k columns by Identify the pixel image [row] [column] and sum the values of its
    neighbors arguments.
    :param image: A picture with a single color channel (two-dimensional list)
    :param kernel_len: An odd natural number!!!
    :param p_row: pixel_raw
    :param p_col: pixel_column
    :return: matrix k x k with all the values next to the pixel matrix
    """
    kernel_x_cordinates = kernel_len // 2
    pixel_value = image[p_row][p_col]
    pixel_matrix = pixel_matrix_pattern(kernel_len, pixel_value)
    for row_i in range(kernel_len):
        for column_j in range(kernel_len):
            x_point_image_cor, y_point_image_cor = coordinates_system_transformation(kernel_x_cordinates, p_col, p_row,
                                                                                     column_j, row_i)
            if x_point_image_cor < 0 or y_point_image_cor < 0:
                pixel_matrix[row_i][column_j] = pixel_value
            elif len(image) <= y_point_image_cor or len(image[0]) <= x_point_image_cor:
                pixel_matrix[row_i][column_j] = pixel_value
            else:
                # print('y_point_image_cor is ', y_point_image_cor)
                # print('x_point_image_cor', x_point_image_cor)
                # print('image[y_point_image_cor][x_point_image_cor]', image[y_point_image_cor][x_point_image_cor] )
                pixel_matrix[row_i][column_j] = image[y_point_image_cor][x_point_image_cor]

    return pixel_matrix


def multi_kernel(image, kernel, row_i, column_j):
    """
    multuplay the pixel matrix of the image with the kernel
    :param image: image
    :param kernel: kernel
    :param row_i: row of the pixel
    :param column_j: column of the pixel
    :return: matrix k * k of the multiplication
    """
    results = []
    #    print(kernel)
    #     print('kernel len is', len(kernel))
    #     print('row_i is - ', row_i)
    #     print('colunm_j is - ', column_j)
    pix_matrix = pixel_matrix(image, len(kernel), row_i, column_j)
    #    print(pix_matrix)
    for row_pair in zip(pix_matrix, kernel):
        for column_pair in zip(row_pair[0], row_pair[1]):
            #            print(column_pair[1], column_pair[0])
            results.append(column_pair[0] * column_pair[1])

    new_value = sum(results)
    if new_value > 255:
        new_value = 255
    if new_value < 0:
        new_value = 0
    return round(new_value)


def apply_kernel(image, kernel):
    """
    Blur an image using the kernel
    :param image: A picture with a single color channel (two-dimensional list)
    :param kernel: (two-dimensional list)
    :return: An image the same size as the original image, when the new_image [row] [column] pixel is calculated using
            The kernel on it
    """
    new_image = copy.deepcopy(image)
    for row_i, row in enumerate(image):
        for column_j, column in enumerate(row):
            new_image[row_i][column_j] = multi_kernel(image, kernel, row_i, column_j)
    return new_image


def getting_a_b_c_d(image, y, x):
    """
    function that calculate a,b,c,d argument with rounding up or down there "place" to the place of the value of the
     image
    :return: the value of a,b,c,d
    """
    if x > 459:
        x = 459
    if y > 249:
        y = 249
    a = image[math.floor(y)][math.floor(x)]
    b = image[math.ceil(y)][math.floor(x)]
    c = image[math.floor(y)][math.ceil(x)]
    d = image[math.ceil(y)][math.ceil(x)]
    return a, b, c, d


def bilinear_interpolation(image, y, x):
    """
    Receives a single-color channel image and pixel coordinates target image as they "fall" in the source image
    and returns the value Same pixel
    :param image: source image
    :param y: length of the image(rows)
    :param x: width of the image(columns)
    :return: the value of the pixel in the target image
    """
    a, b, c, d = getting_a_b_c_d(image, y, x)
    formula_x = x - int(x)
    formula_y = y - int(y)
    new_value = a * (1 - formula_x) * (1 - formula_y) + b * formula_y * (1 - formula_x) + c * \
                formula_x * (1 - formula_y) + d * formula_x * formula_y
    if new_value <= 0:
        return 0
    if new_value >= 255:
        return 255
    return round(new_value)


def new_matrix(new_height, new_width):
    """
    creating a new matrix with the new height and width
    :return: matrix with size new_height x new_width
    """
    matrix = list()
    for i in range(new_height):
        matrix.append(list())
        for j in range(new_width):
            matrix[i].append(-1)
    return matrix


def proportional_values(image, new_height, new_width):
    """
    creating matrix with values of the proportional ratio for the nearest neighbour
    :param image: The source image
    :return: return new image in the size to new_height X new_width with the ratio values
    """
    height_ratio = (len(image) - 1) / (new_height - 1)
    width_ratio = (len(image[0]) - 1) / (new_width - 1)
    new_image = new_matrix(new_height, new_width)
    for row_i, row in enumerate(new_image):
        for column_j, column in enumerate(new_image[row_i]):
            # print('row_i is ', row_i)
            # print('column_j is ', column_j)
            # print('target_image[row_i][column_j][0] is', new_image[row_i][column_j])
            y = row_i * height_ratio  # length of the image(rows)
            x = column_j * width_ratio  # width of the image(columns
            new_image[row_i][column_j] = (y, x)
    return new_image


def resize(image, new_height, new_width):
    """
    Receives an image and returns a new image in size to so that the value of each pixel in the returned image is
    calculated according to its relative position in the original image.
    :param image: image with single color channel
    :return: new image in the size to new_height X new_width
    """

    target_image = proportional_values(image, new_height, new_width)
    for row_i, row in enumerate(target_image):
        for column_j, column in enumerate(row):
            y = target_image[row_i][column_j][0]
            x = target_image[row_i][column_j][1]
            target_image[row_i][column_j] = bilinear_interpolation(image, y, x)
    return target_image


def rotate_matrix_pattern(image):
    """
    creating a rotate matrix pattern
    :param image: the image
    :return: matrix rotate with -1 values
    """
    rows_len = len(image)
    columns_len = len(image[0])
    rotated_matrix = [[-1 for column_i in range(rows_len)] for row_i in range(columns_len)]
    return rotated_matrix


def rotate_90(image, direction):
    """
    rotating image by 90 degrees
    :param image: image
    :param direction: a string that is 'R' or 'L'
    :return: a similar image, rotated 90 degrees in the desired direction.
    """
    target_matrix = rotate_matrix_pattern(image)
    for row_i, row in enumerate(image):
        for column_j, column in enumerate(row):
            if direction == 'R':
                target_matrix[column_j][(len(image) - 1) - row_i] = column
            elif direction == 'L':
                target_matrix[(len(image) - 1) - column_j][row_i] = column
    return target_matrix


def get_edges(image: List, blur_size: int, block_size: int, c: int):
    """
    function that gets the edages of the obiects in the image where black pixels mark borders in the image
    :param image:image with a single color channel (two-dimensional list)
    :param blur_size:
    :param block_size:
    :param c:
    :return: new image, with the same dimensions, Consisting of only two values (black and white)
    """
    blu_kernel = blur_kernel(blur_size)
    blur_mat = apply_kernel(image, blu_kernel)
    block_kernel = blur_kernel(block_size)
    average_mat = apply_kernel(blur_mat, block_kernel)
    for row_i, row in enumerate(average_mat):
        for column_j, column in enumerate(row):
            if blur_mat[row_i][column_j] <= column - c:
                average_mat[row_i][column_j] = 0
            else:
                average_mat[row_i][column_j] = 255
    return average_mat


def quantize(image: List, N: int):
    """
    Reduce a range of values in the image to a single value.
    Selects N shades at equal distances, without selecting optimal shades, and transfers each shade in
    the original image to the shade closest to it understands 𝑁
    :param image: Image as a two-dimensional list (with a single color channel)
    :param N: N Shades at equal distances
    :return: An image with identical dimensions, in which the values of
            the pixels are calculated.
    """
    quantize_image = copy.deepcopy(image)
    for row_i, row in enumerate(quantize_image):
        for column_j, pixel in enumerate(row):
            quantize_image[row_i][column_j] = round(math.floor(pixel * (N / 255)) * (255 / N))
    return quantize_image


def quantize_colored_image(image: List, N: int):
    """
    Reduce a range of values in 3D image to a single value.
    :param image: Image as a three-dimensional list (with a a lot of color channel)
    :param N: N Shades at equal distances
    :return: An image with identical dimensions, in which the values of
            the pixels are calculated.
    """
    sep_image = separate_channels(image)
    for channel_i, channel in enumerate(sep_image):
        sep_image[channel_i] = quantize(channel, N)
    com_image = combine_channels(sep_image)
    return com_image


def add_mask(image1: List, image2: List, mask: List):
    new_image = copy.deepcopy(mask)
    for row_i, row in enumerate(new_image):
        for column_j, pixel in enumerate(row):
            new_image[row_i][column_j] = round(image1[row_i][column_j] *
                                               mask[row_i][column_j] + image2[row_i][column_j] * (
                                                       1 - mask[row_i][column_j]))
    return new_image


def mask(image):
    new_image = []
    row_image = []
    for row_i, row in enumerate(image):
        for column_j, pixel in enumerate(row):
            new_pixel = pixel / 255
            row_image.append(new_pixel)
        new_image.append(row_image)
        row_image = []
    return new_image


def cartoonify(image, blur_size: int, th_block_size: int, th_c, quant_num_shades: int):
    image_c = copy.deepcopy(image)
    image_to_BW = RGB2grayscale(image_c)
    image_with_edge = get_edges(image_to_BW, blur_size, th_block_size, th_c)
    mask_image = mask(image_to_BW)
    after_quantize = quantize_colored_image(image_c, quant_num_shades)
    after_mask = []
    for color_channel in separate_channels(after_quantize):
        after_mask.append(add_mask(image_with_edge, color_channel , mask_image))
    final = combine_channels(after_mask)            #combine saperate image
    return final


def max_size(image, maxi_size):
    height = len(image)
    width = len(image[0])
    if height <= maxi_size and width <= maxi_size:
        return round(height), round(width)

    if height > maxi_size >= width:
        ratio = maxi_size / height
        height = maxi_size
        width = ratio * width
        return round(height), round(width)
    if width > maxi_size >= height:
        ratio = maxi_size / width
        width = maxi_size
        height = ratio * height
        return round(height), round(width)

    if width > maxi_size and height > maxi_size:
        maxi_value = max(width, height)
        ratio = maxi_size / maxi_value
        return round(height * ratio), round(width * ratio)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 8:
        sys.exit("number of arguments is not correct")
    image = ex5_helper.load_image(args[1])
    separte_image = separate_channels(image)
    height, width = max_size(image, int(args[3]))
    resize_image = []
    for channel in separte_image:
        resize_image.append(resize(channel, height, width))
    combine_image = combine_channels(resize_image)
    cartoonify_image = cartoonify(combine_image, int(args[4]), int(args[5]), float(args[6]), int(args[7]))
    ex5_helper.save_image(cartoonify_image, args[2])


im = ex5_helper.load_image("dvir.jpg")
im = RGB2grayscale(im)
im2 = resize(im, 500, 500)
ex5_helper.show_image(im2)
ex5_helper.show_image(im)
# some more documentation

im = ex5_helper.load_image("ziggy.jpg")
im = RGB2grayscale(im)
im2 = resize(im, 250, 460)
im3 = get_edges(im2, 5, 15, 17)
ex5_helper.show_image(im3)
ex5_helper.show_image(im)

# print(combine_channels([[[1, 2, 3],[1, 2, 3]], [[1, 4, 5],[1, 4, 5]], [[1, 6, 7],[1, 6, 7]]]))
#print(cartoonify([[[[50, 150, 250]]], 3, 3, 20, 8]))