import os
import urllib.request
import random
import unicodedata
import time
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.padding import Padding
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
from rich.console import Console
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
loading_animation()

def render_screen():
    title = "     ⚡ MY TOOL "
    subtitle = "Text Analysis + Generation"

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


def open_text(path, mode='r', encoding='utf-8', errors='replace'):
    """Open a text file with a safe default that replaces undecodable bytes.

    Use `errors='replace'` so files with Windows-1252 or other single-byte
    characters don't raise UnicodeDecodeError when read.
    """
    return open(path, mode, encoding=encoding, errors=errors)


def is_special_line(line):
    return line.startswith("*** ")

# Gets the frequency of each word and and prints most common
def most_common(word_counter, n=5, reverse=True):
    sorts = sorted(word_counter.items(), key=lambda x: x[1], reverse=reverse)
    for word,freq in sorts[:n]:
        console.print(f'[yellow]{freq}', f'[blue]{word}', sep='\t')

# Replace hyphen with a space and returns the of text split into individual words
def split_text(line):
    """Splits file into a list of individual words"""
    return line.replace('—', ' ').split()

# Cleans the text by removing punctuations and lower them
def clean_text(text,punctuation):
    """Cleans the text by removing leading/trailing whitespace and normalizing Unicode."""
    return text.strip(punctuation).lower()

# Return a dictionary of words in d1 that are not in d2
def sub(d1,d2):
    result = {}
    for key in d1:
        if key not in d2:
            result[key] = d1[key]
    return result

# Create a successor map for n_grams
successor_map = {}
def add_n_gram(n_gram):
    key = tuple(n_gram[:-1])
    value = n_gram[-1]
    if key not in successor_map:
        successor_map[key] = [value]
    else:
        successor_map[key].append(value)

def generate_text(input_text,length):
    n_gram = input_text
    for i in range(length):
        # Implementation for generating text
        successor = successor_map.get(n_gram,[])
        if not successor:
            console.print("[underline bold red]No mapped successors found!!!")
            break
        next_word = random.choice(successor)
        console.print(f"[blue]{next_word}", end=' ')
        n_gram = (*n_gram[1:], next_word)

#*********************************************************************************************
def text_gen_anl():
    while True:
        render_screen()

        ### Get the file name from the user
        console.print('[underline bold magenta]Step 1 - Text Analysis')
        while True:
            read_input = Prompt.ask('[underline bold green]Enter the name of the file to analyze   (leave blank for default)')
            if not read_input:
                file = "dr_jekyll.txt"
                url = "https://dl.dropboxusercontent.com/scl/fi/2gc8s165f5el55o535f3d/dr_jekyll_cleaned.txt?rlkey=31p5nfo98nb1d283yn3orscat&st=4a95dho1"

                #Checks if file exists
                if not os.path.exists(file):
                    urllib.request.urlretrieve(url,file)
                read_input = file
                break
            elif not os.path.exists(read_input):
                print("Invalid relative path")
            else:
                break
            


        ### Get the punctuation characters from the file
        punc = {}
        with open_text(read_input) as file:
            for line in file:
                for char in line:
                    category = unicodedata.category(char)
                    if category.startswith('P'):
                        punc.setdefault(char, 1)
        punctuation = ''.join(punc)

        ###Count frequency of each word in file and store in a dictionary
        word_counter = {}
        with open_text(read_input) as file:
            for line in file:
                for text in split_text(line):
                    text = clean_text(text,punctuation)
                    word_counter[text] = word_counter.get(text, 0) + 1
        most_common(word_counter)
        console.print(f"[bold green]File Analyzed(lowered & cleaned):[/bold green] [blue]{read_input}")
        print()

        # Get the unique words in the spell-check list and store in a dictionary
        url = url = "https://www.gutenberg.org/files/3201/files/crosswd.txt"
        file = "words.txt"
        spell_check = file
        #Checks if file exists else download file
        if not os.path.exists(file):
            urllib.request.urlretrieve(url,file)
            

        unique_words = {}
        with open_text(spell_check) as file:
            word_list = file.read().split()
            for keys in word_list:
                unique_words[keys] = 1

        # Get the flagged words that are not in the spell-check list and print the last 20
        console.print("[underline bold green]Last 20 Flagged Words — Words not in Spell-Check list(Rare/Proper words,singled letters/digits or mispelled words):")
        diff = sub(word_counter, unique_words)
        singletons = []
        for key,value in diff.items():
            if value == 1:
                singletons.append(key)
        console.print(f'[blue]{singletons[-20:]}')
        print()

        # Text generation using n-grams
        console.print("[underline bold magenta]Step 2 - Text Generation")

        # Get module
        module_input = Prompt.ask(
            """[bold green] list of modules:
                [2] module_1 - Unigram
                [3] module_2 - Biagram
                [4] module_3 - Triagram
                [5] module_4 - Quadgram
                [6] module_5 - five-gram
    Available Options 2,3,4,5,6... (default)""",
            default="5",
        )

        try:
            module = int(module_input) if module_input.strip() else 5
            if module not in range(2,51):
                raise ValueError
        except (ValueError, TypeError):
            module = 5

        choose = ['[bold green]Active module :']
        for i in choose:
            if module == 2:
                console.print(i,"[underline bold brown]Unigram")
            elif module == 3:
                console.print(i, "[underline bold black]Biagram")
            elif module == 4:
                console.print(i,"[underline bold magenta]Triagram")
            elif module == 5:
                console.print(i,"[underline bold cyan]Quadgram")
            elif module == 6:
                console.print(i,"[underline bold blue]five-gram")
            else:
                console.print(i,f"[underline bold yellow]{module}-gram")

        # Create a sliding window to process n_grams
        window = []
        def process_n_gram(text, module):
            window.append(text)
            if len(window) == module:
                add_n_gram(window)
                window.pop(0)

        # Add Create successor_map
        with open_text(read_input) as file:
            for line in file:
                for text in split_text(line):
                    text = clean_text(text,punctuation)
                    process_n_gram(text, module)

        # Get successor_map
        word = random.choice(list(successor_map.items()))
        console.print(f"[underline bold green]Random successor_map of Active module:[/underline bold green] [bold blue]{word}")
        print()


        # Input length of words
        try:
            length = Prompt.ask("[underline bold green]Enter number of words (default 20)")
            length = int(length) if length else 20
        except ValueError:
            length = 20

        # Input pattern for generation
        raw_input = Prompt.ask(f"[underline bold green]Enter {module-1} words to start the text generation (leave blank for random)")
        input_text = tuple(raw_input.split()) if raw_input.strip() else ()
        if not input_text:
            input_text = random.choice(list(successor_map))


        console.print(f"[bold blue]{' '.join(input_text)}:", end=' ')
        generate_text(input_text, length)
        print("\n")
        # Ask if user wants to search again
        again = Prompt.ask("[underline bold green]Search again?", choices=["y", "n"], default="n")
        print()
        if again.lower() != "y":
            console.print("[bold green]Goodbye!")
            break

if __name__ == "__main__":
    text_gen_anl()