import mic
import random

palavras_simples = [
    "apple", "banana", "cat", "dog", "house", "car", "water", "sun", "moon", 
    "book", "tree", "chair", "table", "school", "pen", "door", "food", 
    "milk", "fish", "bird", "shoe", "bag", "hat", "train", "bus", 
    "window", "ball", "key", "flower", "phone", "shirt", "clock", 
    "camera", "bread", "orange", "mouse", "egg", "milk", "bed"
]

pontuacao = 10
nome = input("digite seu nome: ")

while True:
    palavra_aleatoria = random.choice(palavras_simples)
    print(f"Fale: {palavra_aleatoria}")


    text = mic.captura_audio()
    print(text)

    if text == palavra_aleatoria:
        print("pronuncia correta")
        pontuacao += 1
    else:
        print("Palavra incorreta")
        print(f"Parabéns, {nome} sua pontuação foi de {pontuacao} ponto")
        break
