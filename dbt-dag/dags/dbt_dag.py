import os
from datetime import datetime

# import cosmos classes to interact dbt and snowflake with airflow
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

# set up profile configuration for snowflake connection
profile_config = ProfileConfig(
    profile_name = "default",
    target_name = "dev",
    profile_mapping = SnowflakeUserPasswordProfileMapping(
        conn_id = "snowflake_conn",
        profile_args = {"database" : "dbt_db",
                        "schema" : "dbt_schema"}
    )
)

# set up project configuration with location of dbt in dabgs folder
dbt_snowflake_dag = DbtDag(
    project_config = ProjectConfig("C:\\Users\\John Cena\\Documents\\Github\\dbt-snowflake-airflow\\dbt-dag\\dags\\data_pipeline\\"),
    operator_args = {"install_deps" : True},
    profile_config = profile_config,
    execution_config = ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"),
    schedule = "@daily",
    start_date = datetime(2025, 9, 7),
    catchup = False,
    dag_id = "dbt_dag"
)