import os

APPLICATION_NAME = 'FROG Tips for Python'
VERSION = '3.0.5'
SHORT_DESCRIPTION = 'Tips for how to operate your FROG'
LONG_DESCRIPTION = 'Command-line interface to https://frog.tips/ - ' + \
                   'download FROG tips and/or submit your own tips using ' + \
                   'this handy API interface.'

FROG_TIPS_DOMAIN = 'frog.tips'

MAX_TIP_LENGNTH = 280

HOME_DIR = os.path.expanduser('~')
FROG_TIPS_DIR = HOME_DIR + '/' + '.frogtips'
CREDENTIALS_FILE = FROG_TIPS_DIR + '/' + 'credentials'
TIPS_FILE = FROG_TIPS_DIR + '/' + "tips"

ERROR_MSG_404 = "NOT FOUND (ERROR 404)"

HELP = """Usage:
frogtips [options]
  -a --about         Displays the "about" message.

  -f --frogsay       Displays output in a speech bubble spoken by an ASCII art
                     FROG.

  -h --help          Prints this help message.
  
  -n --name [name]   Adds [name] to your API key so that you can submit your
                     own FROG tips. You will only need to perform this
                     operation once.
                     
  -r --random        Print a random FROG tip.
  
  -s --submit [tip]  Submit [tip] to frog.tips. You must add a username to your
                     API key first (see above).
                     
  -t --tip [id]      Download and print FROG tip number [id].
  
  -v --version       Displays the version number.
  
  -w --warranty      Displays an abbreviated version of FROG's warranty."""

WARRANTY = """\
FROG IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL FROG SYSTEMS, 
INCORPORATED BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH FROG OR THE USE OR OTHER DEALINGS IN FROG."""

FROG_IMAGE_1 = """\
  @..@
 (----)
( >__< )
^^ ~~ ^^"""

FROG_IMAGE_2 = """\
  @..@
 (\--/)
(.>__<.)
^^^  ^^^"""

FROG_IMAGE_3 = """\
(l)-(l)
/_____\ 
\_____/"""

FROG_IMAGE_4 = """\
              _   
  __   ___.--'_`. 
 ( _`.'. -   'o` )
 _\.'_'      _.-' 
( \`. )    //\`   
 \_`-'`---'\\\\__,  
  \`        `-\   
   `              """
FROG_IMAGE_5 = """\
                            ,-.
                        _,-' - `--._
                      ,'.:  __' _..-)
                    ,'     /,o)'  ,'
                   ;.    ,'`-' _,)
                 ,'   :.   _.-','
               ,' .  .    (   /
              ; .:'     .. `-/
            ,'       ;     ,'
         _,/ .   ,      .,' ,
       ,','     .  .  . .\,'..__
     ,','  .:.      ' ,\ `\)``
     `-\_..---``````-'-.`.:`._/
     ,'   '` .` ,`- -.  ) `--..`-..
     `-...__________..-'-.._  \ 
        ``--------..`-._ ```
                     ``"""

FROG_IMAGE_6 = """\
           .--._.--.
          ( O     O )
          /   . .   \ 
         .`._______.'.
        /(           )\ 
      _/  \  \   /  /  \_
   .~   `  \  \ /  /  '   ~.
  {    -.   \  V  /   .-    }
_ _`.    \  |  |  |  /    .'_ _
>_       _} |  |  | {_       _<
 /. - ~ ,_-'  .^.  `-_, ~ - .\ 
         '-'|/   \|`-`"""