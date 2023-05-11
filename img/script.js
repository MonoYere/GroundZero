// Validación de Email
function checkEmail() {
    const emaiPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!emailInput.value.match(emaiPattern)) {
        return emailField.classList.add("invalid"); //Agregar clase invalido si el email no cumple validaciones
    }
    emailField.classList.remove("invalid"); //Remover clase invalido si el email es validado
}