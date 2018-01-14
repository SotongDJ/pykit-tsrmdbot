import mmcDefauV, mmctool, pprint

def chooseMode(lingua):
    final = open('descrimmc/'+lingua+'/analiChoose.descri').read()
    return final

def abratioMain(lingua,dicto):
    final = open('descrimmc/'+lingua+'/abratioMain.descri').read()
    final = final.replace('@mode@',mmctool.ul(dicto.get('mode','')))
    final = final.replace('@btempo@',mmctool.ul(dicto.get('btempo','')))
    final = final.replace('@ftempo@',mmctool.ul(dicto.get('ftempo','')))
    final = final.replace('@cokey@',mmctool.ul(dicto.get('cokey','')))
    final = final.replace('@cokas@',mmctool.ul(dicto.get('cokas',''),modda='klass',lingua=lingua))
    final = final.replace('@targe@',mmctool.ul(dicto.get('targe',''),modda='klass',lingua=lingua))
    return final

def abratioKeywo(lingua,keywo):
    final = open('descrimmc/'+lingua+'/abratioKeywo.descri').read()
    final = final.replace('@keywo@',keywo)
    return final

def abratioResut(lingua,resut):
    print('resut : '+pprint.pformat(resut, compact=True))

    btempo = resut.get('btempo','')
    ftempo = resut.get('ftempo','')
    cokas = resut.get('cokas','')
    cokey = resut.get('cokey','')
    targe = resut.get('targe','')
    pri = resut.get('pri',[])
    des = resut.get('des','')
    karen = resut.get('karen','')
    sam = resut.get('sam','')
    par = resut.get('par','')
    kub = resut.get('kub','')
    statik = resut.get('statik','')

    skdic = mmcDefauV.keywo('transle',lingua=lingua)

    a = open('descrimmc/'+lingua+'/abratioResutA.descri').read()
    a = a.replace('@btempo@',btempo)
    a = a.replace('@ftempo@',ftempo)
    a = a.replace('@cokey@',cokey)
    a = a.replace('@cokas@',skdic.get(cokas,''))
    a = a.replace('@targe@',skdic.get(targe,''))

    b = open('descrimmc/'+lingua+'/abratioResutB.descri').read()
    b = b.replace('@pri@','\n'.join(pri))
    b = b.replace('@des@',des)
    b = b.replace('@karen@',karen)
    b = b.replace('@sam@',sam)
    b = b.replace('@par@',par)
    b = b.replace('@kub@',kub)

    c = open('descrimmc/'+lingua+'/abratioResutC.descri').read()
    c = c.replace('@max@',statik.get('max',''))
    c = c.replace('@karen@',karen)
    c = c.replace('@maxPc@',statik.get('maxPc',''))
    c = c.replace('@max@',statik.get('max',''))
    c = c.replace('@min@',statik.get('min',''))
    c = c.replace('@minPc@',statik.get('minPc',''))
    c = c.replace('@time@',statik.get('time',''))
    c = c.replace('@dafro@',statik.get('dafro',''))

    return [a,b,c]

def atrenMain(lingua,dicto):
    ledic = mmcDefauV.keywo('leve')

    final = open('descrimmc/'+lingua+'/atrenMain.descri').read()

    final = final.replace('@mode@',mmctool.ul(dicto.get('mode','')))
    final = final.replace('@btempo@',mmctool.ul(dicto.get('btempo','')))
    final = final.replace('@ftempo@',mmctool.ul(dicto.get('ftempo','')))
    final = final.replace('@cokey@',mmctool.ul(dicto.get('cokey','')))
    final = final.replace('@cokas@',mmctool.ul(dicto.get('cokas',''),modda='klass',lingua=lingua))
    final = final.replace('@leve@',mmctool.ul(ledic.get(dicto.get('leve',10),''),modda='klass',lingua=lingua))
    return final

def atrenKeywo(lingua,keywo):
    final = open('descrimmc/'+lingua+'/atrenKeywo.descri').read()
    final = final.replace('@keywo@',keywo)
    return final

def atrenResut(lingua,resut):
    print('resut : '+pprint.pformat(resut, compact=True))

    btempo = resut.get('btempo','')
    ftempo = resut.get('ftempo','')
    cokas = resut.get('cokas','')
    cokey = resut.get('cokey','')
    graf = resut.get('graf',[])
    des = resut.get('des','')
    karen = resut.get('karen','')
    sam = resut.get('sam','')
    vam = resut.get('vam','')
    san = resut.get('san','')
    van = resut.get('van','')
    statik = resut.get('statik','')

    skdic = mmcDefauV.keywo('transle',lingua=lingua)

    a = open('descrimmc/'+lingua+'/atrenResutA.descri').read()
    a = a.replace('@btempo@',btempo)
    a = a.replace('@ftempo@',ftempo)
    a = a.replace('@cokey@',cokey)
    a = a.replace('@cokas@',skdic.get(cokas,''))

    b = open('descrimmc/'+lingua+'/atrenResutB.descri').read()
    b = b.replace('@graf@','\n'.join(graf))
    b = b.replace('@des@',des)
    b = b.replace('@karen@',karen)
    b = b.replace('@sam@',str(sam))

    c = open('descrimmc/'+lingua+'/atrenResutC.descri').read()
    c = c.replace('@karen@',karen)
    c = c.replace('@sam@',str(sam))
    c = c.replace('@san@',str(san))
    c = c.replace('@vam@',str(vam))
    c = c.replace('@van@',str(van))
    c = c.replace('@sinMax@',statik.get('sinMax',''))
    c = c.replace('@sinMaxPc@',statik.get('sinMaxPc',''))
    c = c.replace('@sinMin@',statik.get('sinMin',''))
    c = c.replace('@sinMinPc@',statik.get('sinMinPc',''))
    c = c.replace('@oveMaxPc@',statik.get('oveMaxPc',''))
    c = c.replace('@oveMaxDat@',statik.get('oveMaxDat',''))
    c = c.replace('@oveMinPc@',statik.get('oveMinPc',''))
    c = c.replace('@oveMinDat@',statik.get('oveMinDat',''))
    c = c.replace('@time@',statik.get('time',''))
    c = c.replace('@modeDat@',statik.get('modeDat',''))

    return [a,b,c]


def akaunMain(lingua,dicto):
    final = open('descrimmc/'+lingua+'/akaunMain.descri').read()

    final = final.replace('@mode@',mmctool.ul(dicto.get('mode','')))
    final = final.replace('@btempo@',mmctool.ul(dicto.get('btempo','')))
    final = final.replace('@ftempo@',mmctool.ul(dicto.get('ftempo','')))
    final = final.replace('@cokas@',mmctool.ul(dicto.get('cokas',''),modda='klass',lingua=lingua))
    final = final.replace('@acuno@',mmctool.ul(dicto.get('acuno',''),modda='klass',lingua=lingua))
    final = final.replace('@balan@',mmctool.ul(dicto.get('balan','')))
    return final

def akaunKeywo(lingua,keywo):
    final = open('descrimmc/'+lingua+'/akaunKeywo.descri').read()
    final = final.replace('@keywo@',keywo)
    return final

def akaunResut(lingua,resut):
    print('resut : '+pprint.pformat(resut, compact=True))

    btempo = resut.get('btempo','')
    ftempo = resut.get('ftempo','')
    acuno = resut.get('acuno','')
    cokas = resut.get('cokas','')
    balan = resut.get('basum','')
    pides = resut.get('pides','')
    codes = resut.get('codes','')
    blanc = resut.get('blanc','')
    pefin = resut.get('pefin','')
    infin = resut.get('infin','')
    otfin = resut.get('otfin','')
    linec = resut.get('linec','')
    bafin = resut.get('bafin','')

    skdic = mmcDefauV.keywo('transle',lingua=lingua)

    a = open('descrimmc/'+lingua+'/akaunResutA.descri').read()
    a = a.replace('@btempo@',btempo)
    a = a.replace('@ftempo@',ftempo)
    a = a.replace('@cokas@',skdic.get(cokas,''))
    a = a.replace('@acuno@',acuno)
    a = a.replace('@balan@',balan)

    b = open('descrimmc/'+lingua+'/akaunResutB.descri').read()
    b = b.replace('@pides@',pides)
    b = b.replace('@codes@',codes)

    c = open('descrimmc/'+lingua+'/akaunResutC.descri').read()
    c = c.replace('@blanc@',blanc)
    c = c.replace('@pefin@',pefin)
    c = c.replace('@infin@',infin)
    c = c.replace('@otfin@',otfin)
    c = c.replace('@linec@',linec)
    c = c.replace('@bafin@',bafin)

    return [a,b,c]

def disca(lingua):
    final = open('descrimmc/'+lingua+'/analiDisca.descri').read()
    return final
