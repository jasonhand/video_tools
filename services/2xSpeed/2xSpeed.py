import subprocess

def double_speed(input_video_path, output_video_path):
    """
    Doubles the speed of the video at input_video_path and saves the result to output_video_path.

    :param input_video_path: Path to the source video file.
    :param output_video_path: Path where the sped-up video will be saved.
    """
    try:
        # Command to double the video speed
        command = [
            'ffmpeg', 
            '-i', input_video_path, 
            '-filter:v', 'setpts=0.5*PTS', 
            '-an',  # Removes audio, since speeding up video desynchronizes it
            output_video_path
        ]
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Video speed doubled successfully. Output saved to {output_video_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video processing: {e}")

# Example usage
input_video_path = '../../output/shortened/input.mov'
output_video_path = '../../output/2xSpeed/output.mov'

double_speed(input_video_path, output_video_path)
