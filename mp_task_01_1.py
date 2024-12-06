import threading
import multiprocessing
import time
import requests
import asyncio

urls = ['https://www.example.com'] * 10

def fetch_url(url):
    response = requests.get(url)
    return response.text

def sequence():
    start_time = time.time()
    results = []

    for url in urls: # Проходим по каждому URL в списке
        result = fetch_url(url) # Запрос к URL
        results.append(result)

    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} секунд\n')

def threads():
    start_time = time.time()
    threads_list = [] # Хранилище потоков
    results = []

    def thread_target(url):
        result = fetch_url(url)
        results.append(result)

    for url in urls:
        thread = threading.Thread(target=thread_target, args=(url,)) # Создаём поток
        thread.start() # Запускаем поток
        threads_list.append(thread)  # Добавляем его в список

    for thread in threads_list: # Ждем завершения всех потоков
        thread.join() # Блокировка до завершения потока

    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} секунд\n')

def processes():
    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:  # Создаём пул из 4 процессов
        results = pool.map(fetch_url, urls)  # Применяем функцию fetch_url ко всем URL

    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} секунд\n')  # Выводим время выполнения




if __name__ == '__main__':
    sequence()
    threads()
    processes()
