# Data Validation Using Pandera

This demonstrates the use of `pandera` Python data validation library. Official documentation can be found here:
https://pandera.readthedocs.io

As an example, Nashville Housing dataset will be used, and a data validation report in Excel format will be generated.


## Setting up the Development Environment
* Install `poetry` https://python-poetry.org/docs/
* Setup environment variables
* Install the project dependencies by running the command `poetry add`
(pandas, matplotlib, pandera, black, pyyaml, frictionless, openpyxl)

## Running the Scripts
* Run the following to generate the validation schema python script:
`poetry run python nashville_housing_data_validation/create_schema.py`
* Update the preliminary schema script with the necessary checks
* Run the following to run the dataset validation against the schema:
`poetry run python nashville_housing_data_validation/validate.py`

## Notes
* Null values will be excluded from the schema check
