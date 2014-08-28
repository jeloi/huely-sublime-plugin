Huely Palette Extractor - Sublime Plugin
========================================

A sublime plugin to extract and visualize colors in your code in a nice interactive palette.

![](https://github.com/Jeloi/sublime-huely-palette/blob/master/huely-plugin-gif.gif)

This is a plugin for [huely.co](http://huely.co), and requires an internet connection to work.

## Installation

___(Coming Soon)_ With Package Control__:<br>
Run “Package Control: Install Package” command, find and install the Huely Palette plugin.
Restart Sublime if necessary.

__Manually__:<br>
Clone or download git repo into your packages folder (in ST, find Browse Packages... menu item to open this folder)
Restart Sublime if necessary.

## Usage

Default OSX Keybinding: __ctrl+shift+h__

Setup your own keybinding by inserting the follow in your user keybindings file:

{ "keys": ["ctrl+shift+h"], "command": "huely_extract" }

## Technical Info, ICYW

- The plugin submits a post request to the huely "API", with the text data in your current file.
- If there are colors to be extracted, huely creates a palette and returns with 200:OK and the palette ID.
- The plugin then uses webbrowser to open your browser to the palette page.
- Don't count on your palettes being permanently reachable! Huely is currently hosted on meteor.com and I don't own the DB.



