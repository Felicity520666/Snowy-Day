# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define I = Character("Isabella", color="#7e0e06")
define m = Character("Mr.BlindPick", color="#ff0000")


# The game starts here.

label start:

    play music "snow-is-coming-427915.mp3" fadein 1.5
    scene pretty
    with fade
    pause 4.0
    show isabella happy
    with moveinright
    I "Oh my gosh! What a gentle snowy day--exactly the kind of day I love!"
    show isabella smile 
    with dissolve
    I "A new year means a new beginning!"
    show isabella awkward 
    with dissolve
    I "Ummm... a new beginning... what actually counts as one...?"
    show isabella laugh
    with dissolve
    I "Oh oh! I should find myself a boyfriend!"
    show isabella cringe 
    with dissolve
    I "That would definitely be something new, and it's been on my New Year's resolution lists for a while..."
    show isabella shy 
    with dissolve
    I "Yeah... why not start today?"
    show isabella smile 
    with dissolve
    I "I'm going to try an app my friend recommended that connects random users based on shared hobbies, age, and preferences."
    show isabella happy
    with dissolve
    I "I'm curious to see how it goes."
    pause 1.0
    scene connecting
    with fade
    stop music fadeout 2.5
    play music "phone-ringing-382734.mp3"
    pause 5.0
    stop music
    scene done 
    play sound "ding-402325.mp3" volume 2.5
    pause 3.0
    play music "romantic-love-romantics-music-459475.mp3" fadein 2.5
    scene pretty
    with fade
    show unknown 
    with pixellate
    show isabella cringe
    I "Oh ummm... haha... he... hello?"
    I "I ummm... I'm Isabella..."
    m "Haha, hi! You sound a little nervous, Isabella."
    show isabella shy
    with dissolve
    m "Isabella, Isabella... Such a good name..."
    m "Do you know Isabella is a feminine given name of Italian and Spanish origin, meaning \"devoted to God\"..."
    show isabella stunned
    with dissolve
    I "Ummm... so I do know it is a feminine name..."
    show isabella normal 
    with dissolve
    m "Isabella... such a beautiful name..."
    m "{i}Isa{/i} sounds soft and gentle, and {i}bella{/i}--well, it literally means beautiful!"
    m "It feels like a flower you'd find in a quiet garden. Elegant, but not trying too hard..."
    show isabella suprised 
    with dissolve
    I "Excuse me... I think we should stop analyzing my name..."
    show isabella laugh
    with dissolve
    I "So, umm, I'm 25 and I'm looking for a boyfriend..."
    show isabella shy 
    with dissolve
    I "Yeah--straight to the point. I guess I'm very direct..."
    m "Hmmm... 25? That's such a radiant age!"
    show isabella normal
    with dissolve
    m "Now I'm curious. May I ask what you look like? Your height? Overall vibe? And..."
    show isabella awkward
    with dissolve
    I "Hey, young man, could we take this a bit slower?"
    show isabella suprised
    with dissolve
    I "You're asking a lot about me, and I don't even know your name!"
    m "Oh easy! Just call me Jack!"
    show isabella stunned
    with dissolve
    I "Okay, Jack. Do you mind telling me how old you are?"
    show isabella shy
    with dissolve
    m "Mind? Ha, baby!"
    show isabella mad
    m "I'd {i}love{/i} to mind!"
    m "I'd tell you, but then I'd have to charge a fee!"
    show isabella angry
    with dissolve
    m "Hey! What kind of person are you! Can't you treat me a little better, huh?"
    show isabella normal
    with dissolve
    m "Hey, sweetheart! Calm down, will ya?"
    m "Why so serious?! I was just joking!"
    m "I'm 28--three years older than you. Satisfied?"
    show isabella happy
    with dissolve
    I "Ha, so you're one of those funny, charming types, huh?"
    show isabella shy
    with dissolve
    I "Hmph, I don't fall for that easily. I'm not buying that..."
    show isabella glad
    with dissolve
    "Anyway... what are some of your hobbies? I personally {b}love{/b} skating!"
    m "Oh me too babe!"
    show isabella laugh
    with dissolve
    I "Really! Oh my gosh! Do you also like skiing?"
    m "Oh, you bet!"
    show isabella glad
    with dissolve
    m "You have no idea how many tricks I can do!"
    m "How about we go hit the slopes together?"
    show isabella cringe
    I "Ahh, like when?"
    show isabella normal 
    with dissolve
    m "Tomorrow night at 11. See you at Pine Ridge Ski Resort."
    show isabella awkward
    with dissolve
    I "That's too late... And Pine Ridge Ski Resort? I've never heard of that place before..."
    show isabella normal
    with dissolve
    m "I'm a bit of a night owl... I can send you the location."
    show isabella stunned
    with dissolve
    I "Hold on, I'll need to think about it."
    show isabella normal 
    with dissolve
    m "What's there to think about?"
    m "Aren't you super into skiing?"
    m "I'll teach you a bunch of cool jumps and tricks if you go!"
    show isabella stunned
    with dissolve
    I "What should I choose...?"
    menu:
        "Do you dare miss this opportunity?! Of course you should go!":
            jump yes
        "Heck, you literally just met him minutes ago. Don't go!":
            jump no

    label yes:
        show isabella shy
        with dissolve
        I "Yeah... Meet you tomorrow night."
        scene bad with vpunch
        play sound "lose-sfx-365579.mp3"
        play music "sad-or-uneasy-situation-instrumental-171061.mp3" fadein 2.0
        I "I went to the location he gave me... and it turned out I had walked straight into a trap."
        I "Bad Ending"
        return

    label no:
        show isabella awkward
        with dissolve
        I "You know, I just met you, man."
        show isabella suprised
        with dissolve
        I "I can't just go out at night with you to some random place I don't even know."
        scene good
        with fade
        play sound "winner-game-sound-404167.mp3"
        play music "snow-is-coming-427915.mp3" fadein 2.5
        show guy at left
        with moveinleft
        I "I didn't go, but I soon found a sincere boyfriend at my workplace, lol, and had a happy life."
        I "Good Ending"
        return




    return
