
function assignedScore(score) {
    if (score >= 90) return "A grade";
    if (score >= 80) return "B grade";
    if (score >= 70) return "C grade";
    if (score >= 60) return "D grade";
    return "F grade";
}

function calculateGrade() {
    const score = parseInt(document.getElementById('scoreInput').value);
    const result = document.getElementById('result');

    if (isNaN(score) || score < 0 || score > 100) {
        result.textContent = "Enter a number between 0-100";
        result.className = "";
        return;
    }

    const grade = assignedScore(score);
    result.textContent = grade;
    result.className = `grade-${grade.charAt(0).toLowerCase()}`;
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('scoreInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') calculateGrade();
    });
});
