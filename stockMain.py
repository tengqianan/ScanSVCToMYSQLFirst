from StockCode import StockCode
from Download_HistoryStock import Download_HistoryStock
import time

if __name__ == '__main__':
    code = StockCode()
    code_list = code.run()
for temp_code in code_list:
    time.sleep(1)
    download = Download_HistoryStock(temp_code)
    download.run()