import subprocess
import json
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_scenes(video_path, min_scene_duration=10):
    """
    Detects scene changes in a video file using ffprobe and groups them based on a minimum duration.

    Parameters:
    - video_path (str): Path to the source video file.
    - min_scene_duration (int): Minimum duration of a scene in seconds.
    """
    logging.info(f"Starting scene detection for video: {video_path}")

    # Use ffprobe to extract frame timestamps
    command = [
        'ffprobe',
        '-v', 'error',  # Only include error messages in the output
        '-select_streams', 'v',  # Select video stream
        '-show_entries', 'frame=pkt_pts_time',  # Show packet presentation timestamps
        '-of', 'json',  # Output format as JSON
        video_path,
    ]

    try:
        # Execute the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        frames = json.loads(result.stdout)['frames']
        timestamps = [float(frame['pkt_pts_time']) for frame in frames if 'pkt_pts_time' in frame]
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during frame extraction: {e}")
        return

    # Group frames into scenes based on the minimum duration
    scenes = []
    start_time = timestamps[0]
    for i in range(1, len(timestamps)):
        if timestamps[i] - start_time >= min_scene_duration:
            scenes.append((start_time, timestamps[i]))
            start_time = timestamps[i]

    # Log detected scenes
    logging.info(f"Detected {len(scenes)} scenes based on minimum duration of {min_scene_duration}s:")
    for i, (start, end) in enumerate(scenes, 1):
        logging.info(f"Scene {i}: Start={start}, End={end}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python script.py <video_path>")
        sys.exit(1)

    video_file_path = sys.argv[1]
    detect_scenes(video_file_path)
