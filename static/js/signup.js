var full_name = document.getElementById("name");
var date_of_birth = document.getElementById("date_of_birth");
var nationality = document.getElementById("nationality");
var phone = document.getElementById("phone");
var add1 = document.getElementById("add1");
var add2 = document.getElementById("add2");
var city = document.getElementById("city");
var state = document.getElementById("state");
var country = document.getElementById("country");
var pin = document.getElementById("pin");
var email = document.getElementById("mail");
var password = document.getElementById("pass");
var username = document.getElementById("usrname");

document.getElementById("form_submit").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the default form submission

  // Gather data into a JSON object
  var formData = {
    full_name: full_name.value,
    date_of_birth: date_of_birth.value,
    nationality: nationality.value,
    phone_number: phone.value,
    address_line_1: add1.value,
    address_line_2: add2.value,
    city: city.value,
    state: state.value,
    country: country.value,
    pin_code: pin.value,
    gender: "NA"
  };

  // Log the JSON object to the console
  console.log(JSON.stringify(formData));


});