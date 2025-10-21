def text_remove_duplicates(txtpath1, txtpath2):
    # 中文注释：从txtpath2中删除与txtpath1重复的文本
    # English note: Remove texts from txtpath2 that are duplicate with txtpath1
    with open(txtpath1, encoding="utf-8") as f1:
        list1 = f1.readlines()
    with open(txtpath2, encoding="utf-8") as f2, open("txt2_unique.txt", "a+", encoding="utf-8") as fnew:
        for line in f2.readlines():
            if line not in list1:
                fnew.write(line)

# 示例调用
text_remove_duplicates(r"C:\Users\testing_corpus.txt", r"C:\Users\train_corpus.txt")
