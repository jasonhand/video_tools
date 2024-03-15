# Captions - Burning Captions into Video

This Python script uses FFmpeg to burn subtitles from an SRT file directly into a video file. The subtitles are positioned higher than the lower third of the screen, making them more visually accessible and less likely to obscure important details in the video content.

## Prerequisites
- Python 3.x installed on your system.
- FFmpeg installed and accessible from your command line or terminal.
- An SRT file containing the captions you wish to burn into your video.

## Features
- **Customizable Vertical Margin**: Adjust the vertical positioning of the captions on the screen by modifying the `margin_vertical` value.
- **Audio Preservation**: The audio track of the original video is copied without re-encoding, ensuring no loss in audio quality.
- **Wide Compatibility**: Works with any video format supported by FFmpeg and SRT subtitle files.

## How to Use

### Setup
Ensure you have Python and FFmpeg installed on your system. You can download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).

### Running the Script
1. **Prepare Your Files**: Place your video file and SRT subtitle file in accessible locations on your filesystem.
2. **Update the Script Paths**:
   - Replace `video_file` with the path to your video file.
   - Replace `srt_file` with the path to your SRT file.
   - Replace `output_video` with the desired path for the output video.
3. **Adjust Caption Positioning** (Optional): Modify the `margin_vertical` variable to change the vertical position of the captions. Increase the value to move the captions higher.
4. **Execute the Script**: Run the script via your terminal or command prompt. Ensure you are in the directory containing the script, or provide the full path to the script.

### Command Line Execution
```sh
python burn_captions_into_video.py
```

## Troubleshooting
- **FFmpeg Not Found**: Ensure FFmpeg is installed and its binary is added to your system's PATH.
- **File Not Found Errors**: Verify the paths to your video file, SRT file, and output file are correct.
- **Permission Errors**: Ensure you have write permissions for the output directory.

## Customization
- **Caption Style**: The script uses FFmpeg's `subtitles` filter with `force_style` to position and style the subtitles. You can customize the appearance of the captions by adjusting the `force_style` parameters.

## Contribution
Feel free to fork this script and submit pull requests with any improvements or additional features.