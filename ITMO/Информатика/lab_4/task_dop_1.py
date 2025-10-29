def parse_yaml_to_json(yaml_file, json_file):
    data = {}
    current_section = data
    indent_level = 0
    stack = [] 
    with open(yaml_file, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue

            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                if not value:  
                    if current_section is not None:
                        stack.append(current_section) 
                    current_section[key] = {}
                    current_section = current_section[key]
                    indent_level +=1
                else: 
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]

                    current_section[key] = value
            else:
                if len(stack) > 0:
                    current_section = stack.pop()
                    indent_level -=1

    def to_json_string(data, indent=0):
        json_string = ""
        if isinstance(data, dict):
            json_string += "{\n"
            items = list(data.items())
            for i, (key, value) in enumerate(items):
                json_string += "    " * (indent + 1) + f'"{key}": '
                json_string += to_json_string(value, indent + 1)
                if i < len(items) - 1:
                    json_string += ","
                json_string += "\n"
            json_string += "    " * indent + "}"
        elif isinstance(data, list): 
            json_string += "[" + ", ".join(map(str, data)) + "]"
        else:
            json_string += f'"{data}"' 
        return json_string
    json_output = to_json_string(data)
    with open(json_file, "w", encoding="utf-8") as outfile:
        outfile.write(json_output)

parse_yaml_to_json("РАСПИСАНИЕ.yaml", "РАСПИСАНИЕ.json")
print("YAML парсинг осуществлен")
