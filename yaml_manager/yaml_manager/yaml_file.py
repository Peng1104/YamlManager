from .file_controller import FileController
from pathlib import Path
import yaml
import os


class YAMLFile(FileController):
    """
    Class to manage YAML files for reading and writing operations.

    This class extends `FileController` to handle YAML file operations,
    such as loading data from a YAML file and saving data back to it.

    Attributes
    ----------
    file_path : str
        The path to the YAML file.
    data : dict
        A dictionary containing the data loaded from the YAML file.
    """

    __version__ = "1.2.1"

    def __init__(self, file_path: str) -> None:
        """
        Initializes the `YAMLFile` instance.

        Parameters
        ----------
        file_path : str
            The path to the YAML file to be managed.

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
        Loads the data from the YAML file into `self.data`.

        This method reads the YAML file specified by `file_path`
        and loads the content into the `data` attribute.

        Raises
        ------
        yaml.YAMLError
            If the file content is not valid YAML.
        FileNotFoundError
            If the file does not exist.
        """
        with open(self.file_path, 'r', encoding="utf-8") as file:
            self._data = yaml.load(file.read(), Loader=yaml.FullLoader)

    def save(self) -> None:
        """
        Saves the data from `self.data` back to the YAML file.

        This method writes the content of `self.data` to the YAML file specified by `file_path`.
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
            file.write(yaml.dump(self._data, indent=2,
                       allow_unicode=True, encoding="utf-8", sort_keys=False))
