import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit introduction")
st.write("DataFrame")

df = pd.DataFrame(
    np.random.rand(20, 4),
    columns = ["a", "b", "c", "d"],
)
st.bar_chart(df)

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

