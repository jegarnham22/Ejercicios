class Repositorio:
    
    def __init__(self, archivos=[]):
        self.archivos_remotos = []
        self.archivos_locales = archivos
        self.archivos_staging = []
        #puedes agregar más atributos si lo estimas necesario ;)
        
    def git_add(self, archivos):
        for archivo in archivos:
            self.archivos_staging.append(archivo)
        #falta chequeo de que no se repitan
    
        
    def git_commit(self, comentario):
        for doc in self.archivos_staging:
            self.archivos_locales.append(doc)
        print(comentario)
        
    
    def git_push(self):
        largo=len(self.archivos_locales)
        for x in range (0,largo-1):
            y=self.archivos_locales.pop(0)
            self.archivos_remotos.append(y)



if __name__ == "__main__":
    mi_repo = Repositorio(["main.py", "windows.py", "user.txt"])
    mi_repo.git_add('README.md')
    mi_repo.git_commit('Agregado el README :D')
    mi_repo.git_push()
    mi_repo.git_add(["data.json", "client.py", "user.txt"])
    mi_repo.git_commit("subiendo datos")
    mi_repo.git_push()