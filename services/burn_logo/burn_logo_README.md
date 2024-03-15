# Image Overlay on Video Utility

This Python utility leverages FFmpeg to overlay an image onto a video file, allowing customization of the image's position and size within the video frame. It's an excellent tool for adding logos, watermarks, or any other static graphic elements to videos.

## Features

- **Customizable Position:** Place the image anywhere within the video frame by specifying the X and Y coordinates.
- **Adjustable Image Size:** Control the dimensions of the image to ensure it fits perfectly within your video without overpowering the content.
- **High-Quality Output:** Maintains the original video and audio quality while embedding the image into the video.
- **Versatility:** Useful for branding purposes, creating watermarked content, or simply adding visual elements to enhance videos.

## Requirements

- **Python:** Ensure you have Python installed on your system. This script was tested with Python 3.
- **FFmpeg:** This script requires FFmpeg to be installed and accessible in your system's PATH. FFmpeg handles the processing of video and image files.

## Installation

1. **Install Python:** Download and install Python from [python.org](https://www.python.org/downloads/) if it's not already installed on your system.

2. **Install FFmpeg:** 
   - **Windows:** Download from [FFmpeg.org](https://ffmpeg.org/download.html) and add it to your system's PATH.
   - **macOS:** Install using Homebrew with `brew install ffmpeg`.
   - **Linux:** Use your distribution's package manager, for example, `sudo apt-get install ffmpeg` for Debian/Ubuntu.

## Usage

1. **Specify File Paths:** Modify the `video_file`, `image_file`, and `output_video` variables to point to your source video file, the image you wish to overlay, and the desired output path for the video with the image burned in.

2. **Set Position and Size:** Adjust the `image_position` and `image_size` variables to place and scale the image as needed. The position is specified as "X:Y" coordinates, where "0:0" is the top-left corner of the video. The size is specified as "widthxheight".

3. **Run the Script:** Execute the script using Python. The script will process the video and image, overlaying the image at the specified position and size, and save the result to the specified output path.

```bash
python burn_image_into_video.py
```

4. **Check the Output:** Upon successful execution, the script prints a confirmation message. The output video will contain the overlay image at the specified position and size.

## Example Usage

In the script's main section, paths are set for demonstration purposes:

```python
video_file = "/path/to/video.mp4"
image_file = "/path/to/image.png"
output_video = "/path/to/output_video.mp4"
image_position = "50:50"  # Overlay position within the video frame
image_size = "250x250"  # Desired dimensions of the overlay image
```

## Troubleshooting

- If FFmpeg commands fail, ensure FFmpeg is correctly installed and accessible from the command line.
- Verify the paths to your video and image files are correct and the files are accessible.

This utility offers a convenient way to enhance your videos with static images, providing flexibility in how and where these images appear within your content.