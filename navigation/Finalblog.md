---
layout: page
title: Sprint 2
description: Home page
hide: true
permalink: /zarak/
---

# 🎨 Cantella Retrospective Blog 🚀

# Cantella & My Feature
- Cantella is a social media platform for students that provides useful study tools and facilitates interaction through backend features like secure authentication, efficient data storage, and seamless API integration.

---

# 🌐 **Backend Development: Core Contributions & Implementation**

## **📌 GitHub Issues & Burndown List**
🔗 <a href="https://github.com/users/XavierTho/projects/3/views/1?pane=issue&itemId=96847217&issue=XavierTho%7Ccantella_frontend%7C70" >Backend Development Github Issue</a>

---

## **🛠️ 1. Developing Backend APIs**

- **What I Did:**
  - Developed **backend APIs** using Flask-RESTful, setting up CRUD operations for studylog features.
### **Code Example:**
```python
    def __init__(self, user_id, subject, hours_studied, notes='', date=None):
        self.user_id = user_id
        self.subject = subject
        self.hours_studied = hours_studied
        self.notes = notes
        self.date = date or datetime.now()

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.warning(f"IntegrityError: Could not create studylog with subject '{self.subject}' due to {str(e)}.")
            return None
        return self

    def read(self):
        user = User.query.get(self.user_id)
        data = {
            "id": self.id,
            "user_id": user.id if user else None,
            "subject": self.subject,
            "hours_studied": self.hours_studied,
            "notes": self.notes,
            "date": self.date.strftime('%Y-%m-%d %H:%M:%S')
        }
        return data

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
```

---

## **💾 2. Database Optimization & Deployment**

- **What I Did:**
  - Set up and optimized the **database using SQLAlchemy**, ensuring data persistence and efficient queries.
  - Started our website and got in running from AWS and cockpit. Was able to create our backend website as well.
  <a href="https://cantella.stu.nighthawkcodingsociety.com/" >Backend Cantella Website</a>
  📸 <img src="/Armaghan_2025/assets/Images/backserver.png" alt="database" style="width:100%;"/>

### **Database Table Structure:**
📸 <img src="/Armaghan_2025/assets/Images/init2.png" alt="database" style="width:100%;"/>

### **Code Example:**
```python
class StudyLog(db.Model):
    __tablename__ = 'studylog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    hours_studied = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text)
    date = db.Column(db.DateTime, default=lambda: datetime.now())
```

### **Postman Testing:**
📌 **Tested API endpoints for:**
- **GET /api/studylognew** → Fetch all studylogs.
- **POST /api/studylognew** → Add new studylogs.
- **PUT /api/studylognew** → Update an existing studylogs.
- **DELETE /api/studylognew** → Remove studylogs.
📸 <img src="/Armaghan_2025/assets/Images/slnpost.png" alt="database" style="width:100%;"/>


---

## **🌍 3. Full Stack Integration & Performance Optimization**

- **What I Did:**
  - Integrated backend APIs with the frontend, ensuring seamless data flow.
  - Optimized backend performance, reducing API response times and improving query efficiency.

### **Code Example:**
```javascript
try {
      const response = await fetch(`${pythonURI}/api/studylognew`, {
          method: 'DELETE',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: logId }),
          credentials: 'include',
      });
```

---

### **Live Demo of Backend Features 🎥**

# 🎨 **Role as Backend Developer**

## **📌 GitHub Issues & Burndown List**

🔗 <a href="https://github.com/XavierTho/cantella_frontend/issues/9#issue-2714007270" >Backend Development Github Issue</a>

---

## **📚 4. Authentication & Security Enhancements**
🎯 **Objective:** Secure user data and sessions.
🛠 **Implementation:**
- Implemented **JWT authentication** for secure user login.
- Enhanced **API security** with token-based authentication.
  📸 <img src="/Armaghan_2025/assets/Images/login.png" alt="database" style="width:100%;"/>

```javascript
    document.addEventListener('DOMContentLoaded', function() {
        const isAuthenticated = localStorage.getItem('authenticated') === 'true';
        if (isAuthenticated) {
            document.getElementById('classes-container').style.display = "block"; // Show the classes container
            document.getElementById('prompt-login').style.display = "none"; // Hide the login prompt
        } else {
            document.getElementById('classes-container').style.display = "none"; // Hide the classes container
            document.getElementById('prompt-login').style.display = "block"; // Show the login prompt
        }
    });
```

```javascript
<div id="classes-container" class="classes-container">
    <!-- Class Cards -->
    <div class="class-card world">
        <a href="{{site.baseurl}}/classes/ap/world/home">📜 AP World History</a>
    </div>
    <div class="class-card csp">
        <a href="{{site.baseurl}}/classes/ap/csp/home">💻 AP CSP</a>
    </div>
    <div class="class-card chem">
        <a href="{{site.baseurl}}/classes/ap/chem/home">⚗️ AP Chemistry</a>
    </div>
    <div class="class-card ush">
        <a href="{{site.baseurl}}/classes/ap/ush/home">🦅 AP US History</a>
    </div>
</div>
```
---
## **🎨 5. Database Initialization & Restoration**  
🎯 **Objective:** Ensure a structured and reliable database setup with backup restoration capabilities.  

🎨 **Implementation:**  
- Initialized **study logs database** using SQLAlchemy models.  
- Implemented **db_init** to set up tables and insert default records.  
- Fixed the **restore backup function** to reload previous study log data efficiently.

![Database Initialization](/Armaghan_2025/assets/Images/dbterm.png)

---

<!-- College Board CPT Requirements Met -->
<section style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #0d6efd; border-radius: 10px; margin-top: 20px;">
    <h2 style="color: #0d6efd; text-align: center;">🎯 College Board CPT Requirements Met</h2>
    <table style="width: 40%; border-collapse: collapse; border: 1px solid #ddd;">
        <thead>
            <tr style="background-color: #0d6efd; color: white;">
                <th style="text-align: left; padding: 12px; border: 1px solid #ddd;">Requirement</th>
                <th style="text-align: left; padding: 12px; border: 1px solid #ddd;">Feature Implementation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><b>Input</b></td>
                <td style="padding: 12px; border: 1px solid #ddd;">
                    Users submit study session details via a JSON request to the API.  
                    <br><b>Example:</b>
                    <pre style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
{
    "user_id": 1,
    "subject": "AP Physics",
    "hours_studied": 2.5,
    "notes": "Studied Newton's Laws of Motion."
}
                    </pre>
                </td>
            </tr>
            <tr style="background-color: #f1f8ff;">
                <td style="padding: 12px; border: 1px solid #ddd;"><b>Use of List/Collection Type</b></td>
                <td style="padding: 12px; border: 1px solid #ddd;">
                    Study logs are stored in an SQL database using SQLAlchemy models.  
                    <br><b>Retrieving logs:</b>
                    <pre style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
all_studylogs = StudyLog.query.all()
studylogs = [log.read() for log in all_studylogs]
                    </pre>
                </td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><b>Procedure</b></td>
                <td style="padding: 12px; border: 1px solid #ddd;">
                    The <code>post</code> method processes user input and stores the log in the database.
                    <br><b>Implementation:</b>
                    <pre style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
def post(self):
    data = request.get_json()
    studylog = StudyLog(data["user_id"], data["subject"], data["hours_studied"], data["notes"])
    studylog.create()
    return jsonify(studylog.read())
                    </pre>
                </td>
            </tr>
            <tr style="background-color: #f1f8ff;">
                <td style="padding: 12px; border: 1px solid #ddd;"><b>Algorithm</b></td>
                <td style="padding: 12px; border: 1px solid #ddd;">
                    Ensures data integrity by checking for existing records before insertion.
                    <br><b>Duplicate Prevention:</b>
                    <pre style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
existing_log = StudyLog.query.filter_by(user_id=data["user_id"], subject=data["subject"]).first()
if not existing_log:
    studylog = StudyLog(**data)
    studylog.create()
                    </pre>
                </td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><b>Output</b></td>
                <td style="padding: 12px; border: 1px solid #ddd;">
                    Study logs are retrieved and displayed as JSON.  
                    <br><b>Response Example:</b>
                    <pre style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
return jsonify([log.read() for log in StudyLog.query.all()])
                    </pre>
                </td>
            </tr>
            <tr style="background-color: #f1f8ff;">
                <td style="padding: 12px; border: 1px solid #ddd;"><b>Functionality Demonstration</b></td>
                <td style="padding: 12px; border: 1px solid #ddd;">
                    Users can input study sessions, view logs, and modify them via API endpoints.
                    <ul>
                        <li><b>POST</b>: <code>/api/studylognew</code> - Add new study logs</li>
                        <li><b>GET</b>: <code>/api/studylognew</code> - Retrieve logs</li>
                        <li><b>PUT</b>: <code>/api/studylognew</code> - Update logs</li>
                        <li><b>DELETE</b>: <code>/api/studylognew</code> - Remove logs</li>
                    </ul>
                </td>
            </tr>
        </tbody>
    </table>
</section>
# 🚀 How My StudyLogs Project Aligns with AP CSP Big Ideas

## 🛠 Big Idea 1: Creative Development
- **StudyLogs solves a real-world problem** by allowing users to **track their study sessions, subjects, and progress dynamically**.  
- The **user interface is interactive**, making it easy to **log, edit, and remove study sessions** with a simple API request.  
- **Creative problem-solving**: Users can analyze their study habits over time to improve learning efficiency.

---

## 📊 Big Idea 2: Data
- The project **collects, organizes, and manages study session data**, allowing users to track hours spent on different subjects.  
- **Data abstraction** is implemented through structured storage (**SQL database, JSON responses, and API endpoints**).  
- Users can **update and delete logs**, demonstrating effective **data manipulation and persistence**.

---

## 🤖 Big Idea 3: Algorithms and Programming
- **Custom functions** like `post()` and `get()` process user input and handle database interactions.  
- Uses **selection (if-statements), iteration (loops), and sequencing** to efficiently **retrieve and manage study logs**.  
- **Event-driven programming**: API functions execute based on user interactions, such as logging new study sessions.

---

## 🌐 Big Idea 4: Computing Systems & Networks
- The **frontend interacts with a backend API**, demonstrating real-world **networking and database integration**.  
- Uses **HTTP requests (GET, POST, PUT, DELETE)** to store and retrieve study session data securely.  
- **Demonstrates distributed computing**, ensuring that user study logs are accessible across multiple devices.

---

## 🌍 Big Idea 5: Impact of Computing
- **StudyLogs helps students improve productivity** by tracking their study hours and subjects effectively.  
- The system can be applied to **education, self-improvement, and time management**, making it a valuable learning tool.  
- Shows how **computing enhances organization and learning strategies** for better academic performance.

---

This project demonstrates all five **AP CSP Big Ideas** in a meaningful way! 🚀
<!-- MCQ Performance Section -->
<section style="background-color: #fff3cd; padding: 15px; border-left: 5px solid #ffc107; border-radius: 8px; margin-top: 20px;">
    <h2 style="color: #d39e00;">🧠 MCQ Performance & Improvement Plan</h2>
    <p>
        For the multiple-choice section, I scored <b>55/67</b>. While this is a solid score, there is room for improvement before the AP exam.
        My key areas for growth include:
    </p>
    <h3>Performance Summary</h3>
    <h4>Struggles (Needs Improvement)</h4>
    <h5>0% Performance:</h5>
    <ul>
        <li><b>Variables and Assignments</b></li>
        <li><b>Strings</b></li>
    </ul>
    <h5>Low Performance (Below 50%):</h5>
    <ul>
        <li><b>Calling Procedures (40%)</b></li>
    </ul>
    <h4>Strengths (Doing Well)</h4>
    <h5>50%+ Performance:</h5>
    <ul>
        <li><b>Algorithmic Efficiency (50%)</b></li>
        <li><b>Fault Tolerance (50%)</b></li>
        <li><b>Extracting Information from Data (57%)</b></li>
    </ul>
    <h5>Above 70%:</h5>
    <ul>
        <li><b>Identifying and Correcting Errors (71%)</b></li>
        <li><b>Developing Algorithms (75%)</b></li>
        <li><b>Iteration (80%)</b></li>
        <li><b>Program Design and Development (100%)</b></li>
    </ul>
    <h4>How to Improve</h4>
    <ul>
        <li><b>Focus on Fundamentals:</b> Review variables, assignments, and string manipulation.</li>
        <li><b>Practice More:</b> Work on calling procedures through hands-on coding problems.</li>
        <li><b>Strengthen Weak Areas:</b> Revisit past mistakes in quizzes/tests and redo those topics.</li>
        <li><b>Keep Up the Momentum:</b> Maintain strong performance in algorithms, iteration, and program design by tackling advanced problems.</li>
    </ul>
    <!-- Space for Screenshot -->
    <div style="text-align: center; margin-top: 10px;">
 <img src="/Armaghan_2025/assets/Images/mcqresponse.png" alt="database" style="width:100%;"/>
        <p style="font-size: 14px; color: #555;">📸 Screenshot of MCQ Scoring Report</p>
    </div>
    <p>
        Moving forward, I will focus on <b>targeted practice</b> and <b>concept reinforcement</b> to improve my score before the AP test. 🚀
    </p>
</section>

## Night at the Museum (N@tM) Presentation
<div style="display: flex; overflow-x: auto; gap: 10px;">
  <img src="/Armaghan_2025/assets/Images/natm1.JPG" alt="N@TM image 1" style="width: 450; height: auto;"/>
  <img src="/Armaghan_2025/assets/Images/natm2.png" alt="N@TM image 2" style="width: 200px; height: auto;"/>
  <img src="/Armaghan_2025/assets/Images/natm3.JPG" alt="N@TM image 3" style="width: 200px; height: 200px;"/>
</div>
## 🎤 Night at the Museum (N@tM) Feedback Summary  

<table>
  <tr>
    <th style="color: #4CAF50; font-size: 18px;">✅ Positive Feedback</th>
    <th style="color: #FF9800; font-size: 18px;">🔹 Areas for Improvement</th>
  </tr>
  <tr>
    <td>
      <ul>
        <li><b>API Efficiency & Security</b> – Many users praised the <b>efficiency and security</b> of the backend APIs.</li>
        <li><b>Functionality & Concept</b> – Users appreciated the <b>robustness and scalability</b> of the backend architecture.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>Documentation</b> – Feedback suggested improving <b>API documentation</b> for better developer understanding.</li>
        <li><b>Scalability</b> – Some mentioned enhancing <b>scalability</b> for larger user loads.</li>
      </ul>
    </td>
  </tr>
</table>

---

### 🚀 **Suggestions for Future Development**
<table>
  <tr>
    <td style="background-color: #2196F3; color: white; padding: 10px;"><b>🛠 Improved API Documentation</b></td>
    <td>Enhance <b>API documentation</b> for better developer onboarding and understanding.</td>
  </tr>
  <tr>
    <td style="background-color: #009688; color: white; padding: 10px;"><b>📚 Microservices Architecture</b></td>
    <td>Explore <b>microservices architecture</b> for better scalability and modularity.</td>
  </tr>
  <tr>
    <td style="background-color: #FF5722; color: white; padding: 10px;"><b>👥 Enhanced Security Measures</b></td>
    <td>Implement <b>advanced security measures</b> to protect user data and sessions.</td>
  </tr>
</table>

---

### ⭐ **Overall Project Rating**
<center>
  <p style="font-size: 20px; color: #FFD700;"><b>🌟 4.5/5</b></p>
  <p>The majority of participants rated the project highly, showing strong appreciation for its backend efficiency and security.</p>
</center>

This feedback provides great insight into **what worked well** and **what needs improvement** for future iterations of Cantella! 🚀

---

# 📝 **Personal Reflection: Strengths & Weaknesses**

| **Strengths** | **Weaknesses** |
|--------------|---------------|
| *Debugging & Problem-Solving:* I was able to quickly identify and resolve backend issues, improving API efficiency and reliability. | I need to improve my documentation skills to ensure better understanding and maintenance of the codebase. |
| *Database Optimization:* I effectively optimized database queries, enhancing performance and reducing response times. | I should focus on better frontend-backend coordination to ensure seamless integration. |
| *Security Implementation:* Implemented robust security measures to protect user data and sessions. | I can enhance test coverage to ensure all edge cases are handled effectively for the MCQ. |

<h3> <b>Solutions:</b> Next trimester I will focus on improving documentation, enhancing test coverage, and better coordinating with frontend development to ensure seamless integration.
</h3>
---

# 🚀 **Future Plans & Next Steps**

## **🌟 Future of Cantella**
- Implementing **microservices architecture** for better scalability.
- Enhancing **API documentation** for improved developer onboarding.
- Exploring **backend-driven AI optimizations** for advanced features.

## **🎓 Future Projects & Application of CSP Knowledge**
- Majoring in **Electrical Engineering**.
- Future projects - exploring ideas in the future and could use this project on my resume.

---

<!-- Reaching Out & Helping Someone Section -->
<section style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-top: 20px;">
    <h2 style="color: #007bff;">🤝 Collaboration with Ahmad Imran</h2>
    <p><b>For the final review, I collaborated with Ahmad Imran, whom I met at Night at the Museum.</b> We exchanged feedback on each other's blogs and provided recommendations for improvement.</p>
    <!-- Image of Studying Together -->
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="/Armaghan_2025/assets/Images/chats.png" alt="Ahmad and I discussing our blogs" style="width: 100%; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
        <p style="font-size: 14px; color: #555;">📸 Discussing our blogs for the final review</p>
    </div>

    <h3 style="color: #28a745;">🔍 Feedback from Ahmad on My Blog</h3>

    <ul style="list-style-type: none; padding-left: 0;">
        <li style="background-color: #e9ecef; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
            📝 <b>Content Structure:</b> "Your blog is well-structured and easy to follow, with clear explanations."
        </li>
        <li style="background-color: #e9ecef; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
            🎨 <b>Engagement:</b> "Adding more visuals or interactive elements could enhance engagement."
        </li>
        <li style="background-color: #e9ecef; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
            📊 <b>Depth of Content:</b> "Going more in-depth on accomplishments would add value."
        </li>
    </ul>

    <h3 style="color: #17a2b8;">📌 How This Helped Me Prepare</h3>
    <p>
        Ahmad's feedback helped me identify areas for enhancement before the final review. Based on his suggestions, I will:
    </p>
    <ul>
        <li>🔹 Add more <b>visuals and interactive elements</b> to increase engagement.</li>
        <li>🔹 Provide more <b>in-depth explanations</b> of my accomplishments.</li>
    </ul>

    <p><b>By exchanging feedback, we both gained valuable insights into our work and improved our final exam preparation.</b> This collaboration offered a fresh perspective and helped refine our projects.</p>
</section>

## 📝 Self-Grade Assessment

### 📊 Main Evaluation (9 Points)
<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th>Criteria</th>
    <th>Self-Grade</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td>🖐 <b>Five things I did over 12 weeks</b> (5 pts)</td>
    <td>4.5/5</td>
    <td>I accomplished a lot in the 12 weeks and learned a lot, especially through the 5 things I presented. I could have improved documentation and test coverage.</td>
  </tr>
  <tr>
    <td>🎥 <b>Full Stack Project Demo</b> (2 pts)</td>
    <td>2/2</td>
    <td>My feature has full stack implementation with efficient backend integration.</td>
  </tr>
  <tr>
    <td>📝 <b>Project Feature Blog Write-Up (CPT/FRQ Language)</b> (1 pt)</td>
    <td>.9/1</td>
    <td>This blog includes how I completed CPT requirements through my work.</td>
  </tr>
  <tr>
    <td>🧠 <b>MCQ Section</b> (1 pt)</td>
    <td>.9/1</td>
    <td>Explanation of performance on the MCQs and accuracy in responses.</td>
  </tr>
</table>
---

### ⭐ Bonus: 10th Point

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Ideas for the 10th Point</th>
      <th>Completed? ✅</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🔍 <b>Taking extreme interest in other projects & people (N@tM reviews, event chronicling, personalization)</b></td>
      <td>✅</td>
    </tr>
    <tr>
      <td>🤝 <b>Helping a new person get Final Exam materials organized</b></td>
      <td>✅</td>
    </tr>
    <tr>
      <td>🎯 <b>Thinking ahead – next steps in CompSci, career, internships, future classes</b></td>
      <td>✅</td>
    </tr>
    <tr>
      <td>💡 <b>Reflecting on personal strengths & weaknesses in detail</b></td>
      <td>✅</td>
    </tr>
    <tr>
      <td>📈 <b>Creating next steps for the project (plans, improvements, future direction)</b></td>
      <td>✅</td>
    </tr>
    <tr>
      <td>📩 <b>Sending a summary of talking points 24 hours in advance</b> 📸 <img src="/Armaghan_2025/assets/Images/mortchat.png" alt="database" style="width:80%;"/></td>
      <td>✅</td>
    </tr>
    <tr>
      <td>⏳ <b>Being able to clearly highlight all 10 points during the live review (Hopefully)</b></td>
      <td>✅</td>
    </tr>
  </tbody>
</table>

---

### 📌 Final Reflection

**_Final Grade: 9.3/10_**
