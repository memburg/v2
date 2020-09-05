from browser import document
from javascript import Date

# DOM objects
greeting_dom = document["greeting_dom"]

# Pages
home_page = document["home"]
about_page = document["about"]
work_page = document["work"]
contact_page = document["contact"]

# Triggers are buttons in side/bottom bar (depending the screen size)
home_trigger = document["home_trigger"]
about_trigger = document["about_trigger"]
work_trigger = document["work_trigger"]
contact_trigger = document["contact_trigger"]

# CONSTANTS
CURRENT_HOURS = int(Date().split()[4].split(':')[0])

def greet():
    if CURRENT_HOURS < 12:
		greeting_dom.innerText = "good morning"
    elif CURRENT_HOURS < 17:
		greeting_dom.innerText = "good afternoon"
    else:
		greeting_dom.innerText = "good evening"

def set_background():
    # Background is set based on the hours of the day and the image is taken
    # from «unsplash.com», this function is suposed to show a different image
    # everyday and depending the hour.
    background_url = "url('https://source.unsplash.com/1920x1080/daily?#')"

    if CURRENT_HOURS < 12:
        document.body.style.backgroundImage = background_url.replace("#", "sand")
    elif CURRENT_HOURS < 17:
        document.body.style.backgroundImage = background_url.replace("#", "sunset")
    else:
        document.body.style.backgroundImage = background_url.replace("#", "dark,nature")

def default_display():
    home_page.style.display  = "grid"
    about_page.style.display = "none"
    work_page.style.display  = "none"
    contact_page.style.display = "none"

def show_home(event):
    home_page.style.display = "grid"
    about_page.style.display = "none"
    work_page.style.display = "none"
    contact_page.style.display = "none"

def show_about(event):
    home_page.style.display = "none"
    about_page.style.display = "grid"
    work_page.style.display = "none"
    contact_page.style.display = "none"

def show_work(event):
    home_page.style.display = "none"
    about_page.style.display = "none"
    work_page.style.display = "grid"
    contact_page.style.display = "none"

def show_contact(event):
    home_page.style.display = "none"
    about_page.style.display = "none"
    work_page.style.display = "none"
    contact_page.style.display = "grid"

def main():
    default_display()
    set_background()

    home_trigger.bind("click", show_home)
    about_trigger.bind("click", show_about)
    work_trigger.bind("click", show_work)
    contact_trigger.bind("click", show_contact)

    greet()

if __name__ == "__main__":
    main()