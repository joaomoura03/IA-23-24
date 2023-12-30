from pydantic import BaseModel


class Client(BaseModel):
    id: int
    name: str
    password: str

    def __str__(self):
        return[self.id, self.name, self.password]
    

    def new_client(id: int, name, password):
        return(Client(id=id, name=name, password=password))
    

class ClientCatalog(BaseModel):
    clients: dict[str, Client] = {}

    
    def load(file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            return ClientCatalog.model_validate_json(fp.read())


    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.model_dump_json())

    
    def signup(self, name, password):
        keys = list(self.clients.keys())
        if len(keys) == 0:
            id = "1"
        else:
            id = str(int(keys[-1]) + 1)
        self.clients[id] = Client.new_client(id, name, password)


    def login(self, name, password):
        for id, client in self.clients.items():
            if client.name == name and client.password == password:
                print("LogIn com sucesso!")
            elif client.name != name:
                print("Nome do utilizador errado!")
            elif client.password != password:
                print("Password errado!")