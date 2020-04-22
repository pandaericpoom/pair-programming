import unittest
import sys
//Hello


def tax_cal(income_self,income_couple):
    print("Salaries Tax Computation (per MONTH)")
    income_self = float(input("Please Self income :"))
    income_couple = float(input("Please Spouse income :"))
    #print(income_self)
    #print(income_couple)

    #print(married_status)

    #Declearation

    Mandatory_Provident_Fund = 0
    couple_Mandatory_Provident_Fund = 0
    net_income_couple = 0
    net_income = 0
    joint_net_income = 0
    net_chargeable = 0
    net_chargeable_couple = 0
    standard_tax = 0
    standard_tax_couple = 0
    joint_net_chargeable = 0
    joint_final = 0
    joint_separate_tax = 0
    couple_final_tax = 0
    couple_separate_tax = 0
    self_final_tax = 0
    separate_tax = 0
    joint_standard_tax = 0

    #madatory contribution
    if income_self <7100:
        Mandatory_Provident_Fund = 0
    elif income_self <=30000:
        Mandatory_Provident_Fund = income_self*0.05
    else:
        Mandatory_Provident_Fund=1500
    print('')
    print('Self Mandatory_Provident_Fund mandatory:')
    print('MONTHLY: $'+str(Mandatory_Provident_Fund))
    print('YEARLY: $'+str(Mandatory_Provident_Fund*12))



    if income_couple <7100:
        couple_Mandatory_Provident_Fund = 0
    elif income_couple <=30000:
        couple_Mandatory_Provident_Fund = income_couple*0.05
    else:
        couple_Mandatory_Provident_Fund=1500
    print('')
    print('Spouse Mandatory_Provident_Fund mandatory:')
    print('MONTHLY: $'+str(couple_Mandatory_Provident_Fund))
    print('YEARLY: $'+str(couple_Mandatory_Provident_Fund*12))


    #Net Chargeable income
    print('')
    print('Yearly Self income: $'+str(income_self*12))
    print('')
    print('Separated Allowances 20/21: $132000')
    print('')
    net_chargeable= (income_self*12) - (Mandatory_Provident_Fund*12) - 132000
    if net_chargeable<0:
        print('Self Net Chargeable Income: $0')
        net_chargeable=0
    else:   
        print('Self Net Chargeable Income: $'+str(net_chargeable))
        
    


    print('')
    print('Yearly Spouse income: $'+str(income_couple*12))
    print('')
    print('Separated Allowances 20/21: $132000')
    print('')
    net_chargeable_couple= (income_couple*12) - (couple_Mandatory_Provident_Fund*12) - 132000
    if net_chargeable_couple<0:
        print('Spouse Net Chargeable Income: $0')
        net_chargeable_couple=0
    else:   
        print('Spouse Net Chargeable Income: $'+str(net_chargeable_couple))


    print('')
    print('Separated Allowances 20/21: $132000')
    print('')
    joint_net_chargeable= (income_couple*12) + (income_self*12) - (couple_Mandatory_Provident_Fund*12) - (Mandatory_Provident_Fund*12) - 264000
    if joint_net_chargeable<0:
        print('Joint Net Chargeable Income: $0')
        joint_net_chargeable=0
    else:   
        print('Joint Net Chargeable Income: $'+str(joint_net_chargeable))
        pass

    # Net income
    net_income_couple = (income_couple * 12) - (couple_Mandatory_Provident_Fund * 12)
    if net_income_couple < 0:
        print('Spouse Net  Income: $0')
        net_income_couple = 0
    else:
        print('Spouse Net  Income: $' + str(net_income_couple))

    net_income = (income_self * 12) - (Mandatory_Provident_Fund * 12)
    if net_income < 0:
        print('Self Net  Income: $0')
        net_chargeable = 0
    else:
        print('Self Net  Income: $' + str(net_income))

    joint_net_income = (income_couple * 12) + (income_self * 12) - (couple_Mandatory_Provident_Fund * 12) - (
    Mandatory_Provident_Fund * 12)
    if joint_net_income < 0:
        print('Joint Net  Income: $0')
        joint_net_income = 0
    else:
        print('Joint Net  Income: $' + str(joint_net_income))
    
    #Salary Tax Paid (Joint Standard)
    joint_standard_tax=joint_net_income*0.15

    # Salary Tax Paid (Separate Standard)
    standard_tax = net_income * 0.15

    standard_tax_couple = net_income_couple * 0.15

    #Salary Tax paid (Separate)
    if net_chargeable <=50000:
        separate_tax= net_chargeable*0.02
    elif net_chargeable <= 100000:
        separate_tax= 1000 + (net_chargeable-50000)*0.06
    elif net_chargeable <= 150000:
        separate_tax= 1000 + 3000 +(net_chargeable-100000)*0.1
    elif net_chargeable <= 200000:
        separate_tax= 1000 + 3000 + 5000 + (net_chargeable-150000)*0.14
    else:
        separate_tax= 1000 + 3000 + 5000 + 7000+ (net_chargeable-200000)*0.17
    print('')   

    
    if standard_tax <separate_tax:
        print('Self Tax paid under separate assessment: $'+str(standard_tax))
        self_final_tax=standard_tax
    else:
        print('Self Tax paid under separate assessment: $'+str(separate_tax))
        self_final_tax=separate_tax

    if net_chargeable_couple <=50000:
        couple_separate_tax= net_chargeable_couple*0.02
    elif net_chargeable_couple <= 100000:
        couple_separate_tax= 1000 + (net_chargeable_couple-50000)*0.06
    elif net_chargeable_couple <= 150000:
        couple_separate_tax= 1000 + 3000 +(net_chargeable_couple-100000)*0.1
    elif net_chargeable_couple <= 200000:
        couple_separate_tax= 1000 + 3000 + 5000 + (net_chargeable_couple-150000)*0.14
    else:
        couple_separate_tax= 1000 + 3000 + 5000 + 7000+ (net_chargeable_couple-200000)*0.17
    print('')
    print('Spouse Tax paid under separate assessment: $'+str(couple_separate_tax))

    
    if standard_tax_couple <couple_separate_tax:
        print('Self Tax paid under separate assessment: $'+str(standard_tax_couple))
        couple_final_tax=standard_tax_couple
    else:
        print('Self Tax paid under separate assessment: $'+str(couple_separate_tax))
        couple_final_tax=couple_separate_tax

    print('Total Tax paid under separate assessment: $'+str(couple_final_tax+self_final_tax))

    #Salary Tax paid (Separate)
    if joint_net_chargeable <=50000:
        joint_separate_tax= joint_net_chargeable*0.02
    elif joint_net_chargeable <= 100000:
        joint_separate_tax= 1000 + (joint_net_chargeable-50000)*0.06
    elif joint_net_chargeable <= 150000:
        joint_separate_tax= 1000 + 3000 +(joint_net_chargeable-100000)*0.1
    elif joint_net_chargeable <= 200000:
        joint_separate_tax= 1000 + 3000 + 5000 + (joint_net_chargeable-150000)*0.14
    else:
        joint_separate_tax= 1000 + 3000 + 5000 + 7000+ (joint_net_chargeable-200000)*0.17
    print('')


    if joint_standard_tax< joint_separate_tax:
        print('Total Tax paid under joint assessment: $'+str(joint_standard_tax))
        joint_final=joint_standard_tax
    else:
        print('Total Tax paid under joint assessment: $'+str(joint_separate_tax))
        joint_final=joint_separate_tax

    if (couple_final_tax+self_final_tax) > joint_final:
        print('')   
        print('')   
        print("You should choose JOINT assessment")

    elif (couple_final_tax+self_final_tax) < joint_final:
        print('')   
        print('')   
        print("You should choose SEPERATE assessment")

    else:
        print("You can choose either SEPERATE or JOINT assessment")

    return(self_final_tax,couple_final_tax,joint_separate_tax,)
class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(tax_cal(20000, 20000), (3760, 3760, 14880),
                         "shouldbe 3760, 3760, 14880")
    def test2(self):
        self.assertEqual(tax_cal(10000, 10000), (0, 0, 0),
                         "shouldbe 0, 0, 0")
    def test3(self):
        self.assertEqual(tax_cal(50000, 50000), (58500.0, 58500.0, 135000.0),
                         "shouldbe 58500.0, 58500.0, 135000.0")
    def test4(self):
        self.assertEqual(tax_cal(27000, 27000), (12612.0, 12612.0, 41772.0),
                         "shouldbe 12612, 12612, 41772")
    def test5(self):
        self.assertEqual(tax_cal(15964.91, 0), (999.9994799999997, 0, 0),
                         "shouldbe 15964.91, 0, 0")
    def test6(self):
        self.assertEqual(tax_cal(15964.91, 15964.91), (999.9994799999997, 999.9994799999997, 3999.9968799999983),
                         "shouldbe 999.9994799999997.91, 999.9994799999997, 3999.9968799999983")
    def test7(self):
        self.assertEqual(tax_cal(15964.91, 15965), (999.9994799999997, 1000.06, 4000.0973999999987),
                         "shouldbe 999.9994799999997.91, 1000.06, 4000.0973999999987")
    def test8(self):
        self.assertEqual(tax_cal(16999, 16999), (1707.3160000000003,1707.3160000000003, 6357.719999999996),
                         "shouldbe 1707.3160000000003, 1707.3160000000003, 6357.719999999996")
    def test9(self):
        self.assertEqual(tax_cal(17000, 17000), (1708.0,1708.0, 6360.0),
                         "shouldbe 1708.0, 1708.0, 6360.0")
    def test10(self):
        self.assertEqual(tax_cal(25000, 25000), (9420.0, 9420.0, 34020.0),
                         "shouldbe 9420, 9420, 34020")
    def test11(self):
        self.assertEqual(tax_cal(30000, 30000), (17700, 17700, 53400),
                         "shouldbe 17700, 17700, 53400")
    def test12(self):
        self.assertEqual(tax_cal(40000, 40000), (38100, 38100, 94200),
                         "shouldbe 38100, 38100, 94200")
    def test13(self):
        self.assertEqual(tax_cal(10000, 50000), (0.0, 58500.0, 55440.0),
                         "shouldbe 0, 58500, 55440")
    def test14(self):
        self.assertEqual(tax_cal(50000, 10000), (58500, 0, 55440),
                         "shouldbe 58500, 0, 55440")
    def test15(self):
        self.assertEqual(tax_cal(15965, 15965), (1000.06, 1000.06, 4000.2),
                         "shouldbe 1000.06, 1000.06, 4000.2")
    def test16(self):
        self.assertEqual(tax_cal(15964, 15964), (999.7920000000001, 999.7920000000001, 3998.751999999997),
                         "shouldbe 999.7920000000001, 999.7920000000001, 3998.751999999997")
    def test17(self):
        self.assertEqual(tax_cal(20350, 20350), (3999.4, 3999.4, 15997.2),
                         "shouldbe 3999.4, 3999.4, 15997.2")
    def test18(self):
        self.assertEqual(tax_cal(20351, 20351), (4000.1399999999994, 4000.1399999999994, 16000.476000000008),
                         "shouldbe 4000.1399999999994, 4000.1399999999994, 16000.476000000008")
    def test19(self):
        self.assertEqual(tax_cal(24736, 24736), (8999.040000000003, 8999.040000000003, 32996.736000000004),
                         "shouldbe 8999.040000000003, 8999.040000000003, 32996.736000000004")
    def test20(self):
        self.assertEqual(tax_cal(24737, 24737), (9000.251999999999, 9000.251999999999, 33000.612000000016),
                         "shouldbe 9000.251999999999, 9000.251999999999, 33000.612000000016")
    def test21(self):
        self.assertEqual(tax_cal(29122, 29122), (15998.712, 15998.712, 49996.87200000002),
                         "shouldbe 15998.712, 15998.712, 49996.87200000002")
    def test22(self):
        self.assertEqual(tax_cal(29123, 29123), (16000.374000000002, 16000.374000000002, 50000.747999999985),
                         "shouldbe 16000.374000000002, 16000.374000000002, 50000.747999999985")
    def test23(self):
        self.assertEqual(tax_cal(17001, 17001), (1708.6839999999997,1708.6839999999997, 6362.280000000004),
                         "shouldbe 1708.6839999999997,1708.6839999999997, 6362.280000000004")
    
    
    
        
        
if __name__ == '__main__':
    sys.exit(tax_cal(0,0))

