from MatrixReader import MatrixReader
from bottle import route, run, request

"""
To use this service, fill in the DATASETS variable in the format
<dataset name/key to be used in URL>:<relative filepath of dataset>
"""
DATASETS = {"CCLE": "CCLE_inferred_prot_abundance.tab"}
reader = MatrixReader(DATASETS)


@route('/query_table/<dataset_name>', method='GET')
def query_table(dataset_name):
    """
    GET request where query rows and columns, and datset name
    are put into URL a JSON of the data for those rows and
    columns is returned

    URL form: .../query_table/dataset_name?rows=row1,row2&cols=col1,col2

    :param dataset_name: Name of datset we are querying
    :return: String that JSON of queried rows and columns
    """
    rows = request.query.rows.split(",")
    cols = request.query.cols.split(",")

    return reader.get_json(rows, cols, dataset_name)


@route('/get_rows/<dataset_name>', method='GET')
def get_rows(dataset_name):
    """
    GET request to get JSON list of all rows in a dataset

    URL form: .../get_rows/dataset_name

    :param dataset_name: Name of dataset we want rows from
    :return: JSON string of all rows
    """
    return reader.get_rows_json(dataset_name)


@route('/get_columns/<dataset_name>', method='GET')
def get_columns(dataset_name):
    """
    GET request to get JSON list of all columns in a dataset

    URL form: .../get_columns/dataset_name

    :param dataset_name: Name of dataset we want column from
    :return: JSON string of all rows
    """
    return reader.get_columns_json(dataset_name)


def start():
    """
    Starts server
    :return: void
    """
    run(host='0.0.0.0', port=8080,debug=True)


if __name__== "__main__":
    start()
