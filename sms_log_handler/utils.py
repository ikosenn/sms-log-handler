from importlib import import_module


def import_from_string(string_representation: str) -> str:
    """
    Import a class from string
    """
    parts = string_representation.split('.')
    module_path, class_name = '.'.join(parts[:-1]), parts[-1]
    module = import_module(module_path)
    return getattr(module, class_name)
