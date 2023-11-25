




class Vector:
    def __init__(self, input):
        if isinstance(input,int):
            self.values = [float(x) for x in range(input)]
            self.shape = (input, 1)
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
     
