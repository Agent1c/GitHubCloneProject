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

def employee_database():
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

