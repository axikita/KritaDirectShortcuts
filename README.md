# Direct Shortcuts Krita Extension
This script adds options to the shortcuts menu for setting the active brush opacity to a fixed value rather than "up" or "down" from the current value.

## Usage
The default shortcut is ctrl+alt+shift+[number key] to set the opacity to [number key*10] percent. Thjese shortcuts are configurable in Krita's configuration settings.
- ctrl+alt+shift+1 = 10%
- ctrl+alt+shift+2 = 20%
- ctrl+alt+shift+3 = 30%
- ctrl+alt+shift+4 = 40%
- ctrl+alt+shift+5 = 50%
- ctrl+alt+shift+6 = 60%
- ctrl+alt+shift+7 = 70%
- ctrl+alt+shift+8 = 80%
- ctrl+alt+shift+9 = 90%
- ctrl+alt+shift+0 = 100%

The intended use is to program these shortcuts to a macro keyboard, and have easy one-press access to the target opacity, without needing to consider the current state of the brush. Alternatively, pick a few that you use often and assign them a more useable shortcut.

## Installation

In krita, go to Settings> Manage Resources > Open Resource Folder.
If you have an "actions" folder, copy the contents of the downloaded "actions" folder to there. If not, copy the downloaded "actions" folder to your resources folder.
If you have a "pykrita" folder in your resources folder, copy the contents of the downloaded "pykrita" folder to there. If not, copy the downloaded "pykrita" folder to your resources folder.
Restart krita. "setopacity" options should now appear under Tools>Scripts and under Settings>Configure Krita>Keyboard Shortcuts>Scripts>DirectShortcuts.


## Credits
[Direct Shortcuts](https://github.com/axikita/KritaDirectShortcuts) was developed by [Axi](https://github.com/axikita) and released under the [GPLv3 license.](https://www.gnu.org/licenses/gpl-3.0.en.html)
