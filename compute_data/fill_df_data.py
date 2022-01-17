import pandas as pd
import config

def fill_df(input_files):
    filename = config.OUTPUT_DIR_RESULT + 'symbol_list_' + input_files + ".csv"
    df = pd.read_csv(filename)
    df = df.set_index('symbol', drop=True)
    df.drop("Unnamed: 0", axis=1, inplace=True)

    df_data = pd.read_csv(config.INPUT_FILE_IMPORTED_DATA)
    df_data = df_data.set_index('symbol', drop=True)

    list_stock_no_data = []
    for stock in df.index.tolist():
        try:
            row_df_stock = df.index.get_loc(df.index[df.index == stock][0])
            row_df_data_stock = df_data.index.get_loc(df_data.index[df_data.index == stock][0])
            df.loc[df.index[row_df_stock]] = df_data.iloc[row_df_data_stock]
        except:
            # print('no data: ', stock)
            list_stock_no_data.append(stock)
    print(len(list_stock_no_data))
    print(list_stock_no_data)
    df.to_csv(filename)
