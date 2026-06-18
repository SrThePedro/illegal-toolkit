from typing import Optional

import questionary
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from illegalkit.tools.downloader import run as downloader_run


def main_menu(console: Console) -> None:
    while True:
        console.print(Align.center(Panel("[bold green]MAIN MENU[/bold green]", border_style="bright_magenta")))
        choice = questionary.select(
            "Choose your mission:",
            choices=[
                "🎬 Video/Audio Downloader (yt-dlp)",
                "❌ Exit",
            ],
            style=Style(
                [
                    ("qmark", "fg:#00ff00 bold"),
                    ("question", "fg:#00ff00 bold"),
                    ("selected", "fg:#00ff00 bold"),
                    ("pointer", "fg:#00ff00 bold"),
                ]
            ),
        ).ask()

        if choice == "🎬 Video/Audio Downloader (yt-dlp)":
            console.print(Align.center("[bold cyan]Launching downloader...[/bold cyan]\n"))
            downloader_run(console)
        elif choice == "❌ Exit":
            console.clear()
            console.print("[bold red]Shutting down IllegalKit...[/bold red]")
            break
        else:
            console.print("[bold yellow]No selection made. Returning to menu.[/bold yellow]\n")
