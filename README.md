![jurrasic copy](https://user-images.githubusercontent.com/105305546/213839749-77b81efa-62d1-4817-af83-3123dbdd54f3.png)

# Wiki
Project 1 for Harvard's CS50w Web Programming with Python and JavaScript.

📹 `Youtube:` https://www.youtube.com/watch?v=VOqKjYN3r5A&t=9s

## Overview:
Built with `Markdown`, `HTML`, `CSS`, `Bootstrap`, `Python`, and `Django`.   
The site links together multiple pages all personally styled in a __Jurassic__ __Park__ theme via `Photoshop CS6` and online gifs. 

## Specifications:

This site contains:

1. __Entry__ __Page__: displaying contents of that encyclopedia entry.  
   If an entry requested does not exist, the user is presented with an error page.
   
   ![jp](https://user-images.githubusercontent.com/105305546/213835896-6b85e956-f226-4de2-a4e2-97070a566d56.gif)
   
   If the entry does exist, the user is presented with a page that displays the contents of the entry.

2. __Search__: allows the user to query in the search bar for an encyclopedia entry.
   If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.
   If the query does not match the name of an encyclopedia entry, the user is taken to a search results page that displays a list of all encyclopedia    entries with the query as a substring. For example, if the search query were `ytho`, `Python` appears in the search results.
   
   <img width="533" alt="Screen Shot 2023-01-20 at 9 24 04 PM" src="https://user-images.githubusercontent.com/105305546/213839819-f70a0038-4c87-4524-9470-c15b81c10585.png">

3. __New__ __Page__: “Create New Page” allows the user to create a new encyclopedia entry.
   Users are able to enter a title and are able to enter Markdown content for the page.

4. __Edit__ __Page__: The user can edit an entry’s Markdown content in a textarea. Once the entry is saved, the user is redirected back to that entry’s    page.

5. __Random__ __Page__: Clicking `Random` in the sidebar takes user to a random encyclopedia entry via the imported `random` function.

   ![bathroom](https://user-images.githubusercontent.com/105305546/213838721-38e0f7f5-13bb-43e4-9ad2-ecafc20ac281.gif)


