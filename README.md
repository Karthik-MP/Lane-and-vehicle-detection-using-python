# Lane Detection using OpenCV

This project demonstrates lane detection using **OpenCV** and **Matplotlib**. The primary goal is to process an image and extract the region of interest (ROI), which helps in isolating the lanes from the rest of the road. The code uses OpenCV to load and process the image and Matplotlib to display the results.

## Overview

The algorithm focuses on identifying the region of interest (ROI) within an image of a road and applies a mask to isolate this region. This is commonly used in self-driving car applications, where lane detection is a critical component of road navigation.

### Key Steps:
1. **Loading Image**: The image is loaded using OpenCV's `imread` function.
2. **Color Conversion**: Since OpenCV loads images in BGR format, we convert the image to RGB format for better display in Matplotlib.
3. **Region of Interest (ROI)**: A polygon is defined to represent the region that is relevant for lane detection, and this area is isolated using a mask.
4. **Masking**: A binary mask is applied to the image to keep only the region of interest, and the result is displayed using Matplotlib.

## Dependencies

- OpenCV
- Matplotlib
- NumPy

## Contributing
We welcome contributions! If you have any ideas, bug fixes, or improvements, feel free to fork the repository and submit a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Open a pull request describing your changes.

## Contact
For further inquiries, please contact the project maintainer at:
- Website: [karthikmp.com](https://karthikmp.com)
