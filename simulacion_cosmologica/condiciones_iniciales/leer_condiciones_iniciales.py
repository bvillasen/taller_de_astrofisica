import pickle
import numpy as np
 

nombre_archivo = '128_20Mpc/0_particulas.pkl'
print( f'Abriendo archivo: {nombre_archivo}')
archivo = open( nombre_archivo, 'rb' )
datos = pickle.load(archivo)
 
masa_de_particula = datos['masa_de_particula'] # en M_solar

# Posiciones iniciales
pos_x = datos['pos_x'][...] # en kpc
pos_y = datos['pos_y'][...] # en kpc
pos_z = datos['pos_z'][...] # en kpc

# Velocidades iniciales
vel_x = datos['vel_x'][...] # en km/sec
vel_y = datos['vel_y'][...] # en km/sec
vel_z = datos['vel_z'][...] # en km/sec

archivo.close()
print('Exito!')