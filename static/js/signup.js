
    document.getElementById("form_btn").addEventListener("click", function(e) {
        e.preventDefault(); // Prevent the default form submission

        console.log("Form submitted"); // Debugging line

        // // Capture form data
        // const fullName = form.querySelector('input[placeholder="Enter your name"]').value;
        // const dob = form.querySelector('input[type="date"]').value;
        // const nationality = form.querySelector('input[placeholder="Enter nationality"]').value;
        // const phoneNumber = form.querySelector('input[placeholder="Enter your number"]').value;
        // const addressLine1 = form.querySelector('input[placeholder="Line 1"]').value;
        // const addressLine2 = form.querySelector('input[placeholder="Line 2"]').value;
        // const city = form.querySelector('input[placeholder="City Name"]').value;
        // const state = form.querySelector('input[placeholder="State"]').value;
        // const country = form.querySelector('input[placeholder="Country"]').value;
        // const pinCode = form.querySelector('input[placeholder="Pin"]').value;
        // const email = form.querySelector('input[name="email"]').value;
        // const password = form.querySelector('input[name="password"]').value;
        // const confirmPassword = form.querySelector('input[placeholder="Confirm your password"]').value;
        // const gender = form.querySelector('input[name="gender"]:checked') ? form.querySelector('input[name="gender"]:checked').nextElementSibling.innerText : '';

        // // Create JSON object
        // const userData = {
        //     fullName,
        //     dob,
        //     nationality,
        //     phoneNumber,
        //     addressLine1,
        //     addressLine2,
        //     city,
        //     state,
        //     country,
        //     pinCode,
        //     email,
        //     password,
        //     confirmPassword,
        //     gender
        // };

        // // Print data for debugging
        // console.log('User Data:', userData);

        // // Call the API
        // fetch('/api/register', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify(userData)
        // })
        // .then(response => response.json())
        // .then(data => {
        //     console.log('Success:', data);
        //     // Handle success (e.g., redirect or show a success message)
        // })
        // .catch((error) => {
        //     console.error('Error:', error);
        //     // Handle error (e.g., show an error message)
        // });
    });

