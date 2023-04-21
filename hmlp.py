import random, os
sL = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Ññ', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
sP = ['æ (a)', 'b', 'k, s', 'd', 'ɛ (e)', 'f', 'g', '(silent)', 'i', 'x (kh, h)', 'k', 'l', 'm', 'n', 'ɲ (ñ, ny)', 'o', 'p', 'k', 'ɾ (r), r (rr)', 's', 't', 'u', 'v', 'u, w', 'ks (x)', 'i (short), ʂ (sh)', 'θ (th), s (depends on accent)']
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

print('### Welcome to HMLP v0.2! ###')
def sM(i, e):
    print('Letter: ' + e)
    print('Name: ' + sN[i])
    print('Number in Alphabet: ' + str((i + 1)))
    print('IPA Pronounciation: ' + sP[i])
    if e == 'Aa':
        print('Variations:\n1 - Áá\n2 - Ää')
    elif e == 'Ee':
        print('Variations:\n1- Éé\n2 - Ëë')
    elif e == 'Ii':
        print('Variations:\n1 - Íí\n2 - Ïï')
    elif e == 'Oo':
        print('Variations:\n1- Óó\n2 - Öö')
    elif e == 'Uu':
        print('Variations:\n1 - Úú\n2 - Üü')
    elif e == 'Cc' or e == 'Hh':
        print('Variations:\n1 - CHch')
    elif e == 'Ll':
        print('Variations:\n1 - LLll')
    if e == 'Aa' or e == 'Ee' or e == 'Ii' or e == 'Oo' or e == 'Uu':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number. If you want to hear the pronounciation, type "Audio".')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            sE()
        elif int(check) == 1:
            os.system('cls')
            print('\nChange: Adds stress to the letter.')
            print(f'\nIf you want to go back, type "Back".')
            check = input('>> ')
            if check.lower() == 'back':
                os.system('cls')
                sM(i, e)
        elif int(check) == 2:
            os.system('cls')
            print('\nChange: Only used letter with this is the Üü. If there is a "g" or "q" before a "u" it is not pronounced, but not if it is a "ü".')
            print(f'\nIf you want to go back, type "Back".')
            check = input('>> ')
            if check.lower() == 'back':
                os.system('cls')
                sM(i, e)
    elif e == 'Ll':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            sE()
        elif int(check) == 1:
            os.system('cls')
            print('\nChange: Makes the "sh" sound.')
            print(f'\nIf you want to go back, type "Back".')
            check = input('>> ')
            if check.lower() == 'back':
                os.system('cls')
                sM(i, e)
    else:
        print(f'\nIf you want to go back, type "Back".')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            sE()
def sE():
    for i, e in enumerate(sL):
        print(str((i + 1)) + ' - ' + e)
    print(f'\nIf you want to go back type "Back". If you want to check a letter, type the respective number.')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        c()
    else:
        for i, e in enumerate(sL):
            if int(check) == int(i) + 1:
                os.system('cls')
                sM(i, e)
def rM(i, e):
    print('Letter: ' + e)
    print('Name: ' + rN[i])
    print('Number in Alphabet: ' + str((i + 1)))
    print('IPA Pronounciation: ' + rP[i])
    print(f'\nIf you want to go back, type "Back".')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        rE()
def rE():
    for i, e in enumerate(rL):
        print(str((i + 1)) + ' - ' + e)
    print(f'\nIf you want to go back type "Back". If you want to check a letter, type the respective number.')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        c()
    else:
        for i, e in enumerate(rL):
            if int(check) == int(i) + 1:
                os.system('cls')
                rM(i, e)
def gM(i, e):
    print('Letter: ' + e)
    print('Name: ' + gN[i])
    print('Number in Alphabet: ' + str((i + 1)))
    print('IPA Pronounciation: ' + gP[i])
    if e == 'Αα':
        print('Variations:\n1 - Άά')
    elif e == 'Εε':
        print('Variations:\n1- Έέ')
    elif e == 'Ιι':
        print('Variations:\n1 - Ίί')
    elif e == 'Οο':
        print('Variations:\n1- Όό')
    elif e == 'Ωω':
        print('Variations:\n1 - Ώώ')
    elif e == 'Ηη':
        print('Variations:\n1 - Ήή')
    elif e == 'Υυ':
        print('Variations:\n1 - Ύύ')
    if e == 'Αα' or e == 'Εε' or e == 'Ιι' or e == 'Οο' or e == 'Ωω' or e == 'Ηη' or e == 'Υυ':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            gE()
        elif int(check) == 1:
            os.system('cls')
            print('\nChange: Adds stress to the letter.')
            print(f'\nIf you want to go back, type "Back".')
            check = input('>> ')
            if check.lower() == 'back':
                os.system('cls')
                gM(i, e)
    else:
        print(f'\nIf you want to go back, type "Back".')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            gE()
def gE():
    for i, e in enumerate(gL):
        print(str((i + 1)) + ' - ' + e)
    print(f'\nIf you want to go back type "Back". If you want to check a letter, type the respective number.')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        c()
    else:
        for i, e in enumerate(gL):
            if int(check) == int(i) + 1:
                os.system('cls')
                gM(i, e)
def jHM(i, e , c):
    print('Letter: ' + e)
    print('Number in Alphabet: ' + str((i + 1)))
    print('IPA Pronounciation: ' + jHP[i])
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
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            jHE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jHDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jHM2(i2, e2, i, e, c, 'D')
    elif e == 'つ':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            print('\nChange: Makes one letter longer the letter after it.')
            print(f'\nIf you want to go back, type "Back".')
            check = input('>> ')
            if check.lower() == 'back':
                os.system('cls')
                jKM(i, e, c)
    elif e == 'は' or e == 'ふ' or e == 'へ' or e == 'ほ':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
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
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
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
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
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
        print(f'\nIf you want to go back, type "Back".')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            jHE()
def jHM2(i, e, i2, e2, c, w):
    print('Letter: ' + e)
    if w == 'D':
        print('IPA Pronounciation: ' + jDP[i])
    elif w == 'H':
        print('IPA Pronounciation: ' + jHP2[i])
    print(f'\nIf you want to go back, type "Back".')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        jHM(i2, e2, c)
def jHM3(i, e, i2, e2, c, w):
    print('Letter: ' + e)
    if w == 'N':
        print('IPA Pronounciation: ' + jYP[i])
    elif w == 'D':
        print('IPA Pronounciation: ' + jDYP[i])
    elif w == 'H':
        print('IPA Pronounciation: ' + jHYP[i])
    print(f'\nIf you want to go back, type "Back".')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        jHM(i2, e2, c)
def jHE():
    for i, e in enumerate(jHL):
        print(str((i + 1)) + ' - ' + e)
    print(f'\nIf you want to go back type "Back". If you want to check a letter, type the respective number.')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        j()
    else:
        for i, e in enumerate(jHL):
            if int(check) == int(i) + 1:
                os.system('cls')
                jHM(i, e, check)
def jKM(i, e , c):
    print('Letter: ' + e)
    print('Number in Alphabet: ' + str((i + 1)))
    print('IPA Pronounciation: ' + jKP[i])
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
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
    elif e == 'ア' or e == 'イ' or e == 'ウ' or e == 'エ' or e == 'オ':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            jKE()
        elif int(check) == 1:
            print('\nChange: Makes one letter longer the letter before it. (Only if it is the same vocal)')
            print(f'\nIf you want to go back, type "Back".')
            check = input('>> ')
            if check.lower() == 'back':
                os.system('cls')
                jKM(i, e, c)
    elif e == 'ツ':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            jKE()
        elif int(check) == 1:
            for i2, e2 in enumerate(jKDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    jKM2(i2, e2, i, e, c, 'D')
        elif int(check) == 2:
            print('\nChange: Makes one letter longer the letter after it.')
            print(f'\nIf you want to go back, type "Back".')
            check = input('>> ')
            if check.lower() == 'back':
                os.system('cls')
                jKM(i, e, c)
    elif e == 'ハ' or e == 'フ' or e == 'ヘ' or e == 'ホ':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
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
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
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
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
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
        print(f'\nIf you want to go back, type "Back".')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            jKE()
def jKM2(i, e, i2, e2, c, w):
    print('Letter: ' + e)
    if w == 'D':
        print('IPA Pronounciation: ' + jDP[i])
    elif w == 'H':
        print('IPA Pronounciation: ' + jHP2[i])
    print(f'\nIf you want to go back, type "Back".')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        jKM(i2, e2, c)
def jKM3(i, e, i2, e2, c, w):
    print('Letter: ' + e)
    if w == 'N':
        print('IPA Pronounciation: ' + jYP[i])
    elif w == 'D':
        print('IPA Pronounciation: ' + jDYP[i])
    elif w == 'H':
        print('IPA Pronounciation: ' + jHYP[i])
    print(f'\nIf you want to go back, type "Back".')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        jKM(i2, e2, c)
def jKE():
    for i, e in enumerate(jKL):
        print(str((i + 1)) + ' - ' + e)
    print(f'\nIf you want to go back type "Back". If you want to check a letter, type the respective number.')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        j()
    else:
        for i, e in enumerate(jKL):
            if int(check) == int(i) + 1:
                os.system('cls')
                jKM(i, e, check)
def j():
    print(f'\nWhat phonetic alphabet would you like to check?\n- Hiragana\n- Katakana\n- Back')
    check = input('>> ')
    if check.lower() == 'hiragana':
        os.system('cls')
        jHE()
    elif check.lower() == 'katakana':
        os.system('cls')
        jKE()
    elif check.lower() == 'back':
        os.system('cls')
        c()
    else:
        os.system('cls')
        print(f'\nSorry, that is not an option. Did you spell it correctly?')
        j()
def hM(i, e, c):
    print('Letter: ' + e)
    print('Name: ' + hN[i])
    print('Number in Alphabet: ' + str((i + 1)))
    print('IPA Pronounciation: ' + hP[i])
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
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            hE()
        elif int(check) == 1:
            for i2, e2 in enumerate(hDL):
                if int(c) == int(i2) + 1:
                    os.system('cls')
                    hM2(i2, e2, i, e, c)
    elif e == 'ש':
        print(f'\nIf you want to go back, type "Back". If you want to check a letter variation, type the respective number.')
        check = input('>> ')
        if check.lower() == 'back':
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
        print(f'\nIf you want to go back, type "Back".')
        check = input('>> ')
        if check.lower() == 'back':
            os.system('cls')
            hE()
def hM2(i, e, i2, e2, c):
    print('Letter: ' + e)
    print('Name: ' + hDN[i])
    print('IPA Pronounciation: ' + hDP[i])
    print(f'\nIf you want to go back, type "Back".')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        hM(i2, e2, c)
def hM3(i, e, i2, e2, c, w):
    print('Letter: ' + e)
    if w == 'SH':
        print('Name: ' + hSHN[i])
        print('IPA Pronounciation: ' + hSHP[i])
    elif w == 'S':
        print('Name : ' + hSHN[i])
        print('IPA Pronounciation: ' + hSP[i])
    print(f'\nIf you want to go back, type "Back".')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        hM(i2, e2, c)
def hE():
    print('REMINDER: I still havent added the "Geresh" and the "Vowel points".\n')
    for i, e in enumerate(hL):
        print(str((i + 1)) + ' - ' + e)
    print(f'\nIf you want to go back type "Back". If you want to check a letter, type the respective number.')
    check = input('>> ')
    if check.lower() == 'back':
        os.system('cls')
        c()
    else:
        for i, e in enumerate(hL):
            if int(check) == int(i) + 1:
                os.system('cls')
                hM(i, e, check)
def c():
    print(f'\nWhat language would you like to check?\n- Spanish\n- Russian (Cyrillic)\n- Greek\n- Japanese (Hiragana & Katakana)\n- Hebrew\n- Back')
    check = input('>> ')
    if check.lower() == 'spanish':
        os.system('cls')
        sE()
    elif check.lower() == 'russian':
        os.system('cls')
        rE()
    elif check.lower() == 'greek':
        os.system('cls')
        gE()
    elif check.lower() == 'japanese':
        os.system('cls')
        j()
    elif check.lower() == 'hebrew':
        os.system('cls')
        hE()
    elif check.lower() == 'back':
        os.system('cls')
        start()
    else:
        os.system('cls')
        print(f'\nSorry, that is not an option. Did you spell it correctly?')
        c()
def p():
    print(f'\nWhat language would you like to practice?\n- Spanish (WIP)\n- Russian (Cyrillic) (WIP)\n- Greek (WIP)\n- Japanese (Hiragana & Katakana) (WIP)\n- Hebrew (WIP)\n- Back')
    check = input('>> ')
    if check.lower() == 'spanish':
        os.system('cls')
        print('This feature has still not been added.')
        start()
    elif check.lower() == 'russian':
        os.system('cls')
        print('This feature has still not been added.')
        start()
    elif check.lower() == 'greek':
        os.system('cls')
        print('This feature has still not been added.')
        start()
    elif check.lower() == 'japanese':
        os.system('cls')
        print('This feature has still not been added.')
        start()
    elif check.lower() == 'hebrew':
        os.system('cls')
        print('This feature has still not been added.')
        start()
    elif check.lower() == 'back':
        os.system('cls')
        start()
    else:
        os.system('cls')
        print(f'\nSorry, that is not an option. Did you spell it correctly?')
        p()
def start():
    print(f'\nWhat would you like to do?\n- Check\n- Practice (WIP)\n- Lesson (WIP)\n- Exit')
    check = input('>> ')
    if check.lower() == 'check':
        os.system('cls')
        c()
    elif check.lower() == 'practice':
        os.system('cls')
        p()
    elif check.lower() == 'lesson':
        os.system('cls')
        print('This feature has still not been added.')
        start()
    elif check.lower() == 'exit':
        exit()
    else:
        os.system('cls')
        print(f'\nSorry, that is not an option. Did you spell it correctly?')
    os.system('cls')
    start()
start()
