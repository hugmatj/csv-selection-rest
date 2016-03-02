import pandas as pd

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

    def __remove_duplicates(self, rows_query, columns_query):
        """
        Removes duplicates from

        :param rows:
        :param columns:
        :return:
        """