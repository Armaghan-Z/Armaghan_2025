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

#### Week 0: Setting Up The Foundation
In the first week of my coding journey, my primary focus was on setting up my development environment and ensuring that the `make` tool was functioning correctly. This involved initializing my repository and troubleshooting any issues that arose during setup. It was a crucial step in laying a solid foundation for my project.

#### Weeks 1 & 2: Enhancing Functionality and Adding Features
During the first and second weeks, I dedicated my efforts to enriching the functionality of the website. I successfully incorporated a variety of features, including:
- **Article Integration**: Added a section for articles to enhance content delivery and keep visitors informed.
- **Emojis**: Implemented emojis to make the site more engaging and visually appealing.
- **Games**: Introduced interactive games to increase user interaction and enjoyment.
- **Mario**: Added a Mario-themed element, which added a playful touch to the site and sparked nostalgia.
- **Buttons**: Included various buttons to improve navigation and user experience across different sections.
- **Navigation Bar**: Updated the navigation bar to include all the new features, ensuring seamless access to all parts of the site.

#### Weeks 1 & 2 Cont.: Improving Visual Design
In this segment, my focus shifted toward enhancing the theme and visual appeal of the website. This involved:
- **Theme Customization**: Worked on customizing the theme to better reflect the intended aesthetic and user experience.
- **Visual Enhancements**: Applied design changes to improve the overall look and feel of the site, making it more visually appealing and user-friendly.

#### Weeks 3 & 4: Expanding Content and Features
Building upon the previous weeks, I continued to enhance the website with several new features and improvements:
- **Calculator Addition**: Developed and integrated a functional calculator, providing a useful tool for visitors to perform quick calculations.
- **Image Gallery Expansion**: Added more images throughout the site to create a richer visual experience, showcasing various topics and personal projects.
- **Formula 1 Blog**: Launched a dedicated blog section for Formula 1, where I share my thoughts, race analyses, and updates about the sport I am passionate about.
- **Cookie Clicker Game**: Introduced the classic Cookie Clicker game, adding a fun and addictive element that keeps users engaged.
- **Jupyter Notebooks Integration**: Included Jupyter notebooks, allowing visitors to explore and interact with my coding projects directly on the site.
- **Attempted vs. Accomplished**: Created sections to highlight my goals versus what I've successfully completed, providing transparency into my progress.
- **Spotify Integration**: Incorporated a Spotify API to showcase my favorite tracks and playlists, enhancing the site's musical aspect.
- **Games Refinement**: Added and fixed various games on the site, ensuring they function smoothly and provide a better user experience.
- **Enhanced About Me Section**: Improved the "About Me" section with more details about my background, interests, and coding journey, making it more personal and relatable.
- **Deployment Fixes**: Addressed issues related to site deployment, ensuring that everything is running smoothly and efficiently.
- **Dropdown Menu Creation**: Developed a dropdown menu for easy navigation, streamlining the user experience by organizing links effectively.
- **Pair Site Improvements**: Worked on fixing the design and functionality of my pair site, enhancing its usability and appeal.
- **Button Updates**: Refined button designs for better aesthetics and responsiveness, ensuring a consistent look throughout the site.
- **Quizzes**: Created interactive quizzes that allow users to test their knowledge on various topics, making learning more fun.
- **API Implementations**: Integrated various APIs to enrich content and functionality, providing dynamic features that enhance user interaction.
- **Video Embedding**: Added video content to further diversify the types of media on my site, creating a more engaging experience for visitors.

Overall, Weeks 3 and 4 were a significant period of growth and creativity. I successfully expanded the scope of my website, integrating diverse features and content that reflect my interests and skills, while continuously enhancing user experience.

####  Weeks 5 & : Sprint 2

<script src="https://utteranc.es/client.js"
        repo="Armaghan-z/Armaghan_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
