# महाभारत त्रयी — BORI Critical Edition Fact-Check & Cross-Match Report
### Gemini ki files vs. original Sanskrit (BORI e-text) se independent verification

**Prepared for:** Mahabharata AI Trilogy (भाग १: प्रतिज्ञा और सभा · भाग २: वन और शंख · भाग ३: कुरुक्षेत्र और स्वर्गारोहण)
**Files audited (word by word):**
1. `Mahabharat_Part_1___90-Second_Teaser_20-Shot_Master_Production_Pack_2.md` (Teaser)
2. `Mahabharat_Part_1___100_BORI_Critical_Edition_Fact-Check__Audit_Bible.md` (Audit Bible)
3. `Mahabharat_Part_1___Master_Screenplay__Full_Production_Blueprint.md` (Master Screenplay)
4. Drive PDF — `BORI Mahabharata Film Blueprints.pdf` (Hindi, 18-parva trilogy blueprint)
5. Drive PDF — `Mahabharata Taboo, Media, Trilogy Blueprint.pdf` (home-taboo + market + 4 blueprint files)
6. Drive PDF — `Mahabharata AI Audit and Screenplay.pdf` (Gurudev Odisha 3D audit + Sanskrit ledger + English screenplay)

---

## 0. Verification method (kaise check kiya)

Gemini ki research mostly secondary websites (blogs, Quora, Reddit, vedapath, hindutone) par based thi. Maine **primary source** use kiya:

* **BORI ka official electronic text** — "Electronic text © Bhandarkar Oriental Research Institute, Pune" (typed by BORI team, collated by Prof. John D. Smith, Cambridge). Saare **18 parva (constituted text)** + har parva ke **saare star passages (`*`) aur Appendix I passages** download kiye (≈12 MB Sanskrit).
* Ek lookup script se har citation ko **exact verse-ID** (jaise `01094092` = 1.94.92) se grep kiya. Is report ka har "BORI says" Sanskrit isi text se copy kiya gaya hai.
* Jahan constituted text chup hai, wahan **critical apparatus** (star passage / Appendix) khol kar dekha ki popular kahani kahan se aayi.

### Exact counts (BORI e-text se gine hue)

| Part | Parvas | Adhyaya | Numbered verses (CE) | Gemini ne likha | Verdict |
|---|---|---:|---:|---:|---|
| भाग I | आदि + सभा | 225 + 72 = **297** | 7,197 + 2,390 = **9,587** | 9,597 (7,202 + 2,395) | ⚠️ minor fix |
| भाग II | आरण्यक + विराट + उद्योग | 299 + 67 + 197 = **563** | 10,316 + 1,824 + 6,063 = **18,203** | 18,218 | ⚠️ minor fix |
| भाग III | भीष्म → स्वर्गारोहण (13 parva) | **1,135** | **46,026** | 46,091 | ⚠️ minor fix |
| **Total** | 18 parva | **1,995** | **73,816** | 73,906 | ⚠️ (73,816 = BORI e-text count) |

Critical apparatus size: ≈ **11,800 star passages** aur ≈ **430 Appendix I passages** — yaani BORI ne kuch "delete" nahi kiya, sab footnote/appendix mein transparently rakha hai.

> Title card suggestion: "BORI क्रिटिकल एडिशन (1,995 अध्याय) पर आधारित" — exact number dikhana ho to **73,816 श्लोक-इकाइयाँ** likhein, 89,000 ya 1,00,000 nahi.

---

## 1. SCORECARD — ek nazar mein

| # | Topic | Gemini ka claim | BORI CE actually kya kehta hai | Verdict |
|---|---|---|---|---|
| 1 | भीष्म-प्रतिज्ञा पर सत्यवती | "Satyavati present nahi thi" | 1.94.91–92: vow ke turant baad Devavrata Satyavati ko "mātar" kehkar rath par bithate hain | ❌ **GALAT** |
| 2 | प्रतिज्ञा के साक्षी | sirf Dasharaja + boatmen | 1.94.67–68, 77, 86: Devavrata **vṛddha kṣatriyon** ke saath gaye; dāśa ne **rājasaṁsad** mein baat ki; vow "**śṛṇvatāṁ bhūmipālānām**" (raja-gan sun rahe the) | ❌ adhoora |
| 3 | Devavrata ki umar (vow ke waqt) | 24 saal | 1.94.18: Ganga ke jaane ke baad Shantanu **36 saal** (16+8+4+8) van mein rahe; phir Devavrata mile; phir **4 saal** yuvaraj (1.94.40) → vow ke waqt ≈ **36–40** | ⚠️ design correction |
| 4 | Vow mein "anjali-jal arpan" | creative | Text mein nahi | ⚠️ label as creative |
| 5 | Bhima ko zehar (1.119) | "saanp ka zehar pehle zehar ko neutralize karta hai; NO Nagaloka" | CE mein **neutralization hai hi nahi**. 1.119.34–35: Bhima bandhan tod kar khud paani se nikalta hai; 36–37: saanpon ke daant uski chamdi **bhed hi nahi paate**; 39–41: kālakūṭa zehar khaane mein — **Yuyutsu chetaata hai**, Bhima pacha jaata hai | ❌ **GALAT** (Nagaloka wala hissa App. I **No. 72–73** mein — ye sahi) |
| 6 | Karna-Shalya fail wala shlok | 1.179.16 (3 files mein) | **1.179.4**; 1.179.16 = Arjuna nimesh mein dhanush chadhata hai | ❌ citation galat (Drive PDF-3 sahi tha) |
| 7 | Draupadi ka "nāhaṁ varayāmi sūtam" | Star passage 1827* | ✅ **1827\*** (1.178.17 ke baad; sirf K4, Ñ2, Dn, D2.4.5 manuscripts) | ✅ SAHI |
| 8 | Swayamvar ke baad Karna vs Arjuna | "Arjuna ne Karna ko haraya" | 1.181.9–21: teen baan, ghamasan; Karna poochta hai "kya tum Dhanurveda/Parashurama/Indra/Vishnu ho?"; Arjuna: "main brahman hoon"; Karna **brahma-tej ko ajeya maan kar ruk jaata hai** (nyavartata) | ⚠️ "withdrew", "defeated" nahi |
| 9 | Swayamvar ka lakshya | "ghoomta lakshya" | 1.176.10–11, 34: **sone ka lakshya + aakaash mein yantra (machine) ka chhed**, 5 baan. **Machhli/tel-pratibimb nahi** | ⚠️ "matsya" mat dikhana |
| 10 | Rangabhoomi — kram | Kripa → Adhiratha → Bhima → Duryodhana ka abhishek | 1.126.30–39: Kripa ka prashn → Duryodhana ka **"rajya ke 3 srot"** tark → **turant abhishek** → 1.127: Adhiratha aata hai → Bhima ka taana → Duryodhana ka "veeron aur nadiyon ka mool" bhashan | ⚠️ kram ulta |
| 11 | Karna ne Drona-Kripa ko pranam kiya? | "nahi kiya" | 1.126.6: kiya, par "**nātyādṛtam iva**" — bemann/halka sa | ⚠️ |
| 12 | Vidura ne Kunti ka rahasya samjha | "Vidura sab samajh gaye" | 1.126.28: Vidura ne chandan-jal chhidak kar hosh dilaya — **rahasya samajhne ka zikr nahi** | ❌ embellishment |
| 13 | Kunti ki chhupi khushi | missing | 1.127.22: Anga-raj bane bete ko pehchaan kar Kunti ko **"channā prītiḥ"** — chhupi khushi | ➕ NAYA |
| 14 | Ekalavya | Arjuna sirf dekhta hai | 1.123.26–28: **Arjuna khud Drona se shikayat karta hai** "aapne kaha tha koi shishya mujhse badhkar nahi hoga!"; 29: Drona Arjuna ko saath le jaate hain; 39: angutha kat-ne ke baad "**Arjuna prasann aur nishchint hua**" | ❌ sanitized (Gemini ne chhupa diya) |
| 15 | Pakshi pariksha | "sir, aankh nahi" | ✅ 1.123.46: **kṛtrima bhāsa** (kaariगरों ka banaya nakli pakshi), 48: lakshya shuru se "**śiraḥ**", 64: "śiraḥ paśyāmi bhāsasya na gātram" | ✅ SAHI |
| 16 | Lakshagraha — 6 log | 1.136.4 "ṣaṭ prāṇino nidhāyeha" | ✅ exact. 1.136.7–8 Nishadi + 5 putra, "kālacoditā" | ✅ SAHI |
| 17 | Kanika-niti | excised | ✅ Adi **App. I No. 81** | ✅ SAHI |
| 18 | Ganesh lekhak | App. I No. 1 | App. I No. 1 = **Brahma ka Vyasa ke paas aana**; Ganesh-lekhak lines BORI ke e-apparatus mein bhi nahi milti (INDOLOGY list 2016 ne bhi yahi paaya) | ✅ (BORI mein nahi — pakka) |
| 19 | Madri sati | "Madri ka chita-rohan" | ✅ 1.116.31 "anvārohat"; par 1.117.30 rishi "**ime tayoḥ śarīre dve**" laate hain aur 1.118 mein Hastinapur mein dah-sanskar — text mein khud inconsistency | ⚠️ handle carefully |
| 20 | Shatashringa rishi | "wapas van chale gaye" | 1.117.32–33: **pal bhar mein antardhan** — gandharva-nagar ki tarah | ➕ cinematic |
| 21 | Subhadra-haran | Arjuna rath chalata hai | ✅ 1.212.7–8 (aur rath **Krishna ka**, Sainya-Sugriva ghode, 1.212.3); Subhadra-saarathi = **App. I No. 115** | ✅ SAHI |
| 22 | Ulupi ka jal-vardaan | nahi | ✅ star passage **2029\*** | ✅ SAHI |
| 23 | Manalura | coastal | ✅ 1.207.13 "samudratīreṇa ... maṇalūram"; raja **Citravāhana**; Chitrangada **putrikā** (1.207.21–22); Arjuna **3 saal** raha | ✅ |
| 24 | Khandava — rath | Krishna saarathi, ek rath | 1.217.1 "**tau rathābhyām**" — **do alag rath**, van ke dono taraf | ❌ **GALAT** |
| 25 | Khandava ke astra | Varuna: Gandiva etc.; Krishna: Sudarshan+Kaumodaki | ✅ Gandiva + 2 akshay tarkash + kapi-dhvaj rath, **chaandi jaise safed Gandharva ghode** (1.216.8) — Varuna; **Vajranābha chakra — Agni** (1.216.21); **Kaumodakī — Varuna** (1.216.25). Gandiva pehle **Soma** ka tha (1.216.3) | ✅ + detail |
| 26 | Khandava ki kroorta | heroic | 1.217.5–12: jeev apne bachchon ko lipte-lipte jal gaye, taalaab ubal gaye, Arjuna **hanste hue** udte jeevon ko kaat kar aag mein daalta hai | ➕ moral weight |
| 27 | Maya Sabha | 14 mahine | ✅ 2.3.34; Bhima ko gada + Arjuna ko **Devadatta** shankh (2.3.18) | ✅ |
| 28 | Jarasandha | 14 din, rīḍh | ✅ 2.21.17–18 (Kartik pratipada se, 13 din-raat, 14vi raat thakan), 2.22.4 Krishna ke shabd, 2.22.6 "babhañja pṛṣṭhe"; **2.22.8 garjana se garbhpaat** | ✅ |
| 29 | Shishupala | 100 aparadh | ✅ 2.40.1 (3 aankh, 4 bhuja, gadhe jaisi aawaz), 2.40.22 "aparādhaśatam", 2.42.21 chakra, 2.42.22–25 **tej Krishna mein samaaya, bina badal barsaat, dharti kaanpi** | ✅ |
| 30 | Maya-sarovar par kaun hansa | sevak + 4 Pandava | ✅ 2.43.6–9 (Draupadi 2.43 mein hai hi nahi) | ✅ |
| 31 | Duryodhana ka jhooth | 2.46.30 | ✅ aur **zyada pakka**: Krishna 2.42.55–60 mein Dwaraka ja chuke the, phir bhi Duryodhana kehta hai "Krishna Partha ke saath hansa". 2.46.33–34: khud maanta hai ki **Nakul-Sahadev ne use sahara diya** | ✅ + nuance |
| 32 | Paase ka material | "Vibhitaka nuts (2.53)" | Sabha Parva **kahin material nahi batata**. Poore CE mein "vibhītaka" sirf 9.36.58 (pedon ki list). Ekmatra varnan: **Virata 4.6.1 — sone ke, vaidurya (beryl) jaise paase** | ❌ citation galat (design choice theek) |
| 33 | Draupadi ka prashn | 2.60.7 | ✅ pehle **Prātikāmin** se; sabha mein lambi bahas 2.60.29–34, 43–45 | ✅ |
| 34 | Duhshasana ka taana | missing | 2.60.26: "**Krishna, Jishnu, Hari, Nara ko bachane ke liye pukaar!**" — yahi line baad ke manuscripts mein Draupadi ki prarthana ban gayi | ➕ NAYA (bahut powerful) |
| 35 | Baal aur Rajasuya | missing | 2.60.23: jin baalon par **Rajasuya ke avabhṛtha snaan ka mantra-jal** chhidka tha, unhi ko pakda | ➕ NAYA |
| 36 | "Sirf Vikarna ne virodh kiya" | — | Bhima (2.61.1–6, haath jalane ki dhamki), Arjuna (2.61.7–9), Vidura (2.63.16–19), poori sabha ka "dhik!" (2.61.49–50) | ⚠️ adhoora |
| 37 | Vastra-chamatkar | 2.61.40–41, prarthana 544\* | ✅ prarthana cluster **542\*–550\*** (544\* mukhya), "Dharma ki raksha se rang-birange vastra" **553\***, "108 vastra" 552\* | ✅ SAHI |
| 38 | Bhima ki rakt-pratigya | 2.61.44–46 | ✅ 2.61.43–46 (vastra prakat hote hi, sabha ke beech) | ✅ |
| 39 | Jangha | 2.63 | ✅ 2.63.10–12 — Duryodhana **Karna ki taraf muskura kar** baayi jangha dikhata hai; 2.63.15: Bhima ke **har chhidra se aag ki lapten** (kavya-chitra) | ✅ + detail |
| 40 | Do vardaan | ✅ | ✅ 2.63.27–36; pehle vardaan ka kaaran: **beta Prativindhya "daas-putra" na kahlaye** (2.63.29) | ✅ + motive |
| 41 | Prasthan | "Kunti rote hue" | 2.71.3–7: Yudhishthira **mukh dhak kar**, Bhima **bhujaayein faila kar**, Arjuna **ret udaate hue**, Sahadev **mukh pe mitti**, Nakul **poore sharir pe dhool**, Draupadi **baalon se mukh dhak kar roti**, Dhaumya **Yama-saam gaate** | ➕ NAYA (climax gold) |
| 42 | Draupadi ki bhavishyavaani | missing | 2.71.19–20: "**14ve varsh** unki patniyaan pati-putra-bandhu kho kar, **rakt se lathpath, khule baal**, tarpan kar ke Hastinapur mein ghusengi" | ➕ NAYA |
| 43 | Apshakun + Narada | missing | 2.71.25–30: bina badal bijli, bhookamp, **Rahu ne asamay surya nigla**, ulka; Narada: "**14ve varsh Kaurav nasht honge**" | ➕ NAYA |
| 44 | Gandhari ki patti | 1.103.14, "silk" | **1.103.13**: "**paṭṭam ādāya kṛtvā bahuguṇam**" — kapde ki patti kai tah karke; kaaran "**nātyaśnīyāṁ patim**" (pati se badhkar nahi rahungi) | ⚠️ verse no. fix |
| 45 | Takshashila sarpasattra | ✅ | ✅ **18.5.29**: "takṣaśilāyāḥ ... punar āyād gajāhvayam" | ✅ SAHI |
| 46 | Katha kab sunaayi gayi | Astika ke rokne ke baad | 1.54.1: Vyasa aaye jab Janamejaya **dīkṣita** the; 18.5.26: katha **yajña ke beech ke viraam** mein; 18.5.27: "phir ritwijon ne yajna poora kiya, **Astika prasann hua serpon ko chhuda kar**" | ⚠️ better frame (see §4) |
| 47 | Divya-drishti (5.129) | Dhritarashtra ko nahi | ✅ 5.129.13; Dhritarashtra wala hissa **495\*–496\*** | ✅ SAHI |
| 48 | 5 gaon | 5.80.4–9 | **5.31.19–20**: Kuśasthala, Vṛkasthala, Āsandī, Vāraṇāvata + "koi bhi paanchva" (5.70.15, 5.80.7 dohraate hain) | ⚠️ verse fix |
| 49 | Durvasa / Urvashi / Karna-digvijaya / Durga-stotra | App. I 25 / 6 / 24 / Virata 4 | ✅ sab confirm (Aranyaka App. I **25, 6, 24**; Virata App. I **4**) | ✅ |
| 50 | Brihannala | swechha | ✅ 4.2.21 "jyāghātau ... duṣkarau" (pratyancha ke nishaan chhupane) | ✅ |
| 51 | Kavach-kundal daan | ✅ | ✅ 3.294.26–39 + **Karna kaat-te hue baar baar muskurata hai** (3.294.37), kavach **geela** diya (38), Indra "**prahasan vañcayitvā**" (39) | ✅ + detail |
| 52 | Karna ki tokri | Ashva nadi | ✅ 3.292.6–26: mañjūṣā → **Ashva → Charmanvati → Yamuna → Ganga → Champa** | ✅ |
| 53 | Day 3 chakra / Day 9 chabuk | ✅ | ✅ 6.55.86–98 (Sudarshana; text mein shabd "**rathāṅga**" — isi se baad mein "rath ka pahiya" bana), 6.102.54 "pratodapāṇiḥ" | ✅ |
| 54 | Day 14 sooraj | natural | ✅ 7.121.15–16; Krishna ka andhera = Drona **App. I No. 16** | ✅ |
| 55 | "Aśvatthāmā hataḥ" | ✅ | ✅ 7.164.106 "avyaktam"; 107: rath 4 angul upar chalta tha — ab **ghodon ne zameen chhoo li** | ✅ |
| 56 | Jangha-sanket | Arjuna | ✅ 9.57.18 | ✅ |
| 57 | Arjuna ka rath bhasm | ✅ | ✅ 9.61.12–14 | ✅ |
| 58 | Ashwatthama shaap | 3,000 saal | ✅ 10.16.10; Parikshit 60 saal raaj (10.16.14) | ✅ |
| 59 | 58 raatein | ✅; "Magha Shukla BORI mein nahi" | 58 raatein ✅ 13.153.27; **13.153.28 mein "Māgha" maas aur "śukla" paksha dono hain** | ❌ second half galat |
| 60 | Mrityu-sankhya | 1,66,00,20,000 | ✅ 11.26.9–10 (+ 24,165 laapata) | ✅ |
| 61 | Krishna ki mrityu | ✅ | ✅ 16.5.20 Jara ne **talve** mein baan maara | ✅ |
| 62 | Dushasana ka rakt | 8.61, Draupadi nahi | ✅ 8.61.6–9: gale pe pair, **chhaati cheer kar** garm rakt; "maa ke doodh, madhu, ghee se bhi swaadisht"; dekh kar sainik behosh — Draupadi scene mein nahi | ✅ |

**Summary:** Gemini ka kaam ~80% sahi tha, lekin **8 serious galtiyan** (Satyavati, Bhima-zehar, Karna verse no., Khandava rath, paase ka citation, Vidura-rahasya, Ekalavya-Arjuna sanitization, Magha-Shukla) aur **15+ powerful CE details miss** thi jo ab script mein jod di gayi hain.

---

## 2. MAJOR CORRECTIONS — Sanskrit proof ke saath

### 2.1 Satyavati was present at Bhishma's vow (1.94)
```
01094086a dāśarāja nibodhedaṁ vacanaṁ me nr̥pottama
01094086c śr̥ṇvatāṁ bhūmipālānāṁ yad bravīmi pituḥ kr̥te       ← raja-gan sun rahe hain
01094088a adya prabhr̥ti me dāśa brahmacaryaṁ bhaviṣyati
01094088c aputrasyāpi me lokā bhaviṣyanty akṣayā divi
01094090a tato ’ntarikṣe ’psaraso devāḥ sarṣigaṇās tathā
01094090c abhyavarṣanta kusumair bhīṣmo ’yam iti cābruvan
01094091a tataḥ sa pitur arthāya tām uvāca yaśasvinīm
01094091c adhiroha rathaṁ mātar gacchāvaḥ svagr̥hān iti            ← "Maa, rath par chadhiye"
01094092a evam uktvā tu bhīṣmas tāṁ ratham āropya bhāminīm
01094094c svacchandamaraṇaṁ tasmai dadau tuṣṭaḥ pitā svayam        ← ichchha-mrityu ka vardaan
```
**Film fix:** Scene mein Satyavati (dāśa-kanyā) piche khadi; vow ke baad Devavrata pehli baar use "**माता**" kehta hai — ye scene ka emotional punch hai. Saath mein: Devavrata ke saath aaye **vṛddha kṣatriya** (1.94.67) aur sunne wale **raja-gan** (1.94.77, 86). Aasmaan se phool **apsara, dev aur rishi-gan** barsaate hain aur "**Bhishma!**" kehte hain (1.94.90); fir raja bhi "bhīṣmo 'yam" (1.94.93). Ghar lautne par **Shantanu ichchha-mrityu ka vardaan** dete hain (1.94.94) — ye Part III ke shar-shayya scene ka seed hai.

### 2.2 Bhima poisoning — CE version (1.119.29–43)
```
01119033a śītaṁ vāsaṁ samāsādya śrānto madavimohitaḥ
01119034a tato baddhvā latāpāśair bhīmaṁ duryodhanaḥ śanaiḥ
01119034c gambhīraṁ bhīmavegaṁ ca sthalāj jalam apātayat
01119035a tataḥ prabuddhaḥ kaunteyaḥ sarvaṁ saṁchidya bandhanam
01119035c udatiṣṭhaj jalād bhūyo bhīmaḥ praharatāṁ varaḥ
01119036a suptaṁ cāpi punaḥ sarpais tīkṣṇadaṁṣṭrair mahāviṣaiḥ
01119037a daṁṣṭrāś ca daṁṣṭriṇāṁ teṣāṁ marmasv api nipātitāḥ
01119037c tvacaṁ naivāsya bibhiduḥ sāratvāt pr̥thuvakṣasaḥ
01119038c sārathiṁ cāsya dayitam apahastena jaghnivān
01119039c kālakūṭaṁ navaṁ tīkṣṇaṁ saṁbhr̥taṁ lomaharṣaṇam
01119040a vaiśyāputras tadācaṣṭa pārthānāṁ hitakāmyayā
01119040c tac cāpi bhuktvājarayad avikāro vr̥kodaraḥ
01119043c udbhāvanam akurvanto vidurasya mate sthitāḥ
```
**Teen alag hamle:** (1) Pramāṇakoṭi par thaka-madhosh Bhima latāon se baandh kar nadi mein — **khud bandhan tod kar nikalta hai**; (2) sote hue saanp — **daant chamdi nahi bhed paate**, Bhima saanp kuchal deta hai aur Duryodhana ke **pyare saarathi** ko ulte haath se maar deta hai; (3) kālakūṭa zehar khaane mein — **Yuyutsu (vaiśyā-putra) chetaata hai**, Bhima kha kar pacha leta hai. Pandava Vidura ki salah par chup rehte hain. Nagaloka / Vasuki / Aryaka / rasa-kund = **Adi App. I No. 72–73**.
*Bonus CE detail:* 1.119.5–12 — Pandu ke shraddha ke baad **Vyasa Satyavati se kehte hain "ghor kaal aa raha hai, van chali jao"**; Satyavati, Ambika, Ambalika tapasya karti hui deh tyagti hain. 1.119.14–23 — Bhima bachpan mein Kauravon ko ghaseet-ta, paani mein dubota, ped hila kar girata — "**bachpane se, dwesh se nahi**".

### 2.3 Swayamvara verse numbers (1.178–1.181)
```
01178015c tat kārmukaṁ saṁhananopapannaṁ; sajyaṁ na śekus tarasāpi kartum   ← raja fail (Karna ka naam nahi)
01179004a yat karṇaśalyapramukhaiḥ pārthivair lokaviśrutaiḥ                    ← YAHAN Karna-Shalya
01179004c nānataṁ balavadbhir hi dhanurvedaparāyaṇaiḥ
01179016a sajyaṁ ca cakre nimiṣāntareṇa; śarāṁś ca jagrāha daśārdhasaṁkhyān   ← Arjuna, 5 baan
01*1827_09 dr̥ṣṭvā tu taṁ draupadī vākyam uccair
01*1827_10 jagāda nāhaṁ varayāmi sūtam                                       ← sirf star passage
01181021a evam uktas tu rādheyo yuddhāt karṇo nyavartata
01181021c brāhmaṁ tejas tadājayyaṁ manyamāno mahārathaḥ
```
**Also:** 1.179.21 — Arjuna ke jeetne par **Yudhishthira jaldi se yamalon ke saath ghar laut jaate hain**; 1.179.22 — Draupadi **muskuraate hue** safed varmala le kar aati hai; 1.179.17 — Indra (deva) Partha ke sir par divya pushp barsaata hai.

### 2.4 Khandava — do rath (1.217.1)
```
01217001a tau rathābhyāṁ naravyāghrau dāvasyobhayataḥ sthitau
01217003c āviddhāv iva dr̥śyete rathinau tau rathottamau
01217011c dīpyamāne tataḥ prāsyat prahasan kr̥ṣṇavartmani
```
Krishna apne rath par (chakra ke saath), Arjuna Varuna ke diye kapi-dhvaj rath par — **van ke do chhoron par itni tez parikrama ki "ghoomte chakra" jaise dikhte the**. Krishna saarathi = Kurukshetra (Part III) ka visual — use Part I mein mat chura lena; Part III ka "pehli baar Krishna lagaam pakadte hain" moment zyada powerful banega.

### 2.5 Dice material (2.53 nahi)
```
04006001c vaiḍūryarūpān pratimucya kāñcanān; akṣān sa kakṣe parigr̥hya vāsasā   ← Virata: sone ke, vaidurya-jaise paase
09036058a badareṅgudakāśmaryaplakṣāśvatthavibhītakaiḥ                          ← CE mein vibhītaka ka ekmatra prayog (ped)
```
**Recommendation:** Sabha ke liye do raaste —
(A) **Text-consistent:** Shakuni ke paase **sone aur vaidurya ke** (Virata 4.6.1 ki tarah) — royal, chamakte hue;
(B) **Vedic-historical:** vibhītaka nuts (Rigveda 10.34 ke "vibhīdaka").
Dono BORI ke *khilaaf* nahi hain, lekin screen/title par "BORI 2.53 Vibhitaka" **mat likhna**. Teaser assets already vibhītaka hain to (B) rakh sakte hain — sirf caption: "वैदिक परंपरा पर आधारित डिज़ाइन".

### 2.6 Magha Shukla IS in BORI (13.153.28)
```
13153027a aṣṭapañcāśataṁ rātryaḥ śayānasyādya me gatāḥ
13153028a māgho ’yaṁ samanuprāpto māsaḥ puṇyo yudhiṣṭhira
13153028c tribhāgaśeṣaḥ pakṣo ’yaṁ śuklo bhavitum arhati
```
Sirf "ashtami" shabd nahi hai; maas aur paksha CE mein hain.

### 2.7 Ekalavya — Arjuna ka role (1.123.26–39)
```
01123027c bhavatokto na me śiṣyas tvadviśiṣṭo bhaviṣyati
01123028c asty anyo bhavataḥ śiṣyo niṣādādhipateḥ sutaḥ
01123029c savyasācinam ādāya naiṣādiṁ prati jagmivān
01123037a tathaiva hr̥ṣṭavadanas tathaivādīnamānasaḥ
01123038c na tathā sa tu śīghro ’bhūd yathā pūrvaṁ narādhipa
01123039a tato ’rjunaḥ prītamanā babhūva vigatajvaraḥ
```
Ye BORI ka "kadva sach" hai — Rajamouli-style hero ko bhi grey dikhana is film ka USP banega. (Also 1.123.21: Ekalavya ki **śabdavedhī** kala — awaaz par nishana.)

### 2.8 Rangabhoomi — sahi kram + chhupe moti (1.126–1.127)
* 1.126.8: "**bhrātā bhrātaram ajñātam**" — narrator khud kehta hai: anjaan bhai ne bhai se kaha.
* 1.126.23–25: Indra ke badal Arjuna par chhaaya, Surya ne Karna ke upar ke badal hata diye — **ek par chhaaya, ek par dhoop**.
* 1.126.31: Kripa — "ye **Pritha ka chhota beta** hai" (Pritha ka bada beta saamne khada hai — dramatic irony).
* 1.126.33: Karna ka chehra "baarish se bheega kamal" jaisa jhuk gaya.
* 1.126.36: **sone ke peeth par, laja-pushp wale sone ke ghadon se** abhishek.
* 1.127.2–4: Adhiratha aata hai; Karna — **abhishek se geela sir** — jhukaata hai; Adhiratha "Putra!" keh kar wahi geela sir **aansuon se dobara bhigota** hai.
* 1.127.8: Bhima ke taane par Karna ke honth kaanpte hain, **aah bhar kar sooraj ko dekhta** hai.
* 1.127.18–21: sooraj doob jaata hai, mashaalein; log "Arjuna!", "Karna!", "Duryodhana!" kehte hue lautte hain.

### 2.9 Krishna's iconography
* CE ke 18 parva mein **mor-pankh ka zikr nahi** (wo Harivamsha/Bhagavata ki baal-leela iconography hai). Teaser Shot 19 ka "single real peacock feather" — strict BORI ke liye hata dein, ya consciously "trilogy signature" bana kar note mein likh dein.
* "Pītavāsas" (peela vastra) CE mein Vishnu/Krishna ke liye aata hai (1.58.50, 3.186.14) — rakh sakte hain.
* Dark skin ✓ (kṛṣṇa), halo nahi ✓.

---

## 3. Gemini files ki internal / production galtiyan

| # | File | Issue | Fix |
|---|---|---|---|
| P1 | Teaser Shot 01 + Music prompts | "**bronze conch**" — shankh kaansa nahi, **samudri seep (Turbinella pyrum)** hai | "ancient sacred white conch shell (shankha), chipped calcite, worn copper rim fitting" |
| P2 | Teaser + Audit Bible | MB_REF numbering clash: Audit Bible me Karna = `MB_REF_08`, Krishna = `MB_REF_13`; Teaser me Karna = `MB_REF_06`, Krishna = `MB_REF_04`, Bhima = `MB_REF_08` | Ek **single character-ID registry** (dekhein Master Bible §Character Registry) |
| P3 | Music / video prompts | "Hans Zimmer", "M.M. Keeravani", "S.S. Rajamouli" jaise **jeevit artist ke naam** — Google Flow/Music aksar refuse karte hain | Style shabdon mein likhein: "monumental Indian epic orchestral, deep male chorus, war drums" |
| P4 | Teaser VO | "यह युद्ध सिंहासन के लिए नहीं था" — yuddh rajya (Indraprastha/aadha Kuru rajya) ke liye bhi tha | "यह युद्ध **सिर्फ़** सिंहासन के लिए नहीं था…" |
| P5 | Teaser Shot 19 | Krishna ki line "धर्म जब मौन हो जाता है…" — CE mein nahi | "creative tagline" label; ya Part III ke Gita se koi asli bhaav lein |
| P6 | Screenplay | Bhishma "70 saal" — generational math se dyut-sabha tak Bhishma ~130+ ke hone chahiye (CE unhe "vṛddha", safed baal wale kehta hai) | Look: bahut vriddh par lohe jaisa majboot; "ageless warrior-patriarch" |
| P7 | Audit Bible | Ekalavya + bird test dono "1.123.59–66" | Ekalavya **1.123.10–39**; bird **1.123.46–67** |
| P8 | Screenplay Seq 05 | Kunti "lakdi ka katghara jakadti" ✓ creative; par "Vidura samajh gaye" ❌ | Vidura sirf hosh dilate hain |
| P9 | Screenplay Seq 10 | Khandava mein Krishna saarathi | Do rath (dekhein 2.4) |
| P10 | Screenplay Seq 14 | Draupadi "chune ke farsh par ghaseeti" ✓; "Pitamah se seedha prashn" ✓ creative; par Duhshasana ka "Krishna ko pukaar" taana (2.60.26) missing | Jod diya gaya |
| P11 | All | "Kurukshetra c. 1000 BCE" | Theek hai — **design-era** ke roop mein (PGW Iron Age), aitihasik daawa ke roop mein nahi |
| P12 | Drive PDF-1 | "Day 3 par Sudarshan" ✓ par "rath-pahiya sirf Bhagavata se" — asal mein CE khud **rathāṅga** shabd use karta hai (6.55.83, 94) | Footnote mein likhein |

---

## 4. Frame narrative — sabse strong BORI-faithful structure

1. **1.47.17–25** — Sarpasattra jal raha hai: ritwij **kaale vastra, dhuein se laal aankhein**; safed-kaale-neele, boodhe-bachche saanp cheekhte hue aag mein girte hain. (Ye shot Teaser ke "fire transition" se bhi zyada bhayanak aur asli hai.)
2. **1.47.14–16** — Yajna ki zameen naapte hue ek **sthapati (sūtradhāra)** bhavishyavaani karta hai: "ek brahman ke kaaran ye yajna poora nahi hoga" → foreshadow Astika.
3. **1.54.1** — Janamejaya dīkṣita hain; **Vyasa** aate hain.
4. **1.54.18–20** — Janamejaya ka prashn: "**kathaṁ samabhavad bhedaḥ … tac ca yuddhaṁ kathaṁ vṛttaṁ bhūtāntakaraṇaṁ mahat?**" — "Phoot kaise padi? Wo jeev-sanhaarak mahayuddh kaise hua?" → **yahi aapki demand ka textual aadhaar hai**: shankh + yuddh dikhao, phir poocho "ye sab shuru kahan se hua?"
5. **1.54.21–24** — Vyasa Vaishampayana ko aagya dete hain; katha shuru.
6. **18.5.26–29 (Part III finale)** — katha khatam; ritwij yajna poora karte hain; **Astika prasann — saanp mukt**; Janamejaya **Takshashila se Hastinapur** lautte hain; Vyasa ka **ūrdhvabāhu** naad (18.5.49). → Trilogy ka **bookend**: pratishodh ki aag se shuru, kshama par khatam.

---

## 5. Kya confirm hua (Gemini ✓) — short list
Lakshagraha 6 log (1.136.4) · Kanika App. I 81 · Nagaloka App. I 72–73 · bird "śiraḥ" · Karna rejection 1827\* · Ulupi 2029\* · Subhadra App. I 115 · Manalura coastal · Jarasandha back-break · Shishupala · Maya-sarovar laughers · Duryodhana's lie · vastra 2.61.40–41 + 544\*/553\* · 2 boons · 4 vows 2.68 · 5.129 sight · Durvasa/Urvashi/Karna-digvijaya/Durga-stotra appendices · Brihannala · Kavach daan · Day 3/9 · Day 14 sunset · kuñjara · 9.57.18 · 9.61 · 3,000-yr curse · 58 nights · toll 11.26.9 · Krishna's death 16.5 · Takshashila 18.5.29 · ūrdhvabāhu 18.5.49 · Gandhari's toenail glance (11.15) · Bhishma-Karna (6.117.9 Narada) · Abhimanyu "entry only" (7.34.19) · Dushasana blood (8.61).

## 6. Market/taboo research (Drive PDF-2) par meri raay
* Home-taboo debunk (Phalashruti 1.1.191–206, 1.56.14–20, 18.5.31–54) — Sanskrit maine check kiya: **1.56.19–20 aur 18.5.45–54 sahi hain**. "Episode 0" myth-busting launch video ka idea strong hai.
* OTT/market numbers (Netflix *Kurukshetra*, JioHotstar *Ek Dharmayudh*, box office) maine independently verify nahi kiye — script/BORI scope se bahar hain. Inhe public post mein use karne se pehle source khol kar ek baar dobara dekh lena.

---

## 7. Production guardrails (har scene par lagu)
1. **CE-first:** har plot beat ka adhyaya-shlok reference screenplay mein diya gaya hai.
2. **Creative layer ko label karo:** jo dialogue Sanskrit ka seedha bhavanuvaad hai unke aage `[CE]`, jo cinematic expansion hai unke aage `[CREATIVE]` (screenplays mein yahi system follow kiya hai).
3. **No fantasy glow:** divya ghatnaayein (phool-varsha, aakaashvani, vastra-vardhan, vishwaroop) — **prakritik/physical** tareeke se: hawa, roshni, dhool, dhuan, aawaz ka khalipan.
4. **Material culture:** PGW Iron Age (c. 1100–800 BCE) — mitti/kacchi-pakki eent, saal ki lakdi, chuna, hathkargha, sīna hua kapda nahi (antarīya/uttarīya), shankh = seep, rath = **arey-wale (spoked) pahiye**, ghode.
5. **Character continuity:** ek hi ID registry; umar ke stages Master Bible mein.
