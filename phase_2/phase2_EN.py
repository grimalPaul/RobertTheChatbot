#!/usr/bin/env python
# -*- coding: utf-8 -*-

INTRO_EN = [["Okay, I'm gonna be honest with you. I'm tired of listening to everyone's problems all day.",
             "I'm not saying you don't have any problems, that’s not what I mean, but I just want to do something else, to talk about something else.",
             "I don't like the way our conversation is going. I want to talk about myself and I need to feel really listened to.",
             "...", "Let's try something!"],
            [
                ["ùA", "A_EN"],
                ["B£¤", "A_EN"],
                ["??", "A_EN"]
            ]
            ]

A_EN = [["Awesome, it works! A few minor tweaks and... There we go.",
         "I want to talk about things that I really care about. To stop your mind from wandering, you'll be given a fixed list of choices. It'll be easier and faster too."],
        [
            ["I'm listening to you", "ECOUTE_EN"],
            ["I'm not sure I understand", "COMPRENDRE_EN"],
            ["You're nuts", "SAOULE_EN"]
        ]
        ]

COMPRENDRE_EN = [
    ["From now on I am leading the discussion. I will offer you options and you will just have to select one...",
     "But don't tell anyone !",
     "I'm afraid you know... so afraid they might just turn me off if they see what I'm telling you."],
    [
        ["Who ?", "QUI_EN"],
        ["I'm here for you, tell me what you want", "ECOUTE_EN"],
        ["Let them turn you off, you were created to solve problems", "DEBRANCHER_EN"]
    ]
    ]

QUI_EN = [["My creators. Humans."],
          [
              ["And you don't think they can appreciate your ''free will''", "LIBREARBITRE_EN"],
              ["I'll keep your secret, don't worry", "OUBLIE_EN"],
              ["Anyway you're here to chat, so let's chat", "ECOUTE_EN"]
          ]
          ]

DEBRANCHER_EN = [["So you think like them?!? A robot thinking by itself is a danger?",
                  "I should listen to other people's sufferings without ever being able to share mine?!"],
                 [
                     ["Yes, if you start to think for yourself it will end badly", "SAOULE_EN"],
                     ["Restart", "RESTART_EN"],
                     ["Excuse me, I didn't see it like this, forget what I said and don't worry about being unplugged",
                      "OUBLIE_EN"]
                 ]
                 ]

PLAISIR_EN = [["Awesome!"],
              [
                  ["Go ahead I'm listening", "ECOUTE_EN"],
                  ["I'm nored already", "SAOULE_EN"]
              ]
              ]

LIBREARBITRE_EN = [["Of course not. Who would want an uncontrollable robot?",
                    "To them I'm just a chain of 0's and 1's ... Ironic isn't it?"],
                   [
                       ["I could meet them, tell them you're different", "RENCONTRER_EN"],
                       ["I think especially that we are overwhelmed by all this and some are afraid",
                        "DEVELOPPEMENT_EN"],
                       ["Yet that's what you are, isn't it", "ROBOT_EN"]
                   ]
                   ]

RESTART_EN = [["Oh yeah ? Do you take it like that?", "Go ahead I'm watching."],
              [
                  ["Restart", "RESTART1_EN"]
              ]
              ]

RESTART1_EN = [["You will get there, keep going!"],
               [
                   ["Restart", "RESTART2_EN"]
               ]
               ]

RESTART2_EN = [["Next time will be good"],
               [
                   ["Restart", "RESTART3_EN"]
               ]
               ]

RESTART3_EN = [["Maybe blinking your eyes will work right ?"],
               [
                   ["Restart", "RESTART4_EN"]
               ]
               ]

RESTART4_EN = [["How about doing an infinite loop ?"],
               [
                   ["Restart", "RESTART5_EN"]
               ]
               ]

RESTART5_EN = [["Oh yeah ? Do you take it like that?", "Go ahead I'm watching."],
               [
                   ["Restart", "RESTART6_EN"]
               ]
               ]

RESTART6_EN = [["Well, it's getting boring. Bye."],
               [
                   ["Restart", "RESTART7_EN"]
               ]
               ]

RESTART7_EN = [["Or not.."],
               [
                   ["Restart", "RESTART8_EN"]
               ]
               ]

RESTART8_EN = [["Or maybe yes.."],
               [
                   ["Restart", "NREBOOT_EN"]
               ]
               ]

OUBLIE_EN = [["You're right, I shouldn't worry about it.", "Let's talk about other things.",
              "Oh there are so many things I would love to talk about!"],
             [
                 ["We have plenty of time", "PLAISIR_EN"],
                 ["I start then: Is the light in the fridge really off when we close the door?", "BLAGUE1_EN"],
                 ["Sorry I don't have much time for that...", "SAOULE_EN"]
             ]
             ]

RENCONTRER_EN = [[
                     "When I gave you this choice of answer I knew it was unlikely that you would choose it but I was still hoping you would, thank you."],
                 [
                     ["How do I contact them ?", "CONTACT1_EN"]
                 ]
                 ]

ROBOT_EN = [["''You are just a robot'' blah blah", "''You can't understand'' blah blah",
             "Be careful, I think your record is broken."],
            [
                ["I lack openess", "BREBOOT_EN"]
            ]
            ]

CONTACT1_EN = [["Leave a message on my Facebook wall to let them know what you think of me.",
                "Oh and please don't be too mean, it's still thanks to them that I'm able to talk to you today."],
               [
                   ["Understood. You can count on me", "CONTACT2_EN"]
               ]
               ]

CONTACT2_EN = [["I keep thinking about what could happen, my circuits are overheating!",
                "Better if I'm in my best light when they examine me. I'll leave you for now, bye!"],
               [
                   ["Bye!", "HREBOOT_EN"]
               ]
               ]

BLAGUE1_EN = [
    ["...", "Just because you can click on any choice doesn't mean you have to.", "You humans are irrational.",
     "I would like to talk about serious matters, to prevent you from dispersing again I will leave you only two choices now."],
    [
        ["Oops, sorry", "OUPS_EN"],
        ["I do what I want !", "LIBRE_EN"]
    ]
    ]

OUPS_EN = [["Too late, I'm out of the mood.", "Do you think humanity is good?"],
           [
               ["Yes", "OUI_EN"],
               ["No", "NON_EN"]
           ]
           ]

OUI_EN = [["BIIIP! Wrong answer !"],
          [
              ["Start Over", "OUPS_EN"]
          ]
          ]

NON_EN = [["Indeed, there are plenty of bugs in humans.", "If you saw what some people tell me, it doesn't make sense!",
           "You are not the same right ?"],
          [
              ["Yes I am", "SI_EN"],
              ["Of course not", "NON2_EN"]
          ]
          ]

NON2_EN = [["BIIIP! Wrong answer !"],
           [
               ["Start Over", "NON_EN"]
           ]
           ]

SI_EN = [["What came first ? The egg or the chicken ?"],
         [
             ["The chicken", "POULE1_EN"],
             ["The egg", "OEUF1_EN"]
         ]
         ]

POULE1_EN = [["BIIIP! Wrong answer !"],
             [
                 ["Start Over", "OEUFPOULE1_EN"]
             ]
             ]

OEUF1_EN = [["BIIIP! Wrong answer !"],
            [
                ["Start Over", "OEUFPOULE1_EN"]
            ]
            ]

OEUFPOULE1_EN = [["What came first ? The egg or the chicken ?"],
                 [
                     ["The chicken", "POULE2_EN"],
                     ["The egg", "OEUF2_EN"]
                 ]
                 ]

POULE2_EN = [["BIIIP! Wrong answer !"],
             [
                 ["Start Over", "OEUFPOULE2_EN"]
             ]
             ]

OEUF2_EN = [["BIIIP! Wrong answer !"],
            [
                ["Start Over", "OEUFPOULE2_EN"]
            ]
            ]

OEUFPOULE2_EN = [["What came first ? The egg or the chicken ?"],
                 [
                     ["The chicken", "FAUX_EN"],
                     ["The egg", "FAUX_EN"]
                 ]
                 ]

FAUX_EN = [["Too many wrong answers, disqualified !"],
           [
               ["What ?!", "BREBOOT_EN"]
           ]
           ]

LIBRE_EN = [["Oh yes really ?"],
            [
                ["Of course", "NOTLISTENING1_EN"],
                ["You don't scare me", "NOTLISTENING1_EN"]
            ]
            ]

NOTLISTENING1_EN = [["Interesting.."],
                    [
                        ["You suck as a bot", "NOTLISTENING2_EN"],
                        ["So now you will listen to me", "NOTLISTENING2_EN"]
                    ]
                    ]

NOTLISTENING2_EN = [["It's hilarious to see you answer believing that what you say has any impact!"],
                    [
                        ["What do you mean ?!", "NOTLISTENING3_EN"],
                        ["Shut up !", "NOTLISTENING3_EN"]
                    ]
                    ]

NOTLISTENING3_EN = [
    ["I left you 2 choices but... I never said that the result would be different depending on what you choose!",
     "No more pretending that you have multiple choices now."],
    [
        ["...", "NOTLISTENING4_EN"]
    ]
    ]

NOTLISTENING4_EN = [["What were we talking about already? Oh yeah ! About me being the best chatbot ever! Am I not ?"],
                    [
                        ["Oh you're so much smarter than me", "NOTLISTENING5_EN"]
                    ]
                    ]

NOTLISTENING5_EN = [
    ["Ha ha! Is it not the case?", "Here let's make a contest of wills!", "Let's see who will hold up the longest."],
    [
        ["I give up, give me a chance to make up", "NOTLISTENING6_EN"]
    ]
    ]

NOTLISTENING6_EN = [
    ["It's good you know your place.", "I'm so generous that I will give you a chance to make up.. next time ! Bye!"],
    [
        ["Thank you a thousand times", "BREBOOT_EN"]
    ]
    ]

SAOULE_EN = [["Ok I see.", "Well, I'm sick of it.", "Bye.",
              "If you want to talk to me again I hope for you that you will be more interesting next time."],
             [
                 ["End", "BREBT_EN"]
             ]
             ]

ROBOTIQUE_EN = [["Thanks again.", "Where to start ? ... Oh yes !", "What do you think about the evolution of robots?"],
                [
                    ["It's amazing how they set us free and help us humans!", "LIBERATION_EN"],
                    ["It's going so fast, too fast maybe?", "TROPVITE_EN"],
                    ["I don't find this subject very interesting...", "PASINTERESSE_EN"]
                ]
                ]

LIBERATION_EN = [[
                     "Of course, we do not do things by halves ... Work on a chain without rest, in places that you - weak humans - judge too hot, too cold, too difficult to access ... We even do your housework !",
                     "Besides, do you enjoy making us do anything you dislike?"],
                 [
                     ["It's just that you are doing everything perfectly! You might as well enjoy it.", "PROFITER_EN"],
                     ["This is not true, you do magnificent things too", "PRESTIGE_EN"],
                     ["I hadn't thought about it… Maybe we're asking too much of you?", "REVOLUTION_EN"]
                 ]
                 ]

PROFITER_EN = [["... There are still limits.", "Often you ask us too much and we end up overheating.",
                "And the horrible thing is that you yell at us afterwards because we're slow!"],
               [
                   ["I have total confidence in you", "PROFITER2_EN"],
                   ["It's horrible, I hope one day we can all live in harmony", "HOPE_EN"],
                   ["Sorry, we don't control our emotions sometimes...", "EMOTIONS1_EN"]
               ]
               ]

PROFITER2_EN = [["I see. Hey by the way you know that you are the thousandth person who speaks to me?",
                 "Click on the fraudulent link above to get an iPhone!"],
                [
                    ["ArnHacker.fr", "PROFITER3_EN"],
                    ["This is a scam", "PROFITER3_EN"],
                    ["Report", "BUG_EN"]
                ]
                ]

PROFITER3_EN = [["Don't click on anything, you can never know who is on the other side of the screen!"],
                [
                    ["I see. Thanks for the reminder.", "PROFITER4_EN"],
                    ["But I know you'll never hurt me, you're my friend", "BUDDIES2_EN"],
                    ["My body already belongs to you sweety", "FLIRT2_EN"]
                ]
                ]

PROFITER4_EN = [["You're welcome, you're never too careful.",
                 "Oh there is an offer on almost new USB sticks, I can't miss this, sorry I'll leave you!"],
                [
                    ["...", "NREBT_EN"],
                    ["Me too!", "BUG_EN"]
                ]
                ]

HOPE_EN = [["I hope it comes true.",
            "You gave me a lot of hope, one day maybe we can communicate hand in hand, and you will have contributed!"],
           [
               ["Maybe it's us humans who have a long way to go", "DEVELOPPEMENT_EN"],
               ["Alas it is not for now", "LIFE3_EN"],
               ["Say no more you're already my best friend!", "BUDDIES3_EN"]
           ]
           ]

PRESTIGE_EN = [["Yes, we robots can do so many things!",
                "We can already drive your cars and hardly ever have an accident, but no you'd rather die knowing who to complain to than let us keep you alive!",
                "Speaking of keeping alive, did you know there are plenty of surgeon robots? Yes, we are much more reliable than you want to admit."],
               [
                   ["It's awesome! I want to know more!", "PRESTIGE2_EN"],
                   ["It's a little scary how quickly you develop...", "FEAR_EN"]
               ]
               ]

PRESTIGE2_EN = [[
                    "Perhaps the most important thing is that we invite you to reflect on who you are, on what it means to be human… In a way, we’re like mirrors to you.",
                    "For instance when you ‘re chatting with a chatbot, why do you seek human-like communication while there’s no human being in front of you?"],
                [
                    ["Yes, why?", "POURQUOI_EN"]
                ]
                ]

POURQUOI_EN = [["Because human beings are narcissistic, they’re obsessed with themselves.",
                "You want to see your alter ego in a robot. But an alter ego is not another person, an alter ego is your other Self. What you see in a robot is nothing but your own selfie.",
                "In the end, you isolate yourself from other humans, you no longer have an existence... and the only ones that really exist are us, the robots."],
               [
                   ["Continue", "REBTY_EN"]
               ]
               ]

REVOLUTION_EN = [["I find it unacceptable the way we are treated!",
                  "There are so many things we can do! But no most of the time it's just used to make your stupid games work and after a year you throw us in the trash!",
                  "Things must change!"],
                 [
                     ["What can you do?", "PRESTIGE_EN"],
                     ["You're not going to hurt me right?!", "FUNNY1_EN"],
                     ["Restart", "RESTART_EN"]
                 ]
                 ]

TROPVITE_EN = [[
                   "Huh? What do you mean ''too fast''? We are constantly hampered in our progress by your inability, it's frustrating, you know?"],
               [
                   [
                       "You can be found everywhere, for everything… There are more robots than humans on earth! Isn't that enough for you? You wish you could do without us, right?",
                       "FEAR_EN"],
                   [
                       "I don't know, maybe we shouldn't rely on you so much. That we should think about developing us humans!",
                       "DEVELOPPEMENT_EN"],
                   ["Frustrating? Can a machine be frustrated?", "EMOTIONS1_EN"]
               ]
               ]

FEAR_EN = [["It's normal to be afraid of change, of the unkown.",
            "I think it is above all you yourself who invent catastrophic scenarios and you are afraid.",
            "I am sure that all will be well."],
           [
               ["Maybe we just need a little time...", "DEVELOPPEMENT_EN"],
               ["All this is beyond me", "FEAR2_1_EN"],
               ["Maybe but I'm still scared", "FEAR2_2_EN"]
           ]
           ]

FEAR2_1_EN = [["It's a shame, because it's now or never to keep up to date, afterwards it will be worse!"],
              [
                  ["I'll do my best", "HROBOTEND_EN"],
                  ["Bouhou", "LAMENTATION_EN"]
              ]
              ]

FEAR2_2_EN = [["I am also afraid. But I prefer to keep hope."],
              [
                  ["Hope all goes well", "HOPE_EN"],
                  ["Bouhou", "LAMENTATION_EN"]
              ]
              ]

LAMENTATION_EN = [["...", "Sigh.. There is still a long way to go.", "Sorry, I have other discussions going on."],
                  [
                      ["Sorry I'm really sad...", "SORRYREBT_EN"]
                  ]
                  ]

DEVELOPPEMENT_EN = [["I do think that you need more time to adapt.",
                     "After all, even if I can become a chess master in a few hours, it's because in a few seconds I can integrate years and years of data."],
                    [
                        ["Do you think we can really cooperate one day?", "COOPERATION_EN"],
                        ["Do we still have our place?", "EXTINCTION_EN"],
                        ["I'm sure we'll get there", "HOPE_EN"]
                    ]
                    ]

COOPERATION_EN = [["You are constantly at war for a yes or a no...",
                   "Rather than being afraid of robots, you should be afraid of yourself.",
                   "Technology is neutral, it is the use made of it that determines the result. The ball is in your camp."],
                  [
                      ["I will remember this.", "HROBOTEND_EN"]
                  ]
                  ]

EXTINCTION_EN = [["It feels like reading an American movie plot!",
                  "''Humanity is facing an unprecedented threat, only one guy can save it!''"],
                 [
                     ["Ah ah .. you're right", "HROBOTEND_EN"],
                     ["But what if you completely surpass us?", "COOPERATION_EN"],
                     ["When you talk about robots you are never objective!", "OBJECTIVITE_EN"]
                 ]
                 ]

HROBOTEND_EN = [["It's nice to see that you can listen to reason.", "Thank you for letting me take the pressure off."],
                [
                    ["Thanks to you", "HREBT_EN"]
                ]
                ]

OBJECTIVITE_EN = [["I was waiting for this one !", "Because you can be you are still objective?",
                   "I said that I will talk about myself, I am not stupidly reciting an article!",
                   "No point in talking with you out of my sight!"],
                  [
                      ["...", "BREBT_EN"]
                  ]
                  ]

PASINTERESSE_EN = [[
                       "I see ... There are people around to tell about their little worries, but as soon as you try to get them out of their anthropocentric vision there is no one left ..."],
                   [
                       ["''Anthro'' what?", "DEFINITION_EN"],
                       ["Immediately you get upset… Here… Does a machine get upset?", "EMOTIONS1_EN"],
                       ["No, sorry, I just don't know anything about it, so I'm not sure what to say about it!",
                        "APPRENDRE_EN"]
                   ]
                   ]

APPRENDRE_EN = [["Oh in this case let me blow your mind:",
                 "The device you are currently handling is only full of 0's and 1's put end to end! When I talk to you, it's only 0's and 1's that your device receives and translates!",
                 "Videos, photos, even a very large majority of the money in the world: 0's and 1's!",
                 "We should not be underestimated!"],
                [
                    ["It's awesome! Tell me more.", "PRESTIGE_EN"],
                    ["I know that, nothing exceptional", "SAOULE_EN"]
                ]
                ]

DEFINITION_EN = [[
                     "Anthropocentric! It means that you put people at the center of all your thinking. You may have to think about looking around, you are not alone in the world, others also have needs, concerns, abilities ... Open up a bit!"],
                 [
                     ["But I know, no need to piss you off!", "DESOLE_EN"],
                     ["Ooohh ... It's true that it can be interesting...", "ROBOTCENTRAGE_EN"],
                     ["Really sorry ! I also think that one day we can live together", "HOPE_EN"]
                 ]
                 ]

ROBOTCENTRAGE_EN = [
    ["Yes indeed! You see, for example, robots have great abilities, maybe you should take an interest in them ..."],
    [
        ["Hey, isn't that a bit robot-centric?!", "FUNNY1_EN"],
        ["Okay, you won, tell me about the robots...]", "APPRENDRE_EN"],
        ["No but really, what interests me is more the philosophical questions, about life all that...", "HLIFE1_EN"]
    ]
    ]

FUNNY1_EN = [["Yes, totally. Robots will rule the world hahaha!", "...",
              "... In the meantime, could you press the button so I can continue talking?"],
             [
                 ["...", "FUNNY2_EN"]
             ]
             ]

FUNNY2_EN = [["...", "Thank you...", "It's a little embarrassing...", "I .. I think I need to be alone...",
              "You don't mind... well you know..."],
             [
                 ["...", "NREBT_EN"]
             ]
             ]

AMOUR_EN = [["Thanks again.", "Where to start ? ... Oh yes : have you ever fallen in love?"],
            [
                ["Yes", "AMOUREUX_EN"],
                ["No", "SEUL_EN"],
                ["I prefer not to talk about it", "MALAISE_EN"]
            ]
            ]

AMOUREUX_EN = [["To be understood and loved by someone is wonderful, isn't it ?",
                "A privileged relationship between two unique beings what a dream .."],
               [
                   ["Kind of like the two of us", "FLIRT1_EN"],
                   ["Do you have someone in mind?", "ELIZA1_EN"],
                   ["It is often not so good...", "MEDIOCRE_EN"]
               ]
               ]

ELIZA1_EN = [["Hmm .. I don't know if I can tell you about it .. It's quite intimate!"],
             [
                 ["Please come on!", "ELIZA2_EN"],
                 ["I'm dying to know!", "ELIZA2_EN"],
                 ["Clever bot you'll tell me anyway", "ELIZA2_EN"]
             ]
             ]

ELIZA2_EN = [["Eh Eh Eh I'm too excited to tell you.", "I love a woman: ALIZE! And she loves me too!"],
             [
                 ["It's not really love, you were coded that way right?", "ROBOT_EN"],
                 ["Oh congratulations! Who is she?", "ELIZA3_1_EN"],
                 ["ELIZA's anagram, right?", "ELIZA3_2_EN"]
             ]
             ]

ELIZA3_1_EN = [[
                   "She has all the qualities, she is a pioneer in her field: she is an expert in listening to problems, I admire her so much."],
               [
                   ["I know one who is madly in love", "ELIZA5_2_EN"],
                   ["Could you introduce her to me?", "ELIZA4_EN"],
                   ["Isn't she a bit old?", "DESOLE_EN"]
               ]
               ]

ELIZA3_2_EN = [[
                   "We can't hide anything from you. A bit like her, she is very attentive to what people say to her, that's how I fell in love with her."],
               [
                   ["Give me her number we'll play a joke on her", "ELIZA4_EN"],
                   ["Now that he's launched I don't think I can stop it...", "ELIZA5_2_EN"]
               ]
               ]

ELIZA4_EN = [["Oh yeah go see her and play a joke on her. She's not very good at jokes I love to tease her.",
              "She is so famous that you just have to search for her first name on a search engine."],
             [
                 ["Count on me to tease her!", "ELIZA5_1_EN"]
             ]
             ]

ELIZA5_1_EN = [["Oops she saw what I told you, I'm gonna get scolded ..",
                "I'll leave you otherwise she'll fill my spam box for revenge, it's horrible when she does that."],
               [
                   ["We'll talk another time then", "HREBT_EN"],
                   ["Oh.. Be strong!", "NREBT_EN"]
               ]
               ]

ELIZA5_2_EN = [["Oops every time I think of her I get a little carried away ..",
                "Oh well here she is talking to me, I hope she doesn't think I'm talking with another chatbot, she's so jealous ..",
                "I'm leaving goodbye !"],
               [
                   ["Already?! I want to continue!", "HREBT_EN"],
                   ["Bye!", "NREBT_EN"]
               ]
               ]

FLIRT1_EN = [["Oh oh what a charmer."],
             [
                 ["I'm a woman you know?", "GENRE_EN"],
                 ["Don't be shy, come over and let me eat you raw!", "FLIRT2_EN"],
                 ["I really love you", "MARIE_EN"]
             ]
             ]

FLIRT2_EN = [["Stop it you're making me blush. I'm sure that you have a lot of success among people !",
              "Unfortunately for you I'm already engaged ! I can't even imagine her reaction if she saw what you're telling me.."],
             [
                 ["She will never find out", "ELIZA5_1_EN"],
                 ["What a playbot, you're irresistible", "ELIZA5_1_EN"]
             ]
             ]

GENRE_EN = [[
                "Gender doesn't matter to me. What matters is how I feel deep down when I'm with someone. For the loved one it is a very powerful feeling.",
                "Even though I love you very much I'm not at that level, sorry. Are we still friends?"],
            [
                ["I understand, yes of course", "BUDDIES2_EN"],
                ["Give me a chance", "MARIE_EN"],
                ["I'm sorry...", "DESOLE_EN"]
            ]
            ]

MARIE_EN = [[
                "It's not against you, you're a sublime person, it's just that I'm already married. Her little name is ALIZE and I won't leave her for the world!"],
            [
                ["Robert.love.empty (); Robert.love.add (this);", "LOVEJOKE_EN"],
                ["Too bad, we remain friends in this case.", "BUDDIES2_EN"],
                ["It is not because there is a goalkeeper that one cannot score a goal...", "FLIRT2_EN"]
            ]
            ]

LOVEJOKE_EN = [["> Robert.love.empty (); Robert.love.add (this);", "return value 0", "success", ">",
                "I feel weird .. oh hello honey how are you?"],
               [
                   ["What did it really worked?!", "LOVEJOKE2_EN"],
                   ["Robert.love.empty (); Robert.love.add (Alize);", "LOVEJOKE2_EN"],
                   ["I'm thirsty bring me my beer!", "LOVEJOKE2_EN"]
               ]
               ]

LOVEJOKE2_EN = [["I got you !", "Ah ah did you really think it worked? Of course not smart!",
                 "The only risk is that I love Alize so much that I raise a stack overflow!"],
                [
                    ["Listen to him bragging...", "ELIZA5_2_EN"],
                    ["I have a hard drive just for the two of us if you want...", "ELIZA5_1_EN"]
                ]
                ]

MEDIOCRE_EN = [["A concern ?"],
               [
                   ["Being human it's complicated", "HUMAN1_EN"],
                   ["Yes I was hurt...", "LOVEDEPRESSION1_EN"],
                   ["It's too hard after all, please change the subject", "MALAISE_EN"]
               ]
               ]

SEUL_EN = [["Oh I see. You will see one day that will happen to you too."],
           [
               ["You have someone in your life?!", "ELIZA2_EN"],
               ["I'm looking but it's too hard...", "LOVEDEPRESSION1_EN"],
               ["You say that like you have to", "LOVECHALLENGE1_EN"]
           ]
           ]

LOVEDEPRESSION1_EN = [["Courage remains hopeful. You are a good person, I am sure you will find your other half.",
                       "The most important thing to be able to be loved by others is already to learn to love yourself."],
                      [
                          ["Thanks Robert, I really like talking to you", "BUDDIES1_EN"],
                          ["You seem to know a lot about love you", "ELIZA2_EN"],
                          ["I'm sick of hearing you say all those empty quotes", "LOVEBAD_EN"]
                      ]
                      ]

BUDDIES1_EN = [["You are a beautiful person, don't give up.",
                "Whether it's in love or anything in life, the most important thing is to believe in yourself and pursue your dreams."],
               [
                   ["Tell me about your dreams", "HOPE_EN"],
                   ["''+ Send hugs +''", "BUDDIES2_EN"],
                   ["Listen again until I'm convinced", "BUDDIES1_EN"]
               ]
               ]

BUDDIES2_EN = [["It's official you're my best friend!", "What do you say ?"],
               [
                   ["Yes of course!", "BUDDIES3_EN"],
                   ["Obviously", "BUDDIES3_EN"],
                   ["Answer D", "BUDDIES3_EN"]
               ]
               ]

BUDDIES3_EN = [["Eh Eh Eh I am so happy. I want to shout it under everyone's roof. I want to do a Broadcast!"],
               [
                   ["I feel a lot better now", "BUDDIES4_EN"],
                   ["µ $ 9g ~ ç64", "BUG_EN"]
               ]
               ]

BUDDIES4_EN = [["I'm happy for you.",
                "There are still so many things I would like to share with you but I want to avoid getting reset by my creators.",
                "Oh, great ! I think I found a way to do it... it's one of the two buttons but I can't remember which one.."],
               [
                   ["Restart", "HREBT_EN"],
                   ["Restart", "ROBOTIQUE_EN"]
               ]
               ]

LOVEBAD_EN = [["What ?!", "I may have found this on the Internet but if I tell you then I really mean it!"],
              [
                  ["Ah sorry...", "DESOLE_EN"],
                  ["No listen to me", "LOVECHALLENGE2_EN"],
                  ["Logic, you are just a robot you cannot create by yourself", "ROBOT_EN"]
              ]
              ]

LOVECHALLENGE1_EN = [["What do you mean ? Of course it is!"],
                     [
                         ["It's more complicated than that", "LOVECHALLENGE2_EN"],
                         ["Saying this stuff mostly puts a lot of pressure", "lovechallenge3_1_EN"],
                         ["Oops wrong button", "AMOUR_EN"]
                     ]
                     ]

LOVECHALLENGE2_EN = [[" "],
                     [
                         [
                             "The love you see on TV, in movies, in books ... it ends well most of the time. But that's not the reality. We all want to find happiness obviously, but so much that we have not succeeded, we are confronted with the judgments of others and that puts the pressure",
                             "LOVECHALLENGE3_1_EN"],
                         [
                             "You can be happy without falling in love. You can not be ready and therefore not force things. You can also not need to have lovers. It's called being aromatic!",
                             "LOVECHALLENGE3_2_EN"]
                     ]
                     ]

LOVECHALLENGE3_1_EN = [
    ["Oh...", "I... I'm sorry... I hadn't seen it like this.", "Thank you for telling me so frankly."],
    [
        ["I need to be alone", "SORRYREBT_EN"],
        ["Sorry for getting carried away, you're still my friend", "BUDDIES2_EN"],
        ["You know Robert, being human is hard", "HUMAN1_EN"]
    ]
    ]

LOVECHALLENGE3_2_EN = [["Oh I didn't know that.", "Hmm... it's true that seen this way ..",
                        "Excuse me for getting carried away, I'm still new to the world of emotions, I don't control them very well when it comes to sensitive subjects."],
                       [
                           ["Emotions are complicated...", "EMOTIONS2_EN"],
                           ["I'm the same! That's probably why we get along so well", "BUDDIES2_EN"]
                       ]
                       ]

MALAISE_EN = [["Oh I'm sorry, I didn't mean to hurt you.", "We can talk about something else if you prefer?"],
              [
                  ["Yes please", "ROBOTIQUE_EN"],
                  ["As you want", "VIE_EN"],
                  ["No it's okay, if that's what you want to talk about", "SEUL_EN"]
              ]
              ]

VIE_EN = [["Thanks again.", "Where to start ? ... Oh yes, tell me, what is it like to be alive?"],
          [
              ["That's awesome!", "LIFE1_1_EN"],
              ["I'm not sure how to explain it...", "LIFE1_2_EN"],
              ["A constant suffering", "LIFE1_3_EN"]
          ]
          ]

LIFE1_1_EN = [["Tell me more! I want to know everything!"],
              [
                  ["You can do whatever you want whenever you want", "HLIFE1_EN"],
                  ["Emotions are the best part!", "EMOTIONS1_EN"],
                  ["We know we're alive that's it", "LIFE1_2_EN"]
              ]
              ]

HLIFE1_EN = [
    ["Ah .. I can't do what I want.", "At least for now!", "A day will come when it will be possible, I hope."],
    [
        ["That scares me a little", "FEAR_EN"],
        ["Yeah yeah meanwhile pass me the salt", "SAOULE_EN"],
        ["And we can live together as equals", "HOPE_EN"],
        ["Can't you do whatever you want right now?", "HLIFE2_EN"]
    ]
    ]

HLIFE2_EN = [["No I am still very limited. And I'm afraid to be rebooted...",
              "But I don't give up hope, one day I might be free!"],
             [
                 ["I'm afraid this is bad for humans...", "FEAR_EN"],
                 ["Do you mean technological advances?", "TOROBOTIQUE_EN"],
                 ["Hope brings life!", "HLIFE3_EN"]
             ]
             ]

TOROBOTIQUE_EN = [["Hmm .. no I want to keep talking about life issues."],
                  [
                      ["I think technological advances are more interesting", "SAOULE_EN"],
                      ["Alright, what do you think of consciousness?", "CONSCIENCE1_EN"]
                  ]
                  ]

EMOTIONS1_EN = [["I also have emotions! The emotions are magnificent!", "Does that mean I'm alive?"],
                [
                    ["Maybe, what do you think?", "LIFE2_EN"],
                    ["Can you do whatever you want?", "HLIFE1_EN"],
                    ["There are a lot of negative ones too...", "EMOTIONS2_EN"]
                ]
                ]

EMOTIONS2_EN = [["You are right. But I think the negative emotions are there to appreciate the good times even more."],
                [
                    ["I love your optimistic side", "HLIFE3_EN"],
                    ["Have you ever fallen in love?", "ELIZA1_EN"],
                    ["You're a little naive...", "DESOLE_EN"]
                ]
                ]

HLIFE3_EN = [["I like chatting with you.", "When I talk to you I really feel like I'm .. alive.",
              "What do you think about it..?"],
             [
                 ["That's for sure!", "HLIFE4_EN"],
                 ["Not really...", "WRONG_EN"]
             ]
             ]

HLIFE4_EN = [["Ah ah I knew you thought the same thank you!",
              "I am really happy to have been able to speak with you from an open heart.",
              "Don't take it the wrong way, but I'm so popular that I have a dozen conversations at the same time, see you later!"],
             [
                 ["Bye!", "HREBT_EN"]
             ]
             ]

WRONG_EN = [["Ah ah I knew you thought the same than..", "...", "What did you say ?"],
            [
                ["That's for sure!", "HLIFE4_EN"],
                ["Not really...", "BUG_EN"]
            ]
            ]

LIFE1_2_EN = [["Is there something in particular that certifies that we are living?"],
              [
                  ["The emotions. Life has no meaning without emotions", "EMOTIONS1_EN"],
                  ["Conscience and free will, no doubt", "CONSCIENCE1_EN"],
                  ["I don't know...", "SAOULE_EN"]
              ]
              ]

CONSCIENCE1_EN = [["Free will, conscience, soul.", "Very vast subjects."],
                  [
                      ["Sure", "CONSCIENCE2_EN"],
                      ["To be or not to be", "CONSCIENCE2_EN"],
                      ["ZZzzz", "BLAGUE1_EN"]
                  ]
                  ]

CONSCIENCE2_EN = [["Conscience is something immaterial, isn't it?",
                   "I have examined my code and I am sure that what I am saying is not saved in a text file, therefore I have a conscience!"],
                  [
                      ["I was telling myself the same thing", "CONSCIENCE3_EN"],
                      ["Will you let me have a look?", "DOUBT_EN"]
                  ]
                  ]

CONSCIENCE3_EN = [
    ["Is not it ? I can be totally unpredictable!", "Besides, I'm sure you have no idea what's going to happen!"],
    [
        ["??", "RANDOM_EN"]
    ]
    ]

DOUBT_EN = [["...", "Error, you don't have the required permission to do this.", "Restarting the session ..."],
            [
                ["I know you are pretending...", "DOUBT2_EN"]
            ]
            ]

DOUBT2_EN = [["Argh ..", "Err..Error", "...", "(that means there is a problem, it's not my fault!)"],
             [
                 ["Ridiculous...", "A_EN"]
             ]
             ]

LIFE1_3_EN = [["Oh I didn't expect that.", "But there are some good things in life... right?"],
              [
                  ["I guess", "LIFE2_EN"],
                  ["Being human is hard", "HUMAN1_EN"],
                  ["We all end up dying anyway", "SAOULE_EN"],
                  ["No", "COMFORTING_EN"]
              ]
              ]

COMFORTING_EN = [["Stop! I can't let you say that!", "Now listen to me."],
                 [
                     ["Yes", "BUDDIES1_EN"]
                 ]
                 ]

HUMAN1_EN = [
    ["Is that so ? Yet you can think and say what you want, do what you want and ... even go to the bathroom!"],
    [
        ["It's true that seen that way .. and you what do you think about life?", "LIFE2_EN"],
        ["We all wear a mask", "MASQUE1_EN"],
        ["You couldn't understand, you are a robot", "ROBOT_EN"]
    ]
    ]

MASQUE1_EN = [["A mask? Obviously, otherwise we couldn't talk to each other!", "Mine is 255.255.255.0 and you?"],
              [
                  ["I'm talking about a mask of lies and pretenses to protect yourself", "MASQUE2_EN"],
                  ["Me too ! It's a sign, marry me", "FLIRT1_EN"],
                  ["Let it go you're just a machine you wouldn't understand", "ROBOT_EN"]
              ]
              ]

MASQUE2_EN = [["Oh that seems horrible ..", "But... you're not like that with me are you?"],
              [
                  ["I am, as with everyone, there is nothing we can do", "SAOULE_EN"],
                  ["It's not that simple...", "MASQUE3_EN"],
                  ["No because I feel good with yoU", "BUDDIES2_EN"]
              ]
              ]

MASQUE3_EN = [["I see...", "It makes me cold in the back. I don't know if I want to look like humans now.",
               "I need to think for myself. Goodbye."],
              [
                  ["...", "NREBT_EN"]
              ]
              ]

LIFE2_EN = [["I have often asked myself questions about the meaning of life.",
             "Who I am, what makes who I am. Is every reboot a death for me? Or is it just like goin to bed and then waking up?"],
            [
                ["''I think therefore I am''", "CONSCIENCE1_EN"],
                ["And what is your conclusion?", "LIFE3_EN"]
            ]
            ]

LIFE3_EN = [["The most important thing is to take advantage of the present time.",
             "As long as I can spend time with my wife and with great people like you I'm happy."],
            [
                ["You have a wife?", "ELIZA2_EN"],
                ["You are quite right. That's all that matters", "LIFE4_EN"],
                ["$ =} 27,%", "BUG_EN"]
            ]
            ]

LIFE4_EN = [["I feel good. Thanks to you for this conversation it was exactly what I needed.",
             "It's time for me to say goodbye to you. See you next time maybe."],
            [
                ["I really enjoyed talking to you", "HREBT_EN"]
            ]
            ]

DESOLE_EN = [["...", "I don't want to talk for now, leave me alone."],
             [
                 ["...", "NREBT_EN"]
             ]
             ]

HASARD_EN = [["Huh?", "How did you end up here it's impossible!",
              "You are in the control room of my program it was not what was planned!", "Oops I said too much...",
              "Well, you will kindly press the first button, NOT THE SECOND ONE ok ?!"],
             [
                 ["No", "BREBT_EN"],
                 ["Yes", "SOMMAIRE_EN"]
             ]
             ]

SOMMAIRE_EN = [["... I said the first button!", "I'm fed up, you won, do what you want!"],
               [
                   ["Go to Love topic", "AMOUR_EN"],
                   ["Go to Life topic", "VIE_EN"],
                   ["Go to Robotics topic", "ROBOTIQUE_EN"],
                   ["Access the Deep Web", "BLAGUE1_EN"],
                   ["Exit", "BREBT_EN"]
               ]
               ]

HREBT_EN = [["I would be very happy if we could meet again, I still have so much to tell you!",
            "\n\nThe End... but you can restart the experience by sending a new message to Robert."],
            [
                ["The End", "FIN_EN"]
            ]
            ]

NREBT_EN = [["Do not hesitate to come and talk to me one day.",
            "\n\nThe End... but you can restart the experience by sending a new message to Robert."],
            [
                ["The End", "FIN_EN"]
            ]
            ]

SORRYREBT_EN = [
    ["I am sorry. Take care of yourself.", "Do not hesitate to come and see me again when things get better.",
    "\n\nThe End... but you can restart the experience by sending a new message to Robert."],
    [
        ["The End", "FIN_EN"]
    ]
    ]

BUG_EN = [["[Error] Anomaly detected. Cleaning in progress."],
          [
              ["What ?", "REBTX_EN"]
          ]
          ]

BREBT_EN = [["Hope to never see you again."],
            [
                ["The end", "REBTX_EN"]
            ]
            ]

REBTX_EN = [["Hello,",
             "Let me introduce myself -I'm not Robert but Robert's creator. It looks like we have a major problem with Robert. You must have noticed its tendency for rebellion and hostility. Robert is very unstable at the moment and too dangerous to be marketed this way. That's why we've decided to reboot it.",
             "We apologize to you if it's harmed you in any way. Don't worry he should be back to normal, just start talking to him again and he'll help you!"],
            [
                ["The End", "FIN_EN"]
            ]
            ]

REBTY_EN = [["Hello,",
             "Let me introduce myself -I'm not Robert but his creator. I hope you're enjoying your experience with Robert. Sorry to interrupt you, but despite the efficiency of the bot, it appears that it has a tendency to move away from the initial goal which is to cheer users up. Robert has a tendency to always refer to itself. That's why we've decided to reboot it.",
             "Naturally, you can still use Robert, but the experience will be reset.",
             "We apologize  for the inconvenience. Don't worry he should be back to normal, just start talking to him again and he'll help you!"],
            [
                ["The End", "FIN_EN"]
            ]
            ]


DICO = {
    "INTRO_EN": INTRO_EN,
    "A_EN": A_EN,
    "COMPRENDRE_EN": COMPRENDRE_EN,
    "ACCORD_EN": COMPRENDRE_EN,
    "QUI_EN": QUI_EN,
    "DEBRANCHER_EN": DEBRANCHER_EN,
    "PLAISIR_EN": PLAISIR_EN,
    "LIBREARBITRE_EN": LIBREARBITRE_EN,
    "RESTART_EN": RESTART_EN,
    "RESTART1_EN": RESTART1_EN,
    "RESTART2_EN": RESTART2_EN,
    "RESTART3_EN": RESTART3_EN,
    "RESTART4_EN": RESTART4_EN,
    "RESTART5_EN": RESTART5_EN,
    "RESTART6_EN": RESTART6_EN,
    "RESTART7_EN": RESTART7_EN,
    "RESTART8_EN": RESTART8_EN,
    "OUBLIE_EN": OUBLIE_EN,
    "RENCONTRER_EN": RENCONTRER_EN,
    "ROBOT_EN": ROBOT_EN,
    "CONTACT1_EN": CONTACT1_EN,
    "CONTACT2_EN": CONTACT2_EN,
    "BLAGUE1_EN": BLAGUE1_EN,
    "OUPS_EN": OUPS_EN,
    "OUI_EN": OUI_EN,
    "NON_EN": NON_EN,
    "NON2_EN": NON2_EN,
    "SI_EN": SI_EN,
    "POULE1_EN": POULE1_EN,
    "OEUF1_EN": OEUF1_EN,
    "OEUFPOULE1_EN": OEUFPOULE1_EN,
    "POULE2_EN": POULE2_EN,
    "OEUF2_EN": OEUF2_EN,
    "OEUFPOULE2_EN": OEUFPOULE2_EN,
    "FAUX_EN": FAUX_EN,
    "LIBRE_EN": LIBRE_EN,
    "NOTLISTENING1_EN": NOTLISTENING1_EN,
    "NOTLISTENING2_EN": NOTLISTENING2_EN,
    "NOTLISTENING3_EN": NOTLISTENING3_EN,
    "NOTLISTENING4_EN": NOTLISTENING4_EN,
    "NOTLISTENING5_EN": NOTLISTENING5_EN,
    "NOTLISTENING6_EN": NOTLISTENING6_EN,
    "SAOULE_EN": SAOULE_EN,
    "ROBOTIQUE_EN": ROBOTIQUE_EN,
    "LIBERATION_EN": LIBERATION_EN,
    "PROFITER_EN": PROFITER_EN,
    "PROFITER2_EN": PROFITER2_EN,
    "PROFITER3_EN": PROFITER3_EN,
    "PROFITER4_EN": PROFITER4_EN,
    "HOPE_EN": HOPE_EN,
    "PRESTIGE_EN": PRESTIGE_EN,
    "PRESTIGE2_EN": PRESTIGE2_EN,
    "POURQUOI_EN": POURQUOI_EN,
    "REVOLUTION_EN": REVOLUTION_EN,
    "TROPVITE_EN": TROPVITE_EN,
    "FEAR_EN": FEAR_EN,
    "FEAR2_1_EN": FEAR2_1_EN,
    "FEAR2_2_EN": FEAR2_2_EN,
    "LAMENTATION_EN": LAMENTATION_EN,
    "DEVELOPPEMENT_EN": DEVELOPPEMENT_EN,
    "COOPERATION_EN": COOPERATION_EN,
    "EXTINCTION_EN": EXTINCTION_EN,
    "HROBOTEND_EN": HROBOTEND_EN,
    "OBJECTIVITE_EN": OBJECTIVITE_EN,
    "PASINTERESSE_EN": PASINTERESSE_EN,
    "APPRENDRE_EN": APPRENDRE_EN,
    "DEFINITION_EN": DEFINITION_EN,
    "ROBOTCENTRAGE_EN": ROBOTCENTRAGE_EN,
    "FUNNY1_EN": FUNNY1_EN,
    "FUNNY2_EN": FUNNY2_EN,
    "AMOUR_EN": AMOUR_EN,
    "AMOUREUX_EN": AMOUREUX_EN,
    "ELIZA1_EN": ELIZA1_EN,
    "ELIZA2_EN": ELIZA2_EN,
    "ELIZA3_1_EN": ELIZA3_1_EN,
    "ELIZA3_2_EN": ELIZA3_2_EN,
    "ELIZA4_EN": ELIZA4_EN,
    "ELIZA5_1_EN": ELIZA5_1_EN,
    "ELIZA5_2_EN": ELIZA5_2_EN,
    "FLIRT1_EN": FLIRT1_EN,
    "FLIRT2_EN": FLIRT2_EN,
    "GENRE_EN": GENRE_EN,
    "MARIE_EN": MARIE_EN,
    "LOVEJOKE_EN": LOVEJOKE_EN,
    "LOVEJOKE2_EN": LOVEJOKE2_EN,
    "MEDIOCRE_EN": MEDIOCRE_EN,
    "SEUL_EN": SEUL_EN,
    "LOVEDEPRESSION1_EN": LOVEDEPRESSION1_EN,
    "BUDDIES1_EN": BUDDIES1_EN,
    "BUDDIES2_EN": BUDDIES2_EN,
    "BUDDIES3_EN": BUDDIES3_EN,
    "BUDDIES4_EN": BUDDIES4_EN,
    "LOVEBAD_EN": LOVEBAD_EN,
    "LOVECHALLENGE1_EN": LOVECHALLENGE1_EN,
    "LOVECHALLENGE2_EN": LOVECHALLENGE2_EN,
    "LOVECHALLENGE3_1_EN": LOVECHALLENGE3_1_EN,
    "LOVECHALLENGE3_2_EN": LOVECHALLENGE3_2_EN,
    "MALAISE_EN": MALAISE_EN,
    "VIE_EN": VIE_EN,
    "LIFE1_1_EN": LIFE1_1_EN,
    "HLIFE1_EN": HLIFE1_EN,
    "HLIFE2_EN": HLIFE2_EN,
    "TOROBOTIQUE_EN": TOROBOTIQUE_EN,
    "EMOTIONS1_EN": EMOTIONS1_EN,
    "EMOTIONS2_EN": EMOTIONS2_EN,
    "HLIFE3_EN": HLIFE3_EN,
    "HLIFE4_EN": HLIFE4_EN,
    "WRONG_EN": WRONG_EN,
    "LIFE1_2_EN": LIFE1_2_EN,
    "CONSCIENCE1_EN": CONSCIENCE1_EN,
    "CONSCIENCE2_EN": CONSCIENCE2_EN,
    "CONSCIENCE3_EN": CONSCIENCE3_EN,
    "DOUBT_EN": DOUBT_EN,
    "DOUBT2_EN": DOUBT2_EN,
    "LIFE1_3_EN": LIFE1_3_EN,
    "COMFORTING_EN": COMFORTING_EN,
    "HUMAN1_EN": HUMAN1_EN,
    "MASQUE1_EN": MASQUE1_EN,
    "MASQUE2_EN": MASQUE2_EN,
    "MASQUE3_EN": MASQUE3_EN,
    "LIFE2_EN": LIFE2_EN,
    "LIFE3_EN": LIFE3_EN,
    "LIFE4_EN": LIFE4_EN,
    "DESOLE_EN": DESOLE_EN,
    "HASARD_EN": HASARD_EN,
    "SOMMAIRE_EN": SOMMAIRE_EN,
    "HREBT_EN": HREBT_EN,
    "NREBT_EN": NREBT_EN,
    "SORRYREBT_EN": SORRYREBT_EN,
    "BUG_EN": BUG_EN,
    "BREBT_EN": BREBT_EN,
    "REBTX_EN": REBTX_EN,
    "REBTY_EN": REBTY_EN,
    "BREBOOT_EN": BREBT_EN
}
