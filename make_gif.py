import subprocess

def convert_video_to_high_quality_gif(input_video_path, output_gif_path, palette_path="palette.png"):
    """
    Converts a video file to a high-quality GIF using FFmpeg, with a custom palette.

    :param input_video_path: Path to the source video file.
    :param output_gif_path: Path where the GIF file will be saved.
    :param palette_path: Temporary path for the palette image. Defaults to "palette.png".
    """
    try:
        # Generate a palette
        palette_cmd = [
            'ffmpeg',
            '-i', input_video_path,
            '-vf', 'fps=10,scale=320:-1:flags=lanczos,palettegen',
            palette_path
        ]
        subprocess.run(palette_cmd, check=True)
        
        # Use the palette to create the GIF
        gif_cmd = [
            'ffmpeg',
            '-i', input_video_path,
            '-i', palette_path,
            '-filter_complex', 'fps=10,scale=1080:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5',
            '-y',  # Overwrite output files without asking
            output_gif_path
        ]
        subprocess.run(gif_cmd, check=True)
        
        print(f"Video converted to high-quality GIF. Output saved to {output_gif_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    finally:
        # Optionally, remove the palette file
        try:
            subprocess.run(['rm', palette_path], check=True)
        except subprocess.CalledProcessError:
            print(f"Error removing the palette file {palette_path}")

# Example usage
input_video_path = 'video/shortened/input.mov'
output_gif_path = 'video/gif/ouput.gif'

convert_video_to_high_quality_gif(input_video_path, output_gif_path)
