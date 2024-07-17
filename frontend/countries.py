import pandas as pd
df = pd.read_excel('/Users/naveenm/Coding/placementDrives/task-MadugulaNaveen/Country-Code.xlsx', header=None)
data_dict = dict(zip(df.iloc[1:, 1],df.iloc[1:, 0]))
