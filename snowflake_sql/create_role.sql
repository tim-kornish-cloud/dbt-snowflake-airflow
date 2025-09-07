use role accountadmin;

create warehouse dbt_warehouse with warehouse_size = 'x-small';

create database dbt_db;

create role dbt_role;