import re


class Result:
    def __init__(self, code: str, text_comment: str, language: str):
        self.__code = code
        self.__text_comment = text_comment
        self.__language = language

    def get(self) -> str:
        if self.__language == "py":
            return self.__py()
        elif self.__language == "ts":
            return self.__ts()

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

    def __ts(self) -> str:
        regexpes = re.finditer(r"\|(.+?)\|\n", self.__text_comment)
        indexes = []

        while True:
            try:
                match = next(regexpes)
                start = match.start()
                end = match.end() - 1
                indexes.append((start, end))
            except:
                break

        names = []
        comments = []
        for i in range(len(indexes)):
            names.append(self.__text_comment[indexes[i][0] + 1 : indexes[i][1] - 1])
            if i < len(indexes) - 1:
                comments.append(
                    re.sub(
                        r"Comment:\n|Comment: \n",
                        "",
                        self.__text_comment[indexes[i][1] + 1 : indexes[i + 1][0]],
                    )
                )
            else:
                comments.append(
                    self.__text_comment[indexes[i][1] :].replace("Comment:\n", "")
                )

        for i in range(len(names)):
            comments[i] = " * " + comments[i].replace("\n", "\n * ")
            comments[i] = re.sub(r"\n\s\*\s\n\s\*\s", "", comments[i])
            for j in range(self.__code.find(names[i]), 0, -1):
                if self.__code[j] == "\n":
                    from_new_string = self.__code[j + 1 :]
                    tabs_end = re.search(r"[a-zA-Z]", from_new_string).start()
                    tabs = from_new_string[:tabs_end]
                    comments[i] = re.sub(r"\n", f"\n{tabs}", comments[i])
                    splitted_code = list(self.__code)
                    splitted_code[j] = f"\n{tabs}/**\n{tabs}{comments[i]}\n{tabs} */\n"
                    self.__code = "".join(splitted_code)
                    break
            else:
                self.__code = f"\n/**\n{comments[i]}\n */\n" + self.__code
        return self.__code
