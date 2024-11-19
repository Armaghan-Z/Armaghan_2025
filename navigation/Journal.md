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

####  Weeks 5 & 6: Sprint 2
- **3.8.1** I Created Period 3's 3.8.1 lesson going over Recursion, Iteration, and Nested For loops.
In weeks 5 and 6, my primary focus was on creating detailed lesson content while continuing to refine my website and existing features.
### Lesson Page on Iteration, Recursion, and Nested For Loops
I dedicated a significant amount of time to creating and structuring my lesson page on iteration, recursion, and nested for loops. The page includes:
- **Concept Explanations**: I provided clear definitions and explanations of key concepts like recursion and nested loops.
- **Coding Examples**: I integrated Python and JavaScript examples to demonstrate how these concepts are applied in real code.
- **Popcorn Hacks**: I added interactive coding exercises to help users practice what they’ve learned, including tasks that involve loops and conditionals.
- **Homework Tasks**: I created homework challenges to further solidify understanding, allowing users to engage with recursion and loops on their own.
### Refinements and Improvements
Alongside the lesson page, I continued refining my website:
- **Popcorn Hacks Enhancements**: I added more examples and scenarios for users to practice, refining the presentation to make it more user-friendly.
- **Interactive Features**: I improved the functionality of existing games and quizzes, ensuring they ran smoothly without bugs.
- **Overall Site Optimization**: Minor tweaks were made to the site’s design and responsiveness to improve the overall user experience.
These weeks were essential for solidifying the educational aspect of my website, ensuring that users not only engage with my content but also learn from it.

- **Script Reflection**: Hey everyone! I’m Armaghan Zarak, and I worked on Big Idea 3.8 with Hithin, Elliot, and Nikhil which was about nested for loops, recursion, and iteration which was what I focused on mostly. Over the past few weeks, we’ve been diving deep into coding, especially focusing on Big Idea 3 for the College Board. Coming in with no coding experience, I feel like I’ve really learned a lot!
One lesson that stood out was Trevor's group on the Fibonacci sequence. It’s amazing how each number is just the sum of the two before it! Learning about recursion showed me how a function can call itself. It sounded weird at first, but coding it made it click. The homework hacks were super helpful too! I created functions to add, subtract, divide, and find the modulus of two numbers, plus a function to find points on the graph of f(x). It was cool seeing how coding connects with math in a practical way.
Collaborating with my classmates made this experience even better. We worked on a lesson plan together and used Git to stay organized. Seeing how pull requests and commits helped us share ideas and track progress was awesome. We learned how to handle feedback and fix merge conflicts, which really brought our project together. Plus, we had to make sure our pull requests were accepted on time so we could actually teach our lesson which was pretty stressful and memorable!
What made our lesson unique was how we organized our topics and added a fun theme. I also enjoyed learning about iteration and nested loops through practical examples like the Popcorn Hack, where we checked numbers for divisibility using recursion. Explaining these concepts to my peers deepened my understanding because I had to know them inside and out to teach them. Knowing how to use lists, nested loops, recursion, and so on has helped me prepare for the AP exam in May.
Overall, this experience has been super memorable and beneficial. Teaching others improved my coding skills and solidified my grasp of recursion, nested loops, and iteration. I feel like I’ve gotten a lot better, and I’m excited to keep going!

## Weeks 7 & 8: Backend Development with Flask
I delved into backend development using Flask, focusing on:
- **Setting Up Flask Environment**: Configuring the development environment.
- **Creating Routes and Views**: Developing endpoints for the web application.
- **Integrating Templates**: Connecting frontend with backend logic.
- **Implementing Forms**: Handling user input and processing data.

## Weeks 9 & 10: Database Integration and API Development
These weeks were dedicated to:
- **Database Setup**: Implementing SQL databases for data persistence.
- **CRUD Operations**: Developing Create, Read, Update, and Delete functionalities.
- **API Development**: Creating RESTful APIs for data interaction.
- **Testing and Debugging**: Ensuring functionality and resolving issues.

## Weeks 11 & 12: Finalizing Project and Presentation Preparation
In the final phase, I focused on:
- **Project Refinement**: Polishing features and fixing bugs.
- **Documentation**: Creating comprehensive guides and comments.
- **Presentation Preparation**: Organizing materials for the “Night at the Museum” event.
- **Deployment**: Ensuring the application is live and accessible.

## Reflection
Throughout this journey, I have gained a deep understanding of both frontend and backend development. The integration of various technologies and the application of theoretical concepts in practical scenarios have been invaluable. Collaborating with peers and receiving feedback have further enriched my learning experience.
I am excited to continue my journey in the world of web development, where I can apply my skills and contribute to meaningful projects that make a positive impact.

## MCQ Review
 - Taking the AP CSP 2018 multiple-choice practice test was a really eye-opening experience. It gave me a clear idea of where I’m doing well and where I need to improve in computer science. The test covered so many areas—like programming, algorithms, and even how technology impacts society—which made me realize how much there is to learn. One of the biggest takeaways for me was how important it is to think critically and pay attention to the little details in a question. I felt pretty confident with basic programming concepts and algorithms, but I definitely struggled with trickier topics, like data representation and edge cases in problem-solving. Those tougher questions really pointed out that I need to work on reading pseudocode better and understanding how to handle unusual scenarios in algorithms. Another big lesson was learning to stay calm and focused under time pressure, which is something I know I’ll need for the real exam. Overall, the test helped me see what I need to work on and reminded me how important it is to have a solid understanding of the basics. It also gave me a boost of motivation to keep studying and tackling challenges head-on!

**Question 7 Assignment statements with start end and current:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Screenshot-2024-11-19-at-2.34.41-AM.png" alt="Questions 7's correct answer" width="500px" height="250px"/>

- For this question I said `1  3` but this option is incorrect. The values 1 and 3 are the original values of start and current, not the final values.

- **Question 12 Social media 12 year projections:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Screenshot-2024-11-19-at-3.07.29-AM.png" alt="Questions 12's correct answer" width="400px" height="300px"/>

- For this question I said `30.6` but this option is incorrect. The approximation 30.6 million would be a better estimate for year 11.

- **Question 14 Comparing loop algorithms:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Question-14-mcq.png" alt="Questions 14's correct answer" width="430px" height="250px"/>

- For this question I said `Program A and program B display a different number of values.` but this option is incorrect. Both programs display ten values.

- **Question 25 Shortening strings by replacing TH and IS:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Question-25-mcqtrue.png" alt="Questions 25's correct answer" width="450px" height="350px"/>s

- For this question I said `"BANANA"` but this option is incorrect. This string can be shortened using byte pair encoding. For example, Open quotation, BANANA, close quotation can be shortened to Open quotation, B, asterisk, asterisk, A, close quotation by replacing each instance of Open quotation, AN, close quotation with Open quotation, asterisk, close quotation.

- **Question 26 Completing robot code by adding if statement:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Question-26-mcq.png" alt="Questions 26's correct answer" width="450px" height="350px"/>

- For this question I said <img src="/Armaghan_2025/assets/Images/Question-26-Answer.png" width="150px" height="60px"/> 
 but this option is incorrect. This code segment does not move the robot at all. The robot cannot move right from its initial position, so the body of the IF statement is never executed, and the robot remains at its starting position.

- **Question 35 Musicians and copyright violations:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Question-35-mcq.png" alt="Questions 35's correct answer" width="450px" height="350px"/>

- For this question I said `Using samples from nondigital sound sources (vinyl records, tapes, etc.)` but this option is incorrect. Using samples from nondigital sound sources could put the musician at risk of violating copyright laws.

- **Question 42 Increasing bit representation for internet protocol:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Question-42-mcq.png" alt="Questions 42's correct answer" width="450px" height="350px"/>

- For this question I said `96 times as many addresses are available.` but this option is incorrect. IPv6 has 2 raised to the ninety sixth power times as many possible addresses as IPv4.

- **Question 44 Using a 4 bit representation for integers:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Question-44-mcq.png" alt="Questions 44's correct answer" width="450px" height="350px"/>

- For this question I said `II and III only` but this option is incorrect. The operation 10 plus 7 causes an overflow error, but 12 plus 3 does not produce a result large enough to cause an overflow error.

- **Question 47 Encrypting and decrypting using public key cryptography:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Question-47-mcq.png" alt="Questions 47's correct answer" width="450px" height="350px"/>

- For this question I said `The sender’s private key` but this option is incorrect. The sender’s private key cannot be used to decrypt the message.

- **Question 52 Using a 4 bit representation for integers:**
- Here is the correct answer: <img src="/Armaghan_2025/assets/Images/Question-52-mcq.png" alt="Questions 52's correct answer" width="450px" height="350px"/>

- For this question I said `I only` but this option is incorrect. Option I does not work because it performs the "shorten" step before the "keep palindromes" step.

<script src="https://utteranc.es/client.js"
        repo="Armaghan-z/Armaghan_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
