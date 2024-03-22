# Video Speed Doubling

This Python script utilizes FFmpeg to double the speed of a given video file. By adjusting the video's playback speed, it creates a new version that plays twice as fast as the original. This utility can be particularly useful for creating time-lapse effects or shortening videos without altering their content.

## Features

- **Speed Adjustment:** Increases the video playback speed to twice its original pace.
- **Audio Removal:** Removes the audio track from the output video to prevent desynchronization issues that typically arise from speed adjustments.
- **Efficient Processing:** Leverages FFmpeg's `setpts` (Set Presentation Timestamp) filter to change the video speed efficiently, ensuring quick processing times.

## How It Works

1. **Specify Input and Output Paths:** The script requires paths to the input video file and the desired output file location.

2. **FFmpeg Command Construction:** Constructs an FFmpeg command using the provided paths. It applies a filter to change the presentation timestamps of the video frames, effectively doubling the speed.

3. **Execution and Error Handling:** Executes the FFmpeg command to perform the speed doubling. It captures and reports any errors encountered during the process, providing feedback on the operation's success or failure.

## Requirements

- Python 3.x
- FFmpeg installed and accessible in the system's PATH.

## Installation

Ensure FFmpeg is installed on your system:
- **Windows:** Download and install from [FFmpeg's official website](https://ffmpeg.org/download.html).
- **macOS:** Use Homebrew with the command `brew install ffmpeg`.
- **Linux:** Use your distribution's package manager, e.g., `sudo apt-get install ffmpeg`.

## Usage

1. Adjust the `input_video_path` and `output_video_path` variables to match the paths to your input and desired output video files.

2. Run the script:
   ```
   python double_speed.py
   ```

## Example

To double the speed of a video named `input.mov` located in `video/shortened` and save the sped-up version as `output.mov` in `video/2xSpeed`:

```python
input_video_path = 'video/shortened/input.mov'
output_video_path = 'video/2xSpeed/output.mov'
double_speed(input_video_path, output_video_path)
```

The output video will play at double the original speed, and its audio track will be removed to avoid synchronization issues. This script is ideal for quickly creating time-lapse effects or condensing longer videos into shorter, sped-up versions without modifying the visual content.