# M4A to MP3 Converter

This Python script provides an easy-to-use solution for converting M4A audio files to MP3 format using FFmpeg. It includes functionality to process a single M4A file as well as batch convert all M4A files within a specified directory. After conversion, the original M4A files are moved to a designated output directory, making it convenient to manage both the original and converted files.

## Features

- **Single File Conversion:** Convert a single M4A file to MP3 format.
- **Batch Conversion:** Automatically convert all M4A files in a specified directory to MP3 format.
- **File Management:** Moves the original M4A files to a specified output directory after conversion.

## Prerequisites

Before running the script, ensure you have the following installed on your system:

- **Python:** The script is written in Python and requires Python to be installed to run.
- **FFmpeg:** This script uses FFmpeg for the conversion process. Ensure FFmpeg is installed and accessible from your system's PATH.

## Installation

1. **Install Python:** Make sure Python is installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install FFmpeg:** Follow the instructions on the [FFmpeg official website](https://ffmpeg.org/download.html) to install FFmpeg and add it to your system's PATH.

3. **Download the Script:** Download the Python script to your local machine.

## Usage

The script can be run from the command line or integrated into a larger Python project.

### Command Line Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using Python and specify the input and output directories. Example:

```bash
python m4a_to_mp3_converter.py
```

Note: The example usage in the script uses placeholder paths. You will need to modify the `input_directory` and `output_directory` variables in the script to match your actual file locations.

### Integrating into Projects

Import the `convert_m4a_to_mp3` or `convert_all_m4a` function from the script and call it with the appropriate file paths or directories as arguments.

## Important Notes

- Ensure you have the legal right to convert any audio files you process with this script.
- The script's performance and the quality of the MP3 output can vary based on the FFmpeg settings used. Adjust the command parameters in the script as needed to suit your quality requirements or specific use case.

## Troubleshooting

If you encounter errors related to FFmpeg not being found, ensure that FFmpeg is correctly installed and that its binary location is included in your system's PATH environment variable. For issues related to file access permissions, check that you have the necessary rights to read the input files and write to the output directory.

## Contributing

Contributions to the script are welcome! Feel free to fork the repository, make your improvements, and submit a pull request.

## License

Specify the license under which the script is released, or state that it is available as open-source software and can be freely used and modified.