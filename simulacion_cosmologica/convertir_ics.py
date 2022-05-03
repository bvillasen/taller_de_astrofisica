import numpy as np
import pickle
import h5py as h5


dir = 'condiciones_iniciales/64_20Mpc/'

# Leer las condiciones iniciales
nombre_archivo = dir + '0_particulas.h5'
archivo = h5.File( nombre_archivo, 'r' )
masa_de_particula = archivo.attrs['particle_mass'] # en M_solar / h
# Posiciones iniciales
pos_x = archivo['pos_x'][...]
pos_y = archivo['pos_y'][...]
pos_z = archivo['pos_z'][...]
# Velocidades iniciales
vel_x = archivo['vel_x'][...]
vel_y = archivo['vel_y'][...]
vel_z = archivo['vel_z'][...]
# Numero de particulas
n_particulas = len(pos_x)
# Terminamos de leer, cerramos el archivo
archivo.close()

data = { 'masa_de_particula': masa_de_particula, 'pos_x':pos_x, 'pos_y':pos_y, 'pos_z':pos_z, 'vel_x':vel_x, 'vel_y':vel_y, 'vel_z':vel_z  }
nombre_archivo = dir + 'particulas.pkl'
f = open( nombre_archivo, 'wb' )
pickle.dump( data, f)
print ( f'Saved File: {nombre_archivo}' )