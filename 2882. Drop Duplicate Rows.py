import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df_with_no_duplicate=customers.drop_duplicates(subset=['email'])
    return df_with_no_duplicate
    