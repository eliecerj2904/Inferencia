from scipy.stats import norm
print("BIENVENIDO, ESTE PROGRAMA TE INDICARÁ LOS TAMAÑOS DE MUESTRA EN TU PROYECTO")
N_1=0.0
N_2=0.0
N_3=0.0
m_1=0.0
m_2=0.0
m_3=0.0
n_1=0.0
n_2=0.0
n_3=0.0
NC=0.0
p=0.0
q=0.0
NC=float(input("Ingresa el Nivel de Confianza con el que vas a trabajar: "))
p=float(input("Ingresa la proporción de espárragos 1: "))
q=float(input("Ingresa la proporción de espárragos 2: "))
e=float(input("Ingresa el error que estás dispuesto a tolerar: "))
N_1=float(input("¿Cuántas cajas de espárragos se producen en un día?: "))
m_1=float(input("¿Cuánto pesa una caja de espárragos en kg?: "))
m_2=float(input("¿Cuánto pesa un espárrago normal en gramos?: "))/1000
N_2=round(m_1/m_2)
m_3=float(input("¿Cuánto pesa un espárrago Jumbo en gramos?"))/1000
N_3=round(m_1/m_3)
alpha=float
alpha=1-NC
medalpha=float
medalpha=alpha/2
Z= float(norm.ppf(1-medalpha))
n_1=(N_1*(Z**2)*(p*q))/((e**2)*(N_1-1)+(Z**2)*(p*q))
n_1=float(round(n_1))
n_2=(N_2*(Z**2)*(p*q))/((e**2)*(N_2-1)+(Z**2)*(p*q))
n_2=float(round(n_2))

n_3=(N_3*(Z**2)*(p*q))/((e**2)*(N_3-1)+(Z**2)*(p*q))
n_3=round(n_3)
print("La población de esparragos normales por caja es igual a", N_2)
print("La población de esparragos Jumbo por caja es igual a", N_3)


print("Necesitas sacar ", n_1, " muestras de cajas.")
print("Necesitas sacar ", n_2, " muestras de espárragos normales por caja de espárragos normal.")
print("Necesitas sacar ", n_3, " muestras de espárragos Jumbo por caja de espárragos Jumbo.")

ntotal=float(0.8*n_1*n_2+0.2*n_1*n_3)
tiempo_muestra=float(input("¿Cuántos segundos demoras en medir todos los datos de un espárrago?"))
print("La cantidad de muestras que vas a medir es: ",ntotal)
tiempototal=tiempo_muestra*ntotal*(1/60)*(1/60)*(1/4)
print("Considerando que los cuatro integrantes toman medidas a la velocidad indicada, van a tomar medidas por ",tiempototal, "Horas")


