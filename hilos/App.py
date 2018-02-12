from hilos.MyThread import MyThread
import datetime


time_ini = datetime.datetime.now()
print("start time: " + str(time_ini))

thread1 = MyThread("Thread-1", 5)
thread2 = MyThread("Thread-2", 3)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

time_fin = datetime.datetime.now()

print("end time " + str(time_fin))
