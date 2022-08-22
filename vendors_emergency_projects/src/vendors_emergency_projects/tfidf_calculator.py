# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import gensim
import config

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

import emergency_checker


def _sort(tfidf_tuples):
    # This sorts based on the second value in our tuple, the tf-idf score
    tfidf_tuples.sort(key=lambda x: x[1], reverse=True)
    return tfidf_tuples

def calc_2(raw_df):
    dataset = [d.split() for d in raw_df[config.CLEAN_TITLE]]
    # dictionary = gensim.corpora.Dictionary(dataset)    # get the transformer params
    #
    # tfidf_params = dict(sublinear_tf=True,
    #                     min_df=5,
    #                     norm='l2',
    #                     ngram_range=(1, 2),
    #                     stop_words='english')
    #
    # features = TfidfVectorizer(**tfidf_params)
    # tfidf_weighted = features.fit_transform(raw_df[config.CLEAN_TITLE])
    # noam = "noam"
    #
    # def emergency_analyser():
    #     # magic is a function that extracts hostname from URL, among other things
    #     return lambda doc: emergency_checker._is_emeregency(doc)

    vect = CountVectorizer(token_pattern='\S+')
    emergency_analyzer = emergency_checker()
    vect.build_analyzer = emergency_analyzer
    tfidf_weighted = vect.fit_transform(raw_df[config.CLEAN_TITLE])
    noam = "noam"
    #####

    # our pipeline is changed to accept model
    # clf = Pipeline(steps=[
    #     ('features', TfidfVectorizer(**tfidf_params))
    #     # ,('model', model) #just model not model() as we have done that in models list
    # ])
    #
    # clf.fit(X_train,y_train)
    #  score = clf.score(X_test,y_test)
    #
    # model_name = clf.named_steps['model'].__class__.__name__ # hack to get name
    #
    # model_params = clf.named_steps['model']. get_params()

def calc(raw_df):
    dataset = [d.split() for d in raw_df[config.CLEAN_TITLE]]
    dictionary = gensim.corpora.Dictionary(dataset)

    # create a bag of words corpus
    bow_corpus = []
    for text in raw_df[config.CLEAN_TITLE]:
        bow_corpus.append(dictionary.doc2bow(text.split()))

    # create gensim TF-IDF model
    model = gensim.models.TfidfModel(bow_corpus)
    # create TF-IDF scores for the ``bow_corpus`` using our model
    corpus_tfidf = model[bow_corpus]

    # sort the tokens with their scores
    raw_df[config.TFIDF_SCORE] = -1
    raw_df[config.TFIDF_TITLE] = ''

    # for index, row in raw_df.iterrows():
    #     print(str(index))
    #     raw_df[config.TFIDF_SCORE][index] = _sort(corpus_tfidf[index])

    # For each document, get the most significant/unique words, and TF/IDF score
    doc_i = 0
    for n, doc in enumerate(corpus_tfidf):
        while doc_i not in raw_df.index:
            doc_i +=1

        if len(doc) < 1:
            doc_i += 1
            continue

        words = []
        words_max_str = ''
        for score_in_doc in doc:
            count_words = 0
            i = score_in_doc[0]
            words.append(dictionary.get(i))
            # if not words_max_str:
                # words_max_str = dictionary.get(i)
            # else:
                # words_max_str = words_max_str + ' ' + dictionary.get(i)
            count_words += 1

        # raw_df[config.TFIDF_TITLE][doc_i] = words_max_str
        raw_df[config.TFIDF_TITLE][doc_i] = words
        doc_i += 1

    return raw_df