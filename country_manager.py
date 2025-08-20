
from country import Country

_countries_list = []

def create_and_add_country(code, name):
    new_country = Country(code, name)
    _countries_list.append(new_country)
    return new_country

def edit_country(code, new_name=None, medals_to_add=0):
    for country in _countries_list:
        if country.code == code:
            if new_name:
                country.edit_name(new_name)
            if medals_to_add > 0:
                country.add_medals(medals_to_add)
            print(f"País com código '{code}' editado com sucesso.")
            return True
    print(f"País com código '{code}' não encontrado.")
    return False

def delete_country(code):
    global _countries_list
    initial_length = len(_countries_list)
    _countries_list = [c for c in _countries_list if c.code != code]
    
    if len(_countries_list) < initial_length:
        print(f"País com código '{code}' excluído com sucesso.")
        return True
    print(f"País com código '{code}' não encontrado.")
    return False

def get_all_countries():
    return _countries_list