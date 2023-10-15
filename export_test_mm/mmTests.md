

# Multimedia Application/AdobeExpress Testing

## Fixtures
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]


### Preparation
### FFMpeg Video Rendering

- [ ] A sample directory with video files.
- [ ] A sample video file.
- [ ] A temporary directory
- [ ]

### Home/Initialize
### Contact (Form Tests)
###  FAQs (Dropdowns)
###  Multimedia Multiple Items Page (Multiple Cards)
### Social Media One Item Page (Single Video)
### Multimedia Category Profile Page
### Multimedia Explore Posts Page
### Multimedia Tags and Search Page
### Multimedia Explore Posts Page (Categories Page)
###  Multimedia Gallery (List of Items)
### Multimedia One Gallery Item (Single Album)
### Multimedia One Gallery Item (Single Video)

## Tests

### Preparation

### FFMpeg Video Rendering

Primary

- [x] A directory that contains media files exists.
- [x] Multimedia files are collected in a list or moved to a new permanent dir.
- [x] A directory to store all media file directories is created.
- [ ]

- [ ]
- [ ]
- [ ] HLS Playlist creation command completes without errors.
- [ ] Playlist dir has been created in the correct location.
- [ ] Each video directory is no larger than 10 gigabytes.
- [ ] Each video directory is read only.
- [ ] Playlist dir has a m3u8 playlist file.
- [ ] Playlist dir has its associated .ts playlist files.
- [ ] The completed HLS playlist plays smoothly and has no graphical errors
- [ ] 
- [ ] HLS video thumbnail creation command completes without errors.
- [ ] Video thumbnail has been created in the correct location.
- [ ] Each Thumbnail image matches the original video.
- [ ] Frames in the thumbnail image are taken from even increments throughout the original video
- [ ] The thumbnail image is in jpg or a better format.
- [ ] Thumbnail is no larger than 5mb.
- [ ]
- [ ] The video preview creation command completes without errors.
- [ ] The preview has been created in the correct location.
- [ ] Preview matches the original video.
- [ ] The preview includes frames that contain 85% or more the same shape/target.
- [ ] The preview video is webp or a better format. 
- [ ] Preview is no larger than 20 megabytes.
- [ ] 
- [ ] The dir has an info.json/metadata file with a title, video description, runtime, resolution, and date.
- [ ] Each info.json/metadata file has accurate information based on its video.

Secondary

- [ ] 
- [ ] The dir has a poster images.
- [ ] Poster images match the video.
- [ ] 
- [ ] The dir has a closed caption file.
- [ ] The closed captions are synchronized with the video
- [ ] 
- [ ] The dir has a licence/copyright file.
- [ ] The licence is up-to-date and valid.
- [ ] 
- [ ] The dir has a transcript file.
- [ ] The transcript accurately documents the spoken words in the video.
- [ ]
- [ ] The dir has an analytics script file.
- [ ]

### Home/Initialize

- [ ] Each Video record includes a playlist dir, info.json file, thumbnail.jpg, and a preview video.
- [ ] 


Other Page Tests are Below

### Contact (Form Tests)

- [ ] Contact page. General form validation, email validation, dropdown button works, etc.
- [ ] Contact submit. Happens instantly, redirects home, flash message is shown correctly, flash message fades.
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ]
- [ ] 
- [ ] 
- [ ] 
- [ ] 

###  FAQs (Dropdowns)

Includes (specific item selection, dropdowns,)

- [ ] Each dropdowns buttons activate the dropdown.
- [ ] Clicking the same dropdown deactivates the dropdown.
- [ ] Clicking a different dropdown deactivates the first dropdown and opens the new one.
- [ ] All dropdowns elements only open the question/answer containers that are direct children.
- [ ] All questions are visible at all times.
- [ ] All questions and the selected answer is visible when a dropdown is activated.
- [ ] The selected answer appears beneath or next to the question it is associated with.
- [ ] The selected answer's content matches the question it is associated with.

###  Multimedia Multiple Items Page (Multiple Cards)

- [ ] Posts are displayed based on the users refined search or sort parameters. 
(relevance, best-selling, manual, product title (A to Z), product title (Z to A), price (Low to high), price (High to low), created (Oldest to newest), created (Newest to oldest)
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ]
- [ ] 
- [ ] 
- [ ] 
- [ ] 

### Social Media One Item Page (Single Video)

Includes (Reveal more toggle)

- [ ] The HLS video is can be played from start to finish without any graphical errors.
- [ ] Video title is included.
- [ ] Video description is included.
- [ ] Video runtime is included.
- [ ] Video resolution is included.
- [ ] Thumbnail image is shown before the video is played.
- [ ] 
- [ ]
- [ ] 
- [ ] 
- [ ] 
- [ ] 

### Multimedia Category Profile Page 

- [ ] Name is included.
- [ ] Bio is included.
- [ ] Website links return no errors.
- [ ] Private information is only visible to authenticated users who follow the account. (followers, follows count, posts, stories, bio, links).
- [ ] A link to log in with a redirect back this page is included in order for the user to easily check if they can see the content. 
- [ ] Bio is included.
- [ ] If no posts are uploaded a message informs the user.


### Multimedia Explore Posts Page


- [ ]
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ]
- [ ] 
- [ ] 
- [ ] 

### Multimedia Tags and Search Page

Search Filters
- [ ] The Search filters container is located on the left side of the search results container. 
- [ ] Filter options with more than options include a reveal more button to show more options. 
- [ ] 
- [ ] 

Search Results

- [ ] The Search results container is located on the right side of the search options container. 
- [ ] The search results are updated on submit search filter submit with only show items that match the last updated query.
- [ ] 
- [ ] 
- [ ] 
- [ ] 

### Multimedia Explore Posts Page (Categories Page)

- [ ] Category cards are displayed in a grid layout.
- [ ] Category images are emphasized when hovered over.
- [ ] Category preview video plays on hover.
- [ ] Category preview stops when not hovered over. 
- [ ] The same Category preview restarts and plays on hover.
- [ ] Category items are clickable links.
- [ ] Category links and lead to the correct category.
- [ ] Category links return ok status codes.
- [ ] A sort button can be clicked to toggle the available sort options and assign one as active.
- [ ] Fewer than four sort options are included in the toggle.
- [ ] Sort button can be clicked to toggle sort options.
- [ ] Categories can be sorted by name (A to Z) or (Z to A) or by popularity.

###  Multimedia Gallery (List of Items)

Includes: (, )

- [ ] All media is optimized for the Web.
- [ ] The masonry/grid button works correctly.
- [ ] Layouts have no overlying items.
- [ ] Layouts 
- [ ] Masonry layout follows the correct order based on item height.
- [ ] Each item plays the preview or a hover effect when hovered over.
- [ ] Each item returns an ok status code.
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ]
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] Page navigation is located at the bottom.
- [ ] The page that the user is current located in is emphasized.
- [ ] Page nav buttons either update the list of items or navigate to a different page.
- [ ] Page nav numbered buttons navigate the page to the correct page number.
- [ ] Page nav next button take the page to the next incremental number.
- [ ] Page nav previous button take the page to the previous incremental number.
- [ ] Page nav last button take the page to the last available page.
- [ ] Page nav first button take the page to the first available page.

### Multimedia One Gallery Item (Single Album)

Includes: (Modals, hover previews, view count, rating calculation)

- [ ] Video length and resolution is located in the bottom right corner of the preview.
- [ ] Video length and resolution is accurate.
- [ ] Video category is in the top left corner.
- [ ] Video category is accurate.
- [ ] Date of creation, video views, and like percentage is in the top right corner.
- [ ] Date of creation, video views, and like percentage is accurate.
- [ ] Video title is at the bottom and fill at least 80% of the available width.
- [ ] Video title is emphasized.
- [ ] Options icon is on the bottom right side.
- [ ] Clicking the options icon opens the options modal.
- [ ] Clicking outside the options modal closes it.
- [ ] The user can see the options modal in the viewport when it opens.
- [ ] Links in the options modal perform the correct task.
- [ ] Enabling the save/favorite option adds the video to the user's collection. 
- [ ] Disabling the save/favorite option removes the video from the user's collection. 
- [ ] The not interested option removes this video from the user's suggestions if using explore/recommendations page. 
- [ ] The share option opens a larger modal that displays links.
- [ ] The share modal links return ok status codes.
- [ ] The copy url link copies a valid link to the selected video to the user's clipboard. 
- [ ] 
- [ ] 

### Multimedia One Gallery Item (Single Video)

- [ ] Slideshow activates on hover or swipe.
- [ ] Video
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 

