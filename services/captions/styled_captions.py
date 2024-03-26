import subprocess
import os

def burn_captions_into_video(video_path, srt_path, output_path, font_name="Arial", font_size=36, font_color="white", margin_vertical=55):
    """
    Burns captions from an SRT file into a video using FFmpeg, allowing customization of font, size, color, and position.

    Parameters:
    - video_path (str): Path to the source video file.
    - srt_path (str): Path to the SRT file containing the captions.
    - output_path (str): Path where the output video will be saved.
    - font_name (str): Name of the font for the captions.
    - font_size (int): Size of the font.
    - font_color (str): Color of the font.
    - margin_vertical (int): Vertical margin to position captions higher or lower on the screen.
    """
    # Define the style for subtitles, including font, size, and color
    subtitle_style = f"'FontName={font_name},FontSize={font_size},PrimaryColour=&H00{font_color},Alignment=2,MarginV={margin_vertical}'"

    # Command to burn captions with customized styling
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f"subtitles={srt_path}:force_style={subtitle_style}",
        '-codec:a', 'copy',  # Copy the audio without re-encoding
        output_path
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Captions successfully burned into video with customized style. Output saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video processing: {e}")

if __name__ == "__main__":
    video_file = "../../output/original/burned_logo_video.mp4"  # Update this path
    srt_file = "../../output/transcriptions/transcription.srt"  # Update this path
    output_video = "../../output/captionsfinal_with_captions.mp4"  # Update this path

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_video), exist_ok=True)
    
    # Example usage with customized font, size, color, and position
    burn_captions_into_video(video_file, srt_file, output_video, font_name="Arial", font_size=16, font_color="white", margin_vertical=45)
