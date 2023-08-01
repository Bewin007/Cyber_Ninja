// renderer.js

document.addEventListener('DOMContentLoaded', () => {
  const getDataButton = document.getElementById('getDataButton');
  const dataContainer = document.getElementById('dataContainer');

  getDataButton.addEventListener('click', () => {
    // Prepare the data you want to send in the POST request
    const requestData = {
      key: 'value', // Replace this with your actual data
    };

    // Make the fetch POST request
    fetch('http://127.0.0.1:8000/binwalk/', {
      method: 'POST', // Specify the HTTP method as POST
      headers: {
        'Content-Type': 'application/json', // Set the content type to JSON
      },
      body: JSON.stringify(requestData), // Convert the data to JSON and send in the request body
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        // Display the fetched data in the container
        dataContainer.innerText = JSON.stringify(data, null, 2);
      })
      .catch(error => {
        console.error('Error:', error);
        dataContainer.innerText = 'Error fetching data';
      });
  });
});
