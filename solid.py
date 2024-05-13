### - Primeira Questao:
# - Dado um sistema de gerenciamento de funcionários, implemente uma classe Employee que siga o SRP, sendo responsável apenas por funcionalidades relacionadas aos funcionários.
# Exercício:
# Refatore o código de uma classe que viola o SRP, dividindo as responsabilidades em classes separadas.


### - SRP
class Employee:
    def __init__(self,func_name,func_age,):
        self.func_name = func_name
        self.func_age = func_age
        self.func_salario = 0

    def display_info(self):
        print(f'Nome do funcionario {self.func_name} - Idade {self.func_age} - Salario {self.func_salario}')    

class SalaryProcessor():
    def Sacar(self,employee,amount):
        if employee.func_salario >= amount:
            employee.func_salario -= amount
            print(F"Retirada de ${amount} realizada com sucesso")
        else:
            print("Salario insuficiente")


    def deposit(self,employee,amount):
        employee.func_salario += amount
        print(f"deposito de ${amount} realizado com sucesso")
  

## - OCP - open/closed Principle: codigo estar aberto para extensao e nao para modificação
class ReportGenerator:
    def generate(self, data, report_type):
        if report_type == "pdf":
            self.generate_pdf(data)
        elif report_type == "csv":
            self.generate_csv(data)
        else:
            print("Formato de relatório não suportado.")

    def generate_pdf(self, data):
        # Lógica para gerar PDF
        ...

    def generate_csv(self, data):
        # Lógica para gerar CSV
        ...


## - LSP (Principio da Substituição de Liskov) - Utilize uma hierarquia de classes que permite adicionar novas formas sem alterar o comportamento existente.
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
