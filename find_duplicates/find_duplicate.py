import os
import time
import hashlib
import shelve
from rich.console import Console
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.padding import Padding
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
console=Console()

def time_stamp():
    return time.strftime("""[dim]%b-%d-%Y  %I:%M:%S %p""").strip()

def loading_animation(duration=1):
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Loading interface..."),
        transient=True,
    ) as progress:
        task = progress.add_task("load", total=None)
        time.sleep(duration)


def render_screen():
    title = "    ⚡ MY TOOL "
    subtitle = "Duplicate File Finder"

    header_color = "bright_magenta"
    box_color = "cyan"
    accent_color = "bright_green"

    console.clear()

    header = Text(title, style=f"bold {header_color}")
    sub = Text(subtitle, style=accent_color)

    console.print(
        Padding(
            Panel(
                Align.center(header + "\n" + sub),
                border_style=header_color
            ),
            (1, 2)
        )
    )
    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{time_stamp()}")
    print()

def is_path(path, extensions):
    # Only consider regular files (not directories) that match the extension(s)
    if not os.path.isfile(path):
        return False
    if not extensions:
        return True
    if isinstance(extensions, str):
        extensions = [extensions]
    root, ext = os.path.splitext(path)
    return ext in extensions

def add_path(path,db_file):
    with open(path,'rb') as file:
        data = file.read()
        md5_hash = hashlib.md5()
        md5_hash.update(data)
        digest = md5_hash.hexdigest()

        key = digest
        if key not in db_file:
            db_file[key] = [path]
        else:
            next = db_file[key]
            next.append(path)  
            db_file[key] = next

def walk_path(dir_name, extensions, db_file):
    for file in os.listdir(dir_name):
        path = os.path.join(dir_name, file)
        if is_path(path, extensions):
            add_path(path, db_file)
        elif os.path.isdir(path):
            walk_path(path, extensions, db_file)
        else:
            console.print('[bold yellow]Unknown file type: %s' % path)
            print()

def same_content(*paths):
    if len(paths) < 2:
        raise ValueError("Provide at least two files")

    with open(paths[0], "rb") as first_file:
        first_data = first_file.read()

    for path in paths[1:]:
        with open(path, "rb") as file:
            if file.read() != first_data:
                return False

    return True

def find_duplicates(dir_name, extensions):
    with shelve.open('digests','n') as db_file:
        walk_path(dir_name, extensions, db_file)
        for digest,paths in db_file.items():
            if len(paths) > 1:
                # Verify that the files actually have the same content
                if all(same_content(paths[0], path) for path in paths[1:]):
                    console.print('[bold cyan]Duplicate files: %s' % paths)
                    print()
            else:
                console.print('[bold red]Non-duplicate files with the same hash: %s' % paths)
                print()

def main():
    loading_animation()
    while True:
        render_screen()

        # Validate directory input
        while True:
            dir_name = Prompt.ask("[underline bold green]Enter the directory to search for duplicates")
            if os.path.exists(dir_name):
                console.print("[bold green]Directory exists. Proceeding with duplicate search...")
                time.sleep(1)  # Simulate processing time  
                print()
                break
            else:
                console.print('[bold red]Directory does not exist.')
                print()
        
        # Ask for extensions and search
        extension_input = Prompt.ask(
            "[underline bold green]Enter file extension(s) to look for (e.g. .txt or .txt,.py). Leave blank to search all files"
        )
        extensions = [part.strip() for part in extension_input.replace(',', ' ').split() if part.strip()]
        extensions = [part if part.startswith('.') else f'.{part}' for part in extensions]
        print()
        find_duplicates(dir_name, extensions)
        
        # Ask if user wants to search again
        again = Prompt.ask("[underline bold green]Search again?", choices=["y", "n"], default="n")
        print()
        if again.lower() != "y":
            console.print("[bold green]Goodbye!")
            break

if __name__ == "__main__":
    main()