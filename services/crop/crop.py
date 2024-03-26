import os
import subprocess

def get_video_dimensions(filename):
    """Get the dimensions of the video."""
    cmd = [
        'ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height', '-of', 'csv=s=x:p=0', filename
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    dimensions = result.stdout.strip().split('x')
    return int(dimensions[0]), int(dimensions[1])

def crop_video_to_portrait(source_file, target_file):
    """Crop the video to a portrait orientation focusing on the center."""
    width, height = get_video_dimensions(source_file)
    if width > height:
        # Landscape, need to crop
        crop_width = height * 9 // 16  # Calculate new width for a 9:16 aspect ratio
        crop_height = height
        x_offset = (width - crop_width) // 2
        y_offset = 0
    else:
        # Portrait or square, no crop needed
        crop_width = width
        crop_height = width * 16 // 9
        x_offset = 0
        y_offset = (height - crop_height) // 2 if height > crop_height else 0

    ffmpeg_cmd = [
        'ffmpeg', '-i', source_file,
        '-vf', f'crop={crop_width}:{crop_height}:{x_offset}:{y_offset}',
        '-c:a', 'copy', target_file
    ]
    subprocess.run(ffmpeg_cmd)

def main():
    input_dir = '../../output/crop'  # Directory containing input videos
    output_dir = '../../output/crop/cropped'  # Directory for cropped videos
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each video in the input directory
    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
            continue  # Skip non-video files
        source_file = os.path.join(input_dir, filename)
        target_file = os.path.join(output_dir, f"cropped_{filename}")
        crop_video_to_portrait(source_file, target_file)
        print(f"Processed {filename}")

if __name__ == "__main__":
    main()
