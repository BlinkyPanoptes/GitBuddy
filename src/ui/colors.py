from colorama import Fore, Style

def color_text(text, color):
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN
    }

    print(colors.get(color, Fore.WHITE) + text + Style.RESET_ALL)