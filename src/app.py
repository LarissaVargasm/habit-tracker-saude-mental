import json
import os

class HabitTracker:
    def __init__(self, filename="habits.json"):
        self.filename = filename
        self.habits = self._load_habits()

    def _load_habits(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        return [h for h in data if isinstance(h, dict)]
                except:
                    return []
        return []

    def _save_habits(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.habits, f, indent=4)

    def add_habit(self, name):
        nome_limpo = name.strip()
        if nome_limpo and not any(h.get('name') == nome_limpo for h in self.habits):
            self.habits.append({"name": nome_limpo, "completed": False})
            self._save_habits()

    def list_habits(self):
        return self.habits

    def complete_habit(self, name):
        nome_busca = name.strip()
        for h in self.habits:
            if h.get('name') == nome_busca:
                h['completed'] = True
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
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do hábito: ").strip()
            if nome:
                tracker.add_habit(nome)
                print(f"✅ Hábito '{nome}' adicionado!")
        
        elif opcao == "2":
            habitos = tracker.list_habits()
            print("\n📋 Seus Hábitos:")
            if not habitos:
                print("📭 Nenhum hábito encontrado.")
            else:
                for h in habitos:
                    nome_h = h.get('name', 'Hábito sem nome')
                    status = "✅" if h.get('completed') else "❌"
                    print(f"- {nome_h} [{status}]")
        
        elif opcao == "3":
            nome = input("Nome do hábito para concluir: ").strip()
            if tracker.complete_habit(nome):
                print(f"🌟 Parabéns por cuidar de você! '{nome}' concluído.")
            else:
                print(f"⚠️ Hábito '{nome}' não encontrado.")
            
        elif opcao == "4":
            print("Até logo! Cuide-se bem. ✨")
            break