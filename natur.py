class PrirodaOptimaizer():    # от пары классов сайкетлернинг наслед. Объект-трансформер/ Гессиан всегда считается

    def __init__(self, relative=False, basis='L1', memory=200, tmp_dir='/tmp', tmp_ram=0):    # L1 аналог CCPVZ
        self.relative = relative    # аргументы для настройки расчета: базис (релятив и нерелятивисткие)
        self.basis = basis
        self.memory = memory
        self.tmp_dir = tmp_dir
        self.tmp_ram = tmp_ram

    def fit(self, x, y = None):
        return self

    def transform(self, x, y=None):    # 38 минут пишем трансформер/ передаем список молекул на оптимизацию после Conformer
        ...# список молекул с начальной геометрией на оптимизацию, возвращ список молекул оптимизированных
#
# кодирует конформацию (состояние) молекулы
class Conformer():   # валидатор атомов atom, мультиплетности, заряда, координаты (координаты в виде тюпла тюплов ((1, 0.5, 0.5), ))
    # if path == файл
    # continue
    # elif path
    # ...
    # elif path
    # ...
    # else:
    # raise ошибку
    # 1 строку файла превр в инт - число атомов
    # 2 пропускаем
    # for line in itertools.islice(g-file, n-число из первой строки): 3 циклом islice из итертулса,

    @classmethod
    def from_xyz(cls, path, charge=0, multipl=1):    # file/путь/паслиб
        c = cls()
        c.atoms = AtomsValidator() # c.atoms = tuple('списка атомов')
        c.coord = CoordinateValidator() # с.xyz = tuple('списка коорд') проверка на float
        c.charge = ChargeValidator()    # Целое число
        c.multipl = MultiplicityValidator()    # >= 1
        c.gessian = GessianValidator()    # ноды все нормальные или нет. по умолч False

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
                    # setattr(self??, self.atoms, value)
                    # self.atoms.append(el)
        # self.atoms = tuple(self.atoms)
        # return self.atoms



    # def __get__(self, obj, obj_type=None):
    #     return getattr(__obj, )
class CoordinateValidator():
    ...
class ChargeValidator():
    ...
class MultiplicityValidator():
    ...
class GessianValidator():
    ...
#
for el



programma = PrirodaOptimaizer()
        # слоты добавить. атомы тюплом храним, 3 валидатора сделать (мультиплетность >=1, а заряд любое целое, атомы - чтоб левые всякие не были)
# B N C Si S F Cl Se Pb
# валидатор - это класс