import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'age':'age_in_years','id':'student_id','first':'first_name','last':'last_name'},inplace=True)
    return students