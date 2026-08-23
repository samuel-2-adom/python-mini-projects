from text_analysis_generation.text_analysis_generation import split_text,sub,clean_text,is_special_line
from anagrams_palindromes_metathesis_pair.anagrams_palindromes_metathesis_pair import is_anagram,is_palindromes,reverse,is_meta_pair
from caesar_cipher.caesar_cipher import encode,decode
from calculator.calculator import add,mul,pow,div,subs 
from find_duplicates.find_duplicate import is_path,same_content
from pattern_search_count_regex.pattern_search_count_regex import find_first,count_first
from banking_simulator.banking_simulator import account_number,date,Customer,Account,SavingsAccount,CurrentAccount,Bank


import unittest
import os
from unittest import TestCase

class TestExample(TestCase):

    # Text_Analysis_Generation
    def test_is_specialline(self):
        result = is_special_line("*** He took that beating like a chanp")
        self.assertTrue(result)

    def test_splittext(self):
        result = split_text("Split Me")
        self.assertEqual(result,["Split","Me"])
    
    def test_splittext_em_dash(self):
        result = split_text("deux—ex—machina")
        self.assertEqual(result,["deux","ex","machina"])
    
    def test_sub(self):
        result = sub({"a":1,"b":2,"c":3},{"a":1,"c":3,"d":4})
        self.assertEqual(result,{"b":2})
    
    def test_cleantext(self):
        p = "!?"
        result = clean_text("!!!Hypothetically Just What A Bigger Idiot He Is???",p)
        self.assertEqual(result,"hypothetically just what a bigger idiot he is")

    # Anagarams Palindromes Meta_Pairs
    def test_is_anagram(self):
        result = is_anagram("mate","tame")
        self.assertTrue(result)
    
    def test_is_palindromes(self):
        result = is_palindromes("mom")
        self.assertTrue(result)
    
    def test_reverse(self):
        result = reverse("trap")
        self.assertEqual(result,"part")
    
    def test_is_meta_pair(self):
        result = is_meta_pair("carve","crave")
        self.assertTrue(result)

    # Caesar  Cypher
    def test_encode(self):
        result = encode("give to caesar what is caesar's",5)
        self.assertEqual(result,"lnaj yt hfjxfw bmfy nx hfjxfw'x")

    def test_decode(self):
        result = decode("lnaj yt hfjxfw bmfy nx hfjxfw'x",5)
        self.assertEqual(result,"give to caesar what is caesar's")

    # Caluculator
    def test_add(self):
        result = add(2,5)
        self.assertEqual(result,7)
    
    def test_sub(self):
        result = subs(5,2)
        self.assertEqual(result,3)
    
    def test_pow(self):
        result = pow(2,5)
        self.assertEqual(result,32)
    
    def test_mul(self):
        result = mul(2,5)
        self.assertEqual(result,10)
    
    def test_div(self):
        result = div(10,5)
        self.assertEqual(result,2)

    # Find_Duplicates
    def test_ispath(self):
        f = "logs4q1.txt"
        with open(f,"w",encoding="utf-8"):
            pass
        result = is_path(f,".txt")
        self.assertTrue(result)
        os.remove(f)
    
    def test_samecontent(self):
        f = "logs4q1.txt"
        f1 = "logs4q2.txt"
        with open(f,"w",encoding="utf-8") as file1,\
             open(f1,"w",encoding="utf-8") as file2:
            file1.write("suck it")
            file2.write("suck it")
        path = [f,f1]
        result = same_content(*path)
        self.assertTrue(result)
        os.remove(f)
        os.remove(f1)
    
    def test_not_samecontent(self):
        f = "logs4q1.txt"
        f1 = "logs4q2.txt"
        with open(f,"w",encoding="utf-8") as file1,\
             open(f1,"w",encoding="utf-8") as file2:
            file1.write("suck it")
            file2.write("shut it")
        path = [f,f1]
        result = same_content(*path)
        self.assertFalse(result)
        os.remove(f)
        os.remove(f1)

    # Pattern_Search_Count_Regex
    def test_findfirst(self):
        f = "logs4q1.txt"
        with open(f,"w",encoding="utf-8") as file:
            file.write("the greates showman")
        result = find_first("showman",f)
        self.assertEqual(str(result),"<re.Match object; span=(12, 19), match='showman'>")
        os.remove(f)
    
    def test_countfirst(self):
        f = "logs4q1.txt"
        with open(f,"w",encoding="utf-8") as file:
            file.write("the greatest showman is a goat")
        result = count_first("goat",f)
        self.assertEqual(result, 1)
        os.remove(f)
    
    # Banking Simulation
    #class Customer
    def test_acc_num(self):
        result = account_number()
        self.assertTrue(result.startswith("1000") and len(result) == 8)
    
    def test_classcustomer_name(self):
        customer = Customer("Gracious","0333****","gracious4165@***")
        self.assertEqual(customer.name,"Gracious")
    
    def test_classcustomer_phone(self):
        customer = Customer("Gracious","0333****","gracious4165@***")
        self.assertEqual(customer.phone,"0333****")
    
    def test_classcustomer_email(self):
        customer = Customer("Gracious","0333****","gracious4165@***")
        self.assertEqual(customer.address,"gracious4165@***")
    
    # class Account
    def test_account(self):
        acc_num = account_number()
        customer = Customer("Gracious","0333****","gracious4165@***")
        ac_type = ["Account","CurrentAccount","SavingsAccount"]
        account = Account(acc_num,customer,0,"Active",ac_type[0],None,0,None)
        result = account.acc_number[:4] == str(1000) and len(account.acc_number) == 8 and account.balance == 0 and account.acc_type == "Account" and account.interest == 0
        self.assertTrue(result)
    
    def test_fee(self):
        account = Account(None,None,0,"Active","Account")
        result = account.fee(101)
        self.assertEqual(result,1.01)
    
    def test_handlenegative_amount(self):
        account1 = Account(None,None,0,"Active","Account")
        account2 = Account(None,None,0,"Active","Account")
        account1.deposit(-100)
        account1.withdraw(-50)
        account1.transfer(account2,-25)
        print()
        result = account1.balance == 24.5 and account2.balance == 25
        self.assertTrue(result)
        
    def test_deposit(self):
        account = Account(None,None,0,"Active","Account")
        account.deposit(159.9)
        print()
        self.assertEqual(account.balance,159.9)
    
    def test_withdrawal_and_charges(self):
        account = Account(None,None,0,"Active","Account")
        account.deposit(159.9)
        account.withdraw(100)
        print()
        self.assertEqual(round(account.balance,1),58.9)
    
    def test_transfer_receiving_end(self):
        account1 = Account(None,None,0,"Active","Account")
        account2 = Account(None,None,0,"Active","Account")
        account1.deposit(100)
        account2.deposit(20)
        account1.transfer(account2,40)
        print()
        self.assertEqual(account2.balance,60)
    
    def test_transfer_and_sending_endcharges(self):
        account1 = Account(None,None,0,"Active","Account")
        account2 = Account(None,None,0,"Active","Account")
        account1.deposit(100)
        account2.deposit(20)
        account1.transfer(account2,60)
        print()
        self.assertEqual(account1.balance,39.4)
    
    def test_checkbalance(self):
        account = Account(None,None,0,"Active","Account")
        account.deposit(159.9)
        self.assertEqual(account.balance,159.9)
    
    def test_history(self):
        account = Account(None,None,0,"Active","Account")
        account.deposit(100)
        result = account.history
        self.assertTrue(len(result) == 1 and type(result) == list)
    
    #class SavingsAccount(Account)
    def test_withrawal_limit_3(self):
        account = SavingsAccount(None,None,0,"Active","SavingsAccount")
        account.deposit(100)
        account.withdraw(20)
        account.withdraw(20)
        account.withdraw(20)
        account.withdraw(20)
        account.withdraw(20)
        print()
        self.assertEqual(account.balance,40)

    # class CurrentAccount(Account)
    def test_availableoverdraft_limit_500(self):
        account = CurrentAccount(None,None,0,"Active","CurrentAccount")
        avail = account.get_available_overdraft()
        self.assertTrue(avail <= account.overdraft_limit)
        
    def test_eligiblefor_overdraft(self):
        account = CurrentAccount(None,None,0,"Active","CurrentAccount")
        elig = account.eligible_for_overdraft(500)
        self.assertTrue(elig)
    
    def test_noteligiblefor_overdraft(self):
        account = CurrentAccount(None,None,0,"Active","SavingsAccount")
        elig = account.eligible_for_overdraft(501)
        self.assertFalse(elig)
        
    def test_overdraft(self):
        account = CurrentAccount(None,None,0,"Active","CurrentAccount")
        account.overdraft(300)
        self.assertEqual(account.balance,-300)
    
    def test_withrawal_overdraftlimitincrement(self):
        account = CurrentAccount(None,None,0,"Active","SavingsAccount")
        account.withdraw(400)
        account.withdraw(110)
        self.assertEqual(account.balance,-400)
    
    def test_withrawal_overdraftlimit(self):
        account = CurrentAccount(None,None,0,"Active","SavingsAccount")
        account.withdraw(600)
        self.assertEqual(account.balance,0)
    
    # class Bank
    
    
        
def run_unittest():
    unittest.main(argv=[' '],verbosity=0,exit=False)

if __name__ == "__main__":
    run_unittest()