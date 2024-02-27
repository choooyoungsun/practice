import numpy as np
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

st.title('#학년 #반 리포트')

"""
# #학년 #반 리포트
"""

option = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [{"data": [820, 823, 901, 934, 956, 1330, 940], "type": "line"}],
}
st_echarts(
    options=option, height="400px",
)
