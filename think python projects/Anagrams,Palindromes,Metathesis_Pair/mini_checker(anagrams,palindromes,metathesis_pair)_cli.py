import os
import urllib.request
from time import strftime
import time
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.rule import Rule
from rich.padding import Padding
from rich.prompt import Confirm
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
console = Console()

url = url = "https://www.gutenberg.org/files/3201/files/crosswd.txt"
file = "words.txt"
#Checks if file exists else download file
if not os.path.exists(file):
    console.print(f"⏳ [bold green]Downloading[/bold green] [bold cyan]'{file}'...")
    urllib.request.urlretrieve(url,file)
    console.print(f"✅ [bold cyan]'{file}'[/bold cyan] [bold green]download complete[/bold green]")
    print()

#Word list
with open("words.txt") as file:
    word_list = file.read().split()


#Anagram function
def is_anagram(word1,word2):
    return "".join(sorted(word1)) == "".join(sorted(word2))

#Palindrome Function
def is_palindromes(x):
    a = "".join(reversed(x))
    if not x == a:
        return False
    else:
        return True
    
#Reverse function
def reverse(x):
    return "".join(reversed(x))

#Metathesis pair function
def is_meta_pair(word1,word2):
    differ = []
    if not is_anagram(word1,word2):
        return False
    for w1,w2 in zip(word1,word2):
        if w1 != w2:
            differ.append((w1,w2))
    if len(differ) != 2:
        return False
    if not differ[0] == differ[1][::-1]:
        return False
    return True

def time_stamp():
    return strftime("""[dim]%b-%d-%Y  %I:%M:%S %p[/dim]""").strip()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def render_screen():
    title = "    ⚡ MY TOOL "
    subtitle = "Checker CLI Interface"
    
    

    menu = [
        "[yellow][01] [/yellow] 🔍 [cyan]Lookup Anagrams[/cyan]",
        "[yellow][02] [/yellow] 📖 [cyan]All Anagrams[/cyan]",
    ]
    
    sub_menu_1 = [
    "[yellow][03] [/yellow]🔍 [cyan]Lookup Palindromes[/cyan]",
    "[yellow][04] [/yellow]📖 [cyan]All Palindromes[/cyan]"
    ]
    
    sub_menu_2 = [
    "[yellow][05] [/yellow]🔍 [cyan]Lookup Metathesis pair[/cyan]",
    "[yellow][06] [/yellow]📖 [cyan]All Metathesis pair[/cyan]",
    " ",
    "[yellow][07] [/yellow]💡 [cyan]About[/cyan]",
    "[yellow][00] [/yellow]🚪 [cyan]Exit[/cyan]"
    ]
    

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

    console.print(Rule(f"[bold {accent_color}] MAIN CONTRO PANEL ", style=accent_color))

    console.print(
        Padding(
            Panel(
                Align.left("\n".join(menu)),
                border_style=box_color,
                title="[bold]Anagrams",
                title_align="left"
            ),
            (1, 4)
        )
    )
 
    console.print(
        Padding(
            Panel(
                Align.left("\n".join(sub_menu_1)),
                border_style=box_color,
                title="[bold]Palindromes",
                title_align="left"
            ),
            (1, 4)
        )
    )
    
    console.print(
        Padding(
            Panel(
                Align.left("\n".join(sub_menu_2)),
                border_style=box_color,
                title="[bold]Metathesis pair",
                title_align="left"
            ),
            (1, 4)
        )
    )

    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{time_stamp()}")
    print()
    console.print(
        Align.center(
            f"[dim {accent_color}]Select an option using numbers[/dim {accent_color}]"
        )
    )

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

while True:

    render_screen()

    #user input
    user_input = Prompt.ask("""
   [underline bold green][ + ][/underline bold green] [underline bold yellow]Choose option[/underline bold yellow]""").strip()
    
    #Error handling
    if user_input not in ("00","01","02","03","04","05","06","07"):
        print()
        console.print("[bold red]Invalid Option[/bold red]!!! [cyan]Choose from 01 - 07")
        continue
    
    #Exit loop
    if user_input == "00":
        print()
        console.print("[bold green]Exiting... Goodbye!")
        time.sleep(1)
        break
    
   
    found = False
    #Lookup for Anagarams
    if user_input == "01":
        print()
        anagram_input = Prompt.ask("[underline bold yellow]Enter word here").strip().lower()
        for char in word_list:
            if char != anagram_input and is_anagram(char,anagram_input):
                console.print(f"[underline bold green]Anagram[/underline bold green] [cyan]: {char}")
                found = True
        if not found:
            print()
            console.print("🚫 [bold red]No anagrams found")
            
    

    #All Anagrams
    elif user_input == "02":
        console.print("\n[underline bold blue]...Anagram Pairs...[/underline bold blue]\n")
        for i in range(len(word_list)):
            for j in range(i + 1,len(word_list)):
                word1 = word_list[i]
                word2 = word_list[j]
                if is_anagram(word1,word2):
                    console.print(f"[underline bold green]Anagram[/underline bold green] [cyan]->{word1}[/cyan]   [magenta]{word2}")
    
    
    
    #Lookup for Palindromes
    elif user_input == "03":
        print()
        palindrome_input = Prompt.ask("[underline bold yellow]Enter word here").strip().lower()
        for char in word_list:
            if char == palindrome_input and is_palindromes(char):
                console.print(f"[underline bold green]Palindrome[/underline bold green] [cyan]: {char}")
                found = True
        if not found:
            print()
            r = reverse(palindrome_input)
            console.print(f"🚫 [bold red]No Palindrome found[/bold red] [bold green]- reversed =[/bold green] [magenta]{r}") 
        
        
    #All Palindromes
    elif user_input == "04":
        print()
        console.print("[underline bold blue]...Palindromes...[/underline bold blue]\n")
        print()
        for char in word_list:
            if is_palindromes(char):
                console.print(f"[underline bold green]Palindrome[/underline bold green] [cyan]-> [magenta]{char}")
    
    #Lookup for Meta_Pair
    elif user_input == "05":
        print()
        meta_input = Prompt.ask("[underline bold yellow]Enter word here").strip().lower()
        for char in word_list:
            if meta_input != char and is_meta_pair(meta_input,char):
                console.print(f"[underline bold green]Meta_Pair[/underline bold green] [cyan]-> {char}")
                found = True
        if not found:
            console.print("🚫 [bold red]No Meta_Pairs found")
        
    
    #All meta_pair
    elif user_input == "06":
        console.print("\n[underline bold blue]...Anagram Pairs...[/underline bold blue]\n")
        for i in range(len(word_list)):
            for j in range(i + 1,len(word_list)):
                word1 = word_list[i]
                word2 = word_list[j]
                if is_meta_pair(word1,word2):
                    console.print(f"[underline bold green]Meta_Pairs[/underline bold green] [cyan]->{word1}[/cyan]   [magenta]{word2}")
    
    #About
    elif user_input == "07":
        console.print("""
[underline bold yellow]Anagrams[/underline bold yellow] [bold green]- A word formed by rearranging the letters of another word.[/bold green]
        [underline bold cyan]Example[/underline bold cyan] [bold green]: 'listen' - 'silent','enlist','inlets'[/bold green]

[underline bold yellow]Palindromes[/underline bold yellow] [bold green]- A word or phrase that reads the same forward and backward.[/bold green]
        [underline bold cyan]Example[/underline bold cyan] [bold green]: 'rotator'- 'rotator' , 'racecar' - 'racecar'[/bold green]

[underline bold yellow]Metathesis Pair[/underline bold yellow] [bold green]- Two words formed by swapping the positions of letters in each other.[/bold green]
        [underline bold cyan]Example[/underline bold cyan] [bold green]: 'form' 'n 'from'[/bold green]
 """)