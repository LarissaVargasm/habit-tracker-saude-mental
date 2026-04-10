import json
import os

class HabitTracker:
    def __init__(self, storage_path="habits.json"):
        self.storage_path = storage_path
        self.habits = self._load_data()

    def _load_data(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def _save_data(self):
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.habits, f, indent=4, ensure_ascii=False)

    def add_habit(self, name):
        if not name or name.strip() == "":
            return "Erro: O nome do hábito não pode ser vazio."
        if name in self.habits:
            return f"Erro: O hábito '{name}' já existe."
        
        self.habits[name] = {"completed": False}
        self._save_data()
        return f"Hábito '{name}' adicionado com sucesso!"

    def edit_habit(self, old_name, new_name):
        if old_name not in self.habits:
            return f"Erro: Hábito '{old_name}' não encontrado."
        if not new_name or new_name.strip() == "":
            return "Erro: O novo nome não pode ser vazio."
        
        data = self.habits.pop(old_name)
        self.habits[new_name] = data
        self._save_data()
        return f"Hábito '{old_name}' alterado para '{new_name}'!"

    def list_habits(self):
        return self.habits

    def complete_habit(self, name):
        if name in self.habits:
            self.habits[name]["completed"] = True
            self._save_data()
            return f"Boa! Você concluiu: {name}"
        return "Erro: Hábito não encontrado."

if __name__ == "__main__":
    # Apenas para teste manual rápido se quiser rodar o arquivo
    tracker = HabitTracker()
    print(tracker.add_habit("Beber água"))