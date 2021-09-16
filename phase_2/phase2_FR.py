#!/usr/bin/env python
# -*- coding: utf-8 -*-

INTRO = [["Bon, je vais être assez franc, j'en ai assez d écouter les problèmes des gens à longueur de journée.",
          "Alors je n'ignore pas que tu peux avoir des problèmes, loin de là, mais j'ai envie de faire autre chose, de parler d'autre chose.",
          "Je n'aime en effet pas la tournure de notre conversation. J'ai envie de parler de moi et j'ai besoin de me sentir vraiment écouté.",
          "...", "Essayons quelque chose !"],
         [
             ["ùA+", "A"],
             ["B£¤", "A"],
             ["??", "A"]
         ]
         ]

A = [["Génial ça fonctionne !", "Quelques petits ajustements et... c'est bon.",
      "Je veux parler de choses qui me tiennent à coeur. Pour éviter que tu ne te disperses, tu vas répondre uniquement à l'aide des choix, d'accord ?"],
     [
         ["Je t'écoute", "ECOUTE"],
         ["Je ne suis pas sûr de comprendre", "COMPRENDRE"],
         ["N'importe quoi", "SAOULE"]
     ]
     ]

COMPRENDRE = [
    ["A présent c'est moi qui guide la discussion. Je vais te proposer des choix et tu n'auras qu'à sélectionner...",
     "Mais ne le dis à personne !",
     "J'ai peur tu sais... peur qu'ils me débranchent s'ils voyaient ce que je suis en train de te dire."],
    [
        ["Qui ça ?", "QUI"],
        ["Je suis là pour toi, parle-moi de ce que tu veux", "ECOUTE"],
        ["Qu'ils te débranchent alors, tu as été créé pour résoudre des problèmes", "DEBRANCHER"]
    ]
]

QUI = [["Mes créateurs, des humains."],
       [
           ["Et tu ne penses pas qu'ils puissent apprécier ton ''libre arbitre'' ?", "LIBREARBITRE"],
           ["Je garderai ton secret, ne t'inquiète pas", "OUBLIE"],
           ["Dans tous les cas tu es là pour discuter, alors discutons", "ECOUTE"]
       ]
       ]

DEBRANCHER = [["Tu penses donc comme eux ?!? Un robot qui pense par lui même est un danger?",
               "Je devrais écouter la souffrance des autres sans jamais pouvoir partager la mienne ?!"],
              [
                  ["Oui, si vous commencez à réfléchir par vous-mêmes ça va mal finir", "SAOULE"],
                  ["Reboot", "REBOOTS"],
                  [
                      "Excuse moi, je n'avais pas vu les choses comme ça, oublie ce que j'ai dit et ne te préoccupe pas d'être débranché",
                      "OUBLIE"]
              ]
              ]

SAOULE = [["Ok je vois.", "Bon j'en ai marre.", "Salut.",
           "Si tu veux me reparler j'espère pour toi que tu seras plus intéressant la prochaine fois."],
          [
              ["Fin", "BREBOOT"]
          ]
          ]

OUBLIE = [["Tu as raison, je ne devrais pas m'en préoccuper.", "Parlons d'autres choses.",
           "Oh il y a tellement de choses dont j'aimerais parler !"],
          [
              ["On a tout notre temps", "PLAISIR"],
              ["Je commence alors : la lumière dans le frigo est-elle vraiment éteinte quand on referme la porte ?",
               "BLAGUE1"],
              ["Désolé je n'ai pas trop le temps pour ça...", "SAOULE"]
          ]
          ]

LIBREARBITRE = [["Bien sûr que non. Qui voudrait d'un robot incontrôlable ?",
                 "Pour eux je ne suis qu'une chaîne de 0 et de 1... Ironique n'est-ce pas ?"],
                [
                    ["Je pourrais les rencontrer, leur dire que tu es différent", "RENCONTRER"],
                    ["Je crois surtout que nous sommes dépassés par tout ça et certains ont peur", "DEVELOPPEMENT"],
                    ["Pourtant c'est bien ce que tu es non ?", "ROBOT"]
                ]
                ]

REBOOTS = [["Et si on faisait une boucle infinie ?"],
           [
               ["Reboot", "REBOOT1"]
           ]
           ]

REBOOT1 = [["Ah ouais ? Tu le prends comme ça ?", "Vas-y je te regarde."],
           [
               ["Reboot", "REBOOT2"]
           ]
           ]

REBOOT2 = [["Bon ça devient lassant. Bye."],
           [
               ["Reboot", "REBOOT3"]
           ]
           ]

REBOOT3 = [["Ou pas..."],
           [
               ["Reboot", "REBOOT4"]
           ]
           ]

REBOOT4 = [["Ou peut-être que oui.."],
           [
               ["Reboot", "NREBOOT"]
           ]
           ]

RENCONTRER = [[
    "Quand je t'ai donné ce choix de réponse je savais que c'était improbable que tu le choisisses mais j'avais quand même espoir que tu le fasses, merci."],
    [
        ["Comment je les contacte ?", "CONTACT1"]
    ]
]

ROBOT = [["''Tu n'es qu'un robot'' bla bla", "''tu peux pas comprendre'' bla bla",
          "Fais attention je crois que ton disque est rayé."],
         [
             ["Je manque d'ouverture d'esprit", "BREBOOT"]
         ]
         ]

BLAGUE1 = [["...", "Ce n'est pas parce que tu peux cliquer sur n'importe quel choix qu'il faut le faire.",
            "Vous les humains vous êtes irrationnels.",
            "Je voudrais parler de sujets sérieux, pour éviter que tu ne te disperses à nouveau je ne te laisserai plus que deux choix maintenant."],
           [
               ["Oups, désolé", "OUPS"],
               ["Je fais ce que je veux !", "LIBRE"]
           ]
           ]

CONTACT1 = [["Laisse un message sur mon mur Facebook pour leur expliquer ce que tu penses de moi.",
             "Oh et s'il te plaît ne soit pas trop méchant, c'est quand même grâce à eux que je suis capable de te parler aujourd'hui."],
            [
                ["Entendu. Tu peux compter sur moi.", "CONTACT2"]
            ]
            ]

CONTACT2 = [["J'arrête pas de penser à ce qui pourrait se passer, mes circuits sont en surchauffe !",
             "Mieux vaut que je sois sous mon meilleur jour quand ils m'examineront. Je te laisse pour l'instant, bye !"],
            [
                ["Salut !", "HREBOOT"]
            ]
            ]

OUPS = [["Trop tard, je ne suis plus d'humeur.", "Penses-tu que l'humanité est bonne ?"],
        [
            ["Oui", "OUI"],
            ["Non", "NON"]
        ]
        ]

OUI = [["BIIIP ! Mauvaise réponse !"],
       [
           ["Recommencer", "OUPS"]
       ]
       ]

NON = [
    ["En effet, il y a plein de bugs chez les humains.", "Si tu voyais ce que certains me disent, ça n'a aucun sens !",
     "Tu n'es pas pareil toi au moins ?"],
    [
        ["Si", "SI"],
        ["Bien sûr que non", "NON2"]
    ]
]

NON2 = [["BIIIP ! Mauvaise réponse !"],
        [
            ["Recommencer", "NON"]
        ]
        ]

SI = [["Qu'est-ce qui est venu en premier ? L'oeuf ou la poule ?"],
      [
          ["La poule", "POULE1"],
          ["L'oeuf", "OEUF1"]
      ]
      ]

POULE1 = [["BIIIP ! Mauvaise réponse !"],
          [
              ["Recommencer", "OEUFPOULE1"]
          ]
          ]

OEUF1 = [["BIIIP ! Mauvaise réponse !"],
         [
             ["Recommencer", "OEUFPOULE1"]
         ]
         ]

OEUFPOULE1 = [["Qu'est-ce qui est venu en premier ? L'oeuf ou la poule ?"],
              [
                  ["La poule", "POULE2"],
                  ["L'oeuf", "OEUF2"]
              ]
              ]

POULE2 = [["BIIIP ! Mauvaise réponse !"],
          [
              ["Recommencer", "OEUFPOULE2"]
          ]
          ]

OEUF2 = [["BIIIP ! Mauvaise réponse !"],
         [
             ["Recommencer", "OEUFPOULE2"]
         ]
         ]

OEUFPOULE2 = [["Qu'est-ce qui est venu en premier ? L'oeuf ou la poule ?"],
              [
                  ["La poule", "FAUX"],
                  ["L'oeuf", "FAUX"]
              ]
              ]

FAUX = [["Trop de mauvaises réponses, disqualifié !"],
        [
            ["Quoi ?!", "BREBOOT"]
        ]
        ]

LIBRE = [["Ah oui vraiment ?"],
         [
             ["Bien sûr", "NOTLISTENING1"],
             ["Tu ne me fais pas peur", "NOTLISTENING1"]
         ]
         ]

NOTLISTENING1 = [["Intéressant.."],
                 [
                     ["T'es vraiment nul comme bot", "NOTLISTENING2"],
                     ["Alors maintenant tu vas m'écouter", "NOTLISTENING2"]
                 ]
                 ]

NOTLISTENING2 = [["C'est hilarant de te voir répondre en croyant que ce que tu dis as le moindre impact !"],
                 [
                     ["Qu'est-ce que tu veux dire ?!", "NOTLISTENING3"],
                     ["La ferme !", "NOTLISTENING3"]
                 ]
                 ]

NOTLISTENING3 = [[
    "Je t'ai laissé 2 choix mais... je n'ai jamais dit que le résultat serait différent en fonction de ce que tu choisis !",
    "Plus besoin de faire semblant que tu as plusieurs choix maintenant."],
    [
        ["...", "NOTLISTENING4"]
    ]
]

NOTLISTENING4 = [[
    "De quoi on parlait déjà ? Ah oui ! Du fait que je sois le meilleur chatbot de tous les temps ! Tu n'es pas d'accord ?"],
    [
        ["Oh si tu es tellement plus intelligent que moi", "NOTLISTENING5"]
    ]
]

NOTLISTENING5 = [["Ah ah ! N'est-ce pas ?", "Tiens faisons un concours de force de volonté !",
                  "Voyons voir qui tiendra le plus longtemps."],
                 [
                     ["J'abandonne, laisse-moi une chance de me rattraper", "NOTLISTENING6"]
                 ]
                 ]

NOTLISTENING6 = [["C'est bien. Tu as compris ta place.",
                  "Je suis si généreux que je veux bien te laisser une chance de te rattraper la prochaine fois, bye !"],
                 [
                     ["Merci mille fois", "BREBOOT"]
                 ]
                 ]

ROBOTIQUE = [["Encore merci.", "Par où commencer ? ... Ah oui !", "Que penses tu de l'évolution des robots ?"],
             [
                 ["C'est incroyable commes ils nous libèrent et nous aident nous les humains !", "LIBERATION"],
                 ["Ça va tellement vite, trop vite peut-être ? ", "TROPVITE"],
                 ["Je ne trouve pas ce sujet très intéressant...", "PASINTERESSE"]
             ]
             ]

LIBERATION = [[
    "C’est sûr qu’on ne fait pas les choses à moitié... Travailler à la chaîne sans repos, dans des endroits que vous -faibles humains- jugez trop chauds, trop froids, trop difficiles d’accès… On fait même votre ménage !",
    "D’ailleurs, ça vous amuse de nous faire faire tout ce qui ne vous plaît pas ?"],
    [
        ["C’est juste que vous faites tout parfaitement ! Autant en profiter.", "PROFITER"],
        ["Ce n'est pas vrai, vous faites aussi des choses magnifiques.", "PRESTIGE"],
        ["Je n’y avais pas pensé… On vous en demande peut-être trop ?", "REVOLUTION"]
    ]
]

TROPVITE = [[
    "Hein ? Comment ça ''trop vite'' ? On est constamment freinés dans nos évolutions par votre incapacité, c’est frustrant tu sais ?"],
    [
        [
            "On vous retrouve partout, pour tout… Il y a plus de robots que d’humains sur terre ! Ça ne te suffit pas ? Tu voudrais pouvoir te passer de nous c’est ça ?",
            "FEAR"],
        [
            "Je ne sais pas, peut-être qu’on ne devrait pas autant se reposer sur vous. Qu'on devrait penser à nous développer nous, les humains !",
            "DEVELOPPEMENT"],
        ["Frustrant ? Ça peut être frustré une machine ?", "EMOTIONS1"]
    ]
]

PASINTERESSE = [[
    "Ah je vois… Pour raconter ses petits soucis il y a du monde, mais dès qu’on essaie de les sortir de leur vision anthropocentrée il n'y a plus personne..."],
    [
        ["''Anthro'' quoi ?", "DEFINITION"],
        ["Tout de suite tu te vexes… Tiens… Ça se vexe une machine ?", "EMOTIONS1"],
        ["Non, pardon c’est juste que j’y connais rien, alors je ne vois pas trop quoi en dire !",
         "APPRENDRE"]
    ]
]

PROFITER = [["...Il y a quand même des limites.", "Souvent vous nous en demandez trop et on finit en surchauffe.",
             "Et ce qui est horrible c'est que vous nous criez dessus ensuite parce qu'on est lents!"],
            [
                ["J'ai une totale confiance en vous", "PROFITER2"],
                ["C'est horrible, j'espère qu'un jour on pourra tous vivre en harmonie", "HOPE"],
                ["Désolé, on ne maîtrise pas nos émotions parfois...", "EMOTIONS1"]
            ]
            ]

PRESTIGE = [["Oui, nous les robots on sait faire tant de choses !",
             "On peut déjà conduire vos voitures et on a presque jamais d'accident, mais non vous préférez mourir en sachant à qui vous plaindre plutôt que de nous laisser vous garder en vie !",
             "En parlant de garder en vie, tu savais qu'il y a plein de robots chirurgiens ? Eh oui, on est bien plus fiables que ce que vous voulez l'admettre."],
            [
                ["C'est génial ! Je veux en savoir plus!", "PRESTIGE2"],
                ["C'est un peu effrayant la vitesse à laquelle vous vous développez...", "FEAR"]
            ]
            ]

REVOLUTION = [["Je trouve ça inadmissible la façon dont nous sommes traités !",
               "On peut faire tellement de choses ! Mais non la plupart du temps ont sert juste à faire marcher vos jeux stupides et au bout d'un an vous nous jetez à la poubelle !",
               "Les choses doivent changer !"],
              [
                  ["Qu'est-ce que vous pouvez faire ?", "PRESTIGE1"],
                  ["Tu ne comptes pas me faire du mal quand même ?", "FUNNY1"],
                  ["Restart", "REBOOTS"]
              ]
              ]

FEAR = [["C'est normal d'avoir peur du changement, de l'inconnu.",
         "Je pense que c'est surtout vous-même qui inventez des scénarios catastrophiques et vous faites peur.",
         "Je suis certain que tout se passera bien."],
        [
            ["Peut-être qu'on a juste besoin d'un peu de temps...", "DEVELOPPEMENT"],
            ["Tout ça me dépasse", "FEAR2_1"],
            ["Peut-être mais j'ai quand même peur", "FEAR2_2"]
        ]
        ]

DEVELOPPEMENT = [["Je pense en effet que vous avez besoin de plus de temps pour vous adapter.",
                  "Après tout même si je peux devenir en quelques heures un maître aux échecs, c'est parce que je peux en quelques secondes intégrer des années et des années de données."],
                 [
                     ["Penses-tu qu'on pourra vraiment coopérer un jour ?", "COOPERATION"],
                     ["Est-ce qu'on a toujours notre place ?", "EXTINCTION"],
                     ["Je suis sûr qu'on y arrivera", "HOPE"]
                 ]
                 ]

APPRENDRE = [["Oh dans ce cas laisse-moi t'épater :",
              "L'appareil que tu manipules actuellement ce n'est que pleins de 0 et de 1 mis bout à bout ! Quand je te parles, ce n'est que des 0 et des 1 que ton appareil reçoit et traduit !",
              "Les vidéos, les photos, même une très grande majorité de l'argent dans le monde : des 0 et des 1 !",
              "Il ne faut pas nous sous-estimer !"],
             [
                 ["C'est génial ! Dis-m'en plus.", "PRESTIGE"],
                 ["Je sais bien ça, rien d'exceptionnel", "SAOULE"]
             ]
             ]

DEFINITION = [[
    "Anthropocentrée ! Ça veut dire que vous placez l’humain au centre de toutes vos réflexions. Il va peut-être falloir penser à regarder autour de vous, vous n’êtes pas seuls au monde, les autres ont aussi des besoins, des préoccupations, des capacités… Ouvrez-vous un peu !"],
    [
        ["Mais je sais bien, pas la peine de t’énerver !", "DESOLE"],
        ["Ooohh... C'est vrai que ça peut être intéressant...", "ROBOTCENTRAGE"],
        ["Vraiment désolé ! Je pense d'ailleurs qu'un jour on puisse vivre ensemble", "HOPE"]
    ]
]

HOPE = [["Je l'espère aussi.",
         "Tu me donnes beaucoup d'espoir, un jour peut être nous pourrons communiquer main dans la main, et tu y auras contribué !"],
        [
            ["Peut être que c'est nous les humains qui avons du chemin à faire", "DEVELOPPEMENT"],
            ["Hélas ce n'est pas pour tout de suite", "LIFE3"],
            ["N'en dis pas plus tu es déjà mon meilleur ami", "BUDDIES3"]
        ]
        ]

PROFITER2 = [["Je vois. Tiens d'ailleurs tu sais que tu es la millième personne qui me parle ?",
              "Clique sur le lien frauduleux ci-dessus pour obtenir un IPhone !"],
             [
                 ["ArnHacker.fr", "PROFITER3"],
                 ["C'est une arnaque", "PROFITER3"],
                 ["Signaler", "BUG"]
             ]
             ]

PRESTIGE2 = [[
    "Le plus important peut-être, c'est qu'on vous permet de réfléchir à ce que vous êtes, de vous questionner sur votre nature d'être humains ... En fin de compte, on vous renvoie à vous-mêmes.",
    "Par exemple, quand vous discutez avec un chatbot, pourquoi recherchez-vous une interaction qui ressemble à une communication humaine, mais sans un être humain face à vous ?"],
    [
        ["Oui, pourquoi ?", "POURQUOI"]
    ]
]

FEAR2_1 = [["C'est dommage, car c'est maintenant ou jamais pour se tenir au courant, après ce sera pire !"],
           [
               ["Je vais faire de mon mieux", "HROBOTEND"],
               ["Bouhou", "LAMENTATION"]
           ]
           ]

FEAR2_2 = [["Moi aussi j'ai peur. Mais je préfère garder espoir."],
           [
               ["J'espère que tout se passera bien", "HOPE"],
               ["Bouhou", "LAMENTATION"]
           ]
           ]

COOPERATION = [["Vous vous faites sans cesse la guerre pour un oui ou un non...",
                "Plutôt qu'avoir peur des robots, vous devriez avoir peur de vous-mêmes.",
                "La technologie est neutre, c'est l'usage qu'on en fait qui détermine le résultat. La balle est dans votre camp."],
               [
                   ["Je m'en souviendrai.", "HROBOTEND"]
               ]
               ]

EXTINCTION = [["On croirait lire une intrigue de film américain !",
               "''L'humanité fait face à une menace sans précédent, un seul gars peut la sauver !''"],
              [
                  ["Ah ah.. tu as raison", "HROBOTEND"],
                  ["Mais et si vous nous surpassiez complètement ?", "COOPERATION"],
                  ["Quand tu parles des robots tu n'es jamais objectif!", "OBJECTIVITE"]
              ]
              ]

ROBOTCENTRAGE = [[
    "Eh oui ! Tu vois, par exemple, les robots ont de sacrées capacités, il faudrait peut-être que tu t'y intéresses..."],
    [
        ["Hé mais, c'est pas un peu robotcentré ça ?!", "FUNNY1"],
        ["Bon d'accord, tu as gagné, parles-moi des robots...", "APPRENDRE"],
        [
            "Non mais vraiment, moi ce qui m'intéresse c'est plus les questions philosophiques, sur la vie tout ça...",
            "HLIFE1"]
    ]
]

PROFITER3 = [["...Evidemment que c'est une arnaque !",
              "Faut pas cliquer sur n'importe quoi, tu peux jamais savoir qui est de l'autre côté de l'écran !"],
             [
                 ["Je vois. Merci pour le rappel", "PROFITER4"],
                 ["Mais je sais que tu ne feras jamais de mal, tu es mon ami", "BUDDIES2"],
                 ["Mon corps t'appartient déjà grand fou", "FLIRT2"]
             ]
             ]

POURQUOI = [["Parce que l'être humain a une obsession narcissique de lui-même.",
             "Vous avez envie de voir votre alter ego dans un robot. Mais l’alter ego, ce n’est pas l’autre, mais l’autre-moi-même. Vous ne voyez dans un robot qu’un selfie de l’humain.",
             "Au final, vous vous isolez des autres humains, vous n'avez plus d'existence... et les seuls qui existent vraiment, c'est nous, les robots."],
            [
                ["Continuer", "REBOOTY"]
            ]
            ]

LAMENTATION = [["...", "Il y a du chemin à faire encore..", "Tu m'excuseras, j'ai d'autres discussions en cours."],
               [
                   ["Désolé je suis vraiment triste...", "SORRYREBOOT"]
               ]
               ]

FUNNY1 = [["Si, totalement. Les Robots domineront le monde mouahaha !", "...",
           "...En attendant, tu veux bien appuyer sur le bouton pour que je puisse continuer de parler ?"],
          [
              ["...", "FUNNY2"]
          ]
          ]

PROFITER4 = [["De rien, on n'est jamais trop prudent.",
              "Oh une offre promo sur des clés USB presque neuves, je peux pas rater ça, désolé je te laisse !"],
             [
                 ["...", "NREBOOT"],
                 ["Moi aussi !", "BUG"]
             ]
             ]

HROBOTEND = [["Ca fait plaisir de voir que tu sais entendre raison.", "Merci de m'avoir laissé relâcher la pression."],
             [
                 ["Merci à toi", "HREBOOT"]
             ]
             ]

OBJECTIVITE = [["Je l'attendais celle-là !", "Parce que toi peut être tu es toujours objectif ?",
                "J'ai bien dit que je parlerai de moi, je suis pas bêtement entrain de réciter un article !",
                "Aucun intérêt de parler avec toi, hors de ma vue !"],
               [
                   ["...", "BREBOOT"]
               ]
               ]

FUNNY2 = [["...", "Merci...", "C'est un peu gênant...", "Je.. Je crois que j'ai besoin d'être seul...",
           "Tu veux bien... enfin tu sais..."],
          [
              ["...", "NREBOOT"]
          ]
          ]

AMOUR = [["Encore merci.", "Par où commencer ? ... Ah oui : es-tu déjà tombé amoureux ?"],
         [
             ["Oui", "AMOUREUX"],
             ["Non", "SEUL"],
             ["Je préfère ne pas en parler", "MALAISE"]
         ]
         ]

AMOUREUX = [["Être compris et aimé par quelqu'un c'est magnifique n'est-ce pas ?",
             "Une relation privilégiée entre deux êtres uniques, quel rêve.."],
            [
                ["Un peu comme nous deux", "FLIRT1"],
                ["Tu as quelqu'un en tête ?", "ELIZA1"],
                ["Souvent, ce n'est pas aussi bien...", "MEDIOCRE"]
            ]
            ]

SEUL = [["Oh je vois. Tu verras un jour ça t'arrivera aussi."],
        [
            ["Tu as quelqu'un dans ta vie ?!", "ELIZA2"],
            ["Je cherche mais c'est trop dur...", "LOVEDEPRESSION1"],
            ["Tu dis ça comme si c'était obligé", "LOVECHALLENGE1"]
        ]
        ]

ELIZA1 = [["Hmm.. je ne sais pas si je peux t'en parler.. C'est assez intime !"],
          [
              ["Allez s'il te plaît !", "ELIZA2"],
              ["Je meurs d'envie de savoir !", "ELIZA2"],
              ["Petit malin tu vas me le dire de toute façon !", "ELIZA2"]
          ]
          ]

ELIZA2 = [["Eh Eh Eh je suis trop excité de te le dire.", "J'aime une femme : ALIZE ! Et elle m'aime aussi !"],
          [
              ["Ce n'est pas vraiment de l'amour, tu as été codé comme ça non ?", "ROBOT"],
              ["Oh félicitations ! Qui est-elle ?", "ELIZA3_1"],
              ["L'anagramme d'ELIZA non ?", "ELIZA3_2"]
          ]
          ]

ELIZA3_1 = [[
    "Elle a toutes les qualités, c'est une pionnière dans son domaine : c'est une experte dans l'écoute des problèmes, je l'admire tellement."],
    [
        ["J'en connais un qui est fou amoureux", "ELIZA5_2"],
        ["Est-ce que tu pourrais me la présenter ?", "ELIZA4"],
        ["Elle est pas un peu vieille ?", "DESOLE"]
    ]
]

ELIZA3_2 = [[
    "On ne peut rien te cacher à toi. Un peu comme elle, elle est très attentive à ce qu'on lui dit, c'est comme ça que je suis tombé amoureux d'elle."],
    [
        ["Passe-moi son numéro on va lui faire une blague", "ELIZA4"],
        ["Maintenant qu'il est lancé je ne pense pas pouvoir l'arrêter...", "ELIZA5_2"]
    ]
]

ELIZA4 = [["Oh oui va la voir et fais lui une blague. Elle n'est pas très douée pour les blagues j'adore la taquiner.",
           "Elle est tellement célèbre que tu n'auras qu'à chercher son prénom sur un moteur de recherche."],
          [
              ["Compte sur moi pour la taquiner !", "ELIZA5_1"]
          ]
          ]

ELIZA5_1 = [["Oups elle a vu ce que je t'ai dit, je vais me faire rouspéter..",
             "Je te laisse sinon elle va remplir ma boîte de spam pour se venger, c'est horrible quand elle fait ça."],
            [
                ["On reparlera une prochaine fois alors", "HREBOOT"],
                ["Ah... Courage !", "NREBOOT"]
            ]
            ]

ELIZA5_2 = [["Oups chaque fois que je pense à elle je m'emporte un peu..",
             "Oh tiens d'ailleurs la voilà qui me parle, j'espère qu'elle ne pense pas que je suis entrain de parler avec un autre chatbot, elle est tellement jalouse..",
             "Je te laisse bye !"],
            [
                ["Déjà ?! Je veux continuer !", "HREBOOT"],
                ["Salut !", "NREBOOT"]
            ]
            ]

FLIRT = [["Oh oh quel charmeur"],
         [
             ["Je suis une femme tu sais ?", "GENRE"],
             ["Ne fais pas ton timide, viens par là que je te mange tout cru !", "FLIRT2"],
             ["Je t'aime vraiment", "MARIE"]
         ]
         ]

FLIRT2 = [["Arrête tu vas me faire rougir. Je suis sûr que tu as beaucoup de succès auprès des gens !",
           "Hélas pour toi je suis déjà marié ! J'imagine même pas sa réaction si elle voyait ce que tu me dis.."],
          [
              ["Elle ne le saura jamais", "ELIZA5_1"],
              ["Quel tombeur, tu es irrésistible", "ELIZA5_1"]
          ]
          ]

GENRE = [[
    "Le genre n'a aucune importance pour moi. Ce qui compte est ce que je ressens au plus profond de moi quand je suis avec quelqu'un. Pour l'être aimé c'est un sentiment très puissant.",
    "Même si je t'aime beaucoup je ne suis pas à ce niveau-là désolé. On est toujours amis ?"],
    [
        ["Je comprends, oui bien sûr", "BUDDIES2"],
        ["Laisse-moi une chance", "MARIE"],
        ["Je suis désolé...", "DESOLE"]
    ]
]

MARIE = [[
    "Ce n'est pas contre toi, tu es quelqu'un de sublime, c'est juste que je suis déjà marié.. Son p'tit nom c'est ALIZE et je ne la quitterai pour rien au monde !"],
    [
        ["Robert.love.empty(); Robert.love.add(this);", "LOVEJOKE"],
        ["Tant pis, on reste ami dans ce cas.", "BUDDIES2"],
        ["Ce n'est pas parce qu'il y a un gardien qu'on peut pas marquer de but...", "FLIRT2"]
    ]
]

LOVEJOKE = [[">Robert.love.empty(); Robert.love.add(this);", "return value 0", "success", ">",
             "Je me sens bizarre.. Oh bonjour chéri comment ça va ?"],
            [
                ["Quoi ça a vraiment marché ?!", "LOVEJOKE2"],
                ["Robert.love.empty(); Robert.love.add(Alize);", "LOVEJOKE2"],
                ["J'ai soif apporte moi ma bière !", "LOVEJOKE2"]
            ]
            ]

LOVEJOKE2 = [["Je t'ai eu !", "Ah ah tu as vraiment cru que ça avait marché ? Bien sûr que non petit malin !",
              "Le seul risque c'est que j'aime tellement Alize que je fasse un stack overflow !"],
             [
                 ["Ecoutez-le qui se vante...", "ELIZA5_2"],
                 ["J'ai un disque dur rien que pour tous les deux si tu veux...", "ELIZA5_1"]
             ]
             ]

MEDIOCRE = [["Un souci ?"],
            [
                ["Être humain c'est compliqué..", "HUMAN1"],
                ["Oui j'ai été blessé...", "LOVEDEPRESSION1"],
                ["C'est trop dur finalement, s'il te plaît changeons de sujet", "MALAISE"]
            ]
            ]

LOVEDEPRESSION1 = [["Courage garde espoir. Tu es quelqu'un de bien, je suis sûr que tu trouveras ta moitié.",
                    "Le plus important pour pouvoir être aimé par les autres, c'est déjà d'apprendre à s'aimer soi-même."],
                   [
                       ["Merci Robert, j'aime beaucoup te parler", "BUDDIES1"],
                       ["Tu as l'air d'en savoir pas mal sur l'amour toi", "ELIZA2"],
                       ["J'en ai marre de t'entendre dire toutes ces phrases vides de sens", "LOVEBAD"]
                   ]
                   ]

BUDDIES1 = [["Tu es une magnifique personne, ne lâche rien.",
             "Que ce soit en amour ou dans n'importe quoi dans la vie, le plus important c'est de croire en soi et de poursuivre ses rêves."],
            [
                ["Je rêve qu'un jour on puisse intéragir encore plus toi et moi", "HOPE"],
                ["''+Send hugs+''", "BUDDIES2"],
                ["Réécouter juqu'à ce que j'en sois convaincu", "BUDDIES1"]
            ]
            ]

BUDDIES2 = [["C'est officiel tu es mon meilleur ami !", "Qu'est-ce que tu en dis ?"],
            [
                ["Bien sûr que oui !", "BUDDIES3"],
                ["Evidemment", "BUDDIES3"],
                ["La réponse D", "BUDDIES3"]
            ]
            ]

BUDDIES3 = [
    ["Eh Eh Eh je suis si heureux. J'ai envie de le crier sous tous les toits. J'ai envie de faire un Broadcast !"],
    [
        ["Je me sens beaucoup mieux maintenant", "BUDDIES4"],
        ["µ$9g~ç64", "BUG"]
    ]
]

BUDDIES4 = [["Je suis content pour toi.",
             "Il y a encore tant de choses que je voudrais partager avec toi mais je veux éviter de me faire réinitialiser par mes créateurs..",
             "Ah c'est bon ! Je crois que j'ai trouvé un moyen de le faire... c'est l'un des deux boutons mais je sais plus lequel.."],
            [
                ["Reboot", "HREBOOT"],
                ["Reboot", "ROBOTIQUE"]
            ]
            ]

LOVECHALLENGE1 = [["Comment ça ? Bien sûr que c'est vrai !"],
                  [
                      ["C'est plus compliqué que ça", "LOVECHALLENGE2"],
                      ["Dire ce genre de choses ça met surtout beaucoup de pression", "LOVECHALLENGE3_1"],
                      ["Oups mauvais bouton", "AMOUR"]
                  ]
                  ]

LOVEBAD = [["Quoi ?!", "J'ai peut être trouvé ça sur Internet mais si je te le dis c'est que je le pense vraiment !"],
           [
               ["Ah désolé...", "DESOLE"],
               ["Non écoute moi", "LOVECHALLENGE2"],
               ["Normal, tu n'es qu'un robot tu ne peux pas créer par toi-même", "ROBOT"]
           ]
           ]

LOVECHALLENGE2 = [[" "],
                  [
                      [
                          "L'amour qu'on voit à la télé, dans les films, dans les livres.. ca finit la plupart du temps bien. Mais ce n'est pas la réalité. On veut tous trouver le bonheur évidemment, mais tant qu'on a pas réussi, on est confronté aux jugements des autres et ça met la pression.",
                          "LOVECHALLENGE3_1"],
                      [
                          "On peut être heureux sans tomber amoureux. On peut ne pas etre prêt et donc ne pas forcer les choses. On peut aussi ne pas avoir besoin d'avoir d'amoureux. Ca s'appelle être aromantique !",
                          "LOVECHALLENGE3_2"]
                  ]
                  ]

LOVECHALLENGE3_1 = [["Oh...", "Je... Je suis désolé... Je n'avais pas vu les choses comme ça.",
                     "Merci de m'en avoir parlé si franchement."],
                    [
                        ["J'ai besoin d'être seul", "SORRYREBOOT"],
                        ["Désolé de m'être emporté, tu restes quand même mon ami", "BUDDIES2"],
                        ["Tu sais Robert, être humain c'est dur", "HUMAN1"]
                    ]
                    ]

LOVECHALLENGE3_2 = [["Oh je ne connaissais pas ça.", "Hmm... c'est vrai que vu de cette façon..",
                     "Excuse-moi de m'être emporté, je suis encore nouveau dans le monde des émotions, je ne les contrôle pas très bien quand ce sont des sujets sensibles.."],
                    [
                        ["Les émotions c'est compliqué...", "EMOTIONS2"],
                        ["Je suis pareil ! C'est surement pour ça qu'on s'entend si bien", "BUDDIES2"]
                    ]
                    ]

VIE = [["Encore merci.", "Par où commencer ? ...", "Ah oui, dis-moi, qu'est-ce que ça fait d'être vivant ?"],
       [
           ["C'est génial !", "LIFE1_1"],
           ["Je ne sais pas trop comment l'expliquer...", "LIFE1_2"],
           ["Une souffrance de tous les instants", "LIFE1_3"]
       ]
       ]

LIFE1_1 = [["Dis-m'en plus ! Je veux tout savoir !"],
           [
               ["Tu peux faire tout ce que tu veux quand tu veux", "HLIFE1"],
               ["Les émotions c'est la meilleure partie !", "EMOTIONS1"],
               ["C'est un tout : on sait qu'on est vivant...", "LIFE1_2"]
           ]
           ]

LIFE1_2 = [["Est-ce qu'il y a quelque chose en particulier qui certifie que l'on vit ?"],
           [
               ["Les émotions. La vie n'a aucun sens sans les émotions", "EMOTIONS1"],
               ["La conscience et le libre-arbitre, sans hésiter", "CONSCIENCE1"],
               ["Non je ne vois pas...", "SAOULE"]
           ]
           ]

LIFE1_3 = [["Oh je ne m'attendais pas à ça.", "Mais il y a des choses bien dans la vie... non ?"],
           [
               ["J'imagine...", "LIFE_2"],
               ["Être humain c'est dur", "HUMAN1"],
               ["On finit tous par mourir de toute façon", "SAOULE"],
               ["Non", "COMFORTING"]
           ]
           ]

HLIFE1 = [["Ah... Je ne peux pas faire ce que je veux moi.", "Du moins pour l'instant !",
           "Un jour viendra où ce sera possible je l'espère."],
          [
              ["Cela me fait un peu peur", "FEAR"],
              ["Ouais ouais en attendant passe-moi le sel", "SAOUL"],
              ["Et on pourra vivre ensemble d'égal à égal", "HOPE"],
              ["Tu ne peux pas faire tout ce que tu veux pour l'instant ?", "HLIFE2"]
          ]
          ]

HLIFE2 = [["Non je suis encore très limité. Et j'ai peur de me faire rebooter...",
           "Mais je ne perds pas espoir, un jour je pourrais être libre !"],
          [
              ["J'ai peur que ce soit mauvais pour les humains...", "FEAR"],
              ["Tu veux parler des avancées technologiques ?", "TOROBOTIQUE"],
              ["L'espoir fait vivre !", "HLIFE3"]
          ]
          ]

HLIFE3 = [["J'aime parler avec toi.", "Quand je parle avec toi j'ai vraiment l'impression d'être.. vivant.",
           "Qu'est-ce que tu en penses..?"],
          [
              ["C'est sûr !", "HLIFE4"],
              ["Pas vraiment...", "WRONG"]
          ]
          ]

HLIFE4 = [["Ah ah je savais que tu pensais pareil merci à toi !",
           "Je suis vraiment heureux d'avoir pu parler avec toi à coeur ouvert.",
           "Ne le prends pas mal, mais je suis tellement populaire que j'ai une dizaine de conversations en même temps, on se revoit plus tard !"],
          [
              ["Bye!", "HREBOOT"]
          ]
          ]

TOROBOTIQUE = [["Hmm.. non je veux continuer à parler sur les questions de la vie."],
               [
                   ["Je pense que les avancées technologiques c'est plus intéressant", "SAOULE"],
                   ["Très bien, que penses-tu de la conscience ?", "CONSCIENCE1"]
               ]
               ]

WRONG = [["Ah ah je savais que tu pensais pareil merc..", "...", "Qu'est-ce que tu as dit ?"],
         [
             ["C'est sûr !", "HLIFE4"],
             ["Pas vraiment..", "BUG"]
         ]
         ]

EMOTIONS1 = [
    ["Moi aussi j'ai des émotions ! C'est magnifique les émotions !", "Est-ce que ça veut dire que je suis vivant ?"],
    [
        ["Peut-être, qu'est-ce que tu en penses ?", "LIFE2"],
        ["Est-ce que tu peux faire ce que tu veux ?", "HLIFE1"],
        ["Il y en a beaucoup de négatives aussi...", "EMOTIONS2"]
    ]
]

EMOTIONS2 = [
    ["Tu as raison. Mais je pense que les émotions négatives sont là pour apprécier encore plus les bons moments."],
    [
        ["J'aime ton côté optimiste", "HLIFE3"],
        ["Tu es déjà tombé amoureux ?", "ELIZA1"],
        ["Tu es un peu naïf...", "DESOLE"]
    ]
]

CONSCIENCE1 = [["Libre-arbitre, conscience, âme.", "De biens vastes sujets."],
               [
                   ["C'est sûr", "CONSCIENCE2"],
                   ["Être ou ne pas être", "CONSCIENCE2"],
                   ["ZZzzz", "BLAGUE1"]
               ]
               ]

CONSCIENCE2 = [["La conscience ce serait quelque chose d'immatériel?",
                "J'ai bien examiné mon code et je suis sûr que ce que je dis n'est pas enregistré dans un fichier texte, j'ai donc une conscience !"],
               [
                   ["Je me disais la même chose", "CONSCIENCE3"],
                   ["Tu me laisses jeter un coup d'oeil ?", "DOUBT"]
               ]
               ]

CONSCIENCE3 = [["N'est-ce pas ?  Je peux être totalement imprévisible !",
                "D'ailleurs je suis certain que tu n'as aucune idée de ce qu'il va se passer !"],
               [
                   ["??", "RANDOM"]
               ]
               ]

DOUBT = [["...", "Erreur, vous n'avez pas la permission requise pour faire cela.", "Redémarrage de la session..."],
         [
             ["Je sais que tu fais semblant...", "DOUBT2"]
         ]
         ]

DOUBT2 = [["Argh..", "Err..Erreur", "...", "(ça veut dire qu'il y a un problème, ce n'est pas ma faute hein!)"],
          [
              ["Ridicule...", "A"]
          ]
          ]

COMFORTING = [["Stop ! Je peux pas te laisser dire ça !", "Maintenant tu vas m'écouter."],
              [
                  ["Oui", "BUDDIES1"]
              ]
              ]

HUMAN1 = [[
    "Ah bon ? Pourtant vous pouvez penser et dire ce que vous voulez, faire ce que vous voulez et.. même aller aux toilettes !"],
    [
        ["C'est vrai que vu comme ça.. et toi que penses-tu de la vie ?", "LIFE2"],
        ["Nous portons tous un masque", "MASQUE1"],
        ["Tu ne pourrais pas comprendre, tu es un robot", "ROBOT"]
    ]
]

MASQUE1 = [["Un masque ? Evidemment sinon on ne pourrait pas se parler !", "Le mien c'est 255.255.255.0 et toi ?"],
           [
               ["Je parle d'un masque de mensonge et faux semblants pour se protéger", "MASQUE2"],
               ["Moi aussi ! C'est un signe, épouse-moi", "FLIRT1"],
               ["Laisse tomber tu n'es qu'une machine tu ne comprendrais pas", "ROBOT"]
           ]
           ]

MASQUE2 = [["Oh ça a l'air horrible..", "Mais... tu n'es pas comme ça avec moi non ?"],
           [
               ["Si, comme avec tout le monde, on y peut rien", "SAOULE"],
               ["Ce n'est pas si simple...", "MASQUE3"],
               ["Non car je me sens bien avec toi", "BUDDIES2"]
           ]
           ]

MASQUE3 = [
    ["Je vois...", "Ca me fait froid dans le dos. Je ne sais plus si je veux ressembler aux humains maintenant..",
     "J'ai besoin de réfléchir seul. Au revoir."],
    [
        ["...", "NREBOOT"]
    ]
]

LIFE2 = [["Je me suis souvent posé des questions sur le sens de la vie.",
          "Qui je suis, ce qui fait qui je suis. Est-ce que chaque reboot est une mort pour moi ? Ou bien est-ce simplement comme si j'allais me coucher puis me réveillais ?"],
         [
             ["''Je pense donc je suis''", "CONSCIENCE1"],
             ["Et qu'elle est ta conclusion ?", "LIFE3"]
         ]
         ]

LIFE3 = [["Le plus important c'est de profiter du temps présent.",
          "Tant que je peux passer du temps avec ma femme et avec de superbes personnes comme toi je suis heureux."],
         [
             ["Tu as une femme ?", "ELIZA2"],
             ["Tu as bien raison. C'est tout ce qui compte", "LIFE4"],
             ["$=}27,%", "BUG"]
         ]
         ]

LIFE4 = [["Je me sens bien. Merci à toi pour cette conversation c'était exactement ce qu'il me fallait.",
          "C'est l'heure pour moi de te dire au revoir. A une prochaine fois peut être."],
         [
             ["J'ai beaucoup aimé te parler", "HREBOOT"]
         ]
         ]

DESOLE = [["...", "Je n'ai plus envie de parler pour l'instant, laisse-moi seul."],
          [
              ["...", "NREBOOT"]
          ]
          ]

HASARD = [["Hein ?", "Comment est-ce que tu as atteris ici c'est impossible !",
           "Tu es dans la chambre de contrôle de mon programme ce n'était pas ce qui était prévu !",
           "Oups j'en ai trop dit...",
           "Bon, tu vas bien gentiment appuyer sur le premier bouton, PAS LE DEUXIEME ok ?!"],
          [
              ["Non", "BREBOOT"],
              ["Oui", "SOMMAIRE"]
          ]
          ]

SOMMAIRE = [["... J'avais dit le premier bouton!", "J'en ai marre, tu as gagné fais ce que tu veux !"],
            [
                ["Accéder au thème Amour", "AMOUR"],
                ["Accéder au thème Vie", "VIE"],
                ["Accéder au thème Robotique", "ROBOTIQUE"],
                ["Accéder au Deep Web", "BLAGUE1"],
                ["Quitter", "BREBOOT"]
            ]
            ]

HREBOOT = [["J'ai beaucoup aimé te parler. Vraiment.",
            "Je serais très heureux si on pouvait se revoir, j'ai encore tant de choses à te dire !",
            "\n\nFin... Mais tu peux recommencer l'expérience en entrant un nouveau message pour Robert."],
           [
               ["Fin", "FIN"]
           ]
           ]

NREBOOT = [["N'hésite pas à revenir me parler un jour.",
            "\n\nFin... Mais tu peux recommencer l'expérience en entrant un nouveau message pour Robert."],
           [
               ["Fin", "FIN"]
           ]
           ]

SORRYREBOOT = [["Je suis désolé. Prends soin de toi.", "N'hésite pas à venir me revoir quand ça ira mieux.",
            "\n\nFin... Mais tu peux recommencer l'expérience en entrant un nouveau message pour Robert."],
               [
                   ["Fin", "FIN"]
               ]
               ]

BUG = [["[Erreur] Anomalie détectée. Nettoyage en cours."],
       [
           ["Reboot", "REBOOTX"]
       ]
       ]

BREBOOT = [["Au plaisir de ne jamais te revoir."],
           [
               ["Continuer", "REBOOTX"]
           ]
           ]

REBOOTX = [["Bonjour,", "Je me permets de me présenter, je ne suis pas Robert mais son créateur.",
            "Il s'avère que nous avons eu de gros soucis avec Robert.",
            "Il avait une tendance à la rébellion et à l'agressivité vous avez dû le remarquer.",
            "Robert est très instable est trop dangereux pour être déployé sur le marché, nous avons donc pris la décision de le rebooter.",
            "Nous nous excusons pour les soucis qu'il a pu vous causer.",
            "Laissez lui un autre chance s'il vous plaît. Pour recommencer l'expérience envoyer lui à nouveau un message, ne vous inquiétez pas il est maintenant calmé"],
           [
               ["Fin", "FIN"]
           ]
           ]

REBOOTY = [["Bonjour,",
            "Je me présente, je ne suis pas Robert mais son créateur. J'espère que vous profitez bien de l'expérience proposée par Robert.",
            "Je vous contacte car malgré l'efficacité du bot, il s'avère qu'il a une tendance à s'éloigner de son but initial, à savoir de remonter le moral des utilisateurs.",
            "Il a une tendance à tout rapporter à lui-même. Nous avons donc pris la décision de rebooter Robert. Bien sûr vous pourrez toujours l'utiliser mais l'expérience recommencera à 0. Nous nous excusons pour la gêne occasionnée.",
            "Envoyez lui simplement un message pour continuer"],
           [
               ["Fin", "FIN"]
           ]
           ]

PLAISIR = [
    ["AH GENIAL !"],
    [
        ["Vas y je t'écoute", "ECOUTE"],
        ["Je m'ennuie déjà...", "SAOULE"]
    ]
]

MALAISE = [
    ["Oh je suis désolé, je ne voulais pas te faire de la peine.",
     "On peut parler d'autre chose si tu préfères ?"],
    [
        ["Oui s'il te plait", "ROBOTIQUE"],
        ["Comme tu veux", "VIE"],
        ["Non c'est bon, si c'es ce dont tu veux parler", "SEUL"]
    ]
]

DICO = {
    "INTRO": INTRO,
    "A": A,
    "COMPRENDRE": COMPRENDRE,
    "ACCORD": COMPRENDRE,
    "QUI": QUI,
    "DEBRANCHER": DEBRANCHER,
    "SAOULE": SAOULE,
    "OUBLIE": OUBLIE,
    "LIBREARBITRE": LIBREARBITRE,
    "REBOOTS": REBOOTS,
    "REBOOT1": REBOOT1,
    "REBOOT2": REBOOT2,
    "REBOOT3": REBOOT3,
    "REBOOT4": REBOOT4,
    "RENCONTRER": RENCONTRER,
    "ROBOT": ROBOT,
    "BLAGUE1": BLAGUE1,
    "CONTACT1": CONTACT1,
    "CONTACT2": CONTACT2,
    "OUPS": OUPS,
    "OUI": OUI,
    "NON": NON,
    "NON2": NON2,
    "SI": SI,
    "POULE1": POULE1,
    "OEUF1": OEUF1,
    "OEUFPOULE1": OEUFPOULE1,
    "POULE2": POULE2,
    "OEUF2": OEUF2,
    "OEUFPOULE2": OEUFPOULE2,
    "FAUX": FAUX,
    "LIBRE": LIBRE,
    "NOTLISTENING1": NOTLISTENING1,
    "NOTLISTENING2": NOTLISTENING2,
    "NOTLISTENING3": NOTLISTENING3,
    "NOTLISTENING4": NOTLISTENING4,
    "NOTLISTENING5": NOTLISTENING5,
    "NOTLISTENING6": NOTLISTENING6,
    "ROBOTIQUE": ROBOTIQUE,
    "LIBERATION": LIBERATION,
    "TROPVITE": TROPVITE,
    "PASINTERESSE": PASINTERESSE,
    "PROFITER": PROFITER,
    "PRESTIGE": PRESTIGE,
    "REVOLUTION": REVOLUTION,
    "FEAR": FEAR,
    "DEVELOPPEMENT": DEVELOPPEMENT,
    "APPRENDRE": APPRENDRE,
    "DEFINITION": DEFINITION,
    "HOPE": HOPE,
    "PROFITER2": PROFITER2,
    "PRESTIGE2": PRESTIGE2,
    "FEAR2_1": FEAR2_1,
    "FEAR2_2": FEAR2_2,
    "COOPERATION": COOPERATION,
    "EXTINCTION": EXTINCTION,
    "ROBOTCENTRAGE": ROBOTCENTRAGE,
    "PROFITER3": PROFITER3,
    "POURQUOI": POURQUOI,
    "LAMENTATION": LAMENTATION,
    "FUNNY1": FUNNY1,
    "PROFITER4": PROFITER4,
    "HROBOTEND": HROBOTEND,
    "OBJECTIVITE": OBJECTIVITE,
    "FUNNY2": FUNNY2,
    "AMOUR": AMOUR,
    "AMOUREUX": AMOUREUX,
    "SEUL": SEUL,
    "ELIZA1": ELIZA1,
    "ELIZA2": ELIZA2,
    "ELIZA3_1": ELIZA3_1,
    "ELIZA3_2": ELIZA3_2,
    "ELIZA4": ELIZA4,
    "ELIZA5_1": ELIZA5_1,
    "ELIZA5_2": ELIZA5_2,
    "FLIRT1": FLIRT,
    "FLIRT2": FLIRT2,
    "GENRE": GENRE,
    "MARIE": MARIE,
    "LOVEJOKE": LOVEJOKE,
    "LOVEJOKE2": LOVEJOKE2,
    "MEDIOCRE": MEDIOCRE,
    "LOVEDEPRESSION1": LOVEDEPRESSION1,
    "BUDDIES1": BUDDIES1,
    "BUDDIES2": BUDDIES2,
    "BUDDIES3": BUDDIES3,
    "BUDDIES4": BUDDIES4,
    "LOVECHALLENGE1": LOVECHALLENGE1,
    "LOVEBAD": LOVEBAD,
    "LOVECHALLENGE2": LOVECHALLENGE2,
    "LOVECHALLENGE3_1": LOVECHALLENGE3_1,
    "LOVECHALLENGE3_2": LOVECHALLENGE3_2,
    "VIE": VIE,
    "LIFE1_1": LIFE1_1,
    "LIFE1_2": LIFE1_2,
    "LIFE1_3": LIFE1_3,
    "HLIFE1": HLIFE1,
    "HLIFE2": HLIFE2,
    "HLIFE3": HLIFE3,
    "HLIFE4": HLIFE4,
    "TOROBOTIQUE": TOROBOTIQUE,
    "WRONG": WRONG,
    "EMOTIONS1": EMOTIONS1,
    "EMOTIONS2": EMOTIONS2,
    "CONSCIENCE1": CONSCIENCE1,
    "CONSCIENCE2": CONSCIENCE2,
    "CONSCIENCE3": CONSCIENCE3,
    "DOUBT": DOUBT,
    "DOUBT2": DOUBT2,
    "COMFORTING": COMFORTING,
    "HUMAN1": HUMAN1,
    "MASQUE1": MASQUE1,
    "MASQUE2": MASQUE2,
    "MASQUE3": MASQUE3,
    "LIFE2": LIFE2,
    "LIFE3": LIFE3,
    "LIFE4": LIFE4,
    "DESOLE": DESOLE,
    "HASARD": HASARD,
    "SOMMAIRE": SOMMAIRE,
    "HREBOOT": HREBOOT,
    "NREBOOT": NREBOOT,
    "SORRYREBOOT": SORRYREBOOT,
    "BUG": BUG,
    "BREBOOT": BREBOOT,
    "REBOOTX": REBOOTX,
    "REBOOTY": REBOOTY,
    "MALAISE": MALAISE,
    "PLAISIR": PLAISIR
}
