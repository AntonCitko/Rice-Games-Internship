import pandas as pd
import mysql.connector as mysql

db = mysql.connect(
        host = "Antons-MacBook-Air.local",
        user = "Anton",
        passwd = "Pinktiger1!",
        database = "ricegames"
        )

table_members = pd.read_sql("SELECT * FROM members", con = db)
table_payment = pd.read_sql("SELECT * FROM payment", con = db)
table_enemies = pd.read_sql("SELECT * FROM sanrin_enemies", con = db)

enemy_type_query = """SELECT name, eng_name,
	CASE
		WHEN hp > 10 THEN 'BOSS'
        ELSE 'ZAKO'
	END AS type
FROM sanrin_enemies
ORDER BY type DESC;"""

table_enemies_type = pd.read_sql(enemy_type_query, con = db)

#table_h = pd.read_csv("/Users/Anton/Documents/GitHub/Rice-Games-Internship/Session 3P - SQL Database Fundamentals/Table H.csv")
#table_mc = pd.read_csv("/Users/Anton/Documents/GitHub/Rice-Games-Internship/Session 3P - SQL Database Fundamentals/Table Mc.csv")
#table_p = pd.read_csv("/Users/Anton/Documents/GitHub/Rice-Games-Internship/Session 3P - SQL Database Fundamentals/Table P.csv")
#table_q = pd.read_csv("/Users/Anton/Documents/GitHub/Rice-Games-Internship/Session 3P - SQL Database Fundamentals/Table Q.csv")

finished = False

print("Welcome to Rice Games. This programs allows you to view data on Team Members, Payroll, and Enemies in the Sanrin level. Enter \"q\" at any time to quit.")

while not finished:
    m_or_e = input("Would you like to check out Team Members or Enemies? ")
    while m_or_e != "Team Members" and m_or_e != "Enemies" and m_or_e != "q":
        m_or_e = input("Invalid selection, must enter \"Enemies\" or \"Team Member\" ")
        
    if m_or_e == "q":
        finished = True
        break
    
    if m_or_e == "Enemies":
        choice = input("""Would you like to
[a] Check list of enemies, name only
[b] List out the enemies (name and eng_name) in order of strength (bi) ascending (bii) descending
[c] List out the ZAKO enemies (name and eng_name)
[d] list out the BOSS enemies.
""")
    
        while choice != "q" and choice != "a" and choice != "b" and choice != "c" and choice != "d"and choice != "bi" and choice != "bii":
            choice = input("""You have not chosen a valid option. Please enter the letter of your choice.
 Would you like to
[a] Check list of enemies, name only
[b] List out the enemies (name and eng_name) in order of strength (bi) ascending (bii) descending
[c] List out the ZAKO enemies (name and eng_name)
[d] list out the BOSS enemies.
""")
        
        while choice == "b" and choice != "bi" and choice != "bii":
            choice = input("""You have chosen b
Please specify if you want to list out the enemies (name and eng_name) in order of strength (bi) ascending (bii) descending
""")
            
        if choice == "q":
            finished = True
            break
            
        if choice == "a":
            print(table_enemies.name.to_string())
        
        if choice == "bi":
            out = table_enemies.sort_values("attack", ascending = True)[["name", "eng_name"]]
            print(out.to_string())
            
        if choice == "bii":
            out = table_enemies.sort_values("attack", ascending = False)[["name", "eng_name"]]
            print(out.to_string())
        
        if choice == "c":
            zako_names = table_enemies_type.loc[table_enemies_type.type == "ZAKO",["name", "eng_name"]]
            print(zako_names.to_string())
            
        if choice == "d":
            boss_names = table_enemies_type.loc[table_enemies_type.type == "BOSS",["name", "eng_name"]]
            print(boss_names.to_string())
    
    else:
        choice = input("""Would you like to
[a] Check the list of team members, name only 
[b] Output a list of people in a certain profession (bi) programming (bii) art (biii) music 
[c] List out how much money each person has made (includes name and money) 
[d] List out the transactions (di) all transactions (dii) last 5 transactions (diii) transactions made to a certain person.
""")
        
        while choice != "q" and choice != "a" and choice != "b" and choice != "c" and choice != "d" and choice != "bi" and choice != "bii" and choice != "biii" and choice != "di" and choice != "dii" and choice != "diii":
            choice = input("""You have not chosen a valid option. Please enter the letter of your choice.
Would you like to
[a] Check the list of team members, name only 
[b] Output a list of people in a certain profession (bi) programming (bii) art (biii) music 
[c] List out how much money each person has made (includes name and money) 
[d] List out the transactions (di) all transactions (dii) last 5 transactions (diii) transactions made to a certain person.
""")
        
        while choice == "b" and choice != "bi" and choice != "bii" and choice != "biii":
            choice = input("""You have chosen b
Please specify if you want to output a list of people in a certain profession (bi) programming (bii) art (biii) music 
 """)
            
        while choice == "d" and choice != "di" and choice != "dii" and choice != "diii":
            choice = input("""You have chosen b
Please specify if you want to list out the transactions (di) all transactions (dii) last 5 transactions (diii) transactions made to a certain person
""")
            
        if choice == "q":
            finished = True
            break
        
        if choice == "a":
            print(table_members.Name.to_string())
            
        if choice == "bi":
            programmers = table_members.loc[(table_members.role == "Programmer") | (table_members.role == "Lead Developer"), "name"]
            print(programmers.to_string())
        
        if choice == "bii":
            art = table_members.loc[table_members.role == "Artist", "name"]
            print(art.to_string())
            
        if choice == "biii":
            art = table_members.loc[table_members.role == "Composer", "name"]
            print(art.to_string())
            
        if choice == "c":
            print(table_members[["name", "total"]].to_string())
        
        if choice == "di":
            print(table_payment[["name", "amount"]].to_string())
            
        if choice == "dii":
            num_rows = table_payment.shape[0]
            print(table_payment.iloc[num_rows - 5 : num_rows][["recipient", "amount"]].to_string())
            
        if choice == "diii":
            person = input("Which person would you like to see? ")
            if not table_payment.recipient.isin([person]).any():
                print("Person not found")
            
            else:
                print(table_payment.loc[table_payment.recipient == person, "amount"].to_string())
    
    
    
    
    
    
    
    
    
    
