import time

segundos_hoje = time.time()
print(segundos_hoje)

data = time.ctime()
print(data)

print("executando processamento dos dados. isso vai demorar")
# time.sleep(3)
print("continuo processando os dados")
# time.sleep(3)
print("processamento finalizado!")

data_detalhes = time.gmtime()
print(data_detalhes)