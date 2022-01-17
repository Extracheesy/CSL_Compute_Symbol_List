import sys
import pandas as pd
import config

from tools import mk_directories
from list_manager import get_list
from merging_csv import merge_list
from scrap_profile import get_info_list
from fill_df_data import fill_df

sys.path.append("./compute_data/")
sys.path.append("./manage_list/")
sys.path.append("./merging/")
sys.path.append("./scraping/")
sys.path.append("./init/")

"""
    CSL module: Compute Symbol List
"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    if (str(sys.argv[1]) == "--COLAB"):
        config.COLAB = True
    else:
        config.COLAB = False

    print(config.DATE)

    mk_directories()

    get_list()

    input_file = str(sys.argv[2])
    input_file = input_file[2:]
    merge_list(input_file + '.csv')
    fill_df(input_file)

    # df = pd.read_csv(config.OUTPUT_DIR_RESULT + 'symbol_list_CSL_ALL.csv')
    # df = pd.read_csv(config.OUTPUT_DIR_RESULT + 'batch_3_symbol_list_CSL_ALL_failed.csv')
    df = pd.read_csv(config.OUTPUT_DIR_RESULT + 'symbol_list_CSL_EURONEXT.csv')

    df_with_info, df_failed = get_info_list(df)

    df_with_info.to_csv(config.OUTPUT_DIR_RESULT + 'CSL_EURONEXT_with_info.csv')
    df_failed.to_csv(config.OUTPUT_DIR_RESULT + 'CSL_EURONEXT_failed.csv')


#    df_with_info.to_csv(config.OUTPUT_DIR_RESULT + 'batch_3_symbol_list_CSL_ALL_with_info_run_2.csv')
#    df_failed.to_csv(config.OUTPUT_DIR_RESULT + 'batch_3_symbol_list_CSL_ALL_failed_run_2.csv')

    print_hi('PyCharm')

