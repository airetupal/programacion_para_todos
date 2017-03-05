#prueba ivan
#prueba alex
___________________________

>>> import math
>>> Vel_Inicial = int(input("Ingrese la velocidad con que sale la habilidad de Goku: "))
>>> gravedad = float(9.8)
>>> Angulo_Salida = int(input("Ingrese el angulo con que sale la habilidad de Goku recpecto al eje Y: "))
>>> tmax = ((2*Vel_Inicial)*(math.sin(Angulo_Salida)))/gravedad
>>> hmax = ((Vel_Inicial**2)*((math.sin(Angulo_Salida))**2))/2*gravedad
>>> xmax = ((2*(Vel_Inicial**2))*((math.cos(Angulo_Salida))**2))/gravedad*(math.tan(Angulo_Salida))
>>> print (str(tmax))
>>> print (str(hmax))
>>> print (str(xmax))
