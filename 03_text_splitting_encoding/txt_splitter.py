def text_splitter(txtpath, keyword):
    # 中文注释：按行拆分TXT并生成带四位编号的子文件
    # English note: Split TXT by line and generate sub-files with 4-digit IDs
    with open(txtpath, encoding="utf-8") as f:
        i = 1
        for line in f.readlines():
            if line not in ["\n", "\r\n"]:
                fileid = str(i).zfill(4)
                with open(f"{keyword}_{fileid}.txt", "w", encoding="utf-8") as fnew:
                    if line[0].isdigit():  # 去除开头数字编号
                        new_line = line[3:].strip()
                        fnew.write(new_line)
                    else:
                        fnew.write(line)
                i += 1

# 示例调用
text_splitter(r"C:\Users\Harry Potter The Complete Collection.txt", "Novel")
