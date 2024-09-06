---
layout: base
title: Student Home 
description: Home Page
hide: true
---

<html lang="en">
<head>
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
    background: black;
    color: white;
    font-family: 'Segoe UI', sans-serif;
  }
  canvas {
    border: 1px solid white;
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
    width: 150px;
  }
  .social-links {
    margin-top: 20px;
  }
  .social-links a {
    margin: 0 10px;
    color: white;
    text-decoration: none;
  }
</style>
</head>

<body>

<!-- Main content -->
<h1>Welcome to Armaghan's World 😎</h1>
<hr>

<!-- About Me Section -->
<div class="bio-section">
  <img src="/Armaghan_2025/assets/images/Me-in-Italy.jpeg" alt="Armaghan Zarak">
  <h2>Hello, I'm Armaghan Zarak</h2>
  <p>A passionate coder, athlete, and lifelong learner.</p>
  <p>From crafting clean code to scoring goals on the field, I thrive on challenge and creativity. This site is a blend of my interests, including projects, thoughts, and things I love to do. Feel free to explore!</p>
  

<hr>
<h2>Fun Game</h2>
<p> - Right below this is a game that I sourced from GitHub. I used HTML and markdown ideology to edit the color and movement speed of the snake. You are able to control using the up, down, left, and right arrow keys.</p>

<!-- Snake Game -->
<canvas width="400" height="400" id="game"></canvas>
<script>
var canvas = document.getElementById('game');
var context = canvas.getContext('2d');
var grid = 16;
var count = 0;
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
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}
function loop() {
  requestAnimationFrame(loop);
  if (++count < 4) {
    return;
  }
  count = 0;
  context.clearRect(0,0,canvas.width,canvas.height);
  snake.x += snake.dx;
  snake.y += snake.dy;
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
  snake.cells.unshift({x: snake.x, y: snake.y});
  if (snake.cells.length > snake.maxCells) {
    snake.cells.pop();
  }
  context.fillStyle = 'red';
  context.fillRect(apple.x, apple.y, grid-1, grid-1);
  context.fillStyle = 'green';
  snake.cells.forEach(function(cell, index) {
    context.fillRect(cell.x, cell.y, grid-1, grid-1);  
    if (cell.x === apple.x && cell.y === apple.y) {
      snake.maxCells++;
      apple.x = getRandomInt(0, 25) * grid;
      apple.y = getRandomInt(0, 25) * grid;
    }
    for (var i = index + 1; i < snake.cells.length; i++) {
      if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
        snake.x = 160;
        snake.y = 160;
        snake.cells = [];
        snake.maxCells = 4;
        snake.dx = grid;
        snake.dy = 0;
        apple.x = getRandomInt(0, 25) * grid;
        apple.y = getRandomInt(0, 25) * grid;
      }
    }
  });
}
document.addEventListener('keydown', function(e) {
  // Prevent default behavior of arrow keys to stop page scrolling
  if ([37, 38, 39, 40].includes(e.which)) {
    e.preventDefault();
  }
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



<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Running Mario</title>
  <style>
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
  </style>
</head>
<body>

  <!-- Mario GIF -->
  <img id="running-mario" src="/Armaghan_2025/assets/images/mario-8bit-unscreen.gif" alt="Running Mario">

</body>
</html>