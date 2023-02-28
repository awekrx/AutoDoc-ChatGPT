import re


class Divider:
    """
    A class that takes a text string and a language string, and splits the text into sections based on language-specific separators.
    
    Arguments:
    
    text (str): A string of text to be split
    language (str): A string representing the language of the text (e.g. "py" for Python)
    
    
    """
    def __init__(self, text: str, language: str):
        """
        Initializes a Divider instance with the given text and language.
        
        Arguments:
        
        text (str): A string of text to be split
        language (str): A string representing the language of the text (e.g. "py" for Python)
        
        
        """
        self.__text = text
        self.__language = language
        self.__splitted_content = []

    def divide(
        self,
    ) -> list[str]:
        """
        Splits the text into sections based on language-specific separators.
        
        Arguments: None
        
        Returns:
        
        list[str]: A list of strings representing the sections of the text.
        
        
        """
        if self.__language == "py":
            return self.__py()

    def __py(self) -> list[str]:
        """
        
        A method that splits Python code into sections based on class and function definitions.
        
        Arguments: None
        
        Returns:
        
        list[str]: A list of strings representing the sections of the Python code.
        """
        starts = re.finditer(r"(?<!.)(class|def)", self.__text)
        ends = re.finditer(r"\n(def|class)", self.__text)

        while True:
            start = 0
            end = 0
            try:
                start = next(starts).start()
                end = next(ends).start()
                if end < start:
                    end = next(ends).start()
                self.__splitted_content.append(self.__text[start:end])
            except:
                self.__splitted_content.append(self.__text[start:])
                break

        return self.__splitted_content
