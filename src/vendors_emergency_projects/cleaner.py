# # from obj import Constants
# import pandas as pd
# import re
# import src.vendors_emergency_projects.config as config
# import spacy
# from gensim.parsing.preprocessing import remove_stopwords
#
# nlp = spacy.load("en_core_web_sm")
#
# text_title = config.TEXT
# text_clean = config.TEXT_CLEAN
#
# ## remove stopwords using preprocessing package
# def _remove_stop_words(text):
#     new_str_cln = remove_stopwords(text)
#     return new_str_cln
#
# ## remove special and non unicode chars
# def _remove_special_chars(raw_text_title):
#     non_unicode_pattern = re.compile(r'[^a-zA-Z\-ֿ\s\.\,\(\)\[\]]')
#     new_str_cln = re.sub(non_unicode_pattern, '', raw_text_title)
#     return new_str_cln
#
# def _convert_to_lemma(text):
#     doc = nlp(text)
#     text = ' '.join([token.lemma_ for token in doc])  # convert word to its original form
#     return text.lower()
#
# def _preprocess_over_text(text_title):
#     fixed_text = _do_pattern_replace(text_title)
#     fixed_text = _remove_special_chars(fixed_text)
#     fixed_text = _remove_stop_words(fixed_text)
#     fixed_text = _convert_to_lemma(fixed_text)
#     return fixed_text
#
# def _do_pattern_replace(line):
#     for (src,dst) in [
#         (' A C ', ' AC '),
#         (' A C.', ' AC.'),
#         (' A c.', ' AC.'),
#         (' a C.', ' AC.'),
#         (' a c.', ' AC.'),
#         (' A C,', ' AC,'),
#         (' A C ', ' AC '),
#         (' A c ', ' AC '),
#         (' a c ', ' AC '),
#         (' a C ', ' AC '),
#         (' i C ', ' AC '),
#         (' I C ', ' AC '),
#         (' i c ', ' AC '),
#         (' I c ', ' AC '),
#         ('A C ', 'AC '),
#         ('A c ', 'AC '),
#         ('a C ', 'AC '),
#         ('a. c.', ' AC '),
#         (' arc ', ' AC '),
#         ('hair conditioner','AC '),
#         ('air conditioned', 'AC '),
#         ('air conditioning', 'AC '),
#         ('air condition', 'AC '),
#         ('age back', 'HVAC'),
#         (' H back ', ' HVAC '),
#         (' H vac ' , ' HVAC '),
#         (' h vac ', ' HVAC '),
#         (' H Vac ', ' HVAC '),
#         (' H factories ', ' HVAC '),
#         ('age fax', 'HVAC'),
#         ('age fact', 'HVAC'),
#         ('Peter', 'heater'),
#         ('peter', 'heater'),
#         ('white down', 'wipe down'),
#         ('white dome', 'wipe down'),
#         ('wipe done', 'wipedown'),
#         ('bacon','vacant'),
#         ('ridge aerator', 'refrigerator'),
#         ('pull filters', 'pool filters'),
#         ('pull pump', 'pool pump'),
#         ('rash door', 'garage door'),
#         ('courage','garage'),
#         ('loan', 'lawn'),
#         ('home 365', ''),
#         ('home', ''),
#         ('behalf', ''),
#         ('make', ''),
#         ('tenant', ''),
#         ('video', ''),
#         ('fix', ''),
#         ('work', ''),
#         ('send',''),
#         ('somebody', ''),
#         ('Roche', 'roach'),
#         ("Roche's", 'roaches')
#     ]:
#         line = line.replace(src, dst)
#
#     return line
#
#
# def preprocess(raw_df):
#     # preprocess per string
#     raw_df[text_clean] = raw_df[text_title].apply(lambda str: _preprocess_over_text(str))
#
#     return raw_df
#
#
# if __name__ == '__main__':
#     raw_df = pd.DataFrame()
#     text = "Nick likes to play football, however he is not too fond of tennis."
#     df1 = {config.TEXT_TITLE: text}
#     raw_df = raw_df.append(df1, ignore_index=True)
#     preprocess(raw_df)
#     print(raw_df[config.TEXT])
#
#
