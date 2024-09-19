---
layout: page
title: Journal
permalink: /Journal/
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
    <a href="/Armaghan_2025/calculator/">Calculator</a>
    <a href="/Armaghan_2025/F1/">Formula 1</a>
    <a href="/Armaghan_2025/Journal/">My Journal</a>
        <a href="/Armaghan_2025/">My Home Page</a>

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

#### Week 0: Setting Up The Foundation
In the first week of my coding journey, my primary focus was on setting up my development environment and ensuring that the `make` tool was functioning correctly. This involved initializing my repository and troubleshooting any issues that arose during setup. It was a crucial step in laying a solid foundation for my project.

#### Weeks 1 & 2: Enhancing Functionality and Adding Features
During the first and second weeks, I dedicated my efforts to enriching the functionality of the website. I successfully incorporated a variety of features, including:
- **Article Integration**: Added a section for articles to enhance content delivery.
- **Emojis**: Implemented emojis to make the site more engaging and visually appealing.
- **Games**: Introduced interactive games to increase user interaction.
- **Mario**: Added a Mario-themed element, adding a playful touch to the site.
- **Buttons**: Included various buttons to improve navigation and user experience.
- **Navigation Bar**: Updated the navigation bar to include all the new features, ensuring seamless access to different sections of the site.

#### Week 1 & 2 Cont.   : Improving Visual Design
In the this week, my focus shifted towards enhancing the theme and visual appeal of the website. This involved:
- **Theme Customization**: Worked on customizing the theme to better reflect the intended aesthetic and user experience.
- **Visual Enhancements**: Applied design changes to improve the overall look and feel of the site, making it more visually appealing and user-friendly.

Overall, these weeks have been a productive period of development and refinement, setting the stage for further enhancements and optimizations.


<script src="https://utteranc.es/client.js"
        repo="Armaghan-z/Armaghan_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>