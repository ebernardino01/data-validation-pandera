from pathlib import Path

import pandas as pd
import pandera as pa

from schema.inferred_schema import schema


# Load raw dataset from google drive
df = pd.read_csv('https://drive.google.com/uc?export=download&id=1CVd4-SWMIfYE84clp50taqTjQGnL5zll')

try:
    # Validate the dataframe with the generated schema
    schema.validate(df, lazy=True)
except pa.errors.SchemaErrors as exc:
    error_columns = exc.failure_cases['column'].unique()
    error_dict = {
        column: exc.failure_cases[exc.failure_cases['column'] == column]['column'].count() \
            for column in list(error_columns)
    }

    # Save the validation errors in a markdown format
    validation_contents = (
        f'''Columns and Error Counts:\n'''
        f'''{error_dict}'''
    )

    print(validation_contents)
    validation_file = Path(Path.cwd() / 'validation/validation_results.xlsx')
    validation_file.touch()
    with pd.ExcelWriter(validation_file) as writer:
        exc.failure_cases.to_excel(writer, sheet_name='Error_Details')
