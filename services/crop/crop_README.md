# Cropping Tool

## Overview

This Python script automates the process of cropping videos to a portrait orientation, focusing on the center of the video. It's particularly useful for adjusting landscape videos into a portrait format, maintaining a 9:16 aspect ratio. The script utilizes FFmpeg for video processing, leveraging its powerful filtering capabilities to crop and re-encode video files efficiently.

## Features

- **Automatic Aspect Ratio Adjustment**: Converts landscape videos to portrait orientation by cropping to a 9:16 aspect ratio, focusing on the center.
- **Support for Various Video Formats**: Works with common video file formats including `.mp4`, `.mov`, `.avi`, and `.mkv`.
- **Batch Processing**: Processes all video files in a specified input directory, outputting the cropped videos to a designated output directory.

## Prerequisites

- **FFmpeg**: The script requires FFmpeg to be installed on your system. FFmpeg should be accessible from the command line (i.e., included in your system's PATH).
- **Python 3**: The script is written for Python 3. Ensure Python 3 is installed and configured correctly on your system.

## Installation

1. **Install FFmpeg**: If FFmpeg is not already installed, download and install it from [FFmpeg's official website](https://ffmpeg.org/download.html) or through your operating system's package manager.

2. **Download the Script**: Clone or download the script to your local machine.

## Usage

1. **Prepare Your Videos**: Place all the videos you wish to crop into the input directory. The script will process each video file, converting landscape videos to portrait orientation by cropping as necessary.

2. **Set Directory Paths**: Open the script in a text editor and modify the `input_dir` and `output_dir` variables to point to your specific directories:
   
   ```python
   input_dir = '/path/to/your/input_videos'
   output_dir = '/path/to/your/output_videos'
   ```
   
3. **Run the Script**: Execute the script from the command line:

   ```bash
   python3 path/to/script.py
   ```
   
   The script will process each video file in the input directory, saving the cropped videos to the output directory.

## Functionality

- **`get_video_dimensions(filename)`**: Retrieves the dimensions of the video.
- **`crop_video_to_portrait(source_file, target_file)`**: Crops the video to portrait orientation based on the calculated dimensions.
- **`main()`**: Orchestrates the processing of each video file in the input directory.

## Notes

- The script assumes that FFmpeg is correctly installed and configured on your system.
- Cropped videos will be saved with the prefix "cropped_" in the file name to distinguish them from the original files.
- Ensure you have the necessary permissions to read and write to the specified directories.

## License

This tool is open-sourced and freely available for personal and commercial use.