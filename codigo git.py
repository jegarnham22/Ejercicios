class Repositorio:
    
    def __init__(self, archivos=[]):
        self.archivos_staging = archivos
        self.archivos_espera = []
        self.archivos_remotos = []
        #puedes agregar más atributos si lo estimas necesario ;)
        
    def git_add(self, archivos):
        

        pass
        
    def git_commit(self, comentario):
        print(comentario)
        #debes completar aquí
        pass
    
    def git_push(self):
        #debes completar aquí
        pass


if __name__ == "__main__":
    mi_repo = Repositorio(["main.py", "windows.py", "user.txt"])
    mi_repo.git_add('README.md')
    mi_repo.git_commit('Agregado el README :D')
    mi_repo.git_push()
    mi_repo.git_add(["data.json", "client.py", "user.txt"])
    mi_repo.git_commit("subiendo datos")
    mi_repo.git_push()