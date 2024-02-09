from moviepy.editor import VideoFileClip, concatenate_videoclips

def clip_video(source_path, timestamps, output_path):
    """
    Clips a video based on given timestamps and outputs the result.

    :param source_path: Path to the source .mov file.
    :param timestamps: A list of tuples, each containing start and end times (in seconds or "min:sec").
    :param output_path: Path to save the clipped output video.
    """
    # Load the source video
    video = VideoFileClip(source_path)
    
    # Convert timestamps from "min:sec" to seconds if necessary
    def parse_time(t):
        if isinstance(t, str):
            min, sec = map(int, t.split(':'))
            return min * 60 + sec
        return t
    
    # Create clips for each timestamp and add them to a list
    clips = []
    for start, end in timestamps:
        start_sec = parse_time(start)
        end_sec = parse_time(end)
        clip = video.subclip(start_sec, end_sec)
        clips.append(clip)
    
    # Concatenate clips
    final_clip = concatenate_videoclips(clips)
    
    # Write the result to the output file, maintaining the format
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Example usage
source_video_path = 'video/original/input.mov'
output_video_path = 'video/shortened/output.mov'
timestamps = [
 ('00:04', '02:00'),
 ('02:04', '02:11'),
 ('02:13', '02:34'),
 ('02:50', '02:54'),
 ('03:12', '03:38'),
 ('03:41', '04:03'),
 ('04:31', '04:43'),
 ('05:09', '05:18'),
 ('05:23', '05:43'),
 ('06:36', '06:52'),
 ('08:20', '08:24'),
 ('08:44', '09:10'),
 ('09:45', '10:28'),
 ('10:36', '10:55')
]

clip_video(source_video_path, timestamps, output_video_path)
