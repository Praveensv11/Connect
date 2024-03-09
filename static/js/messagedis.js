document.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelectorAll('.text-warning');

    messages.forEach(message => {
        setTimeout(() => {
            message.style.display = 'none'; 
        }, 4000); 
    });
});
