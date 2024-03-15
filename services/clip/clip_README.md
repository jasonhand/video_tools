# Clipper - Video Trimming and Enhancement

This Python script provides a convenient method for trimming the beginning of a video file and enhancing its quality using FFmpeg. It's designed to quickly remove unwanted starting portions of a video and improve its visual and auditory quality for further use or distribution.

## Features

- **Time-based Trimming:** Allows for the removal of a specified number of seconds from the beginning of the video.
- **Quality Enhancement:** Improves video quality by adjusting the video and audio codecs and bitrates.
- **Flexible Configuration:** The script can be easily adapted to trim different durations or adjust quality settings based on specific needs.

## How It Works

1. **Configuration:** The script accepts paths to the input and output video files, along with an optional parameter specifying the number of seconds to trim from the start of the video.

2. **FFmpeg Command Construction:** Constructs an FFmpeg command incorporating the specified input, the duration to trim, and settings for enhancing video and audio quality. This includes the use of the H.264 video codec with a higher bitrate and the AAC audio codec also with a higher bitrate.

3. **Execution and Feedback:** Executes the constructed FFmpeg command to trim and enhance the video, providing feedback upon successful completion or reporting any errors encountered.

## Requirements

- Python 3.x
- FFmpeg installed and accessible in the system's PATH. If using a custom installation path for FFmpeg, adjust the script to point to the correct location.

## Installation

Ensure FFmpeg is installed on your system:
- **Windows:** Download and install from [FFmpeg's official website](https://ffmpeg.org/download.html).
- **macOS:** Use Homebrew with `brew install ffmpeg`.
- **Linux:** Use your distribution's package manager, e.g., `sudo apt-get install ffmpeg`.

## Usage

1. Adjust the `input_file` and `output_file` variables to point to your specific video files.

2. (Optional) Modify the `trim_start` parameter if you wish to trim a different amount from the start of the video.

3. Run the script:
   ```
   python trim_enhance_video.py
   ```

## Example

To trim the first 6 seconds from a video file named `S63168.mp4` and save the enhanced version as `S63168-clipped.mp4`:

```python
input_video = 'video/original/S63168.mp4'
output_video = 'video/clipped/S63168-clipped.mp4'
trim_and_enhance_video(input_video, output_video, trim_start=6)
```

The output video will have improved quality with specified codecs and bitrates, and the first 6 seconds of the original video will be removed.

## Note

This utility is useful for preparing video content for presentations, sharing on social media, or any situation where the initial part of a video is unnecessary, and quality improvements are desired. Adjust the codec and bitrate settings as needed to balance quality and file size based on your specific requirements.