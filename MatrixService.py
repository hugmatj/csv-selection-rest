from MatrixReader import MatrixReader
from bottle import route, run, request

"""
To use this service, fill in the DATASETS variable in the format
<dataset name/key to be used in URL>:<relative filepath of dataset>
"""
DATASETS = {"CCLE_protein": "CCLE_inferred_prot_abundance.tab"}
reader = MatrixReader(DATASETS)


# Custom URLs
@route('/context/expression/cell_line/samples_available', method='GET')
def get_rows():
    """
    GET request to get JSON list of all available cell-lines

    :return: JSON list string of all cell-lines
    """
    return reader.get_rows_json("CCLE_protein")


@route('/context/expression/cell_line/ids_available', method='GET')
def get_columns():
    """
    GET request to get JSON list of all available gene ids

    :return: JSON list string of all gene ids
    """
    return reader.get_columns_json("CCLE_protein")


@route('/context/expression/cell_line', method='GET')
def get_abundance():
    """
    GET request where query rows and columns, and datset name
    are put into URL a JSON of the data for those rows and
    columns is returned

    URL: .../context/expression/cell_line?cells=cell1,cell2&genes=gene1,gene2

    :param dataset_name: Name of datset we are querying
    :return: String that JSON of queried rows and columns
    """
    rows = request.query['cells'].split(",")
    cols = request.query['genes'].split(",")

    return reader.get_json(rows, cols, 'CCLE_protein')


def start():
    """
    Starts server
    :return: void
    """
    run(host='0.0.0.0', port=8080,debug=True)


if __name__== "__main__":
    start()
