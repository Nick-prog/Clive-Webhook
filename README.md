[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
 <p align="center">
  <a href="https://github.com/Nick-Prog/Clive-Webhook">
    <img src="images/Clive-1.png" alt="Logo" width="350" height="200">
  </a>
   </p>
</p>

**THIS PROJECT HAS BEEN DISCOUNTIED. PLEASE REFER TO THE IMPROVED-CLIVE-WEBHOOK REPOSITORY FOR THE LATEST VERSION.**

# Clive-Wehbook
The main purpose of this program was to utilize a webhook connection on an online form that has a high amount of traffic on a daily basis. 

**If you wish to convert the program into a runnable program for others to easily download then follow the Publish Python Apps link below.**

# About The Project
<br />
 <p align="center">
  <a href="https://github.com/Nick-Prog/Clive-Webhook">
    <img src="images/Clive-Webhook-1.4.1 (1).png" alt="Logo" width="700" height="500">
  </a>
   </p>
</p>

This tab was created for the clive form titled "Upload Documents".

* The box located on the **top left** provides general information for the user, as well as, a summary of how to use the features of the program.

* The box located on the **bottom left** titled **Department?** provides 7 different options for the user to pick. Each option was made according to the Clive form you can find at the TAMUK Upload Forms link below.

* The box located on the **top right** contains real time information for the user if they wish to know what each departments current amount of entries available for pulling, the date and time they were last submitted, and the last date the system had checked for updates. A "Refresh" push button can also be located to the **top left** of the table as well.

* Finally, the box located on the **bottom right** titled **Storage Location?** allows the user to specify what directory they wish to store the pulled files.

<br />
 <p align="center">
  <a href="https://github.com/Nick-Prog/Clive-Webhook">
    <img src="images/Clive-Webhook-1.4.1 (2).png" alt="Logo" width="700" height="500">
  </a>
   </p>
</p>

This tab was created for the clive form titled "Fee Wavior Request".

* The box located on the **left** provides general information for the user, as well as, a summary of how to use the features of the program.

* The box located on the **top right** contains real time information for the user if they wish to know how many entries are currently available to pull. A "Refresh" push button can also be located to the **top left** of the graph as well.

* Finally, the box located on the **bottom right** titled **Storage Location?** allows the user to specify what directory they wish to store the pulled files.

_________________________________________________________________________________________________________________________________________________________________________________

All user inputs can be viewed on the labels below the progress bar before pulling. Once pulled, all downloading documents will become deleted automatically from the Pipedream webhook. Only up to a _100_ at a time!

# Getting Started
Follow the instruction below to successfully run the program.

## Prerequisities
A Python 3.9 environment was used to create and run this program, but anything up to 3.6 should suffice. Since this program mainly uses Pipedream as a hosting source, a Pipedream account will be needed to genereate your webhook link. 

## Requirements
 1. Clone/download the repo
    ```sh
    git clone https://github.com/your_username/Project-Name.git
    ```
 2. Now that you have the files on your machine, replace all _webhook_ and _api_key_ values within the connection.py file. Your _api_key_ can be found in the settings of your     account with Pipedream, without it you will be  unable to interact with the webhook link so keep it SAFE.
 3. Finally, execute the main.py file and your program  should run after a short period.
 
 **Disclaimer: This program was made SPECIFICALLY for this exact problem. Unless the JSON Snippet metadata genearted for your problem is exactly the same, you must alter most if not all of the code.**
  
 <br />
  <p align="center">
  <a href="https://github.com/Nick-Prog/Clive-Webhook">
    <img src="images/TAMUK Logo 3.jpg" alt="Logo" width="350" height="250">
  </a>
  </p>
</p>
 
# Change Log
**Version 1.3.3 - Version 1.4.1**
* Improved the downloading requests definition in the requests.py file.
* Added new downloading methods to requests.py file to seperate and breakdown the logic.
* Implemented a new clive webhook into the program for another high traffic clive form.
* Added tabs to the program to allow users to swap back a forth between two different clive webhooks.

**Version 1.3.2**
* Improved the downloading requests definition in the requests.py file.
* Added a new dict option in the abbreviation definition in the dictionaries.py file.
* Added comments to important sections of the code.

**Version 1.2.2 - 1.3.1**
* Added a pop-up dialog box to confirm your selection.
* Optimized loading times by removing real time data information from populating on startup.
* Fixed the default value for storage location to better suit this problem.
* Added more entries to the exists and abbrevations dict in dictionaries.py.
* Re-connected the progress bar to the on_refresh event.
* Improved code in various areas.
* Added a timer to track startup times. (Current: ~ 0.56 secs| Previous: ~ 4 to 5 secs)
* Combined the on_click and on_refresh event thread usage to save lines of code.
* Added a "\_\_title__" method to correctly display the name of the current applcation.

 **Version 1.2.1**
 * Fixed downloading issues.
 * Added new dictionaries to reduce code length and improve reuseability.
 * Removed dead code.

 **Version 1.2**
 * Fixed issues from verions 1.0 and 1.1.
 * Reduced load and startup times by bolstering our reusable code methods.
 * Removed progress bar progression for "Refresh" method to improve load times.
 * Combined the "Pull" and "Delete" button method into one button, "Pull".
 * Changed current status label next to "Pull" button to better articulate program status.
 * Added dictionaries.py file for large dicts that may find us outside of their current implementations.
 * Improved delete and download methods to reduce margin of error.
 * Added folder creation functionality that allows the creation of non-existant storage locations possible.
 * Removed text from genearl information box that was deemed unneccesary or out dated.
 * Setup a single thread method that will be utilized by pull and refresh requests.
 * Removed the "Description:" text from info.txt files.
 
 **Version 1.1**
 * Added a "Refresh" push button to the **top left** of the real time information table.
 * Improved load times and added a sleep thread to prevent multiple miss-inputs.
 * Included an autmoated storage location setter for the TAMUK purposes.
 * Fixed problems with the real time information table (i.e. Date, Time, and Last weren't updating properly)
 * Removed the disable feature from the other options under Department and added their funcitonality.
 * Delete button now only removes the entries pulled at that time.
 * Added extra labels to the right of the "Pull" push button to better display the current state of the program.
 * Added a mininize feature and fixed window sizes.
 * Added images to the Dialog box and the "Refresh" button.
 * Disabled editing rights for users on the real time information table.
 
 ## Reported/Known Bugs
 All reported bugs may be caused from similar instead of seperate instances.
 
 **Version 1.3.2**
 * Program didn't recongize "Residency Verification Form" submissions and broke when trying to pull from a singler department.
 
 **Version 1.2**
 * Program may still become temporarily frozen when downloading a large sum of files at once.
 * Downloading errors are still a potential threat until stricter guidelines for the "Upload Documents" form are made.
 * Downloading similar documents can still lead to errors.
 
 **Version 1.1**
 * When downloading to a large share drive, potential temporary freezing may occur.
 * Delete request very rarely skip items that have been just pulled.
 
 **Version 1.0**
 * Program will crash if a similar file name currently exists in the storage location.
  
# Contact
Nickolas Rodriguez | Twitter: @\_Nick_Rod_ | Email: Nickolasrodriguez98@gmail.com | GitHub: Nick-prog

# Acknowledgements
* [Pipedream](https://www.pipedream.com/)
* [TAMUK Upload Forms](https://www.tamuk.edu/enrollment-management/admission/future-students/ftic-transfer/uploaddocs.html)
* [Publish Python Apps](https://gist.github.com/ForgottenUmbrella/ce6ecd8983e76f6d8ef47e07240eb4ac)
 
<!--MARKDOWN LINKS & IMAGES -->
 [linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
 [linkedin-url]: https://linkedin.com/in/nickolas-rodriguez-392498197/
