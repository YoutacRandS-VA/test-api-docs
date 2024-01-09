import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def has_circular_reference(data, visited=None, current_path=None):
    if visited is None:
        visited = set()
    if current_path is None:
        current_path = []

    if isinstance(data, dict):
        for key, value in data.items():
            path_key = tuple(current_path + [key])

            if path_key in visited:
                print(f"Circular reference found: {path_key}")
                return True

            visited.add(path_key)
            if has_circular_reference(value, visited, current_path + [key]):
                return True
            visited.remove(path_key)

    elif isinstance(data, list):
        for i, item in enumerate(data):
            path_index = tuple(current_path + [i])

            if path_index in visited:
                print(f"Circular reference found: {path_index}")
                return True

            visited.add(path_index)
            if has_circular_reference(item, visited, current_path + [i]):
                return True
            visited.remove(path_index)

    return False

if __name__ == "__main__":
    yaml_file_path = "/Users/kody/Desktop/test-api-docs/callous-chasm/schemas/test4.yml"

    try:
        yaml_data = load_yaml(yaml_file_path)
        if has_circular_reference(yaml_data):
            print("Circular references found in the YAML file.")
        else:
            print("No circular references found in the YAML file.")
    except Exception as e:
        print(f"Error loading YAML file: {e}")
