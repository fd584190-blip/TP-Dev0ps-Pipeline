from app import addition

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    print("Tous les tests ont réussi !")
