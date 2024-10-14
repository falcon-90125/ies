import numpy as np

original_luminous_flux = 600
consumer_luminous_flux = 400

coefficient = consumer_luminous_flux / original_luminous_flux

# Считаем данные из файла с помощью NumPy
data = np.genfromtxt('ies_in.txt', delimiter=' ')

data_out = data * coefficient

print(data_out)

np.savetxt('ies_out.txt', data_out, delimiter=' ', fmt='%.3f')
