---
layout: page
title: My Sprint 5
permalink: /sprint5/
---

# **Individual Feature Documentation: Study Log**

Below is a concise but robust documentation of the **Study Log** feature, meeting AP Computer Science Principles Create Task requirements. This blog highlights purpose, implementation, and demonstrations of input/output, database interaction, and core algorithms used in the Study Log feature.

---

## **1. Purpose**

| Aspect                | Description                                                                                                                                    |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Group Program**     | Provides multiple academic tracking tools (e.g., grade logger, study logger) to help students monitor their academic progress in one place.    |
| **My Feature Focus**  | **Study Log** allows users to create, read, update, and delete study records. It helps students track daily study hours, subjects, and notes.   |

---

## **2. Input/Output Requests**

| I/O Mechanism                  | Description                                                                               |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Frontend Form**              | • **Subject**<br/>• **Hours Studied**<br/>• **Notes** (optional)                         |
| **API Endpoints**              | • **GET** `/api/studylognew`<br/>• **POST** `/api/studylognew`<br/>• **PUT** `/api/studylognew`<br/>• **DELETE** `/api/studylognew` |
| **Database**                   | SQLite (via SQLAlchemy). Stores logs in a `studylog` table.                                |
| **Output**                     | JSON data containing study log records.                                                   |

<img src="/Armaghan_2025/assets/Images/input1.png" width="600" height="450" />


### **2.1 Frontend Demo**

- **Add New Log**  
  Users fill out the form and submit:

  ```javascript
  fetch('http://127.0.0.1:8887/api/studylognew', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      user_id: 1,
      subject: subject,
      hours_studied: parseFloat(hours),
      notes: notes
    }),
    credentials: 'include',
  });
  ```

- **Display Logs**  
  On success, logs are displayed in the DOM using JavaScript.

  **On success, logs are displayed in the DOM using JavaScript.**

<br/>

<img src="/Armaghan_2025/assets/Images/form1.png" width="600" height="450" />

### **2.2 Postman Demo**

- **POST**:

  ```json
  POST /api/studylognew
  {
    "user_id": 1,
    "subject": "Math",
    "hours_studied": 2.0,
    "notes": "Algebra practice"
  }
  ```

- **Response**:

  ```json
  {
    "id": 101,
    "user_id": 1,
    "subject": "Math",
    "hours_studied": 2.0,
    "notes": "Algebra practice",
    "date": "2025-01-27 14:00:00"
  }
  ```

- **Error (missing field)**:

  ```json
  {
    "message": "Subject is required"
  }
  ```

<img src="/Armaghan_2025/assets/Images/post1.png" width="600" height="450" />

### **2.3 DB Backup/Restore**

- Executed via custom CLI commands:
  - `./scripts/db_backup.py`
  <img src="/Armaghan_2025/assets/Images/post1.png" width="600" height="450" />

  - `./scripts/db_init.py`
    <img src="/Armaghan_2025/assets/Images/init1.png" width="600" height="450" />

  - `./scripts/db_restore.py`
      <img src="/Armaghan_2025/assets/Images/restore1.png" width="600" height="450" />

- Backs up all table rows (lists) as JSON and restores them when needed.

---

## **3. Data and List/Dictionaries**

| **List (Rows)**         | The `get()` method calls `StudyLog.query.all()` to retrieve all `StudyLog` records from the database as rows. Each row is converted into a dictionary via `log.read()` and then appended to a list (`studylogs`). |
| **Dictionary (Columns)**| Each `StudyLog` object’s `read()` method returns a dictionary with keys like `id`, `user_id`, `subject`, `hours_studied`, `notes`, and `date`. |
| **JSON Formatting**     | Finally, the list of dictionaries is wrapped in `jsonify(studylogs)`, returning the data to the client in valid JSON format. |

```python
# GET: Read all study logs from the database
    @token_required()
    def get(self):
        # Query all StudyLog records from database
        all_studylogs = StudyLog.query.all()
        # Prepare a list to hold each study log's data
        studylogs = []
        for log in all_studylogs:
            # Convert the study log object into a dictionary
            studylogs.append(log.read())
        # Return all study logs as JSON
        return jsonify(studylogs)
```

---

## **4. Algorithmic Code: API Methods**

Below is an example **POST** method, showing sequencing, selection, and iteration.

```python
@token_required()
def post(self):
    # SEQUENCING: Steps to process the request
    data = request.get_json()
    if not data:  # SELECTION: Checking for valid input
        return {'message': 'No input data provided'}, 400

    user_id = data.get('user_id')
    subject = data.get('subject')
    hours_studied = data.get('hours_studied')
    notes = data.get('notes')

    # Additional validations...
    if not user_id:
        return {'message': 'User ID is required'}, 400

    # CREATE: Construct object
    studylog = StudyLog(user_id, subject, hours_studied, notes)
    studylog.create()

    return jsonify(studylog.read())
```

- **Parameters**: Receives JSON body with `user_id`, `subject`, `hours_studied`, and `notes`.  
- **Return Type**: `jsonify` object containing the newly created study log (or error).

### **4.1 Calling the API (Frontend Fetch)**

```javascript
async function addStudyLog(subject, hours, notes) {
  const response = await fetch('http://127.0.0.1:8887/api/studylognew', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      user_id: 1,
      subject,
      hours_studied: parseFloat(hours),
      notes
    }),
    credentials: 'include',
  });

  if (response.ok) {
    const data = await response.json();
    console.log("New log added:", data);
  } else {
    const errMsg = await response.json();
    console.error("Error adding study log:", errMsg);
  }
}
```

- **Normal Condition**: 200 status + JSON data of the new log.  
- **Error Condition**: 4xx/5xx status + JSON error message.

---

## **5. Observations & Reflections**

1. **Collaboration**: Features integrated with other group modules (e.g., Grade Log) for a cohesive academic tracker.  
2. **Data Integrity**: Validation ensures each field is provided; errors returned as JSON.  
3. **Scalability**: RESTful design + SQLAlchemy facilitates robust, scalable data operations.  
4. **Future Enhancements**: Pagination for large logs, user-specific log filters.

---

## **6. Conclusion**

- **Achievement**: This feature meets the AP CSP Create Task guidelines by showing **purpose**, **input/output** methods, **data structures** (lists/dicts), and **algorithmic** logic.
- **Code Reusability**: Well-structured classes and methods (CRUD) make the Study Log extensible to other academic-tracking features.

> **Reference**: [AP Computer Science Principles Course and Exam Description](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-course-and-exam-description.pdf)

---

_This blog post demonstrates how the Study Log feature was designed, how it processes data, and how it aligns with the AP CSP requirements for creating and documenting software._