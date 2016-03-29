import numpy as np
from MatrixReader import MatrixReader
from bottle import route, run, template, request, response

DATASETS = {"CCLE": "CCLE_inferred_prot_abundance.tab"}
reader = MatrixReader(DATASETS)

@route('/query_table/<dataset_name>', method='GET')
def query_table(dataset_name):
    """
    GET request where query rows and columns, and datset name
    are put into URL a JSON of the data for those rows and
    columns is returned

    URL form: .../qury_table/dataset_name?rows=row1,row2&cols=col1,col2

    :param dataset_name: Name of datset we are querying
    :return: String that JSON of queried rows and columns
    """
    rows = request.query.rows.split(",")
    cols = request.query.cols.split(",")

    print("rows: " + str(rows))
    print("rows raw: " + request.query.rows)

    print("cols: " + str(cols))
    print("cols raw: " + request.query.cols)

    return reader.get_submatrix(rows, cols, dataset_name)


@route('/get_rows/<dataset_name>', method='GET')
def get_rows(dataset_name):
    """
    GET request to get JSON list of all rows in a dataset

    URL form: .../get_rows/dataset_name

    :param dataset_name: Name of dataset we want rows from
    :return: JSON string of all rows
    """

@route('/get_columns/<dataset_name>', method='GET')
def get_columns(dataset_name):
    """
    GET request to get JSON list of all columns in a dataset

    URL form: .../get_columns/dataset_name

    :param dataset_name: Name of dataset we want column from
    :return: JSON string of all rows
    """

@route('/test/<a_string>', method ='GET')
def test(a_string):
    vals = request.query.vals
    msg = request.query.msg

    return a_string + " " + vals + " " + msg


@route('/foo', method='GET')
def foo():
    return "Foo!" + request.query.msg

def start():
    """
    Starts server
    :return: void
    """
    run(host='0.0.0.0', port=8080,debug=True)

if __name__== "__main__":
    start()
