import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit introduction")
st.write("Show Progress Bar")
# st.sidebar.write("Sidevar widgets")
"Start!"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)


left_column, right_column = st.columns(2)
button = left_column.button("Show Right Column")
if button:
    right_column.write("This is the right column")

expander1 = st.expander("Contact1")
expander1.write("Write information")
expander2 = st.expander("Contact2")
expander2.write("Write information")
expander3 = st.expander("Contact3")
expander3.write("Write information")

if st.checkbox("Show Image"):
    img = Image.open("aircraft.jpg")
    st.image(img, caption="aircraft", use_column_width=True)

# option = st.sidebar.selectbox(
#     "Select number",
#     list(range(1, 10))
# )

# "Your favorite number is", option

# option2 = st.sidebar.text_input("Input your hobby.")
# "Your hobby is ", option2

# option3 = st.sidebar.slider("How are you doing?", 0, 100, 50)
# "Your condition is ", option3

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

