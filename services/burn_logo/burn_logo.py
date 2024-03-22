import subprocess

def burn_image_into_video(video_path, image_path, output_path, position="50:50", image_size="100x100"):
    """
    Burns an image into a video at a specified position and size using FFmpeg.

    Parameters:
    - video_path (str): Path to the source video file.
    - image_path (str): Path to the image file to overlay on the video.
    - output_path (str): Path where the output video will be saved.
    - position (str): The position for the image overlay specified as "x:y".
                      Default is "10:10" (10 pixels from the left and 10 pixels from the top).
    - image_size (str): The size for the image overlay specified as "widthxheight".
                        Default is "100x100".
    """
    command = [
        'ffmpeg',
        '-i', video_path,  # Input video file
        '-i', image_path,  # Input image file
        '-filter_complex', f"[1:v]scale={image_size}[img];[0:v][img]overlay={position}",  # Scale and overlay image
        '-codec:a', 'copy',  # Copy the audio codec of the original video
        output_path  # Output video file
    ]

    try:
        # Execute the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Image successfully burned into video. Output saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video processing: {e}")

if __name__ == "__main__":
    # Example usage - replace these paths with your actual file paths
    video_file = "../../video_tools/output/original/split/keep0.mp4"
    image_file = "../../video_tools/logos/datadog.png"
    output_video = "../../video_tools/output/original/burned_logo/burned_logo_video.mp4"
    image_position = "50:50"  # Position of the image
    image_size = "250x250"  # Desired size of the image

    burn_image_into_video(video_file, image_file, output_video, image_position, image_size)
