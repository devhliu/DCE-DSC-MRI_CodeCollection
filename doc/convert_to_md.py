import pandas as pd

df = pd.read_csv('doc/code_contributions_record.csv')
md = df.to_markdown(index=False).replace("(../", "(https://github.com/OSIPI/DCE-DSC-MRI_CodeCollection/tree/develop/")
with open('notebooks/overview_of_code_collection.md', 'w') as f:
    f.write("# Overview of code collection\n\n")
    f.write(md)
