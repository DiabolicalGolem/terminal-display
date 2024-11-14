# Terminal Display


### About
---
This project came about as a way to display information in a gui-like manor on the terminal. I made it because I was unsatisfied with the way one of my other projects[^1] was interfacing with its users[^2].

As of right now, it is unfinished, but the basic framework is there—I think.

### Todo
---
- [ ] Reformat `terminal-display` for implementation of update function

### Process
---
The way I currently have `terminal-display` set up is as follows:
- The display is initialized.
- Window elements are created with relevant position, scale, and content attached.
- Everything is drawn in the order it was called, with the most recent being drawn on top.

The way I want it to work:
- The display is initialized.
- Window elements are created with relevant position, scale, and content attached (allowing for updating elements and variable pass-through).
- Everything is drawn.
- An update function is called when either information changes or if the screen is resized. This function:
	- Updates the display scale and "crops" accordingly.
	- Updates window locations if they are placed percentage wise.
	- Re-draws the screen.

### How to use
---
This program is not ready to be used easily, and changes are going to be made as often as I can manage, so the exact process of importing and using this program will not be the same. Therefore, I don't feel like explaining how to use it at this time. When I have added the update function and ironed out most of the kinks, then I will explain how to use it.


---
[^1]: [Screen Extractor](https://github.com/DiabolicalGolem/Screen-Extractor)
[^2]: i.e. Me, myself, and I.
