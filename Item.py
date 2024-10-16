class Item:
    def __init__(self):
        self.Rang = None
        self.Nom_de_l_entreprise = None
        self.url_de_l_entreprise = None
        self.phones = None
        self.emails = None
        self.addresses = None
        self.linkedin = None
        self.founder_profile = None
        self.founder_profile_url = None
        self.profiles = None
        self.Taux_de_croissance_Annuel_moyen = None
        self.Taux_de_croissance_2019_2022 = None
        self.Chiffre_d_affaires_2022 = None
        self.Chiffre_d_affaires_2019 = None
        self.Salariés_2022 = None
        self.Salariés_2019 = None
        self.Salariés_Créations_de_postes_en_2024 = None
        self.Total_2024 = None
        self.Secteur = None
        self.Région = None
        
    def init_from_dic(self, dic):
        self.Rang = dic.get('Rang')
        self.Nom_de_l_entreprise = dic.get('Nom_de_l_entreprise')
        self.url_de_l_entreprise = dic.get('url_de_l_entreprise')
        self.phones = dic.get('phones')
        self.emails = dic.get('emails')
        self.addresses = dic.get('addresses')
        self.linkedin = dic.get('linkedin')
        self.founder_profile = dic.get('founder_profile')
        self.founder_profile_url = dic.get('founder_profile_url')
        self.profiles = dic.get('profiles')
        self.Taux_de_croissance_Annuel_moyen = dic.get('Taux_de_croissance_Annuel_moyen')
        self.Taux_de_croissance_2019_2022 = dic.get('Taux_de_croissance_2019_2022')
        self.Chiffre_d_affaires_2022 = dic.get('Chiffre_d_affaires_2022')
        self.Chiffre_d_affaires_2019 = dic.get('Chiffre_d_affaires_2019')
        self.Salariés_2022 = dic.get('Salariés_2022')
        self.Salariés_2019 = dic.get('Salariés_2019')
        self.Salariés_Créations_de_postes_en_2024 = dic.get('Salariés_Créations_de_postes_en_2024')
        self.Total_2024 = dic.get('Total_2024')
        self.Secteur = dic.get('Secteur')
        self.Région = dic.get('Région')
        
    def __str__(self):
        return f"Rang = {self.Rang}\nNom_de_l_entreprise = {self.Nom_de_l_entreprise}\nurl_de_l_entreprise = \
        {self.url_de_l_entreprise}\nTaux_de_croissance_Annuel_moyen = {self.Taux_de_croissance_Annuel_moyen}\nTaux_de_croissance_2019_2022 = \
        {self.Taux_de_croissance_2019_2022}\nChiffre_d_affaires_2022 = {self.Chiffre_d_affaires_2022}\nChiffre_d_affaires_2019 = \
        {self.Chiffre_d_affaires_2019}\nSalariés_2022 = {self.Salariés_2022}\nSalariés_2019 = {self.Salariés_2019}\`nSalariés_Créations_de_postes_en_2024 = \
        {self.Salariés_Créations_de_postes_en_2024}\nTotal_2024 = {self.Total_2024}\nSecteur = {self.Secteur}\nRégion = {self.Région}\nphones = \
        {self.phones}\nemails = {self.emails}\naddresses = {self.addresses}\nlinkedin = {self.linkedin}\nfounder_profile = \
        {self.founder_profile}\nprofiles = {self.profiles}"
