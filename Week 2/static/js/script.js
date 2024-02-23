document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('promptForm');
    const button = form.querySelector('button[type="submit"]');
    const spinner = button.querySelector('.spinner-border');

    form.addEventListener('submit', function() {
        button.childNodes[0].nodeValue = "Loading... ";
        spinner.style.display = 'inline-block'; // Show spinner
        button.disabled = true; // Disable button to prevent multiple submissions
    });
});

