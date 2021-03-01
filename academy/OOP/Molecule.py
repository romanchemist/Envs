class Molecule:
    def __init__(self):
        self._atoms = {}
        self._bonds = {}

    def add_atom(self, atom, *, map_=None):
        if map_ is None:
            map_ = max(self._atoms, default=0) + 1
        elif not isinstance(map_, int):
            raise TypeError
        elif map_ < 1:
            raise ValueError
        elif map_ in self._atoms:
            raise KeyError
        # if atom:  # дописать проверки для atom
        #     ...
        self._atoms[map_] = atom
        self._bonds[map_] = {}
        return map_  # чтобы значть что это был за атом, чтобы понять, какой это был атом, т.к. мы могли и не знать мап
        # данного атома

    def add_bond(self, map1, map2, bond):
        if not isinstance(bond, int):
            raise TypeError
        if bond not in (1, 2, 3):
            raise ValueError

        # есть ли в селф.атом , что мап1 не равно мап2, что уже есть связь м\у этими атомами, что одноатомн мол-ла
        neigh1 = self._bonds[map1]
        neigh2 = self._bonds[map2]

        if neigh1 is neigh2:  # что мап1 не равно мап2
            raise KeyError
        if map1 in neigh2:  # что уже есть связь м\у этими атомами
            raise KeyError

        neigh1[map2] = bond
        neigh2[map1] = bond
# __________________________________________________26.02.2021__________________________________________________________
# дописать проверки для atom - 15 строка
# добавить метод : del_atom(map_), del_bond(map1, map2)

    def del_atom(self, map_):    # дописать del atom чтобы связи тоже сразу удалялась!
        if not isinstance(map_, int):
            raise TypeError
        elif map_ not in self._atoms:
            raise KeyError
        # self._bonds найти ключи в внутреннем словаре для атома который удаляем - это будут его соседи
        #!!! del self._bonds[...][map_]    # найти в этих ключах этот map_ и поудалять
        del self._atoms[map_]
        print(map_)

    def del_bond(self, map1, map2):
        # if not isinstance(map1, int) or not isinstance(map2, int):
            # raise TypeError
        # elif map1 not in self._bonds[map2]:
        #     raise KeyError
        del self._bonds[map1][map2]
        del self._bonds[map2][map1]

    def get_atom(self, map_):
        return self._atoms(map_)

    def get_bond(self, map1, map2):
        return self._bonds[map1][map2]

    # def __iter__(self):    # ВЕРНЕТ генератор который будет возвращать атомы, но реализация плохая
    #     for n in self._atoms:    # тут в питоне вызывается метод __iter__ (генератор), а если еще есть и next - итератор
    #         yield n    # ГЕНЕРАТОР! содержит next и iter - ЭТО ОБЪЕКТ класса Генератор. из этого объекта с помощью next будет будет работать for
        # ИДЕЯ for n in mol:
            # if mol.get_atom(n) = N возвращает
    def __iter__(self):
        return iter(self._atoms)





m = Molecule()
m.add_atom("C")
print(m._atoms)
print(m._bonds)
m.add_atom("C")
m.add_bond(1, 2, 1)
print(m._atoms)
print(m._bonds)
# m.del_atom(1)
print(m._atoms)
print(m._bonds)
# m.del_bond(1, 2)
print(m._atoms)
print(m._bonds)
g = iter(m)
for x in g:
    print(x)    # == for n in m
# ____________________________________________________HW 03.03.2021_____________________________________________________
# Перечислить все пары атомов которые между собой связаны! генератор. либо через класс с iter init next с IterBonds: передать в init ссылку на bonds кот сохраняет его виде атрибута и вторая которая сохраняет текущ состояние. def __iter__(s): return s
# и next который берет следующий
def iter_bonds(self): # 2 цикла


    ...
    # yield  n, m



