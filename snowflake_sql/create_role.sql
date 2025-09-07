use role accountadmin;

create warehouse dbt_warehouse with warehouse_size = 'x-small';

create database if not exists dbt_db;

create role if not exists dbt_role;