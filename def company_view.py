def company_view():
  print('''
  ****Welcome to your main menu****
  you have the following options available
  1.DashBoard
  2.Profile
  3.Departments
  4.Employees
  ''')
  user_option = input('Choose your Option.')

  if user_option == '1':
     company_employees()
  elif user_option== '2':
     print('Company Departments')
     compony_departments()
  elif user_option == '3':
      print('Company Employees')
      company_employees()
     
  
def compony_departments():
  departments = {
          1: 'Marketing',
          2: 'Sales',
          3: 'Finance',
          4: 'Human Resources',
          5: 'Information Technology',
          6: 'Legal',
          7: 'Operations',
          8: 'Research and Development',
          9: 'Customer Service',
          10: 'Purchasing',
          11: 'Administration',
          12: 'Accounting',
          13: 'Engineering',
          14: 'Management',
          15: 'Public Relations',
          16: 'Quality Assurance',
          17: 'Training',
          18: 'Logistics',
          19: 'Maintenance',
          20: 'Security',
          21: 'Shipping',
          22: 'Warehouse',
          23: 'Production',
          24: 'Facilities',
          25: 'Inventory',
          26: 'Supply Chain',
          27: 'Health and Safety',
          28: 'Procurement',
          29: 'Quality Control',
          30: 'Distribution',
          31: 'Customer Support',
          32: 'Technical Support',
          33: 'Data Entry',
          34: 'Recruiting',
          35: 'Training',
          36: 'Consulting',
          37: 'Catering',
          38: 'Hospitality',
          39: 'Travel',
          40: 'Real Estate',
          41: 'Insurance',
          42: 'Banking',
          43: 'Investment',
          44: 'Mortgage',
          45: 'Credit',
          46: 'Loans',
          47: 'Taxes',
          48: 'Audit',
          49: 'Compliance',
          50: 'Risk Management',
          51: 'Regulatory Affairs',
          52: 'Legal Affairs',
          53: 'Contracts',
          54: 'Intellectual Property',
          55: 'Patents',
          56: 'Trademarks',
          57: 'Copyrights',
          58: 'Litigation',
          59: 'Arbitration',
          60: 'Mediation',
          61: 'Negotiation',
          62: 'Settlement',
          63: 'Claims',
          64: 'Disputes',
  }

def company_employees():
   names = {
          1: 'Aarya Clark',
          2: 'John Garner',
          3: 'Jacqueline Graves',
          4: 'Cesar Griffin',
          5: 'Charlie Mayer',
          6: 'Yahir Roberson',
          7: 'Sasha Savage',
          8: 'Keaton McClain',
          9: 'Marleigh Chen',
          10: 'Emmanuel Curry',
          11: 'Alison Owens',
          12: 'Adriel Huff',
          13: 'Karsyn Avery',
          14: 'Jakari Michael',
          15: 'Aubriella Bush',
          16: 'Tyson Ali',
          17: 'Zelda Nguyen',
          18: 'Gabriel Meza',
        }
        
   for name in names:
      print(names[name])
 
def employee_view():
    print('''
    ****Welcome to your Employee menu****
    you have the following options available
    1.Names and Surname
    2.Profile
    3.Departments and Position
    4. Exit
    ''')
    user_option = input('Choose your Option.')

    if user_option == '1':
        print("""
      Your Name and Surname

      name:Mr Program
      Surname: Quiz_
      """)
    elif user_option == '2':
        print("""
        Your Profile Picture!!
        """)
        
    elif user_option == '3':
        print("""
        Your Department is:
        Title: Senior Buyer
        """)
    elif user_option == '4':
        print('Thank for using the program')
        exit()
  
user_login = input('enter user name: ')
user_password = input('Enter your password: ')
  
if user_login and user_password == 'admin':
  print('youre logged in')
  company_view()
elif user_login and user_password == 'user':
    print('You logged as employee')
    employee_view()
else:
  print("No user found or Check your password correct.")

