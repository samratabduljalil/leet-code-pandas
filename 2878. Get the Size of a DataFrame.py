import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df=players
    row,col= df.shape
    return[row,col]
    