import DBC
import os

os.chdir("..")

d = DBC.DBConnector(conf="conf/")
d.connect()


# #rec = {"id": 1, "nasdfme": "PK1", "count": 106}

# condition = "id=16"

t = "3i_Rules"
for i in range(1, 10000):
    rec = {"RuleName": "Rule"+str(i), "Topic": "Topic"+str(i), "Operation": 1, "TableName":"table"+str(i), "Enabled": True}
    d.insert(table=t, record=rec)

# #d.update(t,rec,condition)
#
# delcond = "ISNULL(id)"
# #d.delete(t,"asd=1")
#
# fld = "id, name, count"
# where = "name='APK-2'"
# grp = "id"
# ord = "id"
# c = d.select(t,fld, condition=where, group_by=None, limit="10")
# r=c.fetchall()
# print(r)
