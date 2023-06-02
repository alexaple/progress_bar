import time

# Прогресс-бар
def progress_bar(steps: int, graph_count: int=20, min_v: int=0, max_v: int=50, limit_v: int=100, pause: float=0.01) -> None:
    if limit_v < max_v:
        limit_v = max_v
    step_size = (max_v - min_v) / steps
    a = limit_v / graph_count
    c = (max_v - min_v) / a
    d = graph_count
    count = min_v / a
    for i in range(0, steps + 1):
        graph = '-' * int(round(count, 10))
        print(f'\r[{graph}{" " * (graph_count - len(graph))}][{int(min_v + i * step_size)}%]', end='')
        d -= c / steps
        count += c / steps
        time.sleep(pause)
    return None

if __name__ == '__main__':
    # Запуск прогресс-бара для одной итерации
    # progress_bar(steps=40, graph_count=20, min_v=25, max_v=75, limit_v=100)

    # Тест прогресс-бара
    # В качесве исходных данных принимается кол-во элементов:
    data = range(0, 100)
    print(f'Элементов: {len(data)}')
    print('=========\n')
    # Аргументы и переменные прогресс-бара
    tb_step = 100 / len(data)
    min_tbv = 0
    max_tbv = int(round(tb_step))
    print('Загрузка:')
    # Загрузка
    for i, el in enumerate(data):
        time.sleep(0.001)
        # Запуск прогресс-бара для каждой итерации
        progress_bar(steps=40, graph_count=20, min_v=min_tbv, max_v=max_tbv, limit_v=100, pause=0.01)
        tb_dif_round = int(100 - tb_step * (len(data) - i - 2))
        min_tbv = max_tbv
        max_tbv = tb_dif_round
    print('\nЗавершено')