import doctest


class Table:
    def __init__(self, square: (int, float), material: str):
        """
        Создание и подготовка к работе объекта "стол"

        :param square: Площадь стола в метрах квадратных
        :param material: Материал, из которого изготовлен стол

        Примеры:
        >>> table = Table(0.6, "oak")
        """
        if not isinstance(square, (int, float)):
            raise TypeError("Площадь стола должна быть типа int или float")
        if square < 0:
            raise ValueError("Площадь не может иметь отрицательное значение")
        self.square = square

        if not isinstance(material, str):
            raise TypeError("Название материала должно быть типа str")
        self.material = material

    def increase_square(self, x: float) -> None:
        """
        Увеличение площади стола
        :param x: величина, на которую увеличивается площадь

        Примеры:
        >>> table = Table(0.5,"oak")
        >>> table.increase_square(0.2)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Добавляемая величина должны быть типа int или float")
        if x < 0:
            raise ValueError("Добавляемая величина должна быть положительной")
        ...

    def is_table_made_of_oak(self) -> bool:
        """
        Функция, что проверяет, сделан ли стол из дуба

        :return: Является ли стол дубовым

        Примеры:
        >>> table = Table(0.4, "linden")
        >>> table.is_table_made_of_oak()
        """

        ...


class Tree:
    def __init__(self, name: str, height: (int, float)):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param name: Наименование вида дерева
        :param height: Высота дерева в метрах

        Примеры:
        >>> tree = Tree("linden", 2)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("высота дерева должна быть типа int или float")
        if height < 0:
            raise ValueError("Высота не может иметь отрицательное значение")
        self.height = height

        if not isinstance(name, str):
            raise TypeError("Название вида дерева должно быть типа str")
        self.name = name

    def decrease_height(self, x: float) -> None:
        """
        подрезание верхушки дерева
        :param x: величина, на которую укорачивается дерево

        :raise ValueError: Если величина, на которую укорачивают дерево больше, чем высота этого дерева-вызываем ошибку

        Примеры:
        >>> tree = Tree("linden",5)
        >>> tree.decrease_height(2)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Величина, на которую укорачивают дерево должна быть типа int или float")
        if x < 0:
            raise ValueError("Величина, на которую укорачивают дерево должна быть положительной")
        ...

    def tree_is_linden(self) -> bool:
        """
        Функция, что проверяет, является ли дерево липой

        :return: Является ли дерево липой

        Примеры:
        >>> tree = Tree("linden", 52)
        >>> tree.tree_is_linden()
        """

        ...


class Facebook:
    def __init__(self, count_of_users: int, version: (int, float), color_theme: str):
        """
        Создание и подготовка к работе объекта "Facebook"

        :param count_of_users: Количество пользователей приложения
        :param version: версия приложения
        :param color_theme: Цветовая тема приложения, к примеру, "Светлая" или "Тёмная".
        Примеры:
        >>> app = Facebook(4000, 1.02, "light")
        """
        if not isinstance(count_of_users, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if count_of_users < 0:
            raise ValueError("Количество пользователей не может иметь отрицательное значение")
        self.count_of_users = count_of_users

        if not isinstance(version, (int, float)):
            raise TypeError("Версия должна быть типа int или float")
        if version <= 0:
            raise ValueError("Версия не может быть отрицательной или равняться нулю")
        self.version = version

        if not isinstance(color_theme, str):
            raise TypeError("Название цветовой темы должно быть типа str")
        self.color_theme = color_theme

    def add_new_users(self, x: int) -> None:
        """
        Добавление новых пользователей
        :param x: количество новых пользователей

        :raise ValueError: Если величина, на которую укорачивают дерево больше, чем высота этого дерева-вызываем ошибку

        Примеры:
        >>> app = Facebook(4000, 1.02, "black")
        >>> app.add_new_users(5)
        """
        if not isinstance(x, int):
            raise TypeError("Количество новых пользователей должно быть типа int")
        if x < 0:
            raise ValueError("Количество новых пользователей должно быть положительным")
        ...

    def theme_is_light(self) -> bool:
        """
        Функция, что проверяет, является ли установленная цветовая тема светлой

        :return: Является ли световая тема светлой

        Примеры:
        >>> app = Facebook(4000, 1.02, "black")
        >>> app.theme_is_light()
        """

        ...

    if __name__ == "__main__":
        doctest.testmod()
    pass
