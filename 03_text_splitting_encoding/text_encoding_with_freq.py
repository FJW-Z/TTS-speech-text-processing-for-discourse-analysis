def text_encoding(txtpath, keyword):
    # 中文注释：为文本添加四位编号并编码，支持去除开头数字编号
    # English note: Add 4-digit ID to text and encode, support removing leading number IDs
    with open(txtpath, encoding="utf-8") as f:
        i = 1
        with open(f"{keyword}_encoded.txt", "w", encoding="utf-8") as fnew:
            for line in f.readlines():
                if line not in ["\n", "\r\n"]:
                    line = line.strip()
                    fileid = str(i).zfill(4)
                    if line[0].isdigit():  # 去除开头数字编号
                        new_line = line[2:].strip()
                        fnew.write(f"{keyword}_{fileid}\t{new_line}\n")
                    else:
                        fnew.write(f"{keyword}_{fileid}\t{line}\n")
                    i += 1

# 示例调用
text_encoding(r"C:\Users\DeviceHelper1000.txt", "vamos_devicehelper")
