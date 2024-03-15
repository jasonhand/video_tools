import subprocess
import re
import os

def auto_crop_video(input_file, output_file):
    """
    Automatically crops black bars from the video.
    """
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file does not exist - {input_file}")
        return

    detect_crop_cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'cropdetect',
        '-f', 'null',
        '-'
    ]

    try:
        # Capture both stdout and stderr for detailed debugging
        result = subprocess.run(detect_crop_cmd, text=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True)
        cropdetect_output = result.stderr  # cropdetect info is usually output to stderr

        # Find the crop parameter in the output
        crop_params = re.search(r'crop=(\d+:\d+:\d+:\d+)', cropdetect_output).group(1)
        print(f"Detected crop parameters: {crop_params}")
    except subprocess.CalledProcessError as e:
        print(f"Error during crop detection. FFmpeg output:\n{e.stderr}")
        return
    except AttributeError:
        print("Could not detect crop parameters.")
        return

    crop_cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f'crop={crop_params}',
        output_file
    ]

    try:
        subprocess.run(crop_cmd, check=True)
        print(f"Cropped video saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video cropping. FFmpeg output:\n{e.stderr}")

if __name__ == "__main__":
    # Make sure to update these paths according to your actual file locations
    input_video_path = '../../video/original/slides.mp4'
    output_video_path = '../../video_tools/video/original/final.mp4'
    auto_crop_video(input_video_path, output_video_path)
