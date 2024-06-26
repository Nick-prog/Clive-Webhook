[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
 <p align="center">
  <a href="https://github.com/Nick-Prog/Clive-Webhook">
    <img src="images/Clive-1.png" alt="Logo" width="350" height="200">
  </a>
   </p>
</p>

# Clive-Wehbook
The main purpose of this program was to utilize a webhook connection on an online form that has a high amount of traffic on a daily basis. 

# About The Project
Similar to the previous Clive-Webhook program, but removes the initial GUI to improve performance and speed. Also, shortens the main code and implements an error handler for improved troubleshooting.

_________________________________________________________________________________________________________________________________________________________________________________

# Getting Started
Follow the instruction below to successfully run the program.

## Prerequisities
A Python 3.9 environment was used to create and run this program, but anything up to 3.6 should suffice. Since this program mainly uses Pipedream as a hosting source, a Pipedream account will be needed to genereate your webhook link. 

## Requirements
 1. Clone/download the repo
    ```sh
    git clone https://github.com/your_username/Project-Name.git
    ```
 2. Now that you have the files on your machine, replace all _source..._ and _authroization_ values within the __init__.py file. Your _authorization_ value can be found in the settings of your account with Pipedream, without it you will be unable to interact with the webhook link so keep it SAFE. Your _source..._ representes what source you would like to access within your Pipedream account. After you create a source and specify webhook as the type, it should be displayed on the page's url and should start with "dc_...".
 3. Finally, execute the main.py file and your program should run after a short period.
 
 **Disclaimer: This program was made SPECIFICALLY for this exact problem. Unless the JSON Snippet metadata genearted for your problem is exactly the same, you must alter most if not all of the code.**
  
 <br />
  <p align="center">
  <a href="https://github.com/Nick-Prog/Clive-Webhook">
    <img src="images/TAMUK Logo 3.jpg" alt="Logo" width="350" height="250">
  </a>
  </p>
</p>
 
# Change Log
 
 **Version 1.1**
 * Removed dead code
 * Improved reutilization of code
 * Improved error handler boxes to display a more accurate troubleshoot description
 
 ## Reported/Known Bugs
 All reported bugs may be caused from similar instead of seperate instances.
 
 **Version 1.0**
 * Program's error handler needs slight improvements
  
# Contact
Nickolas Rodriguez | Twitter: @\_Nick_Rod_ | Email: Nickolasrodriguez98@gmail.com | GitHub: Nick-prog

# Acknowledgements
* [Pipedream](https://www.pipedream.com/)
* [TAMUK Upload Forms](https://www.tamuk.edu/enrollment-management/admission/future-students/ftic-transfer/uploaddocs.html)
* [Publish Python Apps](https://gist.github.com/ForgottenUmbrella/ce6ecd8983e76f6d8ef47e07240eb4ac)
 
<!--MARKDOWN LINKS & IMAGES -->
 [linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
 [linkedin-url]: https://linkedin.com/in/nickolas-rodriguez-392498197/

