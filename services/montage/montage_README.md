# Multi-Version Video Montage Generator

This Python script automates the creation of multiple video montages from a collection of video clips. It's designed to take video files from a specified input directory, clip random sections from each, and then concatenate these clips into several final montage videos, each of a specified duration. The script is especially useful for generating multiple variations of video montages, allowing users to choose their preferred version from the outputs.

## Features

- **Multiple Output Versions**: Generates a specified number of montage videos, each with a unique set of clips.
- **Customizable Final Video Length**: Allows specifying the desired length for each montage video.
- **Supports Various Video Formats**: Compatible with popular video formats such as `.mp4`, `.mov`, `.avi`, and `.mkv`.
- **Automated Video Processing**: Leverages FFmpeg for clipping and concatenating video sections, streamlining the video creation process.

## Prerequisites

- **FFmpeg**: Ensure FFmpeg is installed on your system and accessible from the command line.
- **Python 3**: This script requires Python 3 to run.

## Installation

1. **Install FFmpeg**: Download and install FFmpeg from [the official website](https://ffmpeg.org/download.html) or use your system's package manager. Verify the installation by running `ffmpeg -version` in your command line or terminal.

2. **Prepare the Script**: Clone or download this script to your local system in a directory of your choice.

## Usage

1. **Configure the Script**:
   - Update the `input_dir` variable to the path of your directory containing the input video files.
   - Adjust the `output_dir` variable to specify where you want the montage videos to be saved.
   - Set the `final_video_length` variable to determine the duration of each final montage video (in seconds).
   - Modify the `num_output_files` variable to change the number of montage videos to generate.

2. **Run the Script**:
   - Navigate to the script's directory in your terminal or command line.
   - Execute the script by running `python3 script_name.py`, replacing `script_name.py` with the actual name of the script file.

## How It Works

- The script first scans the input directory for video files matching the supported formats.
- It then clips a random section from each video, aiming to fill the specified `final_video_length` for the montage.
- These clips are concatenated to form a montage video. This process is repeated `num_output_files` times to create multiple montage versions.
- Finally, the script cleans up any temporary files generated during the process.

## Customization

- **Video Duration**: Adjust the `final_video_length` variable to increase or decrease the duration of the montage videos.
- **Number of Montages**: Increase or decrease the `num_output_files` variable to change how many versions of the montage are created.

## Cleanup

The script automatically deletes temporary clip files and the temporary inputs list used for concatenation, keeping your output directory clean and containing only the final montage videos.

## License

This script is provided "as is", without warranty of any kind, express or implied. Feel free to use, modify, and distribute as needed.