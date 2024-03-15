import whisper
import os

def seconds_to_hms(seconds):
    """
    Converts seconds to a HH:MM:SS,MMM format for SRT files.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds, milliseconds = divmod(seconds % 60, 1)
    seconds = int(seconds)  # Ensure seconds is an integer before formatting
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{int(milliseconds * 1000):03d}"

def transcribe_audio_to_srt(audio_path):
    """
    Transcribes the audio file using OpenAI's Whisper model and outputs an SRT file format.
    """
    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing audio. This may take a while depending on the audio length...")
    result = model.transcribe(audio_path)

    srt_content = ""
    if "segments" in result:
        for i, segment in enumerate(result["segments"], start=1):
            start_hms = seconds_to_hms(segment["start"])
            end_hms = seconds_to_hms(segment["end"])
            text = segment["text"].replace("\n", " ")
            srt_content += f"{i}\n{start_hms} --> {end_hms}\n{text}\n\n"
    else:
        print("No segments found in transcription result.")

    return srt_content

if __name__ == "__main__":
    audio_path = "../../video/mp3/audio-to-transcript.mp3"  # Update this path
    srt_path = "../../services/transcribe/transcripts/transcription.srt" 
    
    transcription_srt = transcribe_audio_to_srt(audio_path)
    print("Transcription Completed with Timestamps:")
    
    os.makedirs(os.path.dirname(srt_path), exist_ok=True)
    with open(srt_path, "w", encoding="utf-8") as srt_file:
        srt_file.write(transcription_srt)
    print(f"SRT file saved to {srt_path}")
