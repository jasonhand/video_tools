import subprocess
import os
from shutil import move

def convert_m4a_to_mp3(m4a_file_path, mp3_file_path):
    """
    Converts an M4A file to MP3 format using FFmpeg.

    :param m4a_file_path: Path to the source M4A file.
    :param mp3_file_path: Path where the MP3 file will be saved.
    """
    # Debug: Print the file paths and their types
    print(f"Input file path: {m4a_file_path} (type: {type(m4a_file_path)})")
    print(f"Output file path: {mp3_file_path} (type: {type(mp3_file_path)})")
    
    # Adjusted command to ensure compatibility
    command = f'ffmpeg -i "{m4a_file_path}" -vn -ar 44100 -ac 2 -ab 192k -f mp3 "{mp3_file_path}"'
    try:
        subprocess.check_call(command, shell=True)
        print(f"Conversion complete: {mp3_file_path}")
    except subprocess.CalledProcessError:
        print("Failed to convert file. Ensure FFmpeg is installed and the input file path is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_all_m4a(input_directory, output_directory):
    """
    Converts all M4A files found in the input directory to MP3 format and
    moves the original files to the output directory after conversion.
    """
    for filename in os.listdir(input_directory):
        if filename.endswith(".m4a"):
            m4a_file_path = os.path.join(input_directory, filename)
            # Generate MP3 file name by replacing the extension
            mp3_file_name = filename.replace('.m4a', '.mp3')
            mp3_file_path = os.path.join(output_directory, mp3_file_name)
            
            convert_m4a_to_mp3(m4a_file_path, mp3_file_path)
            # Move the original M4A file to the output directory after conversion
            move(m4a_file_path, output_directory)

# Example usage
input_directory = "/../../video_tools/output/apple_audio/"
output_directory = "/../../video_tools/output/apple_audio/converted_mp3/"

convert_all_m4a(input_directory, output_directory)
