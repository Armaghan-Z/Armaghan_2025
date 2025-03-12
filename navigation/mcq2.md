---
title: "AP CSP MCQ TRI 2 (MCQ)"
description: "This document contains My MCQ practice test review and summary"
date: 2025-03-10
permalink: /mcq2/
categories: [AP Computer Science Principles, Study Log]
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AP CSP MCQ TRI 2 Review</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333;
            text-align: center;
        }
        .question {
            margin-bottom: 20px;
            padding: 15px;
            border-left: 5px solid #007bff;
            background: #e9f5ff;
            border-radius: 5px;
        }
        .image {
            text-align: center;
            margin: 10px 0;
        }
        .correct-answer {
            color: green;
            font-weight: bold;
        }
        .incorrect-answer {
            color: red;
            font-weight: bold;
        }
        .fix {
            background: #fffae6;
            padding: 10px;
            border-left: 5px solid #ffcc00;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>AP CSP MCQ TRI 2 Review & Test Corrections</h1>
        <h2>Performance Summary</h2>
        <ul>
            <li><strong>Total Time Spent:</strong> 2:56:44</li>
            <li><strong>Total Score:</strong> 55/67</li>
            <li><strong>Subjects to Improve:</strong> Variables and Assignments, Strings, Calling Procedures, Algorithmic Efficiency, Fault Tolerance, Extracting Information from Data, Identifying and Correcting Errors</li>
            <li><strong>Strengths:</strong> Iteration, Developing Algorithms</li>
            <li><strong>Goal:</strong> Improve weak areas through structured practice and targeted corrections.</li>
        </ul>
        <h2>Subject Performance Breakdown</h2>
        <div class="image"><img src="/Armaghan_2025/assets/Images/mcqresponse.png" alt="Subject Performance Breakdown"></div>
        <p>The image above shows my performance across different AP CSP topics. Areas with a performance below 80% are those that need improvement.</p>
        <h2>Deep Dive into Areas for Improvement</h2>
        <ul>
            <li><strong>Variables and Assignments (0%)</strong> - I need to review variable initialization, assignment rules, and scope limitations.</li>
            <li><strong>Strings (0%)</strong> - Focus on mastering string manipulation, indexing, slicing, and concatenation.</li>
            <li><strong>Calling Procedures (40%)</strong> - Improve my understanding of function parameters, return values, and nested function calls.</li>
            <li><strong>Algorithmic Efficiency (50%)</strong> - Study sorting algorithms, Big-O notation, and runtime optimizations.</li>
            <li><strong>Fault Tolerance (50%)</strong> - Learn best practices for error handling, debugging, and defensive programming.</li>
            <li><strong>Extracting Information from Data (57%)</strong> - Work on reading, parsing, and transforming data in structured formats.</li>
            <li><strong>Identifying and Correcting Errors (71%)</strong> - Strengthen debugging strategies and logical error identification.</li>
        </ul>
        <h2>Test Corrections</h2>
        <div class="question">
            <h3>Q56: Compare Execution Times of Two Versions</h3>
            <div class="image"><img src="/Armaghan_2025/assets/Images/q56.png" alt="Question 56"></div>
            <p><span class="incorrect-answer">Incorrect Answer:</span> Assumed version I was slower without analyzing function calls.</p>
            <p><span class="correct-answer">Correct Answer:</span> Version II takes longer because it calls the function twice per loop iteration.</p>
            <div class="fix">Fix: Analyze execution time by counting function calls instead of assuming based on structure.</div>
        </div>
        
        <div class="question">
            <h3>Q41: TrimLeft and TrimRight</h3>
            <div class="image"><img src="/Armaghan_2025/assets/Images/q41.png" alt="Question 41"></div>
            <p><span class="incorrect-answer">Incorrect Answer:</span> Chose a statement that incorrectly trimmed both ends simultaneously.</p>
            <p><span class="correct-answer">Correct Answer:</span> The correct sequence is to trim the right first, then trim the left to remove the prefix.</p>
            <div class="fix">Fix: Apply trimming functions in the correct order to isolate the filename's description.</div>
        </div>
        
        <div class="question">
            <h3>Q37: DrawLine on a Coordinate Grid</h3>
            <div class="image"><img src="/Armaghan_2025/assets/Images/q37.png" alt="Question 37"></div>
            <p><span class="incorrect-answer">Incorrect Answer:</span> Miscalculated the iterative adjustment of coordinates.</p>
            <p><span class="correct-answer">Correct Answer:</span> The correct approach is to modify both x and y values appropriately in each iteration.</p>
            <div class="fix">Fix: Carefully track variable updates to ensure proper geometric transformations.</div>
        </div>
        
        <div class="question">
            <h3>Q33: Course Grade Data Analysis</h3>
            <div class="image"><img src="/Armaghan_2025/assets/Images/q33.png" alt="Question 33"></div>
            <p><span class="incorrect-answer">Incorrect Answer:</span> Did not recognize that individual scores can be inferred from averages.</p>
            <p><span class="correct-answer">Correct Answer:</span> The proportion of students improving can be determined by comparing averages before and after dropping a score.</p>
            <div class="fix">Fix: Recognize how statistical analysis of data sets can be used to infer missing values.</div>
        </div>
        
        <div class="question">
            <h3>Q28: Swapping Alpha and Beta</h3>
            <div class="image"><img src="/Armaghan_2025/assets/Images/q28.png" alt="Question 28"></div>
            <p><span class="incorrect-answer">Incorrect Answer:</span> Chose an option that resulted in both variables having the same value.</p>
            <p><span class="correct-answer">Correct Answer:</span> The correct swap process involves a temporary variable to store intermediate values.</p>
            <div class="fix">Fix: Follow step-by-step swapping logic to ensure proper assignment.</div>
        </div>
        
        <div class="question">
            <h3>Q18: Algorithm to Move Robot to Goal</h3>
            <div class="image"><img src="/Armaghan_2025/assets/Images/q18.png" alt="Question 18"></div>
            <p><span class="incorrect-answer">Incorrect Answer:</span> Used a loop condition that led the robot off the grid.</p>
            <p><span class="correct-answer">Correct Answer:</span> Ensure the movement condition prevents boundary violations.</p>
            <div class="fix">Fix: Implement better control flow logic to keep the robot within valid movement paths.</div>
        </div>
        
        <div class="question">
            <h3>Q1: Multiply x by 3 Inside a Loop</h3>
            <div class="image"><img src="/Armaghan_2025/assets/Images/q1.png" alt="Question 1"></div>
            <p><span class="incorrect-answer">Incorrect Answer:</span> Miscalculated the number of multiplications performed in the loop.</p>
            <p><span class="correct-answer">Correct Answer:</span> Recognize that an iteration count of four results in four multiplications.</p>
            <div class="fix">Fix: Carefully follow loop execution to count how many times an operation is performed.</div>
        </div>
        
        <h2>Next Steps</h2>
        <ul>
            <li>Use interactive coding exercises to reinforce function calls and loop execution.</li>
            <li>Practice identifying efficient algorithms by analyzing function call frequency.</li>
            <li>Work on debugging strategies by tracing step-by-step execution of code.</li>
            <li>Regularly review logic for conditionals and loops to avoid execution missteps.</li>
        </ul>
    </div>
</body>
</html>
