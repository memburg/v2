greeting_dom = document.getElementById("greeting_dom")
home_trigger = document.getElementById("home_trigger")
about_trigger = document.getElementById("about_trigger")
work_trigger = document.getElementById("work_trigger")
contact_trigger = document.getElementById("contact_trigger")
hours = new Date().getHours()

greet = ->
	if hours < 12
		greeting_dom.innerText = "good morning"
	else if hours < 17
		greeting_dom.innerText = "good afternoon"
	else
		greeting_dom.innerText = "good evening"

set_background = ->
	if hours < 12
		document.body.style.backgroundImage = "url('https://source.unsplash.com/1920x1080/daily?sand')"
	else if hours < 17
		document.body.style.backgroundImage = "url('https://source.unsplash.com/1920x1080/daily?castle')"
	else
		document.body.style.backgroundImage = "url('https://source.unsplash.com/1920x1080/daily?dark,nature')"

default_display = ->
	document.getElementById("home").style.display = "grid"
	document.getElementById("about").style.display = "none"
	document.getElementById("work").style.display = "none"
	document.getElementById("contact").style.display = "none"

show_home = (event) ->
	document.getElementById("home").style.display = "grid"
	document.getElementById("about").style.display = "none"
	document.getElementById("work").style.display = "none"
	document.getElementById("contact").style.display = "none"

show_about = (event) ->
	document.getElementById("home").style.display = "none"
	document.getElementById("about").style.display = "grid"
	document.getElementById("work").style.display = "none"
	document.getElementById("contact").style.display = "none"

show_work = (event) ->
	document.getElementById("home").style.display = "none"
	document.getElementById("about").style.display = "none"
	document.getElementById("work").style.display = "grid"
	document.getElementById("contact").style.display = "none"

show_contact = (event) ->
	document.getElementById("home").style.display = "none"
	document.getElementById("about").style.display = "none"
	document.getElementById("work").style.display = "none"
	document.getElementById("contact").style.display = "grid"

set_background()
default_display()
home_trigger.addEventListener("click", show_home)
about_trigger.addEventListener("click", show_about)
work_trigger.addEventListener("click", show_work)
contact_trigger.addEventListener("click", show_contact)
greet()
