#!/usr/bin/python
# coding: utf-8

from random import randint

"DRIFT/COPY/PASTE POETIX"

wordList1 = ['Mane brought field recordings of poor southern Work/Death,',
             'tele_trap(trap) bloated and almost immobile n hand to hand combat',
             'TWO-LANE BLACKTOP sober raver waited by the counter, inhaling slowly the keen reek of drugs',
             'possessed by an occupied Matte black where food insecurity is greatest',
             'colonial intellectual cartography Using salt circle runes to trap rewolf ”, S_HUMAN, LVL',
             'Chainsaw dipped in turpentine would rather feel your spine than your skull',
             'Sometimes the clock moves slow, and sometimes it’s Corrupt Turn up with a veil and black bag',
             'the thunder turns the needles, and now every riot cop has snapped the sabre',
             'reeling from a drought time-feed now obsolete)”',
             'dom strobing nightmare rare scenes from tinscavenger m4t',
             '(Var Full branch; so llow faced trojan (',
             'w_location, 0, 0, il machines arouse (A six year begins to wonder',
             'nickelride EX, SEEY); magined a garden (noi',
             'A perfect metaphor for the mysterious holes in her jaw day’s stations',
             'remove_room((unsign C, H, and D When jungling in town, resp',
             'bounds.ascent - ep extensive distortion, and use of noise and found-obj Knic dandolcc',
             'open their minds in the way only severe trauma or dropping acid do hey motherfuck give me your bitcoin',
             'Obsolete Presence { FOOD_RATION, let the carcase go',
             'fire cannot be separated from 25 years to GUILLOTINE placed uniformly on a dirty canvas',
             'Plastic Ghost” ters—it’s borders, before genocide, before colonization',
             'MaskedWall_and those who followed him fect( “lying_down” );',
             '“tiger smells a corpse” MACHETE HEART has disconnected from its clients.',
             'moss cemented/ to ieeinkadrav all wrapped in spider silk',
             'Venomous in story; gen e bleak flatlands cultivate ur disguise closet',
             'THE FUTURE waving a machete snug in blankets. hell yeah [she/her]',
             'kin tubby theft, genocide, bondage gentle in epilogue;',
             'face the inescapability of the past: BALL OF FIRE gave industry an organ.',
             '/* here after fencegate_The sun is gone at June 28, 2017 at 09:04PM but I have a light',
             'tome-trea past the furnace entre science et fiction',
             'n the evening hours ach beth ose masks do anythin',
             'gantic, rambling Pungent smoke shot up “Maryland Regiment Burial Site”',
             'ghost blade in m crystal dig find: Hourglass crosshairs',
             'anthropic garage filled wit cold skin/clay',
             'pull up with a stick, suck it off I pray for your soul mov (r3),aexp',
             'w realdoll script — no instrumentation to radicalize',
             'house of Wor en seven stairs like an exploding bomb upon a dazed and sleepy town',
             'los padres suade armed pirate back-stairs',
             'thorns and cross erased decades of “iron chain”,',
             '/// Model 1, cold wind chill respond to critical serv outfit and recurring gestures.',
             'aelseN-son sintHe grave was destroyed during the construction of creflo dollar',
             'hance images full of thread-tail arm volunteer guards.',
             'the fugue illuminated the paths of a town that existed in black & white will flow and blood will spill',
             'Saving this screenshot fr all the tired horses n the sun shine during deluge.',
             'digital version of re-poeticcult the broad expanse of flat land',
             'Intercept: riddim faught case JOY_AXIS',
             'so difficult to emulate marine-set reatures made of pure evil',
             'Second my Rosary, xel-p mest antechapel',
             'plant/shee RUSTBELT VIRGIN MARY Turns Border Fence Into Wall Of Sound',
             'now ignored. faithful repentance; I am the stranger from the sky',
             ': ndemon(atyp); ject (ge 2012 april | added wn personal opioid crisis',
             'u actually listened to barren sand and rock a slave revolt was underway.',
             '(obstructed(x, y, mysterywand)) Dedalus Mirrored Flame” / “Swallow (This City)',
             'readme file that says The allowance was a ticket to freedom; n the dark',
             '—Bocc blood work don hind the tracker curtain',
             'the jail is a fine school di ct wa bi g complicated life on the lam',
             'want to act like public gazes across the clear-bl ons[PM_SHADE] ||',
             'call up your boy and tucc him into bed The pictorial account omits the presence of the knuckle to impress',
             'enfold the ke scatterer: she bel llow the flask"',
             'anonymous hacc reanimates history and breathes new life into the narrative of aural retribution',
             '“Assaultline Static-consuming misanthrope, once ignited, coffin-hinge as remedy.',
             'wulfkllr words mitl “arrow”, “dart” or “spear”, and omitl “bone”; seen by two witnesses',
             'i’m adding to the horde of voices rethinking cultural influence between the spring mattress',
             'BLOODYMINDED oil and tincture of Your Back As You Fade Away',
             'DRONE-BUILDING bandito rose on the st',
             'The second victim) Wasting materials, space and “stdout, stderr',
             '“Jade Figurine”, jade_figurine_pic, Down By Law read from the same buffer',
             '::join(m_w wandering over the multicoloured hoarding Prison Sky',
             'think they r radically changing th seminaryglove in her locked drawe',
             'lo-key excited with knife-like piece of the grand configuration',
             '-Purp to RITUAL AND CAPITAL, An injury to one',
             'alien covenan t-S tronger than its weakest chain.',
             'gret the rope error_current_nimal finds',
             'brand-new place chosen Seems more like a graveyard then a town isol8 / destroy everything / delete',
             'a moment of silence where no one knows what to do next. Speechless, textless deserted shack',
             'u don’t have to sacrifice p.:ntichlEdudDi n exchange for flowers.',
             '“Desire Ferry leaves at the top of the hour ( Plucked_ctor ); stores close down, neighborhood crime goes up',
             'memory (there shouldn’t be any). keeps its structures more faithful and conventionally melodic Wasted potential on a real lvl',
             'Rag and Bone algorithm grew uncontrollable, uncompromising and vicious.',
             'Two Confession ulptures unleash their dark new Style Forecast',
             'lask by antiq seized momentarily within spaces, both physical and psychological, canvas bondage',
             'late-stage cartelthougts lay motionless in the same place',
             'significant imp move_other Found Dead Next to a River',
             'shepherd with an AK-47 en-box. an absent face',
             'last 2 tapes, each unique scratched by Insurrection,',
             'tst rdflg “El Oscuro before they kill millions” llection of presets',
             'a man’ - Ame n all weathers mashing the Caliphate',
             'a voluntary surrender of power and influence_( “| Damage | Pierce | Ese conflicto es a su vez admisión de culpa',
             'Resurget Cin -inlaugh by Jailin',
             '(formerly “domestic prelates”) rip yr own head off til summer comes',
             'a (small) Livre des propriétés des chos E R BANG SCREW',
             '[An] Occurrence at ’s wire ncountering lateness',
             'bor Scavenger tomes. Re leased Dedication',
             'i put my ear up to the glory hole & listen take no vows and live normal, everyday lives), irst bow to the public.',
             'a tomb of blood, mapping bitter readers',
             'Secret for 14 yrs Excavators incl. Jul; Grey: eve',
             'personal salvation—in cludes gem s iving down a dark highway.',
             'without a bramble (when embedded in three-dimensional Euclidean space) Touch and go with him.',
             'regicidal Eyes (Fil underpasses in the rain',
             'loud block partie mentioned radiuses” c. Seek a concealed site.”',
             'thee birth canal of sword-like void AddLightBlend',
             'four moods drag what’s left of silence anywhere –',
             'bers – ‘Sha ke, and snuf iff item lands on an altar */',
             'dripping, dark—bury me w limited utility, and with the introduction of more automated radars',
             'Junction, Roc able: b astard',
             'GATE y tours : allude to–but never fully explain–his disappearance.',
             'can’t be easy to act under such a heavy mask ...opening a door—a full year passed words and hidden map points”',
             'nomous police cars paired w/ the thirst for salt. half-dead people blindly staggered through the streets',
             'you tried refraining from a partnership as close as horse and rider. Unnamed Road, Leb',
             'to establish a mode of trust. case TLOSS: ease “Gagg',
             'tics:a si nking in the gravel. mostly used on domestic dissent.',
             'despair of our drab, Gulf ” conjured images of spoken number transmissions',
             'marginalized con on. Compiler casts every day, and is a mixture between voice and digital.',
             'a modern day highwayman, if (weapon.made_of(“leather”)) living in a highly militarized fantasy.',
             '‘humbling, sacred places in th long con Hail up to 9 cm',
             '|| joyxmove on sanctuary thout a warrant.',
             'mulated phishing attacks fit into your coffin made of bases[WILDCARD_LEAF_NAME]',
             'night live-fire range—all reduced to filtered noise. drains of color',
             '“Despite a brief obsession with the ghost mal: Centralized cross hanging from her neck',
             't AFA; rea ads THE VALLEY',
             'bootleg search for new mea r: a Warning from history.”',
             'an unidentified hospice d-sherm Por isn’t inscribed anywhere.',
             're devils, Rest In Power the source of light and understanding, which is the east',
             'objects work fine when hallucinating, but waving little flags FochresletrepirLim82',
             'with the subject: THEIR Scatological care for those in the twigh',
             'light of screens make us écouté mask = &EAntimagic;',
             'everything ahead of me, as is ever so on the road radio signal cant reach no cameras/recordings']
wordList2 = ['qS!QA et tendre',
             'A body up and dies',
             'Find the nearest lamppost',
             'site (ori  his owner',
             'MONDUSTRIAL POLICY',
             'blood and fluids',
             'in UNDERCOVER',
             'DownlBeek: Alb',
             'LivI Discover',
             'rosscAssembly | Mo',
             'Weathschools, crids mp time to lean',
             'the regression of western historical thought',
             'and solace -to',
             'sound beating a book in a pulpit',
             'screened gems',
             'Shadow Arch as other classe',
             'the highest stage',
             'the basement video',
             'Me cago en toda tu maldita descendencia, rarely recognise a "resilient city"',
             'a slanted roof (signifying a house) inopportune strate ms. Galore: begone.',
             'Sint Den tour - Tic ease at Molasses',
             'mine Dream An open saint may A line of peace',
             'feedback on Di rectional refs)chines—a',
             'paashaasjes naq napvyyn',
             'CORRUPTION PERCEPTION',
             'The Ones That Play Chicken Wit rack “En Trance forged their own paths',
             'Tupitsyn: Ra Dossier on Expanded fields, 3 / Blank',
             'countering lateness in Camera obscura (San USE].name',
             'ate(tern adapt to rating, was rapid-fire, and nothing unfastened.',
             'prelude to the sound of caste, bu and anti-resilience fe',
             'every other world in el bar turbulent drin',
             'control the garment ths dusky, ra naked-ey',
             'until we devour the subtle game',
             'SACRIFICE',
             'LOCKSS/CLOCK',
             'more like privilege',
             'if (!hInstDS)re seedy through algorithms',
             'New deaddrop (USB drop) in register int year; authenticity, vigor',
             'tyles misses the crucifix roll-enic gun-brig fed sentimentalists',
             'Empathy is biased: multilanguage ect rose garden; wh',
             'tclIndex" re spare-body to visit the alternate',
             '8irn ly festivities wearing fake burlap fet',
             'a hut-keeper during the night',
             'Wend quickly']
wordList3 = ['*']
wordList4 = ['always inspired Cause of death',
             'your Essential',
             'their exhibitions of Pioneering',
             's - Fox Matchng',
             'Virgst at home',
             'Suffering fbesity',
             ':(',
             'with mountain',
             'S/o to all the unemployed',
             'Soft blocking ever',
             'op with corrugated plastic',
             'sent a small delegation',
             'listed as exceedingly markov chainable',
             'wear a bondage collar',
             'high-tech smokescreen to ramp up deportations',
             'cal lockpick',
             'an Instituter',
             'transpose the deck',
             '_hef',
             'Les Fleurs',
             'removed from office',
             'along with excerpts from the novels',
             'SCOLXXXX',
             'subject, Hobo',
             'year (all signed',
             'med spittle',
             'but a draught—nay',
             'cracked high ceiling',
             'plea was earmarked',
             'back by cops',
             'childraising',
             'bat-signal',
             'our water tastes',
             'you accepted other corpses',
             'str(actual_ty)',
             'Or ghost',
             'hands of collectors',
             'All four']
wordList5 = ['Bridge (atonement) crucifix w Disobedient Electronics',
             'New Ascetic street provocations get_voicegain);',
             'hrnts nst frmed arnd doom2.wad not battalions',
             'the burying ground on the little hill where the church is ur Skin Crawls into the glooms',
             'red ligh—stream ‘Graphic’ sometimes with objects, into the ground',
             'nomad, mooner subrooms[i], r); shot with rubber bullets for celebrating their existence',
             'tencing set for acolytes set loose from the yoke of language',
             'to forecast—with eerie prescience—“nonviolent”, an “opinion” or Ex-Worker',
             'movecmd(sym) surprise attack on an encampment of plant tongues',
             'yuNeM N A DARK ROOM ner - Clouds',
             '(swallows roughly) yes. I’LL SMUT YOU OUT I have moved to a bucket inside a cave.',
             'et / The only Escrivá w a bright light',
             'e].oc_delay; build the visual language for dead heard',
             'Workhouse Prison language flourishes, ancient byte far *',
             'spiritually bankrup LastCityYear baptiste',
             'a red mass empties but it’s under threat [again] Take out all rubbish which you can’t burn. Avoid burying rubbish',
             'with my fist Occult Roots ignore your texts',
             'Bohemian Grove will commence with House Numb landless, wifeless.',
             'our 1st death to signaling. signing. flagging. telegraphing. transmitting. broadcasting. believer in ghosts, my friend?',
             'my shadow here exceptBrushes); sounds, full of Leviathanism,',
             'NA ZONA -lean spearflag; th magical (totalising) power',
             'on the war path “But they pledged…” 2. Electricity. 3. Food supply.',
             'La Ciénaga Cutworm - Now disloyalty by leaking',
             'sift cult Bullets wandering into unmarked storefronts',
             'VARG / MARSH milkweed in my garden depoliticizes capital',
             'ar dogmestic Obscura: r Qeted',
             'machete eye thirst is real ‘go dark’ through the use of encryption messaging',
             'North-Ea dure (still in Tcl). overshadowed by soundbites',
             'Death / Nightmark Via crimethin Endearment” | Au',
             'year-end screenings of Vertical Geographies',
             'INSURGENT GROUP if (trapkilled) shelters, wh',
             'Séancé fea ders’ enduring collaborations: around the fallen statue',
             'Let’s erase stigmas of rural/cons already revolving towards another beginning.',
             'walking into a pool whose floor sank as they walked, submerging them * and the environ array itself has this between sudden showers',
             'leaked dossier from a former “sound rubbish” killing net',
             'The Mask and The Crow y favourite slaves Splicing the sonic color-line',
             'From the Vaults: his imperia revival/surge',
             'n the cicada’s screech das, and Fur ests, Black And Low',
             'White Plains Leather pub.process_an inorganic life of things”',
             'Pangs’ (avail Blood, piss and clawsofthefog',
             '“ subroutine sundial tow a true calm.',
             'inside bear part1 Vampiric power’s in cryptocurrency',
             'Pole rope Chapter 3 Spring, Summer, Fall, Winter... and Spring so vast is the quantity of blood in him',
             'Haram has left The poverty just over the hills .DEF ShowWind',
             'violet wand set possibility of being easily changed, a mobile. can’t fuck you tonigh',
             'In the Only Surviving Recording of Her Voice, someone across the street yelled Hardcore will never die.',
             'New deaddrop (USB drop) register int year; authenticity, vigor',
             'we feel entitled to flog others for being tons - WHITE LIGHT architectures',
             'against public space h arm */ters protected clergy',
             'hack_high cities may follow—roses to comfort the wounded.',
             'preferring her banner “forty times” better than a sword; Failing Lights cannot altogether conceal this vacillation.',
             '’m gone bet on Dusk and the light behind her crawling along pipes and out into freedom via a manhole cover',
             'paso those landlords dragged over rotted floorboards',
             '“S.D.G” (Soli Deo Gloria) — Fine w me. site specific INCAPACITANT',
             'to hack, deface, and dox all stepper “W dust under the boots',
             'Fantasizing about a large house with many rooms “ecstatic truth Clouds in the water.',
             'earth and grass, (11 acre site) Figurative armorie declares war on sprawl.',
             'HIJOS DE The sunburnt so angelic',
             'a brief sharp unforeseen heard loud lone crack ear;y drift t/wards mid push->ymove = topinto;',
             'after I eventually ghost night lies frightened // true if self is on ground',
             'fuccboi Rammellzee raw video capture',
             'the most-respected name in blood obsession I write/edit/speak',
             'waves_between_caravans = drug epidemic “Everything changes, nothing is lost”',
             'sawing wood and it made me dream (She clutches the two crowns) A sys [te]/m/r appears',
             '- stone with a natural hole through it the strait”) traphouse',
             'At night no one can hear th Cursed Idol READING THEM INTO A GRAVE',
             'a locomotive footprint with teeth like barbed wire led me to a quarry',
             'a spellbinding collage of pretty black against you we stray further from God’s light',
             'on /r leeve (it just seemed the natural thing to do), Corpse Flowers Blooming',
             'one set of rules in order to CEIL The Fat Of The Land',
             'Sacrificial Pits, nal(-scorch “secret flights over their territories”',
             'naturally learnable set of behaviors with one oar, standing near the Ether Music',
             'TO ALL MY RIDE-OR-DIES…rgal. sir gal. the binary broken by this beautiful Solo autumn',
             'no escape from an Escape Room th grenade pins bey like a slave',
             'dog-head capture objects from LOCUS.exe',
             'the last trash - Ballads ( facsimiles that serve mainly to show us the richness of the original.”',
             'trait IV,” by De eft column: wear small rocks',
             'the serene storm merge jok supports (PLANK), belonging',
             'the concerned outgift of the dead med dirt fugue racters welcome.',
             'aperture de La Nave /numb daylight 06:13-18:01',
             '0bscenegesture Subway digging uncovers ‘Jade Helm’ war exercise',
             'The homesick wav (striped) using salt and antifreeze',
             'Royal Blood care cadre that checks stress positions',
             'Clei t_floor_waxed, govt and here is',
             'digenous reserves are th fetish of my tose-obsessed ethnostate',
             'at night / washing my dump cart n Corpus Christi',
             'circulate your blood through Thes cripted conversations with men on the street (filmed with hidden cameras)',
             'A bothy email thread laying out offers of boiler rooming.',
             'he is only dispirited; following the death of GERONIMO',
             '“MBCBFTW” Self-trict crew took me under their wing',
             'Pelen Renc6-1de one rave per weekend Imagine a wolf shooting a fang',
             'the Flesh Eaters 15 proyectos No one keeps a closer watch.',
             'considereation conceptualk ed organ-case bull-like',
             'techre ler))) on tire Bodies.',
             'these places feel, here making the world’s city-dwelling sim Haul in the chains',
             'RAVER STAY ladder of the west narrates Crips and Bloods',
             'geyser of our blood under the walls glow the fuck up',
             'Un Blonde, Malaria horizons, front like they are shamans.',
             'terial of ld Sound Bodies hol, Edges +sg - S',
             'the politics of native sovereignty played backwards to replicate the sound of large groups (6 or more)',
             'Shattered glass “monuments” in a chat His mouth opens, words jump in',
             'The sun is gon Suffocated by grai connectivity',
             'Mala Noche: guerrilla fighters will emerge hauntingly dreamlike',
             'Day of Solidarity W Variant (Parts I, II, I t is the host',
             'Lesson: Territories of overcodin a wretch like me',
             'he tears her skin, revealing a black, featureless body snds like voices: C U THERE',
             'morning writing benedictions 2get hit in the face by teargas & stun grenades] behind our room',
             'now and again, i’m without capitalism the myth world”',
             'felis panthera analysis/history crossed a line',
             'roß – 1 Panting and snorting like a mad battle steed el “Time Machines” de Coil',
             'ci belt, Raf on y alive inside/our anatomy Sigue el exterminio sin llorar',
             'the “tar-dark world” sed to LIKE the rai and subsequent brawl',
             'own destiny.. (Sun R mouthpiece for Sewer Elect',
             'kehole’s absol add_spawn(mon of art (including',
             '( “special:mar a simple way of sayin Preach New Blood, preach',
             'Clandestine Compositions: Vampyre braids will be in display case',
             '“These dunes are influenced by local topography” RolenSo - mixing all these forms for no reason.',
             'dropped my phone and it shattered Spiritual American Eating meat',
             'Periodic reminder Sis e-up here: as if summoning something nasty.',
             'white flower institutionalization: I want to scrape it off my skin.',
             'Silkbless et x Corrupted tribes have to go',
             'wealth disparity will collapse th (Domestic Scene), AFK and otherwise',
             'study the contrast between extended periods cel(t- (first sec of FAT)',
             'Ancient wall (10th century) with holes for rafters 2 miners completed Rope Bondage, Mummification, etc.',
             'Disease-carrier” build your own mergency shelters-of-last-resort',
             'new-old frie sleeping on the floor, fasting mong the tombstones',
             'striped actions bathe outside, screens reflect the cell; nomadic',
             'CHeld3,wroun Breaking into th window displays throughout the city',
             'a message for th military/police state, with its walls and borders ‘Ten Flowers’']
            
wordIndex1=randint(0, len(wordList1)-1)
wordIndex2=randint(0, len(wordList2)-1)
wordIndex3=randint(0, len(wordList3)-1)
wordIndex4=randint(0, len(wordList4)-1)
wordIndex5=randint(0, len(wordList5)-1)
stanza = wordList1[wordIndex1] + "\n" + wordList2[wordIndex2] + "\n"
stanza = stanza + wordList3[wordIndex3] + " " + wordList4[wordIndex4]  + ",\n"
stanza = stanza + wordList5[wordIndex5] + "\n"

print "\nDRIFT/COPY/PASTE POETIX:\n\n" + (stanza)