import os, fnmatch
import pandas as pd
import numpy as np
import config

def save_list(df, path, filename):
    filename = path + filename
    df.to_csv(filename)

def mk_directories():
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR)
    if not os.path.exists(config.OUTPUT_DIR_DATE):
        os.makedirs(config.OUTPUT_DIR_DATE)
    if not os.path.exists(config.OUTPUT_DIR_MERGED):
        os.makedirs(config.OUTPUT_DIR_MERGED)
    if not os.path.exists(config.OUTPUT_DIR_RESULT):
        os.makedirs(config.OUTPUT_DIR_RESULT)
    if not os.path.exists(config.OUTPUT_DIR_MARKET):
        os.makedirs(config.OUTPUT_DIR_MARKET)
    if not os.path.exists(config.OUTPUT_DIR_EUROPE):
        os.makedirs(config.OUTPUT_DIR_EUROPE)
    if not os.path.exists(config.OUTPUT_DIR_US):
        os.makedirs(config.OUTPUT_DIR_US)
    if not os.path.exists(config.OUTPUT_DIR_ASIA):
        os.makedirs(config.OUTPUT_DIR_ASIA)
    if not os.path.exists(config.OUTPUT_DIR_OTHERS):
        os.makedirs(config.OUTPUT_DIR_OTHERS)

def wipe_out_directory(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))

def get_input_list(file):
    df_input = pd.read_csv(config.INPUT_DIR + file)
    df_input = df_input.set_index('files')

    list_files = []
    for f in df_input.index:
        if df_input.loc[f, 'merge'] == True:
            list_files.append(f+'.csv')
    return list_files

def drop_df_duplicates(df, column):
    len_df = len(df)
    # dropping ALL duplicate values
    df.sort_values(by=[column], inplace=True)
    df.drop_duplicates([column], keep='first',inplace=True)
    df.reset_index(drop=True, inplace=True)
    if(len_df - len(df) > 0):
        print("total tickers nb:      ", len_df)
        print("-> duplicates removed: ", len_df - len(df))
        print("-> remaining symbols:  ", len(df))
        print("")
    return df

def set_euronext_data_symbol(df):
    df["newsymbol"] = ""
    tickers = df['symbol'].tolist()
    # insert_df_column(df)
    df = df.set_index('symbol')
    for ticker in tickers:
        if df.market[ticker].endswith("Paris"):
            df["newsymbol"][ticker] = ticker + ".PA"
        elif df.market[ticker].endswith("Brussels"):
            df["newsymbol"][ticker] = ticker + ".BE"
        elif df.market[ticker].endswith("Amsterdam"):
            df["newsymbol"][ticker] = ticker + ".AS"
        elif df.market[ticker].endswith("Dublin"):
            df["newsymbol"][ticker] = ticker + ".IR"
        elif df.market[ticker].endswith("Lisbon"):
            df["newsymbol"][ticker] = ticker + ".LS"
        elif df.market[ticker].endswith("Oslo"):
            df["newsymbol"][ticker] = ticker + ".OL"

    df['newsymbol'].replace('', np.nan, inplace=True)
    df.dropna(subset=["newsymbol"], inplace=True)

    # df['symbol'] = df.index
    df.reset_index(drop=True, inplace=True)

    first_column = df.pop('newsymbol')
    df.insert(0, 'symbol', first_column)


    return df




def clean_up_df_symbol(path):
    df = pd.read_csv(path)
    df = drop_df_duplicates(df, "symbol")
    for c in df.columns:
        if c.startswith("Unnamed"):
            df.drop(c, axis=1, inplace=True)

    if "euronext" in path.lower():
        df = set_euronext_data_symbol(df)

    df.to_csv(path)




