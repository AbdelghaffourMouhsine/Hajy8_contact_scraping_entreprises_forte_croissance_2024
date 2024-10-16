import csv

class ItemStorage:
    def __init__(self, file_path, value=None):
        self.file_path = f"{file_path}.csv"
        self.fieldnames = ['Rang', 'Nom_de_l_entreprise', 'url_de_l_entreprise', 'phones','emails', 'addresses', 'linkedin', 'founder_profile',
        'founder_profile_url', 'profiles', 'Taux_de_croissance_Annuel_moyen', 'Taux_de_croissance_2019_2022',
        'Chiffre_d_affaires_2022', 'Chiffre_d_affaires_2019', 'Salariés_2022',
        'Salariés_2019', 'Salariés_Créations_de_postes_en_2024', 'Total_2024',
        'Secteur', 'Région']
        
        self.file = open(self.file_path, 'a', newline='', encoding='utf-8-sig')
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        
        # Check if the file is empty, then write the header
        if self.file.tell() == 0:
            self.writer.writeheader()
        if value:
            if type(value) == list:
                self.insert_items(value)
            else:
                self.insert_item(value)
            self.close_file()
            
    def insert_item(self, item):
        data = {
            'Rang' : item.Rang, 
            'Nom_de_l_entreprise' : item.Nom_de_l_entreprise, 
            'url_de_l_entreprise' : item.url_de_l_entreprise,
            'phones' : item.phones, 
            'emails' : item.emails, 
            'addresses' : item.addresses,
            'linkedin' : item.linkedin,
            'founder_profile' : item.founder_profile,
            'founder_profile_url' : item.founder_profile_url,
            'profiles' : item.profiles,
            'Taux_de_croissance_Annuel_moyen' : item.Taux_de_croissance_Annuel_moyen, 
            'Taux_de_croissance_2019_2022' : item.Taux_de_croissance_2019_2022, 
            'Chiffre_d_affaires_2022' : item.Chiffre_d_affaires_2022, 
            'Chiffre_d_affaires_2019' : item.Chiffre_d_affaires_2019, 
            'Salariés_2022' : item.Salariés_2022, 
            'Salariés_2019' : item.Salariés_2019, 
            'Salariés_Créations_de_postes_en_2024' : item.Salariés_Créations_de_postes_en_2024, 
            'Total_2024' : item.Total_2024,
            'Secteur' : item.Secteur,
            'Région' : item.Région
        }
        self.writer.writerow(data)
        
    def insert_items(self, items):
        for item in items:
            try:
                if type(item) == list:
                    self.insert_items(item)
                else:
                    self.insert_item(item)
            
            except Exception as e:
                print('error in insert_items : ',e)
            
    def close_file(self):
        self.file.close()



class ExceptionStorage:
    def __init__(self, item, error ,file_path='results/exceptions_2'):
        self.file_path = f"{file_path}.csv"
        self.fieldnames = ['Rang', 'Nom_de_l_entreprise', 'url_de_l_entreprise', 'phones','emails', 'addresses', 'linkedin', 'founder_profile', 
        'founder_profile_url', 'profiles',
        'Taux_de_croissance_Annuel_moyen', 'Taux_de_croissance_2019_2022', 'Chiffre_d_affaires_2022', 
        'Chiffre_d_affaires_2019', 'Salariés_2022', 'Salariés_2019', 'Salariés_Créations_de_postes_en_2024', 'Total_2024', 'Secteur', 'Région', 'error']
        
        self.file = open(self.file_path, 'a', newline='', encoding='utf-8-sig')
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        
        # Check if the file is empty, then write the header
        if self.file.tell() == 0:
            self.writer.writeheader()
            
        self.insert_item(item, error)
        self.close_file()
        
    def insert_item(self, item, error):
        data = {
            'Rang' : item.Rang, 
            'Nom_de_l_entreprise' : item.Nom_de_l_entreprise, 
            'url_de_l_entreprise' : item.url_de_l_entreprise,
            'phones' : item.phones, 
            'emails' : item.emails, 
            'addresses' : item.addresses,
            'linkedin' : item.linkedin,
            'founder_profile' : item.founder_profile,
            'founder_profile_url' : item.founder_profile_url,
            'profiles' : item.profiles,
            'Taux_de_croissance_Annuel_moyen' : item.Taux_de_croissance_Annuel_moyen, 
            'Taux_de_croissance_2019_2022' : item.Taux_de_croissance_2019_2022, 
            'Chiffre_d_affaires_2022' : item.Chiffre_d_affaires_2022, 
            'Chiffre_d_affaires_2019' : item.Chiffre_d_affaires_2019, 
            'Salariés_2022' : item.Salariés_2022, 
            'Salariés_2019' : item.Salariés_2019, 
            'Salariés_Créations_de_postes_en_2024' : item.Salariés_Créations_de_postes_en_2024, 
            'Total_2024' : item.Total_2024,
            'Secteur' : item.Secteur,
            'Région' : item.Région,
            'error' : error
        }
        self.writer.writerow(data)
            
    def close_file(self):
        self.file.close()