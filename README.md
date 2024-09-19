# YamlManager
Library to simplify the management and creation of JSON and YAML files.

## Functions:

1. **to_json_file:**
   - **Function:**
     - Converts a **dictionary** to a **JSONFile**
   - **Arguments:**
     - `json_path` - A **string** or a **JSONFile**, location of the **JSONFile**
     - `dictionary` - The data that the **JSONFile** should have
   - **Optional Arguments:**
     - `save` - Whether the **JSONFile** should be saved (created or modified) as soon as the data matches the **dictionary**
   - **Returns:**
     - A **JSONFile** located at `json_path`

2. **json_file_to_dict:**
   - **Function:**
     - Converts the data from a **JSONFile** to a **dictionary**
   - **Arguments:**
     - `json_path` - A **string** or a **JSONFile**, location of the **JSONFile**
   - **Returns:**
     - A **dictionary** containing all the data from the **JSONFile**

3. **json_file_to_yaml_file:**
   - **Function:**
     - Converts the data from a **JSONFile** to a **YamlFile**
   - **Arguments:**
     - `json_path` - A **string** or a **JSONFile**, location of the **JSONFile**
     - `yaml_path` - A **string** or a **YamlFile**, location of the **YamlFile**
   - **Optional Arguments:**
     - `save` - Whether the **YamlFile** should be saved (created or modified) as soon as the data matches the **JSONFile**
   - **Returns:**
     - A **YamlFile** located at `yaml_path`

4. **to_yaml_file:**
   - **Function:**
     - Converts a **dictionary** to a **YamlFile**
   - **Arguments:**
     - `yaml_path` - A **string** or a **YamlFile**, location of the **YamlFile**
     - `dictionary` - The data that the **YamlFile** should have
   - **Optional Arguments:**
     - `save` - Whether the **YamlFile** should be saved (created or modified) as soon as the data matches the **dictionary**
   - **Returns:**
     - A **YamlFile** located at `yaml_path`

5. **yaml_file_to_dict:**
   - **Function:**
     - Converts the data from a **YamlFile** to a **dictionary**
   - **Arguments:**
     - `yaml_path` - A **string** or a **YamlFile**, location of the **YamlFile**
   - **Returns:**
     - A **dictionary** containing all the data from the **YamlFile**

6. **yaml_file_to_json_file:**
   - **Function:**
     - Converts the data from a **YamlFile** to a **JSONFile**
   - **Arguments:**
     - `yaml_path` - A **string** or a **YamlFile**, location of the **YamlFile**
     - `json_path` - A **string** or a **JSONFile**, location of the **JSONFile**
   - **Optional Arguments:**
     - `save` - Whether the **JSONFile** should be saved (created or modified) as soon as the data matches the **YamlFile**
   - **Returns:**
     - A **JSONFile** located at `json_path`

## Classes / Objects

### YamlFile
- **Description:**
  - Represents a YAML file and provides methods to manipulate its data.
- **Methods:**
  - `load()`: Loads the YAML file data.
  - `save()`: Saves the current data to the YAML file.

### JSONFile
- **Description:**
  - Represents a JSON file and provides methods to manipulate its data.
- **Methods:**
  - `load()`: Loads the JSON file data.
  - `save()`: Saves the current data to the JSON file.

### FileController
- **Description:**
  - Represents an abstract file controller and provides methods to manipulate file data.
- **Methods:**
  - `__init__(file_path: str)`: Initializes the `FileController` instance with the file path.
  - `reload()`: Abstract method to load data from the file. Must be implemented by subclasses.
  - `save()`: Abstract method to save data to the file. Must be implemented by subclasses.
  - `contains(key: str) -> bool`: Checks if a key exists in the data dictionary.
  - `set(key: str, value: any) -> None`: Sets, modifies, or deletes values in the configuration.
  - `string(key: str, default_value: str | None = None) -> str | None`: Gets a string value from the data.
  - `float(key: str, default_value: float | int | None = None) -> float | None`: Gets a float value from the data.
  - `int(key: str, default_value: int | None = None) -> int | None`: Gets an integer value from the data.
  - `boolean(key: str, default_value: bool | None = None) -> bool | None`: Gets a boolean value from the data.
  - `str_list(key: str, default_value: list[str] | None = None) -> list[str] | None`: Gets a list of strings from the data.
  - `float_list(key: str, default_value: list[float | int] | None = None) -> list[float] | None`: Gets a list of float values from the data.
  - `int_list(key: str, default_value: list[int | float] | None = None) -> list[int] | None`: Gets a list of integer values from the data.
  - `bool_list(key: str, default_value: list[bool] | None = None) -> list[bool] | None`: Gets a list of boolean values from the data.
  - `dictionary(key: str, default_value: dict | None = None) -> dict | None`: Gets a dictionary from the data.
