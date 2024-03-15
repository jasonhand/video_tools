# Stacked - Portrait Stacked

This Python script enhances video presentations by combining 2 video sources (example: speaker footage and slide content) into a single, visually appealing portrait video. 

This allows content such as Datadog On to be repurposed on social media in a format optimized for mobile viewing, featuring a distinct background color and improved accessibility.

>NOTE: It is highly recommended to run the black_bars.py script prior to running this script. This crops the original video containing slides so that the black bars at the top and bottom are removed (if necessary).

>WARNING: This process could take some time depending on the length of your original video source. If you are testing things and want to see an output from a shorter video, it is recommended you try out the trimmer.py script to reduce your original video to something much smaller to work with.

## Features

- **Video Resizing:** Utilizes `ffmpeg` to resize both video sources (i.e. speaker and slide videos) to a target width while maintaining aspect ratios, ensuring content is visually consistent and optimized for the target resolution.
- **Dynamic Background:** Introduces a colored background, customizable to match branding or aesthetic preferences, enhancing the overall look of the combined video.
- **Audio Preservation:** Maintains the original audio from the speaker video, ensuring the message is delivered without compromise.
- **Vertical Layout Optimization:** Arranges speaker footage and slides in a vertical sequence, making the final video suitable for platforms favoring portrait orientation.

## Workflow Overview

1. **Preparation:** Resizes the input videos (speaker footage and slides) to a designated width, ensuring compatibility with the target display resolution.

2. **Background Creation:** Generates a color clip using a specified color, serving as the backdrop for the combined video.

3. **Vertical Assembly:** Stacks the resized speaker video atop the slide video against the colorful background, optimizing the layout for portrait orientation.

4. **Audio Integration:** Attaches the original audio from the speaker video to the final composition, preserving the presentation's auditory component.

5. **Export:** Outputs the assembled video to a file, ready for distribution or upload to video-sharing platforms.

## Requirements

- Python 3.x
- `moviepy` library for video processing in Python.
- `ffmpeg` installed and accessible from the command line for video resizing tasks.

## Installation

Ensure you have Python 3.x installed on your system. Install the required Python library using pip:

```sh
pip install moviepy
```

Verify that `ffmpeg` is installed:

```sh
ffmpeg -version
```

If `ffmpeg` is not installed, download and install it from [FFmpeg's official website](https://ffmpeg.org/download.html) or through your system's package manager.

## Usage Instructions

1. Customize the script parameters (`input_path`, `output_path`, `desired_width`, `background_color`, etc.) to suit your video processing needs.

2. Run the script:

```sh
python script_name.py
```

## Example

Given trimmed speaker footage (`video/original/speakers.mp4`) and corresponding slide content (`video/original/slides.mp4`), the script generates a single video (`video/original/combined_video_portrait.mp4`). This video features both elements against a Datadog Purple background, arranged for optimal mobile viewing, with the speaker's original audio.

## Customization

- **Background Color:** Modify the `background_color` variable to align with your brand or preferred aesthetic.
- **Target Resolution:** Adjust `desired_width` and `desired_height` to match your output resolution requirements.
- **Additional Adjustments:** Further customize the positioning, scaling, or duration of individual components as needed for your specific project.

This script streamlines the creation of engaging, mobile-friendly video content, making it an invaluable tool for educators, marketers, and content creators aiming to enhance their video presentations.