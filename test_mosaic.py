import Indexer
import Stitcher
import basic_mosaic
import intermediate_mosaic
import advanced_mosaic

def open_mosaic(image_set_directory, target_image, output_image):
    Indexer.run_index(image_set_directory)
    Stitcher.run_stitcher(target_image, 20, 'rgb', output_image)

def test_basic_mosaic(image_set_directory, target_image, output_image, width, height):
    basic_mosaic.run_mosaic(image_set_directory, target_image, output_image, width, height)

def test_intermediate_mosaic(image_set_directory, target_image, output_image, width, height):
    intermediate_mosaic.run_mosaic(image_set_directory, target_image, output_image, width, height)

def test_advanced_mosaic(image_set_directory, target_image, output_image, width, height):
    advanced_mosaic.run_mosaic(image_set_directory, target_image, output_image, width, height)


def jeff_2_mosaic():
    pass

if __name__ == "__main__":
    # image_set_directory = 'Source\\my_image_library\\'
    # target_image = 'target3.jpg'
    #
    # test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target3_10.jpg', 10, 10)

    image_set_directory = 'Source\\TestSet2\\'
    target_image = 'target2.jpg'

    test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target2_50.jpg', 50, 50)

    # test_advanced_mosaic(image_set_directory, target_image, 'advanced_mosaic_target_3.jpg', 3, 3)
    # test_advanced_mosaic(image_set_directory, target_image, 'advanced_mosaic_target_5.jpg', 5,5)
    # test_advanced_mosaic(image_set_directory, target_image, 'advanced_mosaic_target_20.jpg', 20,20)
    # test_advanced_mosaic(image_set_directory, target_image, 'advanced_mosaic_target_30.jpg', 30,30)
    # test_advanced_mosaic(image_set_directory, target_image, 'advanced_mosaic_target_40.jpg', 40,40)
    # test_advanced_mosaic(image_set_directory, target_image, 'advanced_mosaic_target_50.jpg', 50,50)

    # test_intermediate_mosaic(image_set_directory, target_image, 'intermediate_mosaic_target_50.jpg', 50, 50)
    # test_intermediate_mosaic(image_set_directory, target_image, 'intermediate_mosaic_target_10.jpg', 10, 10)
    # test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target_10.jpg', 10, 10)
    #
    # test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target_20.jpg', 20, 20)
    # test_intermediate_mosaic(image_set_directory, target_image, 'intermediate_mosaic_target_20.jpg', 20, 20)
    #
    # test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target_30.jpg', 30, 30)
    # test_intermediate_mosaic(image_set_directory, target_image, 'intermediate_mosaic_target_30.jpg',30, 30)
    #
    # test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target_40.jpg', 40, 40)
    # test_intermediate_mosaic(image_set_directory, target_image, 'intermediate_mosaic_target_40.jpg', 40, 40)
    #
    # test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target_50.jpg', 50, 50)
    # test_intermediate_mosaic(image_set_directory, target_image, 'intermediate_mosaic_target_50.jpg', 50, 50)
    #
    # test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target_5.jpg', 5, 5)
    # test_intermediate_mosaic(image_set_directory, target_image, 'intermediate_mosaic_target_5.jpg', 5,5)
    #
    # test_basic_mosaic(image_set_directory, target_image, 'basic_mosaic_target_3.jpg', 3, 3)
    # test_intermediate_mosaic(image_set_directory, target_image, 'intermediate_mosaic_target_3.jpg', 3, 3)

    #open_mosaic(image_set_directory, target_image, 'openMosaicOutput.jpg')
