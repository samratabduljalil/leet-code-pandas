import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    select_data=students.loc[students['student_id']==101]
    df= select_data[['name','age']]
    return df
    