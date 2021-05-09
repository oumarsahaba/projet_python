class GestionFichier():
    os = __import__('os')
    re = __import__('re')
    
    
    def count_nb_lines_mod(self, path):
        """retourne le nombre ligne de codes d'un module.py"""
        pattern1=r'^[ ]*["]{3}[0-9a-zA-Z | ]*["]{3}$'
        pattern2=r'^[ ]*[#]+'
        if self.os.path.exists(path):
            with open(path, 'r') as file:
                content=file.readlines()
                result=list()
                for elt in content:
                    elt=elt.rstrip()
                    if len(elt)!=0 and self.re.search(pattern1,elt)==None and self.re.search(pattern2,elt)==None:
                        result.append(elt)
                        
            return len(result)
                
            
        else:
            raise Exception("ce chemin n'est pas bon")
    
    
    
    def get_modules(self,path):
        """retourne la liste des modules python dans ce dossier"""
        pattern=r".+.py$"
        if self.os.path.exists(path) and self.os.path.isdir(path):
            content=self.os.listdir(path)
            result=list()
            for elt in content:
                if self.re.search(pattern,elt)!=None:
                    result.append(elt)
            return result
    
    
    
    
    def get_packages(self,path):
        """prend en entrée le path et retourne la liste de ses sous dossiers"""
        if self.os.path.exists(path) and self.os.path.isdir(path):
            content=self.os.listdir(path)
            result=list()
            for item in content:
                if self.os.path.isdir(path+item):
                    result.append(item)
            return result
        else:
            raise Exception("chemin invalide")
            
        
    def get_all_modules(self,path):
        """prend en entrée le path d'un paquet en python et retourne l'ensemble des modules de ce paquet"""
        if self.os.path.exists(path) and self.os.path.isdir(path):
            modules=[]
            packages=[]
            list_path=list()
            packages+=self.get_packages(path)
            modules+=self.get_modules(path)
            if len(self.get_packages(path))==0:
                return modules
            else:
                for i in packages:
                    path1=self.os.path.join(path,i+"/")
                    modules+=self.get_all_modules(path1)
                return modules
            
    def count_nb_lines_paquet(self,path):
        """retourne le nombre de ligne d'un paquet python"""
        nbre=0
        if self.os.path.exists(path) and self.os.path.isdir(path):
            pattern=r".+.py$"
            list_path=list()
            for dirpath, dirnames, files in os.walk(path,topdown=False):
                for file_name in files:
                    if re.search(pattern,file_name)!=None:
                        list_path.append(os.path.join(dirpath,file_name))
            for p in list_path:
                nbre+=self.count_nb_lines_mod(p)            
            return nbre
                        


if __name__ == '__main__':
    f=GestionFichier()
    f.get_all_modules('/Users/ahmadou-bamba/Desktop/DIC_2021/')
    f.count_nb_lines_mod('/Users/ahmadou-bamba/Desktop/Itachi_44/informatique/DIC1-GIT/POO_Python/modules_packages/DIC_2021/geometry/area.py')
    