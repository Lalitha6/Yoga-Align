document.addEventListener('DOMContentLoaded', function() {
    const toggleForms = document.querySelectorAll('.toggle-form');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    toggleForms.forEach(button => {
        button.addEventListener('click', function() {
            if (loginForm.style.display === 'none') {
                loginForm.style.display = 'block';
                signupForm.style.display = 'none';
            } else {
                loginForm.style.display = 'none';
                signupForm.style.display = 'block';
            }
        });
    });
});