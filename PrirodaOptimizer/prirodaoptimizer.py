class PrirodaOptimizer():

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
