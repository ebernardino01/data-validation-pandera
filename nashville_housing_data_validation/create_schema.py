from pathlib import Path

import pandas as pd
import pandera as pa


# Load template data to dataframe
df = pd.read_csv('https://drive.google.com/uc?export=download&id=19-cKFUsdawpcNZYUkMTK4bJ0evM7Ubr5')

# Generate validation schema from the dataframe
schema = pa.infer_schema(df).to_script()

# Save the generated schema
schema_file = Path(Path.cwd() / 'schema/inferred_schema.py')
schema_file.touch()
schema_file.write_text(schema)
