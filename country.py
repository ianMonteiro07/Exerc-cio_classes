
class Country:

    def __init__(self, code, name):
        self.code = code  # Código do país (ex: 'BRA')
        self.name = name  # Nome do país (ex: 'Brasil')
        self.medals_won = 0 # Um atributo para guardar o número de medalhas

    def add_medals(self, num_medals):
        if num_medals > 0:
            self.medals_won += num_medals
        else:
            print("Número de medalhas deve ser positivo.")

    def edit_name(self, new_name):
        self.name = new_name
    
    def get_info(self):
        return f"Código: {self.code}, Nome: {self.name}, Medalhas: {self.medals_won}"