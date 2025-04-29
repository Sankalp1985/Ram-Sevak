from flask import Flask, render_template

app = Flask(__name__)

chalisa = [
 {"verse": "श्रीगुरु चरन सरोज रज, निज मनु मुकुरु सुधारि।", "meaning": "With the dust of Sri Guru's lotus feet, I cleanse the mirror of my mind.", "hindi": "Guruji ke charno ki dhool se main apne mann ka aaina saaf karta hoon."},
    {"verse": "बरनऊँ रघुबर बिमल जसु, जो दायकु फल चारि॥", "meaning": "I sing the pure glory of Lord Rama, which bestows the four fruits of life — Dharma, Artha, Kama, and Moksha.", "hindi": "Main Raghukul ke shresth Ramji ke pavitra gun gaata hoon jo chaar phal dete hain – dharm, arth, kaam aur moksh."},
    {"verse": "बुद्धिहीन तनु जानिके, सुमिरौं पवनकुमार।", "meaning": "Knowing that I am lacking wisdom, I remember the son of the wind, Hanuman.", "hindi": "Apne aap ko buddhi se kam samajhkar main Pawanputra Hanuman ka smaran karta hoon."},
    {"verse": "बल बुद्धि विद्या देहु मोहिं, हरहु कलेस विकार॥", "meaning": "Grant me strength, wisdom, and knowledge, and remove my sorrows and impurities.", "hindi": "Hanumanji, mujhe bal, buddhi aur gyaan dijiye, aur mere dukh aur bure vichar door kijiye."},
    {"verse": "जय हनुमान ज्ञान गुण सागर।", "meaning": "Victory to Hanuman, the ocean of knowledge and virtue.", "hindi": "Jay Ho Hanuman, gyaan aur gun ke sagar."},
    {"verse": "जय कपीस तिहुँ लोक उजागर॥", "meaning": "Victory to the King of Monkeys, who is famous in all three worlds.", "hindi": "Jay Ho Hanuman, jo teenon lokon mein prasiddh hain."},
    {"verse": "राम दूत अतुलित बल धामा।", "meaning": "Messenger of Rama, abode of incomparable strength.", "hindi": "Ramji ke sandeshvahak, anant bal ke malik."},
    {"verse": "अंजनि-पुत्र पवनसुत नामा॥", "meaning": "Son of Anjani, also called the son of the wind.", "hindi": "Anjani ki santan, Pawanputra."},
    {"verse": "महाबीर बिक्रम बजरंगी।", "meaning": "Great warrior, mighty and strong like a thunderbolt.", "hindi": "Mahan veer, bijli jaise shaktiwan."},
    {"verse": "कुमति निवार सुमति के संगी॥", "meaning": "Remover of evil thoughts, companion of good sense and wisdom.", "hindi": "Bure vichar ko door karne wale, achhe vichar ke saathi."},
    {"verse": "कंचन बरन बिराज सुबेसा।", "meaning": "Golden in complexion, splendidly dressed.", "hindi": "Sone jaise rang ke, shobhit pehene wale."},
    {"verse": "कानन कुंडल कुंचित केसा॥", "meaning": "Wearing earrings, with curly hair.", "hindi": "Kaale ghungroo, gungunahat ke baal."},
    {"verse": "हाथ वज्र औ ध्वजा बिराजै।", "meaning": "He holds a thunderbolt and a flag in his hands.", "hindi": "Unke haath mein vajra aur dhwaja hai."},
    {"verse": "काँधे मूँज जनेऊ साजै॥", "meaning": "Wears the sacred thread made of munja grass over his shoulder.", "hindi": "Unke kandhe par munja ka jineu hai."},
    {"verse": "शंकर सुवन केसरी नंदन।", "meaning": "Incarnation of Lord Shiva, son of Kesari.", "hindi": "Shankar ji ka avatar, Kesari ka putra."},
    {"verse": "तेज प्रताप महा जग वंदन॥", "meaning": "Full of radiance and glory, worshipped throughout the world.", "hindi": "Tez aur prakash se bhare, poore jagat mein puje jaane wale."},
    {"verse": "विद्यावान गुणी अति चातुर।", "meaning": "Knower of all knowledge, virtuous and extremely clever.", "hindi": "Gyaan aur guno ka dhani, ati chatur."},
    {"verse": "राम काज करिबे को आतुर॥", "meaning": "Always eager to carry out Lord Rama's work.", "hindi": "Hamesha Ram ji ka kaam karne ke liye utavle."},
    {"verse": "प्रभु चरित्र सुनिबे को रसिया।", "meaning": "Loves to hear stories of Lord Rama.", "hindi": "Ram ji ki kahaniyon ko sunna pasand karte hain."},
    {"verse": "राम लखन सीता मन बसिया॥", "meaning": "Rama, Lakshmana, and Sita dwell in his heart.", "hindi": "Ram, Laxman, aur Sita unke mann mein baste hain."},
    {"verse": "सूक्ष्म रूप धरि सियहिं दिखावा।", "meaning": "He took a tiny form to appear before Sita.", "hindi": "Unhone Sita ji ke saamne chhota roop dharan kiya."},
    {"verse": "विकट रूप धरि लंक जरावा॥", "meaning": "Took a terrible form to burn Lanka.", "hindi": "Unhone Lanka ko jalane ke liye bhayankar roop dharan kiya."},
    {"verse": "भीम रूप धरि असुर संहारे।", "meaning": "In a monstrous form, he destroyed demons.", "hindi": "Bhayankar roop mein asuron ko nasht kiya."},
    {"verse": "रामचंद्र के काज सँवारे॥", "meaning": "Accomplished all tasks for Lord Rama.", "hindi": "Ram ji ke saare kaam poore kiye."},
    {"verse": "लाय सजीवन लखन जियाए।", "meaning": "Brought the Sanjeevani herb to revive Lakshmana.", "hindi": "Lakshman ji ko jeevit karne ke liye Sanjeevani booti laaye."},
    {"verse": "श्री रघुबीर हरषि उर लाए॥", "meaning": "Rama embraced him joyfully.", "hindi": "Ram ji ne unhe khushi se apne dil se lagaya."},
    {"verse": "रघुपति कीन्ही बहुत बड़ाई।", "meaning": "Lord Rama praised him greatly.", "hindi": "Ram ji ne unki prashansa ki."},
    {"verse": "तुम मम प्रिय भरत सम भाई॥", "meaning": "He said- You are as dear to me as my brother Bharat", "hindi": "Unhone kaha, Tum mere liye mere bhai Bharat jaise ho."},
	{'verse': 'सहस बदन तुम्हरो जस गावैं।', 'meaning': 'Thousands of mouths sing your glory.', 'hindi': 'Hazaaron muh se tumhari mahima gaayi jaati hai.'},
	{'verse': 'अस कहि श्रीपति कंठ लगावैं॥', 'meaning': 'Saying this, Lord Vishnu embraced him.', 'hindi': 'Aise keh kar Shri Vishnu ne unhe apne kandhe se laga liya.'},
	{'verse': 'सनकादिक ब्रह्मादि मुनीसा।', 'meaning': 'Sages like Sanaka, Brahma, and other sages...', 'hindi': 'Sanakadi Rishi aur Brahma ji jaise mahan rishiyon ne unki mahima gaayi.'},
	{'verse': 'नारद सारद सहित अहीसा॥', 'meaning': '...as well as Narada, Saraswati, and Sheshnag sing your praise.', 'hindi': 'Narad, Saraswati aur Sheshnag bhi tumhari stuti karte hain.'},
	{'verse': 'यम कुबेर दिकपाल जहाँ ते।', 'meaning': 'Yama, Kubera, and the guardians of the directions...', 'hindi': 'Yamraj, Kubera aur disha ke devta bhi tumhari mahima gaate hain.'},
	{'verse': 'कवि कोबिद कहि सके कहाँ ते॥', 'meaning': '...even the best poets cannot describe your glory.', 'hindi': 'Beshumar kaviyon ke liye bhi tumhari mahima varnan karna mushkil hai.'},
	{'verse': 'तुम उपकार सुग्रीवहिं कीन्हा।', 'meaning': 'You helped Sugriva immensely.', 'hindi': 'Sugriv ko tumne kaafi madad ki thi.'},
	{'verse': 'राम मिलाय राजपद दीन्हा॥', 'meaning': 'You introduced him to Rama and got him his kingdom back.', 'hindi': 'Ram ji se milakar, Sugriv ko rajpada dilaya.'},
	{'verse': 'तुम्हरो मंत्र विभीषण माना।', 'meaning': 'Vibhishana followed your advice...', 'hindi': 'Vibhishan ne tumhare updesh ko maana.'},
	{'verse': 'लंकेश्वर भये सब जग जाना॥', 'meaning': '...and became the king of Lanka, known to all.', 'hindi': 'Aur Lanka ke raja ban gaye, sabhi ne jaana.'},
	
  {
    "verse": "जुग सहस्र जोजन पर भानू।",
    "meaning": "The sun is thousands of leagues away...",
    "hindi": "Suraj hazaron yojan door hai..."
  },
  {
    "verse": "लील्यो ताहि मधुर फल जानू॥",
    "meaning": "...yet you leapt and swallowed it thinking it was a sweet fruit.",
    "hindi": "Lekin aapne use meetha phal samajh kar nigal liya."
  },
  {
    "verse": "प्रभु मुद्रिका मेलि मुख माहीं।",
    "meaning": "You carried Lord Rama’s ring in your mouth...",
    "hindi": "Aapne Bhagwan Ram ki mudrika apne muh mein rakh li thi."
  },
  {
    "verse": "जलधि लांघि गए अचरज नाहीं॥",
    "meaning": "...crossed the ocean—what a wonder!",
    "hindi": "Aapne samudra ko paar kiya — koi aashcharya nahi."
  },
  {
    "verse": "दुर्गम काज जगत के जेते।",
    "meaning": "All difficult tasks in this world...",
    "hindi": "Yeh duniya ke saare kathin kaam..."
  },
  {
    "verse": "सुगम अनुग्रह तुम्हरे तेते॥",
    "meaning": "...become easy with your grace.",
    "hindi": "...aapke anugrah se asaan ho jaate hain."
  },
  {
    "verse": "राम दुआरे तुम रखवारे।",
    "meaning": "You are the gatekeeper of Lord Rama.",
    "hindi": "Aap hi Bhagwan Ram ke dwarpali hain."
  },
  {
    "verse": "होत न आज्ञा बिनु पैसारे॥",
    "meaning": "None may enter without your permission.",
    "hindi": "Aapki anumati ke bina koi bhi pravesh nahi kar sakta."
  },
  {
    "verse": "सब सुख लहै तुम्हारी सरना।",
    "meaning": "All happiness comes to those who take shelter in you.",
    "hindi": "Jo aapki sharan mein aate hain, unhe saare sukh milte hain."
  },
  {
    "verse": "तुम रक्षक काहू को डर ना॥",
    "meaning": "When you protect, there is no fear.",
    "hindi": "Aapki raksha se kisi ko bhi dar nahi hota."
  },
  {
    "verse": "आपन तेज सम्हारो आपै।",
    "meaning": "You keep your great power under control...",
    "hindi": "Aap apni mahan shakti ko apne niyantran mein rakhte hain."
  },
  {
    "verse": "तीनों लोक हाँक तें काँपै॥",
    "meaning": "...but your roar makes the three worlds tremble.",
    "hindi": "...lekin aapki garaj se teenon lok kamp uthte hain."
  },
  {
    "verse": "भूत पिशाच निकट नहिं आवै।",
    "meaning": "Ghosts and evil spirits do not come near...",
    "hindi": "Bhoot aur pret aapke paas nahi aa sakte."
  },
  {
    "verse": "महाबीर जब नाम सुनावै॥",
    "meaning": "...when one chants the name of the mighty Hanuman.",
    "hindi": "Jab koi mahaaveer Hanuman ka naam sunta hai."
  },
  {
    "verse": "नासै रोग हरै सब पीरा।",
    "meaning": "Diseases and pain are removed...",
    "hindi": "Rog aur dard door ho jaate hain..."
  },
  {
    "verse": "जपत निरंतर हनुमत बीरा॥",
    "meaning": "...by constantly chanting your name.",
    "hindi": "...jab koi aapka naam nirantar jaap karta hai."
  },
  {
    "verse": "संकट तें हनुमान छुड़ावै।",
    "meaning": "Hanuman removes all troubles...",
    "hindi": "Hanuman sabhi kathinaiyon se mukti dilate hain..."
  },
  {
    "verse": "मन क्रम बचन ध्यान जो लावै॥",
    "meaning": "...for those who meditate on him with heart, action, and speech.",
    "hindi": "...jo man, karm aur vachan se unka dhyaan lagate hain."
  },
  {
    "verse": "सब पर राम तपस्वी राजा।",
    "meaning": "Lord Rama is the supreme ascetic king...",
    "hindi": "Bhagwan Ram sabse mahan tapasi raja hain..."
  },
  {
    "verse": "तिन के काज सकल तुम साजा॥",
    "meaning": "...you fulfilled all his tasks.",
    "hindi": "...aapne unke saare kaam poore kiye."
  },
  {
    "verse": "और मनोरथ जो कोई लावै।",
    "meaning": "Whoever comes with desires...",
    "hindi": "Jo koi manokamna le kar aata hai..."
  },
  {
    "verse": "सोई अमित जीवन फल पावै॥",
    "meaning": "...attains immense fruits in life.",
    "hindi": "...uski jeevan mein anant phal milte hain."
  },
  {
    "verse": "चारों जुग परताप तुम्हारा।",
    "meaning": "Your greatness shines in all four ages.",
    "hindi": "Aapki mahima chaaron yugon mein chamakti hai."
  },
  {
    "verse": "है परसिद्ध जगत उजियारा॥",
    "meaning": "Your fame illuminates the world.",
    "hindi": "Aapki prashansha duniya ko roshan karti hai."
  },
  {
    "verse": "साधु संत के तुम रखवारे।",
    "meaning": "You protect saints and sages...",
    "hindi": "Aap sadhu-sants ke rakshak hain..."
  },
  {
    "verse": "असुर निकंदन राम दुलारे॥",
    "meaning": "...destroy demons, and are dear to Rama.",
    "hindi": "...aap asuron ka vinasht karte hain aur Ram ke priya hain."
  },
  {
    "verse": "अष्ट सिद्धि नव निधि के दाता।",
    "meaning": "You are the giver of eight siddhis and nine treasures...",
    "hindi": "Aap aath siddhiyon aur nau nidhi ka daata hain..."
  },
  {
    "verse": "अस बर दीन जानकी माता॥",
    "meaning": "...as granted by Mother Sita.",
    "hindi": "...jo Mata Sita ne diya hai."
  },
  {
    "verse": "राम रसायन तुम्हरे पासा।",
    "meaning": "You have the essence of devotion to Rama.",
    "hindi": "Aapke paas Ram ki bhakti ka ras hai."
  },
  {
    "verse": "सदा रहो रघुपति के दासा॥",
    "meaning": "Always remain the humble servant of Lord Rama.",
    "hindi": "Sada Ram ke daas bane raho."
  },
  {
    "verse": "तुमhare भजन राम को पावै।",
    "meaning": "By singing your praises, one finds Rama.",
    "hindi": "Aapke bhajan se hi Ram milte hain."
  },
  {
    "verse": "जनम जनम के दुख बिसरावै॥",
    "meaning": "Sorrow of many births is erased.",
    "hindi": "Janmon ke dukh door ho jaate hain."
  },
  {
    "verse": "अंत काल रघुबर पुर जाई।",
    "meaning": "At life’s end, one attains Rama’s abode.",
    "hindi": "Jeevan ke ant mein Ram ki vasati milti hai."
  },
  {
    "verse": "जहाँ जन्म हरि-भक्त कहाई॥",
    "meaning": "And is reborn as a devotee of Hari.",
    "hindi": "Aur Hari ke bhakt ke roop mein janm lete hain."
  },
  {
    "verse": "और देवता चित्त न धरई।",
    "meaning": "I do not seek other gods...",
    "hindi": "Main kisi aur devta ka chintan nahi karta."
  },
  {
    "verse": "हनुमत सेइ सर्ब सुख करई॥",
    "meaning": "...serving Hanuman gives all happiness.",
    "hindi": "Hanuman ki seva se sabhi sukh milte hain."
  },
  {
    "verse": "संकट कटै मिटै सब पीरा।",
    "meaning": "All troubles end and pains are erased...",
    "hindi": "Sab kathinaaiyan aur dard door ho jaate hain..."
  },
  {
    "verse": "जो सुमिरै हनुमत बलबीरा॥",
    "meaning": "...by remembering Hanuman, the mighty hero.",
    "hindi": "Hanuman, jo maha veer hain, unka smaran karne se."
  },
  {
    "verse": "जय जय जय हनुमान गोसाईं।",
    "meaning": "Victory, victory, victory to Lord Hanuman!",
    "hindi": "Jay Jay Jay Hanuman Goswami!"
  },
  {
    "verse": "कृपा करहु गुरुदेव की नाईं॥",
    "meaning": "Grant me your blessings like a true Guru.",
    "hindi": "Mujhe apni ashirwad dena jaise ek sachche guru karte hain."
  },
  {
    "verse": "जो सत बार पाठ कर कोई।",
    "meaning": "Whoever recites this 100 times...",
    "hindi": "Jo 100 baar iska paath karta hai..."
  },
  {
    "verse": "छूटहि बंदि महा सुख होई॥",
    "meaning": "...is freed from bondage and gains great joy.",
    "hindi": "...wo bandhan se mukt hota hai aur maha sukh prapt karta hai."
  },
  {
    "verse": "जो यह पढ़ै हनुमान चालीसा।",
    "meaning": "One who recites the Hanuman Chalisa...",
    "hindi": "Jo Hanuman Chalisa padhta hai..."
  },
  {
    "verse": "होय सिद्धि साखी गौरीसा॥",
    "meaning": "...attains perfection, witnessed by Lord Shiva.",
    "hindi": "...wo siddhi prapt karta hai, jo Bhagwan Shiva ke samarthan se hoti hai."
  },
  {
    "verse": "तुलसीदास सदा हरि चेरा।",
    "meaning": "Tulsidas is always a servant of the Lord.",
    "hindi": "Tulsidas sada Hari ke daas hain."
  },
  {
    "verse": "कीजै नाथ हृदय महँ डेरा॥",
    "meaning": "O Lord, dwell in my heart forever.",
    "hindi": "O Prabhu, hamesha mere hriday mein baso."
  },
  {
    "verse": "पवन तनय संकट हरन, मंगल मूरति रूप।",
    "meaning": "Son of the Wind, remover of troubles, embodiment of auspiciousness.",
    "hindi": "Pawan putra, sabhi dukhon ko door karne wale, mangal roop hain."
  },
  {
    "verse": "राम लखन सीता सहित, हृदय बसहु सुर भूप॥",
    "meaning": "May you dwell in my heart along with Rama, Lakshmana, and Sita.",
    "hindi": "hey Devtaon ke Raja, aap Ram, Laxman aur Sita ke saath mere hriday mein baso."
  }
]


@app.route("/")
def index():
    return render_template("index.html", chalisa=chalisa)

if __name__ == "__main__":
    app.run(debug=True)
