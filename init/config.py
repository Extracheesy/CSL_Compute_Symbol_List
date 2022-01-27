from datetime import date
DATE = str(date.today())

DRIVER_PATH = "./chromedriver.exe"

INPUT_DIR = "./DATA/"
INPUT_DIR_IMPORTED_DATA = INPUT_DIR + "DATABASE/"
INPUT_FILE_IMPORTED_DATA = INPUT_DIR_IMPORTED_DATA + "symbol_list_with_info.csv"
INPUT_FILE_IMPORTED_DATA_ISNI = INPUT_DIR_IMPORTED_DATA + "symbol_isni_match.csv"
INPUT_FILE_IMPORTED_DATA_EURONEXT = INPUT_DIR_IMPORTED_DATA + "Euronext_Equities.csv"

OUTPUT_DIR = "./CSL_OUTPUT/"
OUTPUT_DIR_DATE = OUTPUT_DIR + DATE
OUTPUT_DIR_MERGED = OUTPUT_DIR_DATE + "/LIST_MERGED/"
OUTPUT_DIR_RESULT = OUTPUT_DIR_DATE + "/RESULT/"
OUTPUT_DIR_MARKET = OUTPUT_DIR_DATE + "/MARKETS"
OUTPUT_DIR_EUROPE = OUTPUT_DIR_MARKET + "/EUROPE/"
OUTPUT_DIR_US = OUTPUT_DIR_MARKET + "/US/"
OUTPUT_DIR_ASIA = OUTPUT_DIR_MARKET + "/ASIA/"
OUTPUT_DIR_OTHERS = OUTPUT_DIR_MARKET + "/OTHERS/"

OUTPUT_LIST_DIR = [OUTPUT_DIR_EUROPE, OUTPUT_DIR_US, OUTPUT_DIR_ASIA, OUTPUT_DIR_OTHERS]

GET_CAC = True
GET_DAX = True
GET_FTSE = True
GET_NASDAQ100 = True
GET_NASDAQ = True
GET_DJI = True
GET_SP500 = True
GET_YAHOO = True
GET_IBOVESPA = True
GET_NIFTY = True
GET_EURONEXT = True

CLEAN_DATABASE = True
# FILL_DATA_FROM_DATABASE = True
FILL_DATA_FROM_DATABASE = False     # FILL DATA FROM YAHOO FINANCE
CLEAN_EURONEXT_DATABASE = False