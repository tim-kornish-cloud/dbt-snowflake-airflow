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
