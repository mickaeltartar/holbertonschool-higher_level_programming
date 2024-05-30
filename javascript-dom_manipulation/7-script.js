fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const movies = data.results;
    const ulElement = document.getElementById('list_movies');
    movies.forEach(movie => {
      const title = movie.title;
      const liElement = document.createElement('li');
      liElement.textContent = title;
      ulElement.appendChild(liElement);
    });
  })
  .catch(error => {
    console.error('Fetch failed', error);
  });
  