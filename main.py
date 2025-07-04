from Pagamentos import *

despesa1= DespesaFixa(5,"Compras de casa",200,"semanal")
despesa2= DespesaVariavel(10,"roupas ",100,"calças")
despesa3= DespesaOcasional(15,"Natal",50,"Dezembro")

despesa1.mostrar_informacoes()
despesa2.mostrar_informacoes()
despesa3.mostrar_informacoes()

print(f"Calculo anual despesa 1: {despesa1.calcular_total_anual()}")
print(f"Calculo anual despesa 2: {despesa2.calcular_total_anual()}")
print(f"Calculo anual despesa 3: {despesa3.calcular_total_anual()}")
