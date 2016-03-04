import json
from bottle import route, run, template, request, response


@route('get_data/<dataset_name>', method='GET')
def get_data(dataset_name):
    """
    GET request where query rows and columns, and datset name
    are put into URL a JSON of the data for those rows and
    columns is returned

    URL form: .../get_data/dataset_name?rows=row1,row2&cols=col1,col2

    :param dataset_name: Name of datset we are querying
    :return: String that JSON of queried rows and columns
    """


@route('get_rows/<dataset_name>', method='GET')
def get_rows(dataset_name):
    """
    GET request to get JSON list of all rows in a dataset

    URL form: .../get_rows/dataset_name

    :param dataset_name: Name of dataset we want rows from
    :return: JSON string of all rows
    """

@route('get_columns/<dataset_name>', method='GET')
def get_columns(dataset_name):
    """
    GET request to get JSON list of all columns in a dataset

    URL form: .../get_columns/dataset_name

    :param dataset_name: Name of dataset we want column from
    :return: JSON string of all rows
    """

@route('test/<a_string>', method ='GET')
def test(a_string):
    vals = request.query.vals

    return template("Values are {{stuff}}", stuff=vals)


@route('/foo', method='GET')
def foo():
    return template("Foo!")

def start():
    """
    Starts server
    :return: void
    """
    run(host='0.0.0.0', port=8080,debug=True)

if __name__== "__main__":
    start()
