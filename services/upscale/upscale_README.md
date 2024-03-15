# Upscale - Video Upscaling Utility

This Python script provides a user-friendly method for upscaling video files to a higher resolution using FFmpeg, a powerful multimedia framework. It automatically handles the generation of output file names to reflect the new resolution and incorporates optimal settings for video and audio quality.

## Features

- **Automatic Output Filenaming:** Generates output filenames that prepend the target resolution to the original filename, making it easy to identify upscaled videos.
- **Customizable Resolution:** Allows specifying the target resolution, with a default setting of `1920x1080` (Full HD). This can be adjusted to other resolutions as needed.
- **Optimized Encoding Settings:** Uses the `libx264` video codec for high-quality video output, and `aac` for audio, with preset bitrates to ensure a good balance between quality and file size.
- **Flexible Frame Rate and Bitrate:** Configures the video to a standard frame rate of 30 fps, with a video bitrate suited for Full HD content. Audio bitrate is set to ensure clear sound quality.

## How It Works

1. **Specify Input and Target Resolution:** The script takes an input video file path and a target resolution. The resolution defaults to `1920x1080` but can be customized.

2. **Filename Generation:** It computes an output filename based on the input file's name, automatically adding the target resolution as a prefix.

3. **FFmpeg Command Construction:** Constructs an FFmpeg command using the input and output file paths, the specified resolution, and predefined settings for video and audio codecs, bitrates, and frame rate.

4. **Execution and Error Handling:** Executes the FFmpeg command to perform the upscaling. It provides feedback on success or captures and reports any errors encountered during the process.

## Requirements

- Python 3.x
- FFmpeg installed and accessible in the system's PATH.

## Installation

Ensure FFmpeg is installed on your system:
- **Windows:** Download and install from [FFmpeg's official website](https://ffmpeg.org/download.html).
- **macOS:** Use Homebrew with the command `brew install ffmpeg`.
- **Linux:** Use your distribution's package manager, e.g., `sudo apt-get install ffmpeg` for Debian/Ubuntu.

## Usage

1. Place the script in the same directory as your video files or modify the `input_file` path to point to the location of your video file.

2. (Optional) Adjust the `resolution` variable if you want to upscale to a resolution different from the default `1920x1080`.

3. Run the script:
   ```
   python upscale_video.py
   ```

## Example

To upscale a video named `input.mp4` located in `video/original` to Full HD resolution and save the output in `video/upscaled`:

```python
input_file = 'video/original/input.mp4'
resolution = '1920x1080'
upscale_video(input_file, resolution)
```

The output video will be saved as `video/upscaled/1920x1080-input.mp4`.

## Note

This script is designed to be easily adaptable for different upscaling needs. Modify the `bitrate`, `framerate`, `audio_codec`, `audio_bitrate`, and `video_codec` variables as necessary to tailor the upscaling process to specific requirements or preferences.