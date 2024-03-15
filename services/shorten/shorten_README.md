# Shorten - Video Clipping Utility

This Python script offers an efficient way to create a new video from selected portions of an existing video. By specifying a series of start and end timestamps, users can extract and concatenate multiple segments from the source video, generating a seamlessly edited output video. This utility is particularly useful for creating highlight reels, compiling specific scenes, or summarizing content.

## Features

- **Selective Clipping:** Allows for extracting multiple segments from a source video based on specified start and end timestamps.
- **Flexible Timestamps:** Supports timestamps in both seconds and "min:sec" formats, providing versatility in defining clip boundaries.
- **Automatic Concatenation:** Seamlessly joins the specified clips into a single output video.
- **High-Quality Output:** Utilizes `libx264` for video encoding and `aac` for audio encoding, ensuring high-quality output.

## How It Works

1. **Source Video and Output Path:** The script requires paths to the source video file and the desired output file location.

2. **Defining Timestamps:** Users specify a list of tuples containing start and end times for each desired video segment. Times can be in seconds or "min:sec" format.

3. **Processing Segments:** For each timestamp pair, the script:
   - Converts "min:sec" formatted timestamps to seconds if necessary.
   - Creates a subclip for the defined segment.
   - Collects all subclips into a list.

4. **Concatenation and Output:** Concatenates all subclips into a final clip and writes the result to the specified output path, using `libx264` for video and `aac` for audio encoding.

## Requirements

- Python 3.x
- `moviepy` library

## Installation

1. Ensure you have Python 3.x installed on your system.

2. Install `moviepy` using pip if you haven't already:
   ```
   pip install moviepy
   ```

## Usage

1. Modify the `source_video_path`, `output_video_path`, and `timestamps` variables in the script to match your source video and desired output specifications.

2. Run the script:
   ```
   python clip_video_script.py
   ```

## Example

Given a source video named `input.mov` located in `video/original`, the script can generate an output video named `output.mov` in `video/shortened` by concatenating specified segments:

```python
source_video_path = 'video/original/input.mov'
output_video_path = 'video/shortened/output.mov'
timestamps = [
 ('00:04', '02:00'),
 # Additional timestamps...
]

clip_video(source_video_path, timestamps, output_video_path)
```

The output video will contain only the segments specified in the `timestamps` list, concatenated in the order they're listed.

## Note

This utility is particularly useful for video editing tasks that require precise segment selection and high-quality output. Adjust the timestamps and paths according to your specific needs to create customized video clips efficiently.