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