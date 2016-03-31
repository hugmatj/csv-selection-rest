# csv-selection-rest
## Turn a csv into a REST service
This is a small python tool to allow access of values from a csv file via a GET request.

### Tutorial
1. Identify desired files
2. Change `DATASETS` variable in MatrixService.py to map each csv to a key to be used in the request URL un the format "<dataset name/key to be used in URL>:<relative filepath of dataset>"
3. `python MatrixService.py` to run the service on `0.0.0.0:8080'
4. Service is up and running!

To get values from the table type: `0.0.0.0:8080/query_table/<dataset_name>?rows=row1,row2&cols=col1,col2` into URL of a browser, where row1, col1 etc. represent the row and column names of your desired values from the csv.

To get a list of all row names, type into the URL: `0.0.0.0:8080/get_rows/<dataset_name>` 
To get a list of all column names, type into the URL: `0.0.0.0:8080/get_columns/<dataset_name>` 

### Input
CSV files should have a header row with column names, and an index column with row names.

**Note: Default seperation value is actually a tab, change `sep_char='\t'` on line 15 of MatrixReader.py to change this**

### Output
query_table outputs json in the following format (suppose query rows and columns are named row1, col1, etc.):

```json
{
	"row1": {
			"col1":value,
			"col2":value
	}
	"row2": {
			"col1":value,
			"col2":value
	}
}
```

get_rows and get_columns output is `["row1", "row2", "row3"]` or `["col1", "col2", "col3"]`