import os

from revChatGPT.ChatGPT import Chatbot
from Prompt import Prompt
from Splitter import Splitter


class AutoDoc:
    supported_languages = ["py"]

    def __init__(self, token_path: str):
        self.token_path = token_path
        self.token = None
        self.conversation = None
        self.file_path = None
        self.file_content = None
        self.example_path = None
        self.example_content = None
        self.language = None
        self.splited_content = []
        self.result = []

    def add_file(self, file_path: str):
        self.file_path = file_path
        return self

    def add_example(self, example_path: str):
        self.example_path = example_path
        return self

    def start(self):
        self.__load_token__()
        self.__create_chatbot__()
        self.__define_language__()
        self.__load_content__()
        self.splited_content = Splitter(self.content, self.language).split()

        if self.example_path:
            self.__load_example__()
        for entity in self.splited_content:
            response = self.__ask__(entity)
            self.result.append(response)
        self.__create_file_()

    def __ask__(self, code) -> str | None:
        try:
            if self.example_path:
                response = self.chatbot.ask(
                    Prompt("example", code, self.example_content).create(), conversation_id=self.conversation, parent_id=None)
            else:
                response = self.chatbot.ask(
                    Prompt(self.language, code).create(), conversation_id=self.conversation, parent_id=None)
            if response:
                if not self.conversation:
                    self.conversation = response["conversation_id"]
                return response["message"][3:-3]
            return ""
        except:
            self.__ask__(code)

    def __create_chatbot__(self):
        self.chatbot = Chatbot({
            "session_token": self.token
            }, conversation_id=None, parent_id=None)

    def __load_token__(self):
        self.token: str = open(self.token_path, "r").read()
        if not isinstance(self.token, str) or len(self.token) == 0:
            print("Invalid token")
            exit(0)

    def __load_content__(self):
        self.file_content: str = open(self.file_path, "r").read()
        if not isinstance(self.token, str) or len(self.token) == 0:
            print("Code file is empty")
            exit(0)

    def __load_example__(self):
        self.example_content: str = open(self.example_path, "r").read()
        if not isinstance(self.token, str) or len(self.token) == 0:
            print("Example file is empty")
            exit(0)

    def __define_language__(self):
        lang: str = self.file_path.split(".")[-1]
        if lang in self.supported_languages:
            self.language = lang
        else:
            print(f".{lang} language not supported")
            exit(0)

    def __create_file_(self):
        path = os.path.join(os.path.dirname(self.file_path),
                            os.path.basename(self.file_path).split('.')[0] + f".commented_{self.language}")
        open(path, "x").write("\n".join(self.result))

