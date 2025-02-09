class NapoleonDict(dict):
    def __missing__(self, key):
        if key == "不可能" or key == "impossible":
            return "不可能≪impossible≫の文字はない。"
        return f"{key}の文字はある。"

# 余の辞書
my_dict = NapoleonDict()

# ユーザーの検索
while True:
    word = input("検索する単語を入力（終了するには 'exit' ）：")
    if word.lower() == "exit":  
        break
    print(f"余の辞書に{my_dict[word]}")
