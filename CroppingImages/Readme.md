# Image Cropping and Analysis Tool

This Python script provides functionality for random square cropping of images and analyzing pixel value distributions. It's designed to process multiple images in a folder, create random crops, and visualize pixel intensity distributions.

## Features

1. Random square cropping of images
2. Automatic cropping of corresponding mask images (if available)
3. Visualization of crop locations on the original image
4. Pixel value distribution analysis for grayscale and RGB channels

## Requirements

- Python 3.x
- PIL (Python Imaging Library)
- NumPy
- Matplotlib

You can install the required libraries using pip:


## Usage

1. Place your input images in a folder named 'raw_image'.
2. If you have corresponding mask images, place them in a folder named 'masked_image' with the naming convention 'mask{number}.png'.
3. Run the script:


4. The script will process each image in the 'raw_image' folder, creating random crops and analyzing pixel distributions.

## Output

- Cropped images are saved in the 'cropped_raw_image' folder.
- Corresponding cropped mask images (if available) are saved in the 'cropped_mask_image' folder.
- The script generates visualizations for each crop, showing the crop location on the original image.
- Pixel value distribution plots are generated for each processed image.

## Customization

- You can adjust the number of crops per image by modifying the `num_crops` variable in the main section of the script.
- The crop size is currently set to 50% of the minimum dimension of each image. You can modify this in the `random_square_crop` function.

## Functions

1. `plot_pixel_distributions(image_path)`: Generates and displays histograms of pixel value distributions for grayscale and RGB channels.
2. `random_square_crop(image_path, crop_size, num_crops, global_counter)`: Performs random square cropping on the input image and its corresponding mask (if available).

## Note

Ensure that you have write permissions in the directory where the script is located, as it will create new folders for the cropped images.
