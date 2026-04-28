import re
import os
import urllib.request
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

url = "https://www.gutenberg.org/cache/epub/345/pg345.txt"
file = "pg345.txt"

#Checks if file exists
if not os.path.exists(file):
    console.print(f"⏳ [bold green]Downloading[/bold green] [bold cyan]'{file}'...")
    urllib.request.urlretrieve(url,file)
    console.print(f"✅ [bold cyan]'{file}'[/bold cyan] [bold green]download complete[/bold green]")
    print()

def time_stamp():
    return strftime("""[dim]%b-%d-%Y  %I:%M:%S %p[/dim]""").strip()
    
 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
# P-attern finder for known file
def find_first(pattern):
    with open('pg345.txt',encoding = 'utf-8') as file:
        for line in file:
            result = re.search(pattern,line)
            if result != None:
                return result

#P-attern counter for known file
def count_first(pattern):
    count = 0
    with open('pg345.txt',encoding = 'utf-8') as file:
        for line in file:
            result = re.search(pattern,line)
            if result != None:
                count += 1
        return count
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=++++++++++++++++++++++
# for inpput file
def f_first(pattern):
    with open(file_name,encoding="utf-8") as file:
        for line in file:
            result = re.search(pattern,line)
            if result != None:
                return result

#for input file
def c_first(pattern):
    count = 0
    with open(file_name,encoding = 'utf-8') as file:
        for line in file:
            result = re.search(pattern,line)
            if result != None:
                count += 1
        return count


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def render_screen():
    title = "   ⚡ MY TOOL "
    subtitle = "regex CLI Interface"

    
    menu = Group(
    " [violet][01] [/violet] 🔍 [cyan]S-earch F-irst P-attern & C-ount[/cyan]",
    " [violet][02] [/violet] ℹ️  [cyan]i-nfo[/cyan]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [violet][03] [/violet] 📤 [cyan]--use -local <file>[/cyan]",
    " [violet][00] [/violet] 🚪 [cyan]Q-uit[/cyan]"
)

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
    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{time_stamp()}")
    print()
    console.print(Rule(f"[bold {accent_color}] MAIN CONTRO PANEL ", style=accent_color))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Loading animation
def loading_animation(duration=0):
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Loading interface..."),
        transient=True,
    ) as progress:
        task = progress.add_task("load", total=None)
        time.sleep(duration)
loading_animation(duration=2)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


while True:
    render_screen()

    user_input = Prompt.ask("""

     [underline bold green]Choose option[/underline bold  green]  """)
    
    #Error handling
    if user_input not in ("00","01","02","03"):
        print()
        console.print("[bold red]Invalid choice!!! Choose from options[/bold red] [green]00 - 03")
        continue
    
    #Exit loop
    if user_input == "00":
        print()
        console.print("[bold green]Exiting... Goodbye!")
        break
    
    try:
        if user_input == "01":
            print()
            pattern_input = Prompt.ask("[underline bold green]Enter pattern here").strip()

            #find pattern
            result = find_first(pattern_input)
            if result:
                print()
                console.print(f"✅ [bold green]...[bold green][underline bold blue]Found match[/underline bold blue][bold green]...[/bold green]")
                time.sleep(1)
                console.print(f"[underline bold yellow]Match Object[/underline bold yellow][bold magenta] -> {find_first(pattern_input)}")
                console.print(f"[underline bold yellow]Pattern String[/underline bold yellow][bold magenta] -> {result.string}")
            else:
                print()
                console.print(f"✅ [bold green]...[bold green][underline bold blue]No Found match[/underline bold blue][bold green]...[/bold green]")
                console.print(f"❗[bold red]exception,no traces of [/bold red][bold magenta]'{pattern_input}'[/bold magenta] [bold red]found")
        
            #count pattern
            pattern = f'{pattern_input}'
            count = count_first(pattern)
            if result:
                console.print(f"[underline bold yellow]Count[/underline bold yellow][bold magenta] - {count}")
            else:
                console.print(f"❗[bold red]exception,Count of [/bold red][bold magenta]'{pattern}' = 0")
            print()
        
        elif user_input == "02":
           print()
           console.print("""[yellow]This tool allows you to search for a regex pattern in the text file and count its occurrences.[/yellow]
            [underline cyan]You can use regex patterns like :[/underline cyan]
                     [green]'^' for the beginning of a string, 
                     '$' for the end of a string,
                     '\\b \\b' for word boundary,
                     '\\d' for digits, and 
                     '\\s' for whitespace characters.[/green]
            [underline cyan]Example:[/underline cyan] [green]To find lines that start with 'The', you can enter '^The'.
                     To find lines that end with 'play', you can enter 'play$'.
                     To prevent matching inside word 'sea' , you get 'seat',instaed use \\bsea\\b[/green]
            [yellow]To count the occurrences of a pattern, simply enter the pattern and it will return the count.[/yellow]
            """)
        elif user_input == "03":
            print()
            console.print(f"[underline green]Current Dir:[/underline green] [bold white]{os.getcwd()}")
            print()
            file_name = Prompt.ask("[underline bold green]File name")
            if os.path.exists(file_name):
                pattern_input = Prompt.ask("[underline bold green]Enter pattern here")
                result = f_first(pattern_input)
                if result:
                    print()
                    console.print(f"[underline bold yellow]Match Object[/underline bold yellow][bold magenta] -> {result}")
                    console.print(f"[underline bold yellow]Pattern String[/underline bold yellow][bold magenta] -> {result.string}")
                else:
                    print()
                    console.print(f"❗[bold red]exception,no traces of [/bold red][bold magenta]'{pattern_input}'[/bold magenta] [bold red]found")
            else:
                 console.print(f"❌ [bold magenta]'{file_name}'[/bold magenta][red]not found!!!")
            #count pattern
            pattern = f'{pattern_input}'
            count = count_first(pattern)
            if result:
                console.print(f"[underline bold yellow]Count[/underline bold yellow][bold magenta] - {count}")
            else:
                console.print(f"❗[bold red]exception,Count of [/bold red][bold magenta]'{pattern}' = 0")
            print()
                
    except Exception as e:
        print()
        console.print("⚠ [bold red]...exception,search() missing required argument!!!")