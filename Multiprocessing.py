import multiprocessing
import time

def sleep():
    print(f'Sono nella funzione')

    time.sleep(1)

    print(f'Sto uscendo dalla funzione')



    if __name__ == '__main__':
        tic: float = time.time()