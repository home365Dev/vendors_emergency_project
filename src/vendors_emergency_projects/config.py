import logging
import os
IS_EMERGENCY = 'is_emergency'
INPUT_PATH = 'input/data.csv'
OUTPUT_PATH = 'output/output_data.csv'
TEXT = 'text'
TFIDF_TITLE = 'tfidf_value'
TFIDF_SCORE = 'tfidf_score'
FIXED_TITLE = 'fixed_value'
EMERGENCY = 'emergency'
FEATURES = 'features'
TRAIN_MODEL = True
TAGGED_DATA = 'Category'
# BEST_MATCH = 'best_match'
MAX_CHARS = 50
NUM_OF_RAWS = 500
MATCH_SCORE_THRESHOLD = 70

IS_TEST = os.environ.get("IS_TEST", "False").lower() == "true"

