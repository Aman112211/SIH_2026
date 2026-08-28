document.addEventListener('DOMContentLoaded', () => {
  const voice = document.querySelector('[data-voice]');
  if (voice) voice.addEventListener('click', () => {
    voice.classList.toggle('listening');
    voice.querySelector('strong').textContent = voice.classList.contains('listening') ? 'Listening…' : 'Ask Karigar AI';
    voice.querySelector('small').textContent = voice.classList.contains('listening') ? 'Demo transcript: “This is a Kondapalli horse…”' : 'Tap to speak · Demo transcript ready';
  });
  const intervention = document.querySelector('[data-intervention]');
  if (intervention) intervention.addEventListener('click', () => {
    intervention.textContent = '✓ Plan ready for officer review';
    intervention.style.background = '#177c72';
  });
});
