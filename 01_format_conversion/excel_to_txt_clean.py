import pandas as pd
import numpy as np

def excel_to_txt_clean(path, txtname):
    # 中文注释：读取Excel并按列优先级清洗数据（B列有值则取B列，否则取A列）
    # English note: Read Excel and clean data with column priority (take column B if not null, else column A)
    data = pd.DataFrame(pd.read_excel(path))
    print("数据列名：", data.columns)  # 调试用，可保留或删除
    listtxt = []
    for i in range(1430):  # 假设数据行数为1430，实际可改为len(data)
        if pd.isna(data.iloc[i, 1]):  # 判断第2列（索引1）是否为空
            listtxt.append(data.iloc[i, 0])
        else:
            listtxt.append(data.iloc[i, 1])
    # 写入TXT
    with open(txtname, "w", encoding="utf-8") as f:
        for item in listtxt:
            try:
                f.write(str(item) + "\n")
            except:
                print("写入错误，跳过该条目")
                continue

# 示例调用
excel_to_txt_clean(r"C:\Users\Artist.xlsx", "Artist_clean.txt")
