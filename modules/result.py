import re


class Result:
    def __init__(self, code: str, text_comment: str, language: str):
        self.__code = code
        self.__text_comment = text_comment
        self.__language = language

    def get(self) -> str:
        if self.__language == "py":
            return self.__py()

    def __py(self) -> str:
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
