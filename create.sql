CREATE STAGE multi_page_stage;

CREATE STREAMLIT multi_page_app
ROOT_LOCATION=@multi-page-stage
MAIN_FILE='/streamlit_app.py'
WAREHOUSE=REGRESS;

PUT file://<path-to-directory>/pages/tpch_demo.py @DB_NAME.SCHEMA_NAME.multi_page_stage/pages/ overwrite=true auto_compress=false;
PUT file://<path-to-directory>/pages/plotting_demo.py @DB_NAME.SCHEMA_NAME.multi_page_stage/pages/ overwrite=true auto_compress=false;
PUT file://<path-to-directory>/pages/dataframe_demo.py @DB_NAME.SCHEMA_NAME.multi_page_stage/pages/ overwrite=true auto_compress=false;
