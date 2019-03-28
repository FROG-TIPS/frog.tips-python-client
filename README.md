# FROG Tips for Python 3.0.5

Python interface to the FROG Tips API. Download FROG tips and submit your own!

## Getting Started

### Installation
Installation is very simple. Just type:

    $ sudo -H python3 -m pip install frogtips

### How to run

Running is even easier. To get started, type:

    $ frogtips

### Run-Time Options

Available options are:

    -a 
    --about
    
Displays a help message explaining the reason for the program's existence.

    -f 
    --frogsay
    
Displays program output in a speech bubble as spoken by one of several ASCII 
art FROGs.

    -h
    --help

Prints a help message detailing available command options.

    -n [name]
    --name [name]
    
Adds [name] to your API key. [name] can be your username or twitter handle. 
This is necessary if you want to submit your own FROG tips (see below). You 
will only have to perform this operation once as your name is then permanently
associated with your API key.

    -r
    --random
    
Displays a random FROG tip. If there are no FROG tips cached on disk, the 
program will connect to the https://frog.tips/ API server and download more 
FROG tips.

    -s [tip_text]
    --submit [tip_text]
    
Submits [tip] for inclusion in the FROG Tips database. Once you have submitted
your new tip, it will enter a moderation queue, where your tip may be accepted 
or rejected. Your tip may be edited before acceptance. Only once accepted will
your tip be displayed on https://frog.tips/, available through the API, and/or
tweeted. Note that to be accepted, your tip must meet the following criteria:
* Must be 280 or fewer characters in length.
* Must contain the word FROG.
* Must be in ALL CAPITAL LETTERS.
* Must end with a period.


    -t [tip_id]
    --tip [tip_id]
    
Downloads and displays tip number [tip_id].

    -v
    --version

Displays the version number.

    -w
    --warranty

Displays the FROG warranty.

## FROG Tips API

It's easy to incorporate FROG Tips into your own Python program by using the
FROG Tips API. For example, the following code will print a random FROG tip:

    from frogtips import api

    tips = api.Tips()
    tip = tips.get_next_tip()
    print(tip.get_formatted_tip())

Or to obtain a specific FROG tip (in this case, FROG tip number 2):

    from frogtips import api
    
    tip = api.Tip(2)
    print(tip.get_formatted_tip())

It's that simple!

### Tip() object

The Tip() object contains a single individual FROG tip. Its constructor takes a
single optional argument: _tip_id_, an integer. If given this argument, the
Tip() object will download tip number _tip_id_ from the https://frog.tips/ API 
server and populate itself with the resulting data.

#### Tip() object methods

##### get_id()

Returns the ID number of the FROG tip, if set.

##### get_tip()

Returns the text of the FROG tip, if set.

##### get_formatted_tip()

Returns a string in the format "TIP _tip_id_: _tip_text_"

##### submit_tip(_tip_text_)

Submits _tip_text_ to the https://frog.tips/ API server for inclusion in the 
FROG Tips database and returns the id of the resulting tip (if successful).
To be accepted, your tip must meet the following criteria:
* Must be 280 or fewer characters in length.
* Must contain the word FROG.
* Must be in ALL CAPITAL LETTERS.
* Must end with a period.

### Tips() object

The Tips() object contains a queue of random FROG tips. Each tip is represented
as a Tip() object. When instantiated, the Tips() object will attempt to load 
FROG tips from on-disk cache. If there are no tips in the cache, then the
Tips() object will download more tips from the https://frog.tips/ API server.
 
#### Tips() object methods

##### get_next_tip()

Returns a Tip() object containing the next FROG tip in the queue.