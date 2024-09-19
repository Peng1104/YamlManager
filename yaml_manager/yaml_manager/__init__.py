from .json_file import JSONFile
from .yaml_file import YAMLFile

# Version of FileController
__version__ = "1.2.2"


def to_json_file(path: str | JSONFile, dictionary: dict, save: bool = False) -> JSONFile:
    """
    Converts a dictionary into a JSONFile.

    This function takes a dictionary and converts it into a `JSONFile`.
    If a file path is provided, it creates a new `JSONFile`. Optionally, the file can be saved.

    Parameters
    ----------
    path : str or JSONFile
        The file path or an existing `JSONFile` object.
    dictionary : dict
        The dictionary to be converted into a JSON file.
    save : bool, optional
        If True, the JSON file will be saved (default is False).

    Returns
    -------
    JSONFile
        A `JSONFile` object containing the data from the dictionary.

    Raises
    ------
    TypeError
        If `path` is not a string or `JSONFile`, or if `dictionary` is not a dictionary, or if `save` is not a boolean.
    """
    if not (isinstance(path, (str, JSONFile)) and isinstance(dictionary, dict) and isinstance(save, bool)):
        raise TypeError(
            "path must be a non-empty string or a JSONFile, dictionary must be a dictionary, and save must be a boolean.")

    if type(path) is str:
        file = JSONFile(path)
    else:
        file = path

    file._data = dictionary

    if save:
        file.save()

    return file


def json_file_to_dict(json_path: str | JSONFile) -> dict:
    """
    Converts a JSON file into a dictionary.

    This function loads the data from a `JSONFile` or a file path into a dictionary.

    Parameters
    ----------
    json_path : str or JSONFile
        The path to the JSON file or an existing `JSONFile` object.

    Returns
    -------
    dict
        A dictionary with the data from the JSON file.

    Raises
    ------
    TypeError
        If `json_path` is not a string or `JSONFile`.
    """
    if not isinstance(json_path, (str, JSONFile)):
        raise TypeError("json_path must be a non-empty string or a JSONFile.")
    
    if type(json_path) is str:
        return JSONFile(json_path)._data
    else:
        return json_path._data


def json_file_to_yaml_file(json_path: str | JSONFile, yaml_path: str | YAMLFile, save: bool = False) -> YAMLFile:
    """
    Converts a JSON file into a YAML file and returns a new `YAMLFile` object.

    This function reads a `JSONFile` and converts its content into a `YAMLFile`.
    Optionally, the YAML file can be saved.

    Parameters
    ----------
    json_path : str or JSONFile
        The path to the JSON file or an existing `JSONFile` object.
    yaml_path : str or YAMLFile
        The path to the YAML file or an existing `YAMLFile` object.
    save : bool, optional
        If True, the YAML file will be saved (default is False).

    Returns
    -------
    YAMLFile
        A `YAMLFile` object containing the data from the JSON file.

    Raises
    ------
    TypeError
                If `json_path` is not a string or `JSONFile`, or if `yaml_path` is not a string or `YAMLFile`, or if `save` is not a boolean.
    """
    if ((type(yaml_path) is str and len(yaml_path) > 0) or type(yaml_path) is YAMLFile) and isinstance(save, bool):
        if type(yaml_path) is str:
            file = YAMLFile(yaml_path)
        else:
            file = yaml_path

        file._data = json_file_to_dict(json_path)

        if save:
            file.save()

        return file
    else:
        raise TypeError(
            "yaml_path must be a non-empty string or a YAMLFile, and save must be a boolean.")


def to_yaml_file(yaml_path: str | YAMLFile, dictionary: dict, save: bool = False) -> YAMLFile:
    """
    Converts a dictionary into a YAMLFile object.

    This function takes a dictionary and converts it into a `YAMLFile` object.
    Optionally, the file can be saved.

    Parameters
    ----------
    yaml_path : str or YAMLFile
        The path to the YAML file or an existing `YAMLFile` object.
    dictionary : dict
        The dictionary to be converted into a YAML file.
    save : bool, optional
        If True, the YAML file will be saved (default is False).

    Returns
    -------
    YAMLFile
        A `YAMLFile` object containing the data from the dictionary.

    Raises
    ------
    TypeError
        If `yaml_path` is not a string or `YAMLFile`, or if `dictionary` is not a dictionary, or if `save` is not a boolean.
    """
    if ((type(yaml_path) is str and len(yaml_path) > 0) or type(yaml_path) is YAMLFile) and isinstance(dictionary, dict) and isinstance(save, bool):
        if type(yaml_path) is str:
            file = YAMLFile(yaml_path)
        else:
            file = yaml_path

        file._data = dictionary

        if save:
            file.save()

        return file
    else:
        raise TypeError(
            "yaml_path must be a non-empty string or a YAMLFile, dictionary must be a dictionary, and save must be a boolean.")


def yaml_file_to_dict(yaml_path: str | YAMLFile) -> dict:
    """
    Converts a YAML file into a dictionary.

    This function loads the data from a `YAMLFile` or a file path into a dictionary.

    Parameters
    ----------
    yaml_path : str or YAMLFile
        The path to the YAML file or an existing `YAMLFile` object.

    Returns
    -------
    dict
        A dictionary with the data from the YAML file.

    Raises
    ------
    TypeError
        If `yaml_path` is not a string or `YAMLFile`.
    """
    if (type(yaml_path) is str and len(yaml_path) > 0) or type(yaml_path) is YAMLFile:
        if type(yaml_path) is str:
            return YAMLFile(yaml_path)._data
        else:
            return yaml_path._data
    else:
        raise TypeError("yaml_path must be a non-empty string or a YAMLFile.")


def yaml_file_to_json_file(yaml_path: str | YAMLFile, json_path: str | JSONFile, save: bool = False) -> JSONFile:
    """
    Converts a YAML file into a JSON file and returns a new `JSONFile` object.

    This function reads a `YAMLFile` and converts its content into a `JSONFile`.
    Optionally, the JSON file can be saved.

    Parameters
    ----------
    yaml_path : str or YAMLFile
        The path to the YAML file or an existing `YAMLFile` object.
    json_path : str or JSONFile
        The path to the JSON file or an existing `JSONFile` object.
    save : bool, optional
        If True, the JSON file will be saved (default is False).

    Returns
    -------
    JSONFile
        A `JSONFile` object containing the data from the YAML file.

    Raises
    ------
    TypeError
        If `json_path` is not a string or `JSONFile`, or if `save` is not a boolean.
    """
    if ((type(json_path) is str and len(json_path) > 0) or type(json_path) is JSONFile) and isinstance(save, bool):
        if type(json_path) is str:
            file = JSONFile(json_path)
        else:
            file = json_path

        file._data = yaml_file_to_dict(yaml_path)

        if save:
            file.save()

        return file
    else:
        raise TypeError(
            "json_path must be a non-empty string or a JSONFile, and save must be a boolean.")
