# 🧠 Mini Python Projects

A collection of Python CLI tools and small projects built while learning programming fundamentals and problem solving.

---

## 📚 What You'll Learn

- CLI argument parsing and user interaction
- Regular expressions and pattern matching
- File I/O operations and manipulation
- String manipulation algorithms
- Encryption/decryption concepts
- Problem-solving techniques
- Working with external files and data
- Error handling and validation
- Terminal UI design with Rich library
- **Object-oriented programming (OOP)** ⭐
- Task management and data persistence
- File hashing and duplicate detection
- Text analysis and n-gram generation
- Banking systems and financial simulations
- **Unit testing with unittest framework** ⭐

---

## 🧰 Projects Included

### 📓 Note Manager (OOP + JSON)
A command-line tool for managing notes with beautiful terminal interface and persistent JSON storage.

**Features:**
- ✅ **Refactored to OOP** - Clean object-oriented design
- ✅ **JSON Persistence** - Notes stored in JSON format
- ✅ Create new notes/files
- ✅ Read file contents with formatting
- ✅ Append notes to existing files
- ✅ Truncate (overwrite) files
- ✅ Delete files safely
- ✅ List directory contents
- ✅ Change working directory
- ✅ Search patterns in files using regex
- ✅ Count pattern occurrences
- ✅ Display file size (bytes + human readable format)
- ✅ Timestamped entries for tracking changes

**Usage:**
```bash
cd notemanager
python notemanager.py
```

**Learning:** OOP design, JSON persistence, file I/O, regex patterns, CLI design

---

### 🔢 Calculator
A simple CLI-based calculator with comprehensive input validation and error handling.

**Features:**
- ✅ Basic arithmetic operations (+, -, *, /, **)
- ✅ Input validation for numbers
- ✅ Operation validation
- ✅ Division by zero protection
- ✅ Large number computation safety checks
- ✅ Clean formatted output with Rich
- ✅ Quit functionality

**Usage:**
```bash
cd calculator
python calculator.py
```

**Learning:** Input validation, error handling, exception management

---

### ⚡ Task Manager (OOP + JSON)
A powerful task management CLI tool with priority levels, due dates, and action logging.

**Features:**
- ✅ **Full OOP Implementation** - Task and TaskManager classes
- ✅ **JSON Data Persistence** - Tasks saved and loaded from JSON
- ✅ Add tasks with title, priority, and due date
- ✅ Delete, Load & Complete Tasks by using Assigned Task IDs
- ✅ Mark tasks as complete
- ✅ List all tasks
- ✅ Filter tasks (completed, uncompleted, priority)
- ✅ Load and view individual tasks
- ✅ Action logging with timestamps
- ✅ Priority filtering (High/Low)
- ✅ Due date validation (must be future date)
- ✅ Beautiful Rich terminal UI with panels
- ✅ Human-friendly Task IDs (5-digit random IDs) for easy reference
- ✅ View mapping of Task Title -> Task ID for selection

**Usage:**
```bash
cd taskmanager
python taskmanager.py
```

**Learning:** Object-oriented programming, data management, datetime handling, file logging, JSON persistence

---

### 🔐 Caesar Cipher
A text encryption/decryption tool using shift-based cipher logic for learning cryptography basics.

**Features:**
- ✅ Encode text with known shift value
- ✅ Decode text with known shift value
- ✅ Encode and decode combined operations
- ✅ Brute-force decryption (unknown shift) - tries all 26 possible shifts
- ✅ File encoding capabilities
- ✅ File decoding capabilities (known or unknown shift)
- ✅ Read encoded/decoded files
- ✅ Supports uppercase and lowercase letters
- ✅ Preserves spaces and special characters
- ✅ File operations with path display

**Usage:**
```bash
cd caesar_cipher
python caesar_cipher.py
```

**Learning:** Encryption concepts, file handling, algorithm implementation

---

### 🔍 Pattern Search (Regex)
Search and count regex patterns in text files with a built-in sample file.

**Features:**
- ✅ Search for regex patterns in provided text file
- ✅ Automatically downloads sample file (pg345.txt) on first run
- ✅ Count pattern occurrences
- ✅ Search in custom local files
- ✅ Support for common regex patterns:
  - `^` - Start of line
  - `$` - End of line
  - `\b` - Word boundaries
  - `\d` - Digits
  - `\s` - Whitespace
- ✅ Detailed match information and statistics
- ✅ Help/info section with examples

**Usage:**
```bash
cd "pattern_search,count(regex)"
python "pattern_search,count(regex).py"
```

**Note:** First run will auto-download `pg345.txt` (Gutenberg text file ~870KB)

**Learning:** Regular expressions, file I/O, pattern matching, text processing

---

### 🔤 Anagrams, Palindromes & Metathesis Pairs
Word-based algorithms for linguistic analysis and pattern recognition.

**Features:**

**Anagrams:**
- ✅ Lookup anagrams for a specific word
- ✅ Find all anagram pairs in word list
- ✅ Fast comparison algorithm

**Palindromes:**
- ✅ Check if a word is a palindrome
- ✅ Find all palindromes in word list
- ✅ Display reversed version of words

**Metathesis Pairs:**
- ✅ Lookup metathesis pairs for a word
- ✅ Find all metathesis pair combinations
- ✅ Educational section explaining each type with examples

**Usage:**
```bash
cd "anagrams,palindromes,metathesis_pair"
python "anagrams,palindromes,metathesis_pair.py"
```

**Note:** First run will auto-download `words.txt` (word list file ~1MB)

**Learning:** String algorithms, data structures, word analysis, algorithm optimization

---

### 🔎 Find Duplicates
Detect duplicate files in a directory using MD5 hashing and content verification.

**Features:**
- ✅ Find duplicate files by MD5 hash
- ✅ Verify duplicates by actual content comparison
- ✅ Filter by file extension(s)
- ✅ Recursive directory scanning
- ✅ Support for multiple file extensions (e.g., .txt, .py, .pdf)
- ✅ Search all files or specific types
- ✅ Database persistence using shelve
- ✅ Detailed duplicate file reporting
- ✅ Beautiful Rich UI with progress indicators

**Usage:**
```bash
cd find_duplicates
python find_duplicate.py
```

**Learning:** File hashing, MD5 algorithms, data persistence, recursive directory traversal, file operations

---

### 📝 Text Analysis & Generation
Analyze text files for word frequency and generate new text using n-gram models.

**Features:**
- ✅ Analyze text frequency distribution
- ✅ Remove punctuation and normalize text
- ✅ Generate new text using n-gram models (unigram to n-gram)
- ✅ Auto-download sample text files on first run
- ✅ Extract most common words from text
- ✅ Spell-check flagged words against dictionary
- ✅ Identify rare, proper nouns, or misspelled words
- ✅ Configurable n-gram size (2-50 grams)
- ✅ Random text generation based on learned patterns
- ✅ Support for Unicode normalization

**Usage:**
```bash
cd text_analysis_generation
python text_analysis_generation.py
```

**Note:** Auto-downloads sample files (Dr. Jekyll text and crossword word list)

**Learning:** Text analysis, n-gram models, language generation, Unicode handling, statistical analysis

---

### 🏦 Banking Simulator (OOP + JSON)
A comprehensive banking system simulation with account management, transactions, and financial operations.

**Features:**
- ✅ **Full OOP Implementation** - Customer, Account, SavingsAccount, CurrentAccount classes
- ✅ **JSON Data Persistence** - Account data saved and loaded from JSON
- ✅ Create and manage bank accounts
- ✅ Multiple account types (Savings, Checking/Current)
- ✅ Deposit and withdraw funds
- ✅ Transfer money between accounts
- ✅ Check account balance
- ✅ View transaction history
- ✅ Interest calculations and updates
- ✅ Fee management
- ✅ Withdrawal limits (SavingsAccount: 3 per session)
- ✅ Overdraft facility (CurrentAccount: up to 500)
- ✅ Beautiful Rich terminal UI with formatted tables
- ✅ User authentication and account security
- ✅ Financial reports and summaries

**Usage:**
```bash
cd banking_simulator
python banking_simulator.py
```

**Learning:** Object-oriented programming, financial logic, data persistence, user authentication, banking workflows

---

## 🧪 Testing

This project includes **comprehensive unit tests** covering all major functionality.

**Run all tests:**
```bash
python test.py
```

**Test Coverage:**
- ✅ Text analysis functions (split_text, clean_text, etc.)
- ✅ Anagram/palindrome detection
- ✅ Caesar cipher encoding/decoding
- ✅ Calculator operations
- ✅ File duplicate detection
- ✅ Pattern searching and regex matching
- ✅ **Banking system** (Customer, Account, SavingsAccount, CurrentAccount)
  - Account creation and management
  - Deposit, withdrawal, and transfer operations
  - Fee calculations
  - Withdrawal limits
  - Overdraft facility and eligibility

**Testing Framework:** `unittest` (Python's built-in testing framework)

---

## 📁 Project Structure

```
python-mini-projects/
├── README.md                                          # Project documentation
├── LICENSE                                            # MIT License
├── requirements.txt                                   # Python dependencies
├── .gitignore                                         # Git ignore rules
├── test.py                                            # Comprehensive unit tests ⭐
│
├── calculator/
│   └── calculator.py                                  # Calculator tool
│
├── notemanager/
│   └── notemanager.py                                 # Note management tool (OOP + JSON)
│
├── taskmanager/
│   └── taskmanager.py                                 # Task manager tool (OOP + JSON)
│
├── caesar_cipher/
│   └── caesar_cipher.py                               # Caesar cipher tool
│
├── pattern_search,count(regex)/
│   ├── pattern_search,count(regex).py                 # Pattern search tool
│   └── pg345.txt                                      # (auto-downloaded on first run)
│
├── anagrams,palindromes,metathesis_pair/
│   ├── anagrams,palindromes,metathesis_pair.py        # Word analysis tool
│   └── words.txt                                      # (auto-downloaded on first run)
│
├── find_duplicates/
│   └── find_duplicate.py                              # Duplicate file finder tool
│
├── text_analysis_generation/
│   ├── text_analysis_generation.py                    # Text analysis & generation tool
│   ├── dr_jekyll.txt                                  # (auto-downloaded on first run)
│   └── words.txt                                      # (auto-downloaded on first run)
│
└── banking_simulator/
    └── banking_simulator.py                           # Banking system simulator (OOP + JSON)
```

---

## 🛠 Built With

| Tool | Purpose |
|------|---------|
| **Python 3.14+** | Programming language |
| **`os`** | File and directory operations |
| **`re`** | Regular expressions and pattern matching |
| **`time`** | Timestamps and delays |
| **`urllib`** | Downloading external files |
| **`hashlib`** | MD5 hashing for duplicate detection |
| **`shelve`** | Data persistence and database |
| **`datetime`** | Date and time handling |
| **`json`** | Read/write JSON for data persistence |
| **`unittest`** | Unit testing framework |
| **`rich`>=13.0.0** | Beautiful terminal UI and formatting |

---

## 📋 Prerequisites

- **Python 3.14** or higher
- **pip** (Python package manager) - usually comes with Python
- **Internet connection** (for auto-downloading sample files on first run)

**Check your Python version:**
```bash
python --version
# or
python3 --version
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/samuel-2-adom/python-mini-projects.git
cd python-mini-projects
```

### 2. Install Dependencies

```bash
# On Linux/Mac
python -m pip install -r requirements.txt

# On Windows
py -m pip install -r requirements.txt
```

### 3. Run Tests (Optional)

```bash
python test.py
```

### 4. Run Your First Project

**Note Manager:**
```bash
cd notemanager
python notemanager.py
```

**Calculator:**
```bash
cd calculator
python calculator.py
```

**Task Manager:**
```bash
cd taskmanager
python taskmanager.py
```

**Caesar Cipher:**
```bash
cd caesar_cipher
python caesar_cipher.py
```

**Pattern Search:**
```bash
cd "pattern_search,count(regex)"
python "pattern_search,count(regex).py"
```

**Anagrams & Palindromes:**
```bash
cd "anagrams,palindromes,metathesis_pair"
python "anagrams,palindromes,metathesis_pair.py"
```

**Find Duplicates:**
```bash
cd find_duplicates
python find_duplicate.py
```

**Text Analysis & Generation:**
```bash
cd text_analysis_generation
python text_analysis_generation.py
```

**Banking Simulator:**
```bash
cd banking_simulator
python banking_simulator.py
```

---

## 📝 Usage Examples

Each project is a standalone CLI application with an interactive menu. Simply navigate to the project directory and run the Python file.

### Note Manager Example
```
[OPTIONS]
[01] 🔄 List Dir
[02] 📂 Change Directory
[03] 📬 Fetch Notes
[04] 🧷 Delete Notes

[NOTES OPTIONS]
[05] 💾 Create
[06] 💾 Truncate
[07] 💾 Append To
[08] 🔍 Search - Pattern & Count
[00] 🚪 Exit
```

For detailed functionality, check the inline comments in each `.py` file.

---

## 💡 Key Features & Learning Points

✅ **Rich Terminal UI** - All projects use the `rich` library for beautiful, colored output  
✅ **Error Handling** - Comprehensive input validation and exception handling  
✅ **File Operations** - Reading, writing, and manipulating files safely  
✅ **Regex Patterns** - Practical regex usage for text processing and pattern matching  
✅ **Algorithms** - Anagrams, palindromes, encryption, hashing, and optimization techniques  
✅ **Auto-Downloads** - Projects automatically fetch required data files from the internet  
✅ **CLI Design** - Professional command-line interface design patterns  
✅ **User Experience** - Loading animations, colored output, and clear prompts  
✅ **Object-Oriented Programming** - Task, TaskManager, Customer, Account classes demonstrating OOP principles  
✅ **Data Persistence** - Using JSON for task/note/account management, shelve for file hashes  
✅ **N-gram Generation** - Language model implementation for text generation  
✅ **Banking Systems** - Financial simulations with account management and transaction processing  
✅ **Unit Testing** - Comprehensive test coverage with unittest framework  
✅ **Multiple Account Types** - Savings and Current accounts with different features and limits  

---

## 🔗 Links

- [GitHub Profile](https://github.com/samuel-2-adom)
- [Repository](https://github.com/samuel-2-adom/python-mini-projects)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright © 2026 Samuel Adom**

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork this repository
- Create a feature branch
- Submit pull requests
- Report issues
- Suggest improvements

---

## ✍️ Author

**Samuel Adom** 
- 🚀 Learning Python and building cool projects
- 📚 Passionate about algorithms and problem-solving
- 💻 Building practical CLI tools
- 🧪 Committed to writing quality code with tests

---

## 🎨 Future Plans

This is an active learning project with exciting plans ahead:

- ✅ ~~Unit Tests~~ **DONE!** - Comprehensive test coverage with 60+ tests
- **GUI Version using Tkinter** - A graphical interface for all these tools with buttons and windows! 🎨
- **Web Interface** - Potentially a web-based version using Flask/Django 🌐
- **Additional Projects** - More CLI tools and utilities 🛠️
- **Performance Optimization** - Improve algorithm efficiency for large datasets ⚡
- **Extended Documentation** - Detailed docs for each project with examples 📖
- **Database Integration** - Replace shelve/JSON with SQLite for better data management 💾
- **GitHub Actions CI/CD** - Automated testing on push and pull requests 🔄

---

## 💬 Support

If you have questions or run into issues:
1. Check the inline comments in the code
2. Review the usage examples above
3. Look at the project-specific documentation
4. Run the test suite to verify functionality: `python test.py`
5. Feel free to open an issue on GitHub

---

**Last Updated:** August 24, 2026  
**Status:** Active Learning Project ✅  
**Test Coverage:** 60+ unit tests passing ✅
