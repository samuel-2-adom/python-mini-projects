from text_analysis_generation.text_analysis_generation import split_text,sub,clean_text,is_special_line
from anagrams_palindromes_metathesis_pair.anagrams_palindromes_metathesis_pair import is_anagram,is_palindromes,reverse,is_meta_pair
from caesar_cipher.caesar_cipher import encode,decode
from calculator.calculator import add,mul,pow,div,subs 
from find_duplicates.find_duplicate import is_path,same_content
from pattern_search_count_regex.pattern_search_count_regex import find_first,count_first
from banking_simulator.banking_simulator import account_number,date,Customer


import unittest
import os
from unittest import TestCase

class TestExample(TestCase):

    # Text_Analysis_Generation
    def test_is_specialline(self):
        result = is_special_line("*** He took that beating like a chanp")
        self.assertTrue(result, "*** He took that beating like a champ")

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
        self.assertTrue(result,True)
    
    def test_is_palindromes(self):
        result = is_palindromes("mom")
        self.assertTrue(result,True)
    
    def test_reverse(self):
        result = reverse("trap")
        self.assertTrue(result,"part")
    
    def test_is_meta_pair(self):
        result = is_meta_pair("carve","crave")
        self.assertTrue(result,True)

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
        self.assertTrue(result,True)
        os.remove(f)
    
    def test_samecontent(self):
        f = "logs4q1.txt"
        f1 = "logs4q2.txt"
        with open(f,"w",encoding="utf-8") as file1,\
             open(f1,"w",encoding="utf-8") as file2:
            file1.write("suck it")
            file2.write("shut it")
        result = same_content(f,f1,f,f1)
        self.assertFalse(result,True)
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
            file.write("the greates showman")
        result = count_first("showman",f)
        self.assertEqual(result, 1)
        os.remove(f)
    
    # Banking Simulation
    def test_acc_num(self):
        result = account_number()
        self.assertTrue(len(result) == 8)
    
    def test_classcustomer_name(self):
        customer = Customer("Gracious","0333****","gracious4165@***")
        self.assertEqual(customer.name,"Gracious")
    
    def test_classcustomer_phone(self):
        customer = Customer("Gracious","0333****","gracious4165@***")
        self.assertEqual(customer.phone,"0333****")
    
    def test_classcustomer_email(self):
        customer = Customer("Gracious","0333****","gracious4165@***")
        self.assertEqual(customer.address,"gracious4165@***")
        
def run_unittest():
    unittest.main(argv=[' '],verbosity=0,exit=False)

if __name__ == "__main__":
    run_unittest()