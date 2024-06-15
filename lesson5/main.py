import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit introduction")
st.write("Display Image")
st.sidebar.write("Sidevar widgets")

if st.sidebar.checkbox("Show Image"):
    img = Image.open("aircraft.jpg")
    st.image(img, caption="aircraft", use_column_width=True)

option = st.sidebar.selectbox(
    "Select number",
    list(range(1, 10))
)

"Your favorite number is", option

option2 = st.sidebar.text_input("Input your hobby.")
"Your hobby is ", option2

option3 = st.sidebar.slider("How are you doing?", 0, 100, 50)
"Your condition is ", option3

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

