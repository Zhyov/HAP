import random, os
eL = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
eP = ['eɪ (ei)', 'biː (bii)', 'siː (sii)', 'diː (dii)', 'iː (ii)', 'ɛf (ef)', 'dʒiː (ji)', 'eɪtʃ (eich), heɪtʃ (heich)', 'aɪ (ai)', 'dʒeɪ (jei)', 'keɪ (kei)', 'ɛl (el)', 'ɛm (em)', 'ɛn (en)', 'oʊ (ou)', 'piː (pi)', 'kjuː (kyu)', 'ɑːr (aar)', 'ɛs (es)', 'tiː (tii)', 'juː (yuu)', 'viː (vii)', 'dʌbəl.juː (dabel yu)', 'ɛks (eks)', 'waɪ (wai)', 'zɛd (zed)']
eN = ['a', 'bee', 'cee', 'dee', 'e', 'ef', 'jee', 'aitch, haitch', 'i', 'jay', 'kay', 'el', 'em', 'en', 'o', 'pee', 'cue, kew, kue, que', 'ar', 'ess', 'tee', 'u', 'vee', 'double-u', 'ex', 'wy, wye, why', 'zed']
sL = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Ññ', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
sP = ['æ (a)', 'b', 'k, s', 'd', 'ɛ (e)', 'f', 'g', '(silent)', 'i', 'x (kh, h)', 'k', 'l', 'm', 'n', 'ɲ (ñ, ny)', 'o', 'p', 'k', 'ɾ (r), r (rr)', 's', 't', 'u', 'v', 'u, w', 'ks (x)', 'i (short), ʂ (sh)', 'θ (th no vibration), s (depends on accent)']
sN = ['a', 'be, be larga', 'ce', 'de', 'e', 'efe', 'ge', 'hache', 'i', 'jota', 'ka', 'ele', 'eme', 'ene', 'eñe', 'o', 'pe', 'qü or cu', 'erre', 'ese', 'te', 'u', 've, uve, ve corta', 'doble v' , 'equis', 'i griega', 'zeta, seta (depends on accent)']
rL = ['Аа', 'Бб', 'Вв', 'Гг', 'Дд', 'Ее', 'Ёё', 'Жж', 'Зз', 'Ии', 'Йй', 'Кк', 'Лл', 'Мм', 'Нн', 'Oo', 'Пп', 'Рр', 'Сс', 'Тт', 'Уу', 'Фф', 'Хх', 'Цц', 'Чч', 'Шш', 'Щщ', 'Ъъ', 'Ыы', 'Ьь', 'Ээ', 'Юю', 'Яя']
rP = ['æ (a)', 'b', 'v', 'g', 'd', 'jɛ (ye), ɛ (e)', 'jo (yo)', 'ʐ (zh)', 'z', 'i', 'i (short)', 'k', 'ɫ (l)', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'x (kh, h)', 'ts', 'tɕ (ch)', 'ʂ (sh)', 'ɕ (sch)', '"', 'ɨ (y)', "'", 'e', 'ju (yu)', 'ja (ya)']
rN = ['а', 'бэ', 'вэ', 'гэ', 'дэ', 'е', 'ё', 'жэ', 'зэ', 'и', 'и краткое', 'ка', 'эль, эл', 'эм', 'эн', 'о', 'пэ', 'эр', 'эс', 'тэ', 'у', 'эф', 'ха', 'цэ', 'че', 'ша', 'ща', 'твёрдый знак', 'ы', 'мягкий знак', 'э', 'ю', 'я']
gL = ['Αα', 'Ββ', 'Γγ', 'Δδ', 'Εε', 'Ζζ', 'Ηη', 'Θθ', 'Ιι', 'Κκ', 'Λλ', 'Μμ', 'Νν', 'Ξξ', 'Οο', 'Ππ', 'Ρρ', 'Σσς', 'Ττ', 'Υυ', 'Φφ', 'Χχ', 'Ψψ', 'Ωω']
gP = ['ɐ (a)', 'v', 'ɣ (g)', 'ð (th vibration)', 'e', 'z', 'i (short)', 'θ (th no vibration)', 'i', 'k', 'l', 'm', 'n', 'ks (x)', 'o', 'p', 'r', 's, z (before β, γ, or μ)', 't', 'i (short)', 'f', 'ç (h)', 'ps', 'o̞ (o)']
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
hP = ['ʔ (a)', 'v', 'ɣ (gh)', 'ð (th vibration)', 'h', 'v', 'z', 'χ (ch, kh, h)', 't', 'j (y)', 'χ (ch, kh, h)', 'l', 'm', 'n', 's', 'ɑ̯/ʕ (weird a | For more info, search: Voiced pharyngeal fricative)', 'f', 'ts', 'k', 'ʁ (french r)', 'ʃ (sh), s (For more info, check the "Shin" and "Sin" bellow)', 'θ (th no vibration)']
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
tkDefinitions = []
kL = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ']
kP = ['g, k', 'n', 'd, t', 'ɭ (l), ɾ (r)', 'm', 'b, p', 's, t', '(silent), ŋ (ng)', 'dz (j)', 'tɕ (ch)', 'k', 't', 'p', 'h', 'a', 'ja (ya)', 'ʌ (eo)', 'jʌ (yeo)', 'o', 'jo (yo)', 'u', 'ju (yu)', 'ɯ (eu)', 'i']
aL = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ڧ', 'ک/ك', 'ل', 'م', 'ن', 'ه', 'و', 'ے/ي']
aP = ['a', 'b', 't', 'θ (th no vibration)', 'dʒ (j)', 'ħ (h)', 'x (kh)', 'd', 'ð (th vibration)', 'r', 'z', 's', 'ʃ (sh)', 'sˤ (s throat constricted)', 'dˤ (d throat constricted)', 'tˤ (t throat constricted)', 'ðˤ (th vibration throat constricted)', 'ɑ̯/ʕ (weird a | For more info, search: Voiced pharyngeal fricative)', 'ɣ (g)', 'f', 'q', 'k', 'l', 'm', 'n', 'h', 'w, ū, ∅', 'y, ī']
aN = ['أَلِف', 'بَاء/بَه', 'تَاء/تَه', 'ثَاء/ثَه', 'جِيم', 'حَاء/حَه', 'خَاء/خَه', 'دَال/دَاء/دَه', 'ذَال/ذَاء/ذَه', 'رَاء/رَه', 'زَاي/زَين/زَاء/زَه', 'سِين', 'شِين', 'صَاد', 'ضَاد/ضَاء/ضَه', 'طَاء/طَه', 'ظَاء/ظَه', 'عَيْن', 'غَيْن', 'فَاء/فَه', 'قَاف', 'كَاف/كَاء/كَه', 'لاَم', 'مِيم', 'نُون', 'هَاء/هَه', 'وَاو', 'يَاء/يَه']
globLang = 'no-language'
ver = 'v0.6'

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
        for i, e in enumerate(sL):
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
    if check.lower() == 'hiragana':
        os.system('cls')
        jHE()
    elif check.lower() == 'katakana':
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
    print(msg(24, globLang) + tkDefinitions[i])
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
    global globLang, tkDefinitions
    if sm == False:
        print('\nSelect a language:\n1 - en (English)\n2 - es (Español)\n3 - ru (Русский)')
        check = input('>> ')
        if check == '1' or check.lower() == 'english' or check.lower() == 'en':
            globLang = 'en'
            tkDefinitions = ['[emphasis]', 'reptile', 'no', 'hunt', 'everything, all', 'below', 'different', 'or', 'keep, save', '[object]', 'and', 'trade, commerce', 'thing', 'bad, evil, unnecessary', 'tool', 'interior', 'dirty, unclean', 'person', 'yellow', 'to have', 'fish', 'sound', 'to come', 'plant', 'can', 'to use', 'fruit, vegetable', 'stone, gem', 'stain, gum', 'air', 'colour / color', 'group', 'to hear', '[context]', 'to sleep', 'green', 'head', 'clothing', 'cold', '[predicate]', 'small', 'line', 'paper', 'red', 'on, in', 'hand, five (complex number system)', 'to see, to look', 'hole', 'land, earth', 'parent', 'money', 'woman', 'me, my, I', 'man', 'to eat', 'dead', 'behind, back', '[meow]', 'moon', 'to play', 'many, three or more (simple number system)', 'number', 'crazy, drunk', 'path', 'mountain', 'this, that', 'name, word', 'leg', '[command / mandate]', 'love', 'he, she, they, it', 'to open', 'break, destroy', 'to do, to make', 'stick', 'food, grain', 'to give', 'of', 'to feel', 'black', 'end', 'insect', 'near', 'container, box', 'good', '[interact with the book]', 'same', 'fire, hot', 'skin', 'what', 'tall', 'body', 'circle, ball', 'new', 'you', 'in front', 'image, drawing', 'to know', 'animal', 'big, important', 'sun', 'surface', 'sweet', 'because of, from', 'but', 'to, movement to', 'water', 'time', 'talk, hello, language', 'house, room', 'two', 'sex', 'mouth', 'to fight', 'white', 'one', 'bird', 'strong', 'outside', 'to want, to need']
        elif check == '2' or check.lower() == 'español' or check.lower() == 'espanol' or check.lower() == 'es':
            globLang = 'es'
            tkDefinitions = ['[enfasis]', 'reptil', 'no', 'cazar', 'todo', 'abajo', 'diferente', 'o', 'guardar', '[objeto]', 'y', 'comercio', 'cosa', 'malo, innecesario', 'herramienta', 'interior', 'sucio', 'persona', 'amarillo', 'tener', 'pez', 'sonido', 'venir', 'planta', 'poder (hacer)', 'usar', 'fruta, verdura', 'piedra, gema', 'mancha, pasta', 'aire', 'color', 'grupo', 'escuchar, oir', '[contexto]', 'dormir', 'verde', 'cabeza', 'ropa', 'frio', '[predicado]', 'pequeño', 'linea', 'papel', 'rojo', 'en', 'mano, cinco (sistema complejo de numeros)', 'ver, mirar', 'agujero', 'terreno, tierra', 'padre', 'dinero', 'mujer', 'mi, yo', 'hombre', 'comer', 'muerto', 'atras', '[miau]', 'luna', 'jugar', 'mucho, tres o mas (sistema simple de numeros)', 'numero', 'loco, borracho', 'camino', 'montaña', 'esto, este, eso', 'nombre, palabra', 'pie', '[mandato]', 'amor', 'el, ella, ellos, eso', 'abrir', 'romper, destruir', 'hacer', 'palo', 'comida, miga', 'dar', 'de', 'sentir', 'negro', 'fin', 'insecto', 'cerca', 'contenedor, caja', 'bueno', '[interactuar con el libro]', 'igual', 'fuego, caliente', 'piel', 'que', 'alto', 'cuerpo', 'circulo, bola', 'nuevo', 'vos', 'adelante', 'imagen, dibujo', 'saber', 'animal', 'grande, importante', 'sol', 'superficie', 'dulce', 'a causa de, por', 'pero', 'a, movimiento a', 'agua', 'tiempo', 'hablar, hola, idioma', 'casa, cuarto', 'dos', 'sexo', 'boca', 'luchar', 'blanco', 'uno', 'pajaro', 'fuerte', 'afuera', 'necesitar']
        elif check == '3' or check.lower() == 'русский' or check.lower() == 'ru':
            globLang = 'ru'
            tkDefinitions = ['[ударение]', 'рептилия', 'нет', 'охота', 'все', 'ниже', 'разное', 'или', 'сохранить, сберечь', '[предмет]', 'и', 'торговля, коммерция', 'вещь', 'плохой, злой, ненужный', 'инструмент', 'интерьер', 'грязный, нечистый', 'человек', 'желтый', 'иметь', 'рыба', 'звук', 'приходить', 'растение', 'может', 'использовать', 'фрукт, овощ', 'камень, самоцвет', 'пятно, камедь', 'воздух', 'цвет', 'группа', 'слышать', '[контекст]', 'спать', 'зеленый', 'голова', 'одежда', 'холод', '[сказуемое]', 'маленький', 'линия', 'бумага', 'красный', 'на, в', 'рука, пять (сложная система счисления)', 'видеть, смотреть', 'дыра', 'земля', 'родитель', 'деньги', 'женщина', 'я, мой', 'мужчина', 'есть', 'мертвый', 'сзади', '[мяу]', 'луна', 'играть', 'много, три или больше (простая система счисления)', 'число', 'сумасшедший, пьяный', 'путь', 'гора', 'это, то', 'имя, слово', 'нога', '[команда / мандат]', 'любовь', 'он, она, они, оно', 'открыть', 'сломать, уничтожить', 'сделать', 'палка', 'еда, зерно', 'дать', 'из', 'чувствовать', 'черный', 'конец', 'насекомое', 'рядом', 'контейнер, коробка', 'хорошо', '[взаимодействовать с книгой]', 'то же', 'огонь, горячий', 'кожа', 'что', 'высокий', 'тело', 'круг, шар', 'новый', 'ты', 'перед', 'изображение, рисунок', 'знать', 'животное', 'большой, важный', 'солнце', 'поверхность', 'сладкий', 'из-за, от', 'но', 'к, движение к', 'вода', 'время', 'говорить, привет, язык', 'дом, комната', 'два', 'секс', 'рот', 'бороться', 'белый', 'один', 'птица', 'сильный', 'снаружи', 'хотеть, нуждаться']
        else:
            os.system('cls')
            print('\nSorry, that is not an option. Did you spell it correctly?')
            lang(False)
    elif sm == True:
        print('\nSelect a language:\n1 - en (English)\n2 - es (Español)\n3 - ru (Русский)\n- Back')
        check = input('>> ')
        if check == '1' or check.lower() == 'english' or check.lower() == 'en':
            globLang = 'en'
            tkDefinitions = ['[emphasis]', 'reptile', 'no', 'hunt', 'everything, all', 'below', 'different', 'or', 'keep, save', '[object]', 'and', 'trade, commerce', 'thing', 'bad, evil, unnecessary', 'tool', 'interior', 'dirty, unclean', 'person', 'yellow', 'to have', 'fish', 'sound', 'to come', 'plant', 'can', 'to use', 'fruit, vegetable', 'stone, gem', 'stain, gum', 'air', 'colour / color', 'group', 'to hear', '[context]', 'to sleep', 'green', 'head', 'clothing', 'cold', '[predicate]', 'small', 'line', 'paper', 'red', 'on, in', 'hand, five (complex number system)', 'to see, to look', 'hole', 'land, earth', 'parent', 'money', 'woman', 'me, my, I', 'man', 'to eat', 'dead', 'behind, back', '[meow]', 'moon', 'to play', 'many, three or more (simple number system)', 'number', 'crazy, drunk', 'path', 'mountain', 'this, that', 'name, word', 'leg', '[command / mandate]', 'love', 'he, she, they, it', 'to open', 'break, destroy', 'to do, to make', 'stick', 'food, grain', 'to give', 'of', 'to feel', 'black', 'end', 'insect', 'near', 'container, box', 'good', '[interact with the book]', 'same', 'fire, hot', 'skin', 'what', 'tall', 'body', 'circle, ball', 'new', 'you', 'in front', 'image, drawing', 'to know', 'animal', 'big, important', 'sun', 'surface', 'sweet', 'because of, from', 'but', 'to, movement to', 'water', 'time', 'talk, hello, language', 'house, room', 'two', 'sex', 'mouth', 'to fight', 'white', 'one', 'bird', 'strong', 'outside', 'to want, to need']
        elif check == '2' or check.lower() == 'español' or check.lower() == 'es':
            globLang = 'es'
            tkDefinitions = ['[enfasis]', 'reptil', 'no', 'cazar', 'todo', 'abajo', 'diferente', 'o', 'guardar', '[objeto]', 'y', 'comercio', 'cosa', 'malo, innecesario', 'herramienta', 'interior', 'sucio', 'persona', 'amarillo', 'tener', 'pez', 'sonido', 'venir', 'planta', 'poder (hacer)', 'usar', 'fruta, verdura', 'piedra, gema', 'mancha, pasta', 'aire', 'color', 'grupo', 'escuchar, oir', '[contexto]', 'dormir', 'verde', 'cabeza', 'ropa', 'frio', '[predicado]', 'pequeño', 'linea', 'papel', 'rojo', 'en', 'mano, cinco (sistema complejo de numeros)', 'ver, mirar', 'agujero', 'terreno, tierra', 'padre', 'dinero', 'mujer', 'mi, yo', 'hombre', 'comer', 'muerto', 'atras', '[miau]', 'luna', 'jugar', 'mucho, tres o mas (sistema simple de numeros)', 'numero', 'loco, borracho', 'camino', 'montaña', 'esto, este, eso', 'nombre, palabra', 'pie', '[mandato]', 'amor', 'el, ella, ellos, eso', 'abrir', 'romper, destruir', 'hacer', 'palo', 'comida, miga', 'dar', 'de', 'sentir', 'negro', 'fin', 'insecto', 'cerca', 'contenedor, caja', 'bueno', '[interactuar con el libro]', 'igual', 'fuego, caliente', 'piel', 'que', 'alto', 'cuerpo', 'circulo, bola', 'nuevo', 'vos', 'adelante', 'imagen, dibujo', 'saber', 'animal', 'grande, importante', 'sol', 'superficie', 'dulce', 'a causa de, por', 'pero', 'a, movimiento a', 'agua', 'tiempo', 'hablar, hola, idioma', 'casa, cuarto', 'dos', 'sexo', 'boca', 'luchar', 'blanco', 'uno', 'pajaro', 'fuerte', 'afuera', 'necesitar']
        elif check == '3' or check.lower() == 'русский' or check.lower() == 'ru':
            globLang = 'ru'
            tkDefinitions = ['[ударение]', 'рептилия', 'нет', 'охота', 'все', 'ниже', 'разное', 'или', 'сохранить, сберечь', '[предмет]', 'и', 'торговля, коммерция', 'вещь', 'плохой, злой, ненужный', 'инструмент', 'интерьер', 'грязный, нечистый', 'человек', 'желтый', 'иметь', 'рыба', 'звук', 'приходить', 'растение', 'может', 'использовать', 'фрукт, овощ', 'камень, самоцвет', 'пятно, камедь', 'воздух', 'цвет', 'группа', 'слышать', '[контекст]', 'спать', 'зеленый', 'голова', 'одежда', 'холод', '[сказуемое]', 'маленький', 'линия', 'бумага', 'красный', 'на, в', 'рука, пять (сложная система счисления)', 'видеть, смотреть', 'дыра', 'земля', 'родитель', 'деньги', 'женщина', 'я, мой', 'мужчина', 'есть', 'мертвый', 'сзади', '[мяу]', 'луна', 'играть', 'много, три или больше (простая система счисления)', 'число', 'сумасшедший, пьяный', 'путь', 'гора', 'это, то', 'имя, слово', 'нога', '[команда / мандат]', 'любовь', 'он, она, они, оно', 'открыть', 'сломать, уничтожить', 'сделать', 'палка', 'еда, зерно', 'дать', 'из', 'чувствовать', 'черный', 'конец', 'насекомое', 'рядом', 'контейнер, коробка', 'хорошо', '[взаимодействовать с книгой]', 'то же', 'огонь, горячий', 'кожа', 'что', 'высокий', 'тело', 'круг, шар', 'новый', 'ты', 'перед', 'изображение, рисунок', 'знать', 'животное', 'большой, важный', 'солнце', 'поверхность', 'сладкий', 'из-за, от', 'но', 'к, движение к', 'вода', 'время', 'говорить, привет, язык', 'дом, комната', 'два', 'секс', 'рот', 'бороться', 'белый', 'один', 'птица', 'сильный', 'снаружи', 'хотеть, нуждаться']
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
        if chk.lower() == 'back' or chk.lower() == 'volver' or chk.lower() == 'назад':
            return True
    elif type == 'exit':
        if chk.lower() == 'exit' or chk.lower() == 'salir' or chk.lower() == 'выход':
            return True
    elif type == 'set.lang':
        if chk.lower() == 'language' or chk.lower() == 'idioma' or chk.lower() == 'язык':
            return True
    elif type == 'set.cred':
        if chk.lower() == 'credits' or chk.lower() == 'créditos' or chk.lower() == 'creditos' or chk.lower() == 'кредиты':
            return True
    elif type == 'set.seti':
        if chk.lower() == 'settings' or chk.lower() == 'ajustes' or chk.lower() == 'настройки':
            return True
    elif type == 'set.leso':
        if chk.lower() == 'lesson' or chk.lower() == 'lección' or chk.lower() == 'leccion' or chk.lower() == 'урок':
            return True
    elif type == 'set.prac':
        if chk.lower() == 'practice' or chk.lower() == 'practicar' or chk.lower() == 'практика':
            return True
    elif type == 'set.chek':
        if chk.lower() == 'check' or chk.lower() == 'comprobar' or chk.lower() == 'проверка':
            return True
    elif type == 'set.extr':
        if chk.lower() == 'extra' or chk.lower() == 'дополнительно':
            return True
    elif type == 'lan.engl':
        if chk.lower() == 'english' or chk.lower() == 'inglés' or chk.lower() == 'ingles' or chk.lower() == 'английский':
            return True
    elif type == 'lan.span':
        if chk.lower() == 'spanish' or chk.lower() == 'español' or chk.lower() == 'espanol' or chk.lower() == 'испанский':
            return True
    elif type == 'lan.rusi':
        if chk.lower() == 'russian' or chk.lower() == 'ruso' or chk.lower() == 'русский':
            return True
    elif type == 'lan.grek':
        if chk.lower() == 'greek' or chk.lower() == 'griego' or chk.lower() == 'греческий':
            return True
    elif type == 'lan.japa':
        if chk.lower() == 'japanese' or chk.lower() == 'japonés' or chk.lower() == 'japones' or chk.lower() == 'японский':
            return True
    elif type == 'lan.hebr':
        if chk.lower() == 'hebrew' or chk.lower() == 'hebreo' or chk.lower() == 'иврит':
            return True
    elif type == 'lan.tkpn':
        if chk.lower() == 'toki pona' or chk.lower() == 'токи пона':
            return True
    elif type == 'lan.kore':
        if chk.lower() == 'korean' or chk.lower() == 'coreano' or chk.lower() == 'корейский':
            return True
    elif type == 'lan.arab':
        if chk.lower() == 'arabic' or chk.lower() == 'arabe' or chk.lower() == 'арабский':
            return True
    elif type == 'set.dict':
        if chk.lower() == 'dictionary' or chk.lower() == 'diccionario' or chk.lower() == 'словарь':
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
            return '\nWhat language would you like to check?\n- English\n- Spanish\n- Russian (Cyrillic)\n- Greek\n- Japanese (Hiragana & Katakana)\n- Hebrew\n- Toki Pona\n- Korean (Hangul)\n- Arabic\n- Back'
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
            return '\nWhat language would you like to practice?\n- English (WIP)\n- Spanish (WIP)\n- Russian (Cyrillic) (WIP)\n- Greek (WIP)\n- Japanese (Hiragana & Katakana) (WIP)\n- Hebrew (WIP)\n- Toki Pona (WIP)\n- Korean (Hangul) (WIP)\n- Arabic (WIP)\n- Back'
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
            return '\nCredits:\n- Code: Luke\n- Translations:\n-- English: Luke\n-- Spanish: Luke\n-- Russian: DeepL Translate\n- Ideas: Luke'
        elif int(type) == 22:
            return '\nWhat  would you like to do?\n- Settings\n- Credits\n- Back'
        elif int(type) == 23:
            return '\nIf you want to go back type "Back". If you want to check a word, type the respective number.'
        elif int(type) == 24:
            return 'Definition: '
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
            return '\n¿Qué idioma desea comprobar?\n- Inglés\n- Español\n- Ruso (Cirílico)\n- Griego\n- Japonés (Hiragana & Katakana)\n- Hebreo\n- Toki Pona\n- Coreano (Hangul)\n- Arabe\n- Volver'
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
            return '\n¿Qué idioma te gustaría practicar?\n- Inglés (WIP)\n- Español (WIP)\n- Ruso (Cirílico) (WIP)\n- Griego (WIP)\n- Japonés (Hiragana & Katakana) (WIP)\n- Hebreo (WIP)\n- Toki Pona (WIP)\n- Coreano (Hangul) (WIP)\n- Arabe (WIP)\n- Volver'
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
            return '\nCréditos:\n- Código: Luke\n- Traducciones:\n-- Inglés: Luke\n-- Español: Luke\n-- Ruso: DeepL Traductor\n- Ideas: Luke'
        elif int(type) == 22:
            return '\n¿Qué te gustaría hacer?\n- Ajustes\n- Créditos\n- Volver'
        elif int(type) == 23:
            return '\nSi desea volver atrás, escriba "Volver". Si desea comprobar una palabra, escriba el número correspondiente.'
        elif int(type) == 24:
            return 'Definición: '
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
            return '\nКакой язык вы хотите проверить?\n- Английский\n- Испанский\n- Русский (Кириллица)\n- Греческий\n- Японский (Хирагана и Катакана)\n- Иврит\n- Токи Пона\n- Корейский (Хангыль)\n- Арабский\n- Назад'
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
            return '\nКакой язык вы хотели бы практиковать?\n- Английский (WIP)\n- Испанский (WIP)\n- Русский (Кириллица) (WIP)\n- Греческий (WIP)\n- Японский (Хирагана и Катакана) (WIP)\n- Иврит (WIP)\n- Токи Пона (WIP)\n- Корейский (Хангыль) (WIP)\n- - Арабский (WIP)\n- Назад'
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
            return '\nКредиты:\n- Код: Luke\n- Переводы:\n-- Английский: Luke\n-- Испанский: Luke\n-- Русский: DeepL Translate\n- Идеи: Luke'
        elif int(type) == 22:
            return '\nЧто бы вы хотели сделать?\n- Настройки\n- Кредиты\n- Назад'
        elif int(type) == 23:
            return '\nЕсли вы хотите вернуться назад, введите "Назад". Если вы хотите проверить слово, введите соответствующий номер.'
        elif int(type) == 24:
            return 'Определение: '
        elif int(type) == 98:
            return '\nПОМНИТЕ: Убедитесь, что загружены клавиатуры соответствующих языков, если нет, то вместо букв вы можете увидеть квадратики.'
        elif int(type) == 99:
            return '\nПОМНИТЕ: Я все еще не добавил "Гереш" и "Гласные точки".\n'
lang(False)
