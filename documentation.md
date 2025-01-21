-- UI 
Kafka Connect = http://localhost:8000/
-> To create a connectors ( mysql,postgres,ssms)
  -> You can use postgresConnection.json example to create connectors from postman using (http://localhost:8083/connectors) as Post Request


Kafka UI = http://localhost:9000/

Rest API ( use post man To trigger)
Debezium = http://localhost:8083/ 

 -> To add value 
POST: http://localhost:8083/connectors/  
-> To delete the connecTor 
DELETE : http://localhost:8083/connecTors/mysql-school-connecTor 
-> To get listed connecTors
GET : http://localhost:8083/connecTors/ 
-> To get connecTor status 
GET : http://localhost:8083/connecTors/mysql-school-connecTor/status 
-> To get insantance records
POST: http://localhost:8082/consumers/my-group/instances/my-instance/records 