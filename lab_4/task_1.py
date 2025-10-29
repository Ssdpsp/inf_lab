def parse_toml_to_yaml(toml_file, yaml_file):
    with open(toml_file, "r", encoding="utf-8") as infile, open(yaml_file, "w", encoding="utf-8") as outfile:
        current_indent = 0  
        in_table = False   
        for line in infile:
            line = line.strip()
            if not line:  
                continue
            if line.startswith("#"):  
                continue
            if line.startswith("[") and line.endswith("]"):  
                table_name = line[1:-1]
                if in_table:
                    current_indent -= 2  
                print(" " * current_indent + table_name + ":", file=outfile)
                current_indent += 2
                in_table = True
            else: 
                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    print(" " * current_indent + key + ": " + value, file=outfile)
        if in_table:
            current_indent -= 2
parse_toml_to_yaml("TOML_расписание.toml", "РАСПИСАНИЕ.yaml")
print("TOML парсинг осуществлен")
