---
title: "AP CSP Personalized Project Reference (PPR)"
description: "This document contains required code segments for the AP CSP Create Task, showcasing a student-developed function and list implementation."
date: 2025-03-10
permalink: /ppr/
categories: [AP Computer Science Principles, Study Log]
---

# **AP CSP Personalized Project Reference (PPR)**

## **Component C: Student-Developed Procedure**

### **i. Student-Developed Function**
Below is a student-developed function that:
- Defines the procedure’s name and return type (if applicable).
- Uses one or more parameters that impact its functionality.
- Implements an algorithm that includes sequencing, selection, and iteration.

```python
@token_required()
def post(self):
    try:
        data = request.get_json()
        if not data:
            return {'message': 'No input data provided'}, 400
        user_id = data.get('user_id')
        subject = data.get('subject')
        hours_studied = data.get('hours_studied')
        notes = data.get('notes')
        if not user_id:
            return {'message': 'User ID is required'}, 400
        if not subject:
            return {'message': 'Subject is required'}, 400
        if not hours_studied:
            return {'message': 'Hours studied is required'}, 400
        if not notes:
            return {'message': 'Notes is required'}, 400
        studylog = StudyLog(user_id, subject, hours_studied, notes)
        print(json.dumps({
            "user_id": user_id,
            "subject": subject,
            "hours_studied": hours_studied,
            "notes": notes
        }))
        studylog.create()
        return jsonify(studylog.read())
    except Exception as e:
        return {'message': f"An error occurred: {str(e)}"}, 500
```

### **How this function meets AP CSP requirements:**
- **Sequencing:** Steps are performed in a specific order (data extraction → validation → object creation → saving to database).
- **Selection:** Uses `if` statements to check for missing fields before proceeding.
- **Iteration:** Involves database operations that iterate over records.

---

### **ii. Where the Function is Called**
This code segment shows the exact location where the function is being used within the program:

```python
api.add_resource(CRUD, '/studylognew')
```

---

## **Component D: Data Abstraction**

### **i. List Implementation**
The `StudyLog` model uses a list-like structure to manage study log entries.

```python
class StudyLog(db.Model):
    __tablename__ = 'studylog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    hours_studied = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text)
    date = db.Column(db.DateTime, default=lambda: datetime.now())

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
```

### **ii. JavaScript Functions**
JavaScript functions handle user interactions and communicate with the backend API.

```javascript
document.getElementById('study-log-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formMessages = document.getElementById('form-messages');
    const subject = document.getElementById('subject').value.trim();
    const hours = document.getElementById('hours').value.trim();
    const notes = document.getElementById('notes').value.trim();
    if (!subject || !hours) {
        formMessages.textContent = 'Subject and hours are required!';
        formMessages.className = 'error';
        formMessages.classList.remove('hidden');
        return;
    }
    const data = {
        user_id: 1,
        subject,
        hours_studied: parseFloat(hours),
        notes
    };
    try {
        const response = await fetch(`${pythonURI}/api/studylognew`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
            credentials: 'include',
        });
        if (response.ok) {
            formMessages.textContent = 'Study log added successfully!';
            formMessages.className = '';
            formMessages.classList.remove('hidden');
            loadStudyLogs();
        } else {
            formMessages.textContent = 'Failed to add study log.';
            formMessages.className = 'error';
            formMessages.classList.remove('hidden');
        }
    } catch (error) {
        formMessages.textContent = 'Error adding study log.';
        formMessages.className = 'error';
        formMessages.classList.remove('hidden');
    }
});
```

### **iii. Data Flow Explanation**
1. **User Interaction**: Users interact with the frontend to add, edit, or delete study logs.
2. **API Requests**: The frontend sends HTTP requests to the backend API endpoints.
3. **Database Operations**: The backend processes these requests, performing CRUD operations on the SQLite database.
4. **Response Handling**: The backend sends responses back to the frontend, which updates the UI accordingly.


<script src="https://utteranc.es/client.js"
        repo="armaghan-z.github.io/Armaghan_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>