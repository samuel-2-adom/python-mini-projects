import string
import random
from datetime import datetime
import os
import platform
import json
import time
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

# Assigns a random account number to a new account
def account_number():
    digits = string.digits
    return str(1000) + "".join(random.choices(digits,k=4))

# Clears the screen based on the operating system
def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

# Returns the current date and time in a formatted string
def date():
    now = datetime.now()
    return now.strftime(f"%a-%d-%b |  %I:%M:%S %p\n")

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

# Rich UI design for the CLI interface
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def render_screen():
    title = "   ⚡ MY TOOL "
    subtitle = "🏦 Bank Simulator"

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

    
    " [blue][1] [/blue]🆕 [bold blue]Create an Account[/bold blue]",
    " [yellow][2] [/yellow]🚫 [bold yellow]Close an Account(Acc Num)[/bold yellow]",
    " [green][3] [/green]📋 [bold green]List Accounts[/bold green]",
)
    

    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]ACCOUNT OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)
    #***********************************************

    menu = Group(
    " [blue][4][/blue] 💸 [bold blue]Fund Account/Deposit(Acc Num)[/bold blue]",
    " [green][5][/green] 🏧 [bold green]Withraw from Account(Acc Num)[/bold green]",
    " [blue][6][/blue] 🔁 [bold blue]Transfer to Another Account(Acc Num)[/bold blue]",

    Rule(style="bold"),  # 👈 now goes edge-to-edge
    
    " [magenta][7][/magenta] 📜 [bold magenta]Check AccountTransaction History(Acc Num)[/bold magenta]",
    " [yellow][8][/yellow] 💳 [bold yellow]Check Account Balance(Acc Num)[/bold yellow]",
)
    
    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]ACCOUNT TRANSACTION OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)

#**********************************************
    menu = Group(
    " [cyan][9] [/cyan]🔍 [bold cyan]Find Account(Acc Num)[/bold cyan]",
)
    

    console.print(
    Padding(
        Panel(
            menu,
            border_style="cyan",
            title="[bold]ACCOUNT SEARCH OPTIONS",
            title_align="left",
            expand=True,
            padding=(0, 0)  # 👈 removes inner padding completely
        ),
        (1, 4)
    )
)
    #**************************************************

    console.print(f"[bold yellow]log :[/bold yellow] [bold cyan]{date()}")
    console.print()
    console.print(Rule(f"[bold {accent_color}] MAIN CONTRO PANEL ", style=accent_color))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


### Custemer uses account
class Customer:
    def __init__(self,name=None,phone=None,address=None):
        self.name = name
        self.phone = phone
        self.address = address
    
    # Customer to dict
    def to_dict(self):
        return {"holder name" : self.name,
        "phone" : self.phone,
        "address" : self.address}
    
    # Dict to Customer
    @staticmethod
    def to_acc(d):
        c = Customer(d["holder name"],d["phone"],d["address"])
        return c
        
    def __str__(self):
        return f"""holder name : {self.name}
number : {self.phone}
address : {self.address}"""

#Account for trasactions **************
class Account:
    def __init__(self,acc_number=None,holder_info=None,balance=0,status=None,acc_type=None,history=None,interest=0,last_interest=time.time()):
        self.acc_number = acc_number
        self.holder_info = holder_info
        self.balance = round(balance,2)
        self.status = status
        self.acc_type = acc_type
        self.history = history if history is not None else []
        self.interest = round(interest)
        self.last_interest = last_interest
        
        self.withdrawal_limit = 3
        self.overdraft_limit = 500

        
    #Account to dict
    def to_dict(self):
        return {
        "acc_number" : self.acc_number,
        "holder_info" : self.holder_info,
        "balance" : self.balance,
        "status" : self.status,
        "acc_type" : self.acc_type,
        "history" : self.history,
        "interest" : self.interest,
        "last_interest" : self.last_interest
        }
    
    # Dict to Account
    @staticmethod
    def to_acc(d):
        acc_type = d.get("acc_type")
        if acc_type == "Account":
            acc = Account(d["acc_number"],d["holder_info"],d["balance"],d["status"],d["acc_type"],d.get("history",[]))
        elif acc_type == "SavingsAccount":
            acc = SavingsAccount(d["acc_number"],d["holder_info"],d["balance"],d["status"],d["acc_type"],d.get("history",[]),d.get("interest",0),d.get("last_interest",0))
        elif acc_type == "CurrentAccount":
            acc = CurrentAccount(d["acc_number"],d["holder_info"],d["balance"],d["status"],d["acc_type"],d.get("history",[]))
        return acc
        
    def __str__(self):
        return f"""
Acc_Type    :    {self.acc_type}

Acc_Number    :    {self.acc_number}

Owner    :    {self.holder_info}

Balance    :    GHC{self.balance:.2f}

Status    :    {self.status}"""
    
    # Transaction fee
    def fee(self,amount):
        return 0 if amount < 50 else round(amount / 100,2)
    
    # Deposit into account balance
    def deposit(self,amount):
         amount = amount if amount >= 0 else -amount
         if self.status == "Closed":
            console.print(f"❌ [bold red][{self.acc_type} Closed....Transaction Failed!!!]")
            
         elif self.status == "Active":
             if amount > 0:
                self.balance += amount
                dep = f"{date()}Cash In received for GHS{amount:.2f}. Current Balance: GHS{self.balance:.2f}. Fee charged: GHS{0:.2f}."
                self.history.append(dep)
                console.print(f"[bold blue]{dep}")
             else:
                console.print("❗❗❗[bold red]Transaction Failed...")
    
    # withdraw from account balance
    def withdraw(self,amount):
        amount = amount if amount >= 0 else -amount
        if self.status == "Closed":
            console.print(f"❌ [bold red][Transaction Failed....{self.acc_type} Closed]")
            
        elif self.status == "Active":
            if amount+self.fee(amount) <= self.balance:
                self.balance -= self.fee(amount)
                self.balance -= amount
                withr = f"{date()}Cash Out made for GHS{amount:.2f}. Current Balance: GHS{self.balance:.2f}. Fee charged: GHS{self.fee(amount):.2f}."
                self.history.append(withr)
                console.print(f"[bold blue]{withr}")
                return True
            else:
                console.print(f"❌ [bold red][Insufficient funds, Top up atleast GHS{round(amount-self.balance+self.fee(amount),2)} to proceed Transaction....]")
        
    # Transfer from account balance
    def transfer(self,account,amount):
         amount = amount if amount >= 0 else -amount
         if self.status == "Closed":
            console.print(f"❌ [bold red]Tranfer Account : [{self.acc_type} is Closed....Transaction Failed!!!]")

         elif account.status == "Closed":
             console.print(f"❌ [bold red]Recieving Account : [{self.acc_type} is Closed....Transaction Failed!!!]")
            
         elif self.status == "Active":
             if amount+self.fee(amount) <= self.balance:
                self.balance -= amount
                account.balance += amount
                self.balance -= self.fee(amount)
                trans = f"{date()}Transfer made for GHS{amount:.2f} To {account.holder_info}. Current Balance: GHS{self.balance:.2f}. Fee charges: GHS{self.fee(amount):.2f}."
                self.history.append(trans)
                console.print(f"[bold blue]{trans}")

                dep = f"{date()}Cash In received for GHS{amount:.2f}. From {self.holder_info}. Current Balance: GHS{account.balance:.2f}. Fee charged: GHS{0:.2f}."
                account.history.append(dep)
                return True
             else:
                console.print(f"❌ [bold red][Insufficient funds, Top up atleast GHS{round(amount-self.balance+self.fee(amount),2)} to proceed Transaction....]1")
    
    # Check account balance
    def check_balance(self):
        return self.balance
    
    # Get transaction History
    def transaction_history(self):
        r = [("®"+str(history)) for history in self.history]
        if len(r) > 0:
            print()
            console.print("📜[underline bold yellow]Transaction History")
            console.print(f"[bold blue]{"\n\n".join(r)}")
        if len(r) < 1:
            print()
            console.print("❌ [bold red][No Transaction History Available....]")
        
        
#Inherits from Account***************
class SavingsAccount(Account):
    
    # withdraw from account balance with limits.Polymorphism
    def withdraw(self,amount):
        amount = amount if amount >= 0 else -amount
        if self.status == "Closed":
            console.print(f"❌ [bold red][Transaction Failed....{self.acc_type} Closed!!!!]")

        elif self.status == "Active":
            if self.withdrawal_limit < 1:
                console.print("❌ [bold red][Withdrawal Limits reached : 3 withdrawals per session]")
            elif self.withdrawal_limit > 0:
                if amount+self.fee(amount) <= self.balance:
                    self.withdrawal_limit -= 1
                    self.balance -= self.fee(amount)
                    self.balance -= amount
                    withr = f"{date()}Cash Out made for GHS{amount:.2f}. Current Balance: GHS{self.balance:.2f}. Fee charged: GHS{self.fee(amount):.2f}."
                    self.history.append(withr)
                    console.print(f"[bold blue]{withr}")
                else:
                    console.print(f"❌ [bold red][Insufficient funds, Top up atleast GHS{round(amount-self.balance+self.fee(amount),2)} to proceed Transaction....]")

    def __str__(self):
        base = super().__str__()
        return f"{base}\n\nTotal Interest    :    GHS{self.interest:.2f}"


#Inherits from Account***************
class CurrentAccount(Account):
    
    # Get ovewrdraft amount
    def get_overdraft(self):
        if self.balance < 0:
            return abs(self.balance)
        else:
            return 0

    # Get available overdraft amount
    def get_available_overdraft(self):
        return self.overdraft_limit - self.get_overdraft()

    # Check if the requested amount is eligible for overdraft
    def eligible_for_overdraft(self, amount):
        available_overdraft = self.get_available_overdraft()
        return amount <= available_overdraft

    # Perform overdraft transaction
    def overdraft(self, amount):
        if self.eligible_for_overdraft(amount):
            self.balance -= amount
            draft = f"{date()}Overdraft made for GHS{round(amount-self.get_overdraft()-self.balance, 2)}. Current Balance: GHS{self.balance:.2f}. Fee charged: GHS0.00."
            self.history.append(draft)
            console.print(f"[bold blue]{draft}")
        else:
            console.print("❌ [bold red][Amount exceeds overdraft limit...Try Again...]")

    # Withdraw from account balance with overdraft option. Polymorphism
    def withdraw(self,amount):
        amount = amount if amount >= 0 else -amount
        if self.status == "Closed":
            console.print(f"❌ [bold red][Transaction Failed....{self.acc_type} Closed!!!]")
            
        elif self.status == "Active":
            if amount+self.fee(amount) <= self.balance:
                self.balance -= self.fee(amount)
                self.balance -= amount
                withr = f"{date()}Cash Out made for GHS{amount:.2f}. Current Balance: GHS{self.balance:.2f}. Fee charged: GHS{self.fee(amount):.2f}."
                self.history.append(withr)
                console.print(f"[bold blue]{withr}")
            else:
                console.print(f"❌ [bold red][Insufficient funds, Top up atleast GHS{round(amount-self.balance+self.fee(amount),2)} Or]",end=" ")
                request_input = Prompt.ask("[bold green]Request An Overdraft.[/bold green] [underline bold green]y/n to proceed")
                if request_input == "y":
                    print()
                    overdraft_input = Prompt.ask(f"[bold green]Eligible for an Overdraft with A limit of [/bold green][yellow]GHS{self.get_available_overdraft()}.[yellow] [underline bold green]y/n to proceed")
                    print()
                    if overdraft_input == "y":
                        if self.get_available_overdraft() <= 0:
                            console.print(f"❌ [bold red][Overdraft Limits reached, Settle Overdraft of GHS{self.balance:.2f} to increase limit and reset Overdraft]")
                        elif self.get_available_overdraft() > 0:
                               self.overdraft(amount)
                                
                    else:
                        console.print("❌ [bold red][Overdraft Transaction Failed.....]")
                else:
                    console.print("❌ [bold red][Overdraft Transaction Failed....]")
        

# Bank manages Accounts and Customer Info
class Bank:
    def __init__(self):
        self.customer_info = []
        self.accounts = []
     
     # Saves Account to JSon
    def save_to_json(self):
        with open("bank.json","w",encoding="utf-8") as js1,\
        open("customer_info.json","w",encoding="utf-8") as js2:
            data1 = [account.to_dict() for account in self.accounts]
            data2 = [info.to_dict() for info in self.customer_info]
            
            json.dump(data1,js1,indent=4)
            json.dump(data2,js2,indent=4)
    
    # Loads JSon to retrieve Account
    def load_from_json(self):
        if os.path.exists("bank.json"):
            with open("bank.json",encoding="utf-8") as js1:
                dic1 = json.load(js1)
                for dictionary in dic1:
                    #There are three Classes
                    if dictionary["acc_type"] == "Account":
                        data = Account.to_acc(dictionary)
                        self.accounts.append(data)
                    elif dictionary["acc_type"] == "SavingsAccount":
                        data = SavingsAccount.to_acc(dictionary)
                        self.accounts.append(data)
                    elif dictionary["acc_type"] == "CurrentAccount":
                        data = CurrentAccount.to_acc(dictionary)
                        self.accounts.append(data)
        else:
            self.accounts = []
        
        if os.path.exists("customer_info.json"):
            with open("customer_info.json",encoding="utf-8") as js2:
                dic2 = json.load(js2)
                for dictionary in dic2:
                    data = Customer.to_acc(dictionary)
                    self.customer_info.append(data)
        else:
            self.customer_info = []
 
        
    # Create Account
    def create_account(self):
        print()
        name = Prompt.ask("[underline bold green]Holder Name")
        name = name if len(name) > 0 else "John Doe"
        phone = Prompt.ask("[underline bold green]Phone Num")
        phone = phone if len(phone) >=6 else "0245820xxx"
        address = Prompt.ask("[underline bold green]Email")
        address = address if len(address) >=6 else "johndoe42@gmail.com"
        customer = Customer(name,phone,address)
        self.customer_info.append(customer)
        
        acc_type = Prompt.ask("""
[underline bold green]Account Types[/underline bold green]
[bold blue][ 1 ] Savings Account
[bold blue][ 2 ] Current Account[/bold blue]

    [underline bold green]OPT in Account Type""")

        if acc_type == "1":
            savings_acc = SavingsAccount(account_number(),customer.name,0,"Active","SavingsAccount")
            self.accounts.append(savings_acc)
            print()
            console.print("✅ [bold green][SavingsAccount Created....] 📈")
       
        elif acc_type == "2":
            current_acc = CurrentAccount(account_number(),customer.name,0,"Active","CurrentAccount")
            self.accounts.append(current_acc)
            print()
            console.print("✅ [bold green][CurrentAccount Created....] 💳")
        else:
            print()
            console.print("❌ [bold red][Process Cancelled]")

    # Display Accounts
    def display(self):
        if len(self.accounts) > 0:
            d = {}
            for accounts in self.accounts:
                d.setdefault(f"{accounts.acc_type}  : {accounts.acc_number}",f"{accounts.balance:.2f}    :  {accounts.status}")
            console.print("[bold green]Acc. Type     | Acc. Number  | Acc. Balance | Acc. Status")
            for key,value in d.items():
                console.print("[green]---"*20)
                console.print(f"[bold green]{key}[/bold green]   :  [bold blue]GHS{value}[/bold blue]")
            return True
        elif len(self.accounts) < 1:
            print()
            console.print("[bold green]Acc. Type  |  Acc. Number  |  Acc. Balance  | Acc. Status")
            console.print("[green]---"*17)
            console.print("[bold red]❌ [No Available Accounts]")
            return False

    
    # New Find Function That incoporates The rest
    def find_account(self,feat=None,acc_num=None):
        if feat is None:
            found = False
            print()
            if self.display():
                print()
                acc_num = Prompt.ask("[underline bold green]Input Account Number")
                print()
                for acc in self.accounts:
                    if acc.acc_number == acc_num:
                        found = True
                        console.print(f"[bold blue]{acc}[/bold blue]")
                if not found:
                    console.print("❌ [bold red][Invalid Account Number]")
        elif feat == "helper":
            found = False
            for acc in self.accounts:
                if acc.acc_number == acc_num:
                    found = True
                    return acc
            if not found:
                console.print("❌ [bold red][Invalid Account Number]")
      
          
     # Gets Interest
    def update_interest(self):
        for acc in self.accounts:
            if isinstance(acc,SavingsAccount):
                elapsed = time.time() - acc.last_interest
                periods = int(elapsed // 10)
                if periods > 0:
                    interest = acc.balance * 0.00002 * periods
                    acc.balance += round(interest,3)
                    acc.interest += interest
                    acc.last_interest += periods * 10
                    
     # Check balance
    def check_balance(self):
        print()
        if self.display():
            print()
            acc_num = Prompt.ask("[underline bold green]Input Account Number")
            acc = self.find_account("helper",acc_num)
            if acc:
                if isinstance(acc,SavingsAccount):
                    self.update_interest()
                    console.print(f"""[bold blue]Account Type    :    {acc.acc_type}
Account Balance    :    {acc.balance:.2f}
Total Interest    :    {acc.interest:.2f}[/bold blue]""")
                elif isinstance(acc,CurrentAccount):
                    console.print(f"""[bold blue]Account Type    :    {acc.acc_type}
Account Balance    :    {acc.balance:.2f}[/bold blue]""")
                    
    # Marks An Account As Closed 
    def close_account(self):
        print()
        if self.display():
            print()
            acc_num = Prompt.ask("[underline bold green]Input Account Number")
            acc = self.find_account("helper",acc_num)
            if acc:
                if isinstance(acc,SavingsAccount):
                    self.update_interest()
                if acc.balance > 0:
                    console.print("❌ [bold red][Cannot close Account. Withdraw remaining balance first.]")
                elif acc.balance < 0:
                    console.print("❌ [bold red][Cannot close Account. Settle Overdraft first.]")
                else:
                    acc.status = "Closed"
                    console.print("✅ [bold green][Your Account Has been Closed!!!!]")
    
    
    # Deposit into an account
    def deposit(self):
        print()
        if self.display():
            print()
            acc_num = Prompt.ask("[underline bold green]Deposit to Account(acc num) : ")
            acc = self.find_account("helper",acc_num)
            if acc:
                if isinstance(acc,SavingsAccount):
                    self.update_interest()
                try:
                    amount = float(Prompt.ask("[underline bold green]Deposit Amount"))
                    acc.deposit(amount)
                except ValueError:
                    console.print("❌ [bold red][Invalid Amount....]")
 
    # Transfer money between 2 accoumts
    def transfer(self):
        # Account 1
        print()
        if self.display():
            print()
            acc_num1 = Prompt.ask("[underline bold green]Transfer From Account(acc num)")
            acc1 = self.find_account("helper",acc_num1)
            if acc1:
                # Account 2
                acc_num2 = Prompt.ask("[underline bold green]To Account(acc num)")
                acc2 = self.find_account("helper",acc_num2)
                if acc2:
                    try:
                        print()
                        amount  = float(Prompt.ask("[underline bold green]Transfer Amount"))
                        acc1.transfer(acc2,amount)
                    except ValueError:
                        console.print("❌ [bold red][Invalid Amount....]")

    # Withdraw money from an account
    def withdraw(self):
        print()
        if self.display():
            print()
            acc_num = Prompt.ask("[underline bold green]Withdrawal Account(acc num)")
            acc = self.find_account("helper",acc_num)
            if acc:
                self.update_interest()
                try:
                    print()
                    amount  = float(Prompt.ask("[underline bold green]Withdrawal Amount"))
                    acc.withdraw(amount)
                except ValueError:
                    console.print("❌ [bold red][Invalid Amount....]")

    # List Accounts
    def list_acc(self):
        print()
        if self.display():
            self.update_interest()
            pass
        
    
    # Transaction History
    def transaction_history(self):
        if self.display():
            print()
            acc_num = Prompt.ask("[underline bold green]Account Number")
            acc = self.find_account("helper",acc_num)

            if acc:
                acc.transaction_history()
                return True
        return False
            
            
def simulation():
    b = Bank()
    b.load_from_json()
    b.update_interest()
    
    while True:
        clear_screen()
        render_screen()
        user_input = Prompt.ask("""        
            [underline bold green]OPT in Choice""")
        
        if user_input == "0":
            console.print("🚀 [bold green]Exiting")
            b.save_to_json()
            exit()
            
        elif user_input == "1":
            b.create_account()
            b.save_to_json()
        
        elif user_input == "2":
            b.close_account()
            b.save_to_json()
        
        elif user_input == "3":
            b.list_acc()
            
        elif user_input == "4":
            b.deposit()
            b.save_to_json()
            
        elif user_input == "5":
            b.withdraw()
            b.save_to_json()
            
        
        elif user_input == "6":
            b.transfer()
            b.save_to_json()
               
        elif user_input == "7":
            print()
            if b.transaction_history():
                pass
            else:
                console.print("[bold yellow]Accounts found : 0....")
        
        elif user_input == "8":
            b.check_balance()
            
        elif user_input == "9":
            b.find_account()
        
        print()
        Prompt.ask("[bold green]Input Enter to continue")

if __name__ == "__main__":
    simulation()
            