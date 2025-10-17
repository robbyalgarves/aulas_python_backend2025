import matplotlib.pyplot as plt
import numpy as np

vendas= np.random.randint(1000, 3000, 50) # números aleatorios mediante parametros 1000 a 3000
meses = np.arange(1,51)  # realiza a contagem do parametro dado

print(vendas)
print(meses)

plt.plot(meses, vendas)
plt.ylabel("vendas")
plt.xlabel("meses")
plt.axis([0, 50, 0, max(vendas)+200])
plt.show()