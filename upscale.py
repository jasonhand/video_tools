import subprocess
import os

def upscale_video(input_file, resolution='1920x1080'):
    """
    Upscale a video to the specified resolution using FFmpeg and automatically generate
    an output file name that includes the resolution and a hyphen before the input file's name.

    Args:
    - input_file: The path to the input video file.
    - resolution: The target resolution. Default is '1920x1080' for Ultra HD/4K.
                  Use '1920x1080' for Full HD resolution.
    """
    # Extract the base name of the input file
    base_name = os.path.basename(input_file)
    # Generate the output file path with resolution prefix
    output_file = os.path.join('video/upscaled', f"{resolution}-{base_name}")
    
    # Corrected logic to determine bitrate based on resolution
    bitrate = '8000k' if resolution == '1920x1080' else '8000k'
    
    # Frame rate
    framerate = '30'
    # Audio codec and bitrate
    audio_codec = 'aac'
    audio_bitrate = '192k'
    # Video codec
    video_codec = 'libx264'
    # Define the FFmpeg command for upscaling
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f'scale={resolution}:flags=lanczos',
        '-r', framerate,
        '-b:v', bitrate,
        '-c:v', video_codec,
        '-c:a', audio_codec,
        '-b:a', audio_bitrate,
        output_file
    ]
    
    try:
        # Execute the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Upscaling completed: '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Error during upscaling: {e}")

if __name__ == "__main__":
    # Example usage with a hardcoded input file and resolution
    input_file = 'video/original/input.mp4'  # Example input file
    resolution = '1920x1080'  # Change this variable to adjust resolution
    upscale_video(input_file, resolution)
