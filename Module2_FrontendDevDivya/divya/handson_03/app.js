import { courses } from './data.js';

let currentCourses = [...courses];

const grid = document.querySelector('.course-grid');
const searchBox = document.getElementById('search-courses');
const sortBtn = document.getElementById('sortBtn');
const totalCredits = document.getElementById('total-credits');
const selectedCourse = document.getElementById('selected-course');
const courseCount = document.getElementById('course-count');


// ES6 MAP

const courseStrings = courses.map(
course =>
`${course.code} - ${course.name} (${course.credits} credits)`
);

console.log(courseStrings);


// ES6 FILTER

const filteredCredits =
courses.filter(course => course.credits >= 4);

console.log(
"Courses with credits >= 4:",
filteredCredits.length
);


// ES6 REDUCE

const total =
courses.reduce(
(sum,course)=>sum+course.credits,
0
);

console.log("Total Credits:",total);


// Render Function

function render(data){

grid.innerHTML='';

data.forEach(course=>{

const article =
document.createElement('article');

article.className='course-card';

article.dataset.id=course.id;

article.innerHTML=`

<h3>${course.name}</h3>

<p>
Course Code:
${course.code}
</p>

<p>
Credits:
${course.credits}
</p>

`;

grid.appendChild(article);

});

courseCount.textContent =
`${data.length} Courses Found`;

}


// Initial Render

render(currentCourses);


// Total Credits Display

totalCredits.textContent =
`Total Credits: ${total}`;



// Search Functionality

searchBox.addEventListener('input',e=>{

const value =
e.target.value.toLowerCase();

const filtered =
courses.filter(course=>
course.name
.toLowerCase()
.includes(value)
);

currentCourses = filtered;

render(filtered);

});



// Sort by Credits

sortBtn.addEventListener('click',()=>{

currentCourses.sort(
(a,b)=>b.credits-a.credits
);

render(currentCourses);

});



// Event Delegation

grid.addEventListener('click',event=>{

const card =
event.target.closest('.course-card');

if(!card) return;

const id =
parseInt(card.dataset.id);

const course =
courses.find(c=>c.id===id);

selectedCourse.innerHTML = `

<h3>Selected Course</h3>

<p>
Name:
${course.name}
</p>

<p>
Grade:
${course.grade}
</p>

`;

});