import pandas as pd
import json


class MatrixReader(object):
    """
    Class for reading from matrices and fetching data from them

    :attributes datasets:   Dictionary that maps dataset names to their
                            pandas dataframe representations
    """

    datasets = None

    def __init__(self, dataset_map, sep_char='\t'):
        """
        Reads in csv files and saves pandas dataframes to memory

        :param dataset_map: Dictionary where keys are dataframe names,
            and values are filepaths to their csv files
        :param sep_char: Character used to separate elements in data, tab by
            default
        """
        for name in dataset_map:
            self.datasets[name] = pd.read_csv( dataset_map[name], sep=sep_char,
                index_col=0)

    # TODO Maybe change to static method or remove self param
    def __remove_duplicates(self, query_rows, query_columns):
        """
        Removes duplicates from rows and columns query

        :param query_rows: Rows to be de-duplicated
        :param query_columns: Columns to be de-duplicated
        :return: tuple where first element is query rows, 2nd is query columns,
            both without duplicates
        """
        return set(query_rows), set(query_columns)

    def __check_validity(self, query_rows, query_columns, dataset_name):
        """
        Checks if query parameters are contained in dataset.
        If not, removes invalid elements and returns pruned parameters

        :param query_rows: List of desired rows
        :param query_columns: List of desired columns
        :param dataset_name: String that is name of dataset we want, should be
            exactly the same as dataset name in datasets instance variable
        :return: Tuple where 1st element is pruned query rows,
            and second element is pruned query columns
        """
        table = self.datasets[dataset_name]
        new_query_rows = []
        new_query_columns = []

        # Get pruned list of query rows
        for row in query_rows:
            if row in table.index:
                new_query_rows.append(row)
            else:
                print("Row " + row + " not found, skipping")
                continue

        # Get pruned list of query columns
        for column in query_columns:
            if colunm in table.columns:
                new_query_columns.append(column)
            else:
                print("Column " + column + " not found, skipping")
                continue

        return new_query_rows, new_query_columns

    def get_submatrix(self, query_rows, query_columns, dataset_name):
        """
        Queries specified dataset for particular rows and columns and returns
        a submatrix of just those rows and columns.

        :param query_rows: Rows that are desired from dataset
        :param query_columns: Columns that are desired from dataset
        :param dataset_name: String that is name of dataset we want, should be
            exactly the same as dataset name in datasets instance variable
        :return: Pandas dataframe of only queried rows and columns
        """
        # Get table we are querying
        table = self.datasets[dataset_name]
        output_table = pd.DataFrame()

        # Clean query
        (query_rows, query_columns) = \
            self.__remove_duplicates(query_rows, query_columns)
        (query_rows, query_columns) = \
            self.__check_validity(query_rows, query_columns, dataset_name)

        return table[query_rows,query_columns]

    def get_json(self, query_rows, query_columns, dataset_name):
        """
        Queries specified dataset for particular rows and columns and returns
        a json representation of a submatrix of just those rows and columns.

        :param query_rows: Rows that are desired from dataset
        :param query_columns: Columns that are desired from dataset
        :param dataset_name: String that is name of dataset we want, should be
            exactly the same as dataset name in datasets instance variable
        :return: Json string of only queried rows and columns
        """
        output_table = self.get_submatrix(query_rows, query_columns,
                                          dataset_name)
        return output_table.to_json(orient="index")

    def get_rows(self, dataset_name):
        """
        Returns set of all the row names in a dataset

        :param dataset_name: String that is name of dataset, should be exactly
            the same as dataset name in datasets instance variable
        :return: List of all row names in dataset_name
        """
        return self.datasets[dataset_name].index

    def get_rows_json(self, dataset_name):
        """
        Returns json of all the row names in a dataset

        :param dataset_name: String that is name of dataset, should be exactly
            the same as dataset name in datasets instance variable
        :return: JSON String of all row names in dataset_name
        """
        return json.dumps(list( self.datasets[dataset_name].index ))

    def get_columns(self, dataset_name):
        """
        Returns set of all the column names in a dataset

        :param dataset_name: String that is name of dataset, should be exactly
            the same as dataset name in datasets instance variable
        :return: List of all column names in dataset_name
        """
        return self.datasets[dataset_name].columns

    def get_columns_json(self, dataset_name):
        """
        Returns json of all the column names in a dataset

        :param dataset_name: String that is name of dataset, should be exactly
            the same as dataset name in datasets instance variable
        :return: JSON String of all column names in dataset_name
        """
        return json.dumps(list( self.datasets[dataset_name].columns ))
