import random
import matplotlib.pyplot as plt
from matplotlib import animation, rc
rc('animation', html='html5')

# función inicial con los parámetros de la cuadrícula
def init(Nx= 50,Ny=50):
    """
    Inicializa la cuadrícula con valores aleatorios de 0 y 1.

    Args:
        Nx (int): Número de columnas (por defecto 50).
        Ny (int): Número de filas (por defecto 50).

    Returns:
        list: Matriz (Ny+2)x(Nx+2) con valores 0 o 1, incluyendo bordes.
    """
    C = [[0 for j in range(Ny+2)] for i in range(Ny+2)]
    for i in range(1,Ny+1):
        for j in range(1,Nx+1):
            C[i][j] = random.randint(0,1)
    return C

# función para el color, quitar axis y pintar cuadrícula
def plot(C):
    """
    Muestra la cuadrícula usando matplotlib en una escala de grises.

    Args:
        C (list): Matriz que representa el estado del sistema.
    """
    plt.imshow(C, cmap="gray")
    plt.axis("off")
    plt.show()

# función de la iteracción por columna y línea con las comprobaciones de los vecinos vivos y muertos
def iter(C,):
    """
    Realiza una iteración del juego de la vida de Conway.

    Args:
        C (list): Matriz actual con el estado de cada celda.

    Returns:
        list: Nueva matriz tras aplicar las reglas del juego.
    """
    Ny, Nx = len(C) - 2, len(C[0]) - 2
    C2 = [[0 for j in range(Ny+2)] for i in range(Ny+2)]
    for i in range(1,Ny+1):
        for j in range(1,Nx+1):
            c = C[i][j]
            v = C[i][j+1] + C[i][j-1] + C[i-1][j] + C[i+1][j] + \
                C[i+1][j+1] + C[i+1][j-1] + C[i-1][j+1] + C[i-1][j-1]
   
            if c == 0:
                if v == 3:
                    C2[i][j] = 1
                else:
                    C2[i][j] = 0
            else:
                if v == 2 or v == 3:
                    C2[i][j] = 1
                else:
                    C2[i][j] = 0
    return C2

# función bucle del juego con el máximo de iteraciones
def game(C, MAX_IT = 1000):
    """
    Ejecuta múltiples iteraciones del juego y almacena los resultados.

    Args:
        C (list): Estado inicial de la cuadrícula.
        MAX_IT (int): Número máximo de iteraciones (por defecto 1000).

    Returns:
        list: Lista de matrices que representan la evolución del sistema.
    """
    count = 0
    Cs = [C]
    while count < MAX_IT:
        C = iter(C)
        Cs.append(C)
        C0 = C
        count += 1
    return Cs

# función para animar la cuadrícula 
def update(i):
    """
    Actualiza el gráfico para la animación en el frame i.

    Args:
        i (int): Índice del frame actual.

    Returns:
        AxesSubplot: El eje actualizado.
    """
    ax.clear()
    ax.imshow(Cs[i], cmap="gray")
    ax.axis('off')
    return ax

C = init()
Cs = game(C)
fig = plt.figure(figsize=(5,5))
ax = plt.subplot(1,1,1)

anim = animation.FuncAnimation(fig, update, frames=len(Cs), interval=100)

plt.show()

