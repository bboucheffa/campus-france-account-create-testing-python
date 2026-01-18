Feature: CreationCompteCampusFrance
En tant qu’utilisateur, je souhaite créer un compte sur Campus France selon trois types :
étudiant, chercheur ou institutionnel. Je dois également tester le placeholder,
notamment le texte affiché sur le bouton de création : « CRÉER UN COMPTE ».

Background:
    Given Je suis sur la page de creation de compte campus france

    Scenario: Verification de creation de compte en tant qu Etudiant
	    When je renseigne les champs avec un profil etudiant et je coche la case des conditions
        Then le texte dans le bouton creer est CREER UN COMPTE

