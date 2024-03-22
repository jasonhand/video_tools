# Text File Chunker

This Python script efficiently chunks a large text file into smaller sections, each with a specified maximum number of tokens, and saves the output as a new text file. This functionality is particularly useful for processing large documents that need to be broken down into manageable parts, such as for detailed analysis, easier reading, or to comply with token limits of certain APIs or applications.

## Features

- **Customizable Token Limits:** Define the maximum number of tokens per chunk to suit your specific needs.
- **Numbered Sections:** Each chunk is clearly numbered for easy navigation and reference.
- **Wide Applicability:** Useful for a variety of purposes, including text analysis, processing large documents for machine learning models, or preparing data for APIs with token limitations.

## Prerequisites

- **Python:** Ensure that Python is installed on your system. This script is compatible with Python 3.x.

## Installation

No additional installation is required. Simply ensure that Python is installed on your system.

## Usage

1. Place the text file you wish to chunk in a known directory.
2. Update the `input_file_path` and `output_file_path` variables in the script to point to your input text file and the desired output location, respectively.
3. Run the script using Python:

```bash
python text_file_chunker.py
```

### Parameters

- `input_file_path`: The file path of the text file you wish to chunk.
- `output_file_path`: The file path where the chunked text file will be saved.
- `max_tokens`: Optional. The maximum number of tokens per chunk. Default is set to 4000 tokens.

## Example

```python
input_file_path = "/path/to/your/large_text_file.txt"
output_file_path = "/path/to/your/output_directory/large_text_file_chunked.txt"
max_tokens = 4000

chunk_text_file(input_file_path, output_file_path, max_tokens)
```

## Notes

- The script considers spaces as token separators. Adjust `max_tokens` based on your specific requirements and the average word length in your text.
- The output file will contain sections separated by headers with section numbers and divider lines for clarity and easy navigation.

## Contributing

Your contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License

This script is released under an open-source license. Feel free to use, modify, and distribute it as needed. Please include a reference or credit if you use this script in your project.