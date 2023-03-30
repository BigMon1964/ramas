import platform
import psutil

#a. Cantidad de Procesadores o CPU.
print("procesadores:", platform.processor())



#b. Cantidad de Procesos ejecutándose.
print("cantidd de CPUs logicos:", psutil.cpu_count(logical=True))
print("cantidd de CPUs fisicos:", psutil.cpu_count(logical=False))

print("Cantidad de procesos ejecutándose:", len(psutil.pids()))

#c. Cantidad de Hilos o Threads que posee.
thread_count = 0
for process in psutil.process_iter():
    try:
        thread_count += process.num_threads()
    except (psutil.AccessDenied):
        pass

    print("Número de hilos en ejecución:", thread_count)

#d. Determinar si posee un Bus de Datos de 32 o 64 bits.
    (bits, linkage)= platform.architecture()
    print("Bus de datos:", bits)
#e. Cantidad de Memoria RAM. 

    
    print(f"Cantidad de Memoria RAM: {round(psutil.virtual_memory().total/1000000000, 2)}GB")

#RAM disponible
    print(f"RAM disponible: {round(psutil.virtual_memory().available/1000000000, 2)} GB")

#RAM usada
    print(f"RAM usada: {round(psutil.virtual_memory().used/1000000000, 2)} GB")

#uso de la ram 
    print(f"uso de la RAM: {psutil.virtual_memory().percent}%")

#añadido extra

print(f"Utilizacion actual de la CPU: {psutil.cpu_percent(interval=1)}")


print(f"utilizacion por CPU: {psutil.cpu_percent(interval=1, percpu=True)}")

#frecuencia actual
print(f"#frecuencia actual: {psutil.cpu_freq().current}")
#Minima frecuencia
print(f"#Minima frecuencia: {psutil.cpu_freq().min}")
#Maxima frecuencia
print(f"#Maxima frecuencia: {psutil.cpu_freq().max}")