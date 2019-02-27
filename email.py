import smtplib
import pandas as pd

df = pd.read_csv("file:///Users/yogesh/Downloads/TechVita1.0_FinalSheet1.csv")#location of file in the form of csv

mail = smtplib.SMTP('smtp.gmail.com', 587)#if you are using gmail account
mail.ehlo() #helo can also be used
mail.starttls()
mail.login("unknown@gmail.com","Password")# type your email and password
for i in range(34):
    content ="Hello "+df['NAME'][i]+", "+"any message "#df['NAME'] is the name of column in the data frame or CSV file which contain name 
    message='Subject: {}\n\n{}'.format(subject,content)
    mail.sendmail("unknown@gmail.com",df['EMAIL'][i], message)#df['EMAIL'] is the name of column in the data frame or CSV file and which contain email
    print(i)

print("Completed")

mail.close()    
