class Database():
    sqlite3 = __import__('sqlite3')
    
    def __init__(self):
        self.nomBD='dic-database.db'        
    
    def createTableDIC(self):
        conn = self.sqlite3.connect(self.nomBD)
        try:
            cursor=conn.cursor()
            cursor.execute("""
            CREATE TABLE DIC(
            id_ept INTEGER ,
            nom Varchar(50) not null,
            prenom Varchar(50) not null,
            department Varchar(10) CHECK( department IN ('GIT','GEM','GC','AERO') )  NOT NULL,
            niveau Varchar(4) CHECK( niveau IN ('TC1','TC2','DIC1','DIC2','DIC3') )  NOT NULL,
            telephone VARCHAR(12) not null,
            PRIMARY KEY(id_ept)
            )
            """)
            conn.commit()
            print("Table crée avec succès")
            conn.close()
        except self.sqlite3.OperationalError as e:
            print(e)
            
    def save_db(self):
        conn = self.sqlite3.connect(self.nomBD)

        dico={"nom":"","prenom":"","department":"","niveau":"","telephone":""}
        infos=list()
        
        for key in dico.keys():
            try:
                v=eval(input("entrer {}".format(key)))
                if not isinstance(v,str):
                    print("donnée invalide!!!")
                    break
                else:
                    infos.append(v)
            except NameError:
                print("mettre les entrées sous crochet")
                break
        try:
            infos=tuple(infos)
            print(infos)
            cursor=conn.cursor()
            cursor.execute("""
            INSERT INTO DIC(nom,prenom,department,niveau,telephone) VALUES(?, ?, ?, ?,?);""",infos)
            print("insertions réussies")
            conn.commit()
            conn.close()
        except self.sqlite3.ProgrammingError:
            conn.close()
        
    
    def delete_db(self):
        conn = self.sqlite3.connect(self.nomBD)
        inf=list()
        dico={"nomEtudiant":"", "prenomEtudiant":""}
        for key in dico.keys():
            try:
                v=eval(input("entrer {}".format(key)))
                if not isinstance(v,str):
                    print("donnée invalide!!!")
                    break
                else:
                    inf.append(v)
            except NameError:
                print("mettre les entrées sous crochet")
                break
        try:
            cursor=conn.cursor()
            inf=tuple(inf)
            cursor.execute("""DELETE FROM DIC WHERE nom=? and prenom=?;""",inf)
            print("suppression réussies")
            conn.commit()
            conn.close()
        except self.sqlite3.ProgrammingError:
            conn.close()
    
    def modifier_db(self):
        conn = self.sqlite3.connect(self.nomBD)
        dico={"nomEtudiant":"", "prenomEtudiant":""}
        infos=list()
        for key in dico.keys():
            try:
                v=eval(input("entrer {}".format(key)))
                if not isinstance(v,str):
                    print("donnée invalide!!!")
                    break
                else:
                    infos.append(v)
            except NameError:
                print("mettre les entrées sous crochet")
                break
        try:
            valeurs=list()
            print("veuillez saisir les nouvelles informations de l'Etudiant")
            infosEtudiant={"nom":"","prenom":"","departement":"","niveau":"","telephone":""}
            for key in infosEtudiant.keys():
                try:
                    v=eval(input("entrer {}".format(key)+" "))
                    if not isinstance(v,str):
                        print("donnée invalide!!!")
                        break
                    else:
                        valeurs.append(v)
                except NameError:
                    print("mettre les entrées sous crochet")
                    break
            
            data=valeurs+infos
            infosEtudiant.update(dico)
            cursor=self.conn.cursor()
            cursor.execute("""UPDATE DIC SET nom=?, prenom=?,department=?,
            niveau=?,telephone=? WHERE nom=? and prenom=?; """,tuple(data))
            print("modifications réussies")
            conn.commit()
            conn.close()
        except self.sqlite3.ProgrammingError:
            conn.close()
        
        
    
    
    def get_db(self):
        conn = self.sqlite3.connect(self.nomBD)
        infos=list()
        dico={"nomEtudiant":"", "prenomEtudiant":""}
        for key in dico.keys():
            try:
                v=eval(input("entrer {}".format(key)))
                if not isinstance(v,str):
                    print("donnée invalide!!!")
                    break
                else:
                    infos.append(v)
            except NameError:
                print("mettre les entrées sous crochet")
                break
        try:
            print(tuple(infos))
            cursor=conn.cursor()
            cursor.execute("""SELECT * from DIC where nom=? and prenom=?;""",tuple(infos))
            response=cursor.fetchone()
            conn.close()
            return response
            
        except (self.sqlite3.ProgrammingError,self.sqlite3.Error):
            conn.close()
        
    
        
    def get_all_db(self):
        conn = self.sqlite3.connect(self.nomBD)
        try:
            cursor=conn.cursor()
            cursor.execute("""SELECT * from DIC; """)
            response=cursor.fetchall()
            conn.close()
            return response
            
        except (self.sqlite3.ProgrammingError,sqlite3.Error):
            conn.close()
         
        
        
        
        
        
            
        
        
        
        
        
    def __str__(self):
        return "nom de la BD : {}".format(self.nomBD)

if __name__ == '__main__':
    mydb=Database()
    mydb.createTableDIC()
    #mydb.save_db()
    #mydb.delete_db()
    
    