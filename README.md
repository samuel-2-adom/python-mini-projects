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

---

## 🧰 Projects Included

### 📓 Notes CLI
A command-line tool for managing notes and files with a beautiful terminal interface.

**Features:**
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
cd notes.py
python mini_notes_cli.py
```

**Learning:** File I/O, regex patterns, CLI design

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
cd calculator.py
python mini_calculator_cli.py
```

**Learning:** Input validation, error handling, exception management

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
cd "think python projects/Caesar Cipher"
python mini_caesar_cipher_cli.py
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
cd "think python projects/pattern_search(regex)"
python "mini_checker(regex_pattern_search & counter)_cli.py"
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
cd "think python projects/Anagrams,Palindromes,Metathesis_Pair"
python "mini_checker(anagrams,palindromes,metathesis_pair)_cli.py"
```

**Note:** First run will auto-download `words.txt` (word list file ~1MB)

**Learning:** String algorithms, data structures, word analysis, algorithm optimization

---

## 📁 Project Structure

```
python-mini-projects/
├── README.md                           # Project documentation
├── LICENSE                             # MIT License
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore rules
│
├── notes.py/
│   └── mini_notes_cli.py              # Notes management tool
│
├── calculator.py/
│   └── mini_calculator_cli.py         # Calculator tool
│
└── think python projects/
    ├── Caesar Cipher/
    │   └── mini_caesar_cipher_cli.py   # Caesar cipher tool
    │
    ├── pattern_search(regex)/
    │   ├── mini_checker(regex_pattern_search & counter)_cli.py
    │   └── pg345.txt                   # (auto-downloaded on first run)
    │
    └── Anagrams,Palindromes,Metathesis_Pair/
        ├── mini_checker(anagrams,palindromes,metathesis_pair)_cli.py
        └── words.txt                   # (auto-downloaded on first run)
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

### 3. Run Your First Project

**Notes CLI:**
```bash
cd notes.py
python mini_notes_cli.py
```

**Calculator:**
```bash
cd calculator.py
python mini_calculator_cli.py
```

**Caesar Cipher:**
```bash
cd "think python projects/Caesar Cipher"
python mini_caesar_cipher_cli.py
```

**Pattern Search:**
```bash
cd "think python projects/pattern_search(regex)"
python "mini_checker(regex_pattern_search & counter)_cli.py"
```

**Anagrams & Palindromes:**
```bash
cd "think python projects/Anagrams,Palindromes,Metathesis_Pair"
python "mini_checker(anagrams,palindromes,metathesis_pair)_cli.py"
```

---

## 📝 Usage Examples

Each project is a standalone CLI application with an interactive menu. Simply navigate to the project directory and run the Python file.

### Notes CLI Example
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
✅ **Algorithms** - Anagrams, palindromes, encryption, and optimization techniques  
✅ **Auto-Downloads** - Projects automatically fetch required data files from the internet  
✅ **CLI Design** - Professional command-line interface design patterns  
✅ **User Experience** - Loading animations, colored output, and clear prompts  

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

---

## 🎨 Future Plans

This is a learning project with exciting plans ahead:

- **GUI Version using Tkinter** - A graphical interface for all these tools with buttons and windows! 🎨
- **Web Interface** - Potentially a web-based version using Flask/Django 🌐
- **Additional Projects** - More CLI tools and utilities 🛠️
- **Performance Optimization** - Improve algorithm efficiency for large datasets ⚡
- **Unit Tests** - Comprehensive test coverage 🧪
- **Documentation** - Detailed docs for each project 📖

---

## 💬 Support

If you have questions or run into issues:
1. Check the inline comments in the code
2. Review the usage examples above
3. Look at the project-specific documentation
4. Feel free to open an issue on GitHub

---

**Last Updated:** April 29, 2026
**Status:** Active Learning Project ✅
