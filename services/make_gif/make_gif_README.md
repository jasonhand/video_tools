# Make-gif - High-Quality GIF Conversion Utility

This Python script offers a solution for converting video files into high-quality GIFs using FFmpeg, leveraging a custom color palette to enhance the output quality. The script generates a palette from the input video to ensure the GIF maintains visual fidelity, then uses this palette to create the final GIF.

## Features

- **Custom Color Palette Generation:** Creates a palette from the input video to ensure the GIF retains as much of the original video's color accuracy as possible.
- **High-Quality Scaling:** Utilizes the `lanczos` scaling algorithm to resize the video, enhancing the quality of the resulting GIF.
- **Configurable FPS and Scale:** Sets the frames per second (fps) and scale for the GIF conversion, allowing for balance between quality and file size.
- **Automatic Palette Cleanup:** Optionally removes the generated palette file after the GIF is created, keeping the workspace tidy.

## How It Works

1. **Palette Generation:** Generates a color palette from the input video. This palette captures the video's color scheme, which is crucial for producing a high-quality GIF.

2. **GIF Creation Using Palette:** Utilizes the generated palette to convert the input video into a GIF. This step involves resizing the video and applying the `lanczos` filter for high-quality output.

3. **Output and Cleanup:** Saves the converted GIF to the specified path and optionally deletes the temporary palette file to avoid clutter.

## Requirements

- Python 3.x
- FFmpeg installed and accessible in the system's PATH.

## Installation

Ensure FFmpeg is installed on your system:
- **Windows:** Download and install from [FFmpeg's official website](https://ffmpeg.org/download.html).
- **macOS:** Use Homebrew with `brew install ffmpeg`.
- **Linux:** Use the package manager, e.g., `sudo apt-get install ffmpeg`.

## Usage

1. Set the `input_video_path` variable to the path of your source video file.

2. Set the `output_gif_path` variable to the desired path for the resulting GIF file.

3. (Optional) Adjust the `palette_path` if you prefer to specify a different location or filename for the generated palette.

4. Run the script:
   ```
   python convert_video_to_gif.py
   ```

## Example

To convert a video named `input.mov` located in `video/shortened` to a high-quality GIF and save it as `output.gif` in `video/gif`:

```python
input_video_path = 'video/shortened/input.mov'
output_gif_path = 'video/gif/output.gif'

convert_video_to_high_quality_gif(input_video_path, output_gif_path)
```

The script will create a high-quality GIF version of `input.mov`, optimizing color accuracy and visual quality.

## Note

This utility is designed for users looking to convert videos to GIFs without sacrificing color quality, ideal for presentations, social media, or web content where GIF format is preferred. The settings can be adjusted to suit specific needs, such as changing the fps or scale for different balance points between quality and file size.