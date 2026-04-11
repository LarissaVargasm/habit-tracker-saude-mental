import json
import os

class HabitTracker:
    def __init__(self, storage_path="habits.json"):
        self.storage_path = storage_path
        self.habits = self._load_habits()

    def _load_habits(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    return data if isinstance(data, dict) else {}
                except:
                    return {}
        return {}

    def _save_habits(self):
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.habits, f, indent=4)

    def add_habit(self, name):
        if not name:
            return "Erro: nome vazio"
        if name in self.habits:
            return "Erro: hábito já existe"
        
        self.habits[name] = {"completed": False}
        self._save_habits()
        return "Sucesso: hábito adicionado"

    def edit_habit(self, old_name, new_name):
        if old_name in self.habits and new_name:
            self.habits[new_name] = self.habits.pop(old_name)
            self._save_habits()
            return "Sucesso: hábito alterado"
        return "Erro: falha ao editar"

    def list_habits(self):
        return self.habits

    def complete_habit(self, name):
        if name in self.habits:
            self.habits[name]["completed"] = True
            self._save_habits()
            return True
        return False

if __name__ == "__main__":
    tracker = HabitTracker()
    while True:
        print("\n🌿 --- HabitTracker: Saúde Mental --- 🌿")
        print("1. Adicionar Hábito")
        print("2. Listar Hábitos")
        print("3. Concluir Hábito")
        print("4. Editar Hábito")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do hábito: ").strip()
            print(tracker.add_habit(nome))
        
        elif opcao == "2":
            habitos = tracker.list_habits()
            print("\n📋 Seus Hábitos:")
            if not habitos:
                print("📭 Nenhum hábito encontrado.")
            for nome, info in habitos.items():
                status = "✅" if info["completed"] else "❌"
                print(f"- {nome} [{status}]")
        
        elif opcao == "3":
            nome = input("Nome do hábito para concluir: ").strip()
            if tracker.complete_habit(nome):
                print("🌟 Parabéns por cuidar de você!")
            else:
                print("⚠️ Hábito não encontrado.")

        elif opcao == "4":
            velho = input("Nome atual: ").strip()
            novo = input("Novo nome: ").strip()
            print(tracker.edit_habit(velho, novo))
            
        elif opcao == "5":
            print("Até logo! ✨")
            break