# Mp3 - Video to MP3 Conversion Utility

This utility is a straightforward Python script designed to extract audio from any video file and save it as a high-quality MP3 file. This process is especially useful for creating audio transcripts from video content, listening to the audio of a video on devices without video playback capability, or for any scenario where you need to isolate the audio track from video files.

## Features

- **Simple and Efficient:** Quickly extracts audio from video files with a minimalistic approach.
- **High Audio Quality:** Utilizes the `-q:a 0` option in FFmpeg to ensure the extracted audio is of the best possible quality.
- **Flexible Input and Output:** Allows specifying both the input video path and the desired output MP3 file path.

## Requirements

- **Python:** This script was developed with Python and requires a Python interpreter to run. It's compatible with Python 3.
- **FFmpeg:** This tool uses FFmpeg for processing video and audio, which must be installed and accessible from your system's PATH. FFmpeg is a powerful multimedia framework capable of handling a wide array of audio and video formats.

## Installation

1. **Install Python:** Ensure you have Python installed on your system. Python can be downloaded from [python.org](https://www.python.org/downloads/).

2. **Install FFmpeg:** 
   - **Windows:** Download from [FFmpeg.org](https://ffmpeg.org/download.html) and add FFmpeg to your system's PATH.
   - **macOS:** Install using Homebrew with `brew install ffmpeg`.
   - **Linux:** Use your distribution's package manager, e.g., `sudo apt-get install ffmpeg` for Debian/Ubuntu.

## Usage

1. **Specify Video and Output Paths:** In the script, update the `input_video` and `output_audio` variables with the full paths to your source video file and where you want to save the MP3 file, respectively.

2. **Run the Script:** Execute the script from the command line or an IDE. The script will extract the audio from the specified video file and save it as an MP3 file at the specified output location.

```bash
python video_to_mp3.py
```

3. **Check the Output:** The script will print a confirmation message once the audio has been successfully extracted and saved to the specified output path. In case of errors, diagnostic information will be printed to help troubleshoot the issue.

## Example Usage

The script includes an example usage scenario that can be adjusted to fit your needs:

```python
input_video = "/path/to/your/video.mp4"
output_audio = "/path/to/your/output_audio.mp3"
video_to_mp3(input_video, output_audio)
```

## Troubleshooting

- If you encounter errors related to FFmpeg not being found, ensure FFmpeg is correctly installed and its executable is in your system's PATH.
- Check that the paths to the input video and output audio file are correct and accessible by the script.

This utility offers a convenient way to extract audio from videos for transcription or other audio-only applications, leveraging the power of FFmpeg with the simplicity of a Python script.