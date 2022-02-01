def make_table(data, num_cols):
    """
    Create two dimensional list
    Inputs:
    data - 1-dimensional sequence
    num_cols - number of columns in the table to be created
    """

    table = []

    while data:
        table.append([])
        cols = num_cols if len(data) >= num_cols else len(data)

        for col in range(cols):
            table[-1].append(': '.join(data.pop(0)))

    return table


def format_table(table, formatted_table):
    widths = column_widths(table)

    for row in table:
        num_cols = len(row)

        template = make_row_template(num_cols)

        line = template.format(*row, **widths)

        formatted_table.append(line)

    return '\n'.join(formatted_table)


def column_widths(table):
    """
    Get the minimum width for each column in a table
    INPUTS:
    table - 2 dimensional list of values
    """
    num_cols = len(table[0])
    col_widths = {}
    for col_num in range(num_cols):
        column = extract_column(col_num, table)

        col_width = len(max(column, key=len)) + 4
        col_widths['w%d' % (col_num + 1)] = col_width
    return col_widths


def extract_column(col_num, table):
    """
    Extract a list representing a column from 2
    dimensional list
    INPUTS:
    col_num - determines which item in the row will be
              extracted
    table -   2 dimensional list. Each inner list represents
              one 1 row in the table
    """
    column = []
    for row in table:
        if len(row) - 1 >= col_num:
            column.append(str(row[col_num]))
    return column


def make_row_template(num_cols):
    """
    Generate a formatting template for inserting table
    rows
    """
    cell_template = '|{{:<{{w{num}}}}}|'
    template = ''

    for i in range(1, num_cols + 1):
        template += cell_template.format(num=i)
    return template
