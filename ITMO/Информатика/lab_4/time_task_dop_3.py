import time
def parse_yaml_to_xml(yaml_file, xml_file):
    data = {}
    current_section = [] 
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
                    data[key] = {} 
                    current_section.append(key)
                else:  
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    data[key] = value
    def to_xml_string(data, indent=0):
      xml_string = ""
      if isinstance(data, dict):
          for key, value in data.items():
              xml_string += "  " * indent + f"<{key}>"
              xml_string += to_xml_string(value, indent + 1)
              xml_string += f"</{key}>\n"
      else:
          xml_string += str(data)
      return xml_string
    xml_output = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml_output += "<root>\n"
    xml_output += to_xml_string(data, 1)
    xml_output += "</root>\n"
    with open(xml_file, "w", encoding="utf-8") as outfile:
        outfile.write(xml_output)

start_time = time.time()
for i in range (100):
    parse_yaml_to_xml("РАСПИСАНИЕ.yaml", "РАСПИСАНИЕ.xml")
end_time = time.time()  
elapsed_time = end_time - start_time
print("YAML парсинг осуществлен")
print(f"Затрачено времени: {elapsed_time} сек") 
