import os
import platform
from datetime import datetime
import sqlite3
import json
from contextlib import contextmanager
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

db = "notes.db"

# Get iso format date & time
def today():
    return datetime.now().isoformat(sep=" ", timespec="seconds")

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

def char_count(text):
    c = 0
    for char in text:
        text = len(char.strip())
        c += 1
    return c
    
    

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
    " [red][0][/red]🔴 [bold red]Exit[/bold red]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [blue][1][/blue]➕ [bold blue]Save Note[/bold blue]",
    " [yellow][2][/yellow]➖ [bold yellow]Delete Note[/bold yellow]",
    " [green][3][/green]📋 [bold green]List All Notes[/bold green]",
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
    " [green][4][/green]📖 [bold green]Edit Note(ID)[/bold green]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge
    
    " [blue][5][/blue]⭐ [bold blue]Togle as Favorite(ID)[/bold blue]",
    " [magenta][6][/magenta]🟢 [bold magenta]Pin A Note(ID)[/bold magenta]",
    " [yellow][7][/yellow]🔴 [bold yellow]Unpin A Note(ID)[/bold yellow]",
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
    " [red][8][/red]🚀 [bold red]Load Note(ID)[/bold red]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [blue][9][/blue]⭐ [bold blue]Favorite Notes[/bold blue]",
    " [yellow][10][/yellow]🧷 [bold yellow]Pinned Notes[/bold yellow]",
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
    " [red][11][/red]🔍 [bold red]Search By Title[/bold red]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [blue][12][/blue]🔍 [bold blue]Search By Tag[/bold blue]",
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

    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{today()}")
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

#***********************************************************************************************

@contextmanager
def connect():
    conn = sqlite3.connect(db)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        with conn:
            yield conn
    finally:
        conn.close()

def insert_tag(tags):
    sql = """INSERT INTO tags(tag)
    VALUES(?)"""
    
    with connect() as conn:
        for t in tags:
            row = conn.execute(sql,(t,))
            print(f"ADDED ROW : #{row.lastrowid}")

def check_tags():
    sql = """SELECT id,tag from tags"""
    with connect() as conn:
        row = conn.execute(sql).fetchall()
        for r in row:
            print(f"id : {r[0]}, tag : {r[1]}")
            
           
def init_db():
    if not os.path.exists(db):
        print("DB INITIALIZED......")
        print()
    try:
        with connect() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT DEFAULT NULL,
            favorite INTEGER DEFAULT 0,
            pinned INTEGER DEFAULT 0)
            """)
            
            conn.execute("""CREATE TABLE IF NOT EXISTS note_content(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            note_id INTEGER REFERENCES notes(id) ON DELETE CASCADE)
            """)
            
            conn.execute("""CREATE TABLE IF NOT EXISTS tags(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag TEXT NOT NULL,
            UNIQUE(tag))""")
            
            conn.execute("""CREATE TABLE IF NOT EXISTS note_tag(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_id INTEGER REFERENCES tags(id),
            note_id INTEGER REFERENCES notes(id) ON DELETE CASCADE)""")
   
        tags = ["Programming","School","Personal","Work","Finance","Health","Shopping","Travel","Entertainment","Sports","Food","Ideas","Religion","Technology","Transport","General"]
        insert_tag(tags)
    except sqlite3.IntegrityError:
        pass
        
    except sqlite3.Error as e:
        print(f"An exception occured : [{e}]")
        
def add_note(title,content,tags):
        sql0 = """SELECT id,tag FROM tags"""
        sql1 = """INSERT INTO notes(title,created_at)
        VALUES(?,?)"""
        sql2 = """INSERT INTO note_content(content,note_id)
        VALUES(?,?)"""
        sql3 = """INSERT INTO note_tag(tag_id,note_id)
        VALUES(?,?)"""
        
        # INSERT title and created at
        with connect() as conn:
            row  = conn.execute(sql1,(title,today()))
            last_row = row.lastrowid
            
            # INSERT content and note_id
            conn.execute(sql2,(content,row.lastrowid))
            
            id_tag = {}
            row1 = conn.execute(sql0).fetchall()
            for r in row1:
                id_tag[r[0]] = r[1]
                
            # INSERT tag id and note id
            for id,tag_s in id_tag.items():
                for tag in tags:
                    if tag_s == tag:
                        conn.execute(sql3,(id,last_row))
            print(f"ADDED ROW : #{last_row}")
            

def update_note(title,content):
    sql = """SELECT notes.id,notes.title,note_content.content
    FROM notes
    INNER JOIN note_content
    ON notes.id = note_content.note_id"""
    
    sql1 = """UPDATE  note_content
    SET content = ?
    WHERE note_id = ?
    """
    sql2 = """UPDATE notes
    SET updated_at = ?
    WHERE id = ?
    """
    id_title = {}
    id_content = {}
    with connect() as conn:
        row = conn.execute(sql).fetchall()
        
        for r in row:
            id_title[r[0]] = r[1]
            id_content[r[0]] = r[2]
        
    for id_s,title_s in id_title.items():
        for id,content_s in id_content.items():
            if id_s == id:
                if title_s == title:
                    if content_s != content:
                        c = f"{content_s} \n {content}"
                        with connect() as conn:
                            row1 = conn.execute(sql1,(c,id))
                            conn.execute(sql2,(today(),id))
                            print(f"UPDATED ROWS : {row1.rowcount}")
                            return True
                             
# Class Note
class Note: 
    def __init__(self,title,content,updated_at=None,created_at=None,favorite=None,pinned=None,category=None):
        
        self.title = title
        self.content = content
        self.created_at = None if created_at is None else created_at
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
created_at : {self.created_at}
updated_at : {self.updated_at}
tags : {self.category}
"""


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
        "study", "revision", "quiz", "test", "notes","school"
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
        "presentation", "email", "salary", "career","work"
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
        "gym", "training","sports"
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
        "faith", "christian", "worship", "gospel","religion"
    ],
    
    "Technology": [
    "phones","android","ios","laptop","macbook","artificial inteligence","tablet","tech","smart phones","tv","television"
    ],
    
    "Transport": [
    "bus","car","train","airplane","helicopter","halo","jet","bicycle","motorcycle","scooter"
    ]
}
        
    # Get tags
    def find_tag(self,title,content):
        t = []
        for key,value in NoteManager.tag_keywords.items():
            for item in value:
                if item in title.lower() or item in content.lower():
                    t.extend([key])
        if len(t) == 0:
            t = ["General"]
        return set(t)
   
    
    # Checks if there's an update(add to) else save to
    def save_note(self,title,content):
        if update_note(title,content):
            pass
        else:
            note = Note(title,content)
            add_note(note.title,note.content,self.find_tag(note.title,note.content))
    
    # Remove note by ID
    def remove_note(self,id):
        sql1 = """DELETE FROM notes WHERE id = ?"""
        with connect() as conn:
            row = conn.execute(sql1,(id,))
            print(f"UPDATED ROWS : {row.rowcount}")
            if row.rowcount > 0:
                console.print("[bold green]Notes Deleted Successfully")
            else:
                console.print("🔴 [bold red]INVALID ID / No Notes Available!!!")
                
                
     # Display note and ID when perform an action
    def display(self):
         sql = """SELECT notes.id,notes.title,json_group_array(tags.tag)
         FROM notes
         LEFT JOIN note_tag
         ON notes.id = note_tag.note_id
         LEFT JOIN tags
         ON tags.id = note_tag.tag_id
         GROUP BY notes.id
         """
         with connect() as conn:
             row = conn.execute(sql).fetchall()
             if row:
                 for r in row:
                     console.print(f"[bold blue]#ID[/bold blue] : [bold green]{r[0]}[/bold green]  [bold blue]#TITLE[/bold blue] : [bold green]{r[1]}[/bold green]  [bold blue]#TAGS[/bold blue] : [bold green]{json.loads(r[2])}[/bold green]")
                     console.print("[bold yellow]---"*15)
                 return True
             else:
                 console.print("🔴 [bold red]No Notes Available")
                 return False
         
    # Truncate note and title using Id
    def edit_note(self,id):
        sql = """UPDATE notes
        SET title = ? WHERE id = ?"""
        sql1 = """UPDATE note_content
        SET content = ? WHERE note_id = ?
        """
        title = Prompt.ask("[underline bold green]Input Title")
        if char_count(title) > 30 or char_count(title) < 1:
            console.print("🔴 [bold red]Invalid Title, Min Char (1) Max Char (30)")
        else:
            content = Prompt.ask("[underline bold green]Content")
            with connect() as conn:
                row = conn.execute(sql,(title,id))
                conn.execute(sql1,(content,id))
                print(f"UPDATED ROWS : {row.rowcount}")
                
                if row.rowcount > 0:
                    console.print("🟢 [bold green]Note Title/Content Truncated")
                
                else:
                    console.print("🔴 [bold red]Invalid ID")
                    
       
    # mark note as favorite
    def favorite(self,id):
        sql = """UPDATE notes
        SET favorite = 1 WHERE id = ? AND favorite = 0"""
        with connect() as conn:
            row = conn.execute(sql,(id,))
            print(f"ROWS UPDATED : {row.rowcount}")
            if row.rowcount > 0:
                console.print("🟢 [bold green]Note Marked Favorite")
                  
            else:
                console.print("🔴 [bold red]Invalid ID / Unsuccessful!!! Note Already Marked Favorite")
                
            
     # pin note
    def pin(self,id):
        sql = """UPDATE notes
        SET pinned = 1 WHERE id = ? AND pinned = 0"""
        with connect() as conn:
            row = conn.execute(sql,(id,))
            print(f"ROWS UPDATED : {row.rowcount}")
            if row.rowcount > 0:
                console.print("🟢 [bold green]Note Pinned")
                
            
            else:
                console.print("🔴 [bold red]Invalid ID / Unsuccessful!!! Note already Pinned")
                          
      # Unpin Note
    def unpin(self,id):
        sql = """UPDATE notes
        SET pinned = 0 WHERE id = ? AND pinned = 1"""
        with connect() as conn:
            row = conn.execute(sql,(id,))
            print(f"ROWS UPDATED : {row.rowcount}")
            if row.rowcount > 0:
                console.print("🟢 [bold green]Note UnPinned")
            
            else:
                console.print("🔴 [bold red]Invalid ID / Unsuccessful!!! Note already UnPinned")
                
    
    
    def build(self,row):
        for r in row:
            console.print(f"""[bold green] Title : {r[0]}
 Content : {r[1]}
 ID : {r[2]}
 Created_at : {r[3]}
 Updated_at : {r[4]}
 Tags : {json.loads(r[5])}
""")
                   
        
    # filter by type/feature
    def filter(self,id=None,title=None,tag=None,favorite=False,pinned=False,list=False):
        sql = """SELECT notes.title,note_content.content,notes.id,notes.created_at,notes.updated_at,json_group_array(tags.tag),tags.tag
        FROM notes
        LEFT JOIN note_content
        ON notes.id = note_content.note_id
        LEFT JOIN note_tag
        ON notes.id = note_tag.note_id
        LEFT JOIN tags
        ON tags.id = note_tag.tag_id
        GROUP BY notes.title
        """
        params = []
        
        if id:
            sql += """ HAVING notes.id = ?"""
            params = [id,]
        
        elif title:
            sql += """ HAVING notes.title LIKE ?"""
            params = [f"{title}%",]
        
        elif tag:
            sql += """ HAVING tags.tag LIKE ?"""
            params = [f"{tag}%",]
        
        elif favorite:
            sql += """ HAVING notes.favorite = ?"""
            params = ["1",]
            
        elif pinned:
            sql += """ HAVING notes.pinned = ?"""
            params = ["1",]
        
        elif list:
            params = None
        
        sql += """ ORDER BY created_at DESC"""
        
        with connect() as conn:
            row = []
            if params is None:
                row = conn.execute(sql).fetchall()
            else:
                row = conn.execute(sql,params).fetchall()
            
            
            if not row:
                console.print("🔴 [bold red]No Saved Notes With Params Available.....")
            
            else:
                self.build(row)
        

def notes():
    loading_animation()
    nm = NoteManager()
    
    while True:
        clear_screen()
        render_screen()
        user_input = Prompt.ask("""
        [underline bold green]Choice[/underline bold green]""")
        print()

        if user_input not in ('0','1','2','3','4','5','6','7','8','9','10','11','12'):
            console.print("❌ [bold red]Invalid Option!!! Try 0 - 12[bold red]")
    
        if user_input == "0":
            console.print("🚀 [bold green]Exiting!!! Goodbye")
            print()
            break
        
        elif user_input == "1":
            title = Prompt.ask("[underline bold green]Title")
            if char_count(title) > 30 or char_count(title) < 1:
                console.print("🔴 [bold red]Invalid Title, Min Char (1) Max Char (30)")
            else:
                content = Prompt.ask("[underline bold green]Content")
                nm.save_note(title,content)
                console.print("🟢 [bold green]Notes Saved Successfully")
        
        elif user_input == "2":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input Note ID")
                nm.remove_note(id)
                      
        elif user_input == "3":
            filter = nm.filter(None,None,None,False,False,True)
                
        elif user_input == "4":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input ID")
                nm.edit_note(id)
                                
        elif user_input == "5":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input ID")
                nm.favorite(id)
                    
        elif user_input == "6":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input ID")
                nm.pin(id)
                     
        elif user_input == "7":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input ID")
                nm.unpin(id)
  
        elif user_input == "8":
            if nm.display():
                print()
                id = Prompt.ask("[underline bold green]Input Note ID")
                nm.filter(id)
        
        elif user_input == "9":
            nm.filter(None,None,None,True)  
        
        elif user_input == "10":
            filter = nm.filter(None,None,None,False,True)
        
        elif user_input == "11":
                if nm.display():
                    print()
                    title = Prompt.ask("[underline bold green]Input Title")
                    print()
                    nm.filter(None,title)
        
        elif user_input == "12":
            if nm.display():
                print()
                tag = Prompt.ask("[underline bold green]Input first Tag")
                print()
                nm.filter(None,None,tag)
                
        print()
        Prompt.ask("[underline bold green]Press Enter to continue")

if __name__ == "__main__":
    init_db()
    notes()