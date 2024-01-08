import ast

def get_top_level_class_names_from_file(file_path):
    with open(file_path, "r") as source_code:
        tree = ast.parse(source_code.read())
    class_names = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    return class_names

file_path = r'C:\Users\Baschieri Matteo\Workspace\rebecca\lib\istargeting\api_client\serializers\client_serializer.py'
class_names = get_top_level_class_names_from_file(file_path)
print(class_names)