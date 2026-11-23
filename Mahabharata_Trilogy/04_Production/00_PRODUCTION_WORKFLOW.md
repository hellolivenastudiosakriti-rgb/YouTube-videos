# महाभारत त्रयी — PRODUCTION WORKFLOW (v1.0, "Kathadeep-plus")
> **Kathadeep workflow MD file mujhe nahi mili** — is session ke uploads mein sirf 3 Gemini files thi. Neeche ka workflow poora aur khud mein complete hai. Aap Kathadeep wali file bhejenge to jo cheezein aapke channel par kaam karti hain (thumbnail style, upload routine, prompt format), unhe isme merge kar dunga — par **zero-drift system (sections 1–3) wahi rahega.**

---
## 1. ZERO-DRIFT KE 7 NIYAM (inhe kabhi mat todiye)
1. **Ek hi sach ka srot:** chehra = `01_Cast_and_Look_Bible.md`, jagah = `02_Location_Bible.md`, awaaz/music = `03_Audio_Bible.md`. Prompt kabhi haath se mat likhiye — `build/<chapter>_prompts.md` se copy kijiye (compiler har baar wahi DNA text daalta hai).
2. **Pehle sheet, phir shot:** kisi bhi LOOK ka pehla video shot tab tak nahi banega jab tak uski reference sheet **approved + frozen** (`v1_LOCKED`) na ho. Baad mein sheet badli to us look ke saare purane shots dobara check honge.
3. **Har LOOK ki sheet usi character ki pehli approved sheet ko face-reference bana kar banegi** (jaise `BHS_C` banate waqt `BHS_A` attach) — umar badle, chehra nahi.
4. **Keyframe-first:** har close-up/medium shot ka pehle **still keyframe** banega (image model + sheet reference), use approve karke **Frames-to-Video** se animate. Chehra still image mein theek karna video se 10× aasaan hai.
5. **Ek voice, ek ID:** VOX voice ek baar design → save → kabhi regenerate nahi. Umar ke variant = Voice Remix of the same voice.
6. **Leitmotif masters:** har music cue apne THM master ko upload karke remix/extend se banega — nayi dhun "invent" nahi hogi.
7. **Har shot par drift-QC (section 6)** — fail = regenerate, edit mein "chal jayega" nahi.

---
## 2. PIPELINE — 12 STAGES
| # | Stage | Tool | Input | Output | Gate |
|---|---|---|---|---|---|
| S0 | Setup | Google AI (Flow + Flow Music paid tier), ElevenLabs (Creator/Pro), Drive, DaVinci Resolve | — | accounts, folders (sec. 7) | plans active, terms read |
| S1 | Look sheets | Flow image / Gemini image (Nano Banana) | `01b_Cast_Census_GENERATED.md` §5 prompts | 236 character + 36 extras + 31 creature sheets | QC-A (sec. 6) |
| S2 | Location plates | same image model | `02_Location_Bible.md` | 89 master plates (+ light variants by prompt) | era check: no marble, no neon |
| S3 | Voice casting | ElevenLabs Voice Design / Remix | `03_Audio_Bible.md` §4 | 128 saved voices + 10-line Hindi test each | Hindi pronunciation pass |
| S4 | Music masters | Flow Music (Lyria 3.5) | `03_Audio_Bible.md` §1 | 17 THM masters + stems | motif memorable, no pop drums |
| S5 | Compile | `python3 tools/mbx.py all` | shooting scripts | per-chapter prompts, shots.csv, vo.csv, cue sheet, scene index | 0 validation errors |
| S6 | Keyframes | image model + refs | `build/<ch>_prompts.md` | 1 still per F2V clip | QC-A face match |
| S7 | Video | Google Flow — Veo 3.1 (modes sec. 4) | prompts + keyframes/ingredients | 2–4 takes per clip, best take selected | QC-B motion/continuity |
| S8 | Dialogue | Veo native → ElevenLabs Voice Changer (Method A); TTS (B); actor→STS (C) | `build/<ch>_vo.csv` | DX stems | lips match, same voice |
| S9 | Music & SFX | Flow Music remix/extend; ElevenLabs SFX v2 | cue_sheet.csv, sfx list | MX + FX + AMB stems | cue in/out on picture |
| S10 | Edit & colour | DaVinci Resolve | all of above | chapter timeline, one LUT per Part | runtime ±5% of index |
| S11 | Mix & master | Resolve Fairlight | stems | –14 LUFS stereo master + stems | QC-C audio |
| S12 | Publish | YouTube | master | chapter video + chapters markers + thumbnail | final CE-tag check |

---
## 3. ID SYSTEM (har file ka naam inhi se)
* **Character look:** `BHS_C`, `ARJ_H` … (bible §2) · **Location:** `LOC_DYUTA_SABHA` · **Style:** `STY_MASTER`
* **Chapter:** `P1C07` (Part 1, Chapter 7) · **Scene:** `P1C07S03` · **Setup/shot:** `P1C07S03-05` · **Take/clip:** `P1C07S03-05.2`
* **Line:** `L07` (scene ke andar) · **Voice:** `VOX_12` · **Music:** `MUS_P1C07_H`, theme `THM_DRAUPADI` · **SFX:** `SFX_DICE_CLACK`
* **File naming:** `MBH_<clip>_<mode>_v<nn>.mp4` → `MBH_P1C07S03-05.2_F2V_v02.mp4`; audio `DX_P1C07S03_L07_VOX_12_v01.wav`

---
## 4. GOOGLE FLOW / VEO 3.1 — MODES (shot table ke `MODE` column ka matlab)
| MODE | Flow feature | Kab use karein | Note (Flow help page, Nov 2026 — khud confirm karein) |
|---|---|---|---|
| `F2V` | **Frames to Video** (start frame, optional end frame) | **har character close-up / medium / dialogue** | sab Veo 3.1 tiers par, 4/6/8 s. Sabse zyada identity control. |
| `ING` | **Ingredients to Video** (up to 3 reference images) | wide/two-shot jahan keyframe banana mushkil ho; crowds | 8 s, Veo 3.1 Lite tier. Refs = look sheet + location plate. |
| `T2V` | Text to Video | bina character ke shots: landscape, VFX, inserts | Quality tier par 4/6/8/10 s. |
| `EXT` | Extend (pichhle clip ke last second se) | ek lamba continuous move (dam, charge) | 8 s clips, Lite se extend. Audio continuity sirf last second tak. |
| `INS` | Image only (still / inset / title card) | title cards, shadow-puppet inlays ke still frames | edit mein Ken-Burns |

**Shot ka sec column:** `8` = ek 8-second generation · `8×4` = chaar alag 8-second takes (dialogue lines alag-alag, ya coverage) · edit mein in clips ko kaat kar 2–5 sec ke shots banenge.

---
## 5. DIALOGUE, MUSIC, SFX — kaun kya karega
* **Dialogue:** Audio Bible §5 (Method A default). Hindi line Veo prompt mein sirf hothon ke liye; final awaaz ElevenLabs.
* **Music:** `build/cue_sheet.csv` — har scene ka cue. FLOW cues = THM master upload → "remix/cover" + scene prompt → length set → extend agar 3 min se lamba. ELM cues (sirf 4) = ElevenLabs Music; ya Dhaumya/VOX chants TTS se layer.
* **SFX:** har scene ke `SFX:` aur shot ke `SOUND` column mein IDs. Veo ka native Foley (kadam, kapda, haath) rakh sakte hain; **ambience aur signature sounds hamesha library wale** (har shot mein same shankh, same Gāṇḍīva).

---
## 6. QC GATES — drift checklist
**QC-A (har still / keyframe):**
- [ ] Chehra sheet se match: face shape, nose, eyes, brow, beard pattern, skin tone (Bhīma–Yudhiṣṭhira gaur, Arjuna–Kṛṣṇa–Draupadī saanwle — CE 15.32 / 1.155.42 / 6.102.57)
- [ ] Umar sahi LOOK ki (BOY / YOUTH / PRINCE / EXILE / WAR / OLD)
- [ ] Poshak, gehne, hathiyaar, dhvaj, shankh bible ke hisaab se
- [ ] **Never list** follow hui: Kṛṣṇa ke paas mor-pankh nahi · Gāndhārī ki patti kabhi nahi hatti · Śakuni langdata nahi · shankh asli seashell · chariot ke pahiye spoked · Karṇa ka kavach P2C05 tak, uske baad kabhi nahi · Draupadī ke baal Sabhā ke baad khule · Aśvatthāman ki mani P3C07 tak, phir ghaav
**QC-B (har video clip):** haath/ungliyan theek · aankhein sahi disha mein (Dhṛtarāṣṭra ki aankhein kabhi focus nahi) · left/right geography (180° rule) · rath kis taraf se aaya · shot ke andar chehra badla to reject
**QC-C (audio):** VOX ID sahi · lip-sync · loudness · SIL cues par sach mein khaamoshi · Sanskrit uchchāraṇ
**QC-D (kahani):** `[NOT CE]` wali koi cheez screen par nahi aayi (list: Fact-Check report §7 + har script ke NOT-CE notes)

### Death ledger (CE) — mara hua character baad ke shot mein nahi dikhna chahiye
| When | Who dies | By | CE |
|---|---|---|---|
| Day 1 | Uttara (Virāṭa's son) · Śveta | Śalya · Bhīṣma | 6.44 · 6.45 |
| Day 5 | Sātyaki's ten sons | Bhūriśravas | 6.70 (Day 6 begins 6.71.1) |
| Day 8 | Irāvat | Alambuṣa | 6.86 |
| Day 10 | Bhīṣma falls (dies 58 nights later) | Arjuna behind Śikhaṇḍin | 6.114; 13.153–154 |
| Day 12 | Bhagadatta | Arjuna | 7.28 |
| Day 13 | Lakṣmaṇa (Duryodhana's son) · Abhimanyu | Abhimanyu · Duḥśāsana's son | 7.45 · 7.48 |
| Day 14 | Bhūriśravas · Jayadratha (· Vṛddhakṣatra) | Sātyaki · Arjuna | 7.117–118 · 7.121 |
| Night 14 | Ghaṭotkaca | Karṇa (Śakti) | 7.154 |
| Day 15 | Drupada · Virāṭa · Droṇa | Droṇa · Droṇa · Dhṛṣṭadyumna | 7.161 · 7.165 |
| Day 17 | Duḥśāsana · Karṇa | Bhīma · Arjuna | 8.61 · 8.67 |
| Day 18 | Śalya · Śakuni · Duryodhana (thighs broken; dies at dawn) | Yudhiṣṭhira · Sahadeva · Bhīma | 9.16 · 9.27 · 9.57; 10.9 |
| Night 18 | Dhṛṣṭadyumna, Śikhaṇḍin, Draupadī's five sons, Uttamaujas, Yudhāmanyu | Aśvatthāman (Kṛpa, Kṛtavarman at the gate) | 10.8 |
| +36 yrs | Sātyaki, Kṛtavarman, Yādavas · Balarāma · Kṛṣṇa | each other · yoga · Jarā's arrow | 16.4–16.5 |

---
## 7. FOLDER STRUCTURE (Drive / disk)
```
MBH/
  00_bibles/            (yeh repo ki 04_Production files)
  01_sheets/  CH_*/LOOK_ID_v1_LOCKED.png      02_plates/ LOC_*_v1_LOCKED.png
  03_voices/  VOX_xx_test.wav                 04_music/  THM_*/  MUS_*/  (stems)
  05_sfx/     SFX_*.wav
  P1/ P1C01/ keyframes/  clips/  dx/  mx/  fx/  edit/  P1C01_master.mov
```

---
## 8. CHAPTER DIVISION (YouTube episodes = chapters; teeno films inhi se joD kar)
| Part | Chapter | Title | ≈ min | End hook (cliffhanger) |
|---|---|---|---|---|
| P1 | C01 | शंखनाद | 24 | Śaṁtanu ka vardan — "pratigya ne rajya bachaya… par vansh?" |
| P1 | C02 | टूटता वंश | 23 | Satyavatī van mein; mahal ki chhat se baalak Duryodhana Pāṇḍavon ko dekhta hai |
| P1 | C03 | विष और अंगूठा | 22 | Rangabhūmi mein Karṇa ka pravesh — "Pārtha!" → black |
| P1 | C04 | रंगभूमि और लाक्षागृह | 28 | Hastinapura shok mein; Vidura ki aankh; jungle mein do laal aankhein khulti hain |
| P1 | C05 | अग्निकन्या | 27 | Yamunā tat par aag jaisa brāhmaṇ: "mujhe bhojan do… yah Khāṇḍava" |
| P1 | C06 | खांडव और मय-सभा | 26 | "Sabhā mein lalkāra gaya to main kabhi peechhe nahi hat-ta" + bheri |
| P1 | C07 | द्यूत | 22 | khaali sabhā, deepak bujhta hai, door ek shankh |
| P2 | C01 | किर्मीर | 22 | Kṛṣṇa ka vachan — aur Draupadī ka sawaal: "tumhe krodh kyon nahi aata?" |
| P2 | C02 | क्रोध और तप | 24 | Pāśupata — aasmaan se Mātali ka rath utarta hai |
| P2 | C03 | अमरावती और हनुमान | 26 | "Main Arjuna ki dhvaja par baithunga…" |
| P2 | C04 | अजगर, गंधर्व, जयद्रथ | 28 | Śiva: "ek din — Arjuna ko chhod kar — sab ko rok sakoge" |
| P2 | C05 | कवच और यक्ष | 18 | Virāṭa ke mahal mein Kīcaka ki nazar Sairandhrī par |
| P2 | C06 | कीचक और बृहन्नला | 25 | Virāṭa ke sinhasanon par paanch purush — pehchaan |
| P2 | C07 | शांतिदूत | 24 | Viśvarūpa — andha raja sab sunta hai, dekhta kuch nahi |
| P2 | C08 | कर्ण | 25 | Gāṇḍīva haath se girta hai — THUD |
| P3 | C01 | गीता | 22 | "Naṣṭo mohaḥ" — pehla tīr |
| P3 | C02 | नौ दिन | 20 | "Śikhaṇḍī ko aage karo" |
| P3 | C03 | शरशय्या | 24 | Droṇa chakravyūha bichhata hai |
| P3 | C04 | चक्रव्यूह | 26 | sir Vṛddhakṣatra ki god mein — raat ka yuddh shuru |
| P3 | C05 | रात्रि और द्रोण | 23 | Karṇa senāpati |
| P3 | C06 | सूर्यपुत्र | 25 | Kuntī jaanti hai kaunsa beta mara |
| P3 | C07 | गदा और रात्रि | 20 | "Tīn hazaar varsh" — mani Yudhiṣṭhira ke maathe par |
| P3 | C08 | शान्त | 30 | Vyāsa ki ūrdhvabāhu pukaar; raakh par safed shankh |

---
## 9. ENVIRONMENT & ISOLATION (aapki shart: "is project ko pichhle sessions se mix mat karna")
* Saara kaam **sirf** `Mahabharata_Trilogy/` folder mein, **sirf** branch `ccr-43a322cd-rcdqbs` par. Repo ki koi aur file/folder chhua nahi gaya.
* Cloud environment ka naam ab **"Mahabharata-Trilogy"** hai — personal, sirf is project ke liye; BORI e-text ke hosts allowed; iski setup script har naye session mein CE text `/opt/bori_ce` mein download karti hai. Aapke purane environments ("Akriti", "Default") aur unke sessions se iska koi lena-dena nahi.
* BORI lookup tool: `04_Production/tools/mbh.py` (`python3 tools/mbh.py v 1.94.88`, `g REGEX`, `star 2 544`) — text © BORI repo mein nahi rakha; setup script se aata hai.

## 10. AAPSE CHAHIYE (pending)
1. **12 bane hue characters** ki images + naam → main unhe LOOK IDs se map karke DNA text unke hisaab se lock karunga.
2. **Kathadeep workflow MD** (merge ke liye).
3. **Prologue file** (Part I cold open se jodne ke liye).
4. Paase ka final design: vibhītaka (Vedic) ya sone-vaiḍūrya jaise (Virāṭa 4.6.1) — default: **dark vibhītaka nuts** (Sabhā mein material CE mein nahi).
