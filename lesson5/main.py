import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit introduction")
st.write("DataFrame")

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ["lat", "lon"],
)
st.map(df)

# st.table(df.style.highlight_max(axis=0))

# """
# # 1st line
# ## 2nd line
# ### 3rd line

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

