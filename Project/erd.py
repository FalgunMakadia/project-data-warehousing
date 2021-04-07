import json
from prettytable import PrettyTable

gdd_keys = []
table_list = []

with open('GDD.json') as f:
	data = json.load(f)

local_tables = data["local"]
remote_tables = data["remote"]

var_count = 0

user_input = int(input("Enter 1 for Local site ERD or 2 for Remote site ERD: "))
table_list = local_tables if user_input == 1 else remote_tables
msg = "===================  Local Site ERD  ===================" if user_input == 1 else "===================  Remote Site ERD  ==================="

print("\n\n")
print(msg+"\n")
for i in range(len(table_list)):

	frag = "z" + str(var_count)
	frag = PrettyTable()
	frag.field_names = [table_list[i].upper() + " TABLE", "Column Name", "Data Type", "Primary Key"]

	count = 0
	for j  in data[table_list[i]]:
		cname, ctype = j.split("|") 
		if count == 0:
			frag.add_row(["", cname, ctype, "<---"])
			count += 1
		else:
			frag.add_row(["", cname, ctype, ""])
	print(frag)
	print("\n\n")