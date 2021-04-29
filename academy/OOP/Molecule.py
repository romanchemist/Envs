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

    def iter_bonds(self):   # показывает пары связей
        s = self._bonds
        for n, neighb in s.items():
            for m in neighb:
                yield n, m
 # for m in s[n]:    # ! можно сразу вытаскивать
            #     yield n, m
# ______________________________3.03.PRACTICE________________________________________
# seen = set()
# for n, neighb in s.items():    # В iter bonds для еще и типов связей
#     for m, b in neighb.items():
#         if m in seen:
#             continue
#         yield n, m, b
#     seen.add(n)
# ДРУГОЙ ВАРИАНТ!!! ДЗ!! на след пару
# class IterBonds:
#     def __init__(self, _bonds):
#         bonds = self._bonds
#         print(bonds)    # ?? скрин находил
# _________________________________________

    def __contains__(self, q):
        if isinstance(q, int):
            return q in self._atoms    # выдает № in m true or false
        elif isinstance(q, Atom):
            return q in self._atoms.values()    # q == a
        else:
            raise TypeError


class Atom: # чтобы атом строкой не был . Задаем варианты чем может быть атом
    def __init__(self, isotope=None):
        self._isotope = isotope
        # проверки, общие штуки характ для любых атомов

    def __eq__(self, other):    # наш класс либо тот же либо
        return isinstance(self, type(other)) and self._isotope == other._isotope #? self._isotope  # проверяем являемся тем же или ниже
    # проверка на изотоп


class Bond:
    def __init__(self, bond=None):
        self._bond = bond


class DoubleBond(Bond):
    def __init__(self, bond=2):
        self._bond = bond


class C(Atom):
    def __init__(self, atom="C", isotope=None):
        self._isotope = isotope
        self._atom = atom

# ____________________________________________________HW 03.03.2021_____________________________________________________
# Перечислить все пары атомов которые между собой связаны! генератор. либо через класс с iter init next с IterBonds: передать в init ссылку на bonds кот сохраняет его виде атрибута и вторая которая сохраняет текущ состояние. def __iter__(s): return s
# и next который берет следующий
# couple = m.iter_bonds()
# for x in couple:
#     print(x)

class IterBonds():
    def __init__(self, _bonds):
        self._bonds = _bonds

    def __iter__(self):
        seen = set()
        for map1, nb in self._bonds.items():
            for map2 in nb:
                if map2 in seen:
                    continue
                yield map1, map2
            seen.add(map1)

class IterAtoms():
    def __init__(self, _atoms):
        self._atoms = _atoms

    def __iter__(self):
        seen = set()
        for atom, el in self._atoms.items():
            if atom in seen:
                continue
            yield atom, el

    def __contains__(self, atom, el):
        if isinstance(atom, int) and isinstance(el, Atom):
            return atom, el in self._atoms.items()
        else:
            raise TypeError

class Bfs():
    def __init__(self, _bonds):
        self._adj_ns = _bonds

    def bfs(self, start):
        visited = set()
        q = [start]
        while q:
            c = q.pop(0)
            if c in visited:
                continue
            # ns = set(self._adj_ns[c].keys()) - visited
            q.extend(set(self._adj_ns[c].keys()) - visited)
            # q.extend(ns)
            visited.add(c)
        return visited

class Dfs():
    def __init__(self, _bonds):
        self._adj_ns = _bonds

    def dfs(self, start, target, max_depth):
        max_depth = max_depth
        path = []
        visited = []
        stack = list()
        stack.append((start, 0))    # ??
        neighb = []
        while stack:
            c, d = stack.pop()
            # path.append(c)
            if len(path) > d:    # and stack
                # c, d = stack.pop()
                # visited.extend(path)
                path = path[:d]    # ??
            path.append(c)
                # return path, visited

            # neighb.extend(list(set(self._adj_ns[c].keys())-set(visited)))
            # neighb = list((set(self._adj_ns[c].keys()) - set(path)))
            for n in self._adj_ns[c].keys() - set(path):
                if n == target:
                    path.append(n)
                    return path.copy()
                elif d+1 < max_depth:
                    stack.append((n, d + 1))
class C_double_bonds():
    def __init__(self, _atoms, _bonds):
        self._atoms = _atoms
        self._bonds = _bonds
    def double_bonds(self):
        double_bonds_c = []
        for atom in self._atoms:
            if self._atoms[atom] == "C":
                if list(self._bonds[atom].values()).count(2) == 2:
                    double_bonds_c.append(atom)
        return double_bonds_c

c_doublebond_molecule = Molecule()
last = 8  # циклическая молекула (число атомов = last - 1)
c_doublebond_molecule.add_atom("C")
for i in range(2, last, 1):
    c_doublebond_molecule.add_atom("C")
    # if i == 2:
    #     bfs_molecule.add_bond(1, 2, 1)
    if i != 2 and i != len(range(last)):
        c_doublebond_molecule.add_bond(i - 1, i, 2)
    if i == len(range(last)) - 1:
        c_doublebond_molecule.add_bond(2, last - 1, 1)

c_double = C_double_bonds(c_doublebond_molecule._atoms, c_doublebond_molecule._bonds)
print(c_double.double_bonds())


            # for n in last_neighb:



            # ns = self._adj_ns[c].keys - visited

bfs_molecule = Molecule()
last = 7    # циклическая молекула (число атомов = last - 1)
for i in range(1, last, 1):
    bfs_molecule.add_atom("C")
    # if i == 2:
    #     bfs_molecule.add_bond(1, 2, 1)
    if i != 1 and i != len(range(last)):
        bfs_molecule.add_bond(i-1, i, 1)
    if i == len(range(last))-1:
        bfs_molecule.add_bond(1, last-1, 1)
bfs_molecule.add_atom("C")
bfs_molecule.add_bond(4, 7, 1)
# bfs_molecule.add_atom("C")
# bfs_molecule.add_atom("C")
# bfs_molecule.add_bond(8, 9, 1)
# bfs_molecule.add_atom("C")
# bfs_molecule.add_bond(9, 10, 1)
# bfs_molecule.add_atom("C")
# bfs_molecule.add_bond(9, 11, 1)
print(bfs_molecule._bonds)
print(bfs_molecule._atoms)
methylcyclohexane_bfs = Bfs(bfs_molecule._bonds)
methylcyclohexane_bfs.bfs(1)
print(methylcyclohexane_bfs.bfs(1))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
dfs_molecule = Molecule()
last = 8    # циклическая молекула (число атомов = last - 1)
dfs_molecule.add_atom("C")
for i in range(2, last, 1):
    dfs_molecule.add_atom("C")
    # if i == 2:
    #     bfs_molecule.add_bond(1, 2, 1)
    if i != 2 and i != len(range(last)):
        dfs_molecule.add_bond(i-1, i, 1)
    if i == len(range(last))-1:
        dfs_molecule.add_bond(2, last-1, 1)
dfs_molecule.add_atom("C")
dfs_molecule.add_bond(4, 8, 1)
dfs_molecule.add_bond(1, 2, 1)
print(dfs_molecule._bonds)
print(dfs_molecule._atoms)
m_xylene_dfs = Dfs(dfs_molecule._bonds)
m_xylene_dfs.dfs(1, 8, 5)
print(m_xylene_dfs.dfs(1, 8, 5))
# m = Molecule()
# m.add_atom("C")
# # print(m._atoms)
# # print(m._bonds)
# m.add_atom("C")
# m.add_bond(1, 2, 1)
# m.add_atom("C")
# m.add_atom("C")
# m.add_bond(2, 3, 1)
# m.add_bond(3, 4, 1)
# print(m._atoms)
# print(m._bonds)
#
# bonds = IterBonds(m._bonds)
# for bond in bonds:
#     print(bond)
#
# atoms = IterAtoms(m._atoms)
# for atom in atoms:
#     print(atom)
#
# g = iter(m)
# for x in g:
#     print(x)
#
# _______________________________________________
#
# == for n in m

    # def __contains__(self, q):
    #     if isinstance(q, int):
    #         return q in self._atoms  # выдает № in m true or false
    #     elif isinstance(q, Atom):
    #         return q in self._atoms.values()  # q == a
    #     else:
    #         raise TypeError





