import os
import string
import random
import platform
from datetime import datetime
import json
from time import sleep, strftime
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

# ID for Notes
def notes_id():
    digits = string.digits
    return "".join(random.choices(digits,k=5))

# Get Date and Time
def format():
    now = datetime.now()
    return now.strftime("%Y-%m-%d | %I:%M:%S %p")

def char_count(words):
    count = 0
    for char in words:
        char = len(char.strip())
        count += char
    return count

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


# Rich UI design for the CLI interface
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def render_screen():
    title = "     ⚡ MY TOOL "
    subtitle = "mini NoteManager CLI Interface"

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
    " [red][0] [/red]🔴 [bold red]Exit[/bold red]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [blue][1] [/blue]➕ [bold blue]Save Note[/bold blue]",
    " [yellow][2] [/yellow]➖ [bold yellow]Delete Note[/bold yellow]",
    " [green][3] [/green]📋 [bold green]List All Notes[/bold green]",
)
    

    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]NOTE OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)
    #***********************************************

    menu = Group(
    " [blue][4][/blue] 🔁 [bold blue]Sort Note(Time)[/bold blue]",
    " [green][5][/green] 📖 [bold green]Edit Note(ID)[/bold green]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge
    
    " [blue][6][/blue] ⭐ [bold blue]Togle as Favorite(ID)[/bold blue]",
    " [magenta][7][/magenta] 🟢 [bold magenta]Pin A Note(ID)[/bold magenta]",
    " [yellow][8][/yellow] 🔴  [bold yellow]Unpin A Note(ID)[/bold yellow]",
)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]FUNCTIONALITY OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)

#**********************************************
    menu = Group(
    " [red][9] [/red]🚀 [bold red]Load Note(ID)[/bold red]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [blue][10] [/blue]⭐ [bold blue]Favorite Notes[/bold blue]",
    " [yellow][11] [/yellow]🧷 [bold yellow]Pinned Notes[/bold yellow]",
)
    

    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]FILTER OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)


#**********************************************
    menu = Group(
    " [red][12] [/red]🔍 [bold red]Search By Title[/bold red]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [blue][13] [/blue]🔍 [bold blue]Search By Tag[/bold blue]",
)
    

    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]SEARCH OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)
    #**************************************************

    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{format()}")
    console.print()
    console.print(Rule(f"[bold {accent_color}] MAIN CONTRO PANEL ", style=accent_color))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Loading animation
def loading_animation(duration=1):
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Loading interface..."),
        transient=True,
    ) as progress:
        task = progress.add_task("load", total=None)
        sleep(duration)
loading_animation()
#***********************************************************************************************


# Class Note
class Note: 
    def __init__(self,title,content,updated_at=None,id=None,created_at=None,favorite=None,pinned=None,category=None):
        
        self.title = title
        self.content = content
        self.id = id
        self.created_at = format()
        self.updated_at = updated_at
        self.favorite = favorite
        self.pinned = pinned
        self.category = category
        
    def __eq__(self,other):
        return self.title == other.title
    
    def __lt__(self,other):
        return (self.created_at < other.created_at)
        
    def __str__(self):
        return f"""title : {self.title}
content : {self.content}
id : {self.id}
created_at : {self.created_at}
updated_at : {self.updated_at}
tags : {self.category}
"""
    # Convert Note object to Dictionary
    def note_to_dict(self):
        return {"title" : self.title,
        "content" : self.content,
        "updated_at" : self.updated_at,
        "id" : self.id,
        "created_at" : self.created_at,
        "favorite" : self.favorite,
        "pinned" : self.pinned,
        "tags" : self.category}
    
    # Converts from Dictionary to Note object
    @staticmethod
    def dict_to_note(n_dict):
        return Note(n_dict["title"],n_dict["content"],n_dict["updated_at"],n_dict["id"],n_dict["created_at"],n_dict["favorite"],n_dict["pinned"],n_dict["tags"])

# Class NoteManager
class NoteManager:
    # Key words For Tags
    tag_keywords = {
    "Programming": [
        "python", "django", "flask", "html", "css", "javascript",
        "java", "c++", "c#", "sql", "api", "json", "oop",
        "class", "object", "function", "loop", "variable", "algorithm",
        "coding", "programming", "backend", "frontend", "git", "github"
    ],

    "School": [
        "math", "mathematics", "biology", "chemistry", "physics",
        "english", "science", "history", "geography", "exam",
        "assignment", "homework", "teacher", "lesson", "project",
        "study", "revision", "quiz", "test", "notes"
    ],

    "Personal": [
        "family", "mother", "mom", "father", "dad", "brother",
        "sister", "birthday", "diary", "journal", "home",
        "life", "relationship", "friend", "friends", "feelings",
        "emotion", "dream", "goal", "memory"
    ],

    "Work": [
        "meeting", "office", "client", "boss", "employee",
        "job", "company", "deadline", "report",
        "presentation", "email", "salary", "career"
    ],

    "Finance": [
        "money", "budget", "bank", "loan", "debt", "investment","income", "expense", "payment", "cash",
        "credit", "savings", "tax"
    ],

    "Health": [
        "doctor", "hospital", "medicine", "exercise", "gym",
        "fitness", "diet", "weight", "sleep", "water",
        "mental", "health", "anxiety", "stress", "vitamin"
    ],

    "Shopping": [
        "buy", "purchase", "shopping", "groceries", "milk",
        "bread", "clothes", "shoes", "phone",
        "laptop", "computer", "gift"
    ],

    "Travel": [
        "trip", "travel", "flight", "airport", "hotel",
        "vacation", "holiday", "passport", "visa", "ticket"
    ],

    "Entertainment": [
        "movie", "film", "music", "song", "concert", "game",
        "gaming", "anime", "netflix", "youtube", "series"
    ],

    "Sports": [
        "football", "soccer", "basketball", "tennis",
        "volleyball", "cricket", "swimming", "running",
        "gym", "training"
    ],

    "Food": [
        "food", "recipe", "cook", "breakfast", "lunch",
        "dinner", "snack", "cake", "pizza", "rice",
        "chicken", "fruit", "vegetable"
    ],

    "Ideas": [
        "idea", "startup", "business", "app", "website",
        "innovation", "design", "plan", "concept", "feature"
    ],

    "Religion": [
        "god", "jesus", "church", "bible", "prayer",
        "faith", "christian", "worship", "gospel"
    ]
}

    def __init__(self):
        self.notes = []
        
    # Get tags
    def find_tag(self,title,content):
        t = []
        for key,value in NoteManager.tag_keywords.items():
            for item in value:
                if item in title.lower() or item in content.lower():
                    t.extend([item])
        if len(t) == 0:
            return "#General"
        else:
            return "#" + " #".join(t)
   
    # Adds note to self.notes
    def add_note(self,note):
        self.notes.append(note)
    
    # Checks If title exist and update(add to)
    def is_update(self,title,content):
        for note in self.notes:
            if note.title == title:
                if note.content != content:
                    note.content = f"{note.content} \n{content}"
                    note.updated_at = format()
                    return True
        return False
    
    # Checks if there's an update(add to) else save to
    def save_note(self,title,content):
        if self.is_update(title.title(),content.capitalize()):
            pass
        else:
            note = Note(title.title(),content.capitalize(),None,notes_id(),None,None,None,self.find_tag(title,content))
            self.notes.append(note)
    
    # Remove note by ID
    def remove_note(self,id):
        if len(self.notes) > 0:
            for note in self.notes:
                if note.id == id:
                    self.notes.remove(note)
                    return True
        elif len(self.notes) < 1:
            console.print("🔴 [bold red]No Notes Available!!!")
            return False
            
     
     # Display note and ID when perform an action
    def display(self):
         if len(self.notes) > 0:
             d = {}
             for note in self.notes:
                 key = note.title
                 if key not in d:
                     d[key] = f"{note.id} : {note.category}"
             console.print("[bold blue]TITLE[/bold blue]   [bold green]|  ID   |  Tags")
             for title,id in d.items():
                 console.print("[bold yellow]---"*17)
                 console.print(f"[bold blue]{title}[/bold blue] [bold green]: {id}")
             return True
         elif len(self.notes) < 1:
             console.print("[bold blue]TITLE[/bold blue]   [bold green]|  ID   |  Tags")
             console.print("[bold yellow]---"*17)
             console.print("🔴 [bold red]No Notes Available")
             return False
         print()
         
    # Truncate note and title using Id
    def edit_note(self,id):
        found = False
        for note in self.notes:
            if note.id == id:
                found = True
                print()
                title = Prompt.ask("[underline bold green]Input Title")
                if char_count(title) > 30 or char_count(title) < 1:
                    console.print("🔴 [bold red]Invalid Title, Min Char (1) Max Char (30)")
                    break
                else:
                    content = Prompt.ask("[underline bold green]Content")
                    note.title = title
                    note.content = content
                    return True
        if not found:
            console.print("🔴 [bold red]Invalid ID")
    
    # Sort by date(newest) , favorite and pinned
    def sort(self):
        self.notes.sort(reverse=True)
    
    # mark note as favorite
    def favorite(self,id):
        found = False
        for note in self.notes:
            if note.id == id:
                found = True
                if note.favorite:
                    console.print("🔴 [bold red]Unsuccessful!!! Note already Marked Favorite")
                    break
                else:
                    note.favorite = True
                    return True
        if not found:
            console.print("🔴 [bold red]Invalid ID")
                    
     
     # pin note
    def pin(self,id):
        found = False
        for note in self.notes:
            if note.id == id:
                found = True
                if note.pinned:
                    console.print("🔴 [bold red]Unsucessful!!! Note already Pinned ")
                    break
                elif not note.pinned:
                        note.pinned = True
                        return True
        if not found:
            console.print("🔴 [bold red]Invalid ID")
                
      # Unpin Note
    def unpin(self,id):
        found = False
        for note in self.notes:
            if note.id == id:
                found = True
                if not note.pinned:
                    console.print("🔴 [bold red]Unsuccessful!!! Note already Unpinned / Note not Pinned")
                    break
                elif note.pinned:
                    note.pinned = False
                    return True
        if not found:
            console.print("🔴 [bold red]Invalid ID")
                   
        
    # filter by type/feature
    def filter(self,feature=None,id=None,title=None,tag=None):
        if len(self.notes) > 0:
            res = []
            for note in self.notes:
                if feature == "load": 
                    if note.id == id:
                        res.append(str(note))
                elif feature == "search_title":
                    if title.lower() in note.title.lower():
                        res.append(str(note))
                elif feature == "search_tag":
                    if tag.lower() in note.category.lower():
                        res.append(str(note))
                elif feature == "favorite":
                    if note.favorite:
                        res.append(str(note))
                elif feature == "pinned":
                    if note.pinned:
                        res.append(str(note))
                elif feature == "list":
                    if note.pinned:
                        res.append(str(note))
                    if not note.pinned:
                        res.append(str(note))
            return "\n".join(res)
        elif len(self.notes) < 1:
            return "🔴 [bold red]No Saved Notes Available, Try again after Saving A Note"
        
    def __str__(self):
        r = [str(note) for note in self.notes]
        return "\n".join(r)
        
        
class SaveNote:
    def __init__(self,notemanager):
        self.notemanager = notemanager
   
    def save_to_json(self):
        data = []
        with open("notes.json","w",encoding="utf-8") as s_json:
            for note in self.notemanager.notes:
                data.append(note.note_to_dict())
            json.dump(data,s_json,indent=4)
    
    def load_from_json(self):
        if os.path.exists("notes.json"):
            with open("notes.json",encoding="utf-8") as l_json:
                loaded = json.load(l_json)
                for load in loaded:
                   note = Note.dict_to_note(load)
                   self.notemanager.notes.append(note)
        else:
               self.notemanager.notes = []
               
    def __str__(self):
        r = [str(note) for note in self.notemanager.notes]
        return "\n".join(r)
            

def notes():
    nm = NoteManager()
    sn = SaveNote(nm)
    sn.load_from_json()
    
    while True:
        clear_screen()
        render_screen()
        user_input = Prompt.ask("""
        [underline bold green]Choice[/underline bold green]""")
        print()

        if user_input not in ('0','1','2','3','4','5','6','7','8','9','10','11','12','13'):
            console.print("❌ [bold red]Invalid Option!!! Try 0 - 13[bold red]")
    
        if user_input == "0":
            console.print("🚀 [bold green]Exiting!!! Goodbye")
            sn.save_to_json()
            print()
            exit()
        
        elif user_input == "1":
            title = Prompt.ask("[underline bold green]Title")
            if char_count(title) > 30 or char_count(title) < 1:
                console.print("🔴 [bold red]Invalid Title, Min Char (1) Max Char (30)")
            else:
                content = Prompt.ask("[underline bold green]Content")
                nm.save_note(title,content)
                sn.save_to_json()
                console.print("🟢 [bold green]Notes Saved Successfully")
        
        elif user_input == "2":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input Note ID")
                if nm.remove_note(id):
                    sn.save_to_json()
                    console.print("[bold green]Notes Deleted Successfully")
                else:
                    console.print("🔴 [bold red]Invalid ID")
            
        elif user_input == "3":
            console.print(f"[bold green]{nm.filter("list")}")
            
        elif user_input == "4":
            nm.sort()
            console.print("🟢 [bold green]Notes Sorted")
        
        elif user_input == "5":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input ID")
                if nm.edit_note(id):
                    sn.save_to_json()
                    console.print("🟢 [bold green]Note Title/Content Truncated")
                
        elif user_input == "6":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input ID")
                if nm.favorite(id):
                    console.print("🟢 [bold green]Note Marked Favorite")
               
        
        elif user_input == "7":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input ID")
                if nm.pin(id):
                    sn.save_to_json()
                    console.print("🟢 [bold green]Note Pinned")

        
        elif user_input == "8":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input ID")
                if nm.unpin(id):
                    sn.save_to_json()
                    console.print("🟢 [bold green]Note Unpinned")
  
        elif user_input == "9":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input Note ID")
                if nm.filter("load",id):
                    print()
                    console.print(f"[bold green]{nm.filter("load",id)}")
                else:
                   console.print("🔴 [bold red]Invalid ID")
        
        elif user_input == "10":
            count = char_count(nm.filter("favorite"))
            if count < 1:
                console.print("🔴 [bold red]No Favorite Notes Available")
            elif count > 0:
                console.print(f"[bold green]{nm.filter("favorite")}")
        
        elif user_input == "11":
            count = char_count(nm.filter("pinned"))
            if count < 1:
                console.print("🔴 [bold red]No Pinned Notes Available")
            elif count > 0:
                console.print(f"[bold green]{nm.filter("pinned")}")
        
        elif user_input == "12":
                if nm.display():
                    print()
                    title = Prompt.ask("[underline bold green]Input Title")
                    print()
                    console.print(f"[bold green]{nm.filter("search_title",None,title)}")
        
        elif user_input == "13":
            if nm.display():
                print()
                tag = Prompt.ask("[underline bold green]Input Tag")
                print()
                console.print(f"[bold green]{nm.filter("search_tag",None,None,tag)}")
                
        print()
        Prompt.ask("[underline bold green]Press Enter to continue")

if __name__ =="__main__":
    notes()

