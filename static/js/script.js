var notification = document.getElementById("notification");

var contactForm = document.getElementById("form_contact");
contactForm.addEventListener("submit", function(event) {
	var name = document.getElementById("name").value;
	var email = document.getElementById("email").value;
	var subject = document.getElementById("subject").value;
	var message = document.getElementById("message").value;



	var notification = document.getElementById("notification");
	while(notification.hasChildNodes())
		notification.removeChild(notification.lastChild);
	var form_result = document.createElement("form_result");

	notification.appendChild(form_result);
	form_result.classList.remove("error");
	if (!name){
		
		form_result.innerHTML += "Name field needs to be filled out";
	}
	if (!email){
		if(form_result.innerHTML)
			form_result.appendChild(document.createElement("br"));
		form_result.innerHTML += "E-mail field needs to be filled out";
	}
	if (!subject){
		if(form_result.innerHTML)
			form_result.appendChild(document.createElement("br"));
		form_result.innerHTML += "Subject field needs to be filled out";
	}
	if (!message){
		if(form_result.innerHTML)
			form_result.appendChild(document.createElement("br"));
		form_result.innerHTML += "Message field needs to be filled out";
	}
	
	if (name && email && subject && message){
	
		form_result.innerHTML += "Hi " + name + ", your message has been sent";
		
	} else{
		form_result.classList.add("error");
		event.preventDefault();
	}
})