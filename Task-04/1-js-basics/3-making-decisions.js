let allStudents = [
    'A',
    'B-',
    1,
    4,
    5,
    2
];

let studentsWhoPass = [];

for (let i = 0; i < allStudents.length; i++) {
    let grade = allStudents[i];
    
    // First grading system: numbers 1-5, pass if 3 or higher
    if (typeof grade == 'number') {
        if (grade >= 3) {
            studentsWhoPass.push(grade);
        }
    }
    // Second grading system: letters, pass if A, A-, B, B-, or C
    else if (typeof grade == 'string') {
        if ((grade == 'A') || (grade == 'A-') || (grade == 'B') || (grade == 'B-') || (grade == 'C')) {
            studentsWhoPass.push(grade);
        }
    }
}

console.log("All students:", allStudents);
console.log("Students who pass:", studentsWhoPass);