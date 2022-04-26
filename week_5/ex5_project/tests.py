import cartoonify


def test_separate_channels_pattern():
    assert cartoonify.separate_channels_pattern([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) == [
        [[-1, -1], [-1, -1]], [[-1, -1], [-1, -1]], [[-1, -1], [-1, -1]]]
    assert cartoonify.separate_channels_pattern([[[1, 2]]]) == [[[-1]], [[-1]]]
    assert cartoonify.separate_channels_pattern([[[1, 2, 3], [2, 3, 4]]]) == [[[-1, -1]], [[-1, -1]], [[-1, -1]]]


def test_separate_channels():
    assert cartoonify.separate_channels([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) == [[[1, 4], [7, 10]],
                                                                                                 [[2, 5], [8, 11]],
                                                                                                 [[3, 6], [9, 12]]]
    assert cartoonify.separate_channels([[[1, 2, 3, 4], [4, 5, 6, 7]], [[7, 8, 9, 10], [10, 11, 12, 13]]]) == [
        [[1, 4], [7, 10]], [[2, 5], [8, 11]], [[3, 6], [9, 12]],
        [[4, 7], [10, 13]]]
    assert cartoonify.separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
    assert cartoonify.separate_channels([[[1, 2, 3], [2, 3, 4]]]) == [[[1, 2]], [[2, 3]], [[3, 4]]]
    assert cartoonify.separate_channels([[[1, 2, 3, 4], [2, 3, 4, 5]]]) == [[[1, 2]], [[2, 3]], [[3, 4]], [[4, 5]]]


def test_combine_channels_pattern():
    assert cartoonify.combine_channels_pattern([[[1, 4], [7, 10]], [[2, 5], [8, 11]], [[3, 6], [9, 12]]]) == [
        [[-1, -1, -1], [-1, -1, -1]], [[-1, -1, -1], [-1, -1, -1]]]
    assert cartoonify.combine_channels_pattern([[[1, 2]], [[2, 3]], [[3, 4]]]) == [[[-1, -1, -1], [-1, -1, -1]]]
    assert cartoonify.combine_channels_pattern([[[1]], [[2]]]) == [[[-1, -1]]]


def test_combine_channels():
    assert cartoonify.combine_channels([[[1, 4], [7, 10]], [[2, 5], [8, 11]], [[3, 6], [9, 12]]]) == [
        [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    assert cartoonify.combine_channels([[[1, 2]], [[2, 3]], [[3, 4]], [[4, 5]]]) == [[[1, 2, 3, 4], [2, 3, 4, 5]]]
    assert cartoonify.combine_channels([[[1]], [[2]]]) == [[[1, 2]]]
    assert cartoonify.combine_channels([[[1]], [[2]], [[3]], [[4]]]) == [[[1, 2, 3, 4]]]


def test_RGB2grayscale_pattern():
    assert cartoonify.RGB2grayscale_pattern(
        [[[100, 180, 240], [100, 180, 240]], [[100, 180, 240], [100, 180, 240]]]) == [[-1, -1], [-1, -1]]
    assert cartoonify.RGB2grayscale_pattern([[[100, 180, 240]]]) == [[-1]]
    assert cartoonify.RGB2grayscale_pattern([[[100, 180, 240], [100, 180, 240]]]) == [[-1, -1]]


def test_RGB2grayscale(colored_image):
    assert colored_image == cartoonify.RGB2grayscale(colored_image)
    assert cartoonify.RGB2grayscale([[[100, 180, 240]]]) == [[163]]
    assert cartoonify.RGB2grayscale([[[100, 180, 240], [100, 180, 240]]]) == [[163, 163]]
    assert cartoonify.RGB2grayscale([[[100, 180, 240], [100, 180, 240]], [[100, 180, 240], [100, 180, 240]]]) == [
        [163, 163], [163, 163]]
    assert cartoonify.RGB2grayscale(
        [[[100, 180, 240], [100, 180, 240]], [100, 180, 240], [[100, 180, 240], [100, 180, 240], [100, 180, 240]]]) == [
               [163, 163, 163], [163, 163, 163]]


def test_blur_kernel():
    assert cartoonify.blur_kernel(3) == [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
    assert cartoonify.blur_kernel(1) == [[1]]
    assert cartoonify.blur_kernel(5) == [[1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
                                         [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
                                         [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
                                         [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
                                         [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25]]


def test_pixel_matrix():
    assert cartoonify.pixel_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 1, 1) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix5x5 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    assert cartoonify.pixel_matrix(matrix5x5, 3, 2, 2) == [[7, 8, 9], [12, 13, 14], [17, 18, 19]]
    assert cartoonify.pixel_matrix(matrix5x5, 3, 0, 2) == [[3, 3, 3], [2, 3, 4], [7, 8, 9]]
    # assert cartoonify.pixel_matrix(matrix5x5, 3, 4, 2) == [[17, 18, 19], [22, 23, 24], [23, 23, 23]]
    # assert cartoonify.pixel_matrix(matrix5x5, 3, 3, 0) == [[16, 11, 12], [16, 16, 17], [16, 21, 22]]
    # assert cartoonify.pixel_matrix(matrix5x5, 3, 3, 4) == [[14, 15, 20], [19, 20, 20], [24, 25, 20]]
    # assert cartoonify.pixel_matrix(matrix5x5, 3, 0, 0) == [[1, 1, 1], [1, 1, 12], [1, 6, 7]]
    # assert cartoonify.pixel_matrix(matrix5x5, 3, 4, 0) == [[21, 16, 17], [21, 21, 22], [21, 21, 21]]
    # assert cartoonify.pixel_matrix(matrix5x5, 3, 4, 4) == [[19, 20, 25], [24, 25, 25], [25, 25, 25]]
    assert cartoonify.pixel_matrix(matrix5x5, 7, 2, 2) == [[13, 13, 13, 13, 13, 13, 13], [13, 1, 2, 3, 4, 5, 13],
                                                           [13, 6, 7, 8, 9, 10, 13], [13, 11, 12, 13, 14, 15, 13],
                                                           [13, 16, 17, 18, 19, 20, 13], [13, 21, 22, 23, 24, 25, 13],
                                                           [13, 13, 13, 13, 13, 13, 13]]


def test_apply_kernel():
    assert len(cartoonify.apply_kernel([[0, 128, 255]], cartoonify.blur_kernel(3))) == len([[0, 128, 255]])
    assert len(cartoonify.apply_kernel([[0, 128, 255]], cartoonify.blur_kernel(3))[0]) == len([[0, 128, 255]][0])


def test_multi_kernel():
    matrix5x5 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    assert cartoonify.multi_kernel(matrix5x5, cartoonify.blur_kernel(3), 2, 2) == 13
    assert cartoonify.multi_kernel(matrix5x5, cartoonify.blur_kernel(3), 1, 1) == 7


def test_bilinear_interpolation():
    assert cartoonify.bilinear_interpolation([[0, 64], [128, 255]], 0, 0) == 0
    assert cartoonify.bilinear_interpolation([[0, 64], [128, 255]], 1, 1) == 255
    assert cartoonify.bilinear_interpolation([[0, 64], [128, 255]], 0.5, 0.5) == 112
    assert cartoonify.bilinear_interpolation([[0, 64], [128, 255]], 0.5, 1) == 160
    assert cartoonify.bilinear_interpolation([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 0, 3) == 4


def test_proportional_values():
    assert cartoonify.proportional_values([[0, 64, 128], [0, 128, 255], [100, 100, 100]], 2, 2) == [[(0, 0), (0, 2)],
                                                                                                    [(2, 0), (2, 2)]]


def test_resize():
    assert cartoonify.resize([[0, 64, 128], [0, 128, 255], [100, 100, 100]], 2, 2) == [[0, 128], [100, 100]]
    assert cartoonify.resize([[1, 2], [5, 6], [9, 10], [13, 14]], 4, 4) == [[1, 1, 2, 2], [5, 5, 6, 6], [9, 9, 10, 10],
                                                                            [13, 13, 14, 14]]
    image = [
        [236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236,
         236, 236, 236, 236, 236, 236],
        [236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236,
         236, 236, 236, 236, 236, 236],
        [236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236,
         236, 236, 236, 236, 236, 236],
        [236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236,
         236, 236, 236, 236, 236, 236],
        [236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236,
         236, 236, 236, 236, 236, 236],
        [236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236,
         236, 236, 236, 236, 236, 236],
        [236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236, 236,
         236, 236, 236, 236, 236, 236]]
    assert len(cartoonify.resize(image, 300, 400)) == 300
    assert len(cartoonify.resize(image, 300, 400)[0]) == 400


def test_rotate_matrix_pattern():
    assert cartoonify.rotate_matrix_pattern([[1, 2, 3], [4, 5, 6]]) == [[-1, -1], [-1, -1], [-1, -1]]


def taest_rotate_90(image, direction):
    assert cartoonify.rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[4, 1], [5, 2], [6, 3]]
    assert cartoonify.rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[3, 6], [2, 5], [1, 4]]


def test_quantize():
    assert len(cartoonify.quantize([[0, 50, 100], [150, 200, 250]], 8)) == len([[0, 50, 100], [150, 200, 250]])
    assert len(cartoonify.quantize([[0, 50, 100], [150, 200, 250]], 8)[0]) == len([[0, 50, 100], [150, 200, 250]][0])
    assert cartoonify.quantize([[0, 50, 100], [150, 200, 250]], 8) == [[0, 32, 96], [128, 191, 223]]


def test_coordinates_system_transformation():
    assert cartoonify.coordinates_system_transformation(2, 4, 3, 2, 0) == [4, 1]
    assert cartoonify.coordinates_system_transformation(2,2,0,2,0) == [2, -2]
    assert cartoonify.coordinates_system_transformation(1,1,1,0,0) == [0, 0]


def test_add_mask():
    assert cartoonify.add_mask([[50, 50, 50]], [[200, 200, 200]], [[0, 0.5, 1]]) == [[200, 125, 50]]

def main():
    test_separate_channels_pattern()
    test_combine_channels_pattern()
    test_separate_channels()
    test_combine_channels()
    test_RGB2grayscale_pattern()
#    test_apply_kernel()
#    test_multi_kernel()
    test_bilinear_interpolation()
    test_proportional_values()
    test_resize()
    test_rotate_matrix_pattern()
    # test_get_edges()
    test_quantize()
    test_coordinates_system_transformation()
    test_pixel_matrix()
    test_add_mask()


if __name__ == '__main__':
    main()
