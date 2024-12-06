import threading
import time
import multiprocessing
import math

# Функции для АТ-01

# запускать с n = 700008
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    """Последовательное выполнение вычислений и измерение времени."""
    start_time = time.time()  # Запоминаем время старта

    fibonacci(700008)  # Вычисляем n-е число Фибоначчи

    trapezoidal_rule(math.sin, 0, math.pi, 20000000)  # Вычисляем интеграл функции sin от 0 до pi

    end_time = time.time()  # Запоминаем время окончания
    print(f'sequence time: {end_time - start_time:0.2f} \n')  # Выводим затраченное время


def threads():
    """Выполнение вычислений на потоках и измерение времени."""
    start_time = time.time()

    # Создаём потоки для выполнения функций
    thread1 = threading.Thread(target=fibonacci, args=(700008,))  # Для функции fibonacci
    thread2 = threading.Thread(target=trapezoidal_rule,args=(math.sin, 0, math.pi, 20000000))  # Для функции trapezoidal_rule

    # Запуск потоков
    thread1.start()
    thread2.start()

    # Ожидание завершения потоков
    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f'threads time: {end_time - start_time:0.2f} \n')


def processes():
    """Выполнение вычислений на процессах и измерение времени."""
    start_time = time.time()

    process1 = multiprocessing.Process(target=fibonacci, args=(700008,))  # Для функции fibonacci
    process2 = multiprocessing.Process(target=trapezoidal_rule,args=(math.sin, 0, math.pi, 20000000))  # Для функции trapezoidal_rule

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()
    print(f'processes time: {end_time - start_time:0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):

        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        sequence time:  ???

        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        threads time:  ??? 

        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        processes time:  ???
    """