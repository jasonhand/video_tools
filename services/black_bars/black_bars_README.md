# Black Bar Removal

This Python script provides a utility for processing videos, specifically for resizing and cropping videos to a target resolution while optionally removing additional space from the top and bottom of the video frame. The script utilizes the `ffmpeg` command-line tool, making it a powerful option for video manipulation.

## Features

- **Resizing**: Adjusts the width of the video to a target width while maintaining the aspect ratio.
- **Cropping**: After resizing, the video is cropped to achieve a specified target resolution. This step can remove unwanted black bars or other unnecessary parts from the video frame.
- **Additional Cropping**: Offers an option to crop additional pixels from the top and bottom of the video, providing more control over the final video appearance.

## How It Works

1. **Scale Calculation**: The script calculates a scale factor based on the ratio of the target width to the original width of the video. This scale factor is used to adjust the video's width while maintaining its aspect ratio.

2. **New Height Calculation**: After scaling, the new height of the video is calculated. This height considers the scale factor applied to the original height of the video.

3. **Cropping Calculation**: The script computes how much of the video needs to be cropped from the top and bottom to reach the target height. An additional cropping parameter allows for further reduction of the video frame, useful for removing black bars or other undesired space.

4. **FFmpeg Command**: Using the `ffmpeg` command-line tool, the video is first scaled and then cropped according to the calculated dimensions. The `scale` and `crop` filters in `ffmpeg` are used to perform these actions.

5. **Execution**: The constructed `ffmpeg` command is executed, resulting in a video file that matches the specified target resolution and optionally has additional space removed from the top and bottom.

## Usage

To use this script, you need to provide the input and output file paths, the original and target resolutions, and optionally specify additional pixels to crop from the top and bottom of the video frame.

```python
input_video = "path/to/original/video.mp4"
output_video = "path/to/output/video.mp4"
original_res = (original_width, original_height)  # Original resolution of the video
target_res = (target_width, target_height)  # Desired target resolution
additional_crop = 100  # Optional: Additional pixels to crop from the top and bottom

process_video(input_video, output_video, original_res, target_res, additional_crop)
