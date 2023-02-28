import re


class Result:
    """
    This class represents a code result with its associated text comment and language.
    
    Arguments:
    
    code (str): A string of code.
    text_comment (str): A string of text comment associated with the code.
    language (str): A string representing the language of the code (e.g. "py" for Python).
    
    
    """
    def __init__(self, code: str, text_comment: str, language: str):
        """
        Initializes a Result instance with the given code, text comment, and language.
        
        Arguments:
        
        code (str): A string of code.
        text_comment (str): A string of text comment associated with the code.
        language (str): A string representing the language of the code (e.g. "py" for Python).
        
        
        """
        self.__code = code
        self.__text_comment = text_comment
        self.__language = language

    def get(self) -> str:
        """
        Returns a modified version of the code with the text comments included as docstrings for the appropriate class and function definitions in the code.
        
        Arguments: None
        
        Returns:
        
        str: A string representing the modified version of the code.
        
        
        """
        if self.__language == "py":
            return self.__py()

    def __py(self) -> str:
        """
        A private method that splits Python code into sections based on the "
        """
        regexpes = re.finditer(r"\|(.+?)\|", self.__text_comment)
        indexes = []

        while True:
            try:
                match = next(regexpes)
                start = match.start()
                end = match.end()
                indexes.append((start, end))
            except:
                break

        names = []
        comments = []
        for i in range(len(indexes)):
            """
            " and "..." separators in the text comment associated with the code.
            
            Arguments: None
            
            Returns:
            
            str: A string representing the modified version of the Python code.
            """
            names.append(self.__text_comment[indexes[i][0] + 1 : indexes[i][1] - 1])
            if i < len(indexes) - 1:
                comments.append(
                    self.__text_comment[indexes[i][1] + 1 : indexes[i + 1][0]].replace(
                        "Description: ", ""
                    )
                )
            else:
                comments.append(
                    self.__text_comment[indexes[i][1] :].replace("Description: ", "")
                )

        for i in range(len(names)):
            index = self.__code.index(names[i])
            split_start = self.__code[index:]
            doubledot = index + split_start.index(":\n") + 1
            tabs = re.search(r":\n(.*?)[a-zA-Z]", split_start).span()
            tabs_count = tabs[1] - tabs[0]
            tab = (tabs_count - 3) * " "
            replace_text = self.__code[index:doubledot]
            new_replace_text = comments[i].replace("\n", f"\n{tab}")
            self.__code = self.__code.replace(
                replace_text,
                f'{replace_text}\n{tab}"""\n{tab}{new_replace_text}\n{tab}"""',
            )
        return self.__code
