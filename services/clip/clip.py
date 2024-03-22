import subprocess

def trim_and_enhance_video(input_file, output_file, trim_start=6):
    """
    Trims the first 4 seconds off the given video file and enhances its quality using FFmpeg.

    Parameters:
    input_file (str): Path to the input video file.
    output_file (str): Path to save the enhanced video file.
    trim_start (int, optional): Number of seconds to trim from the start. Default is 4.
    """
    try:
        command = [
            '/opt/homebrew/bin/ffmpeg',  # Replace with the actual path to ffmpeg
            '-i', input_file,
            '-ss', str(trim_start),
            '-c:v', 'libx264',     # Use H.264 video codec
            '-b:v', '6000k',       # Higher video bitrate
            '-c:a', 'aac',         # Use AAC audio codec
            '-b:a', '320k',        # Higher audio bitrate
            output_file
        ]
        subprocess.run(command, check=True)
        print(f"Video trimmed and enhanced successfully. Output file: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
input_video = '../../output/original/S63168.mp4'  # Replace with your video file path
output_video = '../../output/clipped/S63168-clipped.mp4'  # Replace with your desired output path

trim_and_enhance_video(input_video, output_video)
