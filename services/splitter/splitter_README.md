# Splitter - Video Clip Processor

This Python script automates the process of generating multiple video clips from a single input video file, incorporating a variety of transformations and overlaying a static image. It's designed for scenarios where you might want to create snippets or highlights from longer video content, with each clip featuring a consistent graphical overlay.

## Features

- **Random Clip Generation:** Produces a specified number of video clips, each with a random start time and duration within predefined limits.
- **Burn-in Image Overlay:** Adds a static image overlay (referred to as a "burn-in image") to each video clip. This is useful for branding or adding consistent visual elements across all clips.
- **Custom Output Dimensions and Cropping:** Allows for specifying the dimensions of the output clips and crops them accordingly, which can be used to focus on a particular area of interest within the video.
- **Rotation and Resizing:** Supports rotating the video clips and resizing them to fit desired output dimensions.

## How It Works

1. **Input Specifications:** The script begins by setting up the paths to the input video and the overlay image, along with defining the target dimensions and cropping parameters for the output clips.

2. **Validation:** It checks to ensure the specified minimum clip duration is not greater than the maximum duration.

3. **Image Overlay Preparation:** Prepares the overlay image by setting its duration, resizing it to fit the designated area, and positioning it according to specified coordinates.

4. **Clip Generation Loop:** For each clip to be generated:
   - Determines a random start time within the input video's duration, ensuring the clip's end time does not exceed the video's length.
   - Creates a subclip based on the calculated start and end times.
   - Applies the overlay image to the subclip.
   - Optionally rotates and crops the subclip according to predefined parameters.
   - Resizes the final clip to fit the specified output dimensions.
   - Writes the processed clip to an output file.

## Requirements

- Python 3.x
- `moviepy` library
- An input video file and an overlay image file.

## Usage

1. Ensure you have the `moviepy` library installed. If not, you can install it using pip:

   ```
   pip install moviepy
   ```

2. Modify the script parameters (`input_file`, `burn_in_image_path`, `min_duration`, `max_duration`, `num_clips`, etc.) as needed to fit your specific use case.

3. Run the script:

   ```
   python script_name.py
   ```

## Example Usage

Given an input video (`video/Ep77.mp4`) and an overlay image (`images/77-header.png`), the script generates 30 random clips, each with a duration between 37 to 59 seconds. Each clip is overlaid with the specified image, rotated, cropped, resized to 1080x1920, and saved to the output directory with a filename starting with "Ep77-mov_".

## Note

This script is designed for flexibility and can be adapted to various content creation workflows, such as creating social media clips, video highlights, or promotional snippets from longer video content. Adjust the parameters and processing steps according to your specific needs and the characteristics of your input video and overlay image.