---
layout: page
title: About Armaghan Zarak 😎 
permalink: /about/
---


<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.dropbtn {
  background-color: #087950;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}
.dropbtn:hover, .dropbtn:focus {
  background-color: #006400;
}
.dropdown {
  position: relative;
  display: inline-block;
}
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  overflow: auto;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}
.dropdown a:hover {background-color: #ddd;}
.show {display: block;}
</style>
</head>
<body style="background-color:white;">

<div class="dropdown">
  <button onclick="myFunction()" class="dropbtn">Dropdown</button>
  <div id="myDropdown" class="dropdown-content">
    <a href="/Armaghan_2025/about/">About me</a>
    <a href="/Armaghan_2025/Calculator/">Calculator</a>
    <a href="/Armaghan_2025/F1/">Formula 1</a>
    <a href="/Armaghan_2025/Journal/">My Journal</a>
    <a href="/Armaghan_2025/">My Home Page</a>
    <a href="/Armaghan_2025/Cookie_Clicker/">Cookie Clicker</a>

  </div>
</div>

<script>
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
</script>

</body>
</html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Popup Example</title>
    <style>
        /* Styles for the modal */
        .modal {
            display: none; /* Hidden by default */
            position: fixed; /* Stay in place */
            z-index: 1; /* Sit on top */
            left: 0;
            top: 0;
            width: 100%; /* Full width */
            height: 100%; /* Full height */
            overflow: auto; /* Enable scroll if needed */
            background-color: rgb(0,0,0); /* Fallback color */
            background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
        }
        .modal-content {
            background-color: #fefefe;
            margin: 15% auto; /* 15% from the top and centered */
            padding: 20px;
            border: 1px solid #888;
            width: 80%; /* Could be more or less, depending on screen size */
        }
        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }
        .close:hover,
        .close:focus {
            color: black;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="myModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <p>If you hear something weird, such as trailers or many trailers playing at once, please refresh your page. I am still tryinng to figure it out 😁.</p>
            <label>
                <input type="checkbox" id="dontAskAgain"> Don't ask again
            </label>
            <br><br>
            <button id="okButton">OK</button>
        </div>
    </div>
    <script>
        // Check if the user has previously chosen "Don't ask again"
        if (!localStorage.getItem('dontAskAgain')) {
            document.getElementById('myModal').style.display = 'block';
        }
        // Get the button that closes the modal
        var span = document.getElementsByClassName("close")[0];
        var okButton = document.getElementById('okButton');
        var dontAskAgainCheckbox = document.getElementById('dontAskAgain');
        // When the user clicks on the close button, close the modal
        span.onclick = function() {
            document.getElementById('myModal').style.display = 'none';
        }
        // When the user clicks OK, close the modal and save the choice if checked
        okButton.onclick = function() {
            if (dontAskAgainCheckbox.checked) {
                localStorage.setItem('dontAskAgain', 'true');
            }
            document.getElementById('myModal').style.display = 'none';
        }
        // Close the modal if the user clicks outside of it
        window.onclick = function(event) {
            if (event.target == document.getElementById('myModal')) {
                document.getElementById('myModal').style.display = 'none';
            }
        }
    </script>
</body>
</html>

## About Me
<div>
<p>Hello! My name is Armaghan Zarak, and I have a diverse background when it comes to places I’ve called home. I was born in California, specifically in the Bay Area, where I spent my first two years in San Jose. After that, I moved to Dallas, Texas, and lived there for seven years, which gave me a unique perspective on life in both states. For the past seven years, I’ve been back in California, and it feels great to be home again! </p>

<p>Below is the California state flag to represent where my journey began and where I’ve spent most of my life: </p>
</div>
<img src="/Armaghan_2025/assets/Images/Flag_of_California.svg" width= 200px height=150px>
<img src="/Armaghan_2025/assets/Images/StateofTexasFlag_2048x.webp" width= 200px height=200px>

## Sports and Hobbies

I’m a huge sports fan! I love playing basketball, soccer, and American football. When I’m not on the field or court, I enjoy traveling and discovering new, beautiful places around the world. Recently, I had the chance to visit Cappadocia, Turkey, where I experienced an amazing hot air balloon littered sunrise. Here’s a glimpse of that trip:

<img src="/Armaghan_2025/assets/Images/Picture1.jpeg" alt="Hot air balloons littering the Sunrise" width="400px" height="500px"/>
    
## Goals for This Year

This year, my primary focus is on improving my coding skills. I want to become proficient enough to create my own website from scratch and master the basics of various coding languages.

## Previous Experience

Though I’ve taken a short, 2-day coding course outside of school, I am still quite new to the world of programming. This year, I’m dedicated to changing that!

## Interests

Geography is a subject I find fascinating, and I’m always eager to learn more about different places. When I have some downtime, I enjoy playing video games with friends, and of course, playing sports with them is always a great way to stay active.

## Interactive Quiz

<div class="quiz-container">
    <h2>Country Quiz</h2>
    <div id="quiz">
        <div class="question" id="question"></div>
        <div class="answers" id="answers"></div>
        <div class="result" id="result"></div>
    </div>
</div>

<script>
    const quizData = [
        {
            question: "Where is France located?",
            options: ["Europe", "Asia", "Africa", "South America"],
            answer: "Europe"
        },
        {
            question: "Which continent is Australia part of?",
            options: ["Asia", "Europe", "Oceania", "North America"],
            answer: "Oceania"
        },
        {
            question: "Where is Brazil located?",
            options: ["South America", "North America", "Europe", "Africa"],
            answer: "South America"
        },
        {
            question: "Which continent is Egypt part of?",
            options: ["Asia", "Africa", "Europe", "South America"],
            answer: "Africa"
        },
        {
            question: "Where is Japan located?",
            options: ["Europe", "Asia", "Oceania", "South America"],
            answer: "Asia"
        }
    ];

    let currentQuestion = 0;
    let score = 0;

    function loadQuestion() {
        if (currentQuestion < quizData.length) {
            const questionData = quizData[currentQuestion];
            document.getElementById("question").innerText = questionData.question;
            const answersContainer = document.getElementById("answers");
            answersContainer.innerHTML = "";
            questionData.options.forEach(option => {
                const button = document.createElement("button");
                button.innerText = option;
                button.onclick = () => selectAnswer(button, option);
                answersContainer.appendChild(button);
            });
        } else {
            showResult();
        }
    }

    function selectAnswer(button, selectedOption) {
        const questionData = quizData[currentQuestion];
        if (selectedOption === questionData.answer) {
            button.classList.add("correct");
            score++;
        } else {
            button.classList.add("wrong");
        }

        const buttons = document.querySelectorAll(".answers button");
        buttons.forEach(btn => btn.disabled = true);

        setTimeout(() => {
            currentQuestion++;
            loadQuestion();
        }, 1000);
    }

    function showResult() {
        document.getElementById("quiz").innerHTML = `
            <div class="result">
                You got ${score} out of ${quizData.length} correct!
            </div>
        `;
    }

    loadQuestion();
</script>

<h3>This is Tyreek Hill's stats</h3>
<p>As a Miami Dolphins fan, I closely follow Tyreek Hill, who is currently one of the top-rated players in the NFL. You can check out his ESPN stats here:</p>

<a href="https://espn.com/nfl/player/_/id/3116406/tyreek-hill" class="button" target="_blank">
 Tyreek Hill
</a>

## Image Gallery

Here’s a small collection of some images that represent my life and interests:

<div class="gallery-container">
  <div class="gallery">
    <img src="/Armaghan_2025/assets/Images/Chamanoix-View.jpeg" alt="Chamanoix View">
    <img src="/Armaghan_2025/assets/Images/IMG_0282.jpeg" alt="Image 0282">
    <img src="/Armaghan_2025/assets/Images/IMG_7755.jpeg" alt="Image 7755">
    <img src="/Armaghan_2025/assets/Images/IMG_7828.jpeg" alt="Image 7828">

  </div>
</div>

<style>
    .quiz-container {
        max-width: 600px;
        margin: auto;
        background-color: #34495e;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .question {
        font-size: 18px;
        margin-bottom: 15px;
    }
    .answers button {
        display: block;
        width: 100%;
        margin: 5px 0;
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        border: 1px solid #7f8c8d;
        background-color: #1abc9c;
        color: #fff;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
    }
    .answers button:hover {
        background-color: #16a085;
    }
    .correct {
        background-color: #2ecc71 !important;
        transform: scale(1.05);
    }
    .wrong {
        background-color: #e74c3c !important;
        transform: scale(0.95);
    }
    .result {
        font-size: 20px;
        margin-top: 20px;
    }
    .button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        color: black;
        background-color: #007bff;
        border: none;
        border-radius: 5px;
        text-decoration: none;
        text-align: center;
        cursor: pointer;
    }
    .button:hover {
        background-color: #0056b3;
    }
    .gallery-container {
        max-width: 100%;
        overflow: hidden;
    }
    .gallery {
        display: flex;
        overflow-x: auto;
        padding: 10px;
        background-color: #333;
    }
    .gallery img {
        flex: 0 0 auto;
        margin-right: 10px;
        border-radius: 5px;
        max-height: 400px;
    }
</style>

## Explore the World of APIs
<div id="itunes-results"></div>
<script src="{{ '/assets/js/itunes-api.js' | relative_url }}"></script>

<script src="https://utteranc.es/client.js"
        repo="Armaghan-z/Armaghan_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>



<h1>Access data from our Flask server using JavaScript</h1>

<p>This code extracts data "live" from a local Web Server with JavaScript fetch.  Additionally, it formats the data into a table.</p>

<!-- Head contains information to Support the Document -->


<!-- HTML table fragment for page -->
<table id="demo" class="table">
  <thead>
      <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Residence</th>
      </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>

<script>
  // prepare HTML result container for new output
  let resultContainer = document.getElementById("result");
  
  // prepare URL
  url = "http://127.0.0.1:5001/_notebooks/api/armaghan";

  // set options for cross origin header request
  let options = {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'include', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json',
    },
  };

  // fetch the API
  fetch(url, options)
    // response is a RESTful "promise" on any successful fetch
    .then(response => {
      // check for response errors and display
      if (response.status !== 200) {
          console.error(response.status);
          return;
      }
      // valid response will contain json data
      response.json().then(data => {
          console.log(data);
          for (const row of data) {
            // tr and td build out for each row
            const tr = document.createElement("tr");
            const firstname = document.createElement("td");
            const lastname = document.createElement("td");
            const residence = document.createElement("td");
            // data is specific to the API
            firstname.innerHTML = row.FirstName; 
            lastname.innerHTML = row.LastName; 
            residence.innerHTML = row.Residence; 
            // this builds each td into tr
            tr.appendChild(firstname);
            tr.appendChild(lastname);
            tr.appendChild(residence);
            // add HTML to container
            resultContainer.appendChild(tr);
          }
      })
  })
  
</script>

