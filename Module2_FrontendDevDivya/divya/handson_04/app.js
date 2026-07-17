// =========================
// TASK 1 - PROMISES & ASYNC/AWAIT
// =========================

function fetchUser(id) {

    fetch(`https://jsonplaceholder.typicode.com/users/${id}`)

        .then(response => response.json())

        .then(data => {
            console.log("User Name (.then):", data.name);
        })

        .catch(error => {
            console.log(error);
        });
}

fetchUser(1);


// Async/Await Version

async function fetchUserAsync(id) {

    try {

        const response = await fetch(
            `https://jsonplaceholder.typicode.com/users/${id}`
        );

        const data = await response.json();

        console.log("User Name (async):", data.name);

    }

    catch (error) {
        console.log(error);
    }
}

fetchUserAsync(2);


// =========================
// LOCAL COURSES DATA
// =========================

const courses = [

    {
        id: 1,
        name: "Data Structures",
        credits: 4
    },

    {
        id: 2,
        name: "DBMS",
        credits: 3
    },

    {
        id: 3,
        name: "Web Development",
        credits: 4
    },

    {
        id: 4,
        name: "Python",
        credits: 4
    },

    {
        id: 5,
        name: "Artificial Intelligence",
        credits: 3
    }

];


// Simulated Network Delay

function fetchAllCourses() {

    return new Promise(resolve => {

        setTimeout(() => {

            resolve(courses);

        }, 1000);

    });

}

fetchAllCourses()

    .then(data => {

        console.log("Courses Loaded:", data);

    });


// =========================
// PROMISE.ALL()
// =========================

Promise.all([

    fetch(
        'https://jsonplaceholder.typicode.com/users/1'
    ).then(res => res.json()),

    fetch(
        'https://jsonplaceholder.typicode.com/users/2'
    ).then(res => res.json())

])

.then(users => {

    console.log("User 1:", users[0].name);
    console.log("User 2:", users[1].name);

})

.catch(error => {

    console.log(error);

});


// =========================
// TASK 2 - FETCH API
// =========================

const loading =
    document.getElementById('loading');

const notifications =
    document.getElementById('notifications');

const errorDiv =
    document.getElementById('error');

const retryBtn =
    document.getElementById('retryBtn');


// Reusable Fetch Function

async function apiFetch(url) {

    const response = await fetch(url);

    if (!response.ok) {

        throw new Error(
            `HTTP Error ${response.status}`
        );
    }

    return response.json();
}


// Load Notifications

async function loadNotifications() {

    try {

        loading.style.display = 'block';

        errorDiv.innerHTML = '';

        retryBtn.style.display = 'none';

        notifications.innerHTML = '';

        // CHANGE THIS TO invalidurl TO TEST ERROR HANDLING

        const posts = await apiFetch(
            'https://jsonplaceholder.typicode.com/posts?_limit=10'
        );

        loading.style.display = 'none';

        posts.forEach(post => {

            const card =
                document.createElement('div');

            card.className =
                'notification-card';

            card.innerHTML = `

                <h3>${post.title}</h3>

                <p>${post.body}</p>

            `;

            notifications.appendChild(card);

        });

    }

    catch (error) {

        loading.style.display = 'none';

        errorDiv.innerHTML =
            `Failed to load data: ${error.message}`;

        retryBtn.style.display = 'block';

        console.error(error);
    }
}


// Initial Load

loadNotifications();


// Retry Button

retryBtn.addEventListener(
    'click',
    loadNotifications
);


// =========================
// TASK 3 - AXIOS
// =========================


// Axios Interceptor

axios.interceptors.request.use(

    config => {

        console.log(
            `API Call Started: ${config.url}`
        );

        return config;
    }

);


// Axios Request

async function loadUserPosts() {

    try {

        const response = await axios.get(

            'https://jsonplaceholder.typicode.com/posts',

            {
                params: {
                    userId: 1
                }
            }

        );

        console.log(
            "Axios Posts:",
            response.data
        );

    }

    catch (error) {

        console.log(error);

    }

}

loadUserPosts();

