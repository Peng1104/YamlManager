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
- **Descrição:**
  - Representa um controlador de arquivos abstrato e fornece métodos para manipular dados de arquivos.
- **Métodos:**
  - `__init__(file_path: str)`: Inicializa a instância de `FileController` com o caminho do arquivo.
  - `reload()`: Método abstrato para carregar dados do arquivo. Deve ser implementado pelas subclasses.
  - `save()`: Método abstrato para salvar dados no arquivo. Deve ser implementado pelas subclasses.
  - `contains(key: str) -> bool`: Verifica se uma chave existe no dicionário de dados.
  - `set(key: str, value: any) -> None`: Define, modifica ou exclui valores na configuração.
  - `string(key: str, default_value: str | None = None) -> str | None`: Obtém um valor de string dos dados.
  - `float(key: str, default_value: float | int | None = None) -> float | None`: Obtém um valor de ponto flutuante dos dados.
  - `int(key: str, default_value: int | None = None) -> int | None`: Obtém um valor inteiro dos dados.
  - `boolean(key: str, default_value: bool | None = None) -> bool | None`: Obtém um valor booleano dos dados.
  - `string_list(key: str, default_value: list[str] | None = None) -> list[str] | None`: Obtém uma lista de strings dos dados.
  - `float_list(key: str, default_value: list[float | int] | None = None) -> list[float] | None`: Obtém uma lista de valores de ponto flutuante dos dados.
  - `int_list(key: str, default_value: list[int | float] | None = None) -> list[int] | None`: Obtém uma lista de valores inteiros dos dados.
  - `bool_list(key: str, default_value: list[bool] | None = None) -> list[bool] | None`: Obtém uma lista de valores booleanos dos dados.
  - `dictionary(key: str, default_value: dict | None = None) -> dict | None`: Obtém um dicionário dos dados.
