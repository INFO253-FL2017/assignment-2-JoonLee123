var blogForm = document.getElementById("blog_comment");

blogForm.addEventListener("submit", function(event){
	
	var name_key = blogForm.elements.namedItem("name");
	var message_key = blogForm.elements.namedItem("message");

	var name = blogForm.elements.namedItem("name").value;
	var message = blogForm.elements.namedItem("message").value;
	
	localStorage.setItem(name_key, name);
	localStorage.setItem(message_key, message);


	var sendmessage = "Your message has been sent"

	var formDiv = document.getElementById("commentResult");
	
	formDiv.classList.remove("error");
	formDiv.classList.remove("send");
	

	if(name.length == 0 & message.length == 0){
		
		formDiv.innerHTML = "Fields need to be filled out";
	} else if(name.length == 0 & message.length != 0){
		
		formDiv.innerHTML = "Name field needs to be filled out";
	} else if(name.length != 0 & message.length == 0){
		
		formDiv.innerHTML = "Message field needs to be filled out";
	} else {
		formDiv.innerHTML = sendmessage
	}


	if(formDiv.innerHTML != sendmessage){
		formDiv.classList.add("error");
	}
	if(formDiv.innerHTML == sendmessage){
		formDiv.classList.add("send");
	}



	event.preventDefault();

});

