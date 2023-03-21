import json


class Controller:
    def __init__(self):
        pass

    def push_word(self, word):
        with open("bad_words.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        with open("bad_words.json", "w", encoding="utf-8") as file:
            data.append(word)
            json.dump(data, file, ensure_ascii=False, indent=2)

    def check_word(self, message_text):
        with open("bad_words.json", "r", encoding="utf-8") as file:
            bad_words = json.load(file)
            for bad_word in bad_words:
                print(bad_word)
                if bad_word in message_text:
                    return True

