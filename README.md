# AutoDoc-ChatGPT

This is a ChatGPT based prompt generation model for MidJorney. The purpose of this model is to simplify the creation of images and increase their creativity. By introducing a partial hint, ChatGPT creates a follow-up that can be used to stimulate creativity and provide new ideas.

## Getting Started

### Installing

Clone this repository to your local machine:

```bash
git clone https://github.com/awekrx/AutoDoc-ChatGPT.git
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

## Supported programming languages
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="python" width=100 />


## Usage

### Edit config

Open `config.ini` and add `email` and `password` there if you are not using OAuth authorization.
Otherwise open [ChatGPT](https://chat.openai.com) and get the `__Secure-next-auth.session-token` cookieand write it to the `session-token`.

### Start

```bash
py main.py -file "path to the file"
```

The path to the file can be either relative or absolute.

After execution, the file `yourfilename_commented.language` is created in the folder with the desired file.

![Usage preview](./images/usage-preview.png)

## Alternative usage

You can also use this as a function in python.

```python
from modules.autodoc import AutoDoc
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

auth = {
    "email": config["ChatGPT"]["email"],
    "password": config["ChatGPT"]["password"],
    "session_token": config["ChatGPT"]["session_token"]
}

result = AutoDoc(
        auth,
        "Code for commenting",
        "language code. P.S. See Supported languages",
    ).start()
print(result)
# out: Code with comments
```

## Disclaimer
Doesn't always create correct comments. It doesn't always mean what you want. Use as a draft of comments that may need to be edited.


## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks a lot to the development of AI and separately to [СhatGPT](https://chat.openai.com) for generating the Readme.
And also [acheong08](https://github.com/acheong08) for creating [ChatGPT](https://github.com/acheong08/ChatGPT).

## Future

Add JavaScript, C#, C++, Go and other languages...