import subprocess

def video_to_mp3(input_video_path, output_audio_path):
    """
    Extracts the audio from a video file and saves it as an MP3 file.

    Parameters:
    - input_video_path (str): Path to the source video file.
    - output_audio_path (str): Path where the MP3 file will be saved.
    """
    try:
        # Construct and execute the FFmpeg command
        command = [
            'ffmpeg',
            '-i', input_video_path,  # Input video file
            '-q:a', '0',             # Use the best audio quality
            '-map', 'a',             # Map audio streams
            output_audio_path        # Output audio file
        ]
        subprocess.run(command, check=True)
        print(f"Audio extracted and saved to {output_audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during audio extraction: {e}")

if __name__ == "__main__":
    # Example usage
    input_video = "../../video/original/burned_logo_video.mp4"  # Update this path
    output_audio = "../../video/mp3/audio-to-transcript.mp3"  # Update this path
    video_to_mp3(input_video, output_audio)
