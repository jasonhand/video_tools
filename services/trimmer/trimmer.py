import subprocess

def trim_video(input_video_path, output_video_path, trim_duration="1:00"):
    """
    Trims the input video to the specified duration using ffmpeg.

    Parameters:
    - input_video_path: Path to the input video file.
    - output_video_path: Path where the trimmed video will be saved.
    - trim_duration: Duration to trim the video to. Default is "2:00" (2 minutes).
    """
    # Construct the ffmpeg command to trim the video
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_video_path,  # Input video file
        "-t", trim_duration,     # Duration to trim the video to
        "-c", "copy",            # Copy the video and audio streams without re-encoding
        output_video_path       # Output video file
    ]

    # Execute the ffmpeg command
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Video trimmed successfully to {trim_duration} and saved to {output_video_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error trimming video: {e}")

# Example usage
input_video = "../../video/original/slides.mp4"
output_video = "../../video/original/trimmed-slides.mp4"
trim_video(input_video, output_video)
