from colorama import init, Fore


def reset_color():
    return '\033[39m'


class ColoredTextHelper:
    @staticmethod
    def start():
        init()

    @staticmethod
    def red(text: str) -> str:
        return f'{Fore.RED}{text}{reset_color()}'

    @staticmethod
    def green(text: str) -> str:
        return f'{Fore.GREEN}{text}{reset_color()}'

    @staticmethod
    def light_red(text: str) -> str:
        return f'{Fore.LIGHTRED_EX}{text}{reset_color()}'

    @staticmethod
    def black(text: str) -> str:
        return f'{Fore.BLACK}{text}{reset_color()}'
