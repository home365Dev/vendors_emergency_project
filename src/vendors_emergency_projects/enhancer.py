import src.vendors_emergency_projects.config as config
import pandas as pd
import tfidf_calculator
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

## get first 50 chars
## use only nouns in case we should cut the words - TBD

def _get_significant_words_using_tfidf(raw_df):
    return tfidf_calculator.calc(raw_df)
    # return tfidf_calculator.calc_2(raw_df)

def _cut_string_to_max_chars(text):
    cut_text = (text[:config.MAX_CHARS]) if len(text) > config.MAX_CHARS else text
    return cut_text

def _lemmatize(sentence):
    # Init the Wordnet Lemmatizer
    lemmatizer = WordNetLemmatizer()
    word_list = nltk.word_tokenize(sentence)
    # Lemmatize list of words
    # lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
    # return lemmatized_output

    # Lemmatize list of words
    try:
        lemmas_list = ([lemmatizer.lemmatize(w) for w in word_list])
    except:
        lemmas_list = word_list
    return lemmas_list


def enhance(raw_df):
    # preprocess using TF/IDF (over the entire data)
    raw_df = _get_significant_words_using_tfidf(raw_df)

    # ## cut the text by MAX_CHARS
    # raw_df[config.FIXED_TITLE] = raw_df[config.TFIDF_TITLE].apply(lambda str: _cut_string_to_max_chars(str))
    return raw_df


if __name__ == '__main__':
    raw_df = pd.DataFrame()
    text = "Nick likes to play football, however he is not too fond of tennis."
    df1 = {config.CLEAN_TITLE: text}
    raw_df = raw_df.append(df1, ignore_index=True)
    fixed_raw_df = enhance(raw_df)
    noam = "noam"