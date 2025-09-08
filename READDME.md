# set up a snowflake db and dbt role

## Snowflake setup

1) using accountadmin
2) create warehouse
3) create database in warehosue
4) create role
5) grant usage of warehouse to role
6) using role, create a schema in db


### initialize dbt

```code
~$ dbt init
```
- name project: data_pipeline
- choose a database flavor: 2 for snowflake
- for account, get locator tag, copy and paste to console
- enter password
- set role: dbt_role
- set warehouse dbt_warehouse
- set database: dbt_db
- set schema dbt_db
- threads: 10

```code
~$ cd data_pipeline
~$ code .
```

### set up package.yml and dbt_project.yml

1) modify dbt_project.yml
 - add the following under the models: 
models: 
  data__pipeline:
    staging:
      +materialized: view
      snowflake_warehouse: dbt_warehouse
    marts:
      +materialized: table
      snowflake_warehouse: dbt_warehouse


2) running sql scripts:

run script: stg_tpch_line_item.sql

```code
dbt run -s stg_tpch_line_item
```

3) running tests

run any test in current directory

```code
dbt test
```

## current issue running Dag in airflow

since my main computer wsl doesn't work due the use having whitespace,
I'm trying to run this on windows, which does not work for airflow. 
Everything else connecting to snowflake works so far.

Going to set a new user on computer for developing in wsl2-ubuntu