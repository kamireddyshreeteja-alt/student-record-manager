let students = [];  // Array to store all student objects
let chart;          // To store Chart.js instance

function addStudent() {
    let name = document.getElementById("nameInput").value;
    let marks = Number(document.getElementById("marksInput").value);

    if (name === "" || marks === "") {
        alert("Please enter both name and marks");
        return;
    }

    let student = { name: name, marks: marks };
    students.push(student);

    // Display in list
    let li = document.createElement("li");
    li.textContent = name + " - " + marks + (marks >= 40 ? " (Pass)" : " (Fail)");
    li.className = marks >= 40 ? "pass" : "fail";
    document.getElementById("studentList").appendChild(li);

    document.getElementById("nameInput").value = "";
    document.getElementById("marksInput").value = "";

    updateChart(); // Update chart after adding student
}

function analyzeResults() {
    let total = students.length;
    let pass = students.filter(student => student.marks >= 40).length;
    let fail = total - pass;

    // Average marks
    let totalMarks = students.reduce((sum, s) => sum + s.marks, 0);
    let avg = total > 0 ? (totalMarks / total).toFixed(2) : 0;

    // Topper
    let topperStudent = students.reduce((top, s) => s.marks > (top.marks || 0) ? s : top, {});

    // Update HTML
    document.getElementById("totalStudents").textContent = "Total Students: " + total;
    document.getElementById("passCount").textContent = "Pass: " + pass;
    document.getElementById("failCount").textContent = "Fail: " + fail;
    document.getElementById("averageMarks").textContent = "Average Marks: " + avg;
    document.getElementById("topper").textContent = topperStudent.name ? "Topper: " + topperStudent.name + " (" + topperStudent.marks + ")" : "Topper: N/A";
}

// Function to create/update chart
function updateChart() {
    let ctx = document.getElementById('marksChart').getContext('2d');
    
    // Destroy previous chart if exists
    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: students.map(s => s.name),
            datasets: [{
                label: 'Marks',
                data: students.map(s => s.marks),
                backgroundColor: students.map(s => s.marks >= 40 ? 'green' : 'red')
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true, max: 100 }
            }
        }
    });
}
