## Creating Database

On the postgres shell write the following commands:
```
CREATE DATABASE bet_365;
create user bet_365_admin with encrypted password 'bet365admin';
grant all privileges on database bet_365 to bet_365_admin;
```