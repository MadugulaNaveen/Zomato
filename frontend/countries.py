import os
import pandas as pd
from django.templatetags.static import static
from django.conf import settings

Excelpath =os.path.join(settings.BASE_DIR,'static','Data','Country-Code.xlsx')
df = pd.read_excel(Excelpath, header=None)
data_dict = dict(zip(df.iloc[1:, 1],df.iloc[1:, 0]))
