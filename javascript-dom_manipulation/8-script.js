fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const helloTranslation = data.hello;
    document.getElementById('hello').textContent = helloTranslation;
  })
  .catch(error => {
    console.error('Fetch failed', error);
  });
  