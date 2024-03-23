from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) 

INPUT_FILE = os.path.abspath(os.getenv('FILE_PATH_INPUT_TEST') or '../tests/files/mock_input.txt')
OUTPUT_TXT = os.path.abspath(os.getenv('FILE_PATH_OUTPUT_TXT') or '../tests/files/mock_output.txt')
OUTPUT_JSON = os.path.abspath(os.getenv('FILE_PATH_OUTPUT_JSON') or '../tests/files/mock_output.json')
OUTPUT_UNMATCHED = os.path.abspath(os.getenv('FILE_PATH_OUTPUT_UNMATCHED') or '../tests/files/mock_unmatched.txt')

MAX_WORDS = 1
MAX_SYNONYMS = 5
PATTERN = r'"(.*?)"'
GENERATE_JSON = True
EXPORT_TYPE = 'txt'
