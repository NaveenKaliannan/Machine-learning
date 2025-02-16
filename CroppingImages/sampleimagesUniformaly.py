from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import re


def plot_pixel_distributions(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert to RGB if not already
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Convert to numpy array
    img_array = np.array(img)
    
    # Create a figure with 4 subplots
    fig, axs = plt.subplots(2, 2, figsize=(15, 15))
    fig.suptitle(f'Pixel Value Distributions for {os.path.basename(image_path)}', fontsize=16)
    
    # Plot grayscale distribution
    grayscale = np.mean(img_array, axis=2).flatten()
    axs[0, 0].hist(grayscale, bins=256, range=(0, 256), density=True, color='gray', alpha=0.7)
    axs[0, 0].set_title('Grayscale Distribution')
    axs[0, 0].set_xlabel('Pixel Value')
    axs[0, 0].set_ylabel('Density')
    
    # Plot Red channel distribution
    axs[0, 1].hist(img_array[:,:,0].flatten(), bins=256, range=(0, 256), density=True, color='red', alpha=0.7)
    axs[0, 1].set_title('Red Channel Distribution')
    axs[0, 1].set_xlabel('Pixel Value')
    axs[0, 1].set_ylabel('Density')
    
    # Plot Green channel distribution
    axs[1, 0].hist(img_array[:,:,1].flatten(), bins=256, range=(0, 256), density=True, color='green', alpha=0.7)
    axs[1, 0].set_title('Green Channel Distribution')
    axs[1, 0].set_xlabel('Pixel Value')
    axs[1, 0].set_ylabel('Density')
    
    # Plot Blue channel distribution
    axs[1, 1].hist(img_array[:,:,2].flatten(), bins=256, range=(0, 256), density=True, color='blue', alpha=0.7)
    axs[1, 1].set_title('Blue Channel Distribution')
    axs[1, 1].set_xlabel('Pixel Value')
    axs[1, 1].set_ylabel('Density')
    
    plt.tight_layout()
    plt.show()



def random_square_crop(image_path, crop_size, num_crops, global_counter):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Convert the image to RGB mode if it's not already
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Get the image dimensions
            width, height = img.size
            
            # Print the original image size
            print(f"Original Image Size: {width}x{height} pixels")
            
            # Calculate suggested crop sizes based on percentages of the minimum dimension
            min_dim = min(width, height)
            print(f"Suggested Crop Sizes:")
            print(f"- 50% of minimum dimension: {int(min_dim * 0.5)}x{int(min_dim * 0.5)}")
            print(f"- 25% of minimum dimension: {int(min_dim * 0.25)}x{int(min_dim * 0.25)}")
            print(f"- 10% of minimum dimension: {int(min_dim * 0.1)}x{int(min_dim * 0.1)}")
            
            # Get the crop size from the user
            #crop_size = int(input(f"Enter the square crop size for {os.path.basename(image_path)} (e.g., one of the suggested sizes above): "))
            crop_size = int(min_dim * 0.5)
            
            # Ensure the crop size is smaller than the image size
            if crop_size > width or crop_size > height:
                print("Crop size cannot be larger than the image size.")
                return global_counter
            
            # Generate random crops
            for i in range(num_crops):
                # Calculate the maximum random positions to avoid corners
                max_x = width - crop_size
                max_y = height - crop_size
                
                # Adjust the range to avoid corners
                safe_range_x = (crop_size // 2, width - crop_size // 2 - 1)
                safe_range_y = (crop_size // 2, height - crop_size // 2 - 1)
                
                # Generate random positions within the safe range
                random_x = random.randint(safe_range_x[0], safe_range_x[1])
                random_y = random.randint(safe_range_y[0], safe_range_y[1])
                
                # Print the random number range for random_x and random_y
                print(f"\nCrop {i+1} Details for {os.path.basename(image_path)}:")
                print(f"Random Number Range for random_x: [{safe_range_x[0]}, {safe_range_x[1]}]")
                print(f"Random Number Range for random_y: [{safe_range_y[0]}, {safe_range_y[1]}]")
                
                # Crop the image at the random location
                patch_area = (random_x - crop_size // 2, random_y - crop_size // 2, random_x + crop_size // 2, random_y + crop_size // 2)
                patch = img.crop(patch_area)
                
                # Save the patch with a sequential name
                patch.save(f'cropped_raw_image/crop{global_counter}.png')
                
                print(f"Crop {i+1} saved successfully for {os.path.basename(image_path)} as crop{global_counter}.png.")


                # Extract the number from the original image filename
                filename = os.path.basename(image_path)
                numbers = re.findall('\d+', filename)
                if numbers:
                    number = int(numbers[0])
                    mask_image_path = f'masked_image/mask{number}.png'
                    print(mask_image_path)
                    if os.path.exists(mask_image_path):
                        with Image.open(mask_image_path) as maskimg:
                            if maskimg.mode != 'RGB':
                                maskimg = maskimg.convert('RGB')
                            mask_patch = maskimg.crop(patch_area)
                            mask_patch.save(f'cropped_mask_image/crop{global_counter}.png')
                            print(f"Cropped mask saved successfully as cropped_mask_image/crop{global_counter}.png.")
                    else:
                        print(f"Mask image {mask_image_path} does not exist.")
                else:
                    print("No number found in the filename.")
                
                # Visualize the crop
                plt.figure(figsize=(10, 10))
                plt.imshow(img)
                plt.gca().add_patch(plt.Rectangle((patch_area[0], patch_area[1]), crop_size, crop_size, fill=False, edgecolor='red', linewidth=2))
                plt.axvline(x=safe_range_x[0], color='green', linestyle='--', label='Safe Range Start')
                plt.axvline(x=safe_range_x[1], color='green', linestyle='--', label='Safe Range End')
                plt.axhline(y=safe_range_y[0], color='green', linestyle='--')
                plt.axhline(y=safe_range_y[1], color='green', linestyle='--')
                plt.scatter(random_x, random_y, color='blue', s=100, label='Crop Center')
                plt.legend()
                plt.title(f"Crop {i+1} Visualization for {os.path.basename(image_path)}")
                plt.show()
                
                global_counter += 1
            
            return global_counter
    except FileNotFoundError:
        print("The file does not exist.")
        return global_counter
    except Exception as e:
        print(f"An error occurred: {e}")
        return global_counter

# Example usage
if __name__ == "__main__":
    #folder_path = input("Enter the folder path containing images: ")
    folder_path = 'raw_image'
    num_crops = 2
    global_counter = 1
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            global_counter = random_square_crop(image_path, None, num_crops, global_counter)

            # Add this line to plot the distributions for each image
            plot_pixel_distributions(image_path)

