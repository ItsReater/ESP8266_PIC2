import streamlit as st
import pandas as pd
import numpy as np

df_plc1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
df1_plc1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

df_plc2 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
df1_plc2 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

humidity_plc1 = pd.DataFrame(
    {
        "datetime": np.random.randn(20),
        "humidity 1 [%]": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20)
    }
)

humidity_plc2 = pd.DataFrame(
    {
        "datetime": np.random.randn(20),
        "humidity 2 [%]": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20)
    }
)

temperature_plc1 = pd.DataFrame(
    {
        "datetime": np.random.randn(20),
        "temperature 1 [ºC]": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20)
    }
)

temperature_plc2 = pd.DataFrame(
    {
        "datetime": np.random.randn(20),
        "temperature 2 [ºC]": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20)
    }
)

st.title("PLC Data Visualization")

st.write("Select PLC")

plc_selected = st.selectbox("Select PLC",("PLC 1","PLC 2")) # Se puede usar on_change o option == "PLC 1 o 2"

plot_format = st.radio("Select view:",["Graphics","Data Table"])

if plc_selected == "PLC 1":
    st.write(f"Showing data for {plc_selected}")
    if plot_format == "Graphics":
        st.line_chart(humidity_plc1, x="datetime", y="humidity 1 [%]", color="col3")
        st.line_chart(temperature_plc1, x="datetime", y="temperature 1 [ºC]", color="col3")
    else:
        st.dataframe(df_plc1)  # Same as st.write(df)
        st.dataframe(df1_plc1)  # Same as st.write(df)
else:
    st.write(f"Showing data for {plc_selected}")
    if plot_format == "Graphics":
        st.line_chart(humidity_plc2, x="datetime", y="humidity 2 [%]", color="col3")
        st.line_chart(temperature_plc2, x="datetime", y="temperature 2 [ºC]", color="col3")
    else:
        st.dataframe(df_plc2)  # Same as st.write(df)
        st.dataframe(df1_plc2)  # Same as st.write(df)