document.addEventListener('DOMContentLoaded', () => {
    const settingsContainer = document.getElementById('settings-container');
    const backendBaseUrl = settingsContainer ? settingsContainer.dataset.backendBaseUrl : null;

    const form = document.querySelector('.early-access-form');
    const message = document.createElement('p');
    const waveCoverLeft = document.querySelector('.wave-cover-left');

    message.textContent = "Hang tight! We'll be in touch soon.";
    message.className = 'early-access-message hero-gradient hidden';

    if (backendBaseUrl && form && form.parentElement) {
        form.parentElement.appendChild(message);

        form.addEventListener('submit', async function (event) {

            event.preventDefault();

            if (waveCoverLeft) {
                waveCoverLeft.classList.remove('wave-slide-in');
                void waveCoverLeft.offsetWidth;
                waveCoverLeft.classList.add('wave-slide-in');
            }

            const emailInput = form.querySelector('input[name="email"]');
            const email = emailInput.value;

            Array.from(form.elements).forEach((element) => {
                element.disabled = true;
            });

            const url = backendBaseUrl + "/api/landing/early-access/"
            const jsonData = JSON.stringify({ email });

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    body: jsonData,
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    }
                });

                if (!response.ok) {
                    throw new Error('Failed to submit data');
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
                }, 100);
            } catch (error) {
                console.error('Error:', error);
                Array.from(form.elements).forEach((element) => {
                    element.disabled = false;
                });
                alert('Something went wrong. Please try again.');
            }
        });
    }
});

function getCSRFToken() {
    const cookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
}
