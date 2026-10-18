from pathlib import Path
import os
import time
import sqlite3
from contextlib import contextmanager
import hashlib
from datetime import datetime
from collections import defaultdict
import logging
import json
import platform
from logging.handlers import RotatingFileHandler
from rich.console import Console, Group
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.rule import Rule
from rich.padding import Padding
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
console=Console()



# Clear screen after each action to keep the interface clean and user-friendly
def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)


def loading_animation(duration=1):
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Loading interface..."),
        transient=True,
    ) as progress:
        task = progress.add_task("load", total=None)
        time.sleep(duration)


# Rich UI design for the CLI interface
def render_screen():
    title = "    ⚡ MY TOOL "
    subtitle = "Find Duplicate CLI Interface"
    
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


    #***********************************************

    menu = Group(
    " [yellow][0][/yellow] 🏃 [cyan]Exit Copy[/cyan]",
    " [yellow][1][/yellow]  [cyan]Search Directory To Search For Duplicates[/cyan] 🔍",
    " [yellow][2][/yellow]  [cyan]Get Found Duplicates[/cyan] 🗂",
)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]MAIN OPTIONS",
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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Logger for logging
def setup_logger(name, log_name="duplicates.log"):
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

logger = setup_logger("duplicates")
db = "duplicate.db"


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


#Initialized databass
def init_db():
    if not os.path.exists(db):
        logger.info("DB INITIALIZED....")
        print()
    with connect() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS duplicates(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        digest TEXT NOT NULL,
        path TEXT NOT NULL,
        created_at TEXT NOT NULL,
        UNIQUE(digest,path))
        """)
 
 
# add to db table duplicates
def add_to_duplicates(digest,path):
    try:
        sql = """INSERT INTO duplicates(digest,path,created_at)
        VALUES(?,?,?)"""
        params = [digest,path,today()]
        with connect() as conn:
            row = conn.execute(sql,params)
            logger.info(f"ADDED ROW #{row.lastrowid}")
    except sqlite3.Error as e:
        logger.error(f"An exception occurred : [{e}]")


# Remove Stale Duplicates
def cleanup_stale():
    sql = """SELECT
    digest,
    json_group_array(path) AS paths,
    MIN(created_at) AS created_at
FROM duplicates
GROUP BY digest
HAVING COUNT(*) >= 2;"""
    with connect() as conn:
        row = conn.execute(sql).fetchall()
        
        for r in row:
            digest = r[0]
            paths = json.loads(r[1])
    
            try:
                params = [digest,digest]
                sql1 = """DELETE FROM duplicates WHERE digest = ? AND path = ?"""
                sql2 = """DELETE FROM duplicates WHERE digest = ? AND (SELECT COUNT(*) FROM duplicates WHERE digest = ?) < 2
                """
                for path in paths:
                    if not os.path.exists(path):
                        params = [digest,path]
                        with connect() as conn:
                            row = conn.execute(sql1,params)
                            if row.rowcount > 0:
                                logger.info(f"DELETED ROWS : {row.rowcount}")
                            print()
             
                with connect() as conn:
                    row = conn.execute(sql2,params)
                    if row.rowcount > 0:
                        logger.info(f"UPDATED ROWS : {row.rowcount}")
                        print()
                        logger.info("Stale Data Cleaned...")
                        print()
            except sqlite3.Error as e:
                logger.error(f"An exception occurred : [{e}]")
            

# Get data and remove stale state
def get_duplicate():
    cleanup_stale()
    print()
    
    sql = """SELECT
    digest,
    json_group_array(path) AS paths,
    MIN(created_at) AS created_at
FROM duplicates
GROUP BY digest
HAVING COUNT(*) >= 2;"""
    with connect() as conn:
        row = conn.execute(sql).fetchall()
        f = False
        for r in row:
            digest = r[0]
            paths = json.loads(r[1])
            
            path = [path for path in paths if os.path.exists(path)]
            
            console.print(f"""[bold green]digest[bold green] : [underline bold blue]{digest}[/underline bold blue]
[bold green]duplicates[bold green] : [[underline bold blue]{"  ,\n".join(path)}[underline bold blue]]""")
            print()
            f = True
        if not f:
            console.print("🔴 [bold red]No Duplicate Found.....[/bold red]")
            logger.debug("No Duplicates Found......")
                

# Check if path extension in suffix
def is_path(path,extensions=None):
    
    file_extensions = [
    # Documents and text
    ".doc", ".docx", ".pdf", ".txt", ".rtf",
    ".odt", ".md",

    # Spreadsheets and data
    ".xls", ".xlsx", ".csv", ".tsv", ".ods",

    # Presentations
    ".ppt", ".pptx", ".odp",

    # Images and graphics
    ".jpg", ".jpeg", ".png", ".gif", ".svg",
    ".webp", ".bmp", ".tif", ".tiff", ".heic",
    ".ico", ".raw", ".psd", ".ai",

    # Audio
    ".mp3", ".wav", ".aac", ".flac", ".m4a",
    ".ogg", ".wma", ".opus",

    # Video
    ".mp4", ".mkv", ".mov", ".avi", ".wmv",
    ".webm", ".mpeg", ".mpg", ".3gp", ".m4v",

    # Archives and compressed files
    ".zip", ".rar", ".7z", ".tar", ".gz",
    ".bz2", ".xz", ".tgz",

    # Programming and source code
    ".py", ".pyw", ".js", ".ts", ".jsx", ".tsx",
    ".java", ".class", ".c", ".h", ".cpp", ".hpp",
    ".cs", ".php", ".rb", ".go", ".rs", ".swift",
    ".kt", ".dart", ".lua", ".pl", ".r",

    # Web development
    ".html", ".htm", ".css", ".scss", ".sass",
    ".xml", ".json", ".yaml", ".yml", ".toml",
    ".sql", ".graphql",

    # Executables and installers
    ".exe", ".msi", ".bat", ".cmd", ".com",
    ".app", ".apk", ".aab", ".deb", ".rpm",
    ".dmg", ".pkg", ".sh", ".ps1",

    # Configuration and system files
    ".ini", ".cfg", ".conf", ".env", ".log",
    ".tmp", ".bak", ".dat", ".db", ".sqlite",
    ".dll", ".so", ".dylib", ".sys",

    # Fonts
    ".ttf", ".otf", ".woff", ".woff2",

    # 3D models and design
    ".obj", ".fbx", ".stl", ".blend", ".gltf",
    ".glb", ".dae", ".3ds",

    # E-books
    ".epub", ".mobi", ".azw", ".azw3",

    # Disk images and virtual machines
    ".iso", ".img", ".vhd", ".vhdx", ".vmdk",
    ".qcow2",

    # Certificates and keys
    ".pem", ".crt", ".cer", ".key", ".p12",
    ".pfx"
]
    path = Path(path)
    if not Path.is_file(path):
        return False
    if extensions is None:
        extensions = file_extensions
    else:
        if isinstance(extensions, str):
            extensions = [extensions]
    extensions = {i.lower() if i.startswith(".") else f".{i.lower()}" for i in extensions}
    return path.suffix in extensions
        
        
# Get path and digest
def get_path_digest(path):
    sha256_hash = hashlib.sha256()
    with open(path,'rb') as file:
        for chunk in iter(lambda : file.read(65536), b''):
            sha256_hash.update(chunk)
    digest = sha256_hash.hexdigest()
    return digest,path


# Group By Size
def filter_size(dir):
    same_size = defaultdict(list)
    for root,dirs,files in os.walk(dir):
        for file in files:
            path = os.path.join(root,file)
            size = os.path.getsize(path)
            same_size[size].append(path)
    return same_size


# Group By 1mb Content
def filter_content(dic):
    same_content = defaultdict(list)

    for paths in dic.values():
        if len(paths) > 1:
            for path in paths:
                with open(path, 'rb') as file:
                    data = file.read(1024 * 1024)

                sha256_hash = hashlib.sha256()
                sha256_hash.update(data)
                digest = sha256_hash.hexdigest()

                same_content[digest].append(path)

    return same_content


# Group By Extension
def filter_ext(dic):
    same_ext = defaultdict(list)
    for paths in dic.values():
        if len(paths) > 1:
            for path in paths:
                p = Path(path)
                ext = p.suffix
                same_ext[ext].append(path)
    return same_ext
                    
                    
# walk dir,filter by(size,content) hash and insert in db
def walk_path(dir,extensions=None):
    check = 0
    duplicates = defaultdict(list)
    
    check += 1
    logger.info(f"©Check {check} : Grouping By Size")
    print()
    size = filter_size(dir)
  
    check += 1
    logger.info(f"©Check {check} : Grouping By Same Content")
    print()
    content = filter_content(size)
     
    check += 1
    logger.info(f"©Check {check} : Hashing Potential Match")
    print()
    for paths in content.values():
        if len(paths) > 1:
            for path in paths:
                if is_path(path,extensions):
                    digest,path = get_path_digest(path)
                    duplicates[digest].append(path)
    
    check += 1
    logger.info(f"©Check {check} : Grouping Duplicates")
    print()
    f = False
    for digest,paths in duplicates.items():
        if len(paths) > 1:
            for path in paths:
                add_to_duplicates(digest,path)
                f = True
    if not f:
        console.print("🔴 [bold red]No Duplicate Found.....[/bold red]")
        logger.info("No Duplicates Found......")


def main():
    loading_animation()
    init_db()
    while True:
        clear_screen()
        render_screen()

        user_input = input("""
              OPT IN value : """)

        if user_input == "0":
            logger.info("Goodbye...!!!")
            print()
            break

        elif user_input == "1":
            print()
            while True:
                path = input(r"Input Directory To Search : ")
                if os.path.exists(path):
                    print("Directory exists. Proceeding with duplicate search...")
                    time.sleep(1)  # Simulate processing time  
                    print()
                    break
                else:
                    print('Directory does not exist.')
                    print()

            print()

            ext = input("Input File Extension(s) to look for (e.g. .txt or .txt,.py). Leave blank to search [ALL] : ")

            if not ext:
                ext = None

            else:
                ext = [part.strip() for part in ext.replace(',', ' ').split() if part.strip()]
                ext = [part if part.startswith('.') else f'.{part}' for part in ext]

            walk_path(path,ext)
            print()

            input("OPT IN Enter to continue....")
            continue

        elif user_input == "2":
            get_duplicate()
            print()

            input("OPT IN Enter to continue....")

if __name__ == "__main__":
    main()