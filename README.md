[![Build Status](https://travis-ci.org/username/project.svg?branch=master)](https://travis-ci.org/username/project)
# Markti
Markity is a website designed to simplify online shopping by allowing users to search for
products across multiple popular stores and compare prices. The website presents users with a
comprehensive list of search results, showing the price and product details from each store, as
well as a rating system that highlights the best deals. Users can then purchase the item they
desire from the store offering the best deal.

Host Link: [Marketi](https://marketi-ps-caab34e05b6a.herokuapp.com/)    
   
Associated With: 
* [Fadi Tarazi](https://www.linkedin.com/in/fadi-tarazi-952966247/)
* [Sajed AbdAlkareem](https://www.linkedin.com/in/sajed-abdalkareem-4b579b24a/)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
You can view the report made with the project using this link [Marketi Report](https://drive.google.com/file/d/1WjnCDcTZM8i6aRm-i3UVBUCXkVNwoUOi/view?usp=drive_link)



## Installation
> git clone https://github.com/Hanna-Hinn/Markti.git  
> cd Markti  
> pip install django  
> pip install djangorestframework  
> pip install gunicorn  
> pip install whitenoise
> cd ./frontend/  
> npm install

Notes:     
* if it requests to install more dependencies then go check requirements.txt it have all the dependencies names and versions in it   
  
## Usage
The Website is already configured for deployment and hosting on heroku.  

**If you wanna use the project on localhost just change the urls in the frontend
**(in the actions file in the websitepages/actions and the url in the contactus page in websitepages/pages)
     
I think i have setup every file with a documentation of how to use.   
(If you think that it's not clear you are free to start an issue or contact me via email)  
  
Here's a sequance diagram to show how the system will work.  
![Alt Sequence Diagram](https://i.ibb.co/8gQXWDQ/Untitled-Diagram-drawio.png)  
  
If you wanna host you do the follwing commands:  
> cd ./forntend/ (if ur not in the frontend directory)  
> npm run build  
> cd .. (back to the main directory)  
> python manage.py collectstatic  
This should setup the static files for hosting.  

## Contributing
If you wanna contribute just make an issue then add a pull request and i will review as soon as possible.

## License 
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements  
We would like to express our gratitude to the following individuals and projects for their contributions and support to this project:  
- [Fadi Tarazi](https://www.linkedin.com/in/fadi-tarazi-952966247/) - Thank You my partner because without you this would have not happend
- [Yousef Mahmood](https://www.linkedin.com/in/yousef-mahmood-806758226/) - For being the first real user on the website and breaking it in the first 5 mins :)
- [Creative Tim](https://www.creative-tim.com/product/material-kit-react) - For the amazing library of Material Kit 2  
- [Awesome Font](https://fontawesome.com/) - For the Amazing fonts they make.  
- [Material UI](https://mui.com/) - For the variety of UI components they provides in react.  
- [Prop-Types](https://legacy.reactjs.org/docs/typechecking-with-proptypes.html) - For helping us produce better code  
- [Heroki](https://www.heroku.com) - For hosting our website  
- [Amazon Web Services](https://aws.amazon.com/) - For hosting our Postgresql Database on it.  

