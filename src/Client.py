from pydantic import BaseModel


class Client(BaseModel):
    name: str
    password: str

    def __str__(self):
        return[self.name, self.password]
    

    def new_client(name, password):
        return(Client(name=name, password=password))
    

class ClientCatalog(BaseModel):
    clients: dict[str, Client] = {}

    
    def load(file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            return ClientCatalog.model_validate_json(fp.read())


    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.model_dump_json())

    
    def signup(self, c: Client):
        self.clients[c.name] = c


    def login(self, username, passw):
        for key, client in self.clients.items():
            if self.clients[key].name == username:
                if self.clients[key].password == passw:
                    print("LogIn com sucesso!")
                    return 1
                else:
                    print("Password errada!")
                    return 0