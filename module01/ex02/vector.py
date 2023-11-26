class Vector:
    def __init__(self, input_data):
        if isinstance(input_data, int):
            self.values = [[float(i)] for i in range(input_data)]
            self.shape = (input_data, 1)
        elif isinstance(input_data, list):
            if all(isinstance(row, list) and len(row) == 1 for row in input_data):
                self.values = input_data
                self.shape = (len(input_data), 1)
            elif all(isinstance(row, list) and len(row) > 1 for row in input_data):
                self.values = [row[:] for row in input_data]
                self.shape = (1, len(input_data[0]))
            else:
                raise ValueError("Invalid input for Vector")
        elif isinstance(input_data, tuple) and len(input_data) == 2:
            start, end = input_data
            self.values = [[float(i)] for i in range(start, end + 1)]
            self.shape = (end - start + 1, 1)
        else:
            raise ValueError("Invalid input for Vector")
    

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for addition")

        result_values = []
        for x, y in zip(self.values, other.values):
            result_values.append([x[0] + y[0]])

        return Vector(result_values)
    
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            result_values = [[x[0] + other] for x in self.values]
            return Vector(result_values)
        else:
            raise ValueError("Invalid operation: Cannot perform addition with non-scalar types")


    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for addition")

        result_values = []
        for x, y in zip(self.values, other.values):
            result_values.append([x[0] - y[0]])
        return Vector(result_values)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            result_values = [[other - x[0]] for x in self.values]
            return Vector(result_values)
        else:
            raise ValueError("Invalid operation: Cannot perform addition with non-scalar types")


    def __mul__(self, scalar):
        result_values = [[x[0] * scalar] for x in self.values]
        return Vector(result_values)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result_values = [[x[0] / scalar] for x in self.values]
        return Vector(result_values)

    def __rtruediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if 0 in (x[0] for x in self.values):
                raise ZeroDivisionError("Division by zero is not allowed")
            result_values = [[scalar / x[0]] for x in self.values]
            return Vector(result_values)
        else:
            raise ValueError("Invalid operation: Cannot perform division with non-scalar types")


    def __repr__(self):
        return str(self.values)

    def __str__(self):
        return str(self.values)

    def dot(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for dot product")
        result = sum(x[0] * y[0] for x, y in zip(self.values, other.values))
        return result

    def T(self):
        result_values = [[x for x in row] for row in zip(*self.values)]
        if self.shape == (1, len(self.values[0])):
            return Vector(result_values)
        elif self.shape == (len(self.values), 1):
            return Vector(result_values).reshape((1, len(self.values)))

    def test_column_vector_transpose(self):
        v = Vector([[1], [2], [3]])
        result = v.T()
        expected_values = [[1, 2, 3]]
        self.assertEqual(result.values, expected_values)

    def test_row_vector_transpose(self):
        v = Vector([[1, 2, 3]])
        result = v.T()
        expected_values = [[1], [2], [3]]
        self.assertEqual(result.values, expected_values)




if __name__ == '__main__':
    v = Vector(5)
    print(v.values)
    print(v.shape)
    v = Vector([[1.0, 2.0, 3.0]])
    print(v.values)
    print(v.shape)
    v = Vector([[1.0], [2.0], [3.0]])
    print(v.values)
    print(v.shape)
    v = Vector((10, 15))
    print(v.values)
    print(v.shape)