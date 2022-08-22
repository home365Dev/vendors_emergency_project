# from fuzzywuzzy import fuzz
# import config
# import re
#
# ## find the matching score using fuzzywuzzy
# def _find_matching_score(source_text, result_text):
#     ratio = fuzz.partial_ratio(source_text, result_text)
#     return ratio
#
# ## check for the best match between the results
# def _find_best_match(source_text, result_text_lst):
#     best = (-1, -1)
#     for _, result_text in result_text_lst.items():
#         score = _find_matching_score(source_text, result_text)
#         if score > best[1]:
#             best = (result_text, score)
#
#     # check matching threshold
#     if best[1] < amazon_vars.MATCH_SCORE_THRESHOLD:
#         return None
#
#     return best
#
# def run(result_df):
#     result_df[config.BEST_MATCH] = result_df.apply(lambda x: _find_best_match(x[config.FIXED_TITLE], x[config.ALIBABA_RESULT]), axis=1)
#     return result_df
#
# if __name__ == '__main__':
#     ratio = _find_matching_score("Catherine M. Gitau", "Catherine Gitau")
#     print(ratio)
