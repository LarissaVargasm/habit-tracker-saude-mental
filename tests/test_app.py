from src.app import HabitTracker
import os

def setup_function():
    """Executa antes de cada teste para limpar o arquivo de teste."""
    if os.path.exists("test_habits.json"):
        os.remove("test_habits.json")

def test_add_habit():
    tracker = HabitTracker(storage_path="test_habits.json")
    result = tracker.add_habit("Beber Água")
    assert "sucesso" in result.lower()
    assert "Beber Água" in tracker.list_habits()

def test_add_duplicate_habit():
    tracker = HabitTracker(storage_path="test_habits.json")
    tracker.add_habit("Meditar")
    result = tracker.add_habit("Meditar")
    assert "Erro" in result

def test_edit_habit():
    tracker = HabitTracker(storage_path="test_habits.json")
    tracker.add_habit("Lavar louça")
    result = tracker.edit_habit("Lavar louça", "Lavar a cozinha")
    assert "alterado" in result
    assert "Lavar a cozinha" in tracker.list_habits()

def test_complete_habit():
    tracker = HabitTracker(storage_path="test_habits.json")
    tracker.add_habit("Exercício")
    tracker.complete_habit("Exercício")
    assert tracker.list_habits()["Exercício"]["completed"] is True