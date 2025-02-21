class Matrix:
    def __init__(self, rows, cols, fill=0):
        self.rows = rows
        self.cols = cols
        self.data = [[fill for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self, idx, value):
        self.data[idx] = value

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumar.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self[i][j] + other[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sustraer.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self[i][j] - other[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Las matrices deben tener las dimensiones adecuadas para multiplicar.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self[i][k] * other[k][j]
        return result

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

def read_matrix(rows, cols):
    matrix = Matrix(rows, cols)
    for i in range(rows):
        while True:
            row = input(f"Ingrese los valores de la fila {i+1} separados por espacios: ").split()
            if len(row) != cols:
                print(f"Introduzca exactamente valores de {cols}.")
            else:
                break
        for j in range(cols):
            matrix[i][j] = int(row[j])
    return matrix

# Example usage
if __name__ == "__main__":
    try:
        rows, cols = map(int, input("Ingrese el número de filas y columnas para las matrices separadas por espacios:").split())
    except ValueError:
        print("Introduzca dos números enteros separados por espacios.")
        exit(1)
    
    print("Introduzca valores para la Matriz A:")
    A = read_matrix(rows, cols)
    
    print("Introduzca valores para la Matriz B:")
    B = read_matrix(rows, cols)

    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    print("\nA + B:")
    print(A + B)

    print("\nA - B:")
    print(A - B)

    print("\nA * B:")
    print(A * B)