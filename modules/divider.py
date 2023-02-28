import re


class Divider:
    def __init__(self, text: str, language: str):
        self.__text = text
        self.__language = language
        self.__splitted_content = []

    def divide(
        self,
    ) -> list[str]:
        if self.__language == "py":
            return self.__py()

    def __py(self) -> list[str]:
        starts = re.finditer(r"(?<!.)(class|def)", self.__text)
        ends = re.finditer(r"\n(def|class)", self.__text)

        while True:
            start = None
            end = None
            try:
                start = next(starts).start()
                end = next(ends).start()
                if end < start:
                    end = next(ends).start()
                self.__splitted_content.append(self.__text[start:end])
            except:
                if start != None:
                    self.__splitted_content.append(self.__text[start:])
                break

        return self.__splitted_content
