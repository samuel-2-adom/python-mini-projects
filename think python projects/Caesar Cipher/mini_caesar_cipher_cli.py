import os
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

lower = "abcdefghijklmnopqrstuvwxyz"
number1 = range(len(lower))
letter_map1= dict(zip(lower,number1))

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number2 = range(len(upper))
letter_map2 = dict(zip(upper,number2))

#Encode
def encode(word,integer):
    result = []
    for i in word:
        if i in lower:
            old_index = letter_map1[i]
            new_index = (old_index + integer) % 26
            new_letter = lower[new_index]
        elif i in upper:
            old_index = letter_map2[i]
            new_index = (old_index + integer) % 26
            new_letter = upper[new_index]
        else:
            result.append(i)
            continue
        result.append(new_letter)
    joined = "".join(result)
    return joined

#Decode
def decode(word,integer):
    result = []
    for i in word:
        if i in lower:
            old_index = letter_map1[i]
            new_index = (old_index - integer) % 26
            new_letter = lower[new_index]
        elif i in upper:
            old_index = letter_map2[i]
            new_index = (old_index - integer) % 26
            new_letter = upper[new_index]
        else:
            result.append(i)
            continue
        result.append(new_letter)
    joined = "".join(result)
    return joined

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


#render screen
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def render_screen():
    title = "      ⚡ MY TOOL "
    subtitle = "mini Caesar Cipher Interface"
    
    

    menu = [
        "[yellow][01] [/yellow] 🔐 [cyan]Encode(fwd shift) Text - known shift[/cyan]",
        "[yellow][02] [/yellow] 🔓 [cyan]Decode (bwd shift) Text - known shift[/cyan]",
        "[yellow][03] [/yellow] 🔐🔓 [cyan]Encode + Decode Text - known shift[/cyan]",
        "[yellow][04] [/yellow] 🔍 [cyan]Bypass Caesar Cipher - unknown shift[/cyan"
        
    ]
    
    sub_menu_1 = [
    "[yellow][05] [/yellow] 📝 [cyan]Encode File[/cyan]",
    "[yellow][06] [/yellow] 📤 [cyan]Fetch encoded file[/cyan]"
    ]
    
    sub_menu_2 = [
    "[yellow][07] [/yellow] 📝 [cyan]Decode File[/cyan]",
    "[yellow][08] [/yellow] 📤 [cyan]Fetch decoded file[/cyan]",
    " ",
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
                title="[bold]OPTIONS",
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
                title="[bold]ENCODE FILE OPTIONS",
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
                title="[bold]DECODE FILE OPTIONS",
                title_align="left"
            ),
            (1, 4)
        )
    )

    console.print(
        Align.center(
            f"[dim {accent_color}]Select an option using numbers[/dim {accent_color}]"
        )
    )
#*****************************************



while True:
    render_screen()

    user_input = Prompt.ask("""
[underline bold green]Choose Option""").strip()
     
     #Error Handling
    if user_input not in ["00","01","02","03","04","05","06","07","08"]:
        console.print("[bold red]Invalid choice!")
        continue
    
    #Exit loop
    if user_input == "00":
        console.print("[bold green]Exiting... Goodbye!")
        print()
        break

        # Encode
    if user_input == "01":
        try:
            print()
            text_input = Prompt.ask("[underline bold green]Text")
            shift_input = int(Prompt.ask("[underline bold green]Shift integer(positive)",default=int('5')))
            e = encode(text_input,shift_input)
            print()
            console.print(f"✅ [underline bold yellow]Encoded[/underline bold yellow] -> [cyan]{e}")
            print()
        except ValueError:
            console.print("❌ [bold red]Invalid number!!! Try Again")
  
    # Decode
    elif user_input == "02":
        try:
            print()
            text_input = Prompt.ask("[underline bold green]Text")
            shift_input = int(Prompt.ask("[underline bold green]Shift integer(positive)",default=int('5')))
            d = decode(text_input,shift_input)
            print()
            console.print(f"✅ [underline bold yellow]Decoded[/underline bold yellow] -> [cyan]{d}")
            print()
        except Exception as e:
            console.print("❌ [bold red]Invalid number!!! Try Again")

    # Encode & Decode
    elif user_input == "03":
        try:
            print()
            text_input = Prompt.ask("[underline bold green]Text")
            shift_input = int(Prompt.ask("[underline bold green]Shift integer(positive)",default=int('5')))
            print()
            e = encode(text_input,shift_input)
            console.print(f" ✅ [underline bold yellow]Encoded[/underline bold yellow] -> [cyan]{e}")
            d = decode(e,shift_input)
            console.print(f" ✅ [underline bold yellow]Decoded[/underline bold yellow] -> [cyan]{d}")
            print()
        except ValueError:
            console.print("❌ [bold red]Invalid number!!!")
            
    # Bypass
    elif user_input == "04":
            print()
            text_input = Prompt.ask("[underline bold green]Enter encrypted text")
            print()
            console.print("[cyan].....[underline bold green]List of Possible Decryptions[/underline bold green][cyan]......")
            print()
            try:
                for shift in range(1,26):
                    d = decode(text_input,shift)
                    console.print(f"[bold green] ->{d}  [blue]...shift -> [underline cyan]{shift}")
            except Exception as e:
                console.print("❌ [bold red]An exception occurred - digits")
    
    # Encode file
    elif user_input == "05":
        print()
        console.print(f"[underline green]Current Dir:[/underline green] [bold white]{os.getcwd()}")
        print()
        try:
            shift_input = int(Prompt.ask("[underline bold green]Shift integer(positive)",default=int('5')))
            file_input = Prompt.ask("[underline bold green]File name")
            if os.path.exists(file_input):
                with open(file_input,encoding = "utf-8") as file,\
                open("encoded.txt","w",encoding = "utf-8") as write_file:
                    console.print(f"✅ [bold green]...[bold green][bold blue]Encoding '{file_input}'[/bold blue][bold green]...[/bold green]")
                    time.sleep(1)
                    for word in file:
                        e = encode(word,shift_input)
                        write_file.write(e)
                    console.print("✅[bold green]Success : [magenta]encoded to 'encoding.txt'")
            else:
                console.print("❌ [red]not found!!! File does not exist")
        except ValueError:
            console.print("❌ [bold red]Invalid number!!!")

    # Read encoded file
    elif user_input == "06":
        console.print(f"[underline green]Current Dir:[/underline green] [bold white]{os.getcwd()}")
        print()
        file_name = "encoded.txt"
        if os.path.exists(file_name):
            with open(file_name,encoding = "utf-8") as file:
                content = file.read()
                console.print(f"✅ [bold green]Content of [magenta]{file_name} :\n\n[cyan]{content}")
        else:
            console.print("❌ [red]not found!!! encode to fetch encoded file")

    
    # Decode file
    elif user_input == "07":
        console.print(f"[underline green]Current Dir :[/underline green] [bold white]{os.getcwd()}")
        print()
        file_name = "encoded.txt"
        try:
            if Confirm.ask("[underline bold green]Known - shift[/underline bold green] [black]..|..[black] [underline bold red]Unknown - shift[/underline bold red]..."):
                shift_input = int(Prompt.ask("[underline bold green]Shift integer(positive)",default=int('5')))
                if os.path.exists(file_name):
                    with open(file_name,encoding = "utf-8") as file,\
                    open("decoded.txt","w",encoding = "utf-8") as write_file:
                        console.print(f"✅ [bold green]...[bold green][bold blue]Decoding '{file_name}'[/bold blue][bold green]...[/bold green]")
                        time.sleep(1)
                        for word in file:
                            d = decode(word,shift_input)
                            write_file.write(d)
                        console.print("✅[bold green]Success : [magenta]decoded to 'decoded.txt'")
                else:
                    console.print("❌ [red]not found!!! File does not exist")
            else:
                if os.path.exists(file_name):
                    with open(file_name,encoding = "utf-8") as file,\
                    open("decoded.txt","w",encoding = "utf-8") as write_file:
                        word = file.read()
                        console.print(f"✅ [bold green]...[bold green][bold blue]Decoding '{file_name}'[/bold blue][bold green]...[/bold green]")
                        time.sleep(1)
                        for shift in range(1,26):
                            d = decode(word,shift)
                            write_file.write(f"shift -> {shift} : {d}\n\n")
                        console.print("✅[bold green]Success : [magenta]decoded to 'decoded.txt'")
                else:
                    console.print("❌ [red]not found!!! File does not exist")
        except ValueError:
            console.print("❌ [bold red]Invalid number!!!")
    
    # Read decoded file
    elif user_input == "08":
        console.print(f"[underline green]Current Dir :[/underline green] [bold white]{os.getcwd()}")
        print()
        file_name = "decoded.txt"
        if os.path.exists(file_name):
            with open(file_name,encoding = "utf-8") as file:
                content = file.read()
                console.print(f"✅ [bold green]Content of [magenta]{file_name} :\n\n[cyan]{content}")
        else:
            console.print("❌ [red]not found!!! decode to fetch decoded file")