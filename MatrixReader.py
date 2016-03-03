import pandas as pd
import json


class MatrixReader(object):
    """
    Class for reading from matrices and fetching data from them

    :attributes datasets:   Dictionary that maps dataset names to their
                            pandas dataframe representations
    """

    datasets = None

    def __init__(self, dataset_map):
        """
        Reads in csv files and saves pandas dataframes to memory

        :param dataset_map: Dictionary where keys are dataframe names,
            and values are filepaths to their csv files
        """

    def __remove_duplicates(self, query_rows, query_columns):
        """
        Removes duplicates from rows and columns query

        :param query_rows: Rows to be de-duplicated
        :param query_columns: Columns to be de-duplicated
        :return: tuple where first element is query rows, 2nd is query columns,
            both without duplicates
        """

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

    def get_rows(self, dataset_name):
        """
        Returns set of all the row names in a dataset

        :param dataset_name: String that is name of dataset, should be exactly
            the same as dataset name in datasets instance variable
        :return: List of all row names in dataset_name
        """

    def get_rows_json(self, dataset_name):
        """
        Returns json of all the row names in a dataset

        :param dataset_name: String that is name of dataset, should be exactly
            the same as dataset name in datasets instance variable
        :return: JSON String of all row names in dataset_name
        """

    def get_columns(self, dataset_name):
        """
        Returns set of all the column names in a dataset

        :param dataset_name: String that is name of dataset, should be exactly
            the same as dataset name in datasets instance variable
        :return: List of all column names in dataset_name
        """

    def get_columns_json(self, dataset_name):
        """
        Returns json of all the column names in a dataset

        :param dataset_name: String that is name of dataset, should be exactly
            the same as dataset name in datasets instance variable
        :return: JSON String of all column names in dataset_name
        """
