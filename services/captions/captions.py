import subprocess
import os

def burn_captions_into_video(video_path, srt_path, output_path):
    """
    Burns captions from an SRT file into a video using FFmpeg, positioning them higher than the lower third of the screen.

    Parameters:
    - video_path (str): Path to the source video file.
    - srt_path (str): Path to the SRT file containing the captions.
    - output_path (str): Path where the output video will be saved.
    """
    # Adjust MarginV to position captions higher on the screen
    margin_vertical = 80  # Adjust this value to move the captions higher

    # Command to burn captions with adjusted positioning
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f"subtitles={srt_path}:force_style='Alignment=2,Fontname=DejaVu Serif,BorderStyle=0,FontSize=12,Shadow=2,MarginV={margin_vertical}'",
        '-codec:a', 'copy',  # Copy the audio without re-encoding
        output_path
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Captions successfully burned into video. Output saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video processing: {e}")

if __name__ == "__main__":
    video_file = "../../output/burned_logo/burned_logo_video.mp4"  # Update this path
    srt_file = "../../output/transcriptions/transcription.srt"  # Update this path
    output_video = "../../output/captionsfinal_with_captions.mp4"  # Update this path

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_video), exist_ok=True)
    
    burn_captions_into_video(video_file, srt_file, output_video)
