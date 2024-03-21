import json
import os as o


def write_to_file(record):
    if not o.path.isfile("db/records.json"):
        with open("db/records.json", "w") as json_file:
            json.dump([record],json_file ,indent=4)
            
            
    else:
        with open("db/records.json", "r") as json_file:
            data = json.load(json_file)
        data.append(record)
        with open("db/records.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    


# def remove_line_from_file(name_to_delete):
#     file_name = os.environ.get("file_name")

#     with open(file_name, "r") as file:
#         lines = file.readlines()
#     modified_lines = []
#     file_copies = 0
#     for line in lines:
#         line_split = (line.strip()).split(', ')
#         if name_to_delete == line_split[0]:
#             file_copies = int(line_split[1])
#         else:
#             modified_lines.append(line)
#     with open(file_name, "w") as output:
#         output.writelines(modified_lines)
#     return file_copies
