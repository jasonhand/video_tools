# Video Tools
A collection of python scripts to make minor edits to video files.

1. **[2xSpeed - Video Speed Doubling Utility](services/2xSpeed/2xSpeed_README.md)** - This Python script utilizes FFmpeg to double the speed of a given video file. By adjusting the video's playback speed, it creates a new version that plays twice as fast as the original. This utility can be particularly useful for creating time-lapse effects or shortening videos without altering their content. - [View the code](services/2xSpeed/2xSpeed.py)
2. **[Black_bars - Black Bar Removal](services/black_bars/black_bars_README.md)** This Python script provides a utility for processing videos, specifically for resizing and cropping videos to a target resolution while optionally removing additional space from the top and bottom of the video frame. The script utilizes the `ffmpeg` command-line tool, making it a powerful option for video manipulation. - [View the code](services/black_bars/black_bars.py)
3. **[Clip - Video Trimming and Enhancement](services/clip/clip_README.md)** This Python script provides a convenient method for trimming the beginning of a video file and enhancing its quality using FFmpeg. It's designed to quickly remove unwanted starting portions of a video and improve its visual and auditory quality for further use or distribution. - [View the code](services/clip/clip.py)
4. **[Shorten - Video Clipping Utility](services/shorten/shorten_README.md)** This Python script offers an efficient way to create a new video from selected portions of an existing video. By specifying a series of start and end timestamps, users can extract and concatenate multiple segments from the source video, generating a seamlessly edited output video. This utility is particularly useful for creating highlight reels, compiling specific scenes, or summarizing content. - [View the code](services/shorten/shorten.py)
5. **[Splitter - Video Clip Processor](services/splitter/splitter_README.md)** This Python script automates the process of generating multiple video clips from a single input video file, incorporating a variety of transformations and overlaying a static image. It's designed for scenarios where you might want to create snippets or highlights from longer video content, with each clip featuring a consistent graphical overlay. - [View the code](services/splitter/splitter.py)
6. **[Stacked - Portrait Stacked](services/stacked/stacked_README.md)** This Python script enhances video presentations by combining 2 video sources (example: speaker footage and slide content) into a single, visually appealing portrait video. - [View the code](services/stacked/stacked.py)
7. **[Trimmer - Video Trimming Utility](services/trimmer/trimmer_README.m)** This Python script provides a straightforward utility for trimming video files to a specified duration using `ffmpeg`, a powerful multimedia framework capable of handling a wide array of video processing tasks. The script trims the beginning of a video to the desired length without re-encoding, preserving the original quality and ensuring efficient processing. - [View the code](services/trimmer/trimmer.py)
8. **[Upscale - Video Upscaling Utility](services/upscale/upscale_README.md)** This Python script provides a user-friendly method for upscaling video files to a higher resolution using FFmpeg, a powerful multimedia framework. It automatically handles the generation of output file names to reflect the new resolution and incorporates optimal settings for video and audio quality. - [View the code](services/upscale/upscale.py)
9. **[Make-gif - High-Quality GIF Conversion Utility](services/make_gif/make_gif.py)** This Python script offers a solution for converting video files into high-quality GIFs using FFmpeg, leveraging a custom color palette to enhance the output quality. The script generates a palette from the input video to ensure the GIF maintains visual fidelity, then uses this palette to create the final GIF. - [View the code](services/make_gif/make_gif.py)
10. **[Mp3 - Video to MP3 Conversion Utility](services/mp3/mp3_README.md)** This utility is a straightforward Python script designed to extract audio from any video file and save it as a high-quality MP3 file. This process is especially useful for creating audio transcripts from video content, listening to the audio of a video on devices without video playback capability, or for any scenario where you need to isolate the audio track from video files. - [View the code](services/mp3/create_mp3.py)
11. **[Burn Logo - Logo Overlay Utility](services/burn_logo/burn_logo_README.md)** This Python utility leverages FFmpeg to overlay an image onto a video file, allowing customization of the image's position and size within the video frame. It's an excellent tool for adding logos, watermarks, or any other static graphic elements to videos.
12. **[Captions - Burning Captions into Video](services/captions/captions_README.md)** Uses FFmpeg to burn subtitles from an SRT file directly into a video file. The subtitles are positioned higher than the lower third of the screen, making them more visually accessible and less likely to obscure important details in the video content.
13. **[Transcribe - Generates Transcription from Mp3](services/transcribe/transcribe_README.md)** This script leverages OpenAI's Whisper model to transcribe audio from a specified file into the SubRip Text (SRT) format. It's designed to convert spoken words into written text with timestamps, making it ideal for generating accurate subtitles for videos or audio files.