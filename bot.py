"""Дополнительный модуль: искусственный интеллект."""

# импорт дополнительных модулей
import data
import functions


# переменные модуля
# только для поля 3х3
sm_cross = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
sm_zero = [[2, 0, 2], [0, 1, 0], [2, 0, 2]]



def easy() -> data.TurnCoords:
    """Рассчитывает координат ячейки поля для текущего хода бота для низкого уровня сложности."""


def hard(token_index: int) -> data.TurnCoords:
    """Рассчитывает координат ячейки поля для текущего хода для высокого уровня сложности."""
    tw = weights_tokens(data.TURNS, token_index)
    ew = weights_empty(tw)
    sw = matrix_add((sm_cross, sm_zero)[token_index], ew)
    weights_clear(tw, sw)
    return matrix_max_indexes(sw)


def weights_tokens(board: data.Matrix, token_index: int) -> data.Matrix:
    """Конструирует и возвращает матрицу весов занятых ячеек игрового поля."""
    tokensweights = [[0]*data.DIM for _ in data.RANGE]
    for i in data.RANGE:
        for j in data.RANGE:
            if functions.is_cross(board[i][j]):
                tokensweights[i][j] = data.WEIGHTS[token_index]
            elif functions.is_zero(board[i][j]):
                tokensweights[i][j] = data.WEIGHTS[token_index-1]
    return tokensweights


def weights_empty(tokensweights: data.Matrix):
    """Вычисляет и возвращает матрицу весов пустых ячеек игрового поля."""
    emptyweights = [[0]*data.DIM for _ in data.RANGE]
    for i in data.RANGE:
        for j in data.RANGE:
            if tokensweights[i][j] == 0:
                row = get_matrix_row(tokensweights, i)
                if len(set(row) - {0}) < 2:
                    emptyweights[i][j] += sum(row)**2
                column = get_matrix_column(tokensweights, j)
                if len(set(column) - {0}) < 2:
                    emptyweights[i][j] += sum(column)**2
                diags = get_matrix_diagonals(tokensweights, i, j)
                for diag in diags:
                    if len(set(diag) - {0}) < 2:
                        emptyweights[i][j] += sum(diag) ** 2
                emptyweights[i][j] = int(emptyweights[i][j])
    return emptyweights


def weights_clear(tokensweights: data.Matrix, solvingweights: data.Matrix) -> None:
    """Обрабатывает матрицу принятия решения, приравнивая к нолю элементы, соответствующие занятым на поле клеткам."""
    for i in data.RANGE:
        for j in data.RANGE:
            if tokensweights[i][j] != 0:
                solvingweights[i][j] = 0


def matrix_add(matrix1: data.Matrix,
               matrix2: data.Matrix,
               *matrices: data.Matrix) -> data.Matrix:
    """Поэлементно складывает переданные матрицы и возвращает результирующую матрицу."""
    matrices = (matrix1, matrix2) + matrices
    result_matrix = [[0]*data.DIM for _ in data.RANGE]
    for matrix in matrices:
        for i in data.RANGE:
            for j in data.RANGE:
                result_matrix[i][j] = matrix[i][j]
    return result_matrix


def matrix_max_indexes(matrix: data.Matrix) -> data.TurnCoords:
    """Находит наибольший элемент в матрице и возвращает индексы этого элемента в виде кортежа."""
    m, i_m, j_m = 0, 0, 0
    for i in data.RANGE:
        for j in data.RANGE:
            if m < matrix[i][j]:
                m = matrix[i][j]
                i_m, j_m = i, j
    return i_m, j_m


def get_matrix_row(matrix: data.Matrix, row_index: int) -> data.Series:
    """Возвращает последовательность с элементами ряда матрицы по индексу ряда."""
    return matrix[row_index]


def get_matrix_column(matrix: data.Matrix, column_index: int) -> data.Series:
    """Возвращает последовательность с элементами столбца матрицы по индексу столбца."""
    return [row[column_index] for row in matrix]


def get_matrix_diagonals(matrix: data.Matrix,
                         row_index: int,
                         column_index: int) -> tuple[data.Series, data.Series]:
    """Возвращает кортеж последовательностей с элементами главной и побочной диагоналей матрицы по индексам ряда и столбца."""
    if row_index == column_index:
        main_diag = [matrix[i][i] for i in data.RANGE]
    else:
        main_diag = []
    if row_index == data.DIM - column_index - 1:
        anti_diag = [matrix[i][data.DIM-i-1] for i in data.RANGE]
    else:
        anti_diag = []
    return main_diag, anti_diag



# тестирование функций модуля
if __name__ == '__main__':
    pass
