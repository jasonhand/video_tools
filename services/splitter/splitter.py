from moviepy.editor import VideoFileClip
import random
import os

def generate_random_clips(input_file, num_clips=3, min_duration=30, max_duration=59, output_dir='video/original/clips'):
    """
    Generates random clips from a given input video file.

    Parameters:
    - input_file (str): Path to the input video file.
    - num_clips (int): Number of random clips to generate.
    - min_duration (int): Minimum duration of each clip in seconds.
    - max_duration (int): Maximum duration of each clip in seconds.
    - output_dir (str): Directory where the output clips will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load the source video
    video = VideoFileClip(input_file)
    video_duration = video.duration

    for i in range(num_clips):
        # Generate a random start and end time for the clip
        start_time = random.uniform(0, video_duration - max_duration)
        clip_duration = random.uniform(min_duration, max_duration)
        end_time = start_time + clip_duration
        if end_time > video_duration:
            end_time = video_duration

        # Create the subclip
        clip = video.subclip(start_time, end_time)

        # Define the output filename
        output_file = os.path.join(output_dir, f"clip_{i+1}.mp4")

        # Write the subclip to a file
        clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        print(f"Generated clip {i+1}: {output_file}")

if __name__ == "__main__":
    input_video_path = "../../output/original/combined_video_portrait.mp4"  # Replace with your input video path
    output_directory = "../../output/original/split/"  # Replace with your desired output directory
    generate_random_clips(input_video_path, num_clips=5, output_dir=output_directory)  # Adjust num_clips and output_dir as desired
