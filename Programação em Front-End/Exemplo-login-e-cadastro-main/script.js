document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const storedUser = localStorage.getItem(username);
    const userData = storedUser ? JSON.parse(storedUser) : {};

    if (userData.password === password) {
        alert('Login bem-sucedido!');
        // Aqui, redirecione para a página principal do sistema ou mostre informações do usuário
    } else {
        alert('Usuário ou senha incorretos!');
    }
});
