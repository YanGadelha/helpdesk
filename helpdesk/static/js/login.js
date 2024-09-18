function toggleForms() {
    var loginForm = document.getElementById('login-form');
    var registerForm = document.getElementById('register-form');
    var formTitle = document.getElementById('form-title');
    var toggleText = document.getElementById('toggle-form');

    if (loginForm.classList.contains('d-none')) {
        loginForm.classList.remove('d-none');
        registerForm.classList.add('d-none');
        formTitle.innerText = 'Login';
        toggleText.innerHTML = 'Não possui uma conta? <a href="#" onclick="toggleForms()">Clique aqui</a>';
    } else {
        loginForm.classList.add('d-none');
        registerForm.classList.remove('d-none');
        formTitle.innerText = 'Criar Conta';
        toggleText.innerHTML = 'Já possui uma conta? <a href="#" onclick="toggleForms()">Clique aqui</a>';
    }
}

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    window.location.href = '/home';
});