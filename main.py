import json
import requests

def dish_fetch(num):
    url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"
    
    response = requests.get(url)    
    plato = response.json()
    
    return plato

def main():
  
    print("🍲 --- EXPLORADOR DE GASTRONOMÍA COLOMBIANA --- 🍲")
    
    id_plato = input("Introduce el ID del plato: ")
    
    
    resultado = dish_fetch(id_plato)
    
    
    print(f"Resultado: {resultado['name']}")

if __name__=="__main__":
  main()