from itertools import islice

class Validator:
    def __get__(self, instance, owner=None):
        return getattr(instance, self.name)

    def __set_name__(self, owner, name):
        self.name = '_' + name


class AtomValidator(Validator):
    def __set__(self, instance, value):
        for el in value:
            if el not in ['B', 'C', 'H', 'N', 'O', 'F',
                          'Cl', 'Br', 'I', 'P', 'S', 'Se', 'Si']:

                raise ValueError('Некорректные атомы в структуре')
        setattr(instance, self.name, value)    # присваивает value для self.name который является атрибутом экземпляра
        # класса Conformer


class CoordinateValidator(Validator):
    def __set__(self, instance, value):
        for atom in value:
            for point in atom:
                if not isinstance(point, float):
                    raise TypeError
        setattr(instance, self.name, value)


class ChargeValidator(Validator):
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'Недопустимое значение {value}')
        setattr(instance, self.name, value)


class MultiplicityValidator(Validator):
    def __set__(self, instance, value):
        if value < 1:
            raise ValueError(f'Недопустимое значение {value}')
        setattr(instance, self.name, value)


class Conformer():    # класс для начальной (неоптимизированной) конформации молекулы, объект которого мы передаем
    # потом в PrirodaOptimizer. На вход файлы

    atoms = AtomValidator()    # если все успешно, то setattr записывает значение для переменной
    coords = CoordinateValidator()
    charge = ChargeValidator()
    multiplicity = MultiplicityValidator()

    def __init__(self, atoms, coords, charge, multiplicity, hessian):    # запись значений после валидации в атрибуты
        # экземпляра (атрибуты отдельной молекулу)
        self.atoms = atoms
        self.coords = coords
        self.charge = charge
        self.multiplicity = multiplicity
        self.hessian = hessian

    @classmethod
    def from_xyz(cls, file, charge=0, multiplicity=1, hessian=True):
        atoms_list = []
        coord_list = []
        # путь разные варианты прописать
        if isinstance(file, str):
            inp = open(file, 'r')
        else:
            inp = file    # если открытый уже, то присваиваем к inp и дальше идет

        count_atoms = int(inp.readline())
        inp.readline()
        for line in islice(inp, count_atoms):
            atom, x, y, z = line.split()
            atoms_list.append(atom)
            x = float(x); y = float(y); z = float(z)
            coord_list.append((x, y, z))
            # print(line.split())
        atoms = tuple(atoms_list)
        coords = tuple(coord_list)
        # print(coord_tuple)
        # print(atoms_tuple)
        if inp:
            inp.close()
        # conform = cls(atoms, coords, charge, multiplicity, hessian)
        # print(cls(atoms, coords, charge, multiplicity, hessian).__dict__)

        return cls(atoms, coords, charge, multiplicity, hessian)

        # print(c.atoms.__dict__)
if __name__ == '__main__':
    # with open('data/Alanine.xyz', 'r') as inp:
    #     test = Conformer.from_xyz(inp)
#     #     print(type(test))
    with open('Alanine.xyz', 'r') as f:
        molecule = Conformer.from_xyz(f)
        print(type(molecule))
#     print(type(molecule))
#     print(molecule.__dict__)    # ?? nontype был