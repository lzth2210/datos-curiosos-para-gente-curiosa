from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    datoAzar = random.choice(datos_lista)
    return render_template('index.html', mensaje=datoAzar)

datos_lista = [
    "Los pulpos tienen tres corazones y su sangre es de color azul.",
    "La miel nunca se echa a perder; se han encontrado frascos comestibles en tumbas egipcias de hace miles de años.",
    "El planeta Saturno podría flotar en agua debido a su baja densidad.",
    "Los flamencos no nacen rosados, su color proviene de los carotenoides en su dieta.",
    "El corazón de una ballena azul puede pesar más que un automóvil pequeño.",
    "Hay más combinaciones posibles en una partida de ajedrez que átomos en el universo observable.",
    "La Torre Eiffel puede crecer hasta 15 cm en verano por la expansión del metal con el calor.",
    "Los caracoles pueden dormir hasta tres años seguidos si las condiciones ambientales no son favorables.",
    "El código Morse para SOS (· · · — — — · · ·) es un palíndromo sonoro.",
    "Las vacas tienen mejores amigas y se estresan cuando están separadas de ellas."
]

if __name__ == '__main__':
    app.run(debug=True)
