import random, os
eL = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
eP = ['eɪ (ei)', 'biː (bii)', 'siː (sii)', 'diː (dii)', 'iː (ii)', 'ɛf (ef)', 'dʒiː (ji)', 'eɪtʃ (eich), heɪtʃ (heich)', 'aɪ (ai)', 'dʒeɪ (jei)', 'keɪ (kei)', 'ɛl (el)', 'ɛm (em)', 'ɛn (en)', 'oʊ (ou)', 'piː (pi)', 'kjuː (kyu)', 'ɑːɹ (aar)', 'ɛs (es)', 'tiː (tii)', 'juː (yuu)', 'viː (vii)', 'dʌbəl.juː (dabel yu)', 'ɛks (eks)', 'waɪ (wai)', 'zɛd (zed)']
eN = ['a', 'bee', 'cee', 'dee', 'e', 'ef', 'jee', 'aitch, haitch', 'i', 'jay', 'kay', 'el', 'em', 'en', 'o', 'pee', 'cue, kew, kue, que', 'ar', 'ess', 'tee', 'u', 'vee', 'double-u', 'ex', 'wy, wye, why', 'zed']
sL = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Ññ', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
sP = ['æ (a)', 'b, β (lenition)', 'k, s', 'd, ð (th vibration, lenition)', 'ɛ (e)', 'f', 'g, ɣ (gh, lenition)', '(silent)', 'i', 'x (kh)', 'k', 'l', 'm', 'n', 'ɲ (ñ, ny)', 'o', 'p', 'k', 'ɾ (r), r (rr)', 's', 't', 'u', 'v', 'u, w', 'ks (x)', 'i (short), ʂ (sh)', 'θ (th no vibration), s (depends on accent)']
sN = ['a', 'be, be larga', 'ce', 'de', 'e', 'efe', 'ge', 'hache', 'i', 'jota', 'ka', 'ele', 'eme', 'ene', 'eñe', 'o', 'pe', 'qü or cu', 'erre', 'ese', 'te', 'u', 've, uve, ve corta', 'doble v' , 'equis', 'i griega', 'zeta, seta (depends on accent)']
rL = ['Аа', 'Бб', 'Вв', 'Гг', 'Дд', 'Ее', 'Ёё', 'Жж', 'Зз', 'Ии', 'Йй', 'Кк', 'Лл', 'Мм', 'Нн', 'Oo', 'Пп', 'Рр', 'Сс', 'Тт', 'Уу', 'Фф', 'Хх', 'Цц', 'Чч', 'Шш', 'Щщ', 'Ъъ', 'Ыы', 'Ьь', 'Ээ', 'Юю', 'Яя']
rP = ['æ (a)', 'b', 'v', 'g', 'd', 'jɛ (ye), ɛ (e)', 'jo (yo)', 'ʐ (zh)', 'z', 'i', 'i (short)', 'k', 'ɫ (l)', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'x (kh, h)', 'ts', 'tɕ (ch)', 'ʂ (sh)', 'ɕ (sch)', '"', 'ɨ (y)', "'", 'e', 'ju (yu)', 'ja (ya)']
rN = ['а', 'бэ', 'вэ', 'гэ', 'дэ', 'е', 'ё', 'жэ', 'зэ', 'и', 'и краткое', 'ка', 'эль, эл', 'эм', 'эн', 'о', 'пэ', 'эр', 'эс', 'тэ', 'у', 'эф', 'ха', 'цэ', 'че', 'ша', 'ща', 'твёрдый знак', 'ы', 'мягкий знак', 'э', 'ю', 'я']
gL = ['Αα', 'Ββ', 'Γγ', 'Δδ', 'Εε', 'Ζζ', 'Ηη', 'Θθ', 'Ιι', 'Κκ', 'Λλ', 'Μμ', 'Νν', 'Ξξ', 'Οο', 'Ππ', 'Ρρ', 'Σσς', 'Ττ', 'Υυ', 'Φφ', 'Χχ', 'Ψψ', 'Ωω']
gP = ['ɐ (a)', 'v', 'ɣ (gh)', 'ð (th vibration)', 'e', 'z', 'i (short)', 'θ (th no vibration)', 'i', 'k', 'l', 'm', 'n', 'ks (x)', 'o', 'p', 'r', 's, z (before β, γ, or μ)', 't', 'i (short)', 'f', 'ç (h)', 'ps', 'o̞ (o)']
gN = ['άλφα', 'βήτα', 'γάμμα', 'δέλτα', 'έψιλον', 'ζήτα', 'ήτα', 'θήτα', 'ιώτα', 'κάππα	', 'λά(μ)βδα', 'μυ', 'νυ', 'ξι', 'όμικρον', 'πι', 'ρώ', 'σίγμα', 'ταυ', 'ύψιλον', 'φι', 'χι', 'ψι', 'ωμέγα']
jHL = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
jKL = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
jHP = ['a', 'i', 'ɯ (u)', 'e', 'o', 'ka', 'ki', 'kɯ (ku)', 'ke', 'ko', 'sa', 'ɕi (shi)', 'sɯ', 'se', 'so', 'ta', 'tɕi (chi)', 'tsɯ (tsu)', 'te', 'to', 'na', 'ni', 'nɯ (nu)', 'ne', 'no', 'ha (wa as particle)', 'çi (hi)', 'ɸɯ (fu)', 'he (e as particle)', 'ho', 'ma', 'mi', 'mɯ (mu)', 'me', 'mo', 'ja (ya)', 'jɯ (yu)', 'jo (yo)', 'ɾa (ra)', 'ɾi (ri)', 'ɾɯ (ru)', 'ɾe (re)', 'ɾo (ro)', 'wa', '(w)o', 'n']
jKP = ['a', 'i', 'ɯ (u)', 'e', 'o', 'ka', 'ki', 'kɯ (ku)', 'ke', 'ko', 'sa', 'ɕi (shi)', 'sɯ', 'se', 'so', 'ta', 'tɕi (chi)', 'tsɯ (tsu)', 'te', 'to', 'na', 'ni', 'nɯ (nu)', 'ne', 'no', 'ha', 'çi (hi)', 'ɸɯ (fu)', 'he', 'ho', 'ma', 'mi', 'mɯ (mu)', 'me', 'mo', 'ja (ya)', 'jɯ (yu)', 'jo (yo)', 'ɾa (ra)', 'ɾi (ri)', 'ɾɯ (ru)', 'ɾe (re)', 'ɾo (ro)', 'wa', '(w)o', 'n']
jHDL = ['', '', '', '', '', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', '', '', '', '', '', 'ば', 'び', 'ぶ', 'べ', 'ぼ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jKDL = ['', '', '', '', '', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ヂ', 'ヅ', 'デ', 'ド', '', '', '', '', '', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jDP = ['', '', '', '', '', 'ga', 'gi', 'gɯ (gu)', 'ge', 'go', 'za', 'ʑi (ji)', 'zɯ (zu)', 'ze', 'zo', 'da', '(d)ʑi (dji)', '(d)zɯ (dzu)', 'de', 'do', '', '', '', '', '', 'ba', 'bi', 'bɯ (bu)', 'be', 'bo', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jHHL = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jKHL = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'パ', 'ピ', 'プ', 'ペ', 'ポ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jHP2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'pa', 'pi', 'pɯ (pu)', 'pe', 'po', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jHYL = ['', '', '', '', '', '', 'きゃ', 'きゅ', 'きょ', '', '', 'しゃ', 'しゅ', 'しょ', '', '', 'ちゃ', 'ちゅ', 'ちょ', '', '', 'にゃ', 'にゅ', 'にょ', '', '', 'ひゃ', 'ひゅ', 'ひょ', '', '', 'みゃ', 'みゅ', 'みょ', '', '', '', '', '', 'りゃ', 'りゅ', 'りょ', '', '', '', '']
jKYL = ['ァ', 'ィ', 'ゥ', 'ェ', 'ォ', '', 'キャ', 'キュ', 'キョ', '', '', 'シャ', 'シュ', 'ショ', '', '', 'チャ', 'チュ', 'チョ', '', '', 'ニャ', 'ニュ', 'ニョ', '', '', 'ヒャ', 'ヒュ', 'ヒョ', '', '', 'ミャ', 'ミュ', 'ミョ', '', '', '', '', '', 'リャ', 'リュ', 'リョ', '', '', '', '']
jYP = ['', '', '', '', '', '', 'kja (kya)', 'kjɯ (kyu)', 'kjo (kyo)', '', '', 'ɕa (sha)', 'ɕɯ (shu)', 'ɕo (sho)', '', '', 'tɕa (cha)', 'tɕɯ (chu)', 'tɕo (cho)', '', '', 'ɲa (nya)', 'ɲɯ (nyu)', 'ɲo (nyo)', '', '', 'ça (hya)', 'çɯ (hyu)', 'ço (hyo)', '', '', 'mja (mya)', 'mjɯ (myu)', 'mjo (myo)', '', '', '', '', '', 'rja (rya)', 'rjɯ (ryu)', 'rjo (ryo)', '', '', '', '']
jHDYL = ['', '', '', '', '', '', 'ぎゃ', 'ぎゅ', 'ぎょ', '', '', 'じゃ', 'じゅ', 'じょ', '', '', 'ぢゃ', 'ぢゅ', 'ぢょ', '', '', '', '', '', '', '', 'びゃ', 'びゅ', 'びょ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jKDYL = ['', '', '', '', '', '', 'ギャ', 'ギュ', 'ギョ', '', '', 'ジャ', 'ジュ', 'ジョ', '', '', 'ヂャ', 'ヂュ', 'ヂョ', '', '', '', '', '', '', '', 'ビャ', 'ビュ', 'ニョ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jDYP = ['', '', '', '', '', '', 'gja (gya)', 'gjɯ (gyu)', 'gjo (gyo)', '', '', 'ʑa (ja)', 'ʑɯ (ju)', 'ʑo (jo)', '', '', '(d)ʑa (dza)', '(d)ʑɯ (dzu)', '(d)ʑo ((d)zo)', '', '', '', '', '', '', '', 'bja (bya)', 'bjɯ (byu)', 'bjo (byo)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jHHYL = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'ぴゃ', 'ぴゅ', 'ぴょ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jKHYL = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'ピャ', 'ピュ', 'ピョ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
jHYP = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'pja (pya)', 'pjɯ (pyu)', 'pjo (pyo)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
hL = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'ך/כ', 'ל', 'ם/מ', 'ן/נ', 'ס', 'ע', 'ף/פ', 'ץ/צ', 'ק', 'ר', 'ש', 'ת']
hDL = ['', 'בּ', 'גּ', 'דּ', '', '', '', '', '', '', 'ךּ/כּ', '', '', '', '', '', 'ףּ/פּ', '', '', '', '', 'תּ']
hSHL = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'שׁ', '']
hSL = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'שׂ', '']
hP = ['ʔ (glottal stop)', 'v', 'ɣ (gh)', 'ð (th vibration)', 'h', 'v', 'z', 'χ (ch, kh, h)', 't', 'j (y)', 'χ (ch, kh, h)', 'l', 'm', 'n', 's', 'ɑ̯/ʕ (weird a | For more info, search: Voiced pharyngeal fricative)', 'f', 'ts', 'k', 'ʁ (french r)', 'ʃ (sh), s (For more info, check the "Shin" and "Sin" bellow)', 'θ (th no vibration)']
hDP = ['', 'b', 'g', 'd', '', '', '', '', '', '', 'k', '', '', '', '', '', 'p', '', '', '', '', 't']
hSHP = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'ʃ (sh)', '']
hSP = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 's', '']
hN = ['אָלֶף', 'בֵית', 'גִימֵל', 'דָלֶת', 'הֵא', 'וָו', 'זַיִן', 'חֵית', 'טֵית', 'יוֹד', 'כַף סוֹפִית/כַף', 'לָמֶד', 'מֵם סוֹפִית/מֵם', 'נוּן סוֹפִית/נוּן', 'סָמֶךְ', 'עַיִן', 'פֵא סוֹפִית, פֵה סוֹפִית/פֵא, פֵה', 'צָדִי סוֹפִית/צָדִי', 'קוֹף', 'רֵישׁ', 'שִׂין ,שִׁין (For more info, check the "Shin" and "Sin" bellow)', 'תָו']
hDN = ['', 'בֵּית', 'גִּימֵל', 'דָּלֶת', '', '', '', '', '', '', 'כַּף סוֹפִית/כַּף', '', '', '', '', '', 'פֵּא סוֹפִית, פֵּה סוֹפִית/פֵּא, פֵּה', '', '', '', '', 'תָּו']
hSHN = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'שִׁין', '']
hSN = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'שִׂין', '']
tkL = ['a', 'e', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 's', 't', 'u', 'w']
tkP = ['a', 'e', 'i', 'j (y)', 'k', 'l', 'm', 'n', 'o', 'p', 's', 't', 'u', 'w']
tkW = ['a', 'akesi', 'ala', 'alasa', 'ale', 'anpa', 'ante', 'anu', 'awen', 'e', 'en', 'esun', 'ijo', 'ike', 'ilo', 'insa', 'jaki', 'jan', 'jelo', 'jo', 'kala', 'kalama', 'kama', 'kasi', 'ken', 'kepeken', 'kili', 'kiwen', 'ko', 'kon', 'kule', 'kulupu', 'kute', 'la', 'lape', 'laso', 'lawa', 'len', 'lete', 'li', 'lili', 'linja', 'lipu', 'loje', 'lon', 'luka', 'lukin', 'lupa', 'ma', 'mama', 'mani', 'meli', 'mi', 'mije', 'moku', 'moli', 'monsi', 'mu', 'mun', 'musi', 'mute', 'nanpa', 'nasa', 'nasin', 'nena', 'ni', 'nimi', 'noka', 'o', 'olin', 'ona', 'open', 'pakala', 'pali', 'palisa', 'pan', 'pana', 'pi', 'pilin', 'pimeja', 'pini', 'pipi', 'poka', 'poki', 'pona', 'pu', 'sama', 'seli', 'selo', 'seme', 'sewi', 'sijelo', 'sike', 'sin', 'sina', 'sinpin', 'sitelen', 'sona', 'soweli', 'suli', 'suno', 'supa', 'suwi', 'tan', 'taso', 'tawa', 'telo', 'tenpo', 'toki', 'tomo', 'tu', 'unpa', 'uta', 'utala', 'walo', 'wan', 'waso', 'wawa', 'weka', 'wile']
tkD = []
kL = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ']
kP = ['g, k', 'n', 'd, t', 'ɭ (l), ɾ (r)', 'm', 'b, p', 's, t', '(silent), ŋ (ng)', 'dz (j)', 'tɕ (ch)', 'k', 't', 'p', 'h', 'a', 'ja (ya)', 'ʌ (eo)', 'jʌ (yeo)', 'o', 'jo (yo)', 'u', 'ju (yu)', 'ɯ (eu)', 'i']
aL = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ڧ', 'ک/ك', 'ل', 'م', 'ن', 'ه', 'و', 'ے/ي']
aP = ['a', 'b', 't', 'θ (th no vibration)', 'dʒ (j)', 'ħ (h)', 'x (kh)', 'd', 'ð (th vibration)', 'r', 'z', 's', 'ʃ (sh)', 'sˤ (s throat constricted)', 'dˤ (d throat constricted)', 'tˤ (t throat constricted)', 'ðˤ (th vibration throat constricted)', 'ɑ̯/ʕ (weird a | For more info, search: Voiced pharyngeal fricative)', 'ɣ (g)', 'f', 'q', 'k', 'l', 'm', 'n', 'h', 'w, ū, ∅', 'y, ī']
aN = ['أَلِف', 'بَاء/بَه', 'تَاء/تَه', 'ثَاء/ثَه', 'جِيم', 'حَاء/حَه', 'خَاء/خَه', 'دَال/دَاء/دَه', 'ذَال/ذَاء/ذَه', 'رَاء/رَه', 'زَاي/زَين/زَاء/زَه', 'سِين', 'شِين', 'صَاد', 'ضَاد/ضَاء/ضَه', 'طَاء/طَه', 'ظَاء/ظَه', 'عَيْن', 'غَيْن', 'فَاء/فَه', 'قَاف', 'كَاف/كَاء/كَه', 'لاَم', 'مِيم', 'نُون', 'هَاء/هَه', 'وَاو', 'يَاء/يَه']
amL = ['Աա', 'Բբ', 'Գգ', 'Դդ', 'Եե', 'Զզ', 'Էէ', 'Ըը', 'Թթ', 'Ժժ', 'Իի', 'Լլ', 'Խխ', 'Ծծ', 'Կկ', 'Հհ', 'Ձձ', 'Ղղ', 'Ճճ', 'Մմ', 'Յյ', 'Նն', 'Շշ', 'Ոո', 'Չչ', 'Պպ', 'Ջջ', 'Ռռ', 'Սս', 'Վվ', 'Տտ', 'Րր', 'Ցց', 'Ււ', 'Փփ', 'Քք', 'Օօ', 'Ֆֆ']
amP = ['ɑ (a)', 'b', 'g', 'd', 'ɛ (e)', 'z', 'e', 'ə (eo)', 'tʰ (t aspirated)', 'ʒ (zh)', 'i', 'l', 'χ (strong x (kh))', 'ts', 'k', 'h', 'dz', 'ɫ (l)', 'tʃ (ch)', 'm', 'j (y)', 'ɔ (o)', 'tʃʰ (ch aspirated)', 'p', 'dʒ (j)', 'r', 's', 'w', 't', 'ɹ (english r)', 'tsʰ (ts aspirated)', 'w', 'pʰ (p aspirated)', 'kʰ (k aspirated)', 'o', 'f', '', '']
amN = ['այբ', 'բեն', 'գիմ', 'դա', 'եչ', 'զա', 'է', 'ըթ', 'թո', 'ժե', 'ինի', 'լյուն', 'խե', 'ծա', 'կեն', 'հո', 'ձա', 'ղադ', 'ճե', 'մեն', 'հի', 'նու', 'շա', 'ո', 'չա', 'պե', 'ջե', 'ռա', 'սե', 'վեվ', 'տյուն', 'րե', 'ցո', 'հյուն', 'փյուր', 'քե', 'օ', 'ֆե']
tL = ['Aa', 'Bb', 'Cc', 'Çç', 'Dd', 'Ee', 'Ff', 'Gg', 'Ğğ', 'Hh', 'Iı', 'İi', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Öö', 'Pp', 'Rr', 'Ss', 'Şş', 'Tt', 'Uu', 'Üü', 'Vv', 'Yy', 'Zz']
tP = ['a', 'b', 'dʒ (j)', 'tʃ (ch)', 'd', 'e', 'f', 'ɡ, ɟ (If adjacent to the e, i, œ or y sound)', 'ɰ (For more info, search: Voiced velar approximant)', 'h', 'ɯ (eu)', 'i', 'ʒ (sh)', 'k, c (If adjacent to the e, i, œ or y sound)', 'ɫ (l), l (If adjacent to the a, ɯ, o or u sound)', 'm', 'n', 'o', 'œ (For more info, search: Open-mid front rounded vowel)', 'p', 'ɾ (r)', 's', 'ʃ (sh)', 't', 'u', 'y', 'v', 'j (y)', 'z']
tN = ['a', 'be', 'ce', 'çe', 'de', 'e', 'fe', 'ge', 'yumuşak ge', 'he, ha, haş', 'ı', '	i', 'je', 'ke, ka', 'le', 'me', 'ne', 'o', 'ö', 'pe', 're', 'se', 'şe', 'te', 'u', 'ü', 've', 'ye', 'ze']
iL = ['ᐁ', 'ᑉ', 'ᑦ', 'ᒃ', 'ᕻ', 'ᒡ', 'ᒻ', 'ᓐ', 'ᔅ', 'ᓪ', 'ᔾ', 'ᑦᔾ', 'ᖮ', 'ᕝ', 'ᕐ', 'ᖅ', 'ᖅᒃ', 'ᖕ', 'ᖖ', 'ᖦ', 'ᖯ', 'ᕼ', 'ᑊ']
iIL = ['ᐃ', 'ᐱ', 'ᑎ', 'ᑭ', 'ᕵ', 'ᒋ', 'ᒥ', 'ᓂ', 'ᓯ', 'ᓕ', 'ᔨ', 'ᑦᔨ', 'ᖨ', 'ᕕ', 'ᕆ', 'ᕿ', 'ᖅᑭ', 'ᖏ', 'ᙱ', 'ᖠ', '', '', '']
iUL = ['ᐅ', 'ᐳ', 'ᑐ', 'ᑯ', 'ᕷ', 'ᒍ', 'ᒧ', 'ᓄ', 'ᓱ', 'ᓗ', 'ᔪ', 'ᑦᔪ', 'ᖪ', 'ᕗ', 'ᕈ', 'ᖁ', 'ᖅᑯ', 'ᖑ', 'ᙳ', 'ᖢ', '', '', '']
iAL = ['ᐊ', 'ᐸ', 'ᑕ', 'ᑲ', 'ᕹ', 'ᒐ', 'ᒪ', 'ᓇ', 'ᓴ', 'ᓚ', 'ᔭ', 'ᑦᔭ', 'ᖬ', 'ᕙ', 'ᕋ', 'ᖃ', 'ᖅᑲ', 'ᖓ', 'ᙵ', 'ᖤ', '', '', '']
iLIL = ['ᐄ', 'ᐲ', 'ᑏ', 'ᑮ', 'ᕶ', 'ᒌ', 'ᒦ', 'ᓃ', 'ᓰ', 'ᓖ', 'ᔩ', 'ᑦᔩ', 'ᖩ', 'ᕖ', 'ᕇ', 'ᖀ', 'ᖅᑮ', 'ᖐ', 'ᙲ', 'ᖡ', '', '', '']
iLUL = ['ᐆ', 'ᐴ', 'ᑑ', 'ᑰ', 'ᕸ', 'ᒎ', 'ᒨ', 'ᓅ', 'ᓲ', 'ᓘ', 'ᔫ', 'ᑦᔫ', 'ᖫ', 'ᕘ', 'ᕉ', 'ᖂ', 'ᖅᑰ', 'ᖒ', 'ᙴ', 'ᖣ', '', '', '']
iLAL = ['ᐋ', 'ᐹ', 'ᑖ', 'ᑳ', 'ᕺ', 'ᒑ', 'ᒫ', 'ᓈ', 'ᓵ', 'ᓛ', 'ᔮ', 'ᑦᔮ', 'ᖭ', 'ᕚ', 'ᕌ', 'ᖄ', 'ᖅᑳ', 'ᖔ', 'ᙶ', 'ᖥ', '', '', '']
iP = ['ai', 'p', 't', 'k', 'h', 'g', 'm', 'n', 's', 'l', 'j (y)', 'j: (yy)', 'ɟ (dy)', 'v', 'ʁ (french r)', 'q', 'q: (qq)', 'ŋ (ng)', 'ŋ: (nng)', 'ɬ (For more info, search: Voiceless dental and alveolar lateral fricatives)', 'b', 'h', 'ʔ (glottal stop)']
iIP = ['i', 'pi', 'ti', 'ki', 'hi', 'gi', 'mi', 'ni', 'si', 'li', 'ji (yi)', 'j:i (yyi)', 'ɟi (dyi)', 'vi', 'ʁi (ri)', 'qi', 'q:i (qqi)', 'ŋi (ngi)', 'ŋ:i (nngi)', 'ɬi (?i)', '', '', '']
iUP = ['u', 'pu', 'tu', 'ku', 'hu', 'gu', 'mu', 'nu', 'su', 'lu', 'ju (yu)', 'j:u (yyu)', 'ɟu (dyu)', 'vu', 'ʁu (ru)', 'qu', 'q:u (qqu)', 'ŋu (ngu)', 'ŋ:u (nngu)', 'ɬu (?u)', '', '', '']
iAP = ['a', 'pa', 'ta', 'ka', 'ha', 'ga', 'ma', 'na', 'sa', 'la', 'ja (ya)', 'j:a (yya)', 'ɟa (dya)', 'va', 'ʁa (ra)', 'qa', 'q:a (qqa)', 'ŋa (nga)', 'ŋ:a (nnga)', 'ɬa (?a)', '', '', '']
fL = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚨ', 'ᚱ', 'ᚲ', 'ᚷ', 'ᚹ', 'ᚺ/ᚻ', 'ᚾ', 'ᛁ', 'ᛃ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛊ/ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛜ', 'ᛞ', 'ᛟ']
fP = ['f', 'u', 'θ (th no vibration)', 'a', 'r (spanish r)', 'k', 'g', 'w', 'h', 'n', 'i', 'j (y)', 'æ (a)', 'p', 'z', 's', 't', 'b', 'e', 'm', 'l', 'ŋ (ng)', 'd', 'o']
esL = ['Aa', 'Bb', 'Cc', 'Ĉĉ', 'Dd', 'Ee', 'Ff', 'Gg', 'Ĝĝ', 'Hh', 'Ĥĥ', 'Ii', 'Jj', 'Ĵĵ', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Rr', 'Ss', 'Ŝŝ', 'Tt', 'Uu', 'Ŭŭ', 'Vv', 'Zz']
esP = ['a', 'b', 'ts', 'tʃ (ch)', 'd', 'e', 'f', 'g', 'dʒ (j)', 'h', 'x (kh)', 'i', 'j (y)', 'ʒ (zh)', 'k', 'l', 'm', 'n', 'o', 'p', 'r (rr)', 's', 'ʃ (sh)', 't', 'u', 'w', 'v', 'z']
esN = ['a', 'bo', 'co', 'ĉo', 'do', 'e', 'fo', 'go', 'ĝo', 'ho', 'ĥo', 'i', 'jo', 'ĵo', 'ko', 'lo', 'mo', 'no', 'o', 'po', 'ro', 'so', 'ŝo', 'to', 'u', 'ŭo', 'vo', 'zo']
globLang = 'no-language'
ver = 'v0.6.3'

def eM(i, e):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + eN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + eP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        eE()
def eE():
    for i, e in enumerate(eL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(eL):
            if int(check) == int(i) + 1:
                os.system('cls')
                eM(i, e)
def sM(i, e):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + sN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + sP[i])
    if e == 'Aa':
        print(msg(20, globLang) + '\n1 - Áá\n2 - Ää')
    elif e == 'Ee':
        print(msg(20, globLang) + '\n1- Éé\n2 - Ëë')
    elif e == 'Ii':
        print(msg(20, globLang) + '\n1 - Íí\n2 - Ïï')
    elif e == 'Oo':
        print(msg(20, globLang) + '\n1- Óó\n2 - Öö')
    elif e == 'Uu':
        print(msg(20, globLang) + '\n1 - Úú\n2 - Üü')
    elif e == 'Cc' or e == 'Hh':
        print(msg(20, globLang) + '\n1 - CHch')
    elif e == 'Ll':
        print(msg(20, globLang) + '\n1 - LLll')
    if e == 'Aa' or e == 'Ee' or e == 'Ii' or e == 'Oo' or e == 'Uu':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            sE()
        elif int(check) == 1:
            os.system('cls')
            print(msg(19, globLang))
            print(msg(7, globLang))
            check = input('>> ')
            if iToF('back', check):
                os.system('cls')
                sM(i, e)
        elif int(check) == 2:
            os.system('cls')
            print(msg(18, globLang))
            print(msg(7, globLang))
            check = input('>> ')
            if iToF('back', check):
                os.system('cls')
                sM(i, e)
    elif e == 'Ll':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            sE()
        elif int(check) == 1:
            os.system('cls')
            print(msg(17, globLang))
            print(msg(7, globLang))
            check = input('>> ')
            if iToF('back', check):
                os.system('cls')
                sM(i, e)
    else:
        print(msg(7, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            sE()
def sE():
    for i, e in enumerate(sL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(sL):
            if int(check) == int(i) + 1:
                os.system('cls')
                sM(i, e)
def rM(i, e):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + rN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + rP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        rE()
def rE():
    for i, e in enumerate(rL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(rL):
            if int(check) == int(i) + 1:
                os.system('cls')
                rM(i, e)
def gM(i, e):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + gN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + gP[i])
    if e == 'Αα':
        print(msg(20, globLang) + '\n1 - Άά')
    elif e == 'Εε':
        print(msg(20, globLang) + '\n1- Έέ')
    elif e == 'Ιι':
        print(msg(20, globLang) + '\n1 - Ίί')
    elif e == 'Οο':
        print(msg(20, globLang) + '\n1- Όό')
    elif e == 'Ωω':
        print(msg(20, globLang) + '\n1 - Ώώ')
    elif e == 'Ηη':
        print(msg(20, globLang) + '\n1 - Ήή')
    elif e == 'Υυ':
        print(msg(20, globLang) + '\n1 - Ύύ')
    if e == 'Αα' or e == 'Εε' or e == 'Ιι' or e == 'Οο' or e == 'Ωω' or e == 'Ηη' or e == 'Υυ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            gE()
        elif int(check) == 1:
            os.system('cls')
            print(msg(19, globLang))
            print(msg(7, globLang))
            check = input('>> ')
            if iToF('back', check):
                os.system('cls')
                gM(i, e)
    else:
        print(msg(7, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            gE()
def gE():
    for i, e in enumerate(gL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(gL):
            if int(check) == int(i) + 1:
                os.system('cls')
                gM(i, e)
def jHM(i, e , c):
    print(msg(9, globLang) + e)
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + jHP[i])
    if e == 'か':
        print('Dakuten:\n1 - が')
    elif e == 'き':
        print('Dakuten:\n1 - ぎ\nYouon:\n2 - きゃ\n3 - きゅ\n4 - きょ\nYouon Dakuten:\n5 - ぎゃ\n6 - ぎゅ\n7 - ぎょ')
    elif e == 'く':
        print('Dakuten:\n1 - ぐ')
    elif e == 'け':
        print('Dakuten:\n1 - げ')
    elif e == 'こ':
        print('Dakuten:\n1 - ご')
    elif e == 'さ':
        print('Dakuten:\n1 - ざ')
    elif e == 'し':
        print('Dakuten:\n1 - じ\nYouon:\n2 - しゃ\n3 - しゅ\n4 - しょ\nYouon Dakuten:\n5 - じゃ\n6 - じゅ\n7 - じょ')
    elif e == 'す':
        print('Dakuten:\n1 - ず')
    elif e == 'せ':
        print('Dakuten:\n1 - ぜ')
    elif e == 'そ':
        print('Dakuten:\n1 - ぞ')
    elif e == 'た':
        print('Dakuten:\n1 - だ')
    elif e == 'ち':
        print('Dakuten:\n1 - ぢ')
    elif e == 'つ':
        print('Dakuten:\n1 - づ\nYouon:\n2 - っ')
    elif e == 'て':
        print('Dakuten:\n1 - で')
    elif e == 'と':
        print('Dakuten:\n1 - ど')
    elif e == 'に':
        print('Youon:\n1 - にゃ\n2 - にゅ\n3 - にょ')
    elif e == 'は':
        print('Dakuten:\n1 - ば\nHandakuten:\n2 - ぱ')
    elif e == 'ひ':
        print('Dakuten:\n1 - び\nHandakuten:\n2 - ぴ\nYouon:\n3 - ひゃ\n4 - ひゅ\n5 - ひょ\nYouon Dakuten:\n6 - びゃ\n7 - びゅ\n8 - びょ\nYouon Handakuten:\n9 - ぴゃ\n10 - ぴゅ\n11 - ぴょ')
    elif e == 'ふ':
        print('Dakuten:\n1 - ぶ\nHandakuten:\n2 - ぷ')
    elif e == 'へ':
        print('Dakuten:\n1 - べ\nHandakuten:\n2 - ぺ')
    elif e == 'ほ':
        print('Dakuten:\n1 - ぼ\nHandakuten:\n2 - ぽ')
    elif e == 'み':
        print('Youon:\n1 - みゃ\n2 - みゅ\n3 - みょ')
    elif e == 'り':
        print('Youon:\n1 - りゃ\n2 - りゅ\n3 - りょ')
    if e == 'か' or e == 'く' or e == 'け' or e == 'こ' or e == 'さ' or e == 'す' or e == 'せ' or e == 'そ' or e == 'た' or e == 'ち' or e == 'つ' or e == 'て' or e == 'と':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jHE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jHDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM2(i2, e2, i, e, c, 'D')
    elif e == 'つ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            print(msg(15, globLang))
            print(msg(7, globLang))
            check = input('>> ')
            if iToF('back', check):
                os.system('cls')
                jKM(i, e, c)
    elif e == 'は' or e == 'ふ' or e == 'へ' or e == 'ほ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jHE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jHDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            for i2, e2 in enumerate(jHHL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM2(i2, e2, i, e, c, 'D')
    elif e == 'ひ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jHE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jHDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            for i2, e2 in enumerate(jHHL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM2(i2, e2, i, e, c, 'D')
        elif int(check) == 3:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(i2, e2, i, e, c, 'N')
        elif int(check) == 4:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 1, jHYL[i2 + 1], i, e, c, 'N')
        elif int(check) == 5:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 2, jHYL[i2 + 2], i, e, c, 'N')
        elif int(check) == 6:
            for i2, e2 in enumerate(jHDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(i2, e2, i, e, c, 'D')
        elif int(check) == 7:
            for i2, e2 in enumerate(jHDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 1, jHYL[i2 + 1], i, e, c, 'D')
        elif int(check) == 8:
            for i2, e2 in enumerate(jHDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 2, jHYL[i2 + 2], i, e, c, 'D')
        elif int(check) == 9:
            for i2, e2 in enumerate(jHHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(i2, e2, i, e, c, 'H')
        elif int(check) == 10:
            for i2, e2 in enumerate(jHHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 1, jHYL[i2 + 1], i, e, c, 'H')
        elif int(check) == 11:
            for i2, e2 in enumerate(jHHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 2, jHYL[i2 + 2], i, e, c, 'H')
    elif e == 'き' or e == 'し':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jHE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jHDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(i2, e2, i, e, c, 'N')
        elif int(check) == 3:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 1, jHYL[i2 + 1], i, e, c, 'N')
        elif int(check) == 4:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 2, jHYL[i2 + 2], i, e, c, 'N')
        elif int(check) == 5:
            for i2, e2 in enumerate(jHDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(i2, e2, i, e, c, 'D')
        elif int(check) == 6:
            for i2, e2 in enumerate(jHDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 1, jHYL[i2 + 1], i, e, c, 'D')
        elif int(check) == 7:
            for i2, e2 in enumerate(jHDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 2, jHYL[i2 + 2], i, e, c, 'D')
    elif e == 'に' or e == 'み' or e == 'り':
        if int(check) == 1:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(i2, e2, i, e, c, 'N')
        elif int(check) == 2:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 1, jHYL[i2 + 1], i, e, c, 'N')
        elif int(check) == 3:
            for i2, e2 in enumerate(jHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM3(int(i2) + 2, jHYL[i2 + 2], i, e, c, 'N')
    else:
        print(msg(7, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jHE()
def jHM2(i, e, i2, e2, c, w):
    print(msg(9, globLang) + e)
    if w == 'D':
        print(msg(12, globLang) + jDP[i])
    elif w == 'H':
        print(msg(12, globLang) + jHP2[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        jHM(i2, e2, c)
def jHM3(i, e, i2, e2, c, w):
    print(msg(9, globLang) + e)
    if w == 'N':
        print(msg(12, globLang) + jYP[i])
    elif w == 'D':
        print(msg(12, globLang) + jDYP[i])
    elif w == 'H':
        print(msg(12, globLang) + jHYP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        jHM(i2, e2, c)
def jHE():
    for i, e in enumerate(jHL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        j()
    else:
        for i, e in enumerate(jHL):
            if int(check) == int(i) + 1:
                os.system('cls')
                jHM(i, e, check)
def jKM(i, e , c):
    print(msg(9, globLang) + e)
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + jKP[i])
    if e == 'ア':
        print('Youon:\n1 - ァ')
    elif e == 'イ':
        print('Youon:\n1 - ィ')
    elif e == 'ウ':
        print('Youon:\n1 - ゥ')
    elif e == 'エ':
        print('Youon:\n1 - ェ')
    elif e == 'オ':
        print('Youon:\n1 - ォ')
    elif e == 'カ':
        print('Dakuten:\n1 - ガ')
    elif e == 'キ':
        print('Dakuten:\n1 - ギ\nYouon:\n2 - キャ\n3 - キュ\n4 - キョ\nYouon Dakuten:\n5 - ギャ\n6 - ギュ\n7 - ギョ')
    elif e == 'ク':
        print('Dakuten:\n1 - グ')
    elif e == 'ケ':
        print('Dakuten:\n1 - ゲ')
    elif e == 'コ':
        print('Dakuten:\n1 - ゴ')
    elif e == 'サ':
        print('Dakuten:\n1 - ザ')
    elif e == 'シ':
        print('Dakuten:\n1 - ジ\nYouon:\n2 - シャ\n3 - シュ\n4 - ショ\nYouon Dakuten:\n5 - ジャ\n6 - ジュ\n7 - ジョ')
    elif e == 'ス':
        print('Dakuten:\n1 - ズ')
    elif e == 'セ':
        print('Dakuten:\n1 - ゼ')
    elif e == 'ソ':
        print('Dakuten:\n1 - ゾ')
    elif e == 'タ':
        print('Dakuten:\n1 - ダ')
    elif e == 'チ':
        print('Dakuten:\n1 - ヂ')
    elif e == 'ツ':
        print('Dakuten:\n1 - ヅ\nYouon:\n2 - ッ')
    elif e == 'テ':
        print('Dakuten:\n1 - デ')
    elif e == 'ト':
        print('Dakuten:\n1 - ド')
    elif e == 'ニ':
        print('Youon:\n1 - ニャ\n2 - ニュ\n3 - ニョ')
    elif e == 'ハ':
        print('Dakuten:\n1 - バ\nHandakuten:\n2 - パ')
    elif e == 'ヒ':
        print('Dakuten:\n1 - ビ\nHandakuten:\n2 - ピ\nYouon:\n3 - ヒャ\n4 - ヒュ\n5 - ヒョ\nYouon Dakuten:\n6 - ビャ\n7 - ビュ\n8 - ビョ\nYouon Handakuten:\n9 - ピャ\n10 - ピュ\n11 - ピョ')
    elif e == 'フ':
        print('Dakuten:\n1 - ブ\nHandakuten:\n2 - プ')
    elif e == 'ヘ':
        print('Dakuten:\n1 - ベ\nHandakuten:\n2 - ペ')
    elif e == 'ホ':
        print('Dakuten:\n1 - ボ\nHandakuten:\n2 - ポ')
    elif e == 'ミ':
        print('Youon:\n1 - ミャ\n2 - ミュ\n3 - ミョ')
    elif e == 'リ':
        print('Youon:\n1 - リャ\n2 - リュ\n3 - リョ')
    if e == 'カ' or e == 'ク' or e == 'ケ' or e == 'コ' or e == 'サ' or e == 'ス' or e == 'セ' or e == 'ソ' or e == 'タ' or e == 'チ' or e == 'テ' or e == 'ト':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
    elif e == 'ア' or e == 'イ' or e == 'ウ' or e == 'エ' or e == 'オ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jKE()
        elif int(check) == 1:
            print(msg(16, globLang))
            print(msg(7, globLang))
            check = input('>> ')
            if iToF('back', check):
                os.system('cls')
                jKM(i, e, c)
    elif e == 'ツ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            print(msg(15, globLang))
            print(msg(7, globLang))
            check = input('>> ')
            if iToF('back', check):
                os.system('cls')
                jKM(i, e, c)
    elif e == 'ハ' or e == 'フ' or e == 'ヘ' or e == 'ホ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            for i2, e2 in enumerate(jKHL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
    elif e == 'ヒ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            for i2, e2 in enumerate(jKHL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
        elif int(check) == 3:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(i2, e2, i, e, c, 'N')
        elif int(check) == 4:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 1, jKYL[i2 + 1], i, e, c, 'N')
        elif int(check) == 5:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 2, jKYL[i2 + 2], i, e, c, 'N')
        elif int(check) == 6:
            for i2, e2 in enumerate(jKDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(i2, e2, i, e, c, 'D')
        elif int(check) == 7:
            for i2, e2 in enumerate(jKDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 1, jKYL[i2 + 1], i, e, c, 'D')
        elif int(check) == 8:
            for i2, e2 in enumerate(jKDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 2, jKYL[i2 + 2], i, e, c, 'D')
        elif int(check) == 9:
            for i2, e2 in enumerate(jKHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(i2, e2, i, e, c, 'H')
        elif int(check) == 10:
            for i2, e2 in enumerate(jKHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 1, jKYL[i2 + 1], i, e, c, 'H')
        elif int(check) == 11:
            for i2, e2 in enumerate(jKHYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 2, jKYL[i2 + 2], i, e, c, 'H')
    elif e == 'キ' or e == 'シ':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(i2, e2, i, e, c, 'N')
        elif int(check) == 3:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 1, jKYL[i2 + 1], i, e, c, 'N')
        elif int(check) == 4:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 2, jKYL[i2 + 2], i, e, c, 'N')
        elif int(check) == 5:
            for i2, e2 in enumerate(jKDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(i2, e2, i, e, c, 'D')
        elif int(check) == 6:
            for i2, e2 in enumerate(jKDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 1, jKYL[i2 + 1], i, e, c, 'D')
        elif int(check) == 7:
            for i2, e2 in enumerate(jKDYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 2, jKYL[i2 + 2], i, e, c, 'D')
    elif e == 'ニ' or e == 'ミ' or e == 'リ':
        if int(check) == 1:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(i2, e2, i, e, c, 'N')
        elif int(check) == 2:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 1, jKYL[i2 + 1], i, e, c, 'N')
        elif int(check) == 3:
            for i2, e2 in enumerate(jKYL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM3(int(i2) + 2, jKYL[i2 + 2], i, e, c, 'N')
    else:
        print(msg(7, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            jKE()
def jKM2(i, e, i2, e2, c, w):
    print(msg(9, globLang) + e)
    if w == 'D':
        print(msg(12, globLang) + jDP[i])
    elif w == 'H':
        print(msg(12, globLang) + jHP2[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        jKM(i2, e2, c)
def jKM3(i, e, i2, e2, c, w):
    print(msg(9, globLang) + e)
    if w == 'N':
        print(msg(12, globLang) + jYP[i])
    elif w == 'D':
        print(msg(12, globLang) + jDYP[i])
    elif w == 'H':
        print(msg(12, globLang) + jHYP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        jKM(i2, e2, c)
def jKE():
    for i, e in enumerate(jKL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        j()
    else:
        for i, e in enumerate(jKL):
            if int(check) == int(i) + 1:
                os.system('cls')
                jKM(i, e, check)
def j():
    print(msg(13, globLang))
    check = input('>> ')
    if check.lower() == 'hiragana' or check.lower() == 'хирагана' or check.lower() == 'sitelen ilagana':
        os.system('cls')
        jHE()
    elif check.lower() == 'katakana' or check.lower() == 'катакана' or check.lower() == 'sitelen katakana':
        os.system('cls')
        jKE()
    elif iToF('back', check):
        os.system('cls')
        c()
    else:
        os.system('cls')
        msg(1, globLang)
        j()
def hM(i, e, c):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + hN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + hP[i])
    if e == 'ב':
        print('Dagesh:\n1 - בּ')
    elif e == 'ג':
        print('Dagesh:\n1 - גּ')
    elif e == 'ד':
        print('Dagesh:\n1 - דּ')
    elif e == 'ך/כ':
        print('Dagesh:\n1 - ךּ/כּ')
    elif e == 'ף/פ':
        print('Dagesh:\n1 - ףּ/פּ')
    elif e == 'ת':
        print('Dagesh:\n1 - תּ')
    elif e == 'ש':
        print('Shin:\n1 - שׁ\nSin:\n2 - שׂ')
    if e == 'ב' or e == 'ג' or e == 'ד' or e == 'ך/כ' or e == 'ף/פ' or e == 'ת':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            hE()
        elif int(check) == 1:
            for i2, e2 in enumerate(hDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    hM2(i2, e2, i, e, c)
    elif e == 'ש':
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            hE()
        elif int(check) == 1:
            for i2, e2 in enumerate(hSHL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    hM3(i2, e2, i, e, c, 'SH')
        elif int(check) == 2:
            for i2, e2 in enumerate(hSL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    hM3(i2, e2, i, e, c, 'S')
    else:
        print(msg(7, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            hE()
def hM2(i, e, i2, e2, c):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + hDN[i])
    print(msg(12, globLang) + hDP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        hM(i2, e2, c)
def hM3(i, e, i2, e2, c, w):
    print(msg(9, globLang) + e)
    if w == 'SH':
        print(msg(10, globLang) + hSHN[i])
        print(msg(12, globLang) + hSHP[i])
    elif w == 'S':
        print(msg(10, globLang) + hSHN[i])
        print(msg(12, globLang) + hSP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        hM(i2, e2, c)
def hE():
    print(msg(99, globLang))
    for i, e in enumerate(hL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(hL):
            if int(check) == int(i) + 1:
                os.system('cls')
                hM(i, e, check)
def tkM(i, e):
    print(msg(9, globLang) + e)
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + tkP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        tkE()
def tkE():
    for i, e in enumerate(tkL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(tkL):
            if int(check) == int(i) + 1:
                os.system('cls')
                tkM(i, e)
def DtkM(i, e):
    print(msg(9, globLang) + e)
    print(msg(24, globLang) + tkD[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        Dtk()
def Dtk():
    for i, e in enumerate(tkW):
        print(str((i + 1)) + ' - ' + e)
    print(msg(23, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        start()
    else:
        for i, e in enumerate(tkW):
            if int(check) == int(i) + 1:
                os.system('cls')
                DtkM(i, e)
def kM(i, e):
    print(msg(9, globLang) + e)
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + kP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        kE()   
def kE():
    for i, e in enumerate(kL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(kL):
            if int(check) == int(i) + 1:
                os.system('cls')
                kM(i, e)
def aM(i, e):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + aN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + aP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        aE()   
def aE():
    print(msg(97, globLang))
    for i, e in enumerate(aL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(aL):
            if int(check) == int(i) + 1:
                os.system('cls')
                aM(i, e)
def amM(i, e):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + amN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + amP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        amE()   
def amE():
    for i, e in enumerate(amL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(amL):
            if int(check) == int(i) + 1:
                os.system('cls')
                amM(i, e)
def tM(i, e):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + tN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + tP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        tE()   
def tE():
    for i, e in enumerate(tL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(tL):
            if int(check) == int(i) + 1:
                os.system('cls')
                tM(i, e)
def iM(i, e, c):
    print(msg(9, globLang) + e)
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + iP[i])
    if e == 'ᐁ' or e == 'ᑉ' or e == 'ᑦ' or e == 'ᒃ' or e == 'ᕻ' or e == 'ᒡ' or e == 'ᒻ' or e == 'ᓐ' or e == 'ᔅ' or e == 'ᓪ' or e == 'ᔾ' or e == 'ᑦᔾ' or e == 'ᖮ' or e == 'ᕝ' or e == 'ᕐ' or e == 'ᖅ' or e == 'ᖅᒃ' or e == 'ᖕ' or e == 'ᖖ' or e == 'ᖦ':
        print(msg(25, globLang) + '\n1 - "i"\n2- "u"\n3- "a"')
        print(msg(8, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            iE()
        elif int(check) == 1:
            os.system('cls')
            for i2, e2 in enumerate(iIL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    iM2(i2, e2, i, e, c, 1)
        elif int(check) == 2:
            os.system('cls')
            for i2, e2 in enumerate(iUL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    iM2(i2, e2, i, e, c, 2)
        elif int(check) == 3:
            os.system('cls')
            for i2, e2 in enumerate(iAL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    iM2(i2, e2, i, e, c, 3)
    else:
        print(msg(7, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            iE()
def iM2(i, e, i2, e2, c, w):
    print(msg(9, globLang) + e)
    if w == 1:
        print(msg(12, globLang) + iIP[i])
        print(msg(26, globLang) + '\n1- ' +  iLIL[i])
    elif w == 2:
        print(msg(12, globLang) + iUP[i])
        print(msg(26, globLang) + '\n1- ' +  iLUL[i])
    elif w == 3:
        print(msg(12, globLang) + iAP[i])
        print(msg(26, globLang) + '\n1- ' +  iLAL[i])
    print(msg(8, globLang))
    check = input('>> ')
    if iToF('back', check):
            os.system('cls')
            iM(i2, e2, c)
    elif int(check) == 1:
        if w == 1:
            iM3(i2, e2, i, e, c, iLIL[i])
        elif w == 2:
            iM3(i2, e2, i, e, c, iLUL[i])
        elif w == 3:
            iM3(i2, e2, i, e, c, iLAL[i])
def iM3(i, e, i2, e2, c, n):
    os.system('cls')
    print(msg(9, globLang) + n)
    print(msg(27, globLang))
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
            os.system('cls')
            iM(i2, e2, c)
def iE():
    for i, e in enumerate(iL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(iL):
            if int(check) == int(i) + 1:
                os.system('cls')
                iM(i, e, check)
def fM(i, e):
    print(msg(9, globLang) + e)
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + fP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        fE()   
def fE():
    for i, e in enumerate(fL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(fL):
            if int(check) == int(i) + 1:
                os.system('cls')
                fM(i, e)
def esM(i, e):
    print(msg(9, globLang) + e)
    print(msg(10, globLang) + esN[i])
    print(msg(11, globLang) + str((i + 1)))
    print(msg(12, globLang) + esP[i])
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        esE()
def esE():
    for i, e in enumerate(esL):
        print(str((i + 1)) + ' - ' + e)
    print(msg(6, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        c()
    else:
        for i, e in enumerate(esL):
            if int(check) == int(i) + 1:
                os.system('cls')
                esM(i, e)
def c():
    print(msg(5, globLang))
    check = input('>> ')
    if iToF('lan.engl', check):
        os.system('cls')
        eE()
    elif iToF('lan.span', check):
        os.system('cls')
        sE()
    elif iToF('lan.rusi', check):
        os.system('cls')
        rE()
    elif iToF('lan.grek', check):
        os.system('cls')
        gE()
    elif iToF('lan.japa', check):
        os.system('cls')
        j()
    elif iToF('lan.hebr', check):
        os.system('cls')
        hE()
    elif iToF('lan.tkpn', check):
        os.system('cls')
        tkE()
    elif iToF('lan.kore', check):
        os.system('cls')
        kE()
    elif iToF('lan.arab', check):
        os.system('cls')
        aE()
    elif iToF('lan.arme', check):
        os.system('cls')
        amE()
    elif iToF('lan.turk', check):
        os.system('cls')
        tE()
    elif iToF('lan.inuk', check):
        os.system('cls')
        iE()
    elif iToF('lan.futh', check):
        os.system('cls')
        fE()
    elif iToF('lan.espe', check):
        os.system('cls')
        esE()
    elif iToF('back', check):
        os.system('cls')
        start()
    else:
        os.system('cls')
        print(msg(1, globLang))
        c()
def p():
    print(msg(14, globLang))
    check = input('>> ')
    if iToF('lan.engl', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.span', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.rusi', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.grek', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.japa', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.hebr', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.kore', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.arab', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.arme', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.turk', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.inuk', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.futh', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('lan.espe', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('back', check):
        os.system('cls')
        start()
    else:
        os.system('cls')
        print(msg(1, globLang))
        p()
def start():
    print(msg(2, globLang))
    check = input('>> ')
    if iToF('set.chek', check):
        os.system('cls')
        c()
    elif iToF('set.prac', check):
        os.system('cls')
        p()
    elif iToF('set.leso', check):
        os.system('cls')
        print(msg(4, globLang))
        start()
    elif iToF('set.dict', check):
        os.system('cls')
        Dtk()
    elif iToF('set.extr', check):
        os.system('cls')
        extra()
    elif iToF('exit', check):
        exit()
    else:
        os.system('cls')
        print(msg(1, globLang))
    start()
def extra():
    print(msg(22, globLang))
    check = input('>> ')
    if iToF('set.seti', check):
        os.system('cls')
        settings()
    elif iToF('set.cred', check):
        os.system('cls')
        credits()
    elif iToF('back', check):
        os.system('cls')
        start()
    else:
        os.system('cls')
        print(msg(1, globLang))
    settings()
def settings():
    print(msg(3, globLang))
    check = input('>> ')
    if iToF('set.lang', check):
        os.system('cls')
        lang(True)
    elif iToF('back', check):
        os.system('cls')
        extra()
    else:
        os.system('cls')
        print(msg(1, globLang))
    settings()
def lang(sm):
    global globLang, tkD
    if sm == False:
        print('\nSelect a language:\n1 - en/eng (English)\n2 - es/spa (Español)\n3 - ru/rus (Русский)\n4 - tok (toki pona)\n- Back')
        check = input('>> ')
        if check == '1' or check.lower() == 'english' or check.lower() == 'en' or check.lower() == 'eng':
            globLang = 'en'
            tkD = ['[emphasis]', 'reptile', 'no', 'hunt', 'everything, all', 'below', 'different', 'or', 'keep, save', '[object]', 'and', 'trade, commerce', 'thing', 'bad, evil, unnecessary', 'tool', 'interior', 'dirty, unclean', 'person', 'yellow', 'to have', 'fish', 'sound', 'to come', 'plant', 'can', 'to use', 'fruit, vegetable', 'stone, gem', 'stain, gum', 'air', 'colour / color', 'group', 'to hear', '[context]', 'to sleep', 'green', 'head', 'clothing', 'cold', '[predicate]', 'small', 'line', 'paper', 'red', 'on, in', 'hand, five (complex number system)', 'to see, to look', 'hole', 'land, earth', 'parent', 'money', 'woman', 'me, my, I', 'man', 'to eat', 'dead', 'behind, back', '[meow]', 'moon', 'to play', 'many, three or more (simple number system)', 'number', 'crazy, drunk', 'path', 'mountain', 'this, that', 'name, word', 'leg', '[command / mandate]', 'love', 'he, she, they, it', 'to open', 'break, destroy', 'to do, to make', 'stick', 'food, grain', 'to give', 'of', 'to feel', 'black', 'end', 'insect', 'near', 'container, box', 'good', '[interact with the book]', 'same', 'fire, hot', 'skin', 'what', 'tall', 'body', 'circle, ball', 'new', 'you', 'in front', 'image, drawing', 'to know', 'animal', 'big, important', 'sun', 'surface', 'sweet', 'because of, from', 'but', 'to, movement to', 'water', 'time', 'talk, hello, language', 'house, room', 'two', 'sex', 'mouth', 'to fight', 'white', 'one', 'bird', 'strong', 'outside', 'to want, to need']
        elif check == '2' or check.lower() == 'español' or check.lower() == 'es' or check.lower() == 'spa':
            globLang = 'es'
            tkD = ['[enfasis]', 'reptil', 'no', 'cazar', 'todo', 'abajo', 'diferente', 'o', 'guardar', '[objeto]', 'y', 'comercio', 'cosa', 'malo, innecesario', 'herramienta', 'interior', 'sucio', 'persona', 'amarillo', 'tener', 'pez', 'sonido', 'venir', 'planta', 'poder (hacer)', 'usar', 'fruta, verdura', 'piedra, gema', 'mancha, pasta', 'aire', 'color', 'grupo', 'escuchar, oir', '[contexto]', 'dormir', 'verde', 'cabeza', 'ropa', 'frio', '[predicado]', 'pequeño', 'linea', 'papel', 'rojo', 'en', 'mano, cinco (sistema complejo de numeros)', 'ver, mirar', 'agujero', 'terreno, tierra', 'padre', 'dinero', 'mujer', 'mi, yo', 'hombre', 'comer', 'muerto', 'atras', '[miau]', 'luna', 'jugar', 'mucho, tres o mas (sistema simple de numeros)', 'numero', 'loco, borracho', 'camino', 'montaña', 'esto, este, eso', 'nombre, palabra', 'pie', '[mandato]', 'amor', 'el, ella, ellos, eso', 'abrir', 'romper, destruir', 'hacer', 'palo', 'comida, miga', 'dar', 'de', 'sentir', 'negro', 'fin', 'insecto', 'cerca', 'contenedor, caja', 'bueno', '[interactuar con el libro]', 'igual', 'fuego, caliente', 'piel', 'que', 'alto', 'cuerpo', 'circulo, bola', 'nuevo', 'vos', 'adelante', 'imagen, dibujo', 'saber', 'animal', 'grande, importante', 'sol', 'superficie', 'dulce', 'a causa de, por', 'pero', 'a, movimiento a', 'agua', 'tiempo', 'hablar, hola, idioma', 'casa, cuarto', 'dos', 'sexo', 'boca', 'luchar', 'blanco', 'uno', 'pajaro', 'fuerte', 'afuera', 'necesitar']
        elif check == '3' or check.lower() == 'русский' or check.lower() == 'ru' or check.lower() == 'rus':
            globLang = 'ru'
            tkD = ['[ударение]', 'рептилия', 'нет', 'охота', 'все', 'ниже', 'разное', 'или', 'сохранить, сберечь', '[предмет]', 'и', 'торговля, коммерция', 'вещь', 'плохой, злой, ненужный', 'инструмент', 'интерьер', 'грязный, нечистый', 'человек', 'желтый', 'иметь', 'рыба', 'звук', 'приходить', 'растение', 'может', 'использовать', 'фрукт, овощ', 'камень, самоцвет', 'пятно, камедь', 'воздух', 'цвет', 'группа', 'слышать', '[контекст]', 'спать', 'зеленый', 'голова', 'одежда', 'холод', '[сказуемое]', 'маленький', 'линия', 'бумага', 'красный', 'на, в', 'рука, пять (сложная система счисления)', 'видеть, смотреть', 'дыра', 'земля', 'родитель', 'деньги', 'женщина', 'я, мой', 'мужчина', 'есть', 'мертвый', 'сзади', '[мяу]', 'луна', 'играть', 'много, три или больше (простая система счисления)', 'число', 'сумасшедший, пьяный', 'путь', 'гора', 'это, то', 'имя, слово', 'нога', '[команда / мандат]', 'любовь', 'он, она, они, оно', 'открыть', 'сломать, уничтожить', 'сделать', 'палка', 'еда, зерно', 'дать', 'из', 'чувствовать', 'черный', 'конец', 'насекомое', 'рядом', 'контейнер, коробка', 'хорошо', '[взаимодействовать с книгой]', 'то же', 'огонь, горячий', 'кожа', 'что', 'высокий', 'тело', 'круг, шар', 'новый', 'ты', 'перед', 'изображение, рисунок', 'знать', 'животное', 'большой, важный', 'солнце', 'поверхность', 'сладкий', 'из-за, от', 'но', 'к, движение к', 'вода', 'время', 'говорить, привет, язык', 'дом, комната', 'два', 'секс', 'рот', 'бороться', 'белый', 'один', 'птица', 'сильный', 'снаружи', 'хотеть, нуждаться']
        elif check == '4' or check.lower() == 'toki pona' or check.lower() == 'tok':
            tkD = tkW
            globLang = 'tok'
        else:
            os.system('cls')
            print('\nSorry, that is not an option. Did you spell it correctly?')
            lang(False)
    elif sm == True:
        print('\nSelect a language:\n1 - en/eng (English)\n2 - es/spa (Español)\n3 - ru/rus (Русский)\n4 - tok (toki pona)\n- Back')
        check = input('>> ')
        if check == '1' or check.lower() == 'english' or check.lower() == 'en' or check.lower() == 'eng':
            globLang = 'en'
            tkD = ['[emphasis]', 'reptile', 'no', 'hunt', 'everything, all', 'below', 'different', 'or', 'keep, save', '[object]', 'and', 'trade, commerce', 'thing', 'bad, evil, unnecessary', 'tool', 'interior', 'dirty, unclean', 'person', 'yellow', 'to have', 'fish', 'sound', 'to come', 'plant', 'can', 'to use', 'fruit, vegetable', 'stone, gem', 'stain, gum', 'air', 'colour / color', 'group', 'to hear', '[context]', 'to sleep', 'green', 'head', 'clothing', 'cold', '[predicate]', 'small', 'line', 'paper', 'red', 'on, in', 'hand, five (complex number system)', 'to see, to look', 'hole', 'land, earth', 'parent', 'money', 'woman', 'me, my, I', 'man', 'to eat', 'dead', 'behind, back', '[meow]', 'moon', 'to play', 'many, three or more (simple number system)', 'number', 'crazy, drunk', 'path', 'mountain', 'this, that', 'name, word', 'leg', '[command / mandate]', 'love', 'he, she, they, it', 'to open', 'break, destroy', 'to do, to make', 'stick', 'food, grain', 'to give', 'of', 'to feel', 'black', 'end', 'insect', 'near', 'container, box', 'good', '[interact with the book]', 'same', 'fire, hot', 'skin', 'what', 'tall', 'body', 'circle, ball', 'new', 'you', 'in front', 'image, drawing', 'to know', 'animal', 'big, important', 'sun', 'surface', 'sweet', 'because of, from', 'but', 'to, movement to', 'water', 'time', 'talk, hello, language', 'house, room', 'two', 'sex', 'mouth', 'to fight', 'white', 'one', 'bird', 'strong', 'outside', 'to want, to need']
        elif check == '2' or check.lower() == 'español' or check.lower() == 'es' or check.lower() == 'spa':
            globLang = 'es'
            tkD = ['[enfasis]', 'reptil', 'no', 'cazar', 'todo', 'abajo', 'diferente', 'o', 'guardar', '[objeto]', 'y', 'comercio', 'cosa', 'malo, innecesario', 'herramienta', 'interior', 'sucio', 'persona', 'amarillo', 'tener', 'pez', 'sonido', 'venir', 'planta', 'poder (hacer)', 'usar', 'fruta, verdura', 'piedra, gema', 'mancha, pasta', 'aire', 'color', 'grupo', 'escuchar, oir', '[contexto]', 'dormir', 'verde', 'cabeza', 'ropa', 'frio', '[predicado]', 'pequeño', 'linea', 'papel', 'rojo', 'en', 'mano, cinco (sistema complejo de numeros)', 'ver, mirar', 'agujero', 'terreno, tierra', 'padre', 'dinero', 'mujer', 'mi, yo', 'hombre', 'comer', 'muerto', 'atras', '[miau]', 'luna', 'jugar', 'mucho, tres o mas (sistema simple de numeros)', 'numero', 'loco, borracho', 'camino', 'montaña', 'esto, este, eso', 'nombre, palabra', 'pie', '[mandato]', 'amor', 'el, ella, ellos, eso', 'abrir', 'romper, destruir', 'hacer', 'palo', 'comida, miga', 'dar', 'de', 'sentir', 'negro', 'fin', 'insecto', 'cerca', 'contenedor, caja', 'bueno', '[interactuar con el libro]', 'igual', 'fuego, caliente', 'piel', 'que', 'alto', 'cuerpo', 'circulo, bola', 'nuevo', 'vos', 'adelante', 'imagen, dibujo', 'saber', 'animal', 'grande, importante', 'sol', 'superficie', 'dulce', 'a causa de, por', 'pero', 'a, movimiento a', 'agua', 'tiempo', 'hablar, hola, idioma', 'casa, cuarto', 'dos', 'sexo', 'boca', 'luchar', 'blanco', 'uno', 'pajaro', 'fuerte', 'afuera', 'necesitar']
        elif check == '3' or check.lower() == 'русский' or check.lower() == 'ru' or check.lower() == 'rus':
            globLang = 'ru'
            tkD = ['[ударение]', 'рептилия', 'нет', 'охота', 'все', 'ниже', 'разное', 'или', 'сохранить, сберечь', '[предмет]', 'и', 'торговля, коммерция', 'вещь', 'плохой, злой, ненужный', 'инструмент', 'интерьер', 'грязный, нечистый', 'человек', 'желтый', 'иметь', 'рыба', 'звук', 'приходить', 'растение', 'может', 'использовать', 'фрукт, овощ', 'камень, самоцвет', 'пятно, камедь', 'воздух', 'цвет', 'группа', 'слышать', '[контекст]', 'спать', 'зеленый', 'голова', 'одежда', 'холод', '[сказуемое]', 'маленький', 'линия', 'бумага', 'красный', 'на, в', 'рука, пять (сложная система счисления)', 'видеть, смотреть', 'дыра', 'земля', 'родитель', 'деньги', 'женщина', 'я, мой', 'мужчина', 'есть', 'мертвый', 'сзади', '[мяу]', 'луна', 'играть', 'много, три или больше (простая система счисления)', 'число', 'сумасшедший, пьяный', 'путь', 'гора', 'это, то', 'имя, слово', 'нога', '[команда / мандат]', 'любовь', 'он, она, они, оно', 'открыть', 'сломать, уничтожить', 'сделать', 'палка', 'еда, зерно', 'дать', 'из', 'чувствовать', 'черный', 'конец', 'насекомое', 'рядом', 'контейнер, коробка', 'хорошо', '[взаимодействовать с книгой]', 'то же', 'огонь, горячий', 'кожа', 'что', 'высокий', 'тело', 'круг, шар', 'новый', 'ты', 'перед', 'изображение, рисунок', 'знать', 'животное', 'большой, важный', 'солнце', 'поверхность', 'сладкий', 'из-за, от', 'но', 'к, движение к', 'вода', 'время', 'говорить, привет, язык', 'дом, комната', 'два', 'секс', 'рот', 'бороться', 'белый', 'один', 'птица', 'сильный', 'снаружи', 'хотеть, нуждаться']
        elif check == '4' or check.lower() == 'toki pona' or check.lower() == 'tok':
            tkD = tkW
            globLang = 'tok'
        elif check.lower() == 'back':
            os.system('cls')
            settings()
        else:
            os.system('cls')
            print('\nSorry, that is not an option. Did you spell it correctly?')
            lang(True)
    os.system('cls')
    print(msg(0, globLang))
    print(msg(98, globLang))
    start()
def credits():
    print(msg(21, globLang))
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        extra()
    else:
        os.system('cls')
        print(msg(1, globLang))
    credits()
def iToF(type, chk):
    if type == 'back':
        if chk.lower() == 'back' or chk.lower() == 'volver' or chk.lower() == 'назад' or chk.lower() == 'pini':
            return True
    elif type == 'exit':
        if chk.lower() == 'exit' or chk.lower() == 'salir' or chk.lower() == 'выход' or chk.lower() == 'weka':
            return True
    elif type == 'set.lang':
        if chk.lower() == 'language' or chk.lower() == 'idioma' or chk.lower() == 'язык' or chk.lower() == 'toki':
            return True
    elif type == 'set.cred':
        if chk.lower() == 'credits' or chk.lower() == 'créditos' or chk.lower() == 'creditos' or chk.lower() == 'кредиты' or chk.lower() == 'pona e ni':
            return True
    elif type == 'set.seti':
        if chk.lower() == 'settings' or chk.lower() == 'ajustes' or chk.lower() == 'настройки' or chk.lower() == 'lipu ante':
            return True
    elif type == 'set.leso':
        if chk.lower() == 'lesson' or chk.lower() == 'lección' or chk.lower() == 'leccion' or chk.lower() == 'урок' or chk.lower() == 'pana sina e sona':
            return True
    elif type == 'set.prac':
        if chk.lower() == 'practice' or chk.lower() == 'practicar' or chk.lower() == 'практика' or chk.lower() == 'lipu sona':
            return True
    elif type == 'set.chek':
        if chk.lower() == 'check' or chk.lower() == 'comprobar' or chk.lower() == 'проверка' or chk.lower() == 'lukin':
            return True
    elif type == 'set.extr':
        if chk.lower() == 'extra' or chk.lower() == 'дополнительно' or chk.lower() == 'namako':
            return True
    elif type == 'lan.engl':
        if chk.lower() == 'english' or chk.lower() == 'inglés' or chk.lower() == 'ingles' or chk.lower() == 'английский' or chk.lower() == 'toki inli':
            return True
    elif type == 'lan.span':
        if chk.lower() == 'spanish' or chk.lower() == 'español' or chk.lower() == 'espanol' or chk.lower() == 'испанский' or chk.lower() == 'toki epanja':
            return True
    elif type == 'lan.rusi':
        if chk.lower() == 'russian' or chk.lower() == 'ruso' or chk.lower() == 'русский'  or chk.lower() == 'toki losi':
            return True
    elif type == 'lan.grek':
        if chk.lower() == 'greek' or chk.lower() == 'griego' or chk.lower() == 'греческий'  or chk.lower() == 'toki elina':
            return True
    elif type == 'lan.japa':
        if chk.lower() == 'japanese' or chk.lower() == 'japonés' or chk.lower() == 'japones' or chk.lower() == 'японский'  or chk.lower() == 'toki nijon':
            return True
    elif type == 'lan.hebr':
        if chk.lower() == 'hebrew' or chk.lower() == 'hebreo' or chk.lower() == 'иврит'  or chk.lower() == 'toki anku':
            return True
    elif type == 'lan.tkpn':
        if chk.lower() == 'toki pona' or chk.lower() == 'токи пона'  or chk.lower() == 'toki pona':
            return True
    elif type == 'lan.kore':
        if chk.lower() == 'korean' or chk.lower() == 'coreano' or chk.lower() == 'корейский'  or chk.lower() == 'toki anku':
            return True
    elif type == 'lan.arab':
        if chk.lower() == 'arabic' or chk.lower() == 'arabe' or chk.lower() == 'арабский'  or chk.lower() == 'toki alapi':
            return True
    elif type == 'lan.arme':
        if chk.lower() == 'armenian' or chk.lower() == 'armenio' or chk.lower() == 'армянский'  or chk.lower() == 'toki armenian':
            return True
    elif type == 'lan.turk':
        if chk.lower() == 'turkish' or chk.lower() == 'turco' or chk.lower() == 'турецкий'  or chk.lower() == 'toki tuki':
            return True
    elif type == 'lan.inuk':
        if chk.lower() == 'inuktitut' or chk.lower() == 'инуктитут'  or chk.lower() == 'toki inuktitut':
            return True
    elif type == 'lan.futh':
        if chk.lower() == 'futhark' or chk.lower() == 'футарк'  or chk.lower() == 'toki futhark':
            return True
    elif type == 'lan.espe':
        if chk.lower() == 'esperanto' or chk.lower() == 'эсперанто'  or chk.lower() == 'toki epelanto':
            return True
    elif type == 'set.dict':
        if chk.lower() == 'dictionary' or chk.lower() == 'diccionario' or chk.lower() == 'словарь'  or chk.lower() == 'lipu nimi':
            return True
def msg(type, lang):
    if lang == 'en':
        if int(type) == 0:
            return '\n### Welcome to HAP ' + ver + '! ###'
        elif int(type) == 1:
            return '\nSorry, that is not an option. Did you spell it correctly?'
        elif int(type) == 2:
            return '\nWhat would you like to do?\n- Check\n- Practice (WIP)\n- Lesson (WIP)\n- Dictionary (Toki Pona)\n- Extra\n- Exit'
        elif int(type) == 3:
            return '\nWhat would you like to do?\n- Language\n- Back'
        elif int(type) == 4:
            return '\nThis feature has still not been added.'
        elif int(type) == 5:
            return '\nWhat language would you like to check?\n- English\n- Spanish\n- Russian (Cyrillic)\n- Greek\n- Japanese (Hiragana & Katakana)\n- Hebrew\n- Toki Pona\n- Korean (Hangul)\n- Arabic\n- Armenian\n- Turkish\n- Inuktitut\n- Futhark\n- Esperanto\n- Back'
        elif int(type) == 6:
            return '\nIf you want to go back type "Back". If you want to check a letter, type the respective number.'
        elif int(type) == 7:
            return '\nIf you want to go back, type "Back".'
        elif int(type) == 8:
            return '\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.'
        elif int(type) == 9:
            return 'Letter: '
        elif int(type) == 10:
            return 'Name: '
        elif int(type) == 11:
            return 'Number in alphabet: '
        elif int(type) == 12:
            return 'IPA pronounciation: '
        elif int(type) == 13:
            return '\nWhat phonetic alphabet would you like to check?\n- Hiragana\n- Katakana\n- Back'
        elif int(type) == 14:
            return '\nWhat language would you like to practice?\n- English (WIP)\n- Spanish (WIP)\n- Russian (Cyrillic) (WIP)\n- Greek (WIP)\n- Japanese (Hiragana & Katakana) (WIP)\n- Hebrew (WIP)\n- Toki Pona (WIP)\n- Korean (Hangul) (WIP)\n- Arabic (WIP)\n- Armenian (WIP)\n- Turkish (WIP)\n- Inuktitut (WIP)\n- Futhark (WIP)\n- Esperanto (WIP)\n- Back'
        elif int(type) == 15:
            return '\nChange: Makes one letter longer the letter after it.'
        elif int(type) == 16:
            return '\nChange: Makes one letter longer the letter before it. (Only if it is the same vocal)'
        elif int(type) == 17:
            return '\nChange: Makes the "sh" sound.'
        elif int(type) == 18:
            return '\nChange: Only used letter with this is the Üü. If there is a "g" or "q" before and a "e" and "i" after a "u" it is not pronounced, but not if it is a "ü".'
        elif int(type) == 19:
            return '\nChange: Adds stress to the letter.'
        elif int(type) == 20:
            return 'Variations:'
        elif int(type) == 21:
            return '\nCredits:\n- Code: Luke\n- Translations:\n-- English: Luke\n-- Spanish: Luke\n-- Russian: DeepL Translate\n-- Toki Pona: Luke\n- Ideas: Luke and friends'
        elif int(type) == 22:
            return '\nWhat  would you like to do?\n- Settings\n- Credits\n- Back'
        elif int(type) == 23:
            return '\nIf you want to go back type "Back". If you want to check a word, type the respective number.'
        elif int(type) == 24:
            return 'Definition: '
        elif int(type) == 25:
            return 'With vowels: '
        elif int(type) == 26:
            return 'With long vowels: '
        elif int(type) == 27:
            return 'Change: Makes the vowel longer'
        elif int(type) == 97:
            return '\nREMINDER: I still havent added the "Harakat".\n'
        elif int(type) == 98:
            return '\nREMINDER: Make sure to have the keyboards of the languages downloaded, if not, you may see boxes instead of the letters.'
        elif int(type) == 99:
            return '\nREMINDER: I still havent added the "Geresh" and the "Vowel points".\n'
    elif lang == 'es':
        if int(type) == 0:
            return '\n### Bienvenido a HAP ' + ver + '! ###'
        elif int(type) == 1:
            return '\nLo siento, eso no es una opción. ¿Lo has escrito correctamente?'
        elif int(type) == 2:
            return '\n¿Qué te gustaría hacer?\n- Comprobar\n- Practicar (WIP)\n- Lección (WIP)\n- Diccionario (Toki Pona)\n- Extra\n- Salir'
        elif int(type) == 3:
            return '\n¿Qué te gustaría hacer?\n- Idioma\n- Volver'
        elif int(type) == 4:
            return '\nEsta función aún no se ha añadido.'
        elif int(type) == 5:
            return '\n¿Qué idioma desea comprobar?\n- Inglés\n- Español\n- Ruso (Cirílico)\n- Griego\n- Japonés (Hiragana & Katakana)\n- Hebreo\n- Toki Pona\n- Coreano (Hangul)\n- Arabe\n- Armenio\n- Turco\n- Inuktitut\n- Futhark\n- Esperanto\n- Volver'
        elif int(type) == 6:
            return '\nSi desea volver atrás, escriba "Volver". Si desea comprobar una letra, escriba el número correspondiente.'
        elif int(type) == 7:
            return '\nSi desea volver atrás, escriba "Volver".'
        elif int(type) == 8:
            return '\nSi desea volver atrás, escriba "Volver". Si desea comprobar una variación de la letra, escriba el número correspondiente.'
        elif int(type) == 9:
            return 'Letra: '
        elif int(type) == 10:
            return 'Nombre: '
        elif int(type) == 11:
            return 'Número en alfabeto: '
        elif int(type) == 12:
            return 'Pronunciación del IPA: '
        elif int(type) == 13:
            return '\n¿Qué alfabeto fonético desea consultar?\n- Hiragana\n- Katakana\n- Volver'
        elif int(type) == 14:
            return '\n¿Qué idioma te gustaría practicar?\n- Inglés (WIP)\n- Español (WIP)\n- Ruso (Cirílico) (WIP)\n- Griego (WIP)\n- Japonés (Hiragana & Katakana) (WIP)\n- Hebreo (WIP)\n- Toki Pona (WIP)\n- Coreano (Hangul) (WIP)\n- Arabe (WIP)\n- Armenio (WIP)\n- Turco (WIP)\n- Inuktitut (WIP)\n- Futhark (WIP)\n- Esperanto (WIP)\n- Volver'
        elif int(type) == 15:
            return '\nCambio: Hace una letra más larga la letra que le sigue.'
        elif int(type) == 16:
            return '\nCambio: Alarga una letra la letra que la antecede. (Sólo si es la misma vocal)'
        elif int(type) == 17:
            return '\nCambio: Hace el sonido "sh".'
        elif int(type) == 18:
            return '\nCambio: La única letra que se usa con esto es la Üü. Si hay una "g" o una "q" antes y una "e" o "i" despues de una "u" no se pronuncia, pero no si es una "ü".'
        elif int(type) == 19:
            return '\nCambio: Añade acento/estrés a la letra.'
        elif int(type) == 20:
            return 'Variaciones:'
        elif int(type) == 21:
            return '\nCréditos:\n- Código: Luke\n- Traducciones:\n-- Inglés: Luke\n-- Español: Luke\n-- Ruso: Traductor DeepL\n-- Toki Pona: Luke\n- Ideas: Luke y amigos'
        elif int(type) == 22:
            return '\n¿Qué te gustaría hacer?\n- Ajustes\n- Créditos\n- Volver'
        elif int(type) == 23:
            return '\nSi desea volver atrás, escriba "Volver". Si desea comprobar una palabra, escriba el número correspondiente.'
        elif int(type) == 24:
            return 'Definición: '
        elif int(type) == 25:
            return 'Con vocales: '
        elif int(type) == 26:
            return 'Con vocales largas: '
        elif int(type) == 27:
            return 'Cambio: Hace la vocal mas larga'
        elif int(type) == 97:
            return '\nRECORDATORIO: Todavía no he añadido los "Harakat".\n'
        elif int(type) == 98:
            return '\nRECORDATORIO: Asegúrese de tener descargados los teclados de los idiomas, si no, es posible que vea cuadrados en lugar de las letras.'
        elif int(type) == 99:
            return '\nRECORDATORIO: Todavía no he añadido los "Geresh" y los "Puntos vocálicos".\n'
    elif lang == 'ru':
        if int(type) == 0:
            return '\n### Добро пожаловать в HAP ' + ver + '! ###'
        elif int(type) == 1:
            return '\nИзвините, это не вариант. Вы правильно написали?'
        elif int(type) == 2:
            return '\nЧто бы вы хотели сделать?\n- Проверка\n- Практика (WIP)\n- Урок (WIP)\n- Словарь (Токи Пона)\n- Дополнительно\n- Выход'
        elif int(type) == 3:
            return '\nЧто бы вы хотели сделать?\n- Язык\n- Назад'
        elif int(type) == 4:
            return '\nЭта функция до сих пор не добавлена.'
        elif int(type) == 5:
            return '\nКакой язык вы хотите проверить?\n- Английский\n- Испанский\n- Русский (Кириллица)\n- Греческий\n- Японский (Хирагана и Катакана)\n- Иврит\n- Токи Пона\n- Корейский (Хангыль)\n- Арабский\n- Армянский\n- Турецкий\n- Инуктитут\n- Футарк\n- Эсперанто\n- Назад'
        elif int(type) == 6:
            return '\nЕсли вы хотите вернуться назад, введите "Назад". Если вы хотите проверить букву, введите соответствующий номер.'
        elif int(type) == 7:
            return '\nЕсли вы хотите вернуться назад, введите "Назад".'
        elif int(type) == 8:
            return '\nЕсли вы хотите вернуться назад, введите "Назад". Если вы хотите проверить буквенный вариант, введите соответствующий номер.'
        elif int(type) == 9:
            return 'Письмо: '
        elif int(type) == 10:
            return 'Имя: '
        elif int(type) == 11:
            return 'Номер в алфавите: '
        elif int(type) == 12:
            return 'IPA произношение: '
        elif int(type) == 13:
            return '\nКакой фонетический алфавит вы хотите проверить?\n- Хирагана\n- Катакана\n- Назад'
        elif int(type) == 14:
            return '\nКакой язык вы хотели бы практиковать?\n- Английский (WIP)\n- Испанский (WIP)\n- Русский (Кириллица) (WIP)\n- Греческий (WIP)\n- Японский (Хирагана и Катакана) (WIP)\n- Иврит (WIP)\n- Токи Пона (WIP)\n- Корейский (Хангыль) (WIP)\n- - Арабский (WIP)\n- Армянский (WIP)\n- Турецкий (WIP)\n- Инуктитут (WIP)\n- Футарк (WIP)\n- Эсперанто (WIP)\n- Назад'
        elif int(type) == 15:
            return '\nИзменение: Делает одну букву длиннее следующей за ней буквы.'
        elif int(type) == 16:
            return '\nИзменение: Делает одну букву длиннее предыдущей. (Только если это один и тот же вокал).'
        elif int(type) == 17:
            return '\nИзменения: Произносит звук "ш".'
        elif int(type) == 18:
            return '\nИзменение: Единственной используемой буквой при этом является Üü. Если перед "u" стоит "g" или "q", а после "u" - "e" или "i", то она не произносится, но произносится, если это "ü".'
        elif int(type) == 19:
            return '\nИзменение: Добавляет ударение к букве.'
        elif int(type) == 20:
            return 'Вариации:'
        elif int(type) == 21:
            return '\nКредиты:\n- Код: Luke\n- Переводы:\n-- Английский: Luke\n-- Испанский: Luke\n-- Русский: DeepL Translate\n- Токи Пона: Luke\n- Идеи: Luke и друзья'
        elif int(type) == 22:
            return '\nЧто бы вы хотели сделать?\n- Настройки\n- Кредиты\n- Назад'
        elif int(type) == 23:
            return '\nЕсли вы хотите вернуться назад, введите "Назад". Если вы хотите проверить слово, введите соответствующий номер.'
        elif int(type) == 24:
            return 'Определение: '
        elif int(type) == 25:
            return 'С гласными: '
        elif int(type) == 26:
            return 'С долгими гласными: '
        elif int(type) == 27:
            return 'Изменение: Делает гласный более долгим'
        elif int(type) == 97:
            return '\nПОМНИТЕ: Я все еще не добавил "Харакат".\n'
        elif int(type) == 98:
            return '\nПОМНИТЕ: Убедитесь, что загружены клавиатуры соответствующих языков, если нет, то вместо букв вы можете увидеть квадратики.'
        elif int(type) == 99:
            return '\nПОМНИТЕ: Я все еще не добавил "Гереш" и "Гласные точки".\n'
    elif lang == "tok":
        if int(type) == 0:
            return '\n### o kama pona lon HAP ' + ver + '! ###'
        elif int(type) == 1:
            return '\nmi pakala · ni li lon ala. sina sitelen pona e ni anu seme'
        elif int(type) == 2:
            return '\nsina wile pali e seme\n- lukin\n- pana sina e sona (WIP)\n- lipu sona (WIP)\n- lipu nimi (toki pona)\n- namako\n- weka'
        elif int(type) == 3:
            return '\nsina wile pali e seme\n- toki\n- pini'
        elif int(type) == 4:
            return '\ntenpo ni la ijo ni li lon ala' 
        elif int(type) == 5:
            return '\nsina wile lukin e toki seme\n- toki Inli\n- toki Epanja\n- toki Losi (sitelen Losi)\n- toki Elina\n- toki Nijon (sitelen Ilakana & sitelen Katakana)\n- toki Hebrew\n- toki pona\n- toki Anku (sitelen Anku)\n- toki Alapi\n- toki Armenian\n- toki Tuki\n- toki Inuktitut\n- toki Futhark\n- toki Epelanto\n- pini'
        elif int(type) == 6:
            return '\nsina wile pini e ni la sina sitelen e "pini" · sina wile lukin e sitelen la sina sitelen e nanpa ona'
        elif int(type) == 7:
            return '\nsina wile pini e ni la sina sitelen e "pini"'
        elif int(type) == 8:
            return '\nsina wile pini e ni la sina sitelen e "pini" · sina wile lukin e ante sitelen la sina sitelen e nanpa ona'
        elif int(type) == 9:
            return 'sitelen: '
        elif int(type) == 10:
            return 'nimi: '
        elif int(type) == 11:
            return 'nanpa lon sitelen mute: '
        elif int(type) == 12:
            return 'kalama IPA: '
        elif int(type) == 13:
            return '\nsina wile lukin e sitelen kalama seme\n- sitelen Ilakana\n- sitelen Katakana\n- pini'
        elif int(type) == 14:
            return '\nsina wile sona e toki seme\n- toki Inli (WIP)\n- toki Epanja (WIP)\n- toki Losi (sitelen Losi) (WIP)\n- toki Elina (WIP)\n- toki Nijon (sitelen Ilakana & sitelen Katakana) (WIP)\n- toki Hebrew (WIP)\n- toki pona (WIP)\n- toki Anku (sitelen Anku) (WIP)\n- toki Alapi (WIP)\n- toki Armenian (WIP)\n- toki Tuki (WIP)\n- toki Inuktitut (WIP)\n- toki Futhark (WIP)\n- toki Epelanto (WIP)\n- pini'
        elif int(type) == 15:
            return '\nante: o sitelen sinpin li kama lon e suli wan'
        elif int(type) == 16:
            return '\nante: o sitelen monsi li kama lon e suli wan (ona li sitelen sama taso)'
        elif int(type) == 17:
            return '\nante: o kalama e "sh"'
        elif int(type) == 18:
            return '\nante: o "Üü" kepeken lon ni taso · "g" anu "q" li lon monsi e ni en "e" en "i" li lon sinpin e sitelen "u" la "u" li kalama ala · ona li sitelen "ü" la nimi mute monsi ni li lon ala'
        elif int(type) == 19:
            return '\nante: o namako sitelen e suli'
        elif int(type) == 20:
            return 'ante:'
        elif int(type) == 21:
            return '\npona e ni:\n- nanpa sona: jan Lan (Luke)\n- ante toki:\n-- toki Inli: jan Lan (Luke)\n-- toki Epanja: jan Lan (Luke)\n-- toki Losi: ante toki DeepL\n-- toki pona: jan Lan (Luke)\n- lawa sona: jan Lan (Luke) en jan pona'
        elif int(type) == 22:
            return '\nsina wile pali e seme\n- lipu ante\n- pona e ni\n- pini'
        elif int(type) == 23:
            return '\nsina wile pini e ni la sina sitelen e "pini" · sina wile lukin e nimi la sina sitelen e nanpa ona'
        elif int(type) == 24:
            return 'nimi lon: '
        elif int(type) == 25:
            return 'kepeken sitelen a: '
        elif int(type) == 26:
            return 'kepeken sitelen a suli: '
        elif int(type) == 27:
            return 'ante: o sitelen a li kama lon e suli'
        elif int(type) == 97:
            return '\nijo suli: tenpo ni la mi lon ala e "Harakat"'
        elif int(type) == 98:
            return '\nijo suli: o lukin e ni · sina jo e toki sitelen · nimi mute monsi ni li lon ala la sina ken lukin ala sitelen'
        elif int(type) == 99:
            return '\nijo suli: tenpo ni la mi lon ala e "Geresh" e "Vowel points"'
    elif lang == 'no-language':
        return 'Language Error'
lang(False)
