show grants on warehouse dbt_warehouse;

grant usage on warehouse dbt_warehouse to role dbt_role;

grant all on database dbt_db to role dbt_role;

grant all on schema dbt_db.dbt_schema to role dbt_role;

GRANT ROLE dbt_role TO USER tlkornish;