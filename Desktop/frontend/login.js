
// Get login form by the id of the form 
let form = document.getElementById('login-form')

// Event listener for when a form is submitted 
// When a form is submitted: Send a request and the page is refreshed here
form.addEventListener('submit', (e) => {
    e.preventDefault() // Prevents default action of page refreshing: Page does not refresh after submitting action (we handle everything ourselves now )

    // Pull out all info from form to perform an action of sendin it to the backend
    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }

    // Form data is sent to backend (below URL) with a POST request
    fetch('http://127.0.0.1:8000/api/users/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('DATA:', data.access)
            if (data.access) {
                localStorage.setItem('token', data.access)
                window.location = 'file:///Users/charrellsherman/Desktop/frontend/project-list.html'
            } else {
                alert('Username OR password did not work')
            }
        })
})

// 12:35 Storing JSON web tokens

// Fill out the form, add an event listener that listens to this for  -->
// When we submit the form, we take the formData and send it to the API endpoint (URL)
// We pass that data into the body and get a response  