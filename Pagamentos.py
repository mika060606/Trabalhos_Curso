
class Despesa:
    def __init__(self,id,descricao,valor):
        self.dados={
            'id':id,
            'descricao':descricao,
            'valor':valor
        }

    def mostrar_informacoes(self):
        print(self.dados)



class DespesaFixa(Despesa):
    def __init__(self,id,descricao,valor,frequencia):
        super().__init__(id, descricao, valor)
        self.dados.update({'frequencia':frequencia})

    def calcular_total_anual(self):
        if self.dados["frequencia"] == "mensal":
            return self.dados["valor"] * 12
        elif self.dados["frequencia"] == "semanal":
            return self.dados["valor"] * 52
        else:
            raise ValueError("Frequência inválida. Use 'mensal' ou 'semanal'.")



class DespesaVariavel(Despesa):
    def __init__(self,id,descricao,valor,categoria):
        super().__init__(id,descricao,valor)
        self.dados.update({'categoria':categoria})

    def calcular_total_anual(self):
        return self.dados["valor"] * 12


class DespesaOcasional(Despesa):
    def __init__(self,id,descricao,valor,data):
        super().__init__(id, descricao, valor)
        self.dados.update({'data':data})

    def calcular_total_anual(self):
        return self.dados["valor"]