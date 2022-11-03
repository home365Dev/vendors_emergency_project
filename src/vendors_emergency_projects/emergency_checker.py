import pandas as pd
import src.vendors_emergency_projects.config as config
from src.vendors_emergency_projects.logger import logger
import src.vendors_emergency_projects.cleaner as cleaner
import src.vendors_emergency_projects.app as app

negative_terms = ['not', 'no', 'doesnt', 'nt']
two_words_term_1 = ['soon']
two_words_term_2 = ['possible']

emergency_terms = pd.read_csv('terms/emergency_terms.txt', header=None)
required_neg_special_terms = pd.read_csv('terms/required_neg_special_terms.txt', header=None)

## police is no good, since it is converted from the spoken word of "please"

def run(df:pd.DataFrame):
    ## clean the data
    logger.info("cleaner")
    df = cleaner.preprocess(df)
    df[config.IS_EMERGENCY] = "False"
    # df[config.EMERGENCY] = df[config.TFIDF_TITLE].apply(lambda str: _is_emeregency(str))
    df[config.EMERGENCY] = df[config.TEXT_CLEAN].apply(lambda str: _is_emeregency(str))
    df.loc[df[config.EMERGENCY] != "False", config.IS_EMERGENCY] = "True"
    return df

def _is_emeregency(lemmas):
    global emergency_terms
    global required_neg_special_terms
    global negative_terms
    logger.debug("running over: " + lemmas)

    lem_split = lemmas.split(' ')
    for index, row in emergency_terms.iterrows():
        term = row[0]
        if term in lem_split:
            if (lem_split.index(term) - 1 >=0 and lem_split[lem_split.index(term) - 1] not in negative_terms) and \
                    (lem_split.index(term) - 2 >=0 and lem_split[lem_split.index(term) - 2] not in negative_terms):
                logger.debug("result: " + term)
                return term

    for index, row in required_neg_special_terms.iterrows():
        term = row[0]
        if term in lem_split:
            if (lem_split.index(term) - 1 >=0 and lem_split[lem_split.index(term) - 1] in negative_terms) or \
                    (lem_split.index(term) - 2 >= 0 and lem_split[lem_split.index(term) - 2] in negative_terms) or \
                    (lem_split.index(term) - 3 >= 0 and lem_split[lem_split.index(term) - 3] in negative_terms):
                logger.debug("result: no " + term)
                return 'no '+term
            if (lem_split.index(term) + 1 < len(lem_split) and lem_split[lem_split.index(term) + 1] in negative_terms) or \
                    (lem_split.index(term) + 2 < len(lem_split) and lem_split[lem_split.index(term) + 2] in negative_terms):
                logger.debug("result: no " + term)
                return 'no '+term

    for term1 in two_words_term_1:
        if term1 in lem_split:
            if lem_split.index(term1) + 1 < len(lem_split) and lem_split[lem_split.index(term1)+ 1] in two_words_term_2:
                res = term1 + ' ' + lem_split[lem_split.index(term1) + 1]
                logger.debug("result: " + str(res))
                return res

    return "False"


if __name__ == '__main__':
    df = pd.DataFrame(columns=[config.TEXT])
    example_str = "all right , I m probably gon na regret order point , soon possible master bathroom , uh sort valve continually run water toilet bowl . I try I include go Home Depot try replacement um sort flush mechanism like I use . I figure constant run . so end water drain tank fill night long . its drive crazy . not urgent , certainly go , drain trigger refill . um not good house sort chronically run toilet . tub bathroom toilet bathtub machine"
    app.execute({"text": example_str, 'project_id': 'c5c6ba50-245f-4be1-aab8-5c68dac1bb64'})
    data = pd.DataFrame({config.TEXT: [example_str]})
    df = df.append(data)
    a = run(df)
    print(a)