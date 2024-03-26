import re

def clean_transcript_v2(input_file, output_file):
    # Regular expression to match timestamps and bracketed text
    timestamp_regex = re.compile(r'\[\w*\]|\d+:\d+|\:\d+\s')
    bracketed_text_regex = re.compile(r'\[.*?\]')
    # Additional regex to catch isolated timestamp-like patterns within text
    isolated_timestamp_regex = re.compile(r'\s*:\d+\s*')

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Remove timestamps, bracketed text, and isolated timestamp-like patterns
            clean_line = timestamp_regex.sub('', line)
            clean_line = bracketed_text_regex.sub('', clean_line)
            clean_line = isolated_timestamp_regex.sub('', clean_line)
            # Clean up multiple spaces and strip leading/trailing spaces
            clean_line = re.sub(' +', ' ', clean_line).strip()
            # Write the cleaned line to the output file if it's not just whitespace
            if clean_line:
                outfile.write(clean_line + '\n')

# Example usage
input_file_path = '/Users/jason.hand/Dev/video_tools/output/transcriptions/youtube_transcript_to_text.txt'
output_file_path = '/Users/jason.hand/Dev/video_tools/output/transcriptions/processed_youtube_transcript_to_text.txt'
clean_transcript_v2(input_file_path, output_file_path)
