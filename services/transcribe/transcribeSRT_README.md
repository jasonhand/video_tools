# Transcribing Audio to SRT using Whisper

This script leverages OpenAI's Whisper model to transcribe audio from a specified file into the SubRip Text (SRT) format. It's designed to convert spoken words into written text with timestamps, making it ideal for generating accurate subtitles for videos or audio files.

## Features
- **Audio Transcription**: Converts audio files to written text using OpenAI's advanced Whisper model.
- **SRT Format Output**: Outputs transcription in SRT format, complete with timestamps, ready for use as video subtitles.
- **Segment Handling**: Processes audio in segments to ensure detailed and structured output with accurate timings.
- **Customizable Path**: Allows specifying paths for both the input audio and the output SRT file.

## Requirements
- Python environment with Whisper installed (`pip install openai-whisper`).
- An audio file (preferably in MP3 format) for transcription.

## Usage
1. **Prepare Your Audio File**: Ensure your audio file is accessible to the script. Update `audio_path` with the location of your audio file.
2. **Specify Output Path**: Change `srt_path` to your desired output location for the SRT file.
3. **Run the Script**: Execute the script in your Python environment. The script will load the Whisper model, transcribe the audio, and save the transcription in SRT format at the specified location.

## How It Works
1. **Load Model**: The script begins by loading the Whisper model, readying it for transcription.
2. **Transcribe Audio**: It then processes the audio file, transcribing the content while noting timestamps for each spoken segment.
3. **Format Output**: The transcription is formatted into SRT, assigning sequential numbers to segments and converting timestamps to the HH:MM:SS,MMM format.
4. **Save to File**: Finally, the SRT content is written to the specified file path, completing the process.

## Customization
- The `seconds_to_hms` function can be adjusted for different time formats if needed.
- Modify `audio_path` and `srt_path` to fit your file system and requirements.

## Note
This script is designed for simplicity and ease of use. However, transcription accuracy and the quality of the output SRT file may vary based on the audio quality and clarity of speech in the source material.