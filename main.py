from src.data_loader import load_excel_data
from src.weather_api import load_weather_data, sort_weather_data, sample_weather_data
import pandas as pd

df = load_excel_data("./data/treedata.xlsx")

# 查询天气的时间区间
delta_days =30
df["时间_end"] = pd.to_datetime(df["时间"]) + pd.Timedelta(days=delta_days)
df["时间_end"] = df["时间_end"].dt.strftime("%Y/%m/%d")  # 再转成字符串

# for row in df.iterrows():
#     row_area = str(row[1]["所在地区"])
#     row_date = str(row[1]["时间"])
#     row_date_end = str(row[1]["时间_end"])
#     row_weather = str(row[1]["遭受灾害性气候"])


#     # print(f"Area: {row_area}, Date: {row_date},{row_date_end}, Weather: {row_weather}")
#     weather_data = load_weather_data(
#         api_url="https://api.weather.com/v3/wx/conditions/historical",
#         area=row_area,
#         start_date=row_date,
#         end_date=row_date_end
#     )
#     if weather_data:
#         sorted_data = sort_weather_data(weather_data, row_weather)
#         sampled_data = sample_weather_data(sorted_data)
#         print(f"Sorted and sampled data for {row_area} on {row_date}: {sampled_data}")
#     else:
#         print(f"Failed to load weather data for {row_area} on {row_date}.")







df.to_excel("./output/结果.xlsx", index=False) # 保存结果到 Excel 文件