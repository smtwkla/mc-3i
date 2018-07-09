import DBC

d=DBC.DBConnector()
t="test1"
rec={"id":1,"name":"PK1", "count": 106}
d.connect()
d.insert(table=t,record=rec)
