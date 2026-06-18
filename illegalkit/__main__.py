from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from illegalkit.menu import main_menu


def main() -> None:
    console = Console()
    banner = Panel(
        Align.center("[bold green]IllegalKit[/bold green]\n[cyan]Terminal utility toolkit[/cyan]", vertical="middle"),
        title="[bold magenta]WELCOME[/bold magenta]",
        subtitle="[green]ctrl+c to quit[/green]",
        border_style="bright_blue",
        padding=(1, 2),
    )

    try:
        console.clear()
        console.print(Align.center(banner))
        main_menu(console)
        console.clear()
    except KeyboardInterrupt:
        console.clear()
        console.print("\n[bold red]Interrupted by user. Exiting...[/bold red]")


if __name__ == "__main__":
    main()
