let loginBtn = document.getElementById('login-btn') // Query to get login button
let logoutBtn = document.getElementById('logout-btn') // Query to get logout button

let token = localStorage.getItem('token')

// If we're logged in, get login button, if we're logged out, get the logout button
if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

// Event handler for the logout button
logoutBtn.addEventListener('click', (e) => {
    e.preventDefault() // Doesn't try to send the user somewhere
    localStorage.removeItem('token') //Remove token from local storage
    window.location = 'file:///Users/charrellsherman/Desktop/frontend/login.html' // Redirect user back to login page
})


// Making a request to this API/endpoint
let projectsUrl = 'http://127.0.0.1:8000/api/projects/'

// Make an API call
let getProjects = () => {
    // fetch is just sending a GET request
    fetch(projectsUrl) 
        // This is our promise first convert to json data
        // Then we return a nother promise that 
        .then(response => response.json())
        .then(data => {
            console.log(data)
            buildProjects(data)
        })

}

let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects--wrapper')
    projectsWrapper.innerHTML = '' //On each iteration we clear the projects and then load inprojects 

    for (let i = 0; projects.length > i; i++) {
        let project = projects[i]

        let projectCard = `
                <div class="project--card">
                    <img src="http://127.0.0.1:8000${project.featured_image}" />
                    
                    <div>
                        <div class="card--header">
                            <h3>${project.title}</h3>
                            <strong class="vote--option" data-vote="up" data-project="${project.id}" >&#43;</strong>
                            <strong class="vote--option" data-vote="down" data-project="${project.id}"  >&#8722;</strong>
                        </div>
                        <i>${project.vote_ratio}% Positive feedback </i>
                        <p>${project.description.substring(0, 150)}</p>
                    </div>
                
                </div>
        `
        projectsWrapper.innerHTML += projectCard
    }

    addVoteEvents()

    //Add an event listener (on click event that triggers a post request )
}

//Event arrow function in charge of adding event listeners to every single vote icon (gives a collection of HTML elements)
let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option') //query all vote buttons 

    //loop through all event buttons and add an event listener
    for (let i = 0; voteBtns.length > i; i++) {

        voteBtns[i].addEventListener('click', (e) => {
            let token = localStorage.getItem('token') // On each request, we go into local storage and get that token and pass on this request
            console.log('TOKEN:', token)
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            
            // Send a post request
            // Going into url and setting authorization 
            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({ 'value': vote }) // Sends the data and turns it into a string
            })
                .then(response => response.json()) // Promise that turns the response into JSON object
                .then(data => {
                    console.log('Success:', data) // Console the data 
                    getProjects()
                })

        })
    }
}

// Trigger function
getProjects()