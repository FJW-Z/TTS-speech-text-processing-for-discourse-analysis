import pandas as pd

def excel_to_txt_basic(path, txtname, column="answer"):
    # 中文注释：提取Excel指定列并去重后保存为TXT
    # English note: Extract specified column from Excel, remove duplicates, and save to TXT
    data = pd.DataFrame(pd.read_excel(path))
    print("数据列名：", data.columns)
    listdata = list(data[column])
    listtxt = []
    for item in listdata:
        if item not in listtxt:
            listtxt.append(item)
    # 写入TXT
    with open(txtname, "w", encoding="utf-8") as f:
        for item in listtxt:
            try:
                f.write(str(item) + "\n")
            except:
                print("写入错误，跳过该条目")
                continue

# 示例调用
excel_to_txt_basic(r"C:\Users\Trivia.xlsx", "Trivia_basic.txt", column="answer")
