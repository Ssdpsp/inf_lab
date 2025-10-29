import toml
import yaml

def toml_to_yaml(input_toml, output_yaml):
    with open(input_toml, "r", encoding="utf-8") as toml_file:
        data = toml.load(toml_file)  
    with open(output_yaml, "w", encoding="utf-8") as yaml_file:
        yaml.dump(data, yaml_file, indent=2, allow_unicode=True)  

input_toml = "TOML_расписание.toml"
output_yaml = "расписание.yaml"
toml_to_yaml(input_toml, output_yaml)