import os
import re
import time
from time import strftime
from rich.console import Console,Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.rule import Rule
from rich.padding import Padding
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.columns import Columns
from rich.prompt import Prompt
console = Console()


#Get readable size
def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024

#Reads file
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        content = file.read().strip()
        console.print(content if content else "[underline bold red][File is empty]")

#Gets folder directory
def get_dir():
    console.print("[cyan]...[/cyan][underline bold blue]Preparing dir list[/underline bold blue][cyan]...")
    time.sleep(1)
    console.print(f"[underline bold yellow]current directory >[/underline bold yellow][bold white]{os.getcwd()}[/bold white]")
    time.sleep(1)
    console.print("[bold blue]-" * 30)
    entry = os.listdir()
    console.print("\n".join(sorted(entry)))
    console.print("[bold blue]-" * 30)
    return ""

#Delete a file
def delete_file(file_name):
    if os.path.exists(file_name):
        console.print(f"[bold red]Deleting file[/bold red] [blue]'{file_name}'...[/blue]")
        time.sleep(1)
        os.remove(file_name)
        console.print(f"[bold green]file[/bold green] [blue]'{file_name}'[/blue] [bold green]deleted[/bold green]")
    else:
        console.print(f"[bold yellow]file[/bold yellow] [blue]'{file_name}'[/blue] [bold yellow]does not exist[/bold yellow]")

#Timestamp
def time_stamp():
    return strftime("""%b-%d-%Y  %I:%M:%S %p""").strip()

#Change directory
def change_dir(path):
    os.chdir(path)
    console.print(f"[bold blue]directory... changed! to '[/bold blue] [bold white]{os.getcwd()}[/bold white]")
    return ""
    
#Pattern Search
def find_first(pattern,file_name):
    with open(file_name,encoding = "utf-8") as file:
        for line in file:
            result = re.search(pattern,line)
            if result != None:
                return result

#Pattern Count
def count_first(pattern,file_name):
        count = 0
        with open(file_name,encoding = "utf-8") as file:
            for line in file:
                result = re.search(pattern,line)
                if result != None:
                    count += 1
            return count
                
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def render_screen():
    title = "     ⚡ MY TOOL "
    subtitle = "mini Notes CLI Interface"

    header_color = "bright_magenta"
    box_color = "gold"
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


    #**********************************************
    menu = Group(
    " [violet][01] [/violet]🔄 [cyan]List Dir[/cyan]",
    " [violet][02] [/violet]📂 [cyan]Change Directory[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [violet][03] [/violet]📬 [cyan]Fetch Notes| R[/cyan]",
    " [violet][04] [/violet]🧷 [cyan]Delete Notes[/cyan]"
)
    

    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)
    #***********************************************

    menu = Group(
    " [yellow][05][/yellow] 💾 [cyan]Create | C[/cyan]",
    " [yellow][06][/yellow] 💾 [cyan]Truncate | T[/cyan]",
    " [yellow][07][/yellow] 💾 [cyan]Append To | A[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    " [yellow][08][/yellow] 🔍 [cyan]Search - Pattern & Count[/cyan]",
    " [yellow][00][/yellow] 🚪 [cyan]Exit[/cyan]",
)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]NOTES OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)
    #**************************************************

    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{time_stamp()}")
    console.print()
    console.print(Rule(f"[bold {accent_color}] MAIN CONTRO PANEL ", style=accent_color))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Loading animation
def loading_animation(duration=0):
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Loading interface..."),
        transient=True,
    ) as progress:
        task = progress.add_task("load", total=None)
        time.sleep(duration)
loading_animation(duration=1)


#Loop
while True:
    render_screen()

    #Choice Input
    choice = Prompt.ask("""
        [green][ + ] [underline bold green]Select Option[/underline bold green]""").strip()
    print()
    
    
    # * Choice Error Handling 0
    if choice not in ["01","02","03","04","05","06","07","08","00"]:
        console.print("[bold red]Invalid choice! Select from 01 - 09.")
        print()
        continue
    
    #Quit
    if choice == "00":
        console.print("🚪 [bold green]Exiting note app...")
        time.sleep(1)
        break
       
     #Get dir
    if choice == "01":
        print(get_dir())
        print()
        continue
    
    #Change dir
    if choice == "02":
        console.print("""[bold green]Example : /path/to/your/folder | folder name in current directory ---- [/bold green][blue]'Downloads','Document'""")
        try:
            dir_change = Prompt.ask("[underline bold green]change dir to[/underline bold green]").strip()
            print(change_dir(dir_change))
        except FileNotFoundError:
            console.print("🧾 [bold red]No path found")
        except OSError:
            console.print("🧾 [bold red]No input given for directory change, skipping...")
            time.sleep(1)
        continue

    #file name input
    file_name = Prompt.ask("[bold green]Notes name (.txt)[/bold green]").strip()
    console.print()

    # Reads - file name input
    if choice == "03":
        if os.path.exists(file_name):
            console.print("ℹ ℹ[bold yellow]...Reading...Triggered...\n")
            time.sleep(1)
            read_file(file_name)
            console.print()

            size = os.path.getsize(file_name)
            console.print(f"[underline yellow]File size:[/underline yellow] [blue]{size}[/blue] [cyan]bytes")
            console.print(f"[underline yellow]File size:[/underline yellow] [blue]{human_readable_size(size)}[/blue]")
            console.print("[blue]-" * 30)
            console.print()
        else:
            console.print(f"🧾 [bold red]Notes '{file_name}' not in [/bold red][underline bold yellow]current directory[/underline bold yellow][bold white] > {os.getcwd()}[/bold white].")
            console.print()


    # Trigger notes input
    # * notes input for create,truncate,append options
    if choice in ["05", "06","07"]:
        user_input = Prompt.ask("[underline bold green]Taking Notes[/underline bold green]")
        console.print()
    
    #Delete file
    if choice == '04':
        delete_file(file_name)
        print()
        continue


      # Create new file Note
    elif choice == "05":
        if not os.path.exists(file_name):
            with open(file_name, "x", encoding="utf-8") as write_file:
                console.print("✅ [yellow]Creating notes...")
                time.sleep(1)
                write_file.write(f"{time_stamp()} | C | {file_name}\n")
                write_file.write(user_input)
                console.print("✅ [yellow]Notes created!")
                console.print(f"[bold yellow]Total length ->[/bold yellow] [cyan]{len(user_input)}")
                console.print()
        else:
            console.print(f"🧾 [bold red]File '{file_name}' already exists!!")
            console.print()


     # Truncate - existing Note or create new
    elif choice == "06":
        with open(file_name, "w", encoding="utf-8") as write_file:
            console.print("✅ [yellow]Truncating notes...")
            time.sleep(1)
            write_file.write(f"{time_stamp()} | T | {file_name}\n")
            write_file.write(user_input)
            console.print("✅ [yellow]Note truncated!")
            console.print(f"[bold yellow]Total length ->[/bold yellow] [cyan]{len(user_input)}")
            console.print()
            
   
    # Append/overwrite - file name input or create n. with timedatestamp
    elif choice == "07":
        if os.path.exists(file_name):
                with open(file_name, "a", encoding="utf-8") as write_file:
                    console.print("✅ [yellow]Appending notes...")
                    time.sleep(1)
                    write_file.write(f"\n{time_stamp()} | A | {file_name} \n{user_input}\n")
                    console.print("✅ [yellow]Notes appended!")
                    console.print(f"[bold yellow]Total length ->[/bold yellow] [cyan]{len(user_input)}")
                    console.print()
        else:
            console.print(f"❌ [red]File '{file_name}' not found!")
            console.print()


    
    
    # Search - Pattern finder & Counter
    if choice == '08':
        try:
            console.print(f"[blue] -" * 30)
            pattern = Prompt.ask("[underline bold green]Enter pattern")
            result = find_first(pattern,file_name)
            console.print(f"[bold yellow]Pattern ->[/bold yellow] [green]{result.group()}[/green]")
            console.print(f"[bold yellow]first Apperarance ->[/bold yellow] [cyan]{result.string}[/cyan]")
            console.print(f"[bold yellow]Count ->[/bold yellow] [magenta]{count_first(pattern,file_name)}[/magenta]")
            console.print("[blue] -" * 30)
        except FileNotFoundError:
            console.print("❌ [red]File not found, path missing!")
        except AttributeError:
            console.print("❌ [red]Pattern Not Found!")
            console.print()
        continue
