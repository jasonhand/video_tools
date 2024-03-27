# Using the tools to generate a Trip Report

- Audio was recorded for each session. This was done on an iPhone. The output file was `.ma4`
- To transcribe the audio, it first needed to be converted from `.ma4` to `.mp3`. This was done with the first script below.
- Once the format was in `.mp3`, use the second script to transcribe the audio into a text file. Depending on the quality of the recording, some manual cleanup may be necessary.
- The goal now is to summarize the transcript. However, most transcriptions are very large and exceed the context window of popular tools such as ChatGPT. In order to provide the full transcript to ChatGPT, it first must be broken up into smaller "chunks". These can then be sent as individual prompts and summarized. Use the third python script to accomplish this followed by ChatGPT to summarize.
- If you are interested in identifying the keywords in the transcript, use the fourth python script. You may need to add additional words to the "dictionary" of words to ignore. It'll make sense when you look at the code.
- If you have video footage you want to combine into one brief "montage" for use in the trip report, you can use the fifth script to crop a horizontal video so it is formatted as a portrait (the final output). 
- The sixth script will clip random sections from multiple videos and combine them into 5 different videos you can choose from.
- 


## Written Content

1. 🎵 Apple Audio to MP3 Converter: converts M4A audio files to MP3 format using FFmpeg.

2. 📝 Transcribe TXT - Generates (TXT) Transcription from Mp3: Transcribes audio into written text with timestamps using OpenAI's Whisper model, ideal for generating accurate subtitles.

2. 🖼️ Burn Logo - Logo Overlay Utility: Adds logos or watermarks to videos by overlaying images, with customizable positioning and sizing.

3. 📄 Chunk: chunks a large text file into smaller sections, each with a specified maximum number of tokens, and saves the output as a new text file.

4. 🔍 Key Words: Analyze a text file, filtering out common "stop words" and additional uninteresting words to identify and count the most meaningful words.

## Media Content

5. Crop - Crop videos segments: automates the process of cropping videos to a portrait orientation, focusing on the center of the video.

6. Montage - Concactenate Multiple Videos: Create a video montage by clipping random sections from each video in a specified directory and merging them into a new video of a predetermined length.











