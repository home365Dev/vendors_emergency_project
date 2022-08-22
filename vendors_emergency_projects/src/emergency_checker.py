import pandas as pd
import config

emergency_terms = ['urgent', 'crisis', 'danger', 'disaster', 'necessity', 'catastrophe', 'catastrof', 'katastrof', 'critical', 'mergnc', 'mergenc', 'emergency', 'immediately', 'flood', 'tornado', 'hurricane', 'tsunami', 'landslide', 'earthquake', 'fire', 'asap', 'ambulance', '911', 'rescue', 'burn', 'bleed', 'choke', 'attack', 'poison', 'robbery', 'vandalism', 'alert', 'explosion', 'bomb', 'shot', 'accident', 'leak']
special_terms = ['water', 'heat']
negative_terms = ['not', 'no', 'doesnt']
## police is no good, since it is converted from the spoken word of "please"

def run(df:pd.DataFrame):
    # df[config.EMERGENCY] = df[config.TFIDF_TITLE].apply(lambda str: _is_emeregency(str))
    df[config.EMERGENCY] = df[config.CLEAN_TITLE].apply(lambda str: _is_emeregency(str))
    return df

def _is_emeregency(lemmas):
    previous_term = ''
    previous_term_2 = ''
    previous_term_3 = ''
    for term in emergency_terms:
        if term in lemmas:
            return term

    return False


if __name__ == '__main__':
    df = pd.DataFrame(columns=[config.CLEAN_TITLE])
    example_str = "all right , I m probably gon na regret order point , master bathroom , uh sort valve continually run water toilet bowl . I try I include go Home Depot try replacement um sort flush mechanism like I use . I figure constant run . so end water drain tank fill night long . its drive crazy . not urgent , certainly go , drain trigger refill . um not good house sort chronically run toilet . tub bathroom toilet bathtub machine"
    data = pd.DataFrame({"clean_value": [example_str]})
    df = df.append(data)
    run(df)