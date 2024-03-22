
# Whisper Audio Transcription

This Python script utilizes OpenAI's Whisper model to transcribe audio files to text. It's designed to process audio files, convert them into plain text transcriptions, and save these transcriptions to a specified directory.

## Features

- Transcribes audio files using OpenAI's Whisper model.
- Supports audio files in formats that Whisper can process (primarily tested with MP3).
- Outputs transcriptions in plain text format.
- Automatically handles the creation of the output directory if it doesn't exist.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your machine.
- Whisper Python package installed. You can install it using pip:
  ```sh
  pip install whisper
  ```
- FFmpeg installed on your system if working with non-WAV formats. Whisper relies on FFmpeg to process various audio file formats.

## Installation

No additional installation is required for the script itself, provided you have Python and the necessary packages installed.

## Usage

To use this script, follow these steps:

1. Place your audio file(s) in a known directory.
2. Update the `audio_path` and `output_directory` variables in the script to point to your audio file and desired output location, respectively.
3. Run the script:
   ```sh
   python transcribe_audio_to_text.py
   ```

### Example

```sh
audio_path = "../../output/apple_audio/converted_mp3/Session4.mp3"
output_directory = "../../video_tools/output/transcriptions"
```

This will process `Session4.mp3`, transcribe it, and save the transcription as `Session4.txt` in the specified output directory.

## Customizing

You can customize the script by modifying the `audio_path` and `output_directory` variables to point to different locations as per your project's structure.

## Contributing

Feel free to fork the project and submit pull requests with any enhancements or fixes. Your contributions are always welcome!

## License

Specify your project's license here. If you haven't decided on a license, consider options like MIT or GPL for open-source projects.

## Contact

If you have any questions or feedback, please reach out to me at your.contact@email.com.

---

Remember to replace placeholders (like email addresses or specific paths) with actual data relevant to your project. This README provides a comprehensive guide for users to get started with your transcription script, including setup, usage, and customization instructions.