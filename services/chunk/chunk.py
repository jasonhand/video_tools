import os

def chunk_text_file(input_file_path, output_file_path, max_tokens=4000):
    """
    Splits a large text file into smaller chunks, each with a maximum number of tokens.
    
    :param input_file_path: Path to the input text file.
    :param output_file_path: Path where the chunked text file will be saved.
    :param max_tokens: Maximum number of tokens per chunk (default is 4000).
    """
    # Read the content of the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.split()
    chunks = []
    current_chunk = []

    # Split words into chunks
    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) > max_tokens:
            chunks.append(' '.join(current_chunk[:-1]))
            current_chunk = [word]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    # Write chunks to the output file with numbered sections
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for i, chunk in enumerate(chunks, start=1):
            file.write(f"Section {i}\n{'='*20}\n{chunk}\n\n{'#'*50}\n\n")

    print(f"Chunked text has been saved to {output_file_path}")

if __name__ == "__main__":
    input_file_path = "/Users/jason.hand/Dev/video_tools/output/transcriptions/audio-to-transcript.txt"
    output_file_path = os.path.join(os.path.dirname(input_file_path), "Video_transcription_chunked.txt")

    chunk_text_file(input_file_path, output_file_path)
