from pathlib import Path
import shutil

import questionary
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, BarColumn, TaskProgressColumn, DownloadColumn, TimeRemainingColumn, TextColumn
from yt_dlp import YoutubeDL


def run(console: Console) -> None:
    style = Style(
        [
            ("qmark", "fg:#00ff00 bold"),
            ("question", "fg:#00ff00 bold"),
            ("answer", "fg:#00ff00 bold"),
            ("pointer", "fg:#00ff00 bold"),
            ("highlighted", "fg:#00ff00 bold"),
        ]
    )

    url = questionary.text("Enter the video URL:", style=style).ask()
    if not url:
        console.print(Align.center("[bold yellow]No URL provided. Returning to menu.[/bold yellow]\n"))
        return

    quality_choice = questionary.select(
        "Choose the requested quality:",
        choices=[
            "480p",
            "720p",
            "1080p",
            "2K",
            "4K",
        ],
        style=style,
    ).ask()

    if quality_choice is None:
        console.print(Align.center("[bold yellow]No quality selected. Returning to menu.[/bold yellow]\n"))
        return

    format_choice = questionary.select(
        "Choose the download format:",
        choices=[
            "MP4 (Video + Audio)",
            "MP3 (Audio Only)",
        ],
        style=style,
    ).ask()

    if format_choice is None:
        console.print(Align.center("[bold yellow]No format selected. Returning to menu.[/bold yellow]\n"))
        return

    quality_map = {
        "480p": 480,
        "720p": 720,
        "1080p": 1080,
        "2K": 1440,
        "4K": 2160,
    }
    max_height = quality_map.get(quality_choice, 1080)

    download_dir = Path.home() / "Downloads"
    download_dir.mkdir(parents=True, exist_ok=True)
    output_template = str(download_dir / "%(title)s.%(ext)s")

    ffmpeg_available = shutil.which("ffmpeg") is not None

    if format_choice == "MP4 (Video + Audio)":
        if not ffmpeg_available:
            console.clear()
            console.print(
                Align.center(
                    Panel(
                        "[bold red]FFmpeg is required to merge video and audio for MP4 downloads.[/bold red]\n"
                        "Install ffmpeg and try again.",
                        border_style="red",
                        title="[bold red]ERROR[/bold red]",
                    )
                )
            )
            return

        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "merge_output_format": "mp4",
            "outtmpl": output_template,
            "quiet": True,
            "noprogress": True,
        }
    else:
        if not ffmpeg_available:
            console.clear()
            console.print(
                Align.center(
                    Panel(
                        "[bold red]FFmpeg is required to convert audio to MP3.[/bold red]\n"
                        "Install ffmpeg and try again.",
                        border_style="red",
                        title="[bold red]ERROR[/bold red]",
                    )
                )
            )
            return

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "noprogress": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

    task_id = None
    output_path = None

    def progress_hook(download_data: dict) -> None:
        nonlocal task_id, output_path

        if download_data["status"] == "downloading":
            if task_id is None:
                task_id = progress.add_task("[cyan]Downloading...[/cyan]", total=0)

            total_bytes = download_data.get("total_bytes") or download_data.get("total_bytes_estimate")
            downloaded_bytes = download_data.get("downloaded_bytes", 0)

            if total_bytes:
                progress.update(task_id, total=total_bytes)
            progress.update(task_id, completed=downloaded_bytes)

        elif download_data["status"] == "finished":
            output_path = Path(download_data.get("filename", ""))
            if task_id is not None:
                progress.update(task_id, completed=progress.tasks[0].total or progress.tasks[0].completed)

    ydl_opts["progress_hooks"] = [progress_hook]

    console.clear()
    console.print(Align.center(Panel("[bold green]Preparing download...[/bold green]", border_style="bright_blue")))

    try:
        with Progress(
            SpinnerColumn(style="cyan"),
            TextColumn("{task.description}"),
            BarColumn(bar_width=None),
            TaskProgressColumn(),
            DownloadColumn(),
            TimeRemainingColumn(),
            transient=True,
            console=console,
        ) as progress:
            ydl_opts["progress_hooks"] = [progress_hook]
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        console.clear()
        if output_path:
            console.print(
                Align.center(
                    Panel(
                        f"[bold green]Download complete![/bold green]\nSaved to: [bold cyan]{output_path}[/bold cyan]",
                        border_style="green",
                    )
                )
            )
        else:
            console.print(Align.center(Panel("[bold green]Download complete![/bold green]", border_style="green")))
    except KeyboardInterrupt:
        console.clear()
        console.print(Align.center(Panel("[bold red]Download canceled by user.[/bold red]", border_style="red")))
    except Exception as error:
        console.clear()
        console.print(
            Align.center(
                Panel(
                    f"[bold red]Download failed:[/bold red]\n{error}",
                    border_style="red",
                    title="[bold red]ERROR[/bold red]",
                )
            )
        )
