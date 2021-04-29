# from itertools import islice
import itertools
class PrirodaOptimaizer():

    def __init__(self, relative=False, basis='L1', memory=200, tmp_dir='/tmp', tmp_ram=0):    # L1 аналог CCPVZ
        self.relative = relative    # аргументы для настройки расчета: базис (релятив и нерелятивисткие)
        self.basis = basis
        self.memory = memory
        self.tmp_dir = tmp_dir
        self.tmp_ram = tmp_ram

    def fit(self, x, y=None):
        """Затычка, потому что СКЛ так требует"""
        return self    # сам объект(как бы после обучения)

    def transform(self, x, y=None):
        ...

# класс для начальной (неоптимизированной) конформации молекулы, объект которого мы передаем потом в PrirodaOptimaizer.
# на вход файлы
class Conformer():

    @classmethod
    def from_xyz(cls, path, charge=0, multipl=1):
        # if isinstance(path, str):
        #     continue
        # elif isinstance(path, )
        atoms_list = []
        coord_list = []
        count_atoms = int(f.readline())
        f.readline()
        for line in itertools.islice(f, count_atoms):
            atom, x, y, z = line.split()
            atoms_list.append(atom)
            x = float(x); y = float(y); z = float(z)
            coord_list.append((x, y, z))
            # print(line.split())
        atoms_tuple = tuple(atoms_list)
        coord_tuple = tuple(coord_list)
        # print(coord_tuple)
        # print(atoms_tuple)
        c = cls()
        c.atoms = atoms_tuple
        c.coords = coord_tuple
        c.charge = charge
        c.multiplicity = multipl
        print(c.__dict__)
            # print(line)

class AtomsValidator():
    def __set_name__(self, owner, name):
        self.__name = name
    def __set__(self, instance, value):
        #self.atoms = []
        if isinstance(value, list):
            for el in value:
                if el not in {'B','C', 'H', 'N', 'O', 'F',
                        'Cl', 'Br', 'I', 'P', 'S', 'Se', 'Si'}:
                    raise ValueError('Некорректные атомы в структуре')
                else:
                    instance.__dict__[self.__name] = value

with open('Alanine.xyz', 'r') as f:
    molecule = Conformer.from_xyz(f)

