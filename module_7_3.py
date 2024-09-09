from pprint import pprint

class WordsFinder:

    def __init__(self, Name):
        self.name = Name

    def get_all_words(self):
        all_words = {}
        list_ = ''
        deleted_char = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.name, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in deleted_char:
                        line = line.replace(i, '')
                list_ = list_ + line
            all_words.update({self.name: list_.split()})
        return all_words

    def find(self, txt):
        dist = {}
        world = self.get_all_words()[self.name]
        for i in range(len(world)):
            if txt.lower() == world[i]:
                dist.update({self.name: i+1})
                return dist

    def count(self, txt):
        dist = {}
        world = self.get_all_words()[self.name]
        dist.update({self.name: world.count(txt.lower())})
        return dist

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего