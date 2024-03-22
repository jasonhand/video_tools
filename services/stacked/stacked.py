import subprocess
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip

def resize_video_with_ffmpeg(input_path, output_path, target_width):
    command = [
        'ffmpeg', '-i', input_path,
        '-vf', f'scale={target_width}:-2',  # ensures height is divisible by 2
        '-c:a', 'copy',  # copy audio stream
        output_path
    ]
    subprocess.run(command, check=True)

# Desired width and compute height for the background color clip
desired_width = 1080
desired_height = 1920
background_color = (99, 44, 166)  # Datadog Purple

# Use ffmpeg to resize videos
resize_video_with_ffmpeg('../../output/original/speakers.mp4', '../../output/original/resized_speakers.mp4', desired_width)
resize_video_with_ffmpeg('../../output/original/no-black-bars-slides.mp4', '../../output/original/resized-no-black-bars-slides.mp4', desired_width)

# Load the resized video files
speakers_video_resized = VideoFileClip("../../output/original/resized_speakers.mp4")
slides_video_resized = VideoFileClip("../../output/original/resized-no-black-bars-slides.mp4").without_audio()

# Calculate the combined height of the speaker and slide videos to adjust their positions
combined_video_height = speakers_video_resized.size[1] + slides_video_resized.size[1]

# Calculate the vertical position for the speakers video to move it upwards
# It should be positioned at the top of the background clip
speakers_position_y = 0

# Calculate the vertical position for the slides video, directly below the speakers video
slides_position_y = speakers_video_resized.size[1]

# Create a color clip for the background
background_clip = ColorClip(size=(desired_width, desired_height), color=background_color, duration=max(speakers_video_resized.duration, slides_video_resized.duration))

# Create a composite video clip
final_clip = CompositeVideoClip([
    background_clip.set_position(('center', 'center')),
    speakers_video_resized.set_position(('center', speakers_position_y)),
    slides_video_resized.set_position(('center', slides_position_y))
], size=(desired_width, desired_height))

# Set the audio from the speakers video
final_clip = final_clip.set_audio(speakers_video_resized.audio)

# Output file path and write the file
output_file = "../../output/original/combined_video_portrait.mp4"
final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=24)
