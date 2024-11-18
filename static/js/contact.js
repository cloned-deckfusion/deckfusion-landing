function handleFormSubmit(event) {
  event.preventDefault();

  const settingsContainer = document.getElementById('settings-container');
  const backendBaseUrl = settingsContainer ? settingsContainer.dataset.backendBaseUrl : null;

  const waveCoverLeft = document.querySelector('.wave-cover-left');
  if (waveCoverLeft) {
      waveCoverLeft.classList.remove('wave-slide-in');
      void waveCoverLeft.offsetWidth;
      waveCoverLeft.classList.add('wave-slide-in');
  }

  const form = document.querySelector('.contact-form');
  const submissionMessage = document.getElementById('submission-message');

  const firstName = form.querySelector('input[name="first_name"]').value;
  const lastName = form.querySelector('input[name="last_name"]').value;
  const email = form.querySelector('input[name="email"]').value;
  const message = form.querySelector('textarea[name="message"]').value;

  const jsonData = {
    first_name: firstName,
    last_name: lastName,
    email: email,
    message: message,
  };

  const url = backendBaseUrl + "/api/landing/contact/"

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken(),
    },
    body: JSON.stringify(jsonData),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(() => {
      form.style.visibility = 'hidden';
      submissionMessage.classList.remove('hidden');
    })
    .catch((error) => {
      console.error('Error:', error);
      alert('Something went wrong. Please try again.');
    });
}

function getCSRFToken() {
  const cookie = document.cookie.split('; ').find((row) => row.startsWith('csrftoken='));
  return cookie ? cookie.split('=')[1] : '';
}
