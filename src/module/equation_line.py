def equation_line(scope, x, y):
    x_coord = [scope[0][x], scope[-1][x]]
    y_coord = [scope[0][y], scope[-1][y]]
    return x_coord, y_coord
