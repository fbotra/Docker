import pytest  # Importation du module pytest pour les tests unitaires
from routes.main_routes import validate_email  # Importation de la fonction validate_email depuis le module main_routes

# Expression régulière pour valider une adresse e-mail
emailRegex = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Définition d'une expression régulière pour la validation des adresses e-mail

@pytest.mark.parametrize("email, expected_result", [
    # Jeux de données de test avec des adresses e-mail valides et invalides
    ("user@example.com", True),  # Adresse e-mail valide
    ("user.name@example.com", True),  # Adresse e-mail valide avec un point dans le nom
    ("user123@example.com", True),  # Adresse e-mail valide avec des chiffres
    ("invalid_email", False),  # Adresse e-mail invalide sans le symbole '@'
    ("   ", False),  # Chaîne vide (ou espace) considérée comme invalide
])
def test_validate_email(email, expected_result):
    """
    Test unitaire pour la fonction validate_email.

    Args:
        email (str): Adresse e-mail à tester.
        expected_result (bool): Résultat attendu de la validation.
    """
    # Act
    result = validate_email(email)  # Appel de la fonction validate_email avec l'adresse e-mail de test

    # Assert
    assert result == expected_result  # Vérification que le résultat de la fonction correspond au résultat attendu