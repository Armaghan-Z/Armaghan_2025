const searchTerm = "movie"; // Broad term for movies
const apiUrl = `https://itunes.apple.com/search?term=${searchTerm}&media=movie&limit=10`;

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const resultsContainer = document.getElementById('itunes-results');
    resultsContainer.innerHTML = ""; // Clear previous results

    data.results.forEach(item => {
      // Check for valid preview URL
      if (item.previewUrl) {
        const videoContainer = document.createElement('div');
        videoContainer.style.marginBottom = "20px";

        const title = document.createElement('h3');
        title.textContent = item.trackName;
        videoContainer.appendChild(title);

        const iframe = document.createElement('iframe');
        iframe.src = item.previewUrl;
        iframe.width = "300";
        iframe.height = "200";
        iframe.allow = "autoplay; encrypted-media; fullscreen"; // Allow fullscreen
        iframe.frameBorder = "0";

        videoContainer.appendChild(iframe);
        resultsContainer.appendChild(videoContainer);
      }
    });
  })
  .catch(error => console.error('Error fetching data:', error));