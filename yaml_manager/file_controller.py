"""
file_controller.py

This module provides the FileController abstract base class for managing file operations.

Classes:
    FileController: An abstract base class to handle common file operations.
"""

from abc import ABC, abstractmethod
from pathlib import Path
import os
import re


class FileController(ABC):
    """
    Abstract class to handle file operations.

    This class provides the base structure for managing file I/O operations.
    It verifies the file path, ensures read/write permissions, and defines 
    abstract methods for loading and saving data.

    Attributes
    ----------
    file_path : str
        The path to the file being managed.
    data : dict
        Dictionary holding the data loaded from the file.
    """

    __version__ = "1.2.3"

    def __init__(self, file_path: str) -> None:
        """
        Initializes the FileController instance.

        Parameters
        ----------
        file_path : str
            The path to the file to be managed.

        Raises
        ------
        TypeError
            If file_path is not a string.
        IsADirectoryError
            If file_path points to a directory.
        PermissionError
            If the file lacks read or write permissions.
        """
        self.file_path = file_path
        self.data = {}

        if not isinstance(file_path, str):
            raise TypeError("File_path needs to be a string")

        if Path(file_path).exists():
            if Path(file_path).is_file():

                if not os.access(file_path, os.R_OK):
                    raise PermissionError(f"Cannot read file: {file_path}")

                if not os.access(file_path, os.W_OK):
                    raise PermissionError(f"Cannot write to file: {file_path}")

                self.reload()

            else:
                raise IsADirectoryError(f"{file_path} is not a file")

    @abstractmethod
    def reload(self):
        """
        Abstract method for loading data from the file into `self.data`.
        Must be implemented by subclasses.
        """

    @abstractmethod
    def save(self):
        """
        Abstract method for saving `self.data` to the file.
        Must be implemented by subclasses.
        """

    def contains(self, key: str) -> bool:
        """
        Checks if a key exists in the data dictionary.

        Parameters
        ----------
        key : str
            The key to search for in the data dictionary.

        Returns
        -------
        bool
            True if the key exists in the dictionary, False otherwise.
        """
        return key in self.data

    def set(self, key: str, value: any) -> None:
        """
        Sets, modifies, or deletes values in the configuration.

        Parameters
        ----------
        key : str
            The configuration key, separated by dots.
        value : Any
            The value to set. If None, the key will be deleted.

        Raises
        ------
        TypeError
            If `key` is not a string or is an empty string.
        """
        if isinstance(key, str) and len(key) > 0:
            self.data = self.__update_dict(key.split("."), self.data, value)
        else:
            raise TypeError("Key must be a non-empty string.")

    def string(self, key: str, default_value: str | None = None) -> str | None:
        """
        Gets a string value from the data.

        Parameters
        ----------
        key : str
            The key to the configuration key.
        default_value : str, optional
            The default value to return if the key is not found.

        Returns
        -------
        str
            The string value associated with the given key key, or `None` if
            the key is not found.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not a string.
        """
        if not self.__validate_key_and_default(key, default_value, str):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be a string.")

        value = self.__handle_get(key.split("."), self.data, default_value)

        if value is not None:
            return str(value)

        return None

    def float(self, key: string, default_value: float | int | None = None) -> float | None:
        """
        Gets a float value from the data.

        Parameters
        ----------
        key : str
            The configuration key.
        default_value : float or int, optional
            The default value to return if the key is not found.

        Returns
        -------
        float
            The float value associated with the given key key, or `None` if the key is not found.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not a number.
        """
        if not self.__validate_key_and_default(key, default_value, (float, int)):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be a number.")

        string = self.string(key, str(default_value)
                             if default_value is not None else None)

        if string is None:
            return None

        if re.search(r"^-?\d+(\.\d+)?$", string):
            return float(string)

        if default_value is not None:
            self.set(key, default_value)
            return float(default_value)

        return None

    def int(self, key: string, default_value: int | None = None) -> int | None:
        """
        Gets an integer value from the data.

        Parameters
        ----------
        key : str
            The configuration key.
        default_value : int, optional
            The default value to return if the key is not found.

        Returns
        -------
        int
            The integer value associated with the given key key, or `None` if the key is not found.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not an integer.
        """
        if not self.__validate_key_and_default(key, default_value, int):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be an integer.")

        string = self.string(key, str(default_value)
                             if default_value is not None else None)

        if string is None:
            return None

        if re.search(r"^-?\d+$", string):
            return int(string)

        if default_value is not None:
            self.set(key, default_value)
            return int(default_value)

        return None

    def boolean(self, key: string, default_value: bool | None = None) -> bool | None:
        """
        Gets a boolean value from the data.

        Parameters
        ----------
        key : str
            The key to the configuration key.
        default_value : bool, optional
            The default value to return if the key is not found.

        Returns
        -------
        bool
            The boolean value associated with the given key key, or `None` if the key is not found.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not a boolean.
        """
        if not self.__validate_key_and_default(key, default_value, bool):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be a boolean.")

        string = self.string(key, str(default_value)
                             if default_value is not None else None)

        if string is None:
            return None

        return string.lower() == "true"

    def str_list(self, key: string,
                 default_value: list[string] | None = None) -> list[string] | None:
        """
        Gets a list of strings from the data.

        Parameters
        ----------
        key : str
            The key to the configuration key.
        default_value : list of str, optional
            The default value to return if the key is not found.

        Returns
        -------
        list of str
            The list of string values associated with the given key key,
              or `None` if the key is not found.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not a list of strings.
        """
        if not self.__validate_key_and_default(key, default_value, list[str]):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be a list of strings.")

        lista = self.__handle_get(key.split("."), self.data, default_value)

        if isinstance(lista, list):
            return [str(x) for x in lista]

        if default_value is not None:
            self.set(key, default_value)
            return default_value

        return None

    def float_list(self, key: str,
                   default_value: list[float | int] | None = None) -> list[float] | None:
        """
        Gets a list of floats from the data.

        Parameters
        ----------
        key : str
            The key to the configuration key.
        default_value : list of float, optional
            The default value to return if the key is not found.

        Returns
        -------
        list of float
            The list of float values associated with the given key key,
              or `None` if the key is not found.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not a list of numbers.
        """
        if not self.__validate_key_and_default(key, default_value, list[float | int]):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be a list of numbers.")

        entry = self.__handle_get(key.split("."), self.data, default_value)

        if isinstance(entry, list):
            float_list = []

            # Converting values to floats
            for item in entry:
                if isinstance(item, (float, int)):
                    float_list.append(float(item))

                else:
                    string = str(item)

                    if re.search(r"^-?\d+(\.\d+)?$", string):
                        float_list.append(float(string))

                    else:
                        float_list.append(0.0)

            return float_list

        if default_value is not None:
            self.set(key, default_value)
            return default_value

        return None

    def int_list(self, key: string,
                 default_value: list[int | float] | None = None) -> list[int] | None:
        """
        Retrieves a list of integers from the data.

        This method processes the provided key to get a list of integers from the configuration.
        If the values are not integers, they will be converted when possible.
        If the value is not found, the `default_value` will be returned or set.

        Parameters
        ----------
        key : str
            The key to the configuration key, separated by dots.
        default_value : list, optional
            The default value to return if the key is not found (default is None).

        Returns
        -------
        list of int
            A list of integers retrieved from the data.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not a list.
        """
        if not self.__validate_key_and_default(key, default_value, list[int | float]):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be a list of numbers.")

        entry = self.__handle_get(key.split("."), self.data, default_value)

        if isinstance(entry, list):
            int_list = []

            # Converting values to integers
            for item in entry:
                if isinstance(item, (int, float)):
                    int_list.append(int(item))
                else:
                    string = str(item)

                    if re.search(r"^-?\d+(.\d+)?$", string):
                        int_list.append(int(string))

                    else:
                        int_list.append(0)

            return int_list

        if default_value is not None:
            self.set(key, default_value)
            return default_value

        return None

    def bool_list(self, key: string, default_value: list[bool] | None = None) -> list[bool] | None:
        """
        Retrieves a list of booleans from the data.

        This method processes the provided key to get a list of booleans from the configuration.
        Values are converted to booleans based on their types (integers, floats, etc.).

        Parameters
        ----------
        key : str
            The key to the configuration key, separated by dots.
        default_value : list, optional
            The default value to return if the key is not found (default is None).

        Returns
        -------
        list of bool
            A list of boolean values retrieved from the data.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not a list.
        """
        if not self.__validate_key_and_default(key, default_value, list):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be a list.")

        entry = self.__handle_get(key.split("."), self.data, default_value)

        if isinstance(entry, list):
            bool_list = []

            # Converting values to booleans
            for item in entry:
                if isinstance(item, bool):
                    bool_list.append(bool(item))

                else:
                    bool_list.append(str(item).lower() == "true")

            return bool_list

        if default_value is not None:

            self.set(key, default_value)
            return default_value

        return None

    def dictionary(self, key: string, default_value: dict | None = None) -> dict | None:
        """
        Retrieves a dictionary from the data.

        This method processes the provided key to get a dictionary from the configuration. 
        If the dictionary is not found, the `default_value` will be returned or set.

        Parameters
        ----------
        key : str
            The key to the configuration key, separated by dots.
        default_value : dict, optional
            The default value to return if the key is not found (default is None).

        Returns
        -------
        dict
            A dictionary retrieved from the data.

        Raises
        ------
        TypeError
            If `key` is not a string or `default_value` is not a dictionary.
        """
        if not self.__validate_key_and_default(key, default_value, dict):
            raise TypeError(
                "Key must be a non-empty string, and default_value must be a dictionary.")

        result = self.__handle_get(key.split("."), self.data, default_value)

        if isinstance(result, dict):
            return result

        if default_value is not None:

            self.set(key, default_value)
            return default_value

        return None

    def __validate_key_and_default(self, key: string,
                                   default_value: any,
                                   expected_type: type | tuple[type, type]) -> bool:
        """
        Validates the key and default value.

        Parameters
        ----------
        key : str
            The key to validate.
        default_value : any
            The default value to validate.
        expected_type : type or tuple of types
            The expected type or types of the default value.

        Returns
        -------
        bool
            True if the key and default value are valid, False otherwise.
        """
        return (isinstance(key, str) and len(key) > 0 and
                (isinstance(default_value, expected_type) or default_value is None))

    def __generete_new_tree(self, parent: list, value: any) -> dict:
        """
        Creates a new configuration tree structure.

        Parameters
        ----------
        tree : list
            List representing the tree structure of keys.
        value : Any
            The value to assign to the last key in the tree.

        Returns
        -------
        dict
            A new dictionary with the nested structure.
        """
        new_dict = {}

        if len(parent) == 1:
            new_dict[parent[0]] = value

        else:
            new = {parent[-1]: value}

            for x in range(len(parent) - 2, -1, -1):
                new = {parent[x]: new}

            new_dict[parent[0]] = new

        return new_dict

    def __update_dict(self, tree: list, dictionary: dict, value: any) -> dict:
        """
        Processes setting values in the configuration tree.

        Parameters
        ----------
        tree : list
            The list representing the tree structure of keys.
        dictionary : dict
            The current dictionary where the value should be set.
        value : Any
            The value to be set. If None, the key will be deleted.

        Returns
        -------
        dict
            The updated dictionary.
        """
        if tree[0] in dictionary:

            dictionary[tree[0]] = self.__update_existing_key(
                tree, dictionary, value)

        elif value is not None:

            dictionary[tree[0]] = self.__create_new_key(tree, value)

        return dictionary

    def __update_existing_key(self, tree: list, dictionary: dict, value: any) -> any:
        """
        Updates the value for an existing key in the configuration tree.

        This method recursively traverses the configuration tree and updates the 
        specified key with the provided value. If the value is `None`, the key 
        is deleted from the dictionary. If the key points to a non-dictionary 
        value, a new tree is generated.

        Parameters
        ----------
        tree : list
            A list representing the hierarchy of keys in the configuration tree.
        dictionary : dict
            The dictionary where the key-value pair is being updated.
        value : any
            The new value to set. If `None`, the key will be deleted.

        Returns
        -------
        any
            The updated value for the specified key, or the new sub-tree if applicable.
        """
        if len(tree) == 1:
            return value if value is not None else dictionary.pop(tree[0])

        if not isinstance(dictionary[tree[0]], dict):
            return self.__generete_new_tree(tree[1:], value)

        dictionary[tree[0]] = self.__update_dict(
            tree[1:], dictionary[tree[0]], value)

        if len(dictionary[tree[0]]) == 0:
            del dictionary[tree[0]]

        return dictionary[tree[0]]

    def __create_new_key(self, tree: list, value: any) -> any:
        """
        Creates a new key in the configuration tree with the provided value.

        This method generates a new tree structure for the given key path and 
        sets the specified value at the leaf node of the tree.

        Parameters
        ----------
        tree : list
            A list representing the hierarchy of keys to create in the configuration tree.
        value : any
            The value to set at the new key.

        Returns
        -------
        any
            The generated sub-tree with the new key-value pair.
        """
        if len(tree) == 1:
            return value

        return self.__generete_new_tree(tree[1:], value)

    def __handle_get(self, tree: list[string],
                     dictionary: dict,
                     default_value: any | None) -> any | None:
        """
        Internal method to process getting values from the configuration.

        Parameters
        ----------
        tree : list
            The list representing the tree structure of keys.
        dictionary : dict
            The current dictionary where the value should be fetched from.
        default_value : Any
            The default value to return if the key is not found.

        Returns
        -------
        Any
            The value associated with the given key path.
        """
        if tree[0] in dictionary:
            if len(tree) == 1:
                return dictionary[tree[0]]

            if not isinstance(dictionary[tree[0]], dict):
                print(f"ERROR: {tree[0]} is not a configuration tree.")
                return None

            return self.__handle_get(tree[1:], dictionary[tree[0]], default_value)

        if default_value is not None:
            self.__update_dict(tree, dictionary, default_value)
            return default_value

        return None
