# Using the tools to generate a summary of a video presentation

1. Extract audio from a video file using the [Mp3 - Video to MP3 Conversion Utility](services/mp3/mp3_README.md) script.
2. Use the [Transcribe TXT - Generates (TXT) Transcription from Mp3](services/transcribe/transcribeTXT_README.md) script to generate a transcription of the audio.
3. Chunk the audio into smaller sizes to fit the submission size restrictions for ChatGPT using the [Chunk](services/chunk/chunk_README.md) script.
4. Submit to ChatGPT4 in sections and request a summary of the transcript including key topics, takeaways, and interesting quotes.

## Scripts used

1. **🎵 [Mp3 - Video to MP3 Conversion Utility](services/mp3/mp3_README.md)**: Extracts audio from video files and saves it as high-quality MP3 files, useful for isolating audio tracks or creating transcripts.

2. **📝 [Transcribe TXT - Generates (TXT) Transcription from Mp3](services/transcribe/transcribeTXT_README.md)**: Transcribes audio into written text with timestamps using OpenAI's Whisper model, ideal for generating accurate subtitles.

3. **📄 [Chunk](services/chunk/chunk_README.md)**: chunks a large text file into smaller sections, each with a specified maximum number of tokens, and saves the output as a new text file.