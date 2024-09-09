from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    file_ = open(file_name, 'a', encoding='utf-8')
    for i, j in enumerate(strings):
        key = (i+1, file_.tell())
        strings_positions[key] = j
        file_.write(j + '\n')
    file_.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)