document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("registerForm");

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        const name = document.getElementById("name").value;
        const sobrenome = document.getElementById("sobrenome").value;
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirmPassword").value;

        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }

        const data = {
            name: name,
            sobrenome: sobrenome,
            username: username,
            password: password
        };

        fetch("register.html", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok " + response.statusText);
            }
            return response.text().then(text => {
                return text ? JSON.parse(text) : {};
            });
        })
        .then(data => {
            console.log("Success:", data);
            alert("Registration successful!");
            form.reset();
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("Registration failed. " + error.message);
        });
    });
});
