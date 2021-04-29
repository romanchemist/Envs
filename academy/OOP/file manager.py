# для del("<название папки/файла>) и прочих, команды из os ищущие путь до файла и удаляющие в системе, а затем удаляю из словаря по ключу
# Сделал пока только заполнение словаря (кроме открытия файла).
from collections.abc import MutableMapping
import os
class DictManager(MutableMapping):

    def __init__(self, rootf):
        self._path = rootf
        self._data = {}
        tree = os.walk(rootf)
        for i in tree:
            print(i)
            if i[0] == self._path:
                for file in i[2]:
                    with open(os.path.abspath(f"{file}"), "r") as f:
                        self._data[file] = f.read()
                for dir in i[1]:
                    self._data[dir] = {}
            else:
                if not i[1]:    # если папок в этой папке нет. - чтобы лишний раз ключ не добавлялся
                    continue
                else:
                    tmp_dict_dir = dict.fromkeys(i[1], {})
                    tmp_dict_file = dict.fromkeys(i[2], 'текст файла-команду?')
                    tmp_dict_dir.update(tmp_dict_file)
                    h, last = os.path.split(i[0])
                    self._data[last] = tmp_dict_dir
                    # print(last)
                    # self._data[i[0][-1]] = tmp_dict_dir    # вторую [] через срезы универс сделать - от последнего слеша и до конца строки
# ________________________________________________PRINT_______________________________________________________________
    #C:\Users\Roman\Envs\academy\Scripts\python.exe "C:/Users/Roman/Envs/academy/OOP/file manager.py"
#{'root.txt': {'text fr file-команду?'}, 'afsdvdsv': {'d': {}, 'v': {}, 'a1.txt': {'текст файла-команду?'}}, 'b': {}, 'c': {'zdasdew': {}, 'clear.txt': {'текст файла-команду?'}}}

#Process finished with exit code 0
#______________________________________________________________________________________________________________________
    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, default=None):
        try:
            return self._data[key]
        except KeyError:
            self._data[key] = default
            return default

    def __delitem__(self, key):
        del self._data[key]

    def __contains__(self, item):
        try:
            self[item]
        except KeyError:
            return False
        return True

    def __len__(self):
        length = 0
        for couple in self._data:
            length += 1
        return length

    def __iter__(self):
        return iter(self._data)


manager = DictManager(r"C:\manager")
print(manager._data)
