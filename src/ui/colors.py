from rich.console import Console

console = Console()

_STYLES = {
    "red": "bold red",
    "green": "bold green",
    "yellow": "bold yellow",
    "white": "white",
}

def color_text(text, color):
    console.print(text, style=_STYLES.get(color, "white"))
