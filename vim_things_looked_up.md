# VIM
---------------------------------------------

#### yank the word at the cursor including surrounding white space, (in command mode)
yaw

### yank the word at the cursor without surrounding white space, (in command mode)
yiw

### possibly putting aw after many commands will execute them on the whole word at the cursor
vaw  # select the whole word

### there isn't a built in insert line below _without_ entering edit mode, so
o,\<esc\>

### pasting previous cut/yank/delete
:reg  # list the register of paste-ables
"2p  # paste the second, after the cursor
"2P  # paste the second, before the cursor

### replace all of a "word" with another in selection
:s/original/new/g