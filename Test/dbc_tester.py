import DBC
import os

os.chdir("..")

d = DBC.DBConnector()
t = "test1"
#rec = {"id": 1, "nasdfme": "PK1", "count": 106}
rec = {"naaame": "APK1-1", "count":10006}
condition = "id=16"
d.connect()
#d.insert(table=t, record=rec)
#d.update(t,rec,condition)

delcond = "ISNULL(id)"
#d.delete(t,"asd=1")

fld = "id, name, count"
where = "name='APK-2'"
grp = "id"
ord = "id"
c = d.select(t,fld, condition=where, group_by=None, limit="10")
r=c.fetchall()
print(r)
