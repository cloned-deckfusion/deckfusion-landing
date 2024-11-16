document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.early-access-form');
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
            form.classList.add('fade-out');

            setTimeout(() => {
                form.classList.add('hidden');
            }, 500);
        });
    }
});
