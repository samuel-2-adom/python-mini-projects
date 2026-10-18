import sqlite3
from contextlib import contextmanager
import logging
from logging.handlers import RotatingFileHandler
import os
import platform
from datetime import datetime,timedelta
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

# Logger for logging
def setup_logger(name, log_name="taskmanager.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_f = logging.Formatter("%(name)s | %(levelname)s | %(message)s")
    file_f = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_f)

    file_handler = RotatingFileHandler(log_name, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_f)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger("taskmanager")

db = "tasks.db"


#boilerplate for db connection
@contextmanager
def connect():
    conn = sqlite3.connect(db)
    try :
        with conn:
            yield conn
    finally:
        conn.close()


# Get iso format date & time
def today():
    return datetime.now().isoformat(sep=" ", timespec="seconds")


#Reads file
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        content = file.read().strip()
        console.print(f"[green]{content}[/green]" if content else "[underline bold red][File is empty]")


# Clear screen after each action to keep the interface clean and user-friendly
def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


# Get valid due date from user input, ensuring it's in the future and in the correct format
def get_valid_due_date():
    while True:
        week_1 = (datetime.now() + timedelta(days=6)).date()

        date_str = Prompt.ask(f"[underline bold green]Enter Due Date (YYYY-MM-DD) , default ({week_1})[/underline bold green]")
        
        # If empty, use tomorrow's date
        if not date_str.strip():
            return str(week_1)
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            if date_obj.date() < datetime.now().date():
                print()
                console.print("❌ [bold red]Due date must be in the future![/bold red]")
                continue
            return date_str
        except ValueError:
            print()
            console.print("❌ [bold red]Invalid format! Use YYYY-MM-DD[/bold red]")


def render_screen():
    title = "     ⚡ MY TOOL "
    subtitle = "mini TaskManager CLI Interface"

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

    
    " [blue][1][/blue]➕ [bold blue]Add Task[/bold blue]",
    " [yellow][2][/yellow]➖ [bold yellow]Delete Task[/bold yellow]",
    " [green][3][/green]✅ [bold green]Mark Complete[/bold green]",
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
    " [blue][4][/blue]📋 [bold blue]List Tasks[/bold blue]",
    " [green][5][/green]🟢 [bold green]List Completed Tasks[/bold green]",
    " [blue][6][/blue]⏳ [bold blue]List Uncompleted Tasks[/bold blue]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge
    
    " [magenta][7][/magenta]⭐ [bold magenta]List Priority Tasks[/bold magenta]",
    " [yellow][8][/yellow]👁️  [bold yellow]Load Task[/bold yellow]",
    " [blue][9][/blue]🔄 [bold blue]Fetch Logs[/bold blue]",
)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]LIST OPTIONS",
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

  
  #Initialized databass
def init_db():
    if not os.path.exists(db):
        logger.info("DB INITIALIZED....")
        print()
    with connect() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        priority TEXT NOT NULL DEFAULT "Low",
        due TEXT NOT NULL,
        complete INTEGER DEFAULT 0)
        """)

def add_task(title,priority,due):
    sql = """INSERT INTO tasks(title,priority,due)
    VALUES(?,?,?)
    """
    with connect() as conn:
        row = conn.execute(sql,(title,priority,due))
        last_id = row.lastrowid
        print(f"ADDED ROW : #{last_id}")

# Represent Tasks
class Task:
   
   #Initiate attr and creats Task object
   def __init__(self,title,priority,due,completed=None):
       self.title = title
       self.priority = priority
       self.due = due
       self.completed = completed
       
   # Controls the behaviour or Display Output of string object Task
   def __str__(self):
       return f"""title : {self.title}
priority : {self.priority}
due  : {self.due}
completed : {self.completed}'"""


# Represents organisation of tasks
class TaskManager:
    
    # Save Tasks to Taskmanger
    def save_task(self,title,priority,due):
        task = Task(title,priority,due)
        add_task(task.title,task.priority,task.due)
        logger.debug(f"Saved Task : {title}")
                 
    # Remove Task from Taskmanager using its ID
    def remove_task(self,id):
        sql = """DELETE FROM tasks
        WHERE id = ?
        """
        with connect() as conn:
            row = conn.execute(sql,(id,))
            print(f"UPDATED ROWS : {row.rowcount}")
            
            if row.rowcount > 0:
                console.print("[bold underline green]Task Removed Successfully[/bold underline green]✅")
                logger.debug(f"Removed Task #{id}")
            else:
                console.print("❌ [bold red]INVALID Task ID[/bold red]")
        

 
    #  Marks Selected Task as Completed using its ID so it gets fileterd as completed
    def complete_task(self,id):
        sql = """UPDATE tasks
        SET complete = 1 WHERE id = ? AND complete = 0
        """
        with connect() as conn:
            row = conn.execute(sql,(id,))
            print(f"UPDATED ROWS : {row.rowcount}")
            
            if row.rowcount > 0:
                console.print("[bold underline green]Task Completed Successfully[/bold underline green]✅")
                logger.debug(f"Complete Task #{id}")
            else:
                console.print("❌ [bold red]INVALID Task ID / Task Already Completed[/bold red]")
     
    def build(self,row):
        for r in row:
            console.print(f"""[bold green]Title : {r[0]}
Priority : {r[1]}
Due : {r[2]}
Complete : {r[3]}
""")

    def filter(self,id=None,priority=None,complete=False,uncomplete=False,list=False):
        sql = """SELECT title,priority,due,
        CASE
        WHEN complete = 0 THEN 'False'
        ELSE 'True'
        END AS complete 
        FROM tasks"""
        params = []
        if id:
            sql += """ WHERE id = ?"""
            params = [id,]
        elif priority:
            sql += """ WHERE priority LIKE ?"""
            params = [f"{priority}%"]
        elif complete:
            sql += """ WHERE complete = True"""
            params = None
        elif uncomplete:
            sql += """ WHERE complete = False"""
            params = None
        elif list:
            params = None
        
        with connect() as conn:
            row = []
            if params is None:
                row = conn.execute(sql).fetchall()
            else:
                row = conn.execute(sql,params).fetchall()
            
            
            if not row:
                console.print("🔴 [bold red]No Tasks With Params Available.....")
            
            else:
                self.build(row)
                logger.debug("Filter And Biuld Display")
                

    def display(self):
         sql = """SELECT id,title
         FROM tasks"""
         with connect() as conn:
             row = conn.execute(sql).fetchall()
             if row:
                 for r in row:
                     console.print(f"[bold blue]#ID[/bold blue] : [bold green]{r[0]}[/bold green]  [bold blue]#TITLE[/bold blue] : [bold green]{r[1]}[/bold green]")
                     console.print("[bold yellow]---"*15)
                 return True
             else:
                 console.print("🔴 [bold red]No Notes Available")
                 return False

            
def taskmaster():
    loading_animation()
    tm = TaskManager()

    while True:

        clear_screen()
        render_screen()
        user_input = Prompt.ask("""[underline bold green]Choose an option[/underline bold green]""")
        print()
        
        if user_input not in ["0","1","2","3","4","5","6","7","8","9"]:
            console.print("❌ [bold red]Invalid Input. Please try again.[/bold red]")
            
            
        if user_input == "0":
            clear_screen()
            console.print("➡️  [bold yellow]Exiting Task Manager!!![/bold yellow]")
            break

        elif user_input == "1":
            title = Prompt.ask("[underline bold green]Enter Task Title[/underline bold green]").title()
            priority = Prompt.ask("[underline bold green]Enter Task Priority (High/Low) default('Low')[/underline bold green]")
            if priority not in ["High","Low"]:
                priority = "Low"
            due = get_valid_due_date()
            tm.save_task(title,priority,due)
            console.print("[bold underline green]Task Saved Successfully[/bold underline green] ✅")
        
        elif user_input == "2":
            if tm.display():
                print()
                task_id = Prompt.ask("[underline bold green]Input Task ID[/underline bold green]")
                tm.remove_task(task_id)
                

        elif user_input == "3":
            if tm.display():
                task_id = Prompt.ask("[underline bold green]Input Task ID[/underline bold green]")
                tm.complete_task(task_id)

        
        elif user_input == "4":
            tm.filter(None,None,False,False,True)
        
        elif user_input == "5":
            tm.filter(None,None,True)
        
        elif user_input == "6":
            tm.filter(None,None,False,True)
        
        elif user_input == "7":
            tm.filter(None,"High")
        
        elif user_input == "8":
            if tm.display():
                print()
                task_id = Prompt.ask("[underline bold green]Input Task ID[/underline bold green]")
                print()
                tm.filter(task_id)
               
        elif user_input == "9":
            read_file("taskmanager.log")

        Prompt.ask("\n[underline bold green]Press Enter to Continue[/underline bold green]")

if __name__ == "__main__":
    init_db()
    taskmaster()