
from country_manager import (
    create_and_add_country, 
    edit_country, 
    delete_country, 
    get_all_countries
)

print("--- Criando e Adicionando Países ---")
create_and_add_country('BRA', 'Brasil')
create_and_add_country('USA', 'Estados Unidos')
create_and_add_country('CHN', 'China')

print("\n--- Lista Inicial de Países ---")
countries = get_all_countries()
for country in countries:
    print(country.get_info())

print("\n--- Editando Países ---")
edit_country('BRA', new_name='República Federativa do Brasil', medals_to_add=10)
edit_country('USA', medals_to_add=5)

print("\n--- Lista após Edição ---")
countries = get_all_countries()
for country in countries:
    print(country.get_info())

print("\n--- Excluindo um País ---")
delete_country('CHN')
delete_country('JPN')

print("\n--- Lista após Exclusão ---")
countries = get_all_countries()
for country in countries:
    print(country.get_info())