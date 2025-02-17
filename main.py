class Conifer:
    """
    Документация для базового класса Conifer
    Базовый класс для инициализации эксземпляра принимает такие атрибуты экземпляра как:
    _height - высоту дерева в метрах. Значение может быть как целочисленным, так и числом с плавающей точкой.
    _lifespan - продолжительность жизни дерева в годах. Типы значения такие же как у атрибута height.
    Артрибуты сделаны защищенными для того, чтобы пользователь не мог задать им неверное значение в обход методов.
    """

    def __init__(self, _height: (int, float), _lifespan: (int, float)) -> None:
        """ Инициализация экземпляра класса """
        self._height = None
        self.init_height(_height)
        self._lifespan = None
        self.init_lifespan(_lifespan)

    def init_height(self, _height: (int, float)) -> None:
        """
        Метод для инициализации атрибута height с нужными проверками.
        """
        if not isinstance(_height, (int, float)):
            raise TypeError("Высота дерева должна являться целым числом или числом с плавающей точкой")
        if _height < 0:
            raise ValueError("Высота дерева должна быть больше нуля")
        self._height = _height

    def change_height(self, new_height: (int, float)) -> None:
        """
        Метод предназначен для присваивания нового значения атрибуту heigth,что будет соответствовать росту дерева
        или тому, что его подрезали, в него включены проверки для принимаемого значения.
        """
        if not isinstance(new_height, (int, float)):
            raise TypeError("Высота должна быть целым числом или числом с палавающей точкой")
        self._height += new_height
        if self._height <= 0:
            raise ValueError("Высота дерева не может быть как отрицательным числом, так и нулём")

    def init_lifespan(self, _lifespan: (int, float)):
        """
        Метод для присваивания значения атрибуту lifespan с нужными проверками.
        """
        if not isinstance(_lifespan, (int, float)):
            raise TypeError("Срок жизни дерева должен являться целым числом или числом с плавающей точкой")
        if _lifespan <= 0:
            raise ValueError("Срок жизни дерева должен быть больше или равен нулю")
        self._lifespan = _lifespan

    def change_lifespan(self, new_lifespan: (int, float)) -> None:
        """
        Метод предназначен для присваивания нового значения атрибуту lifespan,что будет соответствовать увеличению
        или уменьшению продолжительности жизни дерева, в него включены проверки для принимаемого значения.
        """
        if not isinstance(new_lifespan, (int, float)):
            raise TypeError("Высота должна быть целым числом или числом с палавающей точкой")
        self._lifespan += new_lifespan
        if self._lifespan <= 0:
            raise ValueError("Срок жизни дерева не может быть как отрицательным числом, так и нулём")

    def __str__(self) -> str:
        """" Определяет поведение функции str() """
        return f"{self.__class__.__name__}, " \
            f" высотой {self._height} метров, со сроком жизни (в годах) {self._lifespan}"

    def __repr__(self) -> str:
        """ Определяет поведение функции repr() """
        return f"{self.__class__.__name__} (_height = {self._height}, _lifespan = {self._lifespan})"


class Spruce(Conifer):
    def change_height(self, new_height: (int, float)) -> None:
        """
        Метод предназначен для присваивания нового значения атрибуту heigth,что будет соответствовать росту дерева
        или тому, что его подрезали, в него включены проверки для принимаемого значения.
        Перегружается в связи с тем, что максимальная, задокументированная высота ели - 110 метров.
        Условно примем, что все ели не могут вырасти больше этого значения.
        """
        if not isinstance(new_height, (int, float)):
            raise TypeError("Высота должна быть целым числом или числом с палавающей точкой")
        self._height += new_height
        if self._height <= 0:
            raise ValueError("Высота дерева не может быть как отрицательным числом, так и нулём")
        if self._height > 100:
            raise ValueError("Высота ели не может быть больше сотни метров")


if __name__ == "__main__":
    pass
