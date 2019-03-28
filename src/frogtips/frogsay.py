from frogtips import constants
import random
import os


def say(text_to_say, tip_id=0):
    """Display input text as spoken by an ASCII art FROG.

    Formats and prints the given input text so that it appears to come from
    the speech bubble of FROG ASCII art. Automatically figures out the width of
    the ASCII art and sizes the speech bubble appropriately. The maximim width
    of this function's output is determined by constants.FROGSAY_MAX_COLS"""

    # First, pick a random FROG image and determine its width.
    ascii_art = [constants.FROG_IMAGE_1,
                 constants.FROG_IMAGE_2,
                 constants.FROG_IMAGE_3,
                 constants.FROG_IMAGE_4,
                 constants.FROG_IMAGE_5,
                 constants.FROG_IMAGE_6]
    secure_random = random.SystemRandom()
    frog_image = secure_random.choice(ascii_art)
    frog_image_width = get_max_width(frog_image.split("\n"))

    # Determine the width of the terminal
    try:
        columns, rows = os.get_terminal_size(0)
    except OSError:
        columns, rows = os.get_terminal_size(1)

    # Determine the maximum width of the output text.
    # The number 4 is determined by taking one character for each side of the
    # speech bubble plus one space for each side so the output text doesn't
    # appear crammed up next to the side of the speech bubble.
    # TODO: Figure this number out automatically to avoid a hard-coded value
    max_text_width = columns - frog_image_width - 4

    # Chop the input text up into rows short enough to fit the speech bubble.
    formatted_rows = word_wrap(text_to_say, max_text_width)

    # Finally, print everything.
    print_bubble(formatted_rows, frog_image_width, tip_id)
    print(frog_image)


def word_wrap(text_to_wrap, text_width):
    """Chop up and word-wrap a long string of text."""

    this_row = ''
    previous_row = ''
    rows = []

    # Chop up the input text.
    input_words = text_to_wrap.split(' ')

    # Reconstruct the input text word-by-word, then see if the length of the
    # row is longer than the maximum specified width.
    for word in input_words:
        this_row += word + ' '

        if len(this_row) > text_width:
            rows.append(previous_row[:-1])
            this_row = ''
            this_row += word + ' '
        else:
            previous_row = this_row

    # Append this_row to the list of rows if it contains any text at all
    if not this_row == '':
        rows.append(this_row)

    return rows


def print_bubble(rows_to_print=[], frog_image_width=0, tip_id=0):
    """Print a speech bubble containing input text."""

    # figure out the actual length of the longest row of rows_to_print
    tip_width = get_max_width(rows_to_print)
    left_margin = (' ' * frog_image_width)

    bubble_border_top = left_margin + '╔' + ('═' * (tip_width + 2)) + '╗'
    bubble_border_bottom = left_margin + '╚' + ('═' * (tip_width + 2)) + '╝'

    print(bubble_border_top)

    for row in rows_to_print:
        # Add spaces at the end of each row so the speech bubble's ends
        # are aligned
        row += (' ' * (tip_width - len(row)))

        print(left_margin + "║ " + row + " ║")

    print(bubble_border_bottom)

    url = "https://" + constants.FROG_TIPS_DOMAIN + "/#" + str(tip_id)
    num_of_spaces = tip_width - len(url)
    print(left_margin + " /" + (' ' * num_of_spaces) + url)
    print(left_margin + "/")


def get_max_width(text_array):
    """Get the maximum width of a bunch of rows of text."""

    width = 0

    # Figure out the maximum width
    for row in text_array:
        if len(row) > width:
            width = len(row)

    return width