class Repositorio:
    
    def __init__(self, archivos=[]):
        self.archivos_remotos = []
        self.archivos_locales = archivos
        self.archivos_staging = []
        
    def git_add(self, *args):
        for archivo in args:
            self.archivos_staging.append(archivo)
        print("archivos en staging: " + str(self.archivos_staging))
        #falta chequeo de que no se repitan
    
        
    def git_commit(self, comentario):
        for doc in self.archivos_staging:
            doc=self.archivos_staging.pop(0)
            self.archivos_locales.append(doc)
        print(comentario)
        print("archivos en local: " + str(self.archivos_locales))
        
    
    def git_push(self):
        largo=len(self.archivos_locales)
        largoremoto=len(self.archivos_remotos)
        for x in range (0,largo):
            x=self.archivos_locales.pop(0)
            self.archivos_remotos.append(x)
        print("archivos en remoto: " + str(self.archivos_remotos))



if __name__ == "__main__":
    mi_repo = Repositorio(["main.py", "windows.py", "user.txt"])
    mi_repo.git_add('README.md')
    mi_repo.git_commit('Agregado el README :D')
    mi_repo.git_push()
    mi_repo.git_add(["data.json", "client.py", "user.txt"])
    mi_repo.git_commit("subiendo datos")
    mi_repo.git_push()