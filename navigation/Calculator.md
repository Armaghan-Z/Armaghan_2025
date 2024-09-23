---
layout: page
title: My Handy calculator
permalink: /Calculator/
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

<html lang='en'>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Javascript Calculator</title>
  <meta name="description" content="A common way to become familiar with a language is to build a calculator. This calculator shows off button with actions." />

  <!-- Include CSS for styling -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Primer/15.2.0/primer.css" integrity="sha512-xTz2ys4coGAOz8vuV1NcQBkgVmKhsSEtjbqyMJbBHRplFuvKIUo6xhLHpAyPt9mfR6twHJgn9OgVLuqOvjeBhg==" crossorigin="anonymous" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==" crossorigin="anonymous" />

  <style>
    .calculator-output {
      grid-column: span 4;
      grid-row: span 1;
      border-radius: 10px;
      padding: 0.25em;
      font-size: 20px;
      border: 5px solid white;
      display: flex;
      align-items: center;
      color: white;
    }
    canvas {
      filter: none;
    }
    .calculator-container {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-gap: 10px;
      padding: 10px;
    }
    .calculator-number, .calculator-operation, .calculator-clear, .calculator-equals {
      border-radius: 5px;
      padding: 20px;
      font-size: 18px;
      text-align: center;
      background-color: #eee;
      border: 1px solid #ccc;
      cursor: pointer;
    }
  </style>
</head>

<body>

  <main class="page-content" aria-label="Content">
    <div class="wrapper">
      <article class="post">
       <u> <h1>Javascript Calculator</h1> </u>
        <div id="animation">
          <div class="calculator-container">
            <div class="calculator-output" id="output">0</div>
            <div class="calculator-number">1</div>
            <div class="calculator-number">2</div>
            <div class="calculator-number">3</div>
            <div class="calculator-operation">+</div>
            <div class="calculator-number">4</div>
            <div class="calculator-number">5</div>
            <div class="calculator-number">6</div>
            <div class="calculator-operation">-</div>
            <div class="calculator-number">7</div>
            <div class="calculator-number">8</div>
            <div class="calculator-number">9</div>
            <div class="calculator-operation">*</div>
            <div class="calculator-clear">A/C</div>
            <div class="calculator-number">0</div>
            <div class="calculator-number">.</div>
            <div class="calculator-equals">=</div>
          </div>
        </div>
        <!-- JavaScript -->
        <script>
          var firstNumber = null;
          var operator = null;
          var nextReady = true;
          const output = document.getElementById("output");
          const numbers = document.querySelectorAll(".calculator-number");
          const operations = document.querySelectorAll(".calculator-operation");
          const clear = document.querySelectorAll(".calculator-clear");
          const equals = document.querySelectorAll(".calculator-equals");
          numbers.forEach(button => {
            button.addEventListener("click", function() {
              number(button.textContent);
            });
          });
          function number(value) {
            if (value != ".") {
              if (nextReady) {
                output.innerHTML = value;
                if (value != "0") {
                  nextReady = false;
                }
              } else {
                output.innerHTML += value;
              }
            } else {
              if (output.innerHTML.indexOf(".") == -1) {
                output.innerHTML += value;
                nextReady = false;
              }
            }
          }
          operations.forEach(button => {
            button.addEventListener("click", function() {
              operation(button.textContent);
            });
          });
          function operation(choice) {
            if (firstNumber == null) {
              firstNumber = parseFloat(output.innerHTML);
              nextReady = true;
              operator = choice;
              return;
            }
            firstNumber = calculate(firstNumber, parseFloat(output.innerHTML));
            operator = choice;
            output.innerHTML = firstNumber.toString();
            nextReady = true;
          }
          function calculate(first, second) {
            let result = 0;
            switch (operator) {
              case "+":
                result = first + second;
                break;
              case "-":
                result = first - second;
                break;
              case "*":
                result = first * second;
                break;
              case "/":
                result = first / second;
                break;
              default:
                break;
            }
            return result;
          }
          equals.forEach(button => {
            button.addEventListener("click", function() {
              equal();
            });
          });
          function equal() {
            firstNumber = calculate(firstNumber, parseFloat(output.innerHTML));
            output.innerHTML = firstNumber.toString();
            nextReady = true;
          }
          clear.forEach(button => {
            button.addEventListener("click", function() {
              clearCalc();
            });
          });
          function clearCalc() {
            firstNumber = null;
            output.innerHTML = "0";
            nextReady = true;
          }
        </script>
        <!-- Vanta JS for animation -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r119/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/gh/tengbao/vanta@latest/dist/vanta.halo.min.js"></script>
        <script>
          VANTA.HALO({
            el: "#animation",
            mouseControls: true,
            touchControls: true,
            gyroControls: false
          });
        </script>
      </article>
    </div>
  </main>

  <footer class="site-footer">
    <div class="wrapper">
      <p>&copy; 2024 My Handy Calculator</p>
    </div>
  </footer>
</body>
</html>

<script src="https://utteranc.es/client.js"
        repo="Armaghan-z/Armaghan_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>