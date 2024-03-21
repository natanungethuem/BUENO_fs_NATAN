import pkgutil
import importlib

# Iterate over all modules in the current package
for _, module_name, _ in pkgutil.iter_modules(['backend']):
    # Import the module
    module = importlib.import_module(module_name)

    # Iterate over all classes in the module
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        # If the attribute is a class and it has a generate_sql method, call it
        if isinstance(attribute, type) and hasattr(attribute, 'generate_sql'):
            attribute.generate_sql()