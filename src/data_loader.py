#用来进行excel数据的加载
import pandas as pd

def excel_date_parser(x):
    if pd.isna(x) or str(x).strip() == "":
        return None
    try:
        # 如果是纯数字（Excel 序列号）
        if str(x).strip().isdigit():
            return pd.to_datetime(float(x), unit="d", origin="1899-12-30")
        else:
            # 直接尝试解析字符串（包括 "2025年1月1日" 等格式）
            return pd.to_datetime(x, errors="coerce")
    except:
        return None
    
def load_excel_data(file_path):
    try:
        data = pd.read_excel(file_path,parse_dates=["时间"])
        # 对“时间”列应用
        data["时间"] = data["时间"].apply(excel_date_parser)
        # 如果想统一格式成 YYYY/MM/DD
        data["时间"] = data["时间"].dt.strftime("%Y/%m/%d")
        return data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None




