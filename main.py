# How to replace None with NaN in Pandas DataFrame

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "Name": [
            "Alice",
            "Bobby Hadz",
            "Carl",
            None
        ],
        "Age": [29, 30, None, 32],
    }
)

print(df)

df = df.fillna(value=np.nan)

print('-' * 50)

print(df)