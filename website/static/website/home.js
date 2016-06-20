function clic() {
    var pElt = document.getElementById("bouton2");
    compteur += 1;
    if (compteur % 2 === 0){
		pElt.style.backgroundColor = "pink";
    }
    else{
    	pElt.style.backgroundColor = "green";
    }
	
}

var compteur = 0;

var boutonElt = document.getElementById("bouton2");
// Ajout d'un gestionnaire pour l'événement click
boutonElt.addEventListener("click", clic);

