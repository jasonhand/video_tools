import whisper
import os

def transcribe_audio_to_text(audio_path, output_directory):
    """
    Transcribes the audio file using OpenAI's Whisper model and outputs a plain text file.
    """
    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing audio. This may take a while depending on the audio length...")
    print("--------------------------------------------------------------------------")
    result = model.transcribe(audio_path)

    # Prepare output file path
    base_name = os.path.basename(audio_path).replace('.mp3', '.txt')
    output_path = os.path.join(output_directory, base_name)

    # Write transcription to a text file
    if "text" in result:
        with open(output_path, "w", encoding="utf-8") as text_file:
            text_file.write(result["text"])
        print(f"Transcription saved to {output_path}")
    else:
        print("No transcription result found.")

if __name__ == "__main__":
    audio_path = "/Users/jason.hand/Dev/video_tools/output/mp3/audio-to-transcript.mp3"
    output_directory = "../../output/transcriptions"
    os.makedirs(output_directory, exist_ok=True)
    transcribe_audio_to_text(audio_path, output_directory)
