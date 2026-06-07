#!/usr/bin/env python3
"""Generate espanol-en A1 vocabulary chapters."""

import os
import json
from pathlib import Path

BASE_PATH = Path("/home/user/wordplay/espanol-en/a1")
os.makedirs(BASE_PATH / "vocabulary", exist_ok=True)

VOCAB_DATA = {
    "adjectives-feelings": {
        "title": "Adjectives & Feelings",
        "words": [
            {"word": "happy", "ipa": "ˈhæpi", "def": "contento/alegre", "ex": "I am happy today."},
            {"word": "sad", "ipa": "sæd", "def": "triste/infeliz", "ex": "He feels sad."},
            {"word": "angry", "ipa": "ˈæŋɡri", "def": "enfadado/furioso", "ex": "She is angry."},
            {"word": "tired", "ipa": "ˈtaɪərd", "def": "cansado/fatigado", "ex": "I am tired now."},
            {"word": "excited", "ipa": "ɪkˈsaɪtɪd", "def": "emocionado/entusiasmado", "ex": "He is excited."},
            {"word": "scared", "ipa": "skɛrd", "def": "asustado/aterrado", "ex": "The dog is scared."},
            {"word": "nervous", "ipa": "ˈnɜːrvəs", "def": "nervioso/ansioso", "ex": "I am nervous."},
            {"word": "confused", "ipa": "kənˈfjuzd", "def": "confundido/desorientado", "ex": "She looks confused."},
            {"word": "bored", "ipa": "bɔːrd", "def": "aburrido/hastiado", "ex": "I am bored."},
            {"word": "proud", "ipa": "praʊd", "def": "orgulloso/satisfecho", "ex": "He is proud."},
        ]
    },
    "body": {
        "title": "Body Parts",
        "words": [
            {"word": "head", "ipa": "hɛd", "def": "cabeza", "ex": "I have a headache."},
            {"word": "arm", "ipa": "ɑːrm", "def": "brazo", "ex": "My arm hurts."},
            {"word": "leg", "ipa": "lɛɡ", "def": "pierna", "ex": "I have long legs."},
            {"word": "hand", "ipa": "hænd", "def": "mano", "ex": "Wash your hands."},
            {"word": "foot", "ipa": "fʊt", "def": "pie", "ex": "My foot is cold."},
            {"word": "eye", "ipa": "aɪ", "def": "ojo", "ex": "She has blue eyes."},
            {"word": "ear", "ipa": "ɪər", "def": "oído/oreja", "ex": "My ear hurts."},
            {"word": "nose", "ipa": "noʊz", "def": "nariz", "ex": "Your nose is red."},
            {"word": "mouth", "ipa": "maʊθ", "def": "boca", "ex": "Open your mouth."},
            {"word": "stomach", "ipa": "ˈstʌmək", "def": "estómago", "ex": "I have a stomachache."},
        ]
    },
    "clothes": {
        "title": "Clothes",
        "words": [
            {"word": "shirt", "ipa": "ʃɜːrt", "def": "camisa", "ex": "He wears a blue shirt."},
            {"word": "pants", "ipa": "pænts", "def": "pantalones", "ex": "These pants fit well."},
            {"word": "dress", "ipa": "drɛs", "def": "vestido", "ex": "She wore a red dress."},
            {"word": "shoes", "ipa": "ʃuz", "def": "zapatos", "ex": "My shoes are black."},
            {"word": "hat", "ipa": "hæt", "def": "sombrero", "ex": "He wears a hat."},
            {"word": "jacket", "ipa": "ˈdʒækɪt", "def": "chaqueta", "ex": "I need a jacket."},
            {"word": "socks", "ipa": "sɑːks", "def": "calcetines", "ex": "Where are my socks?"},
            {"word": "skirt", "ipa": "skɜːrt", "def": "falda", "ex": "She wears a short skirt."},
            {"word": "coat", "ipa": "koʊt", "def": "abrigo", "ex": "Wear a coat."},
            {"word": "sweater", "ipa": "ˈswɛtər", "def": "suéter/jersey", "ex": "This sweater is warm."},
        ]
    },
    "daily-routines": {
        "title": "Daily Routines",
        "words": [
            {"word": "wake up", "ipa": "weɪk ʌp", "def": "despertarse", "ex": "I wake up at 7."},
            {"word": "breakfast", "ipa": "ˈbrɛkfəst", "def": "desayuno", "ex": "I eat breakfast."},
            {"word": "shower", "ipa": "ˈʃaʊər", "def": "ducha/bañarse", "ex": "I take a shower."},
            {"word": "brush", "ipa": "brʌʃ", "def": "cepillar", "ex": "I brush my teeth."},
            {"word": "get dressed", "ipa": "ɡɛt drɛst", "def": "vestirse", "ex": "She gets dressed."},
            {"word": "go to work", "ipa": "ɡoʊ tə wɜːrk", "def": "ir al trabajo", "ex": "I go to work at 8."},
            {"word": "lunch", "ipa": "lʌntʃ", "def": "almuerzo", "ex": "We eat lunch at noon."},
            {"word": "dinner", "ipa": "ˈdɪnər", "def": "cena", "ex": "Dinner is at 7."},
            {"word": "sleep", "ipa": "slip", "def": "dormir", "ex": "I sleep 8 hours."},
            {"word": "rest", "ipa": "rɛst", "def": "descansar", "ex": "I rest in the afternoon."},
        ]
    },
    "food-and-drink": {
        "title": "Food & Drink",
        "words": [
            {"word": "apple", "ipa": "ˈæpəl", "def": "manzana", "ex": "I like red apples."},
            {"word": "bread", "ipa": "brɛd", "def": "pan", "ex": "I eat bread for breakfast."},
            {"word": "milk", "ipa": "mɪlk", "def": "leche", "ex": "I drink milk."},
            {"word": "water", "ipa": "ˈwɔːtər", "def": "agua", "ex": "Drink water."},
            {"word": "coffee", "ipa": "ˈkɔːfi", "def": "café", "ex": "I drink coffee."},
            {"word": "rice", "ipa": "raɪs", "def": "arroz", "ex": "She cooks rice."},
            {"word": "chicken", "ipa": "ˈtʃɪkən", "def": "pollo", "ex": "I eat chicken."},
            {"word": "fish", "ipa": "fɪʃ", "def": "pescado/pez", "ex": "Fish is healthy."},
            {"word": "vegetables", "ipa": "ˈvɛdʒtəbəlz", "def": "verduras", "ex": "Eat your vegetables."},
            {"word": "fruit", "ipa": "frut", "def": "fruta", "ex": "I like fruit."},
        ]
    },
    "house-and-home": {
        "title": "House & Home",
        "words": [
            {"word": "bedroom", "ipa": "ˈbɛdrum", "def": "dormitorio", "ex": "My bedroom is upstairs."},
            {"word": "kitchen", "ipa": "ˈkɪtʃən", "def": "cocina", "ex": "We cook in the kitchen."},
            {"word": "bathroom", "ipa": "ˈbæθrum", "def": "baño", "ex": "The bathroom is clean."},
            {"word": "living room", "ipa": "ˈlɪvɪŋ rum", "def": "sala de estar", "ex": "We sit in the living room."},
            {"word": "door", "ipa": "dɔːr", "def": "puerta", "ex": "Close the door."},
            {"word": "window", "ipa": "ˈwɪndoʊ", "def": "ventana", "ex": "Open the window."},
            {"word": "table", "ipa": "ˈteɪbəl", "def": "mesa", "ex": "Sit at the table."},
            {"word": "chair", "ipa": "tʃɛr", "def": "silla", "ex": "This chair is comfortable."},
            {"word": "bed", "ipa": "bɛd", "def": "cama", "ex": "My bed is soft."},
            {"word": "sofa", "ipa": "ˈsoʊfə", "def": "sofá", "ex": "Sit on the sofa."},
        ]
    },
    "jobs-and-occupations": {
        "title": "Jobs & Occupations",
        "words": [
            {"word": "teacher", "ipa": "ˈtitʃər", "def": "profesor/maestra", "ex": "She is a teacher."},
            {"word": "doctor", "ipa": "ˈdɑːktər", "def": "médico/doctor", "ex": "He is a doctor."},
            {"word": "nurse", "ipa": "nɜːrs", "def": "enfermera/enfermero", "ex": "She works as a nurse."},
            {"word": "farmer", "ipa": "ˈfɑːrmər", "def": "granjero/agricultor", "ex": "He is a farmer."},
            {"word": "baker", "ipa": "ˈbeɪkər", "def": "panadero", "ex": "She is a baker."},
            {"word": "chef", "ipa": "ʃɛf", "def": "chef/cocinero", "ex": "He is a chef."},
            {"word": "police officer", "ipa": "pəˈlis ˈɔːfɪsər", "def": "policía", "ex": "She is a police officer."},
            {"word": "firefighter", "ipa": "ˈfaɪrfaɪtər", "def": "bombero", "ex": "He is a firefighter."},
            {"word": "engineer", "ipa": "ˌɛndʒɪˈnɪr", "def": "ingeniero/ingeniera", "ex": "She is an engineer."},
            {"word": "artist", "ipa": "ˈɑːrtɪst", "def": "artista", "ex": "He is an artist."},
        ]
    },
    "numbers-and-time": {
        "title": "Numbers & Time",
        "words": [
            {"word": "one", "ipa": "wʌn", "def": "uno", "ex": "I have one apple."},
            {"word": "two", "ipa": "tu", "def": "dos", "ex": "I have two cats."},
            {"word": "three", "ipa": "θri", "def": "tres", "ex": "I have three dogs."},
            {"word": "ten", "ipa": "tɛn", "def": "diez", "ex": "There are ten students."},
            {"word": "hour", "ipa": "ˈaʊər", "def": "hora", "ex": "One hour has passed."},
            {"word": "minute", "ipa": "ˈmɪnɪt", "def": "minuto", "ex": "Wait a minute."},
            {"word": "morning", "ipa": "ˈmɔːrnɪŋ", "def": "mañana", "ex": "Good morning!"},
            {"word": "afternoon", "ipa": "ˌæftərˈnun", "def": "tarde", "ex": "Good afternoon."},
            {"word": "evening", "ipa": "ˈivnɪŋ", "def": "noche", "ex": "Good evening."},
            {"word": "night", "ipa": "naɪt", "def": "noche/madrugada", "ex": "Good night."},
        ]
    },
    "places-in-town": {
        "title": "Places in Town",
        "words": [
            {"word": "school", "ipa": "skul", "def": "escuela", "ex": "I go to school."},
            {"word": "hospital", "ipa": "ˈhɑːspɪtəl", "def": "hospital", "ex": "She works at the hospital."},
            {"word": "restaurant", "ipa": "ˈrɛstərɑːnt", "def": "restaurante", "ex": "Let's go to a restaurant."},
            {"word": "supermarket", "ipa": "ˈsupərˌmɑːrkɪt", "def": "supermercado", "ex": "I shop at the supermarket."},
            {"word": "park", "ipa": "pɑːrk", "def": "parque", "ex": "Let's go to the park."},
            {"word": "church", "ipa": "tʃɜːrtʃ", "def": "iglesia", "ex": "We go to church."},
            {"word": "bank", "ipa": "bæŋk", "def": "banco", "ex": "I go to the bank."},
            {"word": "post office", "ipa": "poʊst ˈɑːfɪs", "def": "correo", "ex": "I send a letter at the post office."},
            {"word": "library", "ipa": "ˈlaɪbreri", "def": "biblioteca", "ex": "I read at the library."},
            {"word": "market", "ipa": "ˈmɑːrkɪt", "def": "mercado", "ex": "We go to the market."},
        ]
    },
}

TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>{title} — Flashcards | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css?v=v124">
<script src="/shared/auth.js?v=1"></script>
<script src="../../../../shared/dark-init.js?v=v112"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">◐ Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../../../index.html">Home</a><span>›</span><a href="../../index.html">A1</a><span>›</span><a href="../index.html">Vocabulary</a><span>›</span><a href="index.html">{title}</a><span>›</span><strong>Flashcards</strong>
  </div>
  <div class="vocab-page">
    <div id="masteryBadge" style="margin:12px 0;display:none"><span class="mastery-badge">Topic mastered</span></div>
    <div style="font-family:var(--font-sans);font-size:.75rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin-bottom:16px">{word_count} words · tap card to reveal</div>
    <div class="mode-tabs">
      <button class="mode-tab active" onclick="setMode('flash',this)">Flashcards</button>
      <button class="mode-tab" onclick="setMode('match',this)">Match</button>
      <button class="mode-tab" onclick="setMode('list',this)">Word list</button>
    </div>
    <div id="modeFlash">
      <div class="flashcard-wrap">
        <button class="flashcard" id="flashcard" onclick="flipCard()">
          <div class="fc-face fc-front">
            <div class="fc-word" id="fcWord"></div>
            <div class="fc-ipa" id="fcIpa"></div>
            <button class="fc-audio-btn" onclick="speakWord(event)">▶ Pronounce</button>
            <div class="fc-hint">tap to reveal</div>
          </div>
          <div class="fc-face fc-back">
            <div class="fc-def" id="fcDef"></div>
            <div style="margin-top:8px;font-size:.75rem;color:var(--muted)"><em id="fcEx"></em></div>
          </div>
        </button>
      </div>
      <div style="text-align:center;margin-bottom:20px">
        <button class="fc-btn" onclick="fcPrev()">← Prev</button>
        <span class="fc-counter" id="fcCounter"></span>
        <button class="fc-btn" onclick="fcNext()">Next →</button>
      </div>
      <div style="text-align:center">
        <button class="fc-btn primary" onclick="markMastered()" id="btnMastered">Mark topic as mastered</button>
      </div>
    </div>
    <div id="modeMatch" style="display:none">
      <div class="match-score" id="matchScore">Match each word to its definition</div>
      <div class="match-grid">
        <div class="match-col" id="matchWords"></div>
        <div class="match-col" id="matchDefs"></div>
      </div>
      <div style="text-align:center">
        <button class="fc-btn" onclick="initMatch()">New round</button>
      </div>
    </div>
    <div id="modeList" style="display:none">
      <table style="width:100%;border-collapse:collapse">
        <tr style="border-bottom:1px solid var(--hairline)">
          <th style="padding:8px;text-align:left;font-weight:600">Word</th>
          <th style="padding:8px;text-align:left;font-weight:600">IPA</th>
          <th style="padding:8px;text-align:left;font-weight:600">Definition</th>
        </tr>
        <tbody id="wordList"></tbody>
      </table>
    </div>
  </div>
</div>
<footer class="site-footer">Word Play · Spanish A1 · Vocabulary</footer>
<script src="../../../../shared/store.js?v=v107"></script>
<script>
var SLUG = '{slug}';
var LEVEL = 'a1';
var MASTERY_KEY = 'wordplay_vocab_a1_' + SLUG + '_mastered';
var WORDS = {words_json};
var fcIdx = 0, flipped = false;
function setMode(mode, btn) {{
  document.querySelectorAll('.mode-tab').forEach(function(b){{b.classList.remove('active');}});
  btn.classList.add('active');
  document.getElementById('modeFlash').style.display = mode==='flash'?'':'none';
  document.getElementById('modeMatch').style.display = mode==='match'?'':'none';
  document.getElementById('modeList').style.display = mode==='list'?'':'none';
  if(mode==='match') initMatch();
  if(mode==='list') renderList();
}}
function flipCard(){{flipped=!flipped;document.getElementById('flashcard').classList.toggle('flipped',flipped);}}
function showCard(idx){{flipped=false;document.getElementById('flashcard').classList.remove('flipped');var w=WORDS[idx];document.getElementById('fcWord').textContent=w.word;document.getElementById('fcIpa').textContent=w.ipa;document.getElementById('fcDef').textContent=w.def;document.getElementById('fcEx').textContent=w.ex;document.getElementById('fcCounter').textContent=(idx+1)+' / '+WORDS.length;fcSeen.add(idx);if(!mastered&&fcSeen.size>=WORDS.length){{mastered=true;setTimeout(markMastered,700);}}}}
function fcNext(){{fcIdx=(fcIdx+1)%WORDS.length;showCard(fcIdx);}}
function fcPrev(){{fcIdx=(fcIdx-1+WORDS.length)%WORDS.length;showCard(fcIdx);}}
function markMastered(){{try{{localStorage.setItem(MASTERY_KEY,'1');}}catch(e){{}}}document.getElementById('masteryBadge').style.display='block';var btn=document.getElementById('btnMastered');btn.textContent='Mastered!';btn.disabled=true;}}
function checkMastered(){{try{{if(localStorage.getItem(MASTERY_KEY)==='1'){{document.getElementById('masteryBadge').style.display='block';var btn=document.getElementById('btnMastered');btn.textContent='Mastered!';btn.disabled=true;}}}}catch(e){{}}}}}
var matchSelected=null;function shuffle(a){{var b=a.slice();for(var i=b.length-1;i>0;i--){{var j=Math.floor(Math.random()*(i+1));var t=b[i];b[i]=b[j];b[j]=t;}}return b;}}
function initMatch(){{var sample=shuffle(WORDS).slice(0,6);var words=shuffle(sample.map(function(w){{return{{id:w.word,text:w.word,type:'word'}};}}));var defs=shuffle(sample.map(function(w){{return{{id:w.word,text:w.def,type:'def'}};}}));matchSelected=null;document.getElementById('matchScore').textContent='Match each word to its definition';function renderCol(col,items){{col.innerHTML='';items.forEach(function(item){{var el=document.createElement('div');el.className='match-item';el.textContent=item.text;el.dataset.id=item.id;el.dataset.type=item.type;el.addEventListener('click',handleMatch);col.appendChild(el);}});}}renderCol(document.getElementById('matchWords'),words);renderCol(document.getElementById('matchDefs'),defs);}}
function handleMatch(e){{var el=e.currentTarget;if(el.classList.contains('correct'))return;if(!matchSelected){{if(matchSelected&&matchSelected!==el)matchSelected.classList.remove('selected');matchSelected=el;el.classList.add('selected');}}else{{var prev=matchSelected;matchSelected=null;var correct=prev.dataset.id===el.dataset.id&&prev.dataset.type!==el.dataset.type;if(correct){{prev.classList.remove('selected');prev.classList.add('correct');el.classList.add('correct');var remaining=document.querySelectorAll('.match-item:not(.correct)').length;if(remaining===0){{document.getElementById('matchScore').textContent='All matched!';completedRounds++;if(!mastered&&completedRounds>=5){{mastered=true;setTimeout(markMastered,700);}}}}}}else{{prev.classList.remove('selected');prev.classList.add('wrong');el.classList.add('wrong');setTimeout(function(){{prev.classList.remove('wrong');el.classList.remove('wrong');}},600);}}matchSelected=null;}}}}
function renderList(){{var html=WORDS.map(function(w){{return'<tr style="border-bottom:1px solid var(--hairline)"><td style="padding:8px;font-weight:600">'+w.word+'</td><td style="padding:8px;color:var(--muted);font-size:.82rem">'+w.ipa+'</td><td style="padding:8px;font-size:.88rem">'+w.def+'</td></tr>';}}).join('');document.getElementById('wordList').innerHTML=html;}}
function speakWord(e){{if(e)e.stopPropagation();if(!window.speechSynthesis)return;var utt=new SpeechSynthesisUtterance(WORDS[fcIdx].word);utt.lang='es-ES';utt.rate=0.9;window.speechSynthesis.cancel();window.speechSynthesis.speak(utt);}}
var mastered=false;var fcSeen=new Set();var completedRounds=0;showCard(0);checkMastered();
</script>
</body>
</html>"""

# Generate vocabulary chapters
count = 0
for slug, data in VOCAB_DATA.items():
    chapter_dir = BASE_PATH / "vocabulary" / slug
    chapter_dir.mkdir(parents=True, exist_ok=True)

    words_json = json.dumps(data["words"])
    html = TEMPLATE_HTML.format(
        title=data["title"],
        slug=slug,
        word_count=len(data["words"]),
        words_json=words_json
    )

    with open(chapter_dir / "flashcards.html", "w") as f:
        f.write(html)

    count += 1

print("✓ Generated {} espanol-en A1 vocabulary chapters".format(count))
