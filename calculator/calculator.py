from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.padding import Padding
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
import os
import platform
import time
console = Console()


# Clear screen after each action to keep the interface clean and user-friendly
def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def time_stamp():
    return time.strftime("""[dim]%b-%d-%Y  %I:%M:%S %p""").strip()

def add(num1,num2):
    return num1 + num2

def subs(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    if num2 == 0:
        print()
        console.print("[bold red]Error❗, cannot divide by 0")
        print()
    else:
        return num1 / num2 

def pow(num1,num2):
    return num1 ** num2

def loading_animation(duration=1):
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Loading interface..."),
        transient=True,
    ) as progress:
        task = progress.add_task("load", total=None)
        time.sleep(duration)


def render_screen():
    title = "        ⚡ MY TOOL "
    subtitle = "mini Calculator CLI Interface"

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

def calc():
    loading_animation(duration=1)
    while True:
        clear_screen()
        render_screen()


        #First Input
        while True:
            try:
                num_1 = int(Prompt.ask("[underline bold green]Enter 1 number here"))
                break
            except ValueError:
                console.print("[bold red]invalid number❗, Try again❌")
                print()
                
        #Second Input
        while True:
            try:
                num_2 = int(Prompt.ask("[underline bold green]Enter 2 number here"))
                print()
                break
            except ValueError:
                console.print("[bold red]invalid number❗, Try again❌")
                print()
        
        #Operator Input
        while True:
            operation = Prompt.ask("""[bold blue]input operation type[/bold blue]
    [bold green](+) (-) 
    (/) (*) 
    (**)[/bold green]
    [bold red]'q' 'quit'""")
            exit = ["q","quit","close"]
            if operation in exit:
                console.print("[bold green]Goodbye,🤗 f.a.m")
                quit()
                print()
            sum = ['+','-','/','*','**']
            if operation not in sum:
                console.print("[bold red]invalid operation!, Try again👀")
                print()
            else:
                break
        
        #Operation   
        try:
            print()
            console.print("[bold green]Calculating...⏳")
            time.sleep(1)

            ans = None
            if operation == '+':
                ans = add(num_1,num_2)
            elif operation == '-':
                ans = subs(num_1,num_2)
            elif operation == '/':
                ans = div(num_1,num_2)
            elif operation == '*':
                ans = mul(num_1,num_2)
            elif operation == '**':
                ans = pow(num_1,num_2)
            if ans != None:
                console.print()
                console.print(f"✅[bold yellow]Answer is: [/bold yellow][magenta]{ans}")
                print()
        except Exception as e:
            console.print("[bold red]Number too large to compute safely.")
            print()
        Prompt.ask("[bold green]Press Enter to continue...")

if __name__ == "__main__":
    calc()  