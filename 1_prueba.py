
import matplotlib.pyplot as plt

# 1) Carga los datos desde el archivo JSON

# 2) Ordena los datos por el valor de 'x' en orden descendente

# 3) Asigna un valor de opacidad ( 0 a 100% ) a cada valor de z obtenidos en el paso 2


# 4) Filtra los datos por el valor de 'z' y agrega un nuevo valor llamado 'tipo' usando la funcion filterd_z


def filterd_z(filt: str) -> list:
    """
    Consejo de la función (implementala como desees):
    La función filtra una lista de diccionarios en función de un valor específico para la clave 'z' y
    agrega un nuevo 'tipo' de clave con un valor correspondiente de un diccionario predefinido.

    :param filt: El parámetro "filt" se utiliza para especificar el valor de la clave 'z' por la que
    desea filtrar los datos
    :return: una matriz JSON que contiene elementos de la matriz "datos" donde el valor de la clave "z"
    coincide con el filtro proporcionado. Cada elemento de la matriz JSON devuelta también incluye un
    nuevo "tipo" de par clave-valor al que se le asigna el valor de la opacidad en función del
    valor "z".
    """
    pass


# 5) Completa el siguiente for
for idx in range(1, 11):
    filtered_data = filterd_z(idx)
    # Crea los arrays de valores para el eje x y el color
    x = []
    # Asumiendo que 'y' es otra columna en tus datos
    y = []
    color = []  # opacidades

    # Grafica los datos
    for xi, yi, ci in zip(x, y, color):
        plt.scatter(xi, yi, color=ci)
plt.show()

# En resumen, este codigo debe graficar los datos en un scatter
# pero si deseas hacerlo en tu propia logica puedes hacerlo

