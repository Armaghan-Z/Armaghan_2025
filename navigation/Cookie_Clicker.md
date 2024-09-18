---
layout: page
title: Cookie Clicker 9000 🍪
permalink: /Cookie_Clicker/
---

<style>
  body {
    text-align: center;
    font-family: Arial, sans-serif;
  }
  #cookie {
    width: 150px;
    cursor: pointer;
    margin: 20px;
  }
  #score {
    font-size: 24px;
  }
  #shop {
    margin-top: 20px;
  }
  .shop-item {
    margin: 10px;
    border: 1px solid black;
    padding: 10px;
    cursor: pointer;
  }
</style>

<h1>Cookie Clicker Game</h1>

<!-- Cookie Image -->
<img id="cookie" src="/Armaghan_2025/assets/Images/png-clipart-cookie-clicker-clicker-heroes-incremental-game-cookie-game-baked-goods-thumbnail-removebg-preview.png" alt="Cookie" />   

<!-- Score Display -->
<p id="score">Cookies: 0</p>

<!-- Shop Section -->
<div id="shop">
  <h2>Shop</h2>
  <div class="shop-item" id="worker">Buy Worker (Cost: 10 Cookies)</div>
  <div class="shop-item" id="click-upgrade">Click Upgrade (Cost: 20 Cookies)</div>
  <div class="shop-item" id="worker-speed-upgrade">Worker Speed Upgrade (Cost: 30 Cookies)</div>
</div>

<!-- Audio for Click Sound -->
<audio id="clickSound">
  <source src="/Armaghan_2025/assets/Images/mixkit-eating-crispy-cookies-122.wav" type="audio/wav">
</audio>

<script>
  // JavaScript for Cookie Clicker Game

  let score = 0;
  let cookiesPerSecond = 0;
  let cookiesPerClick = 1;
  let workerCost = 10;
  let clickUpgradeCost = 20;
  let workerSpeedUpgradeCost = 30;
  let workerSpeed = 1000;  // Initial worker speed (1000 ms = 1 second)

  // Update the score display
  function updateScore() {
    document.getElementById('score').innerText = `Cookies: ${score}`;
  }

  // Play click sound
  function playClickSound() {
    const clickSound = document.getElementById('clickSound');
    clickSound.play();
  }

  // Handle cookie click
  document.getElementById('cookie').addEventListener('click', function() {
    score += cookiesPerClick;
    updateScore();
    playClickSound();
  });

  // Shop - Buy a worker
  document.getElementById('worker').addEventListener('click', function() {
    if (score >= workerCost) {
      score -= workerCost;
      cookiesPerSecond += 1;
      workerCost = Math.floor(workerCost * 1.5);  // Increase cost for next worker
      updateScore();
      document.getElementById('worker').innerText = `Buy Worker (Cost: ${workerCost} Cookies)`;
    }
  });

  // Shop - Buy a click upgrade
  document.getElementById('click-upgrade').addEventListener('click', function() {
    if (score >= clickUpgradeCost) {
      score -= clickUpgradeCost;
      cookiesPerClick += 1;  // Increase the number of cookies per click
      clickUpgradeCost = Math.floor(clickUpgradeCost * 2);  // Increase cost for next upgrade
      updateScore();
      document.getElementById('click-upgrade').innerText = `Click Upgrade (Cost: ${clickUpgradeCost} Cookies)`;
    }
  });

  // Shop - Buy a worker speed upgrade
  document.getElementById('worker-speed-upgrade').addEventListener('click', function() {
    if (score >= workerSpeedUpgradeCost) {
      score -= workerSpeedUpgradeCost;
      workerSpeed = Math.max(200, workerSpeed - 10);  // Decrease worker interval, minimum is 200ms
      workerSpeedUpgradeCost = Math.floor(workerSpeedUpgradeCost * 1.5);  // Increase cost for next upgrade
      updateScore();
      document.getElementById('worker-speed-upgrade').innerText = `Worker Speed Upgrade (Cost: ${workerSpeedUpgradeCost} Cookies)`;

      // Reset the interval with the new worker speed
      clearInterval(workerInterval);
      workerInterval = setInterval(function() {
        score += cookiesPerSecond;
        updateScore();
      }, workerSpeed);
    }
  });

  // Add cookies passively for workers
  let workerInterval = setInterval(function() {
    score += cookiesPerSecond;
    updateScore();
  }, workerSpeed);  // Initially 1000ms

  // Listen for Control + Z to add 99,999,999 cookies
  document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key === 'z') {
      score += 99999999;
      updateScore();
    }
  });
</script>
