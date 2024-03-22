import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk import pos_tag

# Ensure necessary NLTK data is downloaded
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

def read_file(file_path):
    """Reads the entire content of a text file and returns it."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()

def get_interesting_words(text, num_keywords=20):
    """Identifies and returns the most common 'interesting' words in the text."""
    stop_words = set(stopwords.words('english'))
    additional_uninteresting_words = {'right', 'going', 'like', 'one', 'talk', 'think', 'want', 'lot', 'information', 'see', 'go', 'know', 'thing', 'say', 'foundation', 'things', 'get', 'kind', 'time', 'use', 'checklist', 'using', 'look', 'let', 'take', 'okay', 'way', 'run', 'happening', 'today', 'something', 'need', 'talking', 'part', 'got', 'work', 'version', 'show', 'day', 'bit', 'make', 'questions', 'generation', 'tell', 'dependencies', 'process', 'yeah', 'box', 'cve', 'teaming', 'environment', 'applications', 'deal', 'type', 'put', 'expert', 'hand', 'everything', 'said', 'team', 'set', 'tools', 'item', 'working', 'people', 'sort', 'slide', 'kinds', 'remember', 'years', 'question', 'case', 'point', 'try', 'approach', 'interesting', 'system', 'terms', 'building', 'area', 'management', 'coming', 'build', 'components', 'control', 'find', 'generator', 'access', 'end', 'tool', 'ability', 'power', 'provide', 'level', 'combination', 'ways', 'starting', 'start', 'track', 'example', 'application', 'body', 'sequence', 'built', 'capabilities', 'request', 'changing', 'production', 'output', 'thinking', 'emo', 'help', 'leverage', 'used', 'world', 'released', 'cases', 'courses', 'release', 'source', 'goal', 'share', 'come', 'course', 'develop', 'project', 'objects', 'segment', 'means', 'including', 'helps', 'thank', 'seen', 'mentioned', 'object', 'anything', 'mentioned', 'side', 'product', 'company', 'tasks', 'task', 'progress', 'actions', 'field', 'number', 'action', 'introduced', 'service', 'trying', 'code', 'button', 'value', 'understand', 'couple', 'solve', 'click', 'planning', 'problem', 'technologies', 'websites', 'element', 'broom', 'knowledge', 'sense', 'call', 'arena', 'play', 'thousands', 'millions', 'called', 'skills', 'users', 'order', 'instance', 'change', 'techniques', 'allows', 'user', 'values', 'systems', 'idea', 'steps'}  # Add more as needed
    all_uninteresting_words = stop_words.union(additional_uninteresting_words)
    
    words = word_tokenize(text)
    # Filter out stop words and non-alphabetic words
    filtered_words = [word for word in words if word.isalpha() and word not in all_uninteresting_words]
    
    # Tag parts of speech
    tagged_words = pos_tag(filtered_words)
    
    # Filter based on parts of speech, e.g., NN for noun, singular; VB for verb, base form
    interesting_words = [word for word, tag in tagged_words if tag.startswith('NN') or tag.startswith('VB')]
    
    # Count and return the most common interesting words
    freq_dist = FreqDist(interesting_words)
    return freq_dist.most_common(num_keywords)

if __name__ == "__main__":
    file_path = '/Users/jason.hand/Dev/video_tools/output/transcriptions/Session10.txt'  # Update this path
    text = read_file(file_path)

    # Get interesting words
    interesting_words = get_interesting_words(text)
    print("Interesting words and their counts:")
    for word, count in interesting_words:
        print(f"{word}: {count}")
