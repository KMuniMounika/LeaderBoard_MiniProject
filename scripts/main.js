document.addEventListener('DOMContentLoaded', () => {
    const studentForm = document.getElementById('studentForm');
    const assessmentForm = document.getElementById('assessmentForm');
    const resultForm = document.getElementById('resultForm');
    const leaderboardTable = document.getElementById('leaderboardTable') ? document.getElementById('leaderboardTable').getElementsByTagName('tbody')[0] : null;

    // Placeholder arrays to store data
    const students = [];
    const assessments = [];
    const results = [];

    // Handle student registration form submission
    if (studentForm) {
        studentForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const studentData = {
                id: students.length + 1,
                name: studentForm.name.value,
                rollNumber: studentForm.rollNumber.value,
                dateOfBirth: studentForm.dateOfBirth.value,
                gender: studentForm.gender.value,
                email: studentForm.email.value,
                phone: studentForm.phone.value,
                address: studentForm.address.value,
                dateOfJoining: studentForm.dateOfJoining.value,
                status: studentForm.status.value
            };
            students.push(studentData);
            studentForm.reset();
            console.log('Student registered:', studentData);
        });
    }

    // Handle assessment creation form submission
    if (assessmentForm) {
        assessmentForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const assessmentData = {
                id: assessments.length + 1,
                name: assessmentForm.assessmentName.value,
                totalMarks: assessmentForm.totalMarks.value,
                passingMarks: assessmentForm.passingMarks.value,
                dateCreated: assessmentForm.dateCreated.value,
                dateScheduled: assessmentForm.dateScheduled.value,
                duration: assessmentForm.duration.value
            };
            assessments.push(assessmentData);
            assessmentForm.reset();
            console.log('Assessment created:', assessmentData);
        });
    }

    // Handle result update form submission
    if (resultForm) {
        resultForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const resultData = {
                id: results.length + 1,
                rollNumber: resultForm.rollNumberResult.value,
                assessmentName: resultForm.assessmentNameResult.value,
                score: resultForm.score.value
            };
            results.push(resultData);
            resultForm.reset();
            console.log('Result updated:', resultData);
            updateLeaderboard();
        });
    }

    // Function to update the leaderboard
    function updateLeaderboard() {
        if (!leaderboardTable) return;

        // Clear the current leaderboard
        leaderboardTable.innerHTML = '';

        // Sort results by score (descending)
        const sortedResults = [...results].sort((a, b) => b.score - a.score);

        // Update the leaderboard table
        sortedResults.forEach((result, index) => {
            const student = students.find(s => s.rollNumber === result.rollNumber);
            const assessment = assessments.find(a => a.name === result.assessmentName);
            if (student && assessment) {
                const row = leaderboardTable.insertRow();
                row.insertCell(0).innerText = index + 1; // Rank
                row.insertCell(1).innerText = student.name; // Student Name
                row.insertCell(2).innerText = student.rollNumber; // Roll Number
                row.insertCell(3).innerText = ((result.score / assessment.totalMarks) * 100).toFixed(2) + '%'; // Percentage
                row.insertCell(4).innerText = result.score; // Secured Marks
                row.insertCell(5).innerText = assessment.totalMarks; // Total Marks
            }
        });
    }
});
