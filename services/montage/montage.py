import os
import random
import subprocess

# Configuration Variables
input_dir = '/Users/jason.hand/Dev/video_tools/output/montage'  # Update this to the path of your input videos
output_dir = '/Users/jason.hand/Dev/video_tools/output/montage/output'  # Update this to your desired output directory
final_video_length = 30  # Length of the final video in seconds
output_filename = '/Users/jason.hand/Dev/video_tools/output/montage/output/final_output.mp4'  # Name of the final output video, simplified path

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

def get_video_length(filename):
    """Returns the length of the video in seconds."""
    cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
           '-show_entries', 'stream=duration', '-of', 'default=noprint_wrappers=1:nokey=1', filename]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0  # Return 0 if unable to get the video length

def clip_random_section(source_file, duration, index):
    """Clips a random section from the source file."""
    total_length = get_video_length(source_file)
    if total_length <= 0:
        return None  # Skip the file if the length is 0 or an error occurred

    start_time = random.uniform(0, max(0, total_length - duration))
    output_file_path = os.path.join(output_dir, f"temp_clip_{index}.mp4")

    cmd = [
        'ffmpeg', '-ss', str(start_time), '-i', source_file, '-t', str(duration),
        '-r', '30',
        '-vf', "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",  # Directly specify resolution without quotes
        '-c:v', 'libx264', '-preset', 'medium', '-crf', '23',
        '-c:a', 'aac', '-b:a', '192k',
        output_file_path
    ]

    subprocess.run(cmd, check=True)
    return output_file_path


def concatenate_clips(clip_paths, output_file):
    """Concatenates multiple video clips into a single video file."""
    with open(os.path.join(output_dir, 'inputs.txt'), 'w') as f:
        for clip_path in clip_paths:
            f.write(f"file '{clip_path}'\n")
    # Use the concat demuxer for better compatibility and avoiding re-encoding here
    cmd = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', os.path.join(output_dir, 'inputs.txt'),
           '-c:v', 'libx264', '-preset', 'fast', '-crf', '22',  # Maintaining video quality
           '-c:a', 'aac', '-b:a', '128k',  # Maintaining audio quality
           output_file]
    subprocess.run(cmd, check=True)

def main():
    video_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir)
                   if os.path.isfile(os.path.join(input_dir, f)) and f.lower().endswith(('.mp4', '.mov', '.avi', '.mkv'))]
    if not video_files:
        print("No video files found in the input directory.")
        return

    valid_clips = []
    clip_durations = final_video_length / max(len(video_files), 1)  # Avoid division by zero

    for i, video_file in enumerate(video_files):
        clip_path = clip_random_section(video_file, clip_durations, i)
        if clip_path:
            valid_clips.append(clip_path)
    
    if not valid_clips:
        print("No valid clips were generated.")
        return

    output_file_path = os.path.join(output_dir, output_filename)
    concatenate_clips(valid_clips, output_file_path)

    # Cleanup temporary clip files and inputs list
    for clip_path in valid_clips:
        os.remove(clip_path)
    os.remove(os.path.join(output_dir, 'inputs.txt'))

    print(f"Final video created at {output_file_path}")

if __name__ == "__main__":
    main()
