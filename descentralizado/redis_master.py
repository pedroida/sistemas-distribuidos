import numpy
import time
import multiprocessing

from rq import Queue
from redis import Redis
from redis_modules import cria_matriz, multiplica_linha_coluna

if __name__ == "__main__":
    print "Initializing redis master"
    redis_conn = Redis(host='127.0.0.1', port=6379)
    queue_jobs = Queue('my_queue', connection=redis_conn)
    jobs = []

    linhas, colunas = 10,10

    print("{}: Gerando matrizes no master".format(time.strftime('%c')))
    matrizA = cria_matriz(linhas, colunas)
    matrizB = cria_matriz(linhas, colunas)
    matrizC = numpy.zeros(shape=(linhas, colunas))
    print(matrizA)
    print("\n")
    print(matrizB)
    print("\n")

    queue = multiprocessing.JoinableQueue()
    print("{}: Multiplicando matrizes".format(time.strftime('%c')))

    column = numpy.array(matrizB)

    for i in range(len(matrizA)):
        for j in range(len(matrizA[0])):
            job = queue_jobs.enqueue(multiplica_linha_coluna, matrizA[i], column[:, j], i, j)
            jobs.append(job)

    for job in jobs:
        while job.result is None:
            continue

        i, j, valor = job.result
        matrizC[i][j] = valor

    print("{}: Resultado: \n{}".format(time.strftime('%c'), matrizC))
