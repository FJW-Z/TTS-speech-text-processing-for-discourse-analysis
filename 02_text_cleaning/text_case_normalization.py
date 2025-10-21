def text_case_normalization(txtpath, newtxtname):
    # 中文注释：将全大写文本转换为首字母大写（仅处理长度>3的全大写词汇）
    # English note: Convert all-uppercase text to title case (only process all-uppercase words with length > 3)
    with open(newtxtname, "w", encoding="utf-8") as fn:
        with open(txtpath, encoding="utf-8") as f:
            for line in f.readlines():
                if line.isupper():
                    for word in line.split():
                        if word.isupper() and len(word) > 3:
                            word_new = word.title()
                            line = line.replace(word, word_new)
                fn.write(line)

# 示例调用
text_case_normalization(r"C:\Users\GenericLocation1.txt", "GenericLocation1_normalized.txt")
