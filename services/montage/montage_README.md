# Video Montage

This Python script is designed to create a video montage by clipping random sections from each video in a specified directory and merging them into a new video of a predetermined length. The script can handle videos of various formats, ensuring the final montage is outputted in portrait mode, making it especially useful for preparing content tailored for platforms favoring vertical video formats.

## Features

- **Automatic Video Cropping**: Automatically crops videos to a portrait orientation, focusing on the center.
- **Flexible Duration Setting**: Allows specification of the total duration of the final montage video.
- **Supports Multiple Video Formats**: Capable of processing common video file formats, including `.mp4`, `.mov`, `.avi`, and `.mkv`.
- **Batch Processing**: Processes all video files in the specified input directory, creating a seamless montage.

## Prerequisites

- **Python 3**: The script is written for Python 3 and requires it to be installed on your system.
- **FFmpeg**: This tool relies on FFmpeg for video processing, which must be installed and accessible from your system's command line.

## Installation

1. **Install FFmpeg**: Ensure FFmpeg is installed on your system. It can be downloaded from the [official FFmpeg website](https://ffmpeg.org/download.html) or installed via your system's package manager.
2. **Download the Script**: Clone or download this script to your local machine.

## Usage

1. **Prepare Input Videos**: Place the videos you want to include in the montage into the input directory.
2. **Configure the Script**: Open the script in a text editor. Update the `input_dir`, `output_dir`, `final_video_length`, and `output_filename` variables to suit your project needs:

   ```python
   input_dir = '/path/to/input_videos'
   output_dir = '/path/to/output_videos'
   final_video_length = 30  # In seconds
   output_filename = 'final_output.mp4'
   ```

3. **Run the Script**: Navigate to the script's directory in your command line interface and execute the script:

   ```bash
   python3 script_name.py
   ```

   The script will process the videos in the input directory and generate a final montage video in the output directory.

## Functionality

- **`get_video_length(filename)`**: Retrieves the length of a video.
- **`clip_random_section(source_file, duration, index)`**: Clips a random section from a source video.
- **`concatenate_clips(clip_paths, output_file)`**: Merges the clipped sections into a single montage video.
- **`main()`**: Orchestrates the video processing workflow, from clipping to concatenation.

## Notes

- Videos are cropped to maintain a portrait orientation for the final output.
- The script processes each video file in the specified directory, ignoring non-video files.
- Temporary files generated during the process are cleaned up automatically.

## License

This script is open-source and available for personal and commercial use.