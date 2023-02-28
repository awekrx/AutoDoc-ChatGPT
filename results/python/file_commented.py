import os


class File:
    """
    This class represents a file object with methods to retrieve its content and language, and create a new file with commented content.
    
    Arguments:
    
    path (str): A string representing the path to the file.
    
    
    """
    def __init__(self, path: str):
        """
        Initializes a File instance with the given path.
        
        Arguments:
        
        path (str): A string representing the path to the file.
        
        Returns: None
        
        
        """
        self.__path = os.path.normpath(os.path.abspath(path))
        self.__dirname = os.path.dirname(self.__path)
        self.__basename = os.path.basename(self.__path).split(".")[0]
        self.__language = os.path.basename(self.__path).split(".")[1]

    def content(self) -> str:
        """
        Retrieves the content of the file.
        
        Arguments: None
        
        Returns:
        
        str: A string representing the content of the file.
        
        
        """
        self.__text = open(self.__path, "r").read()
        return self.__text

    def language(self) -> str:
        """
        Retrieves the language of the file.
        
        Arguments: None
        
        Returns:
        
        str: A string representing the language of the file.
        
        
        """
        return self.__language

    def create_commented_file(self, content: str) -> None:
        """
        
        Creates a new file with the commented content.
        
        Arguments:
        
        content (str): A string representing the commented content to be written into the new file.
        
        Returns: None
        """
        path = os.path.join(
            self.__dirname,
            self.__basename + f"_commented.{self.__language}",
        )
        open(path, "w").write(content)
