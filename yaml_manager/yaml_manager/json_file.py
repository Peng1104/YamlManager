from .file_controller import FileController
from pathlib import Path
import os
import json


class JSONFile(FileController):
    """
    Class to manage JSON files for reading and writing operations.

    This class extends `FileController` to handle JSON file operations,
    such as loading data from a JSON file and saving data back to it.

    Attributes
    ----------
    file_path : str
        The path to the JSON file.
    data : dict
        A dictionary containing the data loaded from the JSON file.
    """

    __version__ = "1.2.1"

    def __init__(self, file_path: str) -> None:
        """
        Initializes the `JSONFile` instance.

        Parameters
        ----------
        file_path : str
            The path to the JSON file to be managed.

        Raises
        ------
        TypeError
            If `file_path` is not a string.
        IsADirectoryError
            If `file_path` points to a directory instead of a file.
        PermissionError
            If the file lacks read or write permissions.
        """

        super().__init__(file_path)

    def reload(self) -> None:
        """
        Loads the data from the JSON file into `self.data`.

        This method reads the JSON file specified by `file_path`
        and loads the content into the `data` attribute.

        Raises
        ------
        json.JSONDecodeError
            If the file content is not valid JSON.
        FileNotFoundError
            If the file does not exist.
        """
        with open(self.file_path, 'r', encoding="utf-8") as file:
            self._data = json.load(file)

    def save(self) -> None:
        """
        Saves the data from `self.data` back to the JSON file.

        This method writes the content of `self.data` to the JSON file specified by `file_path`.
        If the directory for the file does not exist, it creates the necessary directories.

        Raises
        ------
        OSError
            If there is an error in creating directories or writing to the file.
        """
        i = self.file_path.rfind("/")

        if i > -1 and not Path(self.file_path[:i]).exists():
            os.makedirs(self.file_path[:i], 0o666)

        with open(self.file_path, 'w', encoding="utf-8") as file:
            file.write(json.dumps(self._data, ensure_ascii=False,
                       allow_nan=False, indent="\t"))
