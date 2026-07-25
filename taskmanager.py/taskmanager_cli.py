import os
from datetime import datetime,timedelta
from time import time, strftime
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

#Timestamp
def time_stamp():
    return strftime("""%b-%d-%Y  %I:%M:%S %p""")

def actions_log(mode,action,title):
    dir = 'logs'
    path = os.path.join('logs',"log.txt")
    os.makedirs('logs',exist_ok=True)
    if os.path.exists(dir):
        with open(path,mode,encoding='utf-8') as log:
            if title is None:
                log.write(f"{action} : {time_stamp()}\n")
            else:
                log.write(f"{time_stamp()} : {action} - title({title})\n")

#Reads file
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        content = file.read().strip()
        console.print(f"[green]{content}[/green]" if content else "[underline bold red][File is empty]")

def clear_screen():
    os.system('cls')  # Windows
    # Use 'clear' for Linux/Mac

def get_valid_due_date():
    while True:
        tomorrow = (datetime.now() + timedelta(days=1)).date()

        date_str = Prompt.ask(f"[underline bold green]Enter Due Date (YYYY-MM-DD) , default ({tomorrow})[/underline bold green]")
        
        # If empty, use tomorrow's date
        if not date_str.strip():
            return str(tomorrow)
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



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
    " [red][0] [/red]🔴 [bold red]Exit[/bold red]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge

    
    " [blue][1] [/blue]➕ [bold blue]Add Task[/bold blue]",
    " [yellow][2] [/yellow]➖ [bold yellow]Delete Task[/bold yellow]",
    " [green][3] [/green]✅ [bold green]Mark Complete[/bold green]",
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
    " [blue][4][/blue] 📋 [bold blue]List Tasks[/bold blue]",
    " [green][5][/green] 🟢 [bold green]List Completed Tasks[/bold green]",
    " [blue][6][/blue] ⏳ [bold blue]List Uncompleted Tasks[/bold blue]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge
    
    " [magenta][7][/magenta] ⭐ [bold magenta]List Priority Tasks[/bold magenta]",
    " [yellow][8][/yellow] 👁️  [bold yellow]Load Task[/bold yellow]",
    " [blue][9][/blue] 🔄 [bold blue]Fetch Logs[/bold blue]",
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

    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{time_stamp()}")
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
        time.sleep(duration)

#***********************************************************************************************

# Represent Tasks
class Task:
   
   #Initiate attr and creats Task object
   def __init__(self,title,priority,due,completed=False):
       self.title = title
       self.priority = priority
       self.due = due
       self.completed = completed
       
   # Controls the behaviour or Display Output of string object Task
   def __str__(self):
       return f"""title : {self.title}
priority  : {self.priority}
due_date  : {self.due}
completed : {self.completed}'"""

# Represents organisation of tasks
class TaskManager:
    
    # initiates attr and create object Taskmanager 
    def __init__(self):
        # Save_State
        self.tasks = []
     
     # Add tasks to Taskmanager
    def add_task(self,task):
        self.tasks.append(task)
    
    # Save Tasks to Taskmanger
    def save_task(self,title,priority,due):
        task = Task(title,priority,due)
        return self.add_task(task)
    
    # Remove Task from Taskmanager
    def remove_task(self,index):
        self.tasks.pop(index) # return object from pop
    
    # Get Priority Task
    def priority_task(self):
        t = []
        for task in self.tasks:
            if task.completed == False:
                if task.priority == "High":
                    t.append(str(task))
        console.print(f"🔴 [underline bold green]Priority Tasks(High)[/underline bold green]\n[bold cyan]{'\n\n'.join(t)}[/bold cyan]......\n")
    
    #  Marks Selected Task as Completed so it gets fileterd as completed
    def complete_task(self,index):
        self.tasks[index].completed = True
        
    # Get Completed Task
    def completed_task(self):
        t = []
        for task in self.tasks:
            if task.completed == True:
                t.append(str(task))
        console.print(f"✅ [underline bold green]Completed Tasks[/underline bold green]\n[bold cyan]{'\n\n'.join(t)}[bold cyan]......\n")
     
     # Get Uncompleted Task
    def uncompleted_task(self):
        t = []
        for task in self.tasks:
            if task.completed == False:
                t.append(str(task))
        console.print(f"⏳ [underline bold green]Uncompleted Tasks[/underline bold green]\n[bold cyan]{'\n\n'.join(t)}[bold cyan]......\n") 
    
    # Get a full List of Task
    def list_task(self):
        t = []
        for task in self.tasks:
            t.append(str(task))
        console.print(f"📋 [underline bold green]Task List[/underline bold green]\n[bold cyan]{'\n\n'.join(t)}[bold cyan]......\n")
    
    # Load a Task
    def load_task(self,index):
        console.print(f"[bold cyan]{self.tasks[index]}[/bold cyan]")
   
   # Controls the behaviour or Display Output of string object TaskManager
    def __str__(self):
        t = []
        for task in self.tasks:
            t.append(str(task))
        return f"...Task List...\n{'\n\n'.join(t)}......\n"
     

def taskmaster():
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
            exit()

        elif user_input == "1":
            title = Prompt.ask("[underline bold green]Enter Task Title[/underline bold green]").title()
            priority = Prompt.ask("[underline bold green]Enter Task Priority (High/Low) default('Low')[/underline bold green]")
            if priority not in ["High","Low"]:
                priority = "Low"
            due = get_valid_due_date()
            tm.save_task(title,priority,due)
            console.print("[bold underline green]Task Saved Successfully[/bold underline green] ✅")
            actions_log("a+", "Task Saved", title)
        
        elif user_input == "2":
            try:
                index = int(Prompt.ask("[underline bold green]Input Task Index[/underline bold green]"))
                tm.remove_task(index)
                console.print("[bold underline green]Task Removed Successfully[/bold underline green]✅")
                actions_log("a+", "Task Removed", None)
            except Exception as e:
                console.print("❌ [bold red]Invalid Index. Please try again.[/bold red]")

        elif user_input == "3":
            try:
                index = int(Prompt.ask("[underline bold green]Input Task Index[/underline bold green]"))
                tm.complete_task(index)
                console.print("[bold underline green]Task Marked as Completed[/bold underline green] ✅")
                actions_log("a+", "Task Marked as Completed", None)
            except Exception as e:
                console.print("❌ [bold red]Invalid Index. Please try again.[/bold red]")
        
        elif user_input == "4":
            tm.list_task()
            actions_log("a+", "Task List Displayed", None)
        
        elif user_input == "5":
            tm.completed_task()
            actions_log("a+", "Completed Tasks Displayed", None)
        
        elif user_input == "6":
            tm.uncompleted_task()
            actions_log("a+", "Uncompleted Tasks Displayed", None)
        
        elif user_input == "7":
            tm.priority_task()
            actions_log("a+", "Priority Tasks Displayed", None)
        
        elif user_input == "8":
            try:
                index = int(Prompt.ask("[underline bold green]Input Task Index[/underline bold green]"))
                tm.load_task(index)
                actions_log("a+", "Task Loaded", None)
            except Exception as e:
                console.print("❌ [bold red]Invalid Index. Please try again.[/bold red]")
        
        elif user_input == "9":
            read_file("logs/log.txt")

        Prompt.ask("\n[underline bold green]Press Enter to Continue[/underline bold green]")

if __name__ == "__main__":
    taskmaster()
