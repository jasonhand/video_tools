# Trimmer - Video Trimming Utility

This Python script provides a straightforward utility for trimming video files to a specified duration using `ffmpeg`, a powerful multimedia framework capable of handling a wide array of video processing tasks. The script trims the beginning of a video to the desired length without re-encoding, preserving the original quality and ensuring efficient processing.

## Features

- **Simple Video Trimming:** Trims the input video to a specific duration, starting from the beginning of the video.
- **No Re-Encoding:** Utilizes the `-c copy` option in `ffmpeg` to copy the video and audio streams directly without re-encoding, preserving the original quality and ensuring fast processing.
- **Customizable Duration:** Allows specifying the duration to which the video should be trimmed, with a default setting of 1 minute.

## How It Works

1. **Input and Output Specification:** The script requires paths to the input video file and the desired output file location, as well as the duration to trim the video to.
   
2. **`ffmpeg` Command Construction:** Constructs an `ffmpeg` command using the provided parameters, specifying the input video, the duration to trim to, and the output file path.

3. **Execution:** Runs the constructed `ffmpeg` command using Python's `subprocess.run` method, effectively trimming the video to the specified duration.

4. **Error Handling:** Catches and reports any errors encountered during the `ffmpeg` command execution, providing feedback on the operation's success or failure.

## Requirements

- Python 3.x
- `ffmpeg` installed and accessible in the system's PATH.

## Installation

Ensure `ffmpeg` is installed on your system:
- On **Windows**, download and install from [FFmpeg's official website](https://ffmpeg.org/download.html).
- On **macOS**, use Homebrew: `brew install ffmpeg`.
- On **Linux**, use your distribution's package manager, e.g., `sudo apt-get install ffmpeg` for Debian/Ubuntu.

No additional Python packages are required for this script.

## Usage

1. Modify the `input_video` and `output_video` variables to reflect the paths to your input and desired output video files.

2. Optionally, adjust the `trim_duration` parameter to specify the length of the video after trimming. Format should be `"HH:MM:SS"`.

3. Run the script:
   ```
   python trim_video_script.py
   ```

## Example

To trim a video file named `slides.mp4` to 1 minute and save it as `trimmed-slides.mp4`:

```python
input_video = "video/original/slides.mp4"
output_video = "video/original/trimmed-slides.mp4"
trim_video(input_video, output_video)
```

This utility is ideal for quickly trimming videos for use in presentations, social media, or other platforms where video length might be constrained.