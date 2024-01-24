from prettytable import PrettyTable

def show_main_menu():
    t = PrettyTable(['№', 'Выбор'])
    t.title = "Представление графов в ЭВМ"
    t.align['Выбор'] = "l"
    t.add_row(['1','Матрица смежности'])
    t.add_row(['2','Список ребер'])
    t.add_row(['3','Массив записей'],divider=True)
    t.add_row(['4','Показать граф'])
    t.add_row(['5','Размер объектов'])
    t.add_row(['6','Время выполнения'],divider=True)
    t.add_row(['0','Выход'])
    print(t)

def show_side_menu():
    t = PrettyTable(['№', 'Выбор'])
    t.align['Выбор'] = "l"
    t.title = "Представление графов в ЭВМ"
    t.add_row(['1','Соседи заданной вершины'])
    t.add_row(['2','Создает ли последовательность цепь'])
    t.add_row(['3','Номера вершин, сумма весов ребер которых больше заданной величины'])
    t.add_row(['4','Количество ребер в графе'])
    t.add_row(['5','Отобразить'],divider=True)
    t.add_row(['0','Назад'])
    print(t)