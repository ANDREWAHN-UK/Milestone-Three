This is the testing section of the readme, placed in a separate file:
- - - -
**8. Testing:**
- - - -

*8.1 Code Validation*
- - - - 

1. I used https://validator.w3.org to validate the html. 

The html validator returned the errors:
  * "End tag li seen, but there were open elements."  This is because I forgot the end </a> on a couple of headings.
  *	"Section lacks heading. Consider using h2-h6 elements". This was on base.html. Adding a heading meant that heading was visible on all pages, obviously unwanted. So I removed the section element, to no ill effect.

2. I used https://jigsaw.w3.org/css-validator/ to validate the CSS:

  * The CSS returned some errors to do with bootstrap.min.css and swiper-bundle.css, none with Style.css"

3. On the recommendation of my tutor, I used https://jshint.com/ to validate the JavaScript:

With jshint, it informed me of the following:
  * 	'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
In other words, no real errors, probably because there was little Javascript used, compared to the previous Project.
It also informed me of several missing semicolons, which I rectified.

4. I used http://pep8online.com/ to validate the Python code.
    * No errors found

5. Google Light House Audit result:
- - - -
![image](https://i.imgur.com/HNM4WUo.png)

- - - -
*8.2 Test cases/ Testing the user goals/stories (section 2):* 
- - - -

1. Potential Employer Goals:

* Upon entering the site, users are greeted with a visually attractive homepage, with clear images, and boxes that highlight the main activities and purposes of the site.

* The homepage immediately establishes the purpose of the website, and directs users to "get started" -as this is the left most option, and therefore the first for most people

* The user has three main options, as shown on the home page, get started --> view reviews --> find out more about the listing this website

* The navbar reinforces these options once rendered visible. To render it visible, the user clicks the top left button. This has a gentle animation that draws the users' attention, effectively mimicking the sun.
- - - -
  Full screen (1920*1080) homepage
- - - -
![image](https://i.imgur.com/PxAKljU.png)
- - - -
Full screen (1920*1080) Reviews
- - - -
  ![image](https://i.imgur.com/VP0FYlI.png)
- - - -
- - - -
Full screen (1920*1080) Register
- - - -
  ![image](https://i.imgur.com/qRB6lXg.png)
- - - -
 Reviews with an iPhone 8:
- - - -
![image](https://i.imgur.com/Hl80rEw.png)
- - - -
 Register with an iPhone 8:
- - - -
![image](https://i.imgur.com/EfrLt6c.png)
- - - -
 Homepage with an iPhone 8:
- - - -
![image](https://i.imgur.com/BFsvkpH.png)
- - - -

2. Users that want to view reviews:
* Users can quickly and easily view the reviews and Home pages.
- - - -
  Full screen (1920*1080) homepage, navbar open
- - - -
![image](https://i.imgur.com/rUAuTiT.png)
- - - -
Full screen (1920*1080) Reviews
- - - -
  ![image](https://i.imgur.com/VP0FYlI.png)
- - - -
 Homepage with an iPhone 8, navbar open:
 - - - -
![image](https://i.imgur.com/gDDuBSI.png)
- - - -
 Reviews with an iPhone 8:
- - - -
![image](https://i.imgur.com/Hl80rEw.png)
- - - -

3. Users that want to create/update and delete reviews:
* The create, edit and delete functionality is accessed via the Profile and Review pages.
Full screen (1920*1080) User Profile
- - - -
  ![image](https://i.imgur.com/cxzjvVX.png)
- - - -
iPhone 8 User Profile:
- - - -
![image](https://i.imgur.com/1NK6NiJ.png)
- - - -
Full screen (1920*1080) Reviews page with edit/delete buttons
- - - -
  ![image](https://i.imgur.com/pT9iKjo.png)
- - - -
iPhone 8 Reviews page with edit/delete buttons:
- - - -
![image](https://i.imgur.com/QU3cA17.png)
- - - -
Full screen (1920*1080) Creating a Review:
- - - -
![image](https://i.imgur.com/nkPGMJp.png)
- - - -
iPhone 8 Creating a Review:
- - - -
![image](https://i.imgur.com/fHZdY4I.png)
- - - -
Full screen (1920*1080) Editing a Review:
- - - -
![image](https://i.imgur.com/r7nn6gx.png)
- - - -
iPhone 8 Editing a Review:
- - - -
![image](https://i.imgur.com/f8U0nAU.png)
- - - -

4. Admin user:
When logged in as Admin, User can access all reviews *and* profiles, via Profile and Reviews Page.
Full screen (1920*1080) Admin Profile
- - - -
  ![image](https://i.imgur.com/8kwbTFV.png)
- - - -
iPhone 8 Admin Profile:
- - - -
![image](https://i.imgur.com/RkDh9Tm.png)
- - - -
Full screen (1920*1080) Admin Profile page, showing  edit/delete Profiles function
- - - -
  ![image](https://i.imgur.com/A6HbNwc.png)
- - - -
iPhone 8 Admin Profile page, showing  edit/delete Profiles function :
- - - -
![image](https://i.imgur.com/wlfwnhF.png)
- - - -
*8.3 Bugs and Bug Fixing:* 
- - - -
There were numerous teething issues with this being the first time using so much Python, Heroku etc.
1.	App would not deploy on Heroku.
    * **Fix:** The config vars need to be exact. Errant commas or quotation marks stop the process working.


2.	Edit Review function would not work.
    * **Fix:** This took a week to fix. I rebuilt the entire website to divine a solution, which had to do with term definitions in the app.py file.


3.	The carousel provided by swiper.js would not scale down properly for smaller viewports.
    * **Fix:** Used      height: 80%;    width: 100%;    margin: auto;    on  .swiper-slide img.


4.	Various of the containers would have their contents spill out on anything other than desktop resolutions.
    * **Fix:** Using a height and width value in VH and VW, e.g. height: 50vh, was the cause. To solve it, I used % values, e.g. height: 50% along with a min-height/width value, e.g. min-height:50vh.


6.	On smaller viewports, the positioning of the nav buttons (on the nav bar) would all shift too far up.
    * **Fix:** In CSS position: Fixed.


7.	Edit profile function would not work.
    * **Fix:** I could only make this work for the admin. Users can't edit their own profile, which I think has to do with accessing the variables inside the Jinja for loop. Currently, this is set to (if admin, show option to edit/delete profile) but repeated experimenting with allowing users to do this resulted in the relevant webpage simply not displaying. Therefore, this was axed.


8.	Users only able to upload single images.
    * **Fix:** Research indicated a possible solution [here](https://devcenter.heroku.com/articles/simple-file-upload) however I chose not to pursue this, on account of time contraints


9.	On the review page, having many reviews opened could make the page clumsy and overloaded.
    * **Fix:** This is only+ really noticeable for the admin user, as they can see all reviews and all profiles. The fix is to limit the amount of items shown by the for loop, i.e.: {% for review  in reviews [:5] %} if one wanted 5 items listed. I couldn't find a way to list items in a for loop randomly, which is a drawback. With a limited view like this, users run the risk of not seeing a review they may be looking for. The search function works and partially mitigates this drawback. On the user profile page, this could in theory also become a problem. Note that no limiter has been put on the profiles the admin user can see, and there is currently no search function for the users.


10. Using a carousel instead of an accordion to house the reviews would not work.
    * **Fix:** Research indicates this is to do with the .active class of the carousel not mixing well with the jinja for loop. In theory, something like this:
     ``` {% for review in reviews %} {% if loop.index == 1 %} active{% endif %}  {% endfor %}```   would have fixed it. I experimented with this briefly, but due to time spent on Point 8.3.2 (edit function) I chose not to pursue this. Referring to Point 5.13.11 (Cards website) the same possible fix applies.

11. Applying animationsto draw the user attention to hte cirtcle at top left of screen, caused the x (close) button to not show up
    * **Fix:** Enclose the original circle within another circle, and apply animations to  the 2nd circle, but ensure 2nd circle position = fixed.

12. The edit review and edit profile templates would not populate values.
    * **Fix:** Save and restart several times. However, I could not get ratings field to populate , no matter what was tried.

13. Because it is fiddly on smaller devices to select a url for images, this option was made non-required, which then led to potentially empty images for reviews & profile pages, not desired.
    * **Fix:** Add in a default image if user did not put in a url. This works for reviews, but not for Profiles.

- - - -
*8.4 Supported screens and browsers:* 
- - - -

There are screenshots, available in the screenshots folder, that show the website working at Fullscreen, and also at example mobile (iPhone 8) viewports.

As there are several screenshots, rather than link them individually, I have linked the containing folder:

[Screenshots](https://github.com/ANDREWAHN-UK/Milestone-Three/tree/main/static/screenshots)

Additional testing on the view ports was done using [Multi Device Mockup Generator](https://techsini.com/multi-mockup/).

I used Opera, Edge, Firefox and Chrome, and tested these, along with general usability, using the dev tools there.

Dev tools in Chrome are accessed by *right click + inspect + toggle device toolbar + select various devices*.

In Opera *right click + inspect + toggle device toolbar + select various devices.*

In Firefox, *right click + responsive design mode (ctrl+shift+m) + select various devices.* NB that Firefox displays this all at the bottom, not the right side like the others.

In Edge *right click + inspect + toggle device emulation + select various devices.*

The procedure for testing was as follows:

1.	In style.css set up media queries for the viewports, in descending order (i.e. starting with 991px --> 767px --> 600px -->480px --> 425px -->280px)

2.	introduce a new element, or change, e.g. a "Review Button."

3.	style it for the desktop, using dev tools and style.css.

4.	when happy with this, use dev tools for the various viewports (e.g. iPad Pro.)

5. If the screen looks ok, leave alone. If not, adjust those elements using the media queries discvussed in Point 1.

6.	Repeat for each element and page, e.g. styling the height and width of containers, as discussed in 8.3.4.

6.	Save changes via GitHub commit and push.

7.	Open up website on mobile device. I have an Oppo X2 Lite and Kindle Fire, my sister has an iPhone 8 and my partner a Galaxy A21.

Further testing was done with friends and family, and by submitting the code for peer review on slack, using fresh eyes to test the UX, most notably ease of navigation between pages, and visibility of text against coloured backgrounds.

Results of this testing led to a **considerable** number of viewport adjustments, the majority of which was adjusting the behavious of the various containers, as discussed in 8.3.4.