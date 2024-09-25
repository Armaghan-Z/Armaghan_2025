---
layout: base
title: Student Home 
description: Home Page
hide: true
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
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
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
  <title>Armaghan's World</title>
  <style>
    /* Style for the navigation bar */
    .navbar {
      width: 100%;
      background-color: #000;
      overflow: hidden;
    }
    .navbar a {
      float: left;
      display: block;
      color: #f2f2f2;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
      font-size: 17px;
    }
    .navbar a:hover {
      background-color: #ddd;
      color: black;
    }
    body {
      margin: 0;
      padding-top: 50px; /* Adjust to the height of the navbar */
      background: white;  /* Change this to white */
      color: black;  /* Update text color to black for readability */
      font-family: 'Segoe UI', sans-serif;
    }
    canvas {
      border: 1px solid white;
      background-color: black; /* Set background to black */
      display: block; /* Make canvas block element */
      margin: 0 auto; /* Center the canvas */
    }
    h1, h2 {
      text-align: center;
      color: #e4002b;
    }
    p {
      text-align: center;
      font-size: 18px;
      margin: 0 20px;
    }
    hr {
      border: 0;
      height: 1px;
      background: #f2f2f2;
      margin: 20px 0;
    }
    .bio-section {
      padding: 20px;
      text-align: center;
    }
    .bio-section img {
      border-radius: 50%;
      width: 300px;
      height: 450px;
    }
    .social-links {
      margin-top: 20px;
    }
    .social-links a {
      margin: 0 10px;
      color: white;
      text-decoration: none;
    }
    /* Keyframes for running animation */
    @keyframes run-across {
      0% {
        transform: translateX(-1000px); /* Start off the left edge of the viewport */
      }
      100% {
        transform: translateX(calc(150vw + 100px)); /* End just off the right edge of the viewport */
      }
    }
    /* Style for Mario */
    #running-mario {
      position: fixed;
      bottom: 50px; /* Distance from the bottom of the screen */
      width: 25px;
      height: 50px;
      animation: run-across 6s linear infinite; /* Adjust '6s' for speed */
    }
    /* Center the image */
    .centered-image {
      display: block;
      margin-left: auto;
      margin-right: auto;
      width: 50%;
    }
  </style>
</head>
<body>

<!-- Main content -->
<h1>Welcome to Armaghan's World 😎</h1>

<hr>

<!-- About Me Section -->
<img src="/Armaghan_2025/assets/Images/Italian-River.jpeg" class="centered-image">

<div class="bio-section">
  <h2>Hello, I'm Armaghan Zarak</h2>
  <p>A passionate coder, athlete, and lifelong learner.</p>
  <p>From crafting clean code to getting baskets on the court, I thrive on challenge and creativity. This site is a blend of my interests, including projects, thoughts, and things I love to do. Feel free to explore!</p>
</div>

<h2>Here is some of my notebooks!</h2>
<a href="/Armaghan_2025/jupyter/Emoji-print" target="_blank">
  <button style="padding: 10px 20px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
    Go to Emoji Jupyter Notebook
  </button>
</a>
<a href="/Armaghan_2025/jupyter/Frontend" target="_blank">
  <button style="padding: 10px 20px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
    Go to Frontend Jupyter Notebook
  </button>
</a>
<a href="/Armaghan_2025/attempted_vs_accomplished/" target="_blank">
  <button style="padding: 10px 20px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
    Go to Attemptec vs. Accomplished 1 Notebook
  </button>
</a>

<h2> My Favorite Spotify Playlist 🎶</h2>

<p>Here’s a Spotify playlist that I love listening to while working or just in General 😄:</p>

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/0QkxqzssAhq5tHPKsfNDho?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

<hr>
<h2>Fun Game</h2>
<p> - Right below this is a game that I sourced from GitHub. I used HTML and markdown ideology to edit the color and movement speed of the snake. You are able to control using the up, down, left, and right arrow keys.</p>

<!-- Snake Game -->
<div style="text-align: center;"> <!-- Center the canvas -->
  <canvas width="400" height="400" id="game"></canvas>
</div>
<h2 id="score">Score: 0</h2>
<h2 id="game-over" style="display:none; color:red; text-align:center;">Game Over! Press Enter to Restart</h2>

<script>
var canvas = document.getElementById('game');
var context = canvas.getContext('2d');
var grid = 16;
var count = 0;
var score = 0;
var gamePaused = false;

var snake = {
  x: 160,
  y: 160,
  dx: grid,
  dy: 0,
  cells: [],
  maxCells: 4
};

var apple = {
  x: 320,
  y: 320
};

var powerUp = {
  x: getRandomInt(0, 25) * grid,
  y: getRandomInt(0, 25) * grid,
  active: false
};

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function loop() {
  if (gamePaused) {
    return; // Pause the game loop if the game is over
  }

  requestAnimationFrame(loop);

  if (++count < 4) {
    return;
  }
  count = 0;

  // Clear the canvas
  context.clearRect(0, 0, canvas.width, canvas.height);

  // Move the snake
  snake.x += snake.dx;
  snake.y += snake.dy;

  // Wrap the snake around the edges
  if (snake.x < 0) {
    snake.x = canvas.width - grid;
  } else if (snake.x >= canvas.width) {
    snake.x = 0;
  }
  if (snake.y < 0) {
    snake.y = canvas.height - grid;
  } else if (snake.y >= canvas.height) {
    snake.y = 0;
  }

  // Keep track of the snake's cells
  snake.cells.unshift({ x: snake.x, y: snake.y });
  if (snake.cells.length > snake.maxCells) {
    snake.cells.pop();
  }

  // Draw the apple
  context.fillStyle = 'red';
  context.fillRect(apple.x, apple.y, grid - 1, grid - 1);

  // Draw the power-up if active
  if (powerUp.active) {
    context.fillStyle = 'blue';
    context.fillRect(powerUp.x, powerUp.y, grid - 1, grid - 1);
  }

  // Draw the snake
  context.fillStyle = 'green';
  snake.cells.forEach(function (cell, index) {
    context.fillRect(cell.x, cell.y, grid - 1, grid - 1);

    // Check if the snake eats the apple
    if (cell.x === apple.x && cell.y === apple.y) {
      snake.maxCells++;
      score += 10; // Increase score
      document.getElementById('score').innerText = 'Score: ' + score;

      // Randomly activate a power-up
      if (Math.random() < 0.2) {
        powerUp.active = true;
        powerUp.x = getRandomInt(0, 25) * grid;
        powerUp.y = getRandomInt(0, 25) * grid;
      }

      apple.x = getRandomInt(0, 25) * grid;
      apple.y = getRandomInt(0, 25) * grid;
    }

    // Check if the snake eats the power-up
    if (powerUp.active && cell.x === powerUp.x && cell.y === powerUp.y) {
      powerUp.active = false;
      snake.maxCells += 3; // Add 3 segments to the snake
      score += 50; // Extra points
      document.getElementById('score').innerText = 'Score: ' + score;
    }

    // Check for snake collision with itself
    for (var i = index + 1; i < snake.cells.length; i++) {
      if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
        gamePaused = true; // Pause the game
        document.getElementById('game-over').style.display = 'block';
        document.getElementById('score').style.display = 'none';
      }
    }
  });
}

function resetGame() {
  snake.x = 160;
  snake.y = 160;
  snake.dx = grid;
  snake.dy = 0;
  snake.cells = [];
  snake.maxCells = 4;
  
  apple.x = getRandomInt(0, 25) * grid;
  apple.y = getRandomInt(0, 25) * grid;

  score = 0;
  document.getElementById('score').innerText = 'Score: ' + score;
  document.getElementById('score').style.display = 'block';
  document.getElementById('game-over').style.display = 'none';
  
  gamePaused = false; // Unpause the game

  requestAnimationFrame(loop); // Ensure game loop starts again
}

// Restart game on Enter key press
document.addEventListener('keydown', function(e) {
  // Prevent the default behavior for arrow keys
  if ([37, 38, 39, 40].indexOf(e.which) > -1) {
    e.preventDefault();
  }

  if (e.which === 13 && gamePaused) {
    resetGame(); // Restart game when Enter is pressed
  }

  // Snake movement controls
  if (e.which === 37 && snake.dx === 0) {
    snake.dx = -grid;
    snake.dy = 0;
  } else if (e.which === 38 && snake.dy === 0) {
    snake.dy = -grid;
    snake.dx = 0;
  } else if (e.which === 39 && snake.dx === 0) {
    snake.dx = grid;
    snake.dy = 0;
  } else if (e.which === 40 && snake.dy === 0) {
    snake.dy = grid;
    snake.dx = 0;
  }
});
requestAnimationFrame(loop);
</script>

<!-- Mario GIF -->
<img id="running-mario" src="/Armaghan_2025/assets/Images/mario-8bit-unscreen.gif">

</body>
</html>

<script src="https://utteranc.es/client.js"
        repo="Armaghan-z/Armaghan_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
