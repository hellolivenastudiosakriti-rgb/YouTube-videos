# महाभारत त्रयी — CAST & LOOK BIBLE (LOCKED v1.0)
**Zero-drift rule:** har shot mein character ka **wahi reference sheet** aur **wahi DNA text, shabdash (word-for-word)** jayega. DNA kabhi "improvise" nahi hoga. Is file ki tables ko `tools/mbx.py` padhta hai. Census (kitne characters / looks / sheets) usi se auto-generate hota hai: `01b_Cast_Census_GENERATED.md`.

**Kaise padhein**
* `CHAR` = ek vyakti/praani (ek hi chehra, poori trilogy mein).
* `LOOK` = us chehre ki ek **umar + poshak** sthiti. Har LOOK = ek reference sheet (jab tak `SHEET` mein `group:` ya `vfx` na likha ho).
* **Final prompt DNA = FACE DNA (CHAR) + LOOK DNA.** NEVER column negative block mein jaata hai.
* `[CE x.y.z]` = BORI Critical Edition se pramaanit roop-varnan. Jahan CE chup hai, wahan design choice hai (CE ke virodh mein nahi).
* **State modifiers** (naya sheet NAHI chahiye, sirf prompt text): `+wet` bhiga, `+dust` dhool, `+blood` khoon ke chheente, `+wounded` ghaav, `+armour-off` kavach utra hua, `+spirit` (Gaṅgā-raatri/svarga: shuddh shwet vastra, shaant chehra, koi glow-effect nahi).

---

## 1. CHARACTERS — FACE DNA (locked)

| CHAR | नाम | TIER | FACE DNA (locked, English for Flow/Veo) | NEVER | CE anchor | VOX |
|---|---|---|---|---|---|---|
| CH_BHISHMA | भीष्म (देवव्रत) | T1 | very tall, long-limbed, broad-shouldered man; long oval face, high cheekbones, deep-set steady eyes, strong straight nose, thin firm lips; wheat-brown skin; perfectly upright posture at every age | bronze conch, fantasy armour, crown of gems | white turban, white armour, white horses 6.16.40, 6.20.9; golden palm banner with five stars 6.16.41 | VOX_01 |
| CH_KRISHNA | कृष्ण वासुदेव | T1 | lean medium-tall man with sapphire-dark skin, long almond eyes with a faint permanent half-smile, fine straight nose, full lips, smooth calm brow, black curling shoulder-length hair | peacock feather, blue body paint, halo, glowing aura, flute in battle | "pītakauśeyasaṁvīto maṇiśyāmo" 6.102.57; "pītavāsā" 5.92.52 | VOX_13 |
| CH_ARJUNA | अर्जुन | T1 | dark-skinned (śyāma) lean man with high lion-like shoulders and long arms, long lotus-shaped eyes with intense focus, sharp straight nose, firm jaw; hard bowstring calluses and thin scars on both forearms | fair skin, bulky bodybuilder physique | "śyāmo yuvā… siṁhonnatāṁso… padmāyatākṣo" 15.32.7; bowstring scars 4.2.21 | VOX_07 |
| CH_KARNA | कर्ण (वसुषेण, वैकर्तन) | T1 | very tall lion-built man (broad chest, narrow waist), warm golden-bronze skin with a natural sheen, large wide eyes, straight heavy brows, strong square jaw, calm proud mouth, long wavy dark hair | metal plate armour on the infant, modern gold jewellery | tall, "like a golden palm", lion-built, large-eyed 1.126.2–5 | VOX_09 |
| CH_DRAUPADI | द्रौपदी (कृष्णा, याज्ञसेनी) | T1 | dark-skinned woman with a blue-lotus hue (śyāmā), very large long eyes shaped like lotus petals, strong dark brows, full lips, high forehead, extremely long black curling hair reaching the knees | fair skin, straight hair, sindoor, modern sari drape | "śyāmā padmapalāśākṣī nīlakuñcitamūrdhajā" 1.155.42; 15.32.9 | VOX_12 |
| CH_YUDHISHTHIRA | युधिष्ठिर | T1 | tall man with golden-fair skin like pure gold, large lion-like frame, prominent strong nose, large long eyes, long face of coppery undertone, gentle steady gaze, head slightly inclined as if listening | dark skin, weak or timid posture | "jāmbūnadaśuddhagaura… pracaṇḍaghoṇaḥ pr̥thudīrghanetraḥ" 15.32.5 | VOX_05 |
| CH_BHIMA | भीम (वृकोदर) | T1 | giant man with warm sun-browned golden skin, enormously broad shoulders, very thick long arms, barrel chest, thick neck, wide open face with laughing eyes that turn terrifying in rage, broad nose, thick curly hair; heavy rolling gait like a rutting elephant | fat belly, cartoon muscles, pale skin | CE gives both: "prataptacāmīkaraśuddhagauraḥ" (fair like heated gold) 15.32.6 and "śyāmo mahābāhuḥ siṁhaskandhaḥ" (Hiḍimbā's view) 1.139.14 → design: sun-browned gold | VOX_06 |
| CH_NAKULA | नकुल | T1 | the most handsome of the brothers: fair, perfectly proportioned, fine-boned oval face, bright open smile, elegant arched brows, wavy hair worn longer than his twin | identical face to Sahadeva | twins "viṣṇumahendrakalpau", matchless in beauty 15.32.8; pride of beauty 17.2 | VOX_08N |
| CH_SAHADEVA | सहदेव | T1 | fair, handsome, a little slighter than his twin: squarer face, narrow thoughtful eyes, straight level brows, small mole on the left cheekbone, straight hair kept in a tight knot, watchful unsmiling mouth | identical face to Nakula | 15.32.8; pride of wisdom 17.2 | VOX_08S |
| CH_DURYODHANA | दुर्योधन (सुयोधन) | T1 | tall, massively built mace-fighter with heavy shoulders and very thick powerful thighs, handsome hard face, thick black moustache, proud raised chin, hooded intense eyes, a sneer that turns into a laugh | cartoon villain makeup, horns, black eyeliner | thigh "like a plantain stem, elephant's trunk" 2.63.11; jewelled serpent banner 7.80.26 | VOX_10 |
| CH_KUNTI | कुंती (पृथा) | T1 | fair woman of medium height, delicate but resolute face, large expressive dark eyes, fine nose, small firm mouth; silent endurance in the eyes | heavy makeup | daughter of Śūra, adopted by Kuntibhoja 1.104.1–3 | VOX_04 |
| CH_DHRITARASHTRA | धृतराष्ट्र | T1 | huge immensely strong man, broad heavy face, eyes open but unseeing (pale, unfocused, drifting), heavy brows, deep lines around the mouth, head always tilted to listen | dark glasses, closed sewn eyes | crushes the iron Bhīma 11.12 | VOX_02 |
| CH_GANDHARI | गांधारी | T1 | tall regal woman with sharp high cheekbones, fine straight nose, composed lips, pale north-western complexion; eyes always covered by a dark cloth band folded many times | thin or transparent blindfold, visible eyes | blindfold "paṭṭa folded many times" 1.103.13 | VOX_17 |
| CH_SHAKUNI | शकुनि (सौबल) | T1 | lean sharp-featured man from Gandhāra: pale skin, narrow clever light-brown eyes, hooked nose, thin lips with a habitual slight smile, thin pointed beard, long fingers; walks normally | limp, walking stick, bone dice, cartoon villain | portion of Dvāpara 1.61.72; dice-master 2.44 | VOX_11 |
| CH_VIDURA | विदुर | T1 | slender man of medium height, calm intelligent face, deep-set kind eyes, prominent cheekbones, thin beard; always dressed simply | royal crown | son of a maidservant 1.100.23 | VOX_03 |
| CH_DRONA | द्रोण | T1 | dark-skinned (śyāma) wiry brahmin-warrior, gaunt cheeks, piercing eyes under heavy brows, long nose, tight thin mouth; moves with the speed of a sixteen-year-old even in old age | fat, slow, white skin | "ākarṇapalitaḥ śyāmo vayasāśītipañcakaḥ … ṣoḍaśavarṣavat" 7.165.49 | VOX_14 |
| CH_VYASA | व्यास (कृष्ण द्वैपायन) | T1 | very dark-skinned tall ascetic with tawny-brown matted hair and a tawny-brown beard, blazing deep-set eyes, gaunt powerful frame, the stillness of a mountain | white skin, neat white beard | "kr̥ṣṇasya kapilā jaṭā dīpte ca locane babhrūṇi … śmaśrūṇi" 1.100.5 | VOX_18 |
| CH_SANJAYA | संजय | T1 | lean sūta in his fifties, clear watchful eyes, close-cropped grey beard, composed reporter's face | — | divine sight from Vyāsa 6.2 | VOX_20 |
| CH_JANAMEJAYA | जनमेजय | T2 | young king in his twenties, gaunt intense face, eyes bright with grief and hatred, unshaven dark stubble, long unbound hair, wheat-brown skin | crown during the rite | consecrated at the snake-sacrifice 1.47 | VOX_19 |
| CH_VAISHAMPAYANA | वैशंपायन | T2 | lean brahmin storyteller in his late fifties, weathered warm-brown face, short grey beard, kind deep-set eyes, expressive hands | — | Vyāsa's disciple 1.54.22 | VOX_00 |
| CH_SUTRADHARA | सूत्रधार (स्थपति) | T3 | old, thin architect-bard with a bald crown and white side-hair, sharp nervous eyes | — | 1.47.14–15 | VOX_U01 |
| CH_ASTIKA | आस्तीक | T3 | serene brahmin boy of twelve, shaved head with a small tuft, unafraid eyes, slight build | — | 1.51–53; 18.5 | VOX_U02 |
| CH_GANGA | गंगा | T2 | woman of impossible calm and timeless beauty, river-pale luminous skin with a wet sheen, long black hair always damp, large still eyes | glowing skin, fish tail, crown of lotuses | 1.92; 13.154 | VOX_23 |
| CH_SHANTANU | शंतनु | T2 | tall handsome king, broad noble face, gentle eyes, strong nose, full beard | — | 1.92–1.94 | VOX_22 |
| CH_SATYAVATI | सत्यवती (काली) | T2 | dark-skinned woman of striking beauty, strong cheekbones, long almond eyes, a knowing mouth | fair skin | called "Kālī" 1.54.2, 1.99.21 | VOX_21 |
| CH_DASHARAJA | दाशराज | T3 | hard intelligent fisher-chief, sun-blackened skin, deep-set calculating eyes, grizzled short beard | — | 1.94.47–89 | VOX_U03 |
| CH_MINISTER_OLD | वृद्ध अमात्य | T3 | old courtier with a white beard and downcast eyes | — | 1.94.65 | — |
| CH_CHITRANGADA_KURU | चित्रांगद (कुरु-राजा) | T3 | arrogant young king, handsome, sharp chin, proud eyes | — | 1.95 | — |
| CH_GANDHARVA_CHITRANGADA | चित्रांगद (गंधर्व) | T3 | otherworldly warrior with pale golden skin, long silver-black hair, cold eyes | wings, glow | 1.95 | — |
| CH_AMBA | अंबा | T2 | princess with fierce eyes, strong jaw, wheat skin | — | 1.96; 5.170–193 | VOX_25 |
| CH_AMBIKA | अंबिका | T3 | young princess, pale delicate face, frightened eyes | — | 1.100 | — |
| CH_AMBALIKA | अंबालिका | T3 | younger princess, very fair soft face | — | 1.100 | — |
| CH_SHALVA | शाल्व | T3 | proud king with a thick moustache and a cruel mouth | — | 1.96; 5.172 | VOX_U05 |
| CH_VICHITRAVIRYA | विचित्रवीर्य | T3 | slender young king, handsome but sickly, hollow cheeks | — | 1.96 | — |
| CH_DASI | दासी (विदुर-माता) | T3 | young maidservant with a calm dignified face, dark skin | — | 1.100.23 | — |
| CH_PANDU | पांडु | T2 | tall king with very pale skin (pāṇḍu), fine features, light eyes, gentle melancholy | — | 1.100–1.116 | VOX_26 |
| CH_DURVASAS | दुर्वासा | T3 | fearsome old ascetic, wild white hair, burning eyes, thunderous brows | — | 1.104.5–6 | VOX_U06 |
| CH_SURYA | सूर्य | T2 | a human-shaped blaze: tall man of golden-white light whose features show only at the edges, heat-shimmer around him | cartoon sun-god, chariot of seven horses | 1.104.8–12; 3.4.1; 5.144.1 | VOX_42 |
| CH_RADHA | राधा | T3 | warm round-faced charioteer's wife, kind eyes | — | 1.104.14 | VOX_U07 |
| CH_ADHIRATHA | अधिरथ | T2 | sturdy charioteer, honest weathered face, big hands | — | 1.104.14–15; 1.127.1–4 | VOX_27 |
| CH_MADRI | माद्री | T2 | fair beautiful young queen of Madra, bright eyes, gentle face | — | 1.105; 1.116 | VOX_28 |
| CH_RISHI_SHATASHRINGA | शतशृंग ऋषि-प्रमुख | T3 | tall serene elder ascetic with a long white beard | — | 1.117 | VOX_U08 |
| CH_DUHSHASANA | दुःशासन | T2 | thick-set coarse-featured man, low brow, wet grin, small hot eyes | — | 2.60.20–27; 8.61 | VOX_16 |
| CH_VIKARNA | विकर्ण | T2 | slender young Kaurava with an earnest, frightened, brave face | — | 2.61.11–24 | VOX_15V |
| CH_YUYUTSU | युयुत्सु | T2 | son of a vaiśya maid: calm, worried, honest face | — | 1.107.35; 1.119.40; 6.41 | VOX_29 |
| CH_KRIPA | कृप | T2 | lean brahmin-warrior with an ascetic's face, long beard (grey, later white) | — | 1.120; bull banner 7.80.14 | VOX_30 |
| CH_KRIPI | कृपी | T3 | thin dignified brahmin woman | — | 1.121 | — |
| CH_ASHVATTHAMA | अश्वत्थामा | T2 | fierce handsome warrior with a natural jewel set in the centre of his forehead (a living gem in the skin), wild eyes | glowing jewel, sci-fi stone | jewel 10.15–16; lion's-tail banner 6.17.21 | VOX_31 |
| CH_EKALAVYA | एकलव्य | T2 | dark-skinned forest youth, matted hair, mud-smeared limbs, open radiant face | — | "kr̥ṣṇaṁ malāvadigdhāṅgaṁ kr̥ṣṇājinadharaṁ jaṭilam" 1.123.18 | VOX_15E |
| CH_DRUPADA | द्रुपद | T2 | proud king with a hawk nose and a grudge in his eyes | — | 1.122; 1.128; 1.155 | VOX_32 |
| CH_DHRISHTADYUMNA | धृष्टद्युम्न | T2 | tall fire-born warrior with copper-dark skin, fierce bright eyes, high cheekbones | — | 1.155.33–39 | VOX_33 |
| CH_SHIKHANDI | शिखंडी | T2 | warrior born a woman: fine-boned face, intense eyes, androgynous grace | — | 5.189–193 | VOX_34 |
| CH_YAJA | याज | T3 | lean ascetic ritual priest | — | 1.155 | — |
| CH_UPAYAJA | उपयाज | T3 | younger ascetic ritual priest | — | 1.155 | — |
| CH_DHAUMYA | धौम्य | T2 | calm family priest, round face, grey beard | — | 1.174; 2.71.20 | VOX_35 |
| CH_ANGARAPARNA | अंगारपर्ण (गंधर्व) | T3 | arrogant handsome gandharva warrior | — | 1.158 | VOX_U09 |
| CH_KUMBHINASI | कुम्भीनसी | T3 | gandharva wife, pleading eyes | — | 1.158 | — |
| CH_BALARAMA | बलराम | T2 | giant man with white-radiant fair skin, huge shoulders, broad face, quick temper | — | "nīlavāsāḥ sitaprabhaḥ" 9.54.42; 1.212.20 | VOX_71 |
| CH_SHALYA | शल्य | T2 | big proud king of Madra, fair, thick moustache, sardonic mouth | — | 1.181; 5.8; golden ploughshare banner 7.80.18 | VOX_36 |
| CH_BRAHMIN_OLD | वृद्ध ब्राह्मण (स्वयंवर) | T3 | anxious old brahmin, white tuft | — | 1.179.4–6 | VOX_U10 |
| CH_BRAHMIN_YOUNG | युवा ब्राह्मण (स्वयंवर) | T3 | eager young brahmin | — | 1.179.9–10 | VOX_U11 |
| CH_NARADA | नारद | T2 | radiant ageless sage, fair skin, white beard, playful knowing eyes | halo | 1.200; 2.5; 2.71.29 | VOX_37 |
| CH_BRAHMIN_ROBBED | लुटा हुआ ब्राह्मण | T3 | wailing old brahmin | — | 1.205 | VOX_U12 |
| CH_ULUPI | उलूपी | T2 | Nāga princess: dusky luminous skin with a faint scale-like sheen at the shoulders, dark wet hair, serpentine grace | snake tail, green skin | 1.206 | VOX_38 |
| CH_KAURAVYA | कौरव्य (नागराज) | T3 | old Nāga king, heavy-lidded eyes | — | 1.206 | — |
| CH_CHITRAVAHANA | चित्रवाहन | T3 | dignified eastern king | — | 1.207 | VOX_U13 |
| CH_CHITRANGADAA | चित्रांगदा | T2 | warrior-princess of Maṇalūra, dark, strong-limbed, frank eyes | — | 1.207; 14.78–82 | VOX_39 |
| CH_VARGA | वर्गा (अप्सरा) | T3 | apsaras freed from a crocodile's form | — | 1.208–209 | VOX_U14 |
| CH_SUBHADRA | सुभद्रा | T2 | golden-fair young woman with a golden radiance, bright fearless eyes | — | "kanakottamābhā … mūrtimatīva gaurī" 15.32.10 | VOX_40 |
| CH_ABHIMANYU | अभिमन्यु | T2 | fair sixteen-year-old warrior with his father's long eyes and his uncle Kṛṣṇa's half-smile, fearless | — | 7.33–7.48 | VOX_41 |
| CH_PRATIVINDHYA | प्रतिविंध्य | T2 | Draupadī's eldest son: dark like his mother, Yudhiṣṭhira's calm brow | — | 1.213; 10.8 | VOX_U15 |
| CH_SUTASOMA | सुतसोम | T3 | Bhīma's son by Draupadī: fair, broad, cheerful | — | 1.213; 10.8 | — |
| CH_SHRUTAKARMAN | श्रुतकर्मा | T3 | Arjuna's son by Draupadī: dark, lean, intense | — | 1.213; 10.8 | — |
| CH_SHATANIKA | शतानीक | T3 | Nakula's son: fair, handsome, wavy hair | — | 1.213; 10.8 | — |
| CH_SHRUTASENA | श्रुतसेन | T3 | Sahadeva's son: fair, serious, straight hair | — | 1.213; 10.8 | — |
| CH_AGNI | अग्नि | T2 | huge tawny-bearded brahmin whose skin shimmers like heat-haze, eyes like embers | flames for hair, red skin | 1.214–216; 17.1 | VOX_43 |
| CH_MAYA | मय (असुर-शिल्पी) | T2 | small wiry asura architect, soot-dark skin, brilliant restless eyes | horns, fangs | 1.219; 2.1–3 | VOX_57 |
| CH_JARASANDHA | जरासंध | T2 | massive scarred king of Magadha with a faint seam running down the centre of his body (joined by Jarā) | split body | "jarayā saṁdhito" 2.17.6 | VOX_58 |
| CH_JARA_RAKSHASI | जरा (राक्षसी) | T3 | old rākṣasī, kindly-grotesque | — | 2.16 | — |
| CH_MAGADHA_PRINCE | सहदेव (जरासंध-पुत्र) | T3 | young prince of Magadha, frightened | — | 2.22 | — |
| CH_SHISHUPALA | शिशुपाल | T2 | handsome arrogant king with a sneering mouth | three eyes or four arms on the adult | 2.37–42 | VOX_59 |
| CH_PRATIKAMIN | प्रातिकामी | T3 | anxious sūta messenger | — | 2.60; 2.67 | VOX_60 |
| CH_PUROCHANA | पुरोचन | T3 | smiling minister-builder with oily charm | — | 1.132–136 | VOX_U16 |
| CH_MINER | खनक | T3 | dirt-caked miner, quick eyes | — | 1.135 | VOX_U17 |
| CH_NISHADI | निषादी | T3 | hungry Niṣāda woman | — | 1.136.7 | — |
| CH_EKACHAKRA_BRAHMIN | एकचक्रा का ब्राह्मण | T3 | frightened poor brahmin | — | 1.145–147 | VOX_U18 |
| CH_EKACHAKRA_WIFE | ब्राह्मणी | T3 | brave weeping brahmin wife | — | 1.145–147 | VOX_U19 |
| CH_EKACHAKRA_DAUGHTER | ब्राह्मण-कन्या | T3 | brave young daughter | — | 1.146 | VOX_U20 |
| CH_HIDIMBA | हिडिंब | T2 | huge man-eater: tawny-yellow eyes, red when enraged, gaping fanged mouth, rough hair standing up | horns, demon wings | "piṅgākṣaḥ karālo … ūrdhvakeśo" 1.139.2; 1.140.2 | VOX_52 |
| CH_HIDIMBI | हिडिंबा | T2 | in her assumed human form: tall dark beauty with a wild edge, large eyes | fangs in human form | 1.139–143 | VOX_53 |
| CH_GHATOTKACHA | घटोत्कच | T2 | giant rākṣasa: bald pot-shaped shining head, misshapen fierce eyes, huge mouth, spike-like pointed ears; terrifying but loving | horns, hair | "virūpākṣaṁ mahāvaktraṁ śaṅkukarṇaṁ" 1.143.28; pot-head bald 1.143.34 | VOX_54 |
| CH_BAKA | बक | T3 | colossal red-brown rākṣasa, tusks, pot belly | — | 1.151 | VOX_55 |
| CH_KIRMIRA | किर्मीर | T3 | Baka's brother: eyes like coals, arms like tree trunks | — | 3.11–12 | VOX_56 |
| CH_MAITREYA | मैत्रेय | T3 | stern elder sage | — | 3.10–11 | VOX_U21 |
| CH_INDRA | इंद्र | T2 | regal powerful god-king, golden-fair skin, curled black beard, calm ancient eyes | thousand eyes on body, glow | 3.38; 3.42; 3.294; 17.3 | VOX_44 |
| CH_SHIVA | शिव | T2 | immense ageless being: as hunter, radiant like a golden tree; revealed, a calm ancient face, ash-pale skin, matted locks piled high | blue skin, glowing third eye, neon | "kairātaṁ veṣam āsthāya kāñcanadrumasaṁnibham" 3.40.2 | VOX_45 |
| CH_UMA | उमा | T3 | goddess in hunter-woman guise, golden, serene | — | "devyā sahomayā … samānavrataveṣayā" 3.40.4 | — |
| CH_YAMA | यम | T3 | dark stern lord with a noose | — | 3.42 | — |
| CH_VARUNA | वरुण | T3 | sea-dark lord with a noose of rope and pearls | — | 3.42 | — |
| CH_KUBERA | कुबेर | T3 | stout golden lord with a heavy necklace | — | 3.42 | — |
| CH_MATALI | मातलि | T2 | Indra's charioteer, lean ageless man, quick eyes | — | 3.43 | VOX_46 |
| CH_CHITRASENA | चित्रसेन (गंधर्व) | T2 | beautiful gandharva king with musician's hands and playful eyes | wings | 3.45; 3.235 | VOX_47 |
| CH_URVASHI | उर्वशी | T3 | apsaras dancer of unearthly grace | — | 3.44.29 | — |
| CH_BRIHADASHVA | बृहदश्व | T3 | gentle storyteller-sage | — | 3.50 | VOX_U22 |
| CH_LOMASHA | लोमश | T3 | hairy cheerful pilgrim-sage | — | 3.80+ | VOX_U23 |
| CH_HANUMAN | हनुमान | T2 | huge old monkey: lightning-tawny fur, broad shoulders, slender waist, short thick neck, red lips, copper-red tongue and mouth, red ears, mobile brows, rounded sharp fangs, face shining like the moon; tail raised like a banner | human face, gada, crown, cartoon | 3.146.59–68; old age 3.147.16 | VOX_49 |
| CH_JATASURA | जटासुर | T3 | rākṣasa disguised as a brahmin, sly smile | — | 3.154 | — |
| CH_NAHUSHA | नहुष | T3 | as king freed from the python: radiant old king | — | 3.175–178 | VOX_50 |
| CH_JAYADRATHA | जयद्रथ | T2 | handsome vain king of Sindhu, oiled curls, weak chin hidden in a beard | — | 3.248–256; silver boar banner 7.80.20 | VOX_61 |
| CH_DHARMA | धर्म | T2 | as Yakṣa: palm-tree-tall, misshapen-eyed, blazing like fire and sun; revealed: dignified elder, calm stern kind eyes | — | "virūpākṣaṁ mahākāyaṁ yakṣaṁ tālasamucchrayam jvalanārkapratīkāśam" 3.297.20 | VOX_48 |
| CH_BRAHMIN_ARANI | अरणी वाला ब्राह्मण | T3 | worried forest brahmin | — | 3.295 | VOX_U24 |
| CH_VIRATA | विराट | T2 | old king of Matsya: florid, boastful, kind at heart | — | 4.1–4.67; 7.161 | VOX_62 |
| CH_SUDESHNA | सुदेष्णा | T2 | queen of Matsya, handsome, nervous | — | 4.8; 4.14 | VOX_63 |
| CH_KICHAKA | कीचक | T2 | huge perfumed brutal commander, heavy jaw | — | 4.13–4.21 | VOX_64 |
| CH_UTTARA | उत्तर (भूमिंजय) | T2 | boastful teenage prince, soft face | — | 4.34–4.62; 6.43 | VOX_65 |
| CH_UTTARAA | उत्तरा | T2 | golden-fair girl, bright shy eyes | — | "niṣṭaptasuvarṇagaurī" 15.32.14 | VOX_66 |
| CH_SUSHARMAN | सुशर्मा (त्रिगर्त) | T3 | grim Trigarta king | — | 4.29–33; 7.17 | VOX_U25 |
| CH_SATYAKI | सात्यकि (युयुधान) | T2 | fierce Vṛṣṇi warrior, hot-tempered, devoted to Kṛṣṇa | — | 5.3; 7.117–118; 16.4 | VOX_67 |
| CH_KRITAVARMAN | कृतवर्मा | T2 | hard Bhoja-Vṛṣṇi warrior with a cold face | — | 10.8; 16.4 | VOX_68 |
| CH_ULUKA | उलूक | T3 | Śakuni's son, sharp-tongued envoy | — | 5.157–161 | VOX_U26 |
| CH_PARASHURAMA | परशुराम | T2 | ancient massive warrior-ascetic, white matted hair, fierce eyes, axe | — | 5.176–186; Karṇa's curse 8.29 | VOX_51 |
| CH_STHUNAKARNA | स्थूणाकर्ण (यक्ष) | T3 | kindly forest yakṣa | — | 5.193 | VOX_U27 |
| CH_SANATSUJATA | सनत्सुजात | T3 | eternal boy-sage with an old man's eyes | — | 5.41–45 | VOX_U28 |
| CH_SHVETA | श्वेत (विराट-पुत्र) | T3 | tall young Matsya prince | — | 6.45 | — |
| CH_BHURISHRAVAS | भूरिश्रवा | T2 | dignified elder Kuru warrior, grey beard | — | 7.117–118; sacrificial-post banner 7.80.22 | VOX_69 |
| CH_IRAVAT | इरावान | T3 | laughing young Nāga-born son of Arjuna | — | 6.86 | VOX_U29 |
| CH_ALAMBUSHA | अलंबुष | T3 | rākṣasa warrior in black armour, red eyes | — | 6.86 | — |
| CH_BHAGADATTA | भगदत्त | T2 | ancient king of Prāgjyotiṣa, deeply wrinkled, fierce | eyelids tied with a band (NOT CE) | 7.25–28 | VOX_70 |
| CH_LAKSHMANA_K | लक्ष्मण (दुर्योधन-पुत्र) | T3 | handsome teenage prince, his father's face softened | — | 7.45 | — |
| CH_DAUSHASANI | दौःशासनि | T3 | young brute with his father's face | — | 7.48 | — |
| CH_VRIDDHAKSHATRA | वृद्धक्षत्र | T3 | old king praying with closed eyes | — | 7.121 | — |
| CH_UTTAMAUJAS | उत्तमौजा | T3 | Pāñcāla prince, wheel-guard | — | 10.8 | — |
| CH_YUDHAMANYU | युधामन्यु | T3 | Pāñcāla prince, wheel-guard | — | 10.8 | — |
| CH_CHARVAKA | चार्वाक (राक्षस) | T3 | rākṣasa disguised as a brahmin, shrieking | — | 12.39 | VOX_U30 |
| CH_PARIKSHIT | परीक्षित | T3 | young king of 36, grave face | — | 10.16; 17.1 | — |
| CH_BABHRUVAHANA | बभ्रुवाहन | T3 | young king of Maṇalūra, his mother's dark strong face | — | 14.78–82 | VOX_U31 |
| CH_SAMBA | साम्ब | T3 | handsome mischievous young Yādava | — | 16.2 | VOX_U32 |
| CH_VISHVAMITRA | विश्वामित्र | T3 | fierce old sage | — | 16.2 | VOX_U33 |
| CH_KANVA | कण्व | T3 | grave old sage | — | 16.2 | VOX_U34 |
| CH_JARA_HUNTER | जरा (व्याध) | T3 | lean forest hunter, frightened eyes | — | 16.5.20–21 | VOX_U35 |
| CH_VAJRA | वज्र | T3 | young Yādava prince, Kṛṣṇa's great-grandson | — | 17.1.8–9 | — |
| CH_DEVADUTA | देवदूत | T3 | messenger of the gods, plain grey-robed guide | — | 18.2 | VOX_U36 |


---

## 2. LOOKS — age + costume (each = one reference sheet unless marked)

| LOOK | CHAR | LOOK NAME | AGE | PARTS | SHEET | USED IN | LOOK DNA (locked) |
|---|---|---|---|---|---|---|---|
| BHS_A | CH_BHISHMA | Devavrata (Gaṅgā dam → vow) | 36–40 | P1 | full | P1C01 | age 38, black hair in a high topknot, short black beard, bare muscular torso, white cotton lower garment, plain gold armlets; for the vow a white upper cloth over one shoulder; great composite bow |
| BHS_B | CH_BHISHMA | Regent (Kāśī) | ~60 | P1 | full | P1C02 | age 60, black hair and beard heavily streaked with grey, topknot, white cotton garments with a plain gold neck-band; in battle a white quilted cotton cuirass with bronze scales and a white turban |
| BHS_C | CH_BHISHMA | Pitāmaha (court) | ancient, appears 85–90 | P1,P2,P3 | full | P1C02–P1C07, P2C06–P2C08, P3C02, P3C08 | very old but iron-strong, long white hair in a topknot, long white beard, deep lines, clear eyes; all-white cotton and wild-silk garments, white upper cloth, a plain gold ring |
| BHS_D | CH_BHISHMA | Kurukṣetra (war) | same as C | P1,P2,P3 | full | P1C01 (lips & beard only), P2C06, P2C08, P3C01–P3C03 | white turban, white armour of quilted cotton with silvered bronze scales, white upper cloth; white horses; tall pole with a golden palm-tree banner bearing five stars; white seashell conch with a copper rim |
| BHS_E | CH_BHISHMA | Śaraśayyā | same as C | P3 | full | P3C03, P3C06, P3C08 | lying held off the ground on hundreds of arrows through back and limbs, armour removed, white lower cloth stained with old blood and dust, white beard on the chest, head resting on three arrows driven into the earth, serene eyes |
| KRS_A | CH_KRISHNA | Yuvā (Svayaṁvara → Rājasūya) | 25–36 | P1 | full | P1C05–P1C06 | clean-shaven, black curls tied with a narrow yellow cloth band, yellow silk lower garment and yellow upper cloth, simple gold earrings, a garland of wildflowers; when armed: thin razor-edged iron discus with a heavy hub, and a mace |
| KRS_B | CH_KRISHNA | Mādhava (forest visits, envoy) | 38–48 | P2,P3 | full | P2C01, P2C07, P2C08, P3C07–P3C08 | thin moustache, close beard shadow, black curls with one gold pin, royal yellow silk with a dark-blue border, gold armlets, a single pearl string |
| KRS_C | CH_KRISHNA | Pārthasārathi (charioteer) | ~49 | P2,P3 | full | P2C08, P3C01–P3C07 | black curls tied back, dust on cheekbones, yellow silk girded tight for driving, light leather-and-bronze cuirass, leather wrist guards, white leather reins, braided whip; Pāñcajanya (white seashell conch) at the belt |
| KRS_D | CH_KRISHNA | Elder Vāsudeva (Mausala) | ~85 | P3 | full | P3C08 | lean and still upright, white hair and short white beard, skin still sapphire-dark, faded yellow silk, simple gold earrings, serene tired eyes |
| ARJ_A | CH_ARJUNA | Bālaka | 11–12 | P1 | full | P1C02–P1C03 | slim dark boy, hair in a side knot, white cotton lower garment, small bow |
| ARJ_B | CH_ARJUNA | Śiṣya (Droṇa's pupil) | 16–19 | P1 | full | P1C03–P1C04 | beardless youth, hair in a high knot with a white band, white cotton lower garment, leather guards on both forearms, bow |
| ARJ_C | CH_ARJUNA | Vipra disguise | 21–22 | P1 | full | P1C04–P1C05 | wispy young beard, brahmin's hair-knot, black deerskin upper wrap, plain white lower cloth, sacred thread, ash marks on forehead and arms |
| ARJ_D | CH_ARJUNA | Rājakumāra (Indraprastha) | 22–36 | P1 | full | P1C04, P1C05–P1C07 | short trimmed black beard, hair tied high with a gold-threaded band, white and saffron cotton garments, gold armlets and earrings; for battle a leather-and-bronze cuirass; Gāṇḍīva (dark-grained bow with many-coloured lacquer bands) |
| ARJ_E | CH_ARJUNA | Vanavāsī | 36–48 | P1,P2 | full | P1C07 (end), P2C01–P2C05 | longer beard, matted locks tied up, black deerskin and bark-cloth garments, no jewellery; Gāṇḍīva wrapped in hide when travelling |
| ARJ_F | CH_ARJUNA | Indraloka | ~41 | P2 | full | P2C03–P2C04 | groomed beard, hair bound by a gold diadem (kirīṭa) from Indra, white-and-gold celestial garments, gold-scaled cuirass |
| ARJ_G | CH_ARJUNA | Bṛhannaḍā | 48 | P2 | full | P2C05–P2C06 | in a woman's guise: long braided hair, large earrings, many conch-shell and gold bangles hiding the bowstring scars, red-bordered woman's garment, kohl-lined eyes, clean-shaven |
| ARJ_H | CH_ARJUNA | Kirīṭī (war) | 48–49 | P2,P3 | full | P2C06 (after reveal), P2C08, P3C01–P3C07 | short beard with first grey at the temples, white cloth tied over the hair under the gold diadem, bronze-scaled armour over quilted cotton, two great quivers, Gāṇḍīva; Devadatta conch |
| ARJ_I | CH_ARJUNA | Rāja (Upaplavya / Hastinapura) | 48–55 | P2,P3 | full | P2C06–P2C08, P3C08 | trimmed beard with grey at the temples, gold diadem, white wild-silk garments with a gold border, gold armlets |
| ARJ_J | CH_ARJUNA | Vṛddha | ~85 | P3 | full | P3C08 | white beard and hair, lean, slightly stooped, bark-cloth garments, Gāṇḍīva now heavy in his hands |
| KRN_A | CH_KARNA | Śiśu (newborn) | newborn | P1 | creature | P1C02 | newborn boy with living golden armour grown on his chest like fine skin-scales and two softly glowing earrings — organic, not metal plates |
| KRN_B | CH_KARNA | Kavacadhārī yuvā | 24–30 | P1 | full | P1C03–P1C05 | light stubble, hair loose to the shoulders, born-with golden armour covering chest and back like living gold scales that move with breath, two earrings of light on his face; plain white lower garment before the coronation, red-and-gold Aṅga royal garments after |
| KRN_C | CH_KARNA | Aṅgarāja (mature, armoured) | 40–54 | P1,P2 | full | P1C06–P1C07, P2C04–P2C05 | short beard, hair tied back, the same living golden armour and earrings, crimson-and-gold Aṅga royal garments, gold armlets; bow Vijaya |
| KRN_D | CH_KARNA | Vaikartana (after the cutting) | 54–55 | P2,P3 | full | P2C05, P2C07–P2C08, P3C03, P3C08 | short beard, bare unscarred chest with a faint sunlit radiance, simple white and saffron garments, no armour, bare whole earlobes |
| KRN_E | CH_KARNA | Senāpati (war) | 55 | P3 | full | P3C03–P3C06 | beard, hair bound under a bronze helmet-band, ordinary bronze-scaled armour, quiver, bow Vijaya; banner of a golden elephant-girth rope |
| DRP_A | CH_DRAUPADI | Yājñasenī (fire-born, bride) | ~18 | P1 | full | P1C05 | rising from a fire altar: hair loose and curling, single unbleached cotton garment, ash on the shoulders, no jewellery; as bride: red-bordered silk and a white garland |
| DRP_B | CH_DRAUPADI | Samrājñī (Indraprastha) | 20–35 | P1 | full | P1C05–P1C06 | hair in a heavy coiled braid with flowers, indigo-and-gold wild silk, gold ornaments, gold hair ornament at the parting |
| DRP_C | CH_DRAUPADI | Ekavastrā (Sabhā) | ~35 | P1 | full | P1C07 | one plain cotton garment (she is in her period), hair loose and dishevelled from being dragged, no ornaments, red-rimmed furious eyes; at the departure the garment wet and blood-stained |
| DRP_D | CH_DRAUPADI | Vanavāsinī | 36–48 | P1,P2 | full | P1C07 (end), P2C01–P2C05 | long hair unbound, bark-cloth and deerskin garments, one bead string, sun-darkened face, burning eyes |
| DRP_E | CH_DRAUPADI | Sairandhrī | 48 | P2 | full | P2C05–P2C06 | palace maid: hair in a plain single braid, coarse ochre cotton, sandal-paste stains, calloused cracked palms, no gold |
| DRP_F | CH_DRAUPADI | Udyoga | 48–49 | P2 | full | P2C06–P2C08 | royal again: dark-blue silk with a gold border, gold ornaments, but her long hair held loose; she holds a lock of it in her left hand |
| DRP_G | CH_DRAUPADI | Putrahīnā (mourning) | ~50 | P3 | full | P3C07–P3C08 | white mourning cotton, hair loose and dusted with ash, hollow eyes, no ornaments |
| DRP_H | CH_DRAUPADI | Mahāprasthāna | ~83 | P3 | full | P3C08 | white hair still long, bark-cloth garments, frail but upright |
| YUD_A | CH_YUDHISHTHIRA | Bālaka | ~14 | P1 | full | P1C02–P1C03 | serious golden-fair boy, hair in a knot, white cotton |
| YUD_B | CH_YUDHISHTHIRA | Yuvā | 18–21 | P1 | full | P1C03–P1C04 | first beard, hair tied with a white band, white cotton with a thin gold border, spear |
| YUD_C | CH_YUDHISHTHIRA | Vipra disguise | ~22 | P1 | full | P1C04–P1C05 | short beard, brahmin's hair-knot, black deerskin upper wrap, white lower cloth, sacred thread, ash marks |
| YUD_D | CH_YUDHISHTHIRA | Dharmarāja (Indraprastha) | 23–37 | P1 | full | P1C05–P1C07 | full neat beard, gold diadem, white wild-silk garments with a gold border, a string of pearls, calm hands |
| YUD_E | CH_YUDHISHTHIRA | Vanavāsī | 37–49 | P1,P2 | full | P1C07 (end), P2C01–P2C05 | long beard, matted hair tied up, black deerskin and bark, no jewellery |
| YUD_F | CH_YUDHISHTHIRA | Kaṅka | 49 | P2 | full | P2C05–P2C06 | brahmin dice-companion: hair in a brahmin's knot, white cotton lower garment and upper cloth, sacred thread, golden beryl-like dice wrapped in cloth under his arm |
| YUD_G | CH_YUDHISHTHIRA | Rāja (Upaplavya / Hastinapura) | 49–55 | P2,P3 | full | P2C06–P2C08, P3C08 | grey-flecked beard, gold diadem, white silk with a gold border |
| YUD_H | CH_YUDHISHTHIRA | War | 50 | P2,P3 | full | P2C08, P3C01–P3C07 | grey-flecked beard, bronze-scaled armour, spear, gold diadem |
| YUD_I | CH_YUDHISHTHIRA | Mahāprasthāna | ~88 | P3 | full | P3C08 | long white beard and hair, bark-cloth garments, walking staff, serene |
| BHM_A | CH_BHIMA | Bālaka | 12–13 | P1 | full | P1C02–P1C03 | boy already as big as a man, golden-fair, laughing, white cotton, mud on the knees |
| BHM_B | CH_BHIMA | Yuvā | 17–21 | P1 | full | P1C03–P1C04 | huge youth, beard coming in, white cotton lower garment, leather belt, mace |
| BHM_C | CH_BHIMA | Vipra disguise | ~21 | P1 | full | P1C04–P1C05 | huge, beard, brahmin's hair-knot, black deerskin, sacred thread, ash marks, a tree-branch staff |
| BHM_D | CH_BHIMA | Rājakumāra | 22–36 | P1 | full | P1C05–P1C07 | thick curly beard, hair tied back with a red band, red-and-white cotton, gold armlets on huge arms, giant iron mace |
| BHM_E | CH_BHIMA | Vanavāsī | 36–48 | P1,P2 | full | P1C07 (end), P2C01–P2C05 | wild beard and long matted hair, black deerskin and bark, mace |
| BHM_F | CH_BHIMA | Ballava (cook) | 48 | P2 | full | P2C05–P2C06 | palace cook: dark-stained cotton wrap, soot on the forearms, iron ladle, hair tied in a rag |
| BHM_G | CH_BHIMA | Rāja | 48–55 | P2,P3 | full | P2C06–P2C08, P3C08 | beard, red-and-gold silk, gold armlets |
| BHM_H | CH_BHIMA | War | 49 | P2,P3 | full | P2C08, P3C01–P3C07 | beard, bronze-scaled armour on a colossal frame, iron mace, lion banner |
| BHM_I | CH_BHIMA | Mahāprasthāna | ~87 | P3 | full | P3C08 | still huge but slowed, white beard, bark garments |
| NAK_A | CH_NAKULA | Bālaka | ~11 | P1 | full | P1C02–P1C03 | beautiful fair boy, wavy hair, white cotton |
| NAK_B | CH_NAKULA | Yuvā | 16–20 | P1 | full | P1C03–P1C04 | beardless, wavy hair tied loosely, white cotton, sword |
| NAK_C | CH_NAKULA | Vipra disguise | ~20 | P1 | full | P1C04–P1C05 | black deerskin, sacred thread, ash marks, light beard |
| NAK_D | CH_NAKULA | Rājakumāra | 21–35 | P1 | full | P1C05–P1C07 | elegant trimmed beard, blue-and-white silk, gold ornaments, sword |
| NAK_E | CH_NAKULA | Vanavāsī | 35–47 | P1,P2 | full | P1C07 (end), P2C01–P2C05 | bark and deerskin, hair tied up, beard |
| NAK_F | CH_NAKULA | Granthika (horse-master) | 47 | P2 | full | P2C05–P2C06 | stable-master's leather apron and cotton wrap, horse-whip, hair tied in a cloth |
| NAK_G | CH_NAKULA | Rāja | 47–54 | P2,P3 | full | P2C06–P2C08, P3C08 | blue-and-gold silk, trimmed beard |
| NAK_H | CH_NAKULA | War | 48 | P2,P3 | full | P2C08, P3C01–P3C07 | bronze armour, sword and shield, bow |
| NAK_I | CH_NAKULA | Mahāprasthāna | ~86 | P3 | full | P3C08 | white hair and beard, still handsome, bark garments |
| SAH_A | CH_SAHADEVA | Bālaka | ~11 | P1 | full | P1C02–P1C03 | fair boy with a serious face, straight hair in a knot, white cotton |
| SAH_B | CH_SAHADEVA | Yuvā | 16–20 | P1 | full | P1C03–P1C04 | beardless, tight hair-knot, white cotton, sword |
| SAH_C | CH_SAHADEVA | Vipra disguise | ~20 | P1 | full | P1C04–P1C05 | black deerskin, sacred thread, ash marks, light beard |
| SAH_D | CH_SAHADEVA | Rājakumāra | 21–35 | P1 | full | P1C05–P1C07 | close-cropped beard, white-and-ochre silk, a single gold earring, sword |
| SAH_E | CH_SAHADEVA | Vanavāsī | 35–47 | P1,P2 | full | P1C07 (end), P2C01–P2C05 | bark and deerskin, tight knot, beard; face smeared with dust at the departure |
| SAH_F | CH_SAHADEVA | Tantipāla (cowherd) | 47 | P2 | full | P2C05–P2C06 | cowherd's coarse wrap, staff, rope coil on the shoulder |
| SAH_G | CH_SAHADEVA | Rāja | 47–54 | P2,P3 | full | P2C06–P2C08, P3C08 | white-and-ochre silk, close beard |
| SAH_H | CH_SAHADEVA | War | 48 | P2,P3 | full | P2C08, P3C01–P3C07 | bronze armour, sword, bow |
| SAH_I | CH_SAHADEVA | Mahāprasthāna | ~86 | P3 | full | P3C08 | white hair, bark garments |
| DUR_A | CH_DURYODHANA | Bālaka | 12–13 | P1 | full | P1C02–P1C03 | sturdy watchful boy, black hair, fine cotton with gold edges |
| DUR_B | CH_DURYODHANA | Yuvā | 17–22 | P1 | full | P1C03–P1C04 | beard coming in, red-and-black silk, gold armlets, mace |
| DUR_C | CH_DURYODHANA | Yuvarāja (Sabhā era) | 23–36 | P1 | full | P1C05–P1C07 | thick moustache and short beard, jewelled diadem, crimson-and-black silk, heavy gold ornaments |
| DUR_D | CH_DURYODHANA | Rājā (forest years, Udyoga) | 37–49 | P2,P3 | full | P2C04, P2C06–P2C08, P3C08 (heaven) | moustache with grey, jewelled diadem, black-and-gold silk, a gold serpent ornament on the armlet |
| DUR_E | CH_DURYODHANA | War | 50 | P3 | full | P3C01–P3C07 | bronze-scaled armour, huge iron mace on the shoulder, jewelled serpent banner with hundreds of bells |
| KUN_A | CH_KUNTI | Kanyā | ~15 | P1 | full | P1C02 | slender girl, hair in a long braid, plain palace cotton |
| KUN_B | CH_KUNTI | Rānī / Mātā | 20–32 | P1 | full | P1C02 | queen in red-and-gold cotton, then forest cotton, hair in a coiled braid |
| KUN_C | CH_KUNTI | Vidhavā | 33–45 | P1 | full | P1C02–P1C05 | widow's plain white cotton, no ornaments, hair pulled back |
| KUN_D | CH_KUNTI | Rājamātā | 55–72 | P1,P2,P3 | full | P1C07, P2C07–P2C08, P3C06–P3C08 | grey streaks, plain white widow's cotton, a fine shawl, upright |
| KUN_E | CH_KUNTI | Vanavāsinī | ~85 | P3 | full | P3C08 | white hair, bark cloth, frail, luminous calm |
| DHR_A | CH_DHRITARASHTRA | Yuvā | 22–30 | P1 | full | P1C02 | huge young prince, black beard, white-and-gold silk, unseeing eyes |
| DHR_B | CH_DHRITARASHTRA | Rājā | 50–66 | P1 | full | P1C03–P1C07 | greying beard, gold diadem, heavy gold ornaments, crimson silk |
| DHR_C | CH_DHRITARASHTRA | Vṛddha | 78–95 | P2,P3 | full | P2C01, P2C07, P3C01–P3C08 | white beard, gaunt but still huge, plain white silk; in the forest bark cloth |
| GAN_A | CH_GANDHARI | Vadhū | ~16 | P1 | full | P1C02 | bride in Gandhāra wool-and-silk, silver ornaments, the folded dark blindfold just tied |
| GAN_B | CH_GANDHARI | Rājñī | 30–66 | P1,P2 | full | P1C02–P1C07, P2C07 | dark wine-red silk, gold ornaments, the folded blindfold |
| GAN_C | CH_GANDHARI | Mother of the dead | 76–92 | P3 | full | P3C08 | white widow's cotton, the folded blindfold, grey hair |
| SHK_A | CH_SHAKUNI | Yuvā | ~18 | P1 | full | P1C02 | Gandhāra wool cloak over a silk tunic, silver earrings, clean-shaven |
| SHK_B | CH_SHAKUNI | Saubala | 55–75 | P1,P2,P3 | full | P1C06–P1C07, P2C04, P2C07, P3C02–P3C07 | grey pointed beard, dark wool shawl over black silk, silver rings, dice pouch at the belt |
| VID_A | CH_VIDURA | Yuvā | 22–30 | P1 | full | P1C02 | plain white cotton, short beard, a minister's simple shawl |
| VID_B | CH_VIDURA | Kṣattā (minister) | 45–76 | P1,P2 | full | P1C03–P1C07, P2C01, P2C07 | greying beard, plain white cotton, brown shawl |
| VID_C | CH_VIDURA | Mahātmā (forest) | ~95 | P3 | full | P3C08 | skeleton-thin, naked but for a loincloth, matted white hair, leaning on a tree |
| DRO_A | CH_DRONA | Young (flashback) | ~18 | P1 | single | P1C03 | thin dark young brahmin, āśrama cotton |
| DRO_B | CH_DRONA | Poor brahmin | ~50 | P1 | full | P1C03 | gaunt, dark, threadbare white cloth, sacred thread, a bundle of reeds |
| DRO_C | CH_DRONA | Ācārya | 54–72 | P1,P2 | full | P1C03–P1C07, P2C07 | grey hair, dark skin, white cotton, sacred thread, bow, deerskin over the shoulder |
| DRO_D | CH_DRONA | War (85) | 84–85 | P2,P3 | full | P2C06, P2C08, P3C01–P3C05 | grey-white hair down to the ears, dark skin, armour over white cotton; banner of a golden altar with a black deerskin; red horses |
| VYA_A | CH_VYASA | Niyoga | ~30 | P1 | full | P1C02 | matted tawny hair piled high, rough tawny beard, bark-cloth lower garment, smoke-darkened skin |
| VYA_B | CH_VYASA | Maharṣi | ageless | P1,P2,P3 | full | P1C01, P1C02, P1C05, P2C02, P3C01, P3C07, P3C08 | tawny matted locks streaked with white, long tawny-white beard, bark cloth and black deerskin, wooden water-pot, barefoot |
| SNJ_A | CH_SANJAYA | Sūta (court) | 50–62 | P1,P2 | full | P1C07, P2C01, P2C07 | white cotton, upper cloth, no weapon |
| SNJ_B | CH_SANJAYA | Divya-dṛṣṭi narrator | ~63 | P3 | full | P3C01–P3C08 | same garments, battlefield dust on face and shoulders, eyes that have seen too much |
| JAN_A | CH_JANAMEJAYA | Dīkṣita | ~25 | P1,P2,P3 | full | P1C01, P2C01, P3C08 | black antelope-skin upper wrap, plain white lower cloth, sacred thread, ash on the forehead |
| VAI_A | CH_VAISHAMPAYANA | Kathāvācaka | ~58 | P1,P2,P3 | full | P1C01, P2C01, P3C08 | plain ochre cotton, sacred thread, a string of dark wooden beads, clay ladle |
| SUT_A | CH_SUTRADHARA | — | ~70 | P1 | single | P1C01 | white cotton, knotted measuring rope coiled on the shoulder |
| AST_A | CH_ASTIKA | Bāla-muni | 12 | P1,P3 | single | P1C01 (glimpse), P3C08 | white cotton, sacred thread, small staff |
| GNG_A | CH_GANGA | Devī | ageless | P1,P3 | full | P1C01, P3C08 | wet unbleached silk, river-pearl ornaments, water dripping, never fully dry |
| SHN_A | CH_SHANTANU | Rājā | ~42 | P1 | full | P1C01 | black beard, gold diadem, white-and-red silk, hunting bow |
| SHN_B | CH_SHANTANU | Vṛddha rājā | ~76 | P1 | full | P1C01 | grey hair and beard, still a vigorous hunter, faded royal cotton, gold armlet |
| SVT_A | CH_SATYAVATI | Dāśeyī (ferry-girl) | 18 | P1 | full | P1C01 | thick braid, coarse indigo cotton tied for work, shell bangles, wet ankles, a punting pole |
| SVT_B | CH_SATYAVATI | Rājamātā | ~44 | P1 | full | P1C02 | white-and-gold royal silk, gold ornaments, coiled braid, hard grief in the eyes |
| SVT_C | CH_SATYAVATI | Vanagāminī | ~80 | P1 | full | P1C02 | white hair, plain white widow's cotton, walking staff |
| DAS_A | CH_DASHARAJA | — | ~55 | P1 | single | P1C01 | coarse brown cotton, shell-and-bone necklace, fish-oil sheen on the forearms |
| MIN_A | CH_MINISTER_OLD | — | ~70 | P1 | single | P1C01 | white court cotton, staff of office |
| CKR_A | CH_CHITRANGADA_KURU | — | 19 | P1 | single | P1C02 | gold diadem, red silk, sword |
| GCH_A | CH_GANDHARVA_CHITRANGADA | — | ageless | P1 | single | P1C02 | pale misty garments, curved sword |
| AMB_A | CH_AMBA | Kāśī princess | 17 | P1,P2 | full | P1C02, P2C08 | red-and-gold bridal silk, gold ornaments, jasmine in the braid |
| AMB_B | CH_AMBA | Tapasvinī | ~22 | P2 | full | P2C08 | emaciated, matted hair, bark cloth, ash, burning eyes |
| AMK_A | CH_AMBIKA | — | ~20 | P1 | group:GRP_KASHI | P1C02 | bridal silk at Kāśī; white widow's silk at the niyoga |
| AML_A | CH_AMBALIKA | — | ~18 | P1 | group:GRP_KASHI | P1C02 | bridal silk at Kāśī; white widow's silk at the niyoga |
| SLV_A | CH_SHALVA | — | ~30 | P1,P2 | single | P1C02, P2C08 | bronze armour, red cloak |
| VCV_A | CH_VICHITRAVIRYA | — | ~23 | P1 | single | P1C02 | fine white silk, gold diadem, white linen cloth at the mouth |
| DSI_A | CH_DASI | — | ~20 | P1 | single | P1C02 | Ambikā's jewels over a plain cotton garment |
| PAN_A | CH_PANDU | Rājā | ~25 | P1 | full | P1C02 | gold diadem, white silk, bow |
| PAN_B | CH_PANDU | Vanavāsī | ~35 | P1 | full | P1C02 | short beard, bark cloth and deerskin, no crown, hunting bow |
| DVS_A | CH_DURVASAS | — | ~70 | P1 | single | P1C02 | bark cloth, ash-smeared, staff |
| SUR_A | CH_SURYA | — | ageless | P1,P2 | vfx | P1C02, P2C01, P2C05, P2C08 | golden-white radiance, gold ornaments glimpsed inside the light |
| RDH_A | CH_RADHA | — | ~25 | P1 | single | P1C02 | simple ochre cotton, washing at the ghat |
| ADH_A | CH_ADHIRATHA | Young sārathi | ~30 | P1 | single | P1C02 | cotton wrap, leather belt, whip |
| ADH_B | CH_ADHIRATHA | Vṛddha | ~55 | P1 | single | P1C04 | upper cloth slipping, sweating, walking stick, grey beard |
| MDR_A | CH_MADRI | — | ~24 | P1 | full | P1C02 | silk at court; forest cotton at Śataśṛṅga; flowers in her hair at the stream |
| RSS_A | CH_RISHI_SHATASHRINGA | — | ~80 | P1 | single | P1C02 | bark cloth, staff |
| DUH_A | CH_DUHSHASANA | Bālaka | ~12 | P1 | single | P1C03 | white cotton, mud |
| DUH_B | CH_DUHSHASANA | Yuvā / Sabhā | 20–35 | P1,P2 | full | P1C04, P1C07, P2C04, P2C07 | red-and-black silk, gold ornaments, sword |
| DUH_C | CH_DUHSHASANA | War | ~48 | P3 | full | P3C02–P3C06 | bronze armour, sword, mace |
| VIK_A | CH_VIKARNA | — | ~28 | P1 | single | P1C07 | white-and-saffron silk |
| YUY_A | CH_YUYUTSU | Bālaka | ~13 | P1 | single | P1C03 | plain cotton |
| YUY_B | CH_YUYUTSU | Warrior | ~50 | P3 | single | P3C01, P3C08 | bronze armour, spear |
| KRP_A | CH_KRIPA | Ācārya | appears ~60 | P1 | full | P1C04, P1C07 | grey beard, white cotton, sacred thread, bow |
| KRP_B | CH_KRIPA | War | appears ~80 | P2,P3 | full | P2C06, P3C01–P3C07 | white beard, armour; bull banner |
| KPI_A | CH_KRIPI | — | ~30 | P1 | single | P1C03 | coarse white cotton |
| ASW_A | CH_ASHVATTHAMA | Yuvā | ~18 | P1 | single | P1C04 | white cotton, bow, the forehead jewel |
| ASW_B | CH_ASHVATTHAMA | War | ~48 | P2,P3 | full | P2C06, P3C01–P3C07 | bronze armour, the jewel on the forehead catching light, lion's-tail banner |
| ASW_C | CH_ASHVATTHAMA | Cursed | ~48 | P3 | full | P3C07 | the jewel cut out — raw bleeding wound in the forehead, torn armour, matted hair |
| EKL_A | CH_EKALAVYA | — | ~18 | P1 | full | P1C03 | black deerskin, mud-smeared limbs, matted hair, forest-wood bow |
| DRU_A | CH_DRUPADA | Young (flashback) | ~18 | P1 | single | P1C03 | āśrama white cotton |
| DRU_B | CH_DRUPADA | Rājā | ~55 | P1 | full | P1C04–P1C05 | gold diadem, red-gold silk |
| DRU_C | CH_DRUPADA | Vṛddha (war) | ~85 | P2,P3 | full | P2C07–P2C08, P3C01–P3C05 | white beard, armour |
| DHD_A | CH_DHRISHTADYUMNA | Agnija | ~20 | P1 | full | P1C05 | armour and bow as he steps from the fire, ash on the skin |
| DHD_B | CH_DHRISHTADYUMNA | Senāpati | ~48 | P2,P3 | full | P2C08, P3C01–P3C07 | bronze armour, sword, commander's banner |
| SKH_A | CH_SHIKHANDI | Śikhaṇḍinī → Śikhaṇḍin | ~20 | P2 | single | P2C08 | first a girl's garments, then a warrior's |
| SKH_B | CH_SHIKHANDI | War | ~45 | P3 | full | P3C02–P3C03, P3C07 | bronze armour, bow |
| YAJ_A | CH_YAJA | — | ~60 | P1 | group:GRP_YAJA | P1C05 | bark and white cotton, ash |
| UPY_A | CH_UPAYAJA | — | ~50 | P1 | group:GRP_YAJA | P1C05 | bark and white cotton, ash |
| DHM_A | CH_DHAUMYA | — | ~50 | P1,P2,P3 | full | P1C05–P1C07, P2C01–P2C05, P3C08 | white cotton, sacred thread, kuśa grass in hand |
| ANG_A | CH_ANGARAPARNA | — | ageless | P1 | group:GRP_GANDHARVA | P1C05 | silver-edged silks, chariot of painted wood |
| KMB_A | CH_KUMBHINASI | — | ageless | P1 | group:GRP_GANDHARVA | P1C05 | pale silks |
| BAL_A | CH_BALARAMA | Yuvā | ~28 | P1 | full | P1C05 | dark-blue garments, plough-weapon (hala), gold armlets |
| BAL_B | CH_BALARAMA | Mature | ~52 | P2,P3 | full | P2C07–P2C08, P3C07 | dark-blue garments, plough-weapon, white streaks in the hair |
| BAL_C | CH_BALARAMA | Vṛddha (Prabhāsa) | ~87 | P3 | single | P3C08 | white hair, dark-blue garment, sitting under a tree |
| SHL_A | CH_SHALYA | — | ~40 | P1 | single | P1C05 | royal armour |
| SHL_B | CH_SHALYA | — | ~65 | P2,P3 | full | P2C07, P3C06–P3C07 | grey moustache, armour, golden ploughshare banner |
| BRO_A | CH_BRAHMIN_OLD | — | ~70 | P1 | group:GRP_SVAYAMVARA_BRAHMINS | P1C05 | deerskin, white tuft |
| BRY_A | CH_BRAHMIN_YOUNG | — | ~25 | P1 | group:GRP_SVAYAMVARA_BRAHMINS | P1C05 | deerskin, eager |
| NRD_A | CH_NARADA | — | ageless | P1,P3 | full | P1C05–P1C07, P3C07 | white garments, a simple arched vīṇā, sacred thread |
| BRB_A | CH_BRAHMIN_ROBBED | — | ~65 | P1 | single | P1C05 | torn white cotton |
| ULP_A | CH_ULUPI | Yuvatī | ~20 | P1 | full | P1C05 | river-green silk, pearl and shell ornaments, wet hair |
| ULP_B | CH_ULUPI | Mātā | ~45 | P3 | single | P3C08 | same palette, matronly |
| KRV_A | CH_KAURAVYA | — | old | P1 | single | P1C05 | pearl-and-shell regalia |
| CTV_A | CH_CHITRAVAHANA | — | ~55 | P1 | single | P1C05 | eastern-coast silk |
| CTR_A | CH_CHITRANGADAA | Yuvatī | ~20 | P1 | single | P1C05 | eastern-coast silk, shell ornaments |
| CTR_B | CH_CHITRANGADAA | Mātā | ~45 | P3 | single | P3C08 | matronly, same palette |
| VRG_A | CH_VARGA | — | ageless | P1 | single | P1C05 | water-soaked pale silks |
| SUB_A | CH_SUBHADRA | Kanyā | ~18 | P1 | full | P1C05 | festival silk in saffron-red, flower garlands |
| SUB_B | CH_SUBHADRA | Mātā | ~50 | P3 | full | P3C04, P3C08 | white mourning cotton |
| ABH_A | CH_ABHIMANYU | — | 16 | P2,P3 | full | P2C06–P2C08, P3C04, P3C08 | bronze-scaled armour, bow, gold earrings; at the wedding white silk |
| UPP_PRA | CH_PRATIVINDHYA | — | ~25 | P2,P3 | group:GRP_UPAPANDAVA | P2C08, P3C07–P3C08 | armour, bow |
| UPP_SUT | CH_SUTASOMA | — | ~24 | P2,P3 | group:GRP_UPAPANDAVA | P2C08, P3C07–P3C08 | armour, mace |
| UPP_SKR | CH_SHRUTAKARMAN | — | ~23 | P2,P3 | group:GRP_UPAPANDAVA | P2C08, P3C07–P3C08 | armour, bow |
| UPP_STN | CH_SHATANIKA | — | ~22 | P2,P3 | group:GRP_UPAPANDAVA | P2C08, P3C07–P3C08 | armour, sword |
| UPP_SSN | CH_SHRUTASENA | — | ~21 | P2,P3 | group:GRP_UPAPANDAVA | P2C08, P3C07–P3C08 | armour, sword |
| AGN_A | CH_AGNI | — | ageless | P1,P3 | full | P1C05–P1C06, P3C08 | red-gold cotton, ash, matted tawny hair, heat-shimmer |
| MAY_A | CH_MAYA | — | ageless | P1 | full | P1C06 | soot-stained leather apron, measuring rods, bronze tools |
| JRS_A | CH_JARASANDHA | — | ~55 | P1 | full | P1C06 | wrestler's loincloth, oil, scars, the seam |
| JRK_A | CH_JARA_RAKSHASI | — | ageless | P1 | single | P1C06 | ragged forest dress |
| MGP_A | CH_MAGADHA_PRINCE | — | ~20 | P1 | single | P1C06 | Magadha silk |
| SHP_A | CH_SHISHUPALA | — | ~35 | P1 | full | P1C06 | royal Cedi silk, jewelled diadem |
| PRK_A | CH_PRATIKAMIN | — | ~40 | P1 | single | P1C07 | messenger's plain cotton |
| PUR_A | CH_PUROCHANA | — | ~45 | P1 | single | P1C04 | fine cotton, rings |
| MIN2_A | CH_MINER | — | ~35 | P1 | single | P1C04 | earth-caked loincloth, digging tools |
| NSD_A | CH_NISHADI | — | ~40 | P1 | single | P1C04 | forest cloth |
| EKB_A | CH_EKACHAKRA_BRAHMIN | — | ~45 | P1 | group:GRP_EKACHAKRA | P1C05 | threadbare white cotton |
| EKW_A | CH_EKACHAKRA_WIFE | — | ~38 | P1 | group:GRP_EKACHAKRA | P1C05 | threadbare cotton |
| EKD_A | CH_EKACHAKRA_DAUGHTER | — | ~14 | P1 | group:GRP_EKACHAKRA | P1C05 | threadbare cotton |
| HDM_A | CH_HIDIMBA | — | ageless | P1 | full | P1C05 | hide loincloth, bones, matted hair |
| HDB_A | CH_HIDIMBI | — | ageless | P1 | full | P1C05 | forest-flower ornaments, red cloth |
| GHT_A | CH_GHATOTKACHA | — | ageless | P1,P2,P3 | full | P1C05, P2C03, P3C02, P3C05, P3C08 | black leather and bronze, huge bow; in war iron armour hung with bells |
| BAK_A | CH_BAKA | — | ageless | P1 | single | P1C05 | hide wrap |
| KRM_A | CH_KIRMIRA | — | ageless | P2 | single | P2C01 | hide wrap, bone ornaments |
| MTY_A | CH_MAITREYA | — | ~70 | P2 | single | P2C01 | bark cloth |
| IND_A | CH_INDRA | Jaṭila tapasvī (disguise) | old | P2 | single | P2C02 | matted-haired old ascetic, bark cloth |
| IND_B | CH_INDRA | Devarāja | ageless | P2,P3 | full | P2C02–P2C03, P3C08 | gold diadem, white-and-gold garments, short golden vajra |
| IND_C | CH_INDRA | Brāhmaṇa (kavaca) | old | P2 | single | P2C05 | old brahmin, white beard, begging bowl, sly eyes |
| SHV_A | CH_SHIVA | Kirāta | ageless | P2 | full | P2C02 | immense hunter radiant like a golden tree, wild hair bound with vines, hunter's garb, great bow, serpent-like arrows |
| SHV_B | CH_SHIVA | Mahādeva | ageless | P2,P3 | full | P2C02, P3C04, P3C07 | calm ancient face, ash-pale skin, matted locks piled high, bow Pināka, a faint vertical mark on the brow |
| UMA_A | CH_UMA | — | ageless | P2 | single | P2C02 | hunter-woman's garb matching the Kirāta |
| YAM_A | CH_YAMA | — | ageless | P2 | group:GRP_LOKAPALA | P2C02 | dark robes, noose |
| VRN_A | CH_VARUNA | — | ageless | P2 | group:GRP_LOKAPALA | P2C02 | sea-dark robes, noose of rope and pearls |
| KUB_A | CH_KUBERA | — | ageless | P2 | group:GRP_LOKAPALA | P2C02 | gold robes, heavy necklace |
| MTL_A | CH_MATALI | — | ageless | P2 | full | P2C02–P2C04 | white-and-gold charioteer's garments |
| CTS_A | CH_CHITRASENA | — | ageless | P2 | full | P2C03–P2C04 | flowing pale silks, vīṇā; silver armour in battle |
| URV_A | CH_URVASHI | — | ageless | P2 | single | P2C03 | dancer's silks |
| BRH_A | CH_BRIHADASHVA | — | ~70 | P2 | single | P2C03 | bark cloth |
| LMS_A | CH_LOMASHA | — | ~70 | P2 | single | P2C03 | bark cloth, hairy arms, staff |
| HAN_A | CH_HANUMAN | Vṛddha vānara | ancient | P2 | full | P2C03 | lying on a broad stone slab in a banana grove, very old, grey-tawny fur, tail across the path |
| JTS_A | CH_JATASURA | — | ageless | P2 | single | P2C03 | brahmin's garb over a rākṣasa body |
| NAH_A | CH_NAHUSHA | Freed king | ageless | P2 | single | P2C04 | radiant old king in white |
| JYD_A | CH_JAYADRATHA | Sindhu-rāja | ~45 | P2 | full | P2C04 | royal Sindhu silks, oiled curls (state +shaved: head shaved leaving five tufts) |
| JYD_B | CH_JAYADRATHA | War | ~46 | P3 | full | P3C04 | armour, silver boar banner |
| DHA_A | CH_DHARMA | Yakṣa | ageless | P2 | vfx | P2C05 | palm-tree-tall figure, misshapen eyes, body blazing like fire and sun, standing against a dam of stones |
| DHA_B | CH_DHARMA | Dharmadeva | ageless | P2,P3 | full | P2C05, P3C08 | calm elder in dark-blue robes, white beard, staff |
| BRA_A | CH_BRAHMIN_ARANI | — | ~50 | P2 | single | P2C05 | white cotton |
| VRT_A | CH_VIRATA | Rājā | ~70 | P2 | full | P2C05–P2C07 | Matsya royal silk, gold ornaments |
| VRT_B | CH_VIRATA | War | ~71 | P3 | single | P3C01–P3C05 | armour |
| SDS_A | CH_SUDESHNA | — | ~45 | P2 | full | P2C05–P2C06 | Matsya royal silk |
| KCK_A | CH_KICHAKA | — | ~40 | P2 | full | P2C05–P2C06 | perfumed silks, garlands, gold |
| UTR_A | CH_UTTARA | — | ~16 | P2,P3 | full | P2C06, P3C02 | young prince's silks; armour at Kurukṣetra |
| UTA_A | CH_UTTARAA | Rājakumārī | ~15 | P2 | full | P2C06–P2C07 | golden-fair princess, Matsya silk, dolls |
| UTA_B | CH_UTTARAA | Vidhavā-mātā | ~17 | P3 | full | P3C04, P3C08 | white mourning cotton, pregnant |
| SSM_A | CH_SUSHARMAN | — | ~50 | P2,P3 | single | P2C06, P3C03–P3C04 | Trigarta armour |
| SYK_A | CH_SATYAKI | — | ~45 | P2,P3 | full | P2C07–P2C08, P3C01–P3C07 | Vṛṣṇi armour |
| SYK_B | CH_SATYAKI | Vṛddha | ~85 | P3 | single | P3C08 | drunk, old |
| KTV_A | CH_KRITAVARMAN | — | ~48 | P2,P3 | full | P2C07, P3C01–P3C07 | Bhoja armour |
| KTV_B | CH_KRITAVARMAN | Vṛddha | ~84 | P3 | single | P3C08 | drunk, old |
| ULK_A | CH_ULUKA | — | ~35 | P2 | single | P2C08 | envoy's silks |
| PRM_A | CH_PARASHURAMA | — | ancient | P2,P3 | full | P2C08, P3C06 | black deerskin, axe, bow, ash |
| STK_A | CH_STHUNAKARNA | — | ageless | P2 | single | P2C08 | forest-yakṣa garb |
| SNT_A | CH_SANATSUJATA | — | ageless | P2 | single | P2C07 | a boy's body, an old man's eyes, bark cloth |
| SVT2_A | CH_SHVETA | — | ~25 | P3 | single | P3C02 | Matsya armour |
| BHU_A | CH_BHURISHRAVAS | — | ~70 | P3 | full | P3C02, P3C04 | armour; banner of a golden sacrificial post |
| IRV_A | CH_IRAVAT | — | ~20 | P3 | single | P3C02 | light armour |
| ALM_A | CH_ALAMBUSHA | — | ageless | P3 | single | P3C02, P3C05 | black armour |
| BGD_A | CH_BHAGADATTA | — | ancient | P3 | full | P3C03 | armour, goad, on the elephant Supratīka |
| LKM_A | CH_LAKSHMANA_K | — | ~18 | P3 | single | P3C04 | gold armour |
| DSN_A | CH_DAUSHASANI | — | ~20 | P3 | single | P3C04 | bronze armour, mace |
| VDK_A | CH_VRIDDHAKSHATRA | — | ~90 | P3 | single | P3C04 | white robes, praying |
| UTM_A | CH_UTTAMAUJAS | — | ~30 | P3 | group:GRP_PANCHALA | P3C07 | armour |
| YDM_A | CH_YUDHAMANYU | — | ~30 | P3 | group:GRP_PANCHALA | P3C07 | armour |
| CRV_A | CH_CHARVAKA | — | ageless | P3 | single | P3C08 | brahmin's garb |
| PKT_A | CH_PARIKSHIT | Yuvā rājā | ~36 | P3 | single | P3C08 | gold diadem, white silk |
| BBV_A | CH_BABHRUVAHANA | — | ~25 | P3 | single | P3C08 | Maṇalūra armour |
| SMB_A | CH_SAMBA | — | ~22 | P3 | single | P3C08 | disguised as a pregnant woman (state); Yādava silks |
| VSM_A | CH_VISHVAMITRA | — | ancient | P3 | group:GRP_MAUSALA_SAGES | P3C08 | bark cloth |
| KNV_A | CH_KANVA | — | ancient | P3 | group:GRP_MAUSALA_SAGES | P3C08 | bark cloth |
| JRH_A | CH_JARA_HUNTER | — | ~35 | P3 | single | P3C08 | hunter's loincloth, bow |
| VJR_A | CH_VAJRA | — | ~20 | P3 | single | P3C08 | Yādava prince's silks |
| DVD_A | CH_DEVADUTA | — | ageless | P3 | single | P3C08 | plain grey robes |

---

## 3. GROUP SHEETS (ek image mein kai chehre — census mein 1 sheet)
| GROUP | Members | PARTS | Composition |
|---|---|---|---|
| GRP_KASHI | AMK_A, AML_A | P1 | the two Kāśī princesses side by side, front and 3/4 views, bridal and widow costume variants |
| GRP_YAJA | YAJ_A, UPY_A | P1 | the two ritual priests at a fire altar, front and 3/4 |
| GRP_GANDHARVA | ANG_A, KMB_A | P1 | gandharva husband and wife beside a painted chariot |
| GRP_SVAYAMVARA_BRAHMINS | BRO_A, BRY_A | P1 | old and young brahmin in deerskins, front and 3/4 |
| GRP_EKACHAKRA | EKB_A, EKW_A, EKD_A | P1 | the brahmin family of three, plus a small boy as an extra |
| GRP_UPAPANDAVA | UPP_PRA, UPP_SUT, UPP_SKR, UPP_STN, UPP_SSN | P2,P3 | Draupadī's five sons in a row, each labelled, each resembling his father |
| GRP_LOKAPALA | YAM_A, VRN_A, KUB_A | P2 | three world-guardians on mountain peaks |
| GRP_PANCHALA | UTM_A, YDM_A | P3 | two Pāñcāla wheel-guards |
| GRP_MAUSALA_SAGES | VSM_A, KNV_A | P3 | two old sages (with Nārada NRD_A) |

---

## 4. EXTRAS — crowd type sheets (ek type = ek sheet; chehre generic)
| EXTRA | Type | PARTS | DNA |
|---|---|---|---|
| X_PRIEST_BLACK | Sarpasattra priests | P1,P3 | ritual priests in black robes, eyes red from smoke, shaved heads with tufts, holding ladles |
| X_BRAHMIN | Brahmins | P1,P2,P3 | brahmins of all ages in white cotton and deerskin, sacred threads, tufts |
| X_RISHI | Forest ascetics | P1,P2,P3 | gaunt ascetics with matted hair, bark cloth, water-pots |
| X_KING | Assembly kings | P1,P2 | kings of many regions: varied turbans, silk, gold, armour |
| X_COURTIER | Hastinapura court | P1,P2,P3 | courtiers and ministers in white and saffron cotton |
| X_CITIZEN | Townsfolk | P1,P2,P3 | men, women and children of an Iron-Age town, hand-loom cotton, bare feet |
| X_FISHERFOLK | Dāśa settlement | P1 | fishermen and women, nets, shell ornaments |
| X_MAID | Palace maids | P1,P2 | maids in plain coloured cotton, braided hair |
| X_SERVANT | Male servants | P1,P2,P3 | servants with water-pots, fans, torches |
| X_SOLDIER_KURU | Kaurava infantry | P2,P3 | foot soldiers in red-and-black cloth, leather and bronze, spears and shields |
| X_SOLDIER_PANDAVA | Pāṇḍava infantry | P2,P3 | foot soldiers in white-and-ochre cloth, leather and bronze, spears and bows |
| X_CHARIOTEER | Sūtas | P1,P2,P3 | charioteers in short cotton, leather wrist guards, whips |
| X_CHARIOT_WARRIOR | Generic mahārathas | P2,P3 | armoured chariot archers with banners |
| X_ELEPHANT_CREW | Mahouts and howdah warriors | P3 | mahouts with goads, archers on elephant back |
| X_YADAVA | Dvārakā folk | P1,P2,P3 | Yādava men and women in bright coastal silks |
| X_GANDHARVA_WARRIOR | Gandharva host | P2 | beautiful warriors in silver armour and pale silks |
| X_RAKSHASA | Rākṣasa host | P2,P3 | huge rākṣasas, bald or wild-haired, hide and iron |
| X_NAGA | Nāga court | P1 | Nāga men and women with a faint scaled sheen, pearl ornaments |
| X_BHUTA | Śiva's followers | P2 | strange beings of many guises (bhūtas) and hunter-women |
| X_APSARA | Amarāvatī dancers | P2 | apsaras dancers in sheer silks |
| X_YAKSHA_GUARD | Kubera's guards | P2 | squat powerful yakṣas with clubs |
| X_DANAVA | Nivātakavaca / Kālakeya | P2 | armoured asuras in black iron |
| X_MATSYA_COURT | Virāṭa's court | P2 | Matsya courtiers, guards, door-keepers |
| X_UPAKICHAKA | Kīcaka's brothers (105) | P2 | big perfumed brutal men resembling Kīcaka |
| X_COWHERD | Herdsmen | P2 | cowherds with staffs and ropes |
| X_SAMSHAPTAKA | Trigarta oath-warriors | P2,P3 | grim warriors with ash-marked foreheads |
| X_KALINGA | Kaliṅga host | P3 | Kaliṅga soldiers with elephants |
| X_WIDOW | Kuru widows | P3 | women in white with loose hair, searching the field |
| X_ABHIRA | Cowherd robbers | P3 | rough cowherd raiders with staffs and slings |
| X_KAURAVA_BOYS | The hundred boys | P1 | many boys of 10–13 in fine cotton |
| X_NEWBORN | Newborns | P1,P3 | swaddled newborns (generic) |
| X_NISHADA | Forest people | P1 | Niṣāda men and boys |
| X_POTTER | Potter's household | P1 | potter's family and wheel |
| X_CRAFTSMAN | Builders | P1 | masons, carpenters, lapidaries |
| X_MUSICIAN | Bards and drummers | P1,P2,P3 | bards, drummers, conch-blowers |
| X_PRISONER_KING | Jarāsaṁdha's captives | P1 | 86 captive kings in chains |

---

## 5. CREATURES, ANIMALS & DIVINE-VFX ELEMENTS
| CRE | Being | PARTS | DNA |
|---|---|---|---|
| CR_HORSE_WHITE_ARJUNA | Arjuna's white gandharva horses | P1,P2,P3 | four silver-white horses with golden garlands, like white clouds, swift |
| CR_HORSE_WHITE_BHISHMA | Bhīṣma's white horses | P2,P3 | four tall white horses with white plumes and silvered tack |
| CR_HORSE_SAINYA_SUGRIVA | Kṛṣṇa's horses | P1,P2 | Kṛṣṇa's chariot horses Sainya and Sugrīva: one dappled grey, one pale bay, gold harness |
| CR_HORSE_RED_DRONA | Droṇa's red horses | P3 | red-chestnut horses |
| CR_HORSE_WAR | Generic war horses | P1,P2,P3 | Iron-Age war horses, lean, leather tack |
| CR_ELEPHANT_WAR | War elephants | P2,P3 | Indian elephants with rope-and-leather howdahs, bells |
| CR_SUPRATIKA | Bhagadatta's elephant | P3 | colossal old bull elephant, painted tusks, chain armour |
| CR_ELEPHANT_ASHVATTHAMAN | Mālava elephant "Aśvatthāman" | P3 | ordinary war elephant killed by Bhīma |
| CR_DEER_KINDAMA | Kindama and his mate | P1 | a stag and a doe in a spring forest |
| CR_TIGER | Tiger at Śataśṛṅga | P1 | Himalayan tiger prowling at a cave mouth |
| CR_COBRA | Black cobras | P1 | black cobras |
| CR_CROCODILE | Crocodiles | P1 | mugger crocodiles in shallow water |
| CR_DOG_HUNT | The servant's dog | P1 | lean village hunting dog |
| CR_DOG_DHARMA | The dog at Mahāprasthāna | P3 | lean patient dog, tawny, intelligent eyes |
| CR_ASHVASENA | Takṣaka's son | P1,P3 | large dark serpent with a hooded head and gold-flecked eyes |
| CR_SNAKES_SATTRA | Falling serpents | P1,P3 | white, black and blue snakes of all sizes |
| CR_SHARNGAKA | Jaritā's four chicks | P1 | four unfledged chicks in a hollow tree |
| CR_BOAR_MUKA | Giant boar (dānava) | P2 | monstrous black boar |
| CR_PYTHON | Nahuṣa as python | P2 | mountain-sized python with turmeric-yellow skin, chequered markings, a cave-like mouth with four fangs, copper-red blazing eyes [CE 3.175.13–14] |
| CR_CRANE | The Yakṣa's crane | P2 | a crane on a dead tree by a still lake |
| CR_DEER_ARANI | Deer with fire-sticks | P2 | a deer with fire-sticks caught in its antlers |
| CR_MONGOOSE | Half-golden mongoose | P3 | mongoose whose head and half its body are golden |
| CR_OWL_CROWS | Owl and crows | P3 | thousands of sleeping crows in a banyan, one great owl |
| CR_JACKAL | Jackals | P1,P2,P3 | jackals (omen) |
| CR_VULTURE | Vultures and crows | P1,P3 | vultures and crows (omen and battlefield) |
| CR_DONKEY | Donkeys | P1 | donkeys braying (omen) |
| CR_COW | Cattle | P1,P2 | humped zebu cattle |
| CR_WHITE_SERPENT | Serpent leaving Balarāma | P3 | great white serpent sliding into the sea |
| CR_APE_BANNER | Ape on Arjuna's banner | P1,P2,P3 | a fierce ape figure with a lion's tail atop the banner pole (the banner "roars") |
| CR_GARUDA_BANNER | Kṛṣṇa's Garuḍa banner | P1,P3 | golden Garuḍa emblem on Kṛṣṇa's own chariot |
| CR_FISH_TURTLE | Boiling lake life | P1 | dead fish and turtles floating |

---

## 6. AAPKE 12 BANE HUE CHARACTERS — MAPPING PROTOCOL
1. Har image ka naam bataiye (kaun hai, kis umar/scene ke liye banaya).
2. Main use **ek LOOK ID** se map karunga (jaise "Bhishma old" → `BHS_C`).
3. Agar aapki image is DNA se alag hai (rang, daadhi, kapde) — **image jeetegi**, main DNA text ko image ke hisaab se badal dunga. Bas ek shart: CE ke virodh mein nahi (jaise Kṛṣṇa ka mor-pankh, Bhīma ka saanwla rang, Śakuni ka langdaana — ye CE ke saath nahi chalte).
4. Har LOOK ki sheet = **turnaround (front · 3/4 · profile · back) + 3 expressions (neutral · rage · grief) + 1 full-body costume**, plain mid-grey background, same lighting. Prompt templates `01b_Cast_Census_GENERATED.md` mein hain.
