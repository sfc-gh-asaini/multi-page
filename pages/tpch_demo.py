import streamlit as st
from snowflake.snowpark.context import get_active_session

st.title("TPC_H Summary Stats :balloon:")

session = get_active_session()


st.header('TPC-H data')

st.subheader('Tables')
sql = "SHOW TABLES IN snowflake_sample_data.tpch_sf1"
data = session.sql(sql).collect()
st.write(data)

st.subheader('Count of rows')
sql = "select count(*) from snowflake_sample_data.tpch_sf1.lineitem"
data = session.sql(sql).collect()
st.write(data)


st.subheader('Top 20 rows')
sql = f"select * from snowflake_sample_data.tpch_sf1.lineitem limit 200"
data = session.sql(sql).collect()
st.write(data)
