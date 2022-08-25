import pandas as pd
import src.vendors_emergency_projects.config

emergency_terms = ['urgent', 'crisis', 'danger', 'disaster', 'necessity', 'catastrophe', 'catastrof', 'katastrof', 'critical', 'mergnc', 'mergenc', 'emergency', 'immediately', 'flood', 'tornado', 'hurricane', 'tsunami', 'landslide', 'earthquake', 'asap', 'ambulance', '911', 'rescue', 'burn', 'bleed', 'choke', 'attack', 'robbery', 'vandalism', 'explosion', 'leak']
required_neg_special_terms = ['water', 'heat']
negative_terms = ['not', 'no', 'doesnt']
two_words_term_1 = ['soon']
two_words_term_2 = ['possible']

## police is no good, since it is converted from the spoken word of "please"

def run(df:pd.DataFrame):
    # df[config.EMERGENCY] = df[config.TFIDF_TITLE].apply(lambda str: _is_emeregency(str))
    df[config.EMERGENCY] = df[config.CLEAN_TITLE].apply(lambda str: _is_emeregency(str))
    return df

def _is_emeregency(lemmas):
    lem_split = lemmas.split(' ')
    for term in emergency_terms:
        if term in lem_split:
            if (lem_split.index(term) - 1 >=0 and lem_split[lem_split.index(term) - 1] not in negative_terms) and \
                    (lem_split.index(term) - 2 >=0 and lem_split[lem_split.index(term) - 2] not in negative_terms):
                return term
    for term in required_neg_special_terms:
        if term in lem_split:
            if (lem_split.index(term) - 1 >=0 and lem_split[lem_split.index(term) - 1] in negative_terms) or \
                    (lem_split.index(term) - 2 >= 0 and lem_split[lem_split.index(term) - 2] in negative_terms) or \
                    (lem_split.index(term) - 3 >= 0 and lem_split[lem_split.index(term) - 3] in negative_terms):
                return 'no '+term
            if (lem_split.index(term) + 1 < len(lem_split) and lem_split[lem_split.index(term) + 1] in negative_terms) or \
                    (lem_split.index(term) + 2 < len(lem_split) and lem_split[lem_split.index(term) + 2] in negative_terms):
                return 'no '+term
    for term1 in two_words_term_1:
        if term1 in lem_split:
            if lem_split.index(term1) + 1 < len(lem_split) and lem_split[lem_split.index(term1)+ 1] in two_words_term_2:
                return term1 + ' ' + lem_split[lem_split.index(term1)+ 1]

    return False


if __name__ == '__main__':
    df = pd.DataFrame(columns=[config.CLEAN_TITLE])
    example_str = "all right , I m probably gon na regret order point , soon possible master bathroom , uh sort valve continually run water toilet bowl . I try I include go Home Depot try replacement um sort flush mechanism like I use . I figure constant run . so end water drain tank fill night long . its drive crazy . not urgent , certainly go , drain trigger refill . um not good house sort chronically run toilet . tub bathroom toilet bathtub machine"
    data = pd.DataFrame({"clean_value": [example_str]})
    df = df.append(data)
    a = run(df)
    print(a)