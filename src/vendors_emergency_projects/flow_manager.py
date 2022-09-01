import pandas as pd

import src.vendors_emergency_projects.cleaner as cleaner
import src.vendors_emergency_projects.config as config
import src.vendors_emergency_projects.emergency_checker as emergency_checker
from src.vendors_emergency_projects.logger import logger


def _read_data(input_path):
    # raw_df = pd.read_csv(input_path, encoding='ISO-8859-1', skipinitialspace=True, error_bad_lines=False, nrows=10)
    # return raw_df

    orig_df = pd.read_csv(input_path, encoding='ISO-8859-1', skipinitialspace=True, error_bad_lines=False)
    orig_df = orig_df[orig_df.text.isna() == False]
    orig_df.columns = ['object key', 'category', 'file_path','text','objects']
    orig_df['objects'] = orig_df['objects'].apply(lambda x: '' if pd.isna(x) else ' ' + x.replace(',','').lower())
    orig_df['text'] = orig_df['text'] + orig_df['objects']

    logger.info("categories check: " + str(orig_df.category.value_counts()))
    return orig_df

def run_flow():
    input_path = config.INPUT_PATH
    raw_df = _read_data(input_path)

    if raw_df.empty:
        raise Exception("Input data is empty")

    ## clean the data
    logger.info("cleaner")
    raw_df = cleaner.preprocess(raw_df)

    # ## prepare the data before running over it - No need for now!
    # logger.info("enhancer")
    # raw_df = enhancer.enhance(raw_df)

    ## check emergency terms
    # raw_df = features.run(raw_df)

    logger.info ("emergency checker")
    raw_df = emergency_checker.run(raw_df)

    # if config.TRAIN_MODEL:
    #     raw_df = trainer.run(raw_df)

    # result_df = matcher.run(raw_df)

    ## print results - only of the matched items
    # print("found matches:")
    # for index, row in result_df.iterrows():
    #     if row[amazon_vars.BEST_MATCH]:
    #         print(row[amazon_vars.TEXT_TITLE], " ---> ", row[amazon_vars.BEST_MATCH])

    ## output results:
    # output_df = result_df[[config.TEXT_TITLE, config.BEST_MATCH]]
    raw_df.to_csv(config.OUTPUT_PATH, mode='w', header=True, index=False, encoding='utf_8_sig')


if __name__ == '__main__':
    run_flow()