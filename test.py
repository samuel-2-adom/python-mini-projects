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

class TestAnalysisGen(TestCase):
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

class TestPairs(TestCase):
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

class TestCipher(TestCase):
    # Caesar  Cipher
    def test_encode(self):
        result = encode("give to caesar what is caesar's",5)
        self.assertEqual(result,"lnaj yt hfjxfw bmfy nx hfjxfw'x")

    def test_decode(self):
        result = decode("lnaj yt hfjxfw bmfy nx hfjxfw'x",5)
        self.assertEqual(result,"give to caesar what is caesar's")

class TestCalc(TestCase):
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

class TestDuplicate(TestCase):
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

class TestPatternSearch(TestCase):
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

class TestBankSim(TestCase):
    # Banking Simulation
    
    # class Customer
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
    def test_account_number(self):
        acc_num = account_number()
        account = Account(acc_num,None,0,"Active","Account",None,0,None)
        result = account.acc_number.startswith("1000") and len(account.acc_number) == 8
        self.assertTrue(result)
    
    def test_account_type(self):
        account = Account(None,None,0,"Active","CurrentAccount",None,0,None)
        result = account.acc_type == "CurrentAccount"
        self.assertTrue(result)
    
    def test_account_balance_interest(self):
        account = Account(None,None,104,"Active","Account",None,10,None)
        result = account.balance == 104 and account.interest == 10
        self.assertTrue(result)
    
    def test_account_holder_name(self):
        customer = Customer("Klien","0123xxxxxx","@klienXXX")
        account = Account(None,customer,0,"Active","Account",None,0,None)
        self.assertEqual(account.holder_info.name,"Klien")
    
    def test_account_holder_phone(self):
        customer = Customer("Klien","0123xxxxxx","@klienXXX")
        account = Account(None,customer,0,"Active","Account",None,0,None)
        self.assertEqual(account.holder_info.phone,"0123xxxxxx")
    
    def test_account_holder_address(self):
        customer = Customer("Klien","0123xxxxxx","@klienXXX")
        account = Account(None,customer,0,"Active","Account",None,0,None)
        self.assertEqual(account.holder_info.address,"@klienXXX")
        
    def test_fee(self):
        account = Account(None,None,0,"Active","Account")
        result = account.fee(101)
        self.assertEqual(result,1.01)
    
    def test_deposit_negative_amount(self):
        account1 = Account(None,None,0,"Active","Account")
        account1.deposit(-100)
        print()
        result = account1.balance == 100
        self.assertTrue(result)
    
    def test_deposit_zero_amount(self):
        account = Account(None,None,0,"Active","Account")
        account.deposit(0)
        print()
        self.assertTrue(account.balance==0)
    
    def test_deposit_closed_account(self):
        account1 = SavingsAccount(None,None,0,"Closed","Account")
        account1.deposit(50)
        self.assertEqual(account1.balance,0)
        
    def test_deposit(self):
        account = Account(None,None,0,"Active","Account")
        account.deposit(159.9)
        print()
        self.assertEqual(account.balance,159.9)
    
    def test_withdrawal_closed_account(self):
        account = Account(None,None,100,"Closed","Account",None,0,None)
        account.withdraw(59)
        self.assertEqual(account.balance,100)
    
    def test_withdrawal_negative_amount(self):
        account = Account(None,None,100,"Active","Account",None,0,None)
        account.withdraw(-59)
        self.assertEqual(account.balance,40.41)
    
    def test_withdrawal_andcharges(self):
        account = Account(None,None,159.9,"Active","Account")
        account.withdraw(100)
        print()
        self.assertEqual(round(account.balance,1),58.9)
    
    def test_transfer_receiving(self):
        account1 = Account(None,None,100,"Active","Account")
        account2 = Account(None,None,20,"Active","Account")
        account1.transfer(account2,40)
        print()
        self.assertEqual(account2.balance,60)
    
    def test_transfer_sending_andcharges(self):
        account1 = Account(None,None,100,"Active","Account")
        account2 = Account(None,None,20,"Active","Account")
        account1.transfer(account2,60)
        print()
        self.assertEqual(account1.balance,39.4)
    
    def test_transfer_closed_account_one_end(self):
        account1 = Account(None,None,100,"Active","Account")
        account2 = Account(None,None,20,"Closed","Account")
        account1.transfer(account2,60)
        self.assertEqual(account2.balance,20)
        
    def test_transfer_closed_account_both_ends(self):
        account1 = Account(None,None,100,"Closed","Account")
        account2 = Account(None,None,20,"Closed","Account")
        account1.transfer(account2,60)
        account2.transfer(account1,10)
        self.assertTrue(account1.balance == 100 and account2.balance == 20)
    
    def test_transfer_negative_amount(self):
        account1 = Account(None,None,100,"Active","Account")
        account2 = Account(None,None,20,"Active","Account")
        account1.transfer(account2,-60)
        self.assertEqual(account2.balance,80)
    
    def test_checkbalance(self):
        account = Account(None,None,159.9,"Active","Account")
        self.assertEqual(account.balance,159.9)
    
    def test_history(self):
        account = Account(None,None,0,"Active","Account")
        account.deposit(100)
        result = account.history
        self.assertTrue(len(result) == 1 and type(result) == list)
    
    #class SavingsAccount(Account)
    def test_withrawal_limit_three_per_session(self):
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
    
    def test_not_eligiblefor_overdraft(self):
        account = CurrentAccount(None,None,0,"Active","SavingsAccount")
        elig = account.eligible_for_overdraft(501)
        self.assertFalse(elig)
        
    def test_overdraft(self):
        account = CurrentAccount(None,None,0,"Active","CurrentAccount")
        account.overdraft(300)
        self.assertEqual(account.balance,-300)
    
    def test_withrawal_overdraftlimit_increment(self):
        account = CurrentAccount(None,None,0,"Active","SavingsAccount")
        account.withdraw(400) #yes
        account.withdraw(110) #yes
        self.assertEqual(account.balance,-400) #yes
    
    def test_withrawal_overdraftlimit(self):
        account = CurrentAccount(None,None,0,"Active","SavingsAccount")
        account.withdraw(600)
        self.assertEqual(account.balance,0)
       
def run_unittest():
    unittest.main(argv=[' '],verbosity=0,exit=False)

if __name__ == "__main__":
    run_unittest()