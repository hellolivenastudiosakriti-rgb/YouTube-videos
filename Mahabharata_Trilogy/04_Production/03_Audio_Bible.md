# महाभारत त्रयी — AUDIO BIBLE (LOCKED v1.0)
Music · Sound effects · Voices · Mix — **Google Flow Music pehle, ElevenLabs sirf wahan jahan Flow nahi kar sakta.**
IDs yahin define hote hain; shooting scripts (`Part*/P*C*.md`) inhi IDs ko use karte hain; `tools/mbx.py compile` har ID check karta hai aur `build/cue_sheet.csv`, `build/sfx_usage.csv`, `build/vo_all.csv` banata hai.

---
## 0. TOOL REALITY CHECK (23 Nov 2026 — launch ke pehle khud verify karein)
| Tool | Kya karega | Abhi ki limits / shartein |
|---|---|---|
| **Google Flow Music** (pehle ProducerAI; Apr 2026 se Flow Music; Lyria 3 → **Lyria 3.5**, 29 Jul 2026) | Saara background score: themes, action, ambient, gaane | Track length + tempo control, **~3 min per generation**, *extend* aur *replace section*, apna audio upload karke remix/cover, **stem split**. Free tier mein daily credits; commercial use paid tiers (Starter / Plus / Member) par listed — monetize se pehle terms padhein. |
| **ElevenLabs Eleven v4** (28 Sep 2026; v3 fallback) | Saare dialogue aur narration (TTS), audio tags se acting | 90+ languages bataye gaye; Hindi ki quality **pehle 10 lines par test karein**. Tags jaise `[whispers]`, `[angry]` — SSML break tags v4 mein band hain, pause tags se hota hai. |
| **ElevenLabs Voice Design + Voice Remix + Voice Changer (STS)** | Har character ki locked voice; umar ke variants; Veo ki boli ko character ki awaaz mein badalna | Ek baar design karke "My Voices" mein VOX ID ke naam se save. Variant (jawaan/boodha) = usi voice ka Remix, nayi voice nahi. |
| **ElevenLabs Sound Effects v2** | Saare designed SFX + loopable ambience | **Max 30 s per generation**, seamless loop option, non-loop WAV 48 kHz. |
| **ElevenLabs Eleven Music** | Sirf exact-text Sanskrit chant cues (fallback) | Commercial use paid plan par, **lekin film/TV/radio self-serve terms se bahar** (Enterprise chahiye) — isliye isko **minimum** rakha hai. |
| **Veo 3.1 (Google Flow) native audio** | Clip ke andar ka Foley + lip-sync wali "temporary" boli | Final mix mein ambience/voice ElevenLabs se replace hogi (har clip ki native awaaz alag hoti hai = drift). |

---
## 1. LEITMOTIF MASTERS — Flow Music mein SABSE PEHLE yeh 17 banaiye
Har theme ka **ek approved master (2:30–3:00)** banega. Har scene-cue usi master ko **upload → remix/cover/extend** karke banega, taaki dhun poori trilogy mein ek rahe (music drift = 0).

| THEME | Name | TOOL | PROMPT (Flow Music / Lyria 3.5) | DUR |
|---|---|---|---|---|
| THM_MAIN | महाभारत — मुख्य थीम | FLOW | epic Indian orchestral main theme in a dark Bhairav-like mode, 72 BPM rising to 96, massive earth drums and pakhawaj ensemble, low brass, string ostinato, sixty-voice male chorus on long open vowels, a sustained conch-like horn call; heroic, tragic, ancient; no Western pop drums | 3:00 |
| THM_BHISHMA | भीष्म — प्रतिज्ञा | FLOW | solo cello lament in slow descending Darbari-like phrases, joined by low strings and soft distant drums, 60 BPM; the loneliness of an unbreakable vow | 3:00 |
| THM_KARNA | कर्ण — सूर्यपुत्र | FLOW | solo bansuri in sunset Marwa-like phrases, wounded and proud, slowly rising into a radiant brass 'sunrise' chord with strings, then collapsing back to the single flute | 3:00 |
| THM_DRAUPADI | द्रौपदी — अग्नि | FLOW | raw solo sarangi in Bhairavi, almost a human voice crying, low tanpura drone; second half a full orchestral swell with frame drums; fire and dignity | 3:00 |
| THM_SHAKUNI | शकुनि — पासे | FLOW | sly unsettling cue, dry pizzicato strings, wooden clicks and rattling dice-like percussion, low drone, a creeping descending chromatic motif on santoor, 84 BPM | 2:30 |
| THM_KRISHNA | कृष्ण — शांत केंद्र | FLOW | rudra veena drone and slow plucks, warm low strings, distant hummed male chorus, gentle mridangam, unhurried and knowing; the calm eye of a storm | 3:00 |
| THM_WAR | युद्ध | FLOW | relentless war ostinato at 138 BPM, massed dhol and nagara kettledrums, pakhawaj rolls, huge low hits, brass stabs, horn calls, a dissonant male choir underneath; brutal, no melody hero | 3:00 |
| THM_DHARMA | युधिष्ठिर — धर्म | FLOW | tanpura drone, solo male ālāp without words, sparse strings; steadfast and sorrowful | 2:30 |
| THM_BHIMA | भीम — वायुपुत्र | FLOW | heavy mridangam and dhol groove, low brass growls, roaring horns, joyful brute strength that can turn terrifying | 2:30 |
| THM_ARJUNA | अर्जुन — गांडीव | FLOW | rising string arpeggios over a metallic bowstring-like pluck motif, noble horns, focused and graceful, 90 BPM | 2:30 |
| THM_DURYODHANA | दुर्योधन — अभिमान | FLOW | proud slow march on nagara and low brass with a nasal shehnai-like reed, wounded royal pride | 2:30 |
| THM_KUNTI | कुंती — छिपा प्रेम | FLOW | a lullaby fragment hummed by a soft female voice over swarmandal plucks and low strings; secret love and guilt | 2:30 |
| THM_FRAME | सर्पसत्र — कथा-मंडप | FLOW | ritual dread: low drone, crackling fire, hissing textures, distant murmured male chant without clear words, slow frame drum | 2:30 |
| THM_KALA | काल — नियति | FLOW | cosmic inhuman cue: overtone throat-singing drone, sub-bass pulses, slow cymbal swells, a choir that sounds like wind; time devouring everything | 3:00 |
| THM_VAN | वनवास | FLOW | longing forest theme: bansuri and soft strings, monsoon textures, distant birds, slow 66 BPM | 2:30 |
| THM_ABHIMANYU | अभिमन्यु — बालवीर | FLOW | bright youthful heroic theme: fast strings, ringing horns, war drums, 120 BPM, ends broken on a single note | 2:30 |
| THM_GANGA | गंगा — माँ | FLOW | flowing harp and jal-tarang arpeggios, wordless female choir, water textures; a river who is also a mother | 2:30 |

---
## 2. SCENE CUES — chapter-wise (MUS_*). TOOL: FLOW = Flow Music · ELM = ElevenLabs Music · SIL = jaan-boojh kar silence (no cue generation)
| CUE | Moment | TOOL | PROMPT (base theme + scene change) | DUR |
|---|---|---|---|---|
| MUS_P1C01_A | Cold open — pit drums only | FLOW | earth drums only, 72 BPM, starting from near silence, slowly building, no melody | 1:40 |
| MUS_P1C01_B | The charge | FLOW | THM_WAR full force, chariots colliding, ends on a cut | 1:30 |
| MUS_P1C01_C | Sarpasattra | FLOW | THM_FRAME with screaming-serpent textures underneath | 2:30 |
| MUS_P1C01_D | TITLE — म…हा…भा…र…त | ELM | THM_MAIN chorus: deep male choir sings five separated hammer-blow syllables "Ma… ha… bhaa… ra… ta" over earth drums and conch horn, 7-second stretch, then orchestral hit | 0:45 |
| MUS_P1C01_E | Gaṅgā's seven sons | FLOW | THM_GANGA turned uneasy, a repeated splash-like harp figure | 2:30 |
| MUS_P1C01_F | The arrow dam (only heroic Bhīṣma) | FLOW | THM_BHISHMA made heroic: cello + low brass + pit drums, building to a burst | 2:00 |
| MUS_P1C01_G | Four golden years | FLOW | warm pastoral strings and bansuri, father and son | 0:50 |
| MUS_P1C01_H | Fragrance on the wind | FLOW | mysterious romantic cue, santoor and strings, river at dusk | 2:00 |
| MUS_P1C01_I | The vow | FLOW | THM_BHISHMA: one solitary cello note growing; at the vow a choir rises as flowers fall; ends in awe | 3:00 |
| MUS_P1C01_J | The boon | FLOW | THM_BHISHMA resolving into the loneliest chord of the film | 1:30 |
| MUS_P1C02_A | The breaking line (montage) | FLOW | THM_KALA with strings, a heartbeat-like drum, montage pace | 3:00 |
| MUS_P1C02_B | Niyoga | FLOW | dark single-lamp texture, low reeds, unease | 1:30 |
| MUS_P1C02_C | The blindfold | FLOW | one low drone that stops dead when the knot tightens | 1:00 |
| MUS_P1C02_D | Sūrya's mantra | FLOW | rising heat drone, shimmering strings, blinding crescendo | 2:00 |
| MUS_P1C02_E | The basket on the river | FLOW | THM_KARNA first statement (bansuri alone) answered by THM_KUNTI hum | 2:00 |
| MUS_P1C02_F | Kindama | FLOW | tense forest cue, sudden stop on the arrow | 1:00 |
| MUS_P1C02_G | Births and the split rock | FLOW | wonder cue with a sub-boom on the rock splitting | 1:30 |
| MUS_P1C02_H | 101 pots and the jackals | FLOW | dread; THM_DURYODHANA first faint statement; lids like a funeral drum | 2:00 |
| MUS_P1C02_I | Mādrī's pyre | FLOW | grief, wordless female vocalise, fire crackle | 1:30 |
| MUS_P1C02_J | The ṛṣis vanish | FLOW | eerie suspended chord, then nothing | 1:00 |
| MUS_P1C02_K | Satyavatī walks into the forest | FLOW | THM_GANGA as an elegy, strings only | 1:30 |
| MUS_P1C03_A | Bhīma the bully | FLOW | THM_BHIMA as playful percussion | 1:00 |
| MUS_P1C03_B | Pramāṇakoṭi — feast to drowning | FLOW | festive to sinister; underwater section slows to a heartbeat | 2:30 |
| MUS_P1C03_C | Cobras and kālakūṭa | FLOW | creeping strings, comic release at the burp | 1:30 |
| MUS_P1C03_D | Droṇa and the reeds | FLOW | austere cue, single plucked string, reeds clicking | 1:30 |
| MUS_P1C03_E | Ekalavya's devotion | FLOW | THM_VAN forest bansuri, devotional | 1:30 |
| MUS_P1C03_F | Seven arrows | FLOW | sudden held breath, string tremolo | 1:00 |
| MUS_P1C03_G | The thumb | SIL | NO MUSIC — only birds stopping and breathing | 0:00 |
| MUS_P1C03_H | The bird test | FLOW | THM_ARJUNA first statement, narrowing focus | 1:30 |
| MUS_P1C03_I | Crocodile and brahmaśiras | FLOW | short action cue then an ominous hush | 0:50 |
| MUS_P1C03_J | Arena display | FLOW | festive drums, THM_ARJUNA bright | 2:00 |
| MUS_P1C03_K | Karṇa walks in | FLOW | THM_KARNA brass sunrise over the bansuri; hard cut | 1:30 |
| MUS_P1C04_A | The challenge — the sky chooses | FLOW | THM_KARNA against THM_ARJUNA in counterpoint, storm drums vs radiant brass | 2:30 |
| MUS_P1C04_B | Kuntī faints | SIL | NO MUSIC | 0:00 |
| MUS_P1C04_C | Coronation of Aṅga | FLOW | regal processional, conches, drums | 1:30 |
| MUS_P1C04_D | The father | FLOW | tender strings, THM_KARNA fragment | 1:00 |
| MUS_P1C04_E | Duryodhana's roar | FLOW | THM_DURYODHANA bursting into full march | 1:00 |
| MUS_P1C04_F | Torches | FLOW | THM_KUNTI secret smile woven with THM_KARNA | 1:30 |
| MUS_P1C04_G | Drupada humbled | FLOW | military cue, then bitter quiet | 1:30 |
| MUS_P1C04_H | Vidura's riddle | FLOW | suspense drones, whispered textures | 1:30 |
| MUS_P1C04_I | A year in the lac house | FLOW | ticking suspense, low pulses | 2:00 |
| MUS_P1C04_J | Storm night — six sleepers | FLOW | dread to dead silence before ignition | 2:00 |
| MUS_P1C04_K | Inferno and the run | FLOW | THM_BHIMA heroic run, massive percussion | 2:30 |
| MUS_P1C04_L | Stars, false mourning | FLOW | THM_DHARMA with an elegy for Hastinapura | 1:30 |
| MUS_P1C05_A | Hiḍimba | FLOW | raw forest fight percussion | 1:30 |
| MUS_P1C05_B | Hiḍimbā and Ghaṭotkaca | FLOW | wild tender cue, huge drums for the giant child | 1:00 |
| MUS_P1C05_C | Baka | FLOW | comic march turning horrific | 1:30 |
| MUS_P1C05_D | Born of fire | FLOW | THM_DRAUPADI first statement — sarangi rising out of fire roar | 2:00 |
| MUS_P1C05_E | Gandharva on the Gaṅgā | FLOW | night action cue with eerie strings | 1:00 |
| MUS_P1C05_F | Svayaṁvara pageant | FLOW | royal procession; THM_KRISHNA almost subliminal | 2:00 |
| MUS_P1C05_G | The bow | FLOW | THM_ARJUNA payoff, five beats for five arrows | 1:30 |
| MUS_P1C05_H | Kings' brawl | FLOW | light THM_WAR, Karṇa–Arjuna exchange, Bhīma–Śalya | 2:00 |
| MUS_P1C05_I | "Sab milkar bhogo" | FLOW | comic sting, then a held question | 0:40 |
| MUS_P1C05_J | Five weddings | FLOW | joyful shehnai wedding music, folk drums | 1:30 |
| MUS_P1C05_K | Indraprastha rises | FLOW | building montage, hammers as rhythm | 1:30 |
| MUS_P1C05_L | Sunda–Upasunda (shadow play) | FLOW | shadow-puppet theatre ensemble: harmonium-free, mukhavina reed, chenda drum | 1:00 |
| MUS_P1C05_M | Twelve years (Ulūpī, Citrāṅgadā, crocodiles) | FLOW | travel montage, sea and river colours | 2:00 |
| MUS_P1C05_N | Raivataka festival | FLOW | festive Yādava song with joyful wordless chorus, clapping, drums | 1:30 |
| MUS_P1C06_A | Agni's hunger | FLOW | heat drone, crackling | 1:00 |
| MUS_P1C06_B | Gāṇḍīva rises from the water | FLOW | THM_ARJUNA with THM_MAIN horns; awe | 2:00 |
| MUS_P1C06_C | Khāṇḍava burns | FLOW | THM_WAR 138 BPM with a dissonant choir that makes the audience uneasy | 3:00 |
| MUS_P1C06_D | The four birds | SIL | MUSIC TO ZERO — only fire breath and tiny voices | 0:00 |
| MUS_P1C06_E | Maya builds the hall | FLOW | wonder cue, glassy textures made of struck stone and bronze | 1:30 |
| MUS_P1C06_F | Jarāsaṁdha — the 14th night | FLOW | no music for the fight; one roaring brass-and-drum sting at the kill | 0:20 |
| MUS_P1C06_G | Digvijaya | FLOW | four-direction montage march | 0:40 |
| MUS_P1C06_H | Rājasūya and Śiśupāla | FLOW | regal to tense, cuts dead at the discus | 2:30 |
| MUS_P1C06_I | The pool | FLOW | light comic cue that sours | 1:30 |
| MUS_P1C06_J | Śakuni's offer | FLOW | THM_SHAKUNI full statement | 2:00 |
| MUS_P1C06_K | The invitation | FLOW | single deep bheri drum, funeral pulse, nothing else | 1:00 |
| MUS_P1C07_A | The game | FLOW | THM_SHAKUNI accelerating over the bheri pulse | 3:00 |
| MUS_P1C07_B | Women's quarters | FLOW | tight tension drone | 1:00 |
| MUS_P1C07_C | The dragging | FLOW | low strings only | 1:00 |
| MUS_P1C07_D | The question | FLOW | near-silence; sarangi enters only at "धिक्कार" | 2:00 |
| MUS_P1C07_E | Bhīma, Arjuna, Vikarṇa, Karṇa | FLOW | taut strings, a rising pulse | 1:30 |
| MUS_P1C07_F | The miracle | SIL | ABSOLUTE SILENCE — room tone only | 0:00 |
| MUS_P1C07_G | Bhīma's blood-oath | FLOW | a sub-bass swell under his voice, then cut | 0:40 |
| MUS_P1C07_H | The jackal and the boons | FLOW | THM_DRAUPADI full payoff, orchestra rises once under "लोभ धर्म का नाश करता है" | 2:00 |
| MUS_P1C07_I | Anudyūta | FLOW | the bheri pulse returns, colder | 1:00 |
| MUS_P1C07_J | The four vows | FLOW | THM_MAIN erupts — then cut dead | 1:30 |
| MUS_P1C07_K | Departure — Dhaumya sings the Sāmans of Yama | ELM | slow solemn Sāmavedic-style chant by one priestly male voice over a low drone, ancient and funereal (if ELM refuses, layer VOX_35 TTS chant) | 1:00 |
| MUS_P1C07_L | The empty hall | FLOW | almost nothing; a far conch-horn at the end | 1:00 |
| MUS_P1C07_Z | End credits — Part I | FLOW | THM_MAIN full concert suite with all leitmotifs | 3:00 |
| MUS_P2C01_A | Frame — the fire low | FLOW | THM_FRAME softer, the king exhausted | 1:00 |
| MUS_P2C01_B | Kirmīra | FLOW | rain and percussion fight cue | 1:30 |
| MUS_P2C01_C | Sūrya's boon | FLOW | THM_DHARMA into a molten-gold sunrise swell | 2:00 |
| MUS_P2C01_D | Vidura exiled and recalled | FLOW | anxious strings resolving warm | 1:30 |
| MUS_P2C01_E | Maitreya's curse | FLOW | low dread on the thigh-slap | 1:00 |
| MUS_P2C01_F | Kṛṣṇa's vow to Draupadī | FLOW | THM_KRISHNA with full orchestra under THM_DRAUPADI | 2:30 |
| MUS_P2C01_G | Saubha | FLOW | aerial siege action, iron and fire | 2:00 |
| MUS_P2C02_A | Dvaitavana argument | SIL | NO MUSIC — two cameras, a lake | 0:00 |
| MUS_P2C02_B | After the argument | FLOW | single drone as Draupadī turns to the lake | 1:00 |
| MUS_P2C02_C | Arjuna leaves | FLOW | THM_VAN farewell, first tenderness | 1:30 |
| MUS_P2C02_D | The Himālaya and the old ascetic | FLOW | cold high strings, wind | 2:00 |
| MUS_P2C02_E | Austerity | FLOW | THM_KALA slowed, seasons passing | 1:30 |
| MUS_P2C02_F | Kirāta fight | SIL | NO MUSIC — breath, snow, laughter | 0:00 |
| MUS_P2C02_G | Śiva revealed, Pāśupata | FLOW | THM_KALA with a vast choir, then stillness | 2:00 |
| MUS_P2C02_H | The world-guardians | FLOW | THM_MAIN on horns | 1:30 |
| MUS_P2C03_A | Ascent to Amarāvatī | FLOW | soaring cue through cloud | 1:30 |
| MUS_P2C03_B | Citrasena's lessons | FLOW | diegetic gandharva chamber music: vīṇā, drums, a voice singing sargam | 2:00 |
| MUS_P2C03_C | Apsaras dance | FLOW | celestial dance music, anklet rhythm | 1:30 |
| MUS_P2C03_D | Nala–Damayantī (shadow play) | FLOW | shadow-puppet ensemble, melancholy | 1:30 |
| MUS_P2C03_E | Tīrthayātrā tales | FLOW | travelogue montage, changing regions | 2:00 |
| MUS_P2C03_F | Gandhamādana storm | FLOW | storm cue, Ghaṭotkaca's drums | 2:00 |
| MUS_P2C03_G | The saugandhika lotus | FLOW | delicate wonder | 1:00 |
| MUS_P2C03_H | Hanumān's tail | FLOW | THM_BHIMA comic swagger draining into awe | 2:30 |
| MUS_P2C03_I | Hanumān's form | FLOW | THM_KALA swell, then tender | 1:00 |
| MUS_P2C03_J | Kubera's lake, Jaṭāsura | FLOW | short brutal action | 2:00 |
| MUS_P2C04_A | Arjuna returns | FLOW | THM_ARJUNA radiant | 1:30 |
| MUS_P2C04_B | Nivātakavacas / Hiraṇyapura | FLOW | underwater and sky battle cue | 2:30 |
| MUS_P2C04_C | The python | FLOW | coiling suspense | 1:30 |
| MUS_P2C04_D | Ghoṣayātrā plan | FLOW | THM_SHAKUNI with THM_DURYODHANA | 1:00 |
| MUS_P2C04_E | Gandharva battle | FLOW | elegant silver action | 2:00 |
| MUS_P2C04_F | Arjuna vs Citrasena — "Guru!" | FLOW | duel cue breaking into laughter | 1:00 |
| MUS_P2C04_G | Duryodhana's fast, the underworld | FLOW | dark THM_FRAME variation, red-fire cavern | 2:00 |
| MUS_P2C04_H | Vaiṣṇava sacrifice | FLOW | ritual drums, golden plough | 0:40 |
| MUS_P2C04_I | Jayadratha's abduction and chase | FLOW | chase cue, galloping drums | 2:30 |
| MUS_P2C04_J | Five tufts, Śiva's boon | FLOW | humiliation sting then THM_KALA seed | 1:30 |
| MUS_P2C05_A | Sūrya's warning | FLOW | THM_KARNA in a dream key | 1:30 |
| MUS_P2C05_B | Cutting the armour | SIL | NO MUSIC during the cut — breath, blade, river | 0:00 |
| MUS_P2C05_C | Vaikartana | FLOW | THM_KARNA after the cut, brass rising like the sun | 1:30 |
| MUS_P2C05_D | The deer and the thirst | FLOW | chase into exhaustion | 1:00 |
| MUS_P2C05_E | The still lake | FLOW | horror drones, no melody | 2:30 |
| MUS_P2C05_F | The questions | FLOW | sparse tanpura under question and answer | 1:30 |
| MUS_P2C05_G | Dharma revealed | FLOW | THM_DHARMA blossoming | 1:00 |
| MUS_P2C05_H | The śamī tree | FLOW | dark cremation-ground cue | 1:00 |
| MUS_P2C05_I | Disguises | FLOW | playful-tense montage | 1:30 |
| MUS_P2C06_A | Kīcaka's desire | FLOW | heavy sensual threat | 1:00 |
| MUS_P2C06_B | The kick in court | SIL | NO MUSIC | 0:00 |
| MUS_P2C06_C | The kitchen at night | FLOW | THM_DRAUPADI sarangi, intimate | 2:00 |
| MUS_P2C06_D | The dance hall | SIL | NO MUSIC — only bodies | 0:00 |
| MUS_P2C06_E | 105 Upakīcakas | FLOW | explosive action | 1:30 |
| MUS_P2C06_F | "Yah Bhīma hai" | FLOW | THM_DURYODHANA sting | 0:40 |
| MUS_P2C06_G | Uttara boasts | FLOW | comic cue | 1:00 |
| MUS_P2C06_H | The śamī reveal | FLOW | THM_ARJUNA, ten names like hammer-blows | 2:00 |
| MUS_P2C06_I | One chariot against six | FLOW | THM_WAR with THM_ARJUNA on top | 3:00 |
| MUS_P2C06_J | Sammohana and the cloths | FLOW | eerie-comic hush | 1:30 |
| MUS_P2C06_K | Five men on the thrones | FLOW | THM_MAIN short statement | 1:00 |
| MUS_P2C07_A | Wedding at Upaplavya | FLOW | joyous wedding song with wordless women's chorus, shehnai, drums | 2:00 |
| MUS_P2C07_B | Kṛṣṇa's choice | FLOW | THM_KRISHNA, a small smile in music | 1:30 |
| MUS_P2C07_C | Śalya trapped | FLOW | ironic feast cue | 1:00 |
| MUS_P2C07_D | Five villages | FLOW | THM_DHARMA plea | 1:30 |
| MUS_P2C07_E | A sleepless king | FLOW | night counsel, lamp-light strings | 1:30 |
| MUS_P2C07_F | The needle's point | FLOW | one cold sting | 0:20 |
| MUS_P2C07_G | Draupadī's hair | FLOW | THM_DRAUPADI, cut to silence as the chariot leaves | 2:00 |
| MUS_P2C07_H | Hastinapura welcomes Kṛṣṇa | FLOW | festive city cue | 1:30 |
| MUS_P2C07_I | The embassy | FLOW | minimal; low strings under the speech | 2:00 |
| MUS_P2C07_J | The plot and the cosmic form | FLOW | THM_KALA full with roaring choir | 2:30 |
| MUS_P2C08_A | Kṛṣṇa and Karṇa in the chariot | FLOW | THM_KRISHNA and THM_KARNA in dialogue | 3:00 |
| MUS_P2C08_B | The sacrifice of weapons | FLOW | THM_KALA ritual pulse | 1:00 |
| MUS_P2C08_C | Omens | FLOW | celestial dread | 1:00 |
| MUS_P2C08_D | Kuntī and Karṇa | FLOW | THM_KUNTI into the full THM_KARNA for the first time, collapsing into one bansuri | 3:00 |
| MUS_P2C08_E | Commanders | FLOW | mobilisation montage | 1:30 |
| MUS_P2C08_F | Ulūka | FLOW | mocking sting | 0:40 |
| MUS_P2C08_G | Ambā | FLOW | dark tragic inlay cue, fire at the end | 2:00 |
| MUS_P2C08_H | Rāma vs Bhīṣma, 23 days | FLOW | THM_WAR ancient variant | 1:00 |
| MUS_P2C08_I | Day One — the conches | FLOW | THM_MAIN building to the conches | 2:00 |
| MUS_P2C08_J | Gāṇḍīva falls | FLOW | one sting, then silence | 0:30 |
| MUS_P2C08_Z | End credits — Part II | FLOW | THM_KARNA and THM_DRAUPADI suite | 3:00 |
| MUS_P3C01_A | Sañjaya's report | FLOW | THM_KALA quiet, a blind king's darkness | 1:30 |
| MUS_P3C01_B | Vyāsa's gift | FLOW | short mystical cue | 0:40 |
| MUS_P3C01_C | Arjuna's despair | FLOW | THM_ARJUNA broken, strings sagging | 1:30 |
| MUS_P3C01_D | The teaching | FLOW | THM_KRISHNA long-form, minimal and luminous | 3:00 |
| MUS_P3C01_E | The form of Time | FLOW | THM_KALA at full scale, orchestra and choir | 2:00 |
| MUS_P3C01_F | "Kālo'smi" choral | ELM | massive male choir chanting the Sanskrit line "kālo 'smi lokakṣayakṛt pravṛddhaḥ" in slow syllables over sub-bass | 0:40 |
| MUS_P3C01_G | "Naṣṭo mohaḥ" — Gāṇḍīva lifted | FLOW | THM_MAIN rising | 1:00 |
| MUS_P3C01_H | Yudhiṣṭhira's barefoot walk | FLOW | THM_DHARMA | 2:30 |
| MUS_P3C01_I | Yuyutsu crosses | FLOW | single brave phrase | 0:40 |
| MUS_P3C02_A | Day 1 — the collision | FLOW | THM_WAR full | 2:30 |
| MUS_P3C02_B | Uttara and Śveta fall | FLOW | short elegy | 1:00 |
| MUS_P3C02_C | Day 2 — Bhīma and the Kaliṅgas | FLOW | THM_BHIMA as battle percussion | 2:00 |
| MUS_P3C02_D | Day 3 — the discus | FLOW | THM_KRISHNA furious, then THM_BHISHMA opening its arms | 2:00 |
| MUS_P3C02_E | Days 4–8 | FLOW | THM_WAR variations montage | 3:00 |
| MUS_P3C02_F | Irāvat | FLOW | young elegy | 1:00 |
| MUS_P3C02_G | Day 9 — the whip | FLOW | THM_WAR breaking into THM_KRISHNA | 1:00 |
| MUS_P3C02_H | Night 9 — "How do we kill you?" | FLOW | THM_BHISHMA intimate, single lamp | 2:30 |
| MUS_P3C03_A | Day 10 — Śikhaṇḍin in front | FLOW | THM_WAR slowing into THM_BHISHMA | 3:00 |
| MUS_P3C03_B | "Ye Śikhaṇḍī ke bāṇ nahīṁ" | FLOW | refrain-like build under the three lines | 1:30 |
| MUS_P3C03_C | The fall | FLOW | silence, one conch, then THM_GANGA under the wind | 1:30 |
| MUS_P3C03_D | Pillow and water | FLOW | THM_BHISHMA tender | 2:00 |
| MUS_P3C03_E | Karṇa at the arrow-bed | FLOW | THM_KARNA with THM_BHISHMA | 2:30 |
| MUS_P3C03_F | Droṇa's vow | FLOW | martial cue | 1:00 |
| MUS_P3C03_G | Saṁśaptaka death-oath | FLOW | ritual fire drums | 1:00 |
| MUS_P3C03_H | Bhagadatta and Supratīka | FLOW | colossal elephant action | 2:30 |
| MUS_P3C03_I | Vaijayantī | FLOW | THM_KRISHNA sudden softness | 0:40 |
| MUS_P3C04_A | The cakravyūha forms | FLOW | THM_ABHIMANYU with turning-wheel percussion | 1:30 |
| MUS_P3C04_B | The breach | FLOW | THM_ABHIMANYU full | 2:00 |
| MUS_P3C04_C | Inside the wheel | FLOW | THM_WAR with THM_ABHIMANYU fighting through it | 3:00 |
| MUS_P3C04_D | Wheel and mace | FLOW | THM_ABHIMANYU breaking apart | 1:30 |
| MUS_P3C04_E | After the boy | FLOW | four seconds of silence, one bird, then a strings elegy | 1:30 |
| MUS_P3C04_F | Arjuna's vow | FLOW | THM_ARJUNA turned dark, conches | 2:00 |
| MUS_P3C04_G | Dream of the white mountain | FLOW | dream cue, distant choir | 1:30 |
| MUS_P3C04_H | Day 14 — the charge | FLOW | THM_WAR driving | 2:30 |
| MUS_P3C04_I | Horses bathed mid-battle | FLOW | calm island in chaos | 1:00 |
| MUS_P3C04_J | Sātyaki and Bhūriśravas | FLOW | tension and shame | 1:30 |
| MUS_P3C04_K | Sunset — the flying head | FLOW | THM_KALA with THM_ARJUNA, racing the sun | 2:30 |
| MUS_P3C05_A | The night battle | FLOW | THM_WAR in darkness, torches | 2:30 |
| MUS_P3C05_B | Ghaṭotkaca's terror | FLOW | rākṣasa drums and roars | 2:00 |
| MUS_P3C05_C | The Śakti, the giant's fall | FLOW | meteor rise then crushing fall | 1:30 |
| MUS_P3C05_D | Kṛṣṇa dances | FLOW | strange joyous music turning dissonant | 1:00 |
| MUS_P3C05_E | Drupada and Virāṭa fall | FLOW | elegy | 1:00 |
| MUS_P3C05_F | The half-truth | FLOW | sub-drone under the lie | 1:30 |
| MUS_P3C05_G | Droṇa in yoga | FLOW | THM_KALA, the head taken | 1:30 |
| MUS_P3C05_H | Nārāyaṇa weapon | FLOW | fire-choir onslaught | 2:00 |
| MUS_P3C06_A | Karṇa commander, Śalya's condition | FLOW | THM_KARNA martial | 1:30 |
| MUS_P3C06_B | The ride and the two curses | FLOW | THM_KARNA memory, Paraśurāma motif | 2:00 |
| MUS_P3C06_C | Brothers' quarrel | FLOW | THM_DHARMA under strain | 2:00 |
| MUS_P3C06_D | Duḥśāsana | FLOW | horror drums | 1:30 |
| MUS_P3C06_E | The field clears | FLOW | THM_MAIN suspended | 1:00 |
| MUS_P3C06_F | Karṇa vs Arjuna | FLOW | THM_WAR with THM_KARNA and THM_ARJUNA interlocked | 4:00 |
| MUS_P3C06_G | The serpent arrow | FLOW | hiss-like strings, sub-boom | 0:40 |
| MUS_P3C06_H | "Tab dharma kahāṁ gayā thā?" | FLOW | drums only, each question a hit | 1:30 |
| MUS_P3C06_I | The añjalika | FLOW | THM_KARNA bansuri alone, then silence | 1:30 |
| MUS_P3C06_J | Kuntī knows | FLOW | one drone note | 0:40 |
| MUS_P3C07_A | Śalya and Śakuni fall | FLOW | THM_WAR | 1:30 |
| MUS_P3C07_B | The lake | FLOW | suspense on water | 1:30 |
| MUS_P3C07_C | The mace duel | FLOW | THM_BHIMA against THM_DURYODHANA | 3:00 |
| MUS_P3C07_D | Balarāma's fury | FLOW | angry brass | 1:00 |
| MUS_P3C07_E | "Mujhse achchhā ant kiska?" | FLOW | THM_DURYODHANA as a noble requiem, heavenly voices | 2:00 |
| MUS_P3C07_F | The chariot burns | FLOW | THM_KALA | 1:00 |
| MUS_P3C07_G | Aśvatthāman anointed | FLOW | dark low cue | 0:40 |
| MUS_P3C07_H | The owl, the gate, the massacre | SIL | NO MUSIC — breath, cloth, bodies | 0:00 |
| MUS_P3C07_I | Śiva at the gate | FLOW | THM_KALA | 1:00 |
| MUS_P3C07_J | Draupadī's fast | FLOW | THM_DRAUPADI | 1:00 |
| MUS_P3C07_K | Brahmaśiras over the Gaṅgā | FLOW | THM_KALA with choir, two suns | 2:00 |
| MUS_P3C07_L | The curse | FLOW | judgement cue | 1:00 |
| MUS_P3C08_A | The iron Bhīma | FLOW | short dread cue | 0:40 |
| MUS_P3C08_B | Field of women | FLOW | wordless female choir lament | 3:00 |
| MUS_P3C08_C | "Karṇa ko bhī jal do" | FLOW | THM_KUNTI into THM_KARNA | 1:30 |
| MUS_P3C08_D | Coronation, Cārvāka | FLOW | hollow regal cue | 1:00 |
| MUS_P3C08_E | Teachings on the arrow-bed | FLOW | THM_DHARMA through seasons | 2:30 |
| MUS_P3C08_F | The 58th night | FLOW | THM_BHISHMA final statement into THM_GANGA | 2:30 |
| MUS_P3C08_G | The mongoose | FLOW | parable cue | 1:30 |
| MUS_P3C08_H | Elders to the forest, Vidura | FLOW | THM_VAN | 1:30 |
| MUS_P3C08_I | Night of the dead | FLOW | THM_MAIN on a single soft bansuri | 3:00 |
| MUS_P3C08_J | Forest fire | FLOW | calm acceptance cue | 0:40 |
| MUS_P3C08_K | Mausala | FLOW | drunken revelry into chaos | 2:00 |
| MUS_P3C08_L | Kṛṣṇa's foot | FLOW | THM_KRISHNA final, almost silent | 2:00 |
| MUS_P3C08_M | Dvārakā sinks, the robbers | FLOW | loss cue | 1:30 |
| MUS_P3C08_N | Mahāprasthāna | FLOW | THM_VAN with THM_DHARMA, wind | 2:30 |
| MUS_P3C08_O | Heaven and hell | FLOW | THM_KALA | 2:00 |
| MUS_P3C08_P | "Ūrdhvabāhur virauṁy eṣa" | ELM | ancient solo male chant of the Sanskrit verse over a low drone, then a vast choir echo | 1:00 |
| MUS_P3C08_Z | End credits — the trilogy | FLOW | THM_MAIN grand suite with every leitmotif, ending on the soft chorus syllables | 4:00 |

---
## 3. SOUND EFFECTS LIBRARY (ElevenLabs SFX v2 — max 30 s; LOOP = seamless-loop option)
| SFX | Sound | TOOL | PROMPT (ElevenLabs SFX v2) | LEN |
|---|---|---|---|---|
| SFX_BREATH_GIANT | Enormous slow inhale (cold open) | EL | one enormous slow human inhale, extremely close, as if inside the listener's skull, dry room | 4s |
| SFX_CONCH_BHISHMA | Bhīṣma's conch | EL | a lion-like human roar followed by one huge seashell conch blast, long sustain, four-second valley echo across a plain | 9s |
| SFX_CONCH_PANCAJANYA | Pāñcajanya (Kṛṣṇa) | EL | deep round unhurried seashell conch blast with a warm low fundamental, outdoor plain | 6s |
| SFX_CONCH_DEVADATTA | Devadatta (Arjuna) | EL | bright piercing seashell conch blast like a falcon's cry, outdoor | 6s |
| SFX_CONCH_PAUNDRA | Pauṇḍra (Bhīma) | EL | gigantic booming seashell conch with chest-shaking low end | 7s |
| SFX_CONCH_ANANTAVIJAYA | Anantavijaya (Yudhiṣṭhira) | EL | a steady sorrowful seashell conch note | 6s |
| SFX_CONCH_TWINS | Sughoṣa + Maṇipuṣpaka | EL | two seashell conches sounding together in harmony, sweet and bright | 6s |
| SFX_CONCH_TUMULT_KURU | Kaurava tumult | EL | thousands of conches, kettledrums, cymbals and cow-horns erupting at once across a vast plain | 12s |
| SFX_CONCH_TUMULT_PANDAVA | Pāṇḍava answer | EL | massed conches answering in a rolling wave across a plain, ground rumble | 12s |
| SFX_CONCH_FAR | One far conch | EL | a single seashell conch heard very far away across a valley, faint | 6s |
| SFX_GANDIVA_TWANG | Gāṇḍīva twang (signature) | EL | deep metallic bell-like twang of a giant bowstring being strung, rolling echo, heart-lurching | 4s |
| SFX_BOW_DRAW | Bow draw creak | EL | heavy composite bow drawn to full, wood and horn creaking, leather grip | 3s |
| SFX_BOW_RELEASE | Bowstring release | EL | bowstring released with a sharp thrum | 1s |
| SFX_ARROW_WHISTLE | Arrow flyby | EL | single arrow whistling past close, left to right | 2s |
| SFX_ARROW_VOLLEY | Thousand arrows | EL | thousands of arrows released at once, a rushing hiss overhead | 6s |
| SFX_ARROW_RAZOR | Razor-head arrow | EL | a heavy razor-headed arrow, deep whoosh and a chop into wood | 2s |
| SFX_ARROW_FIRE | Flaming arrow | EL | a flaming arrow in slow motion, fire flutter and whoosh | 3s |
| SFX_ARROW_SERPENT | Serpent arrow | EL | an arrow flying with a living hiss inside it, rising scream | 3s |
| SFX_ARROW_ANJALIKA | Añjalika — the last arrow | EL | a single great arrow released with a deep low tone that rises to a blade-like ring | 3s |
| SFX_ARROW_HIT_FLESH | Arrow into body | EL | arrow striking flesh and armour padding, dull thud | 1s |
| SFX_ARROW_HIT_BRONZE | Arrow on bronze | EL | iron arrowhead sparking off a hammered bronze shield | 1s |
| SFX_ARROW_DAM | Arrows into riverbed | EL | rhythmic thock thock thock of arrows driving into wet riverbed and wood | 8s LOOP |
| SFX_ARROW_ROOF_RAIN | Rain on the arrow-roof | EL | torrential rain hitting a canopy of thousands of arrows over a fire, hissing into steam | 10s LOOP |
| SFX_QUIVER_EMPTY | Empty quiver | EL | a hand reaching into an empty leather quiver, hollow scrape | 2s |
| SFX_DISCUS_ZING | Discus | EL | a spinning razor-edged iron discus whirring past then a metallic zing and a cut | 3s |
| SFX_MACE_SWING | Mace swing | EL | heavy iron mace swung, deep whoosh | 1s |
| SFX_MACE_CLASH | Mace on mace | EL | two iron maces colliding with a heavy ringing clang and sparks | 2s |
| SFX_MACE_BONE | Mace on bone | EL | an iron mace smashing into a thigh, heavy wet crack | 2s |
| SFX_SWORD_DRAW | Sword draw | EL | iron sword drawn from a leather scabbard | 1s |
| SFX_SWORD_CLASH | Sword clash | EL | iron swords clashing twice | 2s |
| SFX_SWORD_SHATTER | Sword shatters on a skull | EL | an iron sword shattering against something harder than stone, ringing fragments | 2s |
| SFX_SPEAR_THROW | Spear | EL | a heavy spear thrown, whoosh and impact into armour | 2s |
| SFX_SHIELD_BLOCK | Shield | EL | hide-and-bronze shield blocking a blow | 1s |
| SFX_CHARIOT_ROLL | Chariot rolling | EL | a wooden spoked-wheel war chariot rolling fast over packed earth, axle creak, hoof beats | 15s LOOP |
| SFX_CHARIOT_CRASH | Head-on chariots | EL | two wooden war chariots colliding head-on, timber exploding into splinters, horses screaming | 4s |
| SFX_WHEEL_ROLL_AWAY | Loose wheel | EL | a broken spoked wheel rolling away across mud and falling | 3s |
| SFX_WHEEL_SINK | Wheel swallowed by earth | EL | a chariot wheel grinding and sinking into soft earth, sucking mud | 4s |
| SFX_CHARIOT_BURN | Chariot bursts into flame | EL | a wooden chariot suddenly igniting with a roar and collapsing into ash | 6s |
| SFX_WHIP_CRACK | Whip | EL | leather chariot whip cracking | 1s |
| SFX_HORSE_NEIGH | Horse neigh | EL | war horse neighing, snorting | 2s |
| SFX_HORSE_SCREAM | Horse scream | EL | horse screaming in panic | 2s |
| SFX_HORSES_BLOW | Horses breathing | EL | several horses blowing through their nostrils in cold morning air | 8s LOOP |
| SFX_ELEPHANT_TRUMPET | Elephant trumpet | EL | war elephant trumpeting close, the ground shaking | 3s |
| SFX_ELEPHANT_FALL | Colossal elephant falls | EL | a colossal elephant collapsing, earth-shaking thud, armour clatter | 4s |
| SFX_LEATHER_ARMY | A million straps | EL | the creak of countless leather straps and armour plates of a waiting army, wind | 20s LOOP |
| SFX_ARMOUR_FOLEY | Armour movement | EL | bronze-scale armour and leather moving with a walking warrior | 6s LOOP |
| SFX_DICE_CLACK | The dice (signature) | EL | dice thrown onto a wooden board, a single sharp clack like a gunshot in a silent hall, short reverb | 2s |
| SFX_DICE_RATTLE | Dice in a palm | EL | dice rattled softly in a cupped hand | 2s |
| SFX_CLOTH_DRAG | Endless cloth | EL | coarse hand-loomed cotton being pulled continuously off a body, long dragging rasp, a man's breathing | 20s LOOP |
| SFX_CLOTH_PILE | Mountain of cloth | EL | heavy cloth falling and piling softly on a wooden floor | 4s |
| SFX_BHERI | Funeral bheri | EL | one deep bheri drum hit, dry, long decay | 3s |
| SFX_KNOT_TIGHTEN | The blindfold knot | EL | a folded cloth band pulled tight into a knot, close | 1s |
| SFX_PRESSURE_BOOM | Air-pressure drop | EL | low 38 Hz pressure boom from above, flames leaning, reeds flattening in a downdraft | 4s |
| SFX_FLOWER_FALL | Flower-rain | EL | soft rain of petals falling on cloth and water, very gentle | 10s LOOP |
| SFX_SKY_VOICE_BED | Sky-voice bed | EL | airy layered whispers of many voices like wind high above | 10s LOOP |
| SFX_DIVINE_DRUMS | Divine drums | EL | distant celestial kettledrums rolling across the sky | 6s |
| SFX_SUN_BLAZE | Sun intensifies | EL | rising roar of heat and light, crackling air, shimmering hiss crescendo | 6s |
| SFX_EARTH_TREMOR | Earthquake | EL | deep rumbling earth tremor, dust and pebbles shaking | 5s |
| SFX_THUNDER_CLEAR | Thunder, clear sky | EL | dry thunderclap in a cloudless sky, no rain | 4s |
| SFX_ECLIPSE_HUSH | Eclipse hush | EL | birds suddenly silent, wind drops, a low hum as light fades | 8s |
| SFX_METEOR | Meteor | EL | a meteor streaking low overhead, tearing whoosh | 4s |
| SFX_VISHVARUPA | Cosmic form | EL | roaring flames bursting from a standing figure, rushing wind, a deep choir-like drone | 8s |
| SFX_KALA_MAW | The maw of Time | EL | immense low cosmic roar, grinding like mountains, distant screams sucked inward | 10s |
| SFX_NARAYANA_ASTRA | Nārāyaṇa weapon | EL | sky filling with thousands of hissing fire-darts, roaring descent | 10s |
| SFX_BRAHMASHIRAS | Brahmaśiras | EL | two colossal fire-roars rising over a river like two suns, air tearing | 10s |
| SFX_SAMMOHANA | Sound-weapon | EL | a deep throbbing hypnotic tone that swells until bodies collapse, weapons dropping | 8s |
| SFX_SHAKTI | Indra's Śakti | EL | a spear leaving a hand like a meteor, rising scream then impact | 4s |
| SFX_VAIJAYANTI | Weapon becomes garland | EL | a roaring weapon impact that softens instantly into a whisper of flowers | 3s |
| SFX_BRAHMIN_HUM | Brahmins' hum | EL | hundreds of men humming one furious low note, then a burst of fire | 6s |
| SFX_RIVER_GANGA | Gaṅgā | EL | broad river flowing over stones, gentle wash | 30s LOOP |
| SFX_RIVER_STOP | River goes silent | EL | river sound sucked into total silence for one second | 2s |
| SFX_SPLASH_INFANT | The seven splashes | EL | a small body-weight splash into a river, ripple | 2s |
| SFX_DAM_BURST | Arrow-dam bursts | EL | a lattice of wood cracking and a river bursting through with a roar | 6s |
| SFX_UNDERWATER_HEART | Underwater heartbeat | EL | muffled underwater, slowing heartbeat, bubbles | 10s LOOP |
| SFX_VINES_SNAP | Vines snapping | EL | wet vines snapping one by one underwater | 3s |
| SFX_POOL_SPLASH | Duryodhana falls in | EL | a man falling fully clothed into an indoor pool, big splash, echo | 3s |
| SFX_LAC_IGNITE | Lac house ignites | EL | resin, ghee and lac igniting with a huge whoomph and roaring spread | 6s |
| SFX_FIRE_INFERNO | Inferno | EL | a timber building fully on fire, roaring, crackling, beams falling | 30s LOOP |
| SFX_FOREST_FIRE | Khāṇḍava | EL | an entire forest burning with a howling roar, animals far within | 30s LOOP |
| SFX_LAKE_BOIL | Lakes boiling | EL | a lake boiling, bubbling and hissing | 8s LOOP |
| SFX_SACRIFICE_FIRE | Sacrificial fire | EL | a great sacrificial fire roaring, ghee spitting, crackling | 30s LOOP |
| SFX_TORCH | Torch | EL | burning torch flutter | 10s LOOP |
| SFX_LAMP_GUTTER | Lamp goes out | EL | an oil lamp flame guttering and dying | 2s |
| SFX_SNAKES_SCREAM | Serpents into the fire | EL | a terrible chorus of hissing turning to shrieks, things falling into fire | 10s |
| SFX_COBRA | Cobra | EL | a cobra hissing and striking | 2s |
| SFX_PYTHON | Python | EL | a giant serpent's heavy breathing hiss and scales grinding on rock | 6s |
| SFX_CROCODILE | Crocodile | EL | a crocodile lunging from shallow water, jaws snapping | 2s |
| SFX_TIGER | Tiger | EL | a tiger's low growl at a cave mouth | 3s |
| SFX_JACKAL | Jackal | EL | a jackal howling at night, answered by others | 5s |
| SFX_DONKEY | Donkeys | EL | many donkeys braying from all sides | 4s |
| SFX_CROWS_VULTURES | Carrion birds | EL | crows and vultures screaming over a battlefield | 10s LOOP |
| SFX_OWL_ATTACK | The owl | EL | an owl's silent wing-beat then crows waking in panic and dying | 6s |
| SFX_DOG_ARROWS | The dog | EL | a dog's whimper muffled by something filling its mouth, running back | 3s |
| SFX_CHICKS | Four chicks | EL | four tiny chicks chirping in a burning forest | 6s |
| SFX_BOAR | Giant boar | EL | a huge boar charging through snowmelt, squeal | 3s |
| SFX_CRANE | The crane | EL | a crane's single harsh cry over still water | 2s |
| SFX_TAIL_THUMP | Hanumān's tail | EL | a huge tail slapping the ground like thunder, echo in mountains | 3s |
| SFX_RAKSHASA_ROAR | Rākṣasa roar | EL | a giant man-eater's roar in a forest, trees shaking | 3s |
| SFX_BONE_CRACK | Bones breaking | EL | a heavy body being broken, deep bone crack | 2s |
| SFX_BACK_BREAK | Back broken over a knee | EL | a spine snapping over a knee, a final exhale | 2s |
| SFX_CROWD_ROAR | Arena roar | EL | thousands of people roaring in a timber arena | 8s LOOP |
| SFX_CROWD_GASP | Crowd gasp | EL | a huge crowd gasping at once then silence | 3s |
| SFX_HAHAKARA | Cry of horror | EL | a crowd crying out in horror and shouting | 4s |
| SFX_ARMY_SHOUT | Army war-cry | EL | an army roaring a war-cry | 4s |
| SFX_WOMEN_WAIL | Women wailing | EL | many women wailing in grief, distant and near | 15s LOOP |
| SFX_HEARTBEAT | Heartbeat | EL | slow human heartbeat, close | 10s LOOP |
| SFX_THIGH_SLAP | Thigh slap | EL | a palm slapping a thigh hard | 1s |
| SFX_KNIFE_CUT | Ekalavya's knife | EL | a quick iron knife cut, restrained, no gore | 1s |
| SFX_ARMOUR_PEEL | Karṇa cuts his armour | EL | a blade slowly sliding under living metal skin, wet, restrained, water around | 6s |
| SFX_TIMBER_GROAN | Structure groans | EL | timber lattice groaning under pressure | 3s |
| SFX_HOOVES_GROUND | Chariot touches the earth | EL | a sound like a bone breaking under the earth, then hooves hitting ground | 3s |
| SFX_AMB_KURU_DAWN | Kurukṣetra waiting | EL | endless plain at pre-dawn, wind, distant horses, armour creak of a huge army | 30s LOOP |
| SFX_AMB_BATTLE_NEAR | Battle — close | EL | close battle: clashing bronze, screams, hooves, chariots | 30s LOOP |
| SFX_AMB_BATTLE_FAR | Battle — distant | EL | a huge battle heard from far away, rumble | 30s LOOP |
| SFX_AMB_NIGHT_BATTLE | Night battle | EL | battle at night with torches crackling, elephants, shouting | 30s LOOP |
| SFX_AMB_PALACE_DAY | Palace day | EL | Iron-Age palace by day, distant voices, birds, wind through timber | 30s LOOP |
| SFX_AMB_PALACE_NIGHT | Palace night | EL | quiet palace at night, crickets, a lamp's faint hiss | 30s LOOP |
| SFX_AMB_COURT | Packed assembly | EL | a packed assembly hall murmuring, shuffling | 30s LOOP |
| SFX_AMB_FOREST_DAY | Forest day | EL | Indian forest by day, birds, insects, leaves | 30s LOOP |
| SFX_AMB_FOREST_NIGHT | Forest night | EL | Indian forest at night, insects, owls, distant animals | 30s LOOP |
| SFX_AMB_RAIN_FOREST | Monsoon forest | EL | heavy rain on a forest canopy, dripping | 30s LOOP |
| SFX_AMB_HIMALAYA | High mountains | EL | high Himalayan wind, snow hiss, vast silence | 30s LOOP |
| SFX_AMB_SEA | Sea shore | EL | ocean waves on a wide shore, wind in reeds | 30s LOOP |
| SFX_AMB_CITY | City street | EL | Iron-Age town street, voices, carts, animals, no modern sounds | 30s LOOP |
| SFX_AMB_FISHER | Fisher village | EL | river village at night, nets creaking, water lapping, fire | 30s LOOP |
| SFX_AMB_SATTRA | Snake-sacrifice pavilion | EL | great fire roaring, many priests murmuring, hissing far off | 30s LOOP |
| SFX_AMB_STORM | Storm | EL | violent wind and rain storm | 30s LOOP |
| SFX_AMB_KITCHEN | Royal kitchen | EL | big kitchen, fires, pots, ladles | 30s LOOP |
| SFX_AMB_UNDERWATER | Underwater | EL | deep underwater ambience | 30s LOOP |
| SFX_AMB_HEAVEN | Heaven | EL | high, soft, airy ambience with faint distant music | 30s LOOP |
| SFX_AMB_HELL | Hell road | EL | low groans, boiling liquid, flies, wind in razor leaves | 30s LOOP |
| SFX_AMB_CAMP_NIGHT | Army camp night | EL | army camp at night, fires, horses, low voices | 30s LOOP |
| SFX_AMB_LAKE_STILL | Dead-still lake | EL | unnatural silence by a lake, a faint wind, no birds | 30s LOOP |
| SFX_AMB_CREMATION | Cremation ground | EL | cremation ground at dusk, pyre crackle, jackals far off | 30s LOOP |
| SFX_AMB_STRI_FIELD | Field of the dead | EL | wind over a battlefield of the dead, crows, distant wailing | 30s LOOP |
| SFX_AMB_ROOM_TONE | Silent hall | EL | room tone of a large timber hall with hundreds of people holding their breath | 30s LOOP |

---
## 4. VOICE CASTING — locked voices (ElevenLabs Voice Design → save as "VOX_xx Name")
**Sab voices ke liye common:** native Hindi speaker, clear Sanskritised Hindi (शुद्ध), North-Indian accent, no English accent, no radio-announcer gloss. Model **Eleven v4** (Hindi test pass hone par), warna **Eleven v3**. Default settings: stability **Natural**, similarity **0.85–0.90**, style **0.25**, speaker boost **on**. Narrators: stability **Robust**. Emotional peaks: **Creative**. Umar ke variants (`A`/`K`/`Y`/`B`) = base voice ka **Voice Remix (age)**, nayi voice NAHI.
| VOX | Who | Voice design (ElevenLabs prompt) | Settings |
|---|---|---|---|
| VOX_00 | Vaiśaṁpāyana (narrator) | man in his late fifties, gravelly warm storyteller baritone, intimate, unhurried, like a voice by a fire | Robust · sim 0.9 · style 0.2 |
| VOX_01A | Devavrata (36–40) | man of 38, granite-firm resonant baritone, controlled power, few words, no tremor | Natural · 0.9 · 0.2 |
| VOX_01 | Bhīṣma (60+) | very old man, deep slow dignified bass-baritone with a slight rasp, absolute authority, rarely raised | Natural · 0.9 · 0.2 |
| VOX_02A | Dhṛtarāṣṭra (young) | man of 30, heavy deep voice, a little petulant | Natural · 0.85 · 0.25 |
| VOX_02 | Dhṛtarāṣṭra | old heavy bass trembling with need and fear, listening pauses of a blind man | Natural · 0.85 · 0.3 |
| VOX_03 | Vidura | razor-sharp calm mid-baritone, crystalline diction, warm | Natural · 0.9 · 0.2 |
| VOX_04A | Kuntī (15) | girl of fifteen, soft, curious, frightened | Natural · 0.85 · 0.3 |
| VOX_04 | Kuntī | woman 35–70, soft-spoken alto with steel underneath, restrained grief | Natural · 0.9 · 0.3 |
| VOX_05K | Yudhiṣṭhira (boy) | serious gentle boy of fourteen | Natural · 0.85 · 0.2 |
| VOX_05 | Yudhiṣṭhira | mild warm baritone, measured and truthful, can turn flat and stone-cold | Natural · 0.9 · 0.2 |
| VOX_05B | Yudhiṣṭhira (old) | very old man, quiet, serene | Natural · 0.9 · 0.2 |
| VOX_06K | Bhīma (boy) | boy of twelve with a huge chesty voice, laughing | Natural · 0.85 · 0.35 |
| VOX_06 | Bhīma | giant man, booming chesty bass, laughs loudly, roars in rage | Creative · 0.85 · 0.4 |
| VOX_07K | Arjuna (boy) | bright eager boy of twelve | Natural · 0.85 · 0.25 |
| VOX_07Y | Arjuna (16–19) | proud youth, clear light baritone, hurt easily | Natural · 0.85 · 0.3 |
| VOX_07 | Arjuna | focused baritone, quiet intensity, can break | Natural · 0.9 · 0.3 |
| VOX_07B | Arjuna (85) | old man of eighty-five, tired, gentle | Natural · 0.9 · 0.2 |
| VOX_08N | Nakula | smooth aristocratic tenor, warm | Natural · 0.85 · 0.3 |
| VOX_08S | Sahadeva | sharp intense tenor, clipped, can hiss | Natural · 0.85 · 0.35 |
| VOX_09 | Karṇa | deep resonant baritone like distant thunder, proud and wounded, slows when hurt | Natural · 0.9 · 0.3 |
| VOX_10K | Duryodhana (boy) | sullen intense boy of twelve | Natural · 0.85 · 0.3 |
| VOX_10 | Duryodhana | rich commanding baritone, mocking laugh, aristocratic menace, never shrill | Natural · 0.9 · 0.35 |
| VOX_11 | Śakuni | silky ice-cold tenor, soft, amused, every word deliberate | Natural · 0.9 · 0.3 |
| VOX_12 | Draupadī | low clear mezzo, razor-sharp royal fire, dignity that breaks but never bends | Natural · 0.9 · 0.35 |
| VOX_13 | Kṛṣṇa | warm velvety baritone with a smile in it, playful, then bottomlessly still | Natural · 0.9 · 0.3 |
| VOX_13B | Kṛṣṇa (85) | the same voice aged to eighty-five, quieter, breathier | Natural · 0.9 · 0.2 |
| VOX_14 | Droṇa | dry steel-edged elder baritone, military precision | Natural · 0.9 · 0.25 |
| VOX_15E | Ekalavya | pure serene youthful tenor | Natural · 0.85 · 0.3 |
| VOX_15V | Vikarṇa | young baritone trembling with courage | Natural · 0.85 · 0.35 |
| VOX_16 | Duḥśāsana | coarse wet raspy voice, manic laughter | Creative · 0.8 · 0.5 |
| VOX_17A | Gāndhārī (16) | girl of sixteen, low and quiet, decisive | Natural · 0.85 · 0.2 |
| VOX_17 | Gāndhārī | low controlled contralto, never shrill, terrifying calm | Natural · 0.9 · 0.25 |
| VOX_18 | Vyāsa | dry ancient unhurried bass, like a mountain speaking | Robust · 0.9 · 0.15 |
| VOX_19 | Janamejaya | young intense baritone, raw grief and anger | Natural · 0.85 · 0.35 |
| VOX_20 | Sañjaya (Part III narrator) | clear reportorial tenor-baritone, precise, haunted | Robust · 0.9 · 0.2 |
| VOX_21 | Satyavatī (young) | young woman of eighteen, husky confident alto | Natural · 0.85 · 0.3 |
| VOX_21B | Satyavatī (old) | old queen, cracked, dignified | Natural · 0.85 · 0.25 |
| VOX_22 | Śaṁtanu | noble warm baritone | Natural · 0.9 · 0.25 |
| VOX_22B | Śaṁtanu (76) | the same voice grey and tired | Natural · 0.9 · 0.25 |
| VOX_23 | Gaṅgā | timeless calm woman, voice echoing like a cave under water | Robust · 0.9 · 0.2 |
| VOX_24 | Ākāśavāṇī (sky-voice) | soft layered chorus of male and female whispers in perfect unison | Robust · 0.85 · 0.1 |
| VOX_25 | Ambā | young woman, fierce and proud | Natural · 0.85 · 0.35 |
| VOX_26 | Pāṇḍu | gentle melancholic baritone | Natural · 0.85 · 0.25 |
| VOX_27 | Adhiratha | simple warm charioteer, older | Natural · 0.85 · 0.25 |
| VOX_28 | Mādrī | sweet young woman, resolute | Natural · 0.85 · 0.3 |
| VOX_29 | Yuyutsu | calm honest voice | Natural · 0.85 · 0.2 |
| VOX_30 | Kṛpa | lean dry elder voice | Natural · 0.85 · 0.2 |
| VOX_31 | Aśvatthāman | fierce wild baritone that becomes grief-mad | Creative · 0.85 · 0.45 |
| VOX_32 | Drupada | proud king, bitter | Natural · 0.85 · 0.3 |
| VOX_33 | Dhṛṣṭadyumna | commanding young warrior baritone | Natural · 0.85 · 0.3 |
| VOX_34 | Śikhaṇḍin | clear androgynous voice | Natural · 0.85 · 0.3 |
| VOX_35 | Dhaumya | calm priestly baritone, able to chant | Robust · 0.9 · 0.2 |
| VOX_36 | Śalya | big proud sardonic voice | Natural · 0.85 · 0.35 |
| VOX_37 | Nārada | bright melodious ageless voice, knowing | Natural · 0.85 · 0.3 |
| VOX_38 | Ulūpī | low silky female voice with a slight breathy hiss | Natural · 0.85 · 0.3 |
| VOX_39 | Citrāṅgadā | frank strong young woman | Natural · 0.85 · 0.3 |
| VOX_40 | Subhadrā | bright fearless young woman | Natural · 0.85 · 0.3 |
| VOX_41 | Abhimanyu | bright fearless boy-warrior of sixteen | Natural · 0.85 · 0.35 |
| VOX_42 | Sūrya | radiant deep male voice with fatherly warmth | Robust · 0.9 · 0.2 |
| VOX_43 | Agni | huge crackling deep voice | Natural · 0.85 · 0.35 |
| VOX_44 | Indra | regal smooth voice, a little sly | Natural · 0.85 · 0.3 |
| VOX_45 | Śiva | vast calm bass; as the hunter rough and amused | Robust · 0.9 · 0.25 |
| VOX_46 | Mātali | quick crisp voice | Natural · 0.85 · 0.25 |
| VOX_47 | Citrasena | musical laughing tenor | Natural · 0.85 · 0.35 |
| VOX_48 | Dharma / Yakṣa | booming stern voice from everywhere; revealed, warm and fatherly | Robust · 0.9 · 0.25 |
| VOX_49 | Hanumān | old gravelly amused voice, enormous resonance when revealed | Natural · 0.85 · 0.35 |
| VOX_50 | Nahuṣa | hollow serpent-like old king's voice | Natural · 0.85 · 0.3 |
| VOX_51 | Paraśurāma | thunderous ancient voice | Natural · 0.85 · 0.35 |
| VOX_52 | Hiḍimba | guttural roaring man-eater | Creative · 0.8 · 0.5 |
| VOX_53 | Hiḍimbā | wild husky woman | Natural · 0.85 · 0.35 |
| VOX_54 | Ghaṭotkaca | huge booming young giant, affectionate | Natural · 0.85 · 0.35 |
| VOX_55 | Baka | guttural, gluttonous | Creative · 0.8 · 0.45 |
| VOX_56 | Kirmīra | guttural, hateful | Creative · 0.8 · 0.45 |
| VOX_57 | Maya | quick clever nasal voice | Natural · 0.85 · 0.3 |
| VOX_58 | Jarāsaṁdha | massive gravel bass | Natural · 0.85 · 0.35 |
| VOX_59 | Śiśupāla | sneering baritone | Natural · 0.85 · 0.4 |
| VOX_60 | Prātikāmin | nervous servant | Natural · 0.85 · 0.3 |
| VOX_61 | Jayadratha | vain oily voice | Natural · 0.85 · 0.35 |
| VOX_62 | Virāṭa | florid old boastful king | Natural · 0.85 · 0.35 |
| VOX_63 | Sudeṣṇā | nervous queen | Natural · 0.85 · 0.3 |
| VOX_64 | Kīcaka | heavy lustful voice | Natural · 0.85 · 0.4 |
| VOX_65 | Uttara | boastful teenager whose voice cracks when scared | Creative · 0.8 · 0.45 |
| VOX_66 | Uttarā | sweet girl | Natural · 0.85 · 0.3 |
| VOX_67 | Sātyaki | hot-tempered strong voice | Natural · 0.85 · 0.35 |
| VOX_68 | Kṛtavarman | cold hard voice | Natural · 0.85 · 0.3 |
| VOX_69 | Bhūriśravas | dignified elder | Natural · 0.85 · 0.25 |
| VOX_70 | Bhagadatta | ancient fierce voice | Natural · 0.85 · 0.3 |
| VOX_71 | Balarāma | loud big voice, quick to anger | Natural · 0.85 · 0.4 |
| VOX_U01 | Sūtradhāra | nervous old man | Natural · 0.85 · 0.3 |
| VOX_U02 | Āstīka | calm boy | Natural · 0.85 · 0.2 |
| VOX_U03 | Dāśarāja | hard shrewd middle-aged man | Natural · 0.85 · 0.3 |
| VOX_U05 | Śālva | proud cruel king | Natural · 0.85 · 0.35 |
| VOX_U06 | Durvāsas | thunderous irritable ascetic | Natural · 0.85 · 0.4 |
| VOX_U07 | Rādhā | warm motherly woman | Natural · 0.85 · 0.3 |
| VOX_U08 | Elder ṛṣi | serene old man | Natural · 0.85 · 0.2 |
| VOX_U09 | Aṅgāraparṇa | arrogant gandharva | Natural · 0.85 · 0.35 |
| VOX_U10 | Old brahmin | anxious old man | Natural · 0.85 · 0.3 |
| VOX_U11 | Young brahmin | eager young man | Natural · 0.85 · 0.3 |
| VOX_U12 | Robbed brahmin | wailing old man | Creative · 0.8 · 0.4 |
| VOX_U13 | Citravāhana | dignified king | Natural · 0.85 · 0.25 |
| VOX_U14 | Vargā | soft apsaras | Natural · 0.85 · 0.3 |
| VOX_U15 | Prativindhya | calm young man | Natural · 0.85 · 0.25 |
| VOX_U16 | Purocana | oily charming | Natural · 0.85 · 0.35 |
| VOX_U17 | Miner | gruff whisper | Natural · 0.85 · 0.3 |
| VOX_U18 | Ekacakrā brahmin | frightened man | Natural · 0.85 · 0.35 |
| VOX_U19 | Brahmin wife | brave weeping woman | Natural · 0.85 · 0.35 |
| VOX_U20 | Brahmin daughter | brave young girl | Natural · 0.85 · 0.3 |
| VOX_U21 | Maitreya | stern old sage | Natural · 0.85 · 0.3 |
| VOX_U22 | Bṛhadaśva | gentle storyteller sage | Natural · 0.85 · 0.25 |
| VOX_U23 | Lomaśa | cheerful old sage | Natural · 0.85 · 0.3 |
| VOX_U24 | Araṇī brahmin | worried man | Natural · 0.85 · 0.3 |
| VOX_U25 | Suśarman | grim warrior | Natural · 0.85 · 0.3 |
| VOX_U26 | Ulūka | sharp-tongued young man | Natural · 0.85 · 0.4 |
| VOX_U27 | Sthūṇākarṇa | kindly yakṣa | Natural · 0.85 · 0.3 |
| VOX_U28 | Sanatsujāta | boy's voice with an old soul | Natural · 0.85 · 0.2 |
| VOX_U29 | Irāvat | laughing young man | Natural · 0.85 · 0.35 |
| VOX_U30 | Cārvāka | shrieking false brahmin | Creative · 0.8 · 0.5 |
| VOX_U31 | Babhruvāhana | young king | Natural · 0.85 · 0.3 |
| VOX_U32 | Sāmba | mischievous youth | Natural · 0.85 · 0.4 |
| VOX_U33 | Viśvāmitra | fierce old sage | Natural · 0.85 · 0.35 |
| VOX_U34 | Kaṇva | grave old sage | Natural · 0.85 · 0.25 |
| VOX_U35 | Jarā (hunter) | frightened forest hunter | Natural · 0.85 · 0.35 |
| VOX_U36 | Devadūta | plain flat voice | Robust · 0.85 · 0.1 |
| VOX_U37 | The four chicks | four tiny high child voices in unison, trembling | Creative · 0.8 · 0.4 |
| VOX_U38 | Kindama (dying deer) | a dying man's voice coming from an animal, breathy | Creative · 0.8 · 0.4 |
| VOX_U39 | Herald / crier | loud ceremonial herald | Natural · 0.85 · 0.35 |
| VOX_U40 | Kaurava soldier / messenger | panicked soldier | Creative · 0.8 · 0.4 |
| VOX_U41 | Yama | deep stern unhurried bass, cold as stone | Robust · 0.85 · 0.15 |
| VOX_CROWD | Crowd lines ("धिक्!", "भीष्म!", "अर्जुन!") | build from 12 different utility voices, each line generated 3× with slight variation, layered and panned | — |

---
## 5. DIALOGUE PIPELINE (lip-sync + zero voice drift)
1. **On-camera line (default — Method A, "Veo bolta hai, Eleven awaaz deta hai")**: Flow prompt mein line likhi hoti hai → Veo natural lip-sync ke saath clip banata hai → clip ki audio nikaal kar **ElevenLabs Voice Changer** mein character ki VOX voice par convert → timing aur hoth 100% match, awaaz har baar same.
2. **Narration / V.O. / off-screen (Method B)**: `build/<chapter>_vo.csv` se seedha **Eleven v4 TTS** (tags ke saath). Lip-sync ki zaroorat nahi.
3. **Hero close-ups / emotional peaks (Method C)**: aap khud (ya voice artist) line perform karein → Voice Changer → character voice. Sabse achhi acting control. (Peaks: Devavrata ki pratigya, Draupadī ka prashn, "लोभ धर्म का नाश करता है", Karṇa–Kuntī, Gītā ke mukhya shlok, "ये शिखंडी के बाण नहीं", Duryodhana ke antim shabd, Vyāsa ka ūrdhvabāhu.)
4. **Tag rule:** audio tags hamesha English mein `[whispers]`, `[angry]`, `[sighs]`, `[crying]`, `[laughs]`, `[shouting]`, `[slowly]`, `[trembling]`. Har line max ~250 characters; lambi speech ko lines mein toda gaya hai.
5. **Sanskrit lines:** pehle Devanagari Sanskrit, phir Hindi. Saṁhitā-pāṭha ke liye `[slowly] [reverent]` tag; galat uchchāraṇ ho to shabd ko hyphen se todein (उदा. "ऊर्ध्व-बाहुर्-विरौम्य्-एष").

## 6. MIX & DELIVERY
* **YouTube master:** stereo, **–14 LUFS integrated**, true-peak **≤ –1 dBTP**, LRA 10–14 LU (cinematic). Dialogue anchor ~–20 LUFS short-term; music bed –18 to –24 dB under dialogue.
* **Stems (M&E for future dubs):** DX (dialogue) · MX (music) · FX (sfx) · AMB — har chapter ke alag. Future OTT/theatre ke liye 5.1 / Atmos re-mix inhi stems se.
* **Silence rule:** SIL cues = jaan-boojh kar khaamoshi; mix engineer inhe "bharne" ki koshish na kare.
* **Spatial notes** (`height`, `rear`, `LFE`) screenplays mein hain: stereo mein = reverb-width aur low-end se; 5.1 mein = actual channels.

## 7. QUANTITY SUMMARY (auto-check: `tools/mbx.py compile` → cue_sheet.csv, sfx_usage.csv, vo_all.csv)
Final totals (minutes per tool, SFX count, VO characters) are written by the compiler into `05_Scene_Index_GENERATED.md` → section "Audio totals".
