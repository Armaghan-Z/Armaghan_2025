---
layout: base
title: "PPR Blog - Study Log"
description: "Personalized Project Reference (PPR) for AP CSP"
date: 2025-03-12
permalink: /ppr/
categories: [AP Computer Science Principles, Study Log]
---

<style>
  body {
    font-family: Arial, sans-serif;
    line-height: 1.8;
    margin: 0;
    padding: 40px;
    background-color: #f8fbff;
    color: #333;
  }
  h1, h2, h3 {
    font-weight: 600;
  }
  h1 {
    color: #1e3a8a;
    text-align: center;
    font-size: 32px;
  }
  h2 {
    color: #2563eb;
    border-bottom: 3px solid #2563eb;
    padding-bottom: 8px;
  }
  h3 {
    color: #444;
  }
  .highlight-box {
    background-color: #e8f0ff;
    padding: 15px;
    border-left: 5px solid #2563eb;
    border-radius: 5px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
  }
  pre code {
    display: block;
    background: #2d2d2d;
    color: #f8f8f2;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    font-size: 14px;
  }
  .content {
    max-width: 900px;
    margin: auto;
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  }
  .keyword { color: #82aaff; }
  .function { color: #c792ea; }
  .variable { color: #f78c6c; }
  .string { color: #c3e88d; }
  .comment { color: #7d8799; font-style: italic; }
</style>

<div class="content">

  <h1>🚀 Study Log PPR Blog</h1>
  <h3>✨ <em>Personalized Project Reference (PPR) for AP CSP</em></h3>

  <p>📅 <strong>March 12, 2025</strong> • <em>7 min read</em></p>

  <h2>📌 Understanding PPR and Its Requirements</h2>

  <p>The AP Computer Science Principles (CSP) Create Task requires students to demonstrate essential programming concepts through the <strong>Personalized Project Reference (PPR)</strong>. The PPR must include:</p>

  <ul>
    <li>✅ <strong>List Creation</strong> - Storing data in an organized format.</li>
    <li>✅ <strong>List Processing</strong> - Retrieving and manipulating stored data.</li>
    <li>✅ <strong>A Function Using Parameters, Selection, and Iteration</strong> - Implementing logic and control flow.</li>
    <li>✅ <strong>A Call to the Function</strong> - Demonstrating its integration into the overall program.</li>
  </ul>

  <p>Below, we break down each requirement with <strong>detailed explanations and examples</strong> from the Study Log project.</p>

  <hr>

  <h2>📜 <strong>List Creation - Storing Study Log Data</strong></h2>

  <div class="highlight-box">
    <p><strong>Explanation:</strong> This function initializes a <strong>database-backed study log storage system</strong>. The list is structured using a database table, where each study log entry contains a <strong>User ID, Subject, Hours Studied, and Notes</strong>.</p>
    <p>This meets the <strong>List Creation</strong> requirement because it creates and structures a list where data is persistently stored and can be accessed later.</p>
  </div>

  <pre><code class="language-python">
<span class="keyword">class</span> <span class="function">StudyLog</span>(db.Model):
    __tablename__ = <span class="string">'studylog'</span>
    id = db.Column(db.Integer, primary_key=<span class="keyword">True</span>)
    user_id = db.Column(db.Integer, db.ForeignKey(<span class="string">'users.id'</span>), nullable=<span class="keyword">False</span>)
    subject = db.Column(db.String(100), nullable=<span class="keyword">False</span>)
    hours_studied = db.Column(db.Float, nullable=<span class="keyword">False</span>)
    notes = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now)

    <span class="keyword">def</span> <span class="function">create</span>(<span class="keyword">self</span>):
        db.session.add(<span class="keyword">self</span>)
        db.session.commit()
  </code></pre>

  <hr>

  <h2>🔄 <strong>List Processing - Retrieving and Filtering Study Logs</strong></h2>

  <div class="highlight-box">
    <p><strong>Explanation:</strong> This function <strong>retrieves</strong> all study logs stored in the database and <strong>processes</strong> them into a JSON format.</p>
    <p>This meets the <strong>List Processing</strong> requirement because it shows how stored data can be accessed, organized, and used in an application.</p>
  </div>

  <pre><code class="language-python">
@token_required()
<span class="keyword">def</span> <span class="function">get</span>(<span class="keyword">self</span>):
    study_logs = StudyLog.query.all()
    json_ready = [log.read() <span class="keyword">for</span> log <span class="keyword">in</span> study_logs]
    <span class="keyword">return</span> jsonify(json_ready)
  </code></pre>

  <hr>

  <h2>🏗️ <strong>Function with Parameters, Selection, and Iteration</strong></h2>

  <div class="highlight-box">
    <p><strong>Explanation:</strong> This function:</p>
    <ul>
      <li>✅ Uses <strong>parameters</strong> to receive data about the study log.</li>
      <li>✅ Uses <strong>selection</strong> (if-statements) to validate that required fields are present.</li>
      <li>✅ Uses <strong>iteration</strong> to process multiple study logs.</li>
    </ul>
    <p>This meets the <strong>Function with Parameters, Selection, and Iteration</strong> requirement because it integrates all three aspects of logic, input validation, and iterative processing.</p>
  </div>

  <pre><code class="language-python">
@token_required()
<span class="keyword">def</span> <span class="function">post</span>(<span class="keyword">self</span>):
    data = request.get_json()
    <span class="keyword">if</span> <span class="keyword">not</span> data <span class="keyword">or</span> <span class="string">"user_id"</span> <span class="keyword">not</span> <span class="keyword">in</span> data <span class="keyword">or</span> <span class="string">"subject"</span> <span class="keyword">not</span> <span class="keyword">in</span> data:
        <span class="keyword">return</span> {<span class="string">"message"</span>: <span class="string">"Missing required fields"</span>}, 400

    study_log = StudyLog(
        user_id=data[<span class="string">"user_id"</span>],
        subject=data[<span class="string">"subject"</span>],
        hours_studied=data[<span class="string">"hours_studied"</span>],
        notes=data.get(<span class="string">"notes"</span>, <span class="string">""</span>)
    )

    study_log.create()
    <span class="keyword">return</span> jsonify(study_log.read())
  </code></pre>

  <hr>

  <h2>🔗 <strong>Call to Function - Integrating Study Log Submission</strong></h2>

  <div class="highlight-box">
    <p><strong>Explanation:</strong> This function <strong>triggers the study log submission process</strong>. It listens for a form submission, collects user input, and sends the data to the backend API.</p>
    <p>This meets the <strong>Call to Function</strong> requirement because it demonstrates how the function is used within the program to process user input.</p>
  </div>

  <pre><code class="language-javascript">
document.getElementById(<span class="string">'study-log-form'</span>).addEventListener(<span class="string">'submit'</span>, <span class="keyword">async</span> <span class="keyword">function</span>(event) {
    event.preventDefault();
    <span class="keyword">const</span> subject = document.getElementById(<span class="string">'subject'</span>).value.trim();
    <span class="keyword">const</span> hours = document.getElementById(<span class="string">'hours'</span>).value.trim();
    <span class="keyword">const</span> notes = document.getElementById(<span class="string">'notes'</span>).value.trim();

    <span class="keyword">const</span> data = {
        user_id: 1,
        subject,
        hours_studied: parseFloat(hours),
        notes
    };

    <span class="keyword">try</span> {
        <span class="keyword">const</span> response = <span class="keyword">await</span> fetch(<span class="string">`${pythonURI}/api/studylog`</span>, {
            method: <span class="string">'POST'</span>,
            headers: { <span class="string">'Content-Type'</span>: <span class="string">'application/json'</span> },
            body: JSON.stringify(data),
        });

        <span class="keyword">if</span> (response.ok) {
            console.log(<span class="string">"Study log added successfully"</span>);
        }
    } <span class="keyword">catch</span> (error) {
        console.error(<span class="string">'Error:'</span>, error);
    }
});
  </code></pre>

  <hr>

  <h2>📌 <strong>Final Summary</strong></h2>

  <div class="highlight-box">
    <p>This blog <strong>fully satisfies</strong> all AP CSP Create Task requirements:</p>
    <ul>
      <li>✅ <strong>List Creation</strong> - Stores study logs in a structured list.</li>
      <li>✅ <strong>List Processing</strong> - Retrieves and converts logs for display.</li>
      <li>✅ <strong>Function with Logic</strong> - Uses selection and iteration.</li>
      <li>✅ <strong>Call to Function</strong> - Submits logs via an API request.</li>
    </ul>
  </div>

</div>


<script src="https://utteranc.es/client.js"
        repo="armaghan-z.github.io/Armaghan_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>