document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit').disabled = true;

    document.querySelector('#noempty').onkeyup = () => {
        if (document.querySelector('#noempty').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
    };
});
