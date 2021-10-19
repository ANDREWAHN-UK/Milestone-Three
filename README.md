# MILESTONE PROJECT THREE
![image](https://i.imgur.com/XCHBmiZ.jpg)
 - - - -

**1. Purpose of the project:**
 - - - -


When I was living in Spain, I ran an [Airbnb](https://www.airbnb.co.uk/rooms/18222301), which is still in operation. Naturally I now use agents to run it. Airbnb has a feature called [Guide Books](https://www.airbnb.co.uk/s/guidebooks?refinement_paths[]=/guidebooks/134487) , which is something the host can upload, as an adjunct to the listing. When I set up the listing, I started the guidebook, but quickly realised that to do it well would be extremely time intensive, especially considering that the area in question, if one considers just the beach, is 3 miles long. That means very many restaurants, bars etc.

 I had the onerous task of trying most of them. 

With Milestone Project 3, it seemed a natural idea to ask the guests to register on this review site (along with friends still there) and leave reviews, for future guests. In other words, a version of [Trip Advisor](https://www.tripadvisor.co.uk/) made by guests, for guests, that other people can view.

Limiting the scope like this has the advantages of users being already interested (As it sparks good memories of their stay or gives them ideas for future stays) and also makes my job as a host considerably easier, as approximately one in three guests asks for a place to eat or drink. By default, I recommend the closest (very good) [Italian restaurant](https://ristorantepiemonte.com/) but being able to present them with a semi-curated and useful guide would uplift their experience.
It is potentially good advertising for the listing in question, which has in excess of 100 very positive reviews.


- - - - 
**2. User Goals/stories**
 - - - -

 * As a **Potential Employer** for a Coding Role, I want to view Andrew’s website, to see how he performs as a Full stack developer. I want to be able to navigate the website and compare it to others, of similar scope.
* As a **Potential Employer** for a Coding Role, further to the above, I would be particularly interested in the use of Python and Flask in this website.
* As a **Potential new visitor** to Las Palmas, specifically this Airbnb listing, I want to be able to read reviews, so I can decide where to go eat/drink
* As a **returning visitor** I want to see what is new, to inform future visits.
* As a **previous visitor who has patronised the area** I want to be able to create, update and delete my own reviews, so as ensure other people are aware of the good and perhaps not so good establishments.
* As a **resident of the area** I want to be able to create, update and delete my own reviews, so as ensure other people are aware of the good and perhaps not so good establishments.
* As an **adminstrator of the website** I want to be able to update and delete other peoples' reviews and profiles.

 - - - - 
**3. Stakeholder Goals**
 - - - -

 * To lead the user to create a profile 
 * To lead the user to read and leave reviews.

- - - - 
**4. Typography and colour scheme:**
 - - - -
*	Font - Lato. For the simple reason that it worked well.
*	Icons - very few icons were used here. I used font awesome for the icons.
*	Colours – I want to emphasise Las Canteras beach, which means lots of sea and beach and sun related colours, and the national colours of the island are yellow, blue, and white. This review site is meant to complement an existing Airbnb listing, which has been decorated in …yellow, blue and white.
*	Images – I sourced the images from google images, Unsplash and the official [Las Canteras beach website](https://www.hellocanaryislands.com/beaches/gran-canaria/las-canteras-beach/), as well as my own images.

 - - - - 
**5. Features:**
 - - - -
* Feature - Header/Navbar basic - to consist of links to the home page, reviews page, about page (a link to the Airbnb listing,) log in/register page (replaced by a log out link once the user is logged in) and user profile (shows once a user is logged in) 

Because this website is intended to be quite fun in its theming, the navbar is not at the top as is traditional, but comes in from the left, when the top left circle is clicked. This was intended as a bit of whimsy, and also to allow maximum use of the screen for beach themed images.
* Feature - Navbar plus – log out button to replace login/register, link to Profile Page, link to New Review 
* Page - Homepage – with search functionality, clear images about Las Canteras, and some links to reviews page, about page (a link to the Airbnb listing,) log in/register page.
* Page - create and edit review page
* Page - Log In / Registration Page – to register a user (updating the database) or log them in (checking the database)
* Page - User Profile Page – available once user logs in. This is where users can manipulate their data.
* Function – Create User
* Function – Create Review
* Function – Read Review
* Function – Update Review
* Function – Delete Review
* Minimal Viable Project is :
    * Navbar basic
    * Homepage
    * Registration/ Log in page
    * User profile Page (once logged in)
    * Reviews page (i.e. view all reviews)
    * Create User function
    * (Create /Read /Update/ Delete) own Reviews function
    * Admin to be able to modify all reviews
* Future features/expanding the website :
    * This review focussed website could form part of a larger website, intended to highlight the Airbnb listing itself, similar to how the neighbouring building has a [website](https://www.brisamarcanteras.com/) but lists everything through booking.com
    * The scope could expand to include places further from the beach
    * The scope could expand to include events, such as concerts
    * The website couyld be made available in other languages, such as German, Spanish or Russian, in order to better accomodate the variety of visitors and residents
    * The scope could be linked to another organisation
    * It would be very useful for users to pin the lkocation on a map, and/or, like with Trip Advisor, have the address of the place to hand
    * Relating to this last, it could be useful for each place to have its own mini page, like a modal, with reviews by various users linked to it
    * The ability for usersto upload their own images, and several of them, would be nice, and have these in a carousel within the review itself
    * A more fleshed out User Profile page, with the ability to edit it, and for others to be able to view it, in effect a very small, highly curated version of Facebook, focussed on the beach 



- - - - 
**6. Wireframes:**
- - - -
The wireframes can be accessed from the "wireframes" folder, and also directly here:

 [Wireframes file](https://github.com/ANDREWAHN-UK/Milestone-Three/blob/main/MS3.bmpr)

 [Wireframes PDF](https://github.com/ANDREWAHN-UK/Milestone-Three/blob/main/MS3.pdf)

- - - - 
 **7. Technology.**
- - - -
Languages Used:
 * HTML5
 * CSS3
 * JavaScript
 * Python

Frameworks, Libraries & Programs Used:
1.	Bootstrap 4.4.1:
    *	Bootstrap was used to assist with the responsiveness and styling of the website.

2.	Flask:
    *	Used to create the web app.

3.	Mongo dB:
    *	Used to create the database.

4.	Jinja:
    *	Used for templating, for loops and conditionals within Flask.

5.	Google Fonts:
    *	Google fonts were used to import the 'Lato' font into the style.css file which is used on all pages throughout the project.

6.	Font Awesome:
    *	Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

7.	jQuery:
    *	jQuery came with Bootstrap to make the accordion work.

8.	Swiper.js
    *	This was used to make the images carousel.

9.	GitPod
    *	Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

10.	GitHub:
    *	GitHub is used to store the projects code after being pushed from Git.

11.	Balsamiq:
    *	Balsamiq was used to create the wireframes during the design process.

- - - - 
**8. Testing.**
- - - - 

- - - - 
**9. Deployment.**
- - - - 
The website has been deployed on:
* Heroku

- - - - 
  **10. Credits**
- - - - 

**Media:**

 * [Unsplash](https://unsplash.com/) for some of the images used.
 * [Google](https://www.google.com/)  for other images
 * [My Listing](https://www.airbnb.co.uk/rooms/18222301)  for some of my own images
 * [The Official Las Canteras website](https://www.hellocanaryislands.com/beaches/gran-canaria/las-canteras-beach/)  for some images



**Acknowledgements:**
* Code Institute slack community
* Code Institute tutor support 
* Code Institute mentor (Rohit Sharma)
* [StackOverflow](https://stackoverflow.com/) - for various fixes