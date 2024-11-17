document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.early-access-form');
    const message = document.createElement('p');
    const waveCoverLeft = document.querySelector('.wave-cover-left');

    message.textContent = "Hang tight! We'll be in touch soon.";
    message.className = 'early-access-message hero-gradient hidden';

    if (form && form.parentElement) {
        form.parentElement.appendChild(message);

        form.addEventListener('submit', function (event) {
            event.preventDefault();

            if (waveCoverLeft) {
                waveCoverLeft.classList.remove('wave-slide-in');
                void waveCoverLeft.offsetWidth;
                waveCoverLeft.classList.add('wave-slide-in');
            }

            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });

            form.classList.add('fade-out');

            setTimeout(() => {
                form.classList.add('hidden');
                message.classList.remove('hidden');
                message.classList.add('fade-in');
            }, 500);
        });
    }
});
