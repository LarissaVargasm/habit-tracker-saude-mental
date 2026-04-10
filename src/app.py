import json
import os 

class HabitTracker: 
    def __init__(self, storage_path="habits.json"):
        self.storege_path = storage_path
        self.habits = self._load_data()

    def _load_data(self):
        if os.path.exists(self.storege_path):
            with open(self.storege_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return{}
        return {}
    
    def _save_data(self):
        with open (self.storege_path, 'w') as f:
            json.dump(self.habits, f, indent=4)
    
    def add_habit (self, name):
        if not name or name.strip() == "": 
            return "Erro: O nome do hábito não pode ser vazio."
        if name in self.habits:
            return f"Erro: O hábito '{name}' já existe."
        
        self.habits[name] = {"completed": False}
        self._save_data()
        return f"Hábito '{name}' adicionado com sucesso!"
    
def edit_habit(self, old_name, new_name):
    if old_name not in self.habits:
        return f"Erro: Hábito '{old_name}' não foi encontrado."
    if not new_name or new_name.strip() == "":
        return "Erro: o novo nome não pode ser vazio."
    
#Vai pegar os dados atuais, remover a chave antiga e criar a nova chave.
    data = self.habits.pop(old_name)
    self.habits[new_name] = data
    self._svae_data()
    return f"Hábito '{old_name}' alterado com sucesso para '{new_name}'!"

    def list_habits(self):
        return self.habits
    
    def complete_habit(self, name):
        if name in self.habits:
            self.habits[name]["completed"] = True
            self._save_data()
            return f"Muito bem! Você concluiu: {name}"
        return "Erro: Esse hábito não foi encotrado"
    
#Simulação de interface CLI
def main():
    tracker = HabitTracker
print ("--- HabitTracker: Foco em Saúde Mental ---")
print ("1. Adicionar Hábito | 2. Listar | 3. Concluir | 4. Sair  | 5. Alterar ")

if __name__ == "__main__":
    main()