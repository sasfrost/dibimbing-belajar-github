import pandas as pd

#read CSV file from folder 
file_path = 'C:/!SASAKI/-FILES-/THECAREER/Dibimbing.id/04-Main_Material/03-Git/03-Git-assignment/dibimbing-belajar-github/03-Git-assignment_username_file.csv'
df = pd.read_csv(file_path) 

#show print DataFrame 
print(df)