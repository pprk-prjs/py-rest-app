# -*- coding: utf-8 -*-
'''
Created on Oct 4, 2017

@author: peperk
'''
import scrapy
from datetime import datetime, timedelta, date
import pytvinfo.p_libs.p_utils as pu
from unidecode import unidecode
from pytvinfo.items import PytvinfoItem
import re

class WebTvInfo:
    
    start_urls = []
    
    def __init__(self):
        
        tomorrow = pu.time_str(datetime.now() + timedelta(days=1), '%Y-%m-%d')        
        #today link
        self.start_urls.append('http://www.tvprogram.cz/index.php?P_id_kategorie=56456&P_soubor=televize%2Findex.php%3F%26zobrazeni%3D%26typprg_pouze%3D%26casod%3D-1%26typzanr%3D',)
        #tomorrow link
        self.start_urls.append('http://www.tvprogram.cz/index.php?P_id_kategorie=56456&P_soubor=televize%2Findex.php%3Fdatum%3D{0}%26zobrazeni%3D%26typprg_pouze%3D%26casod%3D-1%26typzanr%3D'.format(tomorrow))

        # val = "Doma%7C%2CJOJ%7C%2CJOJ+Plus%7C%2CMark%EDza%7C%2CSTV1%7C%2CSTV2%7C%2CBarrandov%7C%2C%C8T1%7C%2C%C8T2%7C%2CNova%7C%2CPrima%7C%2C%C8eskoslovensko%7C%2CFestival%7C%2CJOJ+Family%7C%2CAXN%7C%2CAXN+Black%7C%2CAXN+Digi+TV%7C%2CAXN+HD%7C%2CAXN+White%7C%2CBarrandov+Plus%7C%2CCBS+Drama%7C%2CCinemax%7C%2CCinemax2%7C%2CCS+Film%7C%2CCS+Mini%7C%2C%C8S+Film%7C%2CNova+Action%7C%2CFilm+Europe%7C%2CFilm%2B%7C%2CFilmbox%7C%2CFilmbox+Extra+HD%7C%2CFilmbox+Family%7C%2CFilmbox+Plus%7C%2CFilmbox+Premium%7C%2CFine+Living+Network%7C%2CHBO%7C%2CHBO2%7C%2CHBO3%7C%2CHOROR+FILM%7C%2CJOJ+Cinema%7C%2CKino+Barrandov%7C%2CKino+CS%7C%2CNova+International%7C%2CPrima+Comedy+Central%7C%2CPrima+LOVE%7C%2CPrima+MAX%7C%2CNova+2%7C%2CNova+Gold%7C%2CVOYO%7C%2CAMC%7C%2CNova+Cinema%7C%2CPrima+Cool%7C%2C%C8T+%3AD%7C%2CDisney+Channel%7C%2CJim+Jam%7C%2CMegamax%7C%2CMinimax%7C%2CNickelodeon%7C%2CAnimalPlanet%7C%2CCBS+Reality%7C%2CCrime+and+Investigation%7C%2C%C8T+art%7C%2CDiscovery%7C%2CDiscovery+HD+Showcase%7C%2CDiscovery+Investigation%7C%2CDiscovery+Science%7C%2CDoku+CS%7C%2CDTX%7C%2CFood+Network+HD%7C%2CHistory+Channel%7C%2CKinoSv%ECt%7C%2CNational+Geographic%7C%2CNational+Geographic+HD%7C%2CNational+Geographic+Wild%7C%2CPrima+ZOOM%7C%2CSpektrum%7C%2CSpektrum+Home%7C%2CThe+Fishing+and+Hunting%7C%2CTLC%7C%2CTravel+Channel%7C%2CViasat+Explorer%7C%2CViasat+History%7C%2CViasat+History+HD%7C%2CViasat+Nature%7C%2CViasat+Nature+HD%7C%2CBtv%7C%2C%C8T24%7C%2CMeteoTV%7C%2CPOLAR%7C%2Cregionalnitelevize.cz%7C%2CRT+%DAstecko%7C%2CRTM%7C%2CSlov%E1cko%7C%2CTIK%7C%2CAuto+Motor+und+Sport+Channel%7C%2C%C8T4+Sport%7C%2CEurosport+1%7C%2CEurosport+2%7C%2CGolf+Channel%7C%2CNova+Sport+1%7C%2CNova+Sport+2%7C%2CO2+Sport%7C%2CO2TV+Fotbal%7C%2CO2TV+Tenis%7C%2CSport+5%7C%2CSport+M%7C%2CSport1%7C%2CSport2%7C%2CBarrandov+Family%7C%2CCountry+No.+1%7C%2CFUN1%7C%2CMTV%7C%2CMuzika+CS%7C%2C%D3%E8ko%7C%2C%D3%E8ko+Expres%7C%2C%D3%E8ko+Gold%7C%2CRetro+Music%7C%2CSlu%9Anej+Kan%E1l+TV%7C%2C%8Al%E1gr+TV%7C%2CErox+HD%7C%2CExtasy%7C%2CLeo%7C%2CFashionTV%7C%2CFashionTV+czsk%7C%2CHarmonie+TV%7C%2CHD+Plus%7C%2CID+Xtra%7C%2CJiho%E8esk%E1+televize%7C%2CM%F2am+TV%7C%2CM%F2au+TV%7C%2CNoe%7C%2CO2+Info+1%7C%2COIK+TV%7C%2CPaprika%7C%2CPRAHA+TV%7C%2CReality+Kings+TV%7C%2CRebel%7C%2Cregiony%2B%7C%2CRELAX%7C%2CRing%7C%2CV1%7C%2CZAK%7C%2CMark%EDza+International%7C%2CPrima+Plus%7C%2CTV+DAJTO%7C%2CWAU%7C%2Cduck.tv%7C%2Cduck.tv+HD%7C%2CRiK%7C%2C%8Duki%7C%2CCETV%7C%2CLiptov%7C%2CTA3%7C%2C213%7C%2CArena+Sport+1%7C%2CArena+Sport+2%7C%2CDigi+sport+SK%7C%2CDigi+sport+SK+2%7C%2CDigi+sport+SK+3%7C%2CDigi+sport+SK+4%7C%2CSpartak+TV%7C%2CMusic+Box%7C%2CSENZI%7C%2CKres%9Dansk%E1+telev%EDzia%7C%2CLifeTV%7C%2CLux%7C%2CPVTV%7C%2CR%E1dio+Vlna%7C%2CTV+Bratislava%7C%2CTV+Na%9Aa%7C%2CTV8%7C%2CTV9%7C%2CPolonia%7C%2CPolsat%7C%2CPolsat2%7C%2CTVP1%7C%2CTVP2%7C%2CTVP3%7C%2CKino+Polska%7C%2CPolsat+Film%7C%2CPolsat+Romans%7C%2CCartoon+Network+%28pl%29%7C%2CTVP+Historia%7C%2CTVP+Kultura%7C%2CPolsat+News%7C%2CnSport+HD%7C%2CPolsat+Sport%7C%2CPolsat+Sport+Extra%7C%2CPolsat+Sport+News%7C%2CTVP+Sport%7C%2CESKA+TV%7C%2CKuchnia%2B%7C%2CONTV%7C%2CPolsat+Caf%E9%7C%2CPolsat+Play%7C%2CPuls+2%7C%2CTele5%7C%2CTV+Bialorus%7C%2CTV+Puls%7C%2CTV4%7C%2CTV6%7C%2CTVN%7C%2CTVN7%7C%2CTVP+HD%7C%2CTVP+Info%7C%2CTVP+Rozrywka%7C%2CTVP+Seriale%7C%2CTVP+Warszawa%7C%2CTVS%7C%2CARD%7C%2CORF1%7C%2CORF2%7C%2CPRO7%7C%2CRTL%7C%2CRTL2%7C%2CVOX%7C%2CZDF.kultur%7C%2CKika%7C%2CSuper+RTL%7C%2CDeutsche+Welle%7C%2CZDFneo%7C%2CN24%7C%2CSPORT1+%28DSF%29%7C%2CDeluxe+Lounge+HD%7C%2CDeluxe+Music%7C%2CMTV+Germany%7C%2CVIVA%7C%2C3SAT%7C%2CANIXE+HD%7C%2CARD-alpha%7C%2CARTE%7C%2CATV+%28de%29%7C%2CBR%7C%2CEinsFestival%7C%2CEinsPlus%7C%2CHR-fernsehen%7C%2CKabel1%7C%2CMDR%7C%2Cn-tv%7C%2CNDR+Fernsehen%7C%2CORF+SPORT+%2B%7C%2CORF3%7C%2CPassion%7C%2CPhoenix%7C%2CPuls+4%7C%2CRBB+Berlin%7C%2CRTL+Crime%7C%2CRTL+Living%7C%2CRTL+Nitro%7C%2CSAT1%7C%2CSixx%7C%2CSWR+Fernsehen%7C%2Ctagesschau24%7C%2CWDR+Fernsehen%7C%2CZDF%7C%2CZDFinfo%7C%2CComedy+Central%7C%2CComedy+Central+Extra%7C%2CTCM%7C%2CTCM+%28v+UPC%29%7C%2CBaby+TV%7C%2CBoomerang%7C%2CCartoon+Network%7C%2CCartoon+Network+%28v+UPC+direct%29%7C%2CCartoon+Network+UK%7C%2CDisney+Junior%7C%2CDisney+Junior+HD+UK%7C%2CNick+Jr.%7C%2CNickelodeon+HD+UK%7C%2CPlayhouse+Disney%7C%2CAnimalPlanet+%28Digi+TV%29%7C%2CAnimalPlanet+UK%7C%2CCCTV9%7C%2CCrime+and+Investigation+UK%7C%2CDiscovery+%28Digi+TV%29+%28en%29%7C%2CDiscovery+EN%7C%2CDiscovery+History+SD%7C%2CDiscovery+Home+and+Health+SD+UK%7C%2CDocuBox+HD%7C%2CFilmBox+Arthouse%7C%2CFood+Network%7C%2CH2%7C%2CHistory+HD+UK%7C%2COutdoor+Channel%7C%2CAljazeera%7C%2CBBC+Entertainment%7C%2CBBC+World+News%7C%2CBloomberg%7C%2CCCTV+News%7C%2CCNBC+Europe%7C%2CCNN%7C%2CExtreme+Sports%7C%2CFightbox+HD%7C%2CMotorsTV%7C%2CSetanta+Sports+1%7C%2CSky+Sports+1%7C%2CSky+Sports+2%7C%2CSky+Sports+3%7C%2CSky+Sports+4%7C%2CSky+Sports+News%7C%2CThe+Active+Channel%7C%2CAlibi+SD+Ireland%7C%2CArirang%7C%2CAt+the+Races%7C%2CB+in+Balance%7C%2CBBC+Four%7C%2CBBC+One%7C%2CBBC+Three%7C%2CBBC+Two%7C%2CbeIN+LaLiga%7C%2CBeIn+Sports+11+HD%7C%2CBeIn+Sports+12+HD%7C%2CBeIn+Sports+13+HD%7C%2CBT+Sport+1+HD%7C%2CBT+Sport+2+HD%7C%2CBT+Sport+ESPN+SD%7C%2CBT+Sport+Europe+HD%7C%2CCanal%2B+Accion+HD%7C%2CCanal%2B+Comedia+HD%7C%2CCanal%2B+DCine+HD%7C%2CCanal%2B+Deportes+2+HD%7C%2CCanal%2B+Deportes+HD%7C%2CCanal%2B+Estrenos+HD%7C%2CCanal%2B+Futbol+HD%7C%2CCanal%2B+Golf+HD%7C%2CCanal%2B+Series+HD%7C%2CChannel+4%7C%2CChannel+5%7C%2CCNTV%7C%2CDave+SD+UK%7C%2CDisney+XD%7C%2CE%21+Entertainment%7C%2CE4+HD+UK%7C%2CEden+HD%7C%2CEnglish+Club+TV%7C%2CEurochannel%7C%2CEurosport+2+HD+British%7C%2CEurosport+HD+British%7C%2CEWTN+Africa+India%7C%2CFashion+One%7C%2CFashion+TV+F.MEN%7C%2CFashionBox+HD%7C%2CFashionTV+HD%7C%2CFast%26Funbox+HD%7C%2CFilm+4%7C%2CFuel%7C%2CGinx%7C%2CGood+Food+Channel+HD%7C%2CITV%7C%2CITV+HD+London%7C%2CITV2%7C%2CITV3%7C%2CITV4%7C%2CKBS+World%7C%2CLuxe.tv+HD%7C%2CMore+4%7C%2CNational+Geographic+HD+UK%7C%2CNational+Geographic+Wild+HD+Europe%7C%2CNBA+SD%7C%2CNHK+World+TV%7C%2CPick+TV%7C%2CPremier+Sports+SD%7C%2CRacing+UK+SD%7C%2CSetanta+Ireland+SD%7C%2CShortsHD%7C%2CSky+Arts+HD%7C%2CSky+Atlantic+HD+UK%7C%2CSky+Living+HD%7C%2CSky+Movies+Action+%26+Adventure+HD%7C%2CSky+Movies+Comedy+HD%7C%2CSky+Movies+Crime+%26+Thriller+HD%7C%2CSky+Movies+Disney+HD%7C%2CSky+Movies+Drama+%26+Romance+HD%7C%2CSky+Movies+Family+HD%7C%2CSky+Movies+Greats+HD%7C%2CSky+Movies+Premiere+HD%7C%2CSky+Movies+Select+HD%7C%2CSky+Movies+Showcase+HD%7C%2CSky+news%7C%2CSky+News+HD+UK%7C%2CSky+SciFi+%26+Horror+SD%7C%2CSky+Sports+5%7C%2CSky+Sports+F1+HD%7C%2CSky1+HD+UK%7C%2CSundance+TV%7C%2CSyfy+SD+UK%7C%2CTV5monde+%28en%29%7C%2CUniversal+SD+UK%7C%2CWorld+Fashion%7C%2C360TuneBox%7C%2CC+Music+TV%7C%2CiConcerts%7C%2CMTV+Dance%7C%2CMTV+Hits%7C%2CMTV+Live+HD%7C%2CMTV+Rocks%7C%2CMTV+UK+HD%7C%2CUnitel+Classica+HD%7C%2CVH1%7C%2CVH1+Classic%7C%2CAdult+Channel%7C%2CBlue+Hustler%7C%2CBrazzers+TV+Europe%7C%2CEroxxx+HD%7C%2CEsquire+TV%7C%2CHustler+HD%7C%2CHustler+TV%7C%2CPlayboy+TV%7C%2CPrivate+TV%7C%2CRedlight+HD%7C%2CSuper+One%7C%2CViasat+Spice%7C%2CATV%7C%2CAXN+Sat%7C%2CAXN+White+%28hu%29%7C%2CCool+TV%7C%2CFEM3%7C%2CFOX%7C%2CH%EDr+TV%7C%2CIzaura+TV%7C%2CLife+Network%7C%2CM3%7C%2CM5+HD%7C%2CMegamax+%28hu%29%7C%2CMozi%2B%7C%2CN%F3ta+TV%7C%2COzone+Network%7C%2CPaprika+%28hu%29%7C%2CParamount+Channel%7C%2CPax+TV%7C%2CPRIME%7C%2CPRO4%7C%2CRTL+klub%7C%2CRTL%2B%7C%2CRTL2+%28hu%29%7C%2CSpiler+TV%7C%2CStory4%7C%2CStory5%7C%2CSuperTV2%7C%2CTV2%7C%2CViasat6%7C%2CZenebutik%7C%2CH%21t+Music+Channel+%28hu%29%7C%2CMTV+%28hu%29%7C%2CMusic+Channel+%28hu%29%7C%2CMuzsika+TV%7C%2CVIVA+%28hu%29%7C%2CDigi+Sport+1+HD%7C%2CDigi+Sport+2+HD%7C%2CM4+Sport%7C%2CSport1+%28hu%29%7C%2CSport2+%28hu%29%7C%2CSportklub%7C%2CSportM+%28hu%29%7C%2CDiscovery+%28Digi+TV%29%7C%2CDiscovery+%28hu%29%7C%2CNational+Geographic+%28hu%29%7C%2CNational+Geographic+Wild+%28hu%29%7C%2CSpektrum+%28hu%29%7C%2CSpektrum+Home+%28hu%29%7C%2CThe+Fishing+and+Hunting+%28hu%29%7C%2CViasat3%7C%2CMinimax+%28hu%29%7C%2CNickelodeon+%28hu%29%7C%2CAXN+Black+%28hu%29%7C%2CCartoon+Network%2BTCM+%28hu%29%7C%2CComedy+Central+%28hu%29%7C%2CDoQ%7C%2CFilm+Caf%E9%7C%2CFilm+M%E1nia%7C%2CFilm%2B+%28hu%29%7C%2CFilm%2B+2%7C%2CMGM+%28hu%29%7C%2CSorozat%2B%7C%2CUniversal+Channel+%28hu%29%7C%2CDuna%7C%2CDuna+World%7C%2CM1%7C%2CM2%7C%2C1TV%7C%2CCCTV+Russkij%7C%2CKHL+TV%7C%2CRTR%7C%2CRussia+24%7C%2CShanson+TV%7C%2CSoyuz%7C%2CTNT-Comedy%7C%2CMuzyka+Pervogo%7C%2CDa+Vinci+Learning%7C%2CRT+Doc%7C%2CRussian+Travel+Guide%7C%2CVremya%7C%2CTV+Nanny%7C%2CDom+Kino%7C%2CAljazeera+%28Arabic%29%7C%2CBrava+HDTV%7C%2CBVN%7C%2CCCTV+Arabic%7C%2CCCTV4+Europe%7C%2CCredo%7C%2CGospel%7C%2CHRT1%7C%2CHRT2%7C%2CIneditTV%7C%2CJurnal+TV+Moldova%7C%2CKazakh+TV%7C%2CNetviet%7C%2CNPO+1%7C%2CNPO+2%7C%2CNPO+3%7C%2CProTV+International%7C%2CPublika%7C%2CRTL+4%7C%2CRTL+5%7C%2CR%DAV%7C%2CSBS6%7C%2CServusTV%7C%2CSlovenija+1%7C%2CSlovenija+2%7C%2CVeronica%7C%2CVTV4%7C%2CXMO%7C%2CBBC+Czech%7C%2CBBC+Radio%7C%2CClassic+FM%7C%2C%C8RO+-+D+Dur%7C%2C%C8RO+-+Plus%7C%2C%C8RO+-+Proglas%7C%2C%C8RO+-+Wave%7C%2C%C8Ro+Brno%7C%2C%C8Ro+%C8esk%E9+Bud%ECjovice%7C%2C%C8Ro+Hradec+Kr%E1lov%E9%7C%2C%C8Ro+Liberec%7C%2C%C8Ro+Olomouc%7C%2C%C8Ro+Ostrava%7C%2C%C8Ro+Pardubice%7C%2C%C8Ro+Plze%F2%7C%2C%C8Ro+Radio+Praha%7C%2C%C8Ro+Regina%7C%2C%C8Ro+Region+-+St%E8.+kraj%7C%2C%C8Ro+Region+-+Vyso%E8ina%7C%2C%C8Ro+Sever%7C%2C%C8RO1+-+Radio%9Eurn%E1l%7C%2C%C8RO2+-+Praha%7C%2C%C8RO3+-+Vltava%7C%2CDance+Radio%7C%2CEuropa+2%7C%2CFrekvence+1%7C%2CFun+r%E1dio%7C%2CImpuls%7C%2CJanko+Hra%9Ako%7C%2CJemne+Melodie%7C%2CLumen%7C%2CRadio+1%7C%2CRadio+Beat%7C%2CRadio+Expres%7C%2CR%E1dio+Junior%7C%2CRadio+Junior+%28sk%29%7C%2CRadio+Ko%9Aice%7C%2CR%E1dio+Retro%7C%2CRadio+%8Aport%7C%2CR%E1dio+VIVA%7C%2CRadio+WOW%7C%2CRadio7%7C%2CSRO1+-+Slovensko%7C%2CSRO2+-+Regina+Banska+Bystrica%7C%2CSRO2+-+Regina+Bratislava%7C%2CSRO2+-+Regina+Ko%9Aice%7C%2CSRO3+-+Dev%EDn%7C%2CSRO4+-+Radio+FM%7C%2CSRO5+-+Patria%7C%2CSRO6+-+Slovakia+International%7C%2CSRO7+-+Klasika%7C%2CSRO8+-+Litera%7C%2CCountry+Radio%7C%2C%C8RO+-+Jazz%7C%2CEvropa+2%7C%2CFajn+radio%7C%2CKiss+98%7C%2CKiss+Morava%7C%2CR%E1dio+Ant%E9na+Rock%7C%2CR%E1dio+Blan%EDk%7C%2CRadio+%C8as%7C%2CVALC+1+-+Gold%7C%2CVALC+2+-+Country+and+Folk%7C%2CVALC+3+-+Hit%7C%2CVALC+4+-+Rock%7C%2CVALC+5+-+Classic%7C%2CVALC+6+-+Valc%E1rka%7C%2CVALC+Live%7C"
        # val = "Doma%7C%2CJOJ%7C%2CJOJ+Plus%7C%2CMark%EDza%7C%2CSTV1%7C%2CSTV2%7C%2CBarrandov%7C%2C%C8T1%7C%2C%C8T2%7C%2CNova%7C%2CPrima%7C%2C%C8eskoslovensko%7C%2CFestival%7C%2CJOJ+Family%7C%2CAXN%7C%2CAXN+Black%7C%2CAXN+Digi+TV%7C%2CAXN+HD%7C%2CAXN+White%7C%2CBarrandov+Plus%7C%2CCBS+Drama%7C%2CCinemax%7C%2CCinemax2%7C%2CCS+Film%7C%2CCS+Mini%7C%2C%C8S+Film%7C%2CFANDA%7C%2CFilm+Europe%7C%2CFilm%2B%7C%2CFilmbox%7C%2CFilmbox+Extra+HD%7C%2CFilmbox+Family%7C%2CFilmbox+Plus%7C%2CFilmbox+Premium%7C%2CFine+Living+Network%7C%2CHBO%7C%2CHBO2%7C%2CHBO3%7C%2CHOROR+FILM%7C%2CJOJ+Cinema%7C%2CKino+Barrandov%7C%2CKino+CS%7C%2CNova+International%7C%2CPrima+Comedy+Central%7C%2CPrima+LOVE%7C%2CPrima+MAX%7C%2CSM%CDCHOV%7C%2CTELKA%7C%2CVOYO%7C%2CAMC%7C%2CNova+Cinema%7C%2CPrima+Cool%7C%2C%C8T+%3AD%7C%2CDisney+Channel%7C%2CJim+Jam%7C%2CMegamax%7C%2CMinimax%7C%2CNickelodeon%7C%2CAnimalPlanet%7C%2CCBS+Reality%7C%2CCrime+and+Investigation%7C%2C%C8T+art%7C%2CDiscovery%7C%2CDiscovery+HD+Showcase%7C%2CDiscovery+Investigation%7C%2CDiscovery+Science%7C%2CDoku+CS%7C%2CDTX%7C%2CFood+Network+HD%7C%2CHistory+Channel%7C%2CKinoSv%ECt%7C%2CNational+Geographic%7C%2CNational+Geographic+HD%7C%2CNational+Geographic+Wild%7C%2CPrima+ZOOM%7C%2CSpektrum%7C%2CSpektrum+Home%7C%2CThe+Fishing+and+Hunting%7C%2CTLC%7C%2CTravel+Channel%7C%2CViasat+Explorer%7C%2CViasat+History%7C%2CViasat+History+HD%7C%2CViasat+Nature%7C%2CViasat+Nature+HD%7C%2CBtv%7C%2C%C8T24%7C%2CMeteoTV%7C%2CPOLAR%7C%2Cregionalnitelevize.cz%7C%2CRT+%DAstecko%7C%2CRTM%7C%2CSlov%E1cko%7C%2CTIK%7C%2CAuto+Motor+und+Sport+Channel%7C%2C%C8T4+Sport%7C%2CEurosport+1%7C%2CEurosport+2%7C%2CGolf+Channel%7C%2CNova+Sport+1%7C%2CNova+Sport+2%7C%2CO2+Sport%7C%2CO2TV+Fotbal%7C%2CO2TV+Tenis%7C%2CSport+5%7C%2CSport+M%7C%2CSport1%7C%2CSport2%7C%2CBarrandov+Family%7C%2CCountry+No.+1%7C%2CFUN1%7C%2CMTV%7C%2CMuzika+CS%7C%2C%D3%E8ko%7C%2C%D3%E8ko+Expres%7C%2C%D3%E8ko+Gold%7C%2CRetro+Music%7C%2CSlu%9Anej+Kan%E1l+TV%7C%2C%8Al%E1gr+TV%7C%2CErox+HD%7C%2CExtasy%7C%2CLeo%7C%2CFashionTV%7C%2CFashionTV+czsk%7C%2CHarmonie+TV%7C%2CHD+Plus%7C%2CID+Xtra%7C%2CJiho%E8esk%E1+televize%7C%2CM%F2am+TV%7C%2CM%F2au+TV%7C%2CNoe%7C%2CO2+Info+1%7C%2COIK+TV%7C%2CPaprika%7C%2CPRAHA+TV%7C%2CReality+Kings+TV%7C%2CRebel%7C%2Cregiony%2B%7C%2CRELAX%7C%2CRing%7C%2CV1%7C%2CZAK%7C%2CMark%EDza+International%7C%2CPrima+Plus%7C%2CTV+DAJTO%7C%2CWAU%7C%2Cduck.tv%7C%2Cduck.tv+HD%7C%2CRiK%7C%2C%8Duki%7C%2CCETV%7C%2CLiptov%7C%2CTA3%7C%2C213%7C%2CArena+Sport+1%7C%2CArena+Sport+2%7C%2CDigi+sport+SK%7C%2CDigi+sport+SK+2%7C%2CDigi+sport+SK+3%7C%2CDigi+sport+SK+4%7C%2CSpartak+TV%7C%2CMusic+Box%7C%2CSENZI%7C%2CKres%9Dansk%E1+telev%EDzia%7C%2CLifeTV%7C%2CLux%7C%2CPVTV%7C%2CR%E1dio+Vlna%7C%2CTV+Bratislava%7C%2CTV+Na%9Aa%7C%2CTV8%7C%2CTV9%7C%2CPolonia%7C%2CPolsat%7C%2CPolsat2%7C%2CTVP1%7C%2CTVP2%7C%2CTVP3%7C%2CKino+Polska%7C%2CPolsat+Film%7C%2CPolsat+Romans%7C%2CCartoon+Network+%28pl%29%7C%2CTVP+Historia%7C%2CTVP+Kultura%7C%2CPolsat+News%7C%2CnSport+HD%7C%2CPolsat+Sport%7C%2CPolsat+Sport+Extra%7C%2CPolsat+Sport+News%7C%2CTVP+Sport%7C%2CESKA+TV%7C%2CKuchnia%2B%7C%2CONTV%7C%2CPolsat+Caf%E9%7C%2CPolsat+Play%7C%2CPuls+2%7C%2CTele5%7C%2CTV+Bialorus%7C%2CTV+Puls%7C%2CTV4%7C%2CTV6%7C%2CTVN%7C%2CTVN7%7C%2CTVP+HD%7C%2CTVP+Info%7C%2CTVP+Rozrywka%7C%2CTVP+Seriale%7C%2CTVP+Warszawa%7C%2CTVS%7C%2CARD%7C%2CORF1%7C%2CORF2%7C%2CPRO7%7C%2CRTL%7C%2CRTL2%7C%2CVOX%7C%2CZDF.kultur%7C%2CKika%7C%2CSuper+RTL%7C%2CDeutsche+Welle%7C%2CZDFneo%7C%2CN24%7C%2CSPORT1+%28DSF%29%7C%2CDeluxe+Lounge+HD%7C%2CDeluxe+Music%7C%2CMTV+Germany%7C%2CVIVA%7C%2C3SAT%7C%2CANIXE+HD%7C%2CARD-alpha%7C%2CARTE%7C%2CATV+%28de%29%7C%2CBR%7C%2CEinsFestival%7C%2CEinsPlus%7C%2CHR-fernsehen%7C%2CKabel1%7C%2CMDR%7C%2Cn-tv%7C%2CNDR+Fernsehen%7C%2CORF+SPORT+%2B%7C%2CORF3%7C%2CPassion%7C%2CPhoenix%7C%2CPuls+4%7C%2CRBB+Berlin%7C%2CRTL+Crime%7C%2CRTL+Living%7C%2CRTL+Nitro%7C%2CSAT1%7C%2CSixx%7C%2CSWR+Fernsehen%7C%2Ctagesschau24%7C%2CWDR+Fernsehen%7C%2CZDF%7C%2CZDFinfo%7C%2CComedy+Central%7C%2CComedy+Central+Extra%7C%2CTCM%7C%2CTCM+%28v+UPC%29%7C%2CBaby+TV%7C%2CBoomerang%7C%2CCartoon+Network%7C%2CCartoon+Network+%28v+UPC+direct%29%7C%2CCartoon+Network+UK%7C%2CDisney+Junior%7C%2CDisney+Junior+HD+UK%7C%2CNick+Jr.%7C%2CNickelodeon+HD+UK%7C%2CPlayhouse+Disney%7C%2CAnimalPlanet+%28Digi+TV%29%7C%2CAnimalPlanet+UK%7C%2CCCTV9%7C%2CCrime+and+Investigation+UK%7C%2CDiscovery+%28Digi+TV%29+%28en%29%7C%2CDiscovery+EN%7C%2CDiscovery+History+SD%7C%2CDiscovery+Home+and+Health+SD+UK%7C%2CDocuBox+HD%7C%2CFilmBox+Arthouse%7C%2CFood+Network%7C%2CH2%7C%2CHistory+HD+UK%7C%2COutdoor+Channel%7C%2CAljazeera%7C%2CBBC+Entertainment%7C%2CBBC+World+News%7C%2CBloomberg%7C%2CCCTV+News%7C%2CCNBC+Europe%7C%2CCNN%7C%2CExtreme+Sports%7C%2CFightbox+HD%7C%2CMotorsTV%7C%2CSetanta+Sports+1%7C%2CSky+Sports+1%7C%2CSky+Sports+2%7C%2CSky+Sports+3%7C%2CSky+Sports+4%7C%2CSky+Sports+News%7C%2CThe+Active+Channel%7C%2CAlibi+SD+Ireland%7C%2CArirang%7C%2CAt+the+Races%7C%2CB+in+Balance%7C%2CBBC+Four%7C%2CBBC+One%7C%2CBBC+Three%7C%2CBBC+Two%7C%2CbeIN+LaLiga%7C%2CBeIn+Sports+11+HD%7C%2CBeIn+Sports+12+HD%7C%2CBeIn+Sports+13+HD%7C%2CBT+Sport+1+HD%7C%2CBT+Sport+2+HD%7C%2CBT+Sport+ESPN+SD%7C%2CBT+Sport+Europe+HD%7C%2CCanal%2B+Accion+HD%7C%2CCanal%2B+Comedia+HD%7C%2CCanal%2B+DCine+HD%7C%2CCanal%2B+Deportes+2+HD%7C%2CCanal%2B+Deportes+HD%7C%2CCanal%2B+Estrenos+HD%7C%2CCanal%2B+Futbol+HD%7C%2CCanal%2B+Golf+HD%7C%2CCanal%2B+Series+HD%7C%2CChannel+4%7C%2CChannel+5%7C%2CCNTV%7C%2CDave+SD+UK%7C%2CDisney+XD%7C%2CE%21+Entertainment%7C%2CE4+HD+UK%7C%2CEden+HD%7C%2CEnglish+Club+TV%7C%2CEurochannel%7C%2CEurosport+2+HD+British%7C%2CEurosport+HD+British%7C%2CEWTN+Africa+India%7C%2CFashion+One%7C%2CFashion+TV+F.MEN%7C%2CFashionBox+HD%7C%2CFashionTV+HD%7C%2CFast%26Funbox+HD%7C%2CFilm+4%7C%2CFuel%7C%2CGinx%7C%2CGood+Food+Channel+HD%7C%2CITV%7C%2CITV+HD+London%7C%2CITV2%7C%2CITV3%7C%2CITV4%7C%2CKBS+World%7C%2CLuxe.tv+HD%7C%2CMore+4%7C%2CNational+Geographic+HD+UK%7C%2CNational+Geographic+Wild+HD+Europe%7C%2CNBA+SD%7C%2CNHK+World+TV%7C%2CPick+TV%7C%2CPremier+Sports+SD%7C%2CRacing+UK+SD%7C%2CSetanta+Ireland+SD%7C%2CShortsHD%7C%2CSky+Arts+HD%7C%2CSky+Atlantic+HD+UK%7C%2CSky+Living+HD%7C%2CSky+Movies+Action+%26+Adventure+HD%7C%2CSky+Movies+Comedy+HD%7C%2CSky+Movies+Crime+%26+Thriller+HD%7C%2CSky+Movies+Disney+HD%7C%2CSky+Movies+Drama+%26+Romance+HD%7C%2CSky+Movies+Family+HD%7C%2CSky+Movies+Greats+HD%7C%2CSky+Movies+Premiere+HD%7C%2CSky+Movies+Select+HD%7C%2CSky+Movies+Showcase+HD%7C%2CSky+news%7C%2CSky+News+HD+UK%7C%2CSky+SciFi+%26+Horror+SD%7C%2CSky+Sports+5%7C%2CSky+Sports+F1+HD%7C%2CSky1+HD+UK%7C%2CSundance+TV%7C%2CSyfy+SD+UK%7C%2CTV5monde+%28en%29%7C%2CUniversal+SD+UK%7C%2CWorld+Fashion%7C%2C360TuneBox%7C%2CC+Music+TV%7C%2CiConcerts%7C%2CMTV+Dance%7C%2CMTV+Hits%7C%2CMTV+Live+HD%7C%2CMTV+Rocks%7C%2CMTV+UK+HD%7C%2CUnitel+Classica+HD%7C%2CVH1%7C%2CVH1+Classic%7C%2CAdult+Channel%7C%2CBlue+Hustler%7C%2CBrazzers+TV+Europe%7C%2CEroxxx+HD%7C%2CEsquire+TV%7C%2CHustler+HD%7C%2CHustler+TV%7C%2CPlayboy+TV%7C%2CPrivate+TV%7C%2CRedlight+HD%7C%2CSuper+One%7C%2CViasat+Spice%7C%2CATV%7C%2CAXN+Sat%7C%2CAXN+White+%28hu%29%7C%2CCool+TV%7C%2CFEM3%7C%2CFOX%7C%2CH%EDr+TV%7C%2CIzaura+TV%7C%2CLife+Network%7C%2CM3%7C%2CM5+HD%7C%2CMegamax+%28hu%29%7C%2CMozi%2B%7C%2CN%F3ta+TV%7C%2COzone+Network%7C%2CPaprika+%28hu%29%7C%2CParamount+Channel%7C%2CPax+TV%7C%2CPRIME%7C%2CPRO4%7C%2CRTL+klub%7C%2CRTL%2B%7C%2CRTL2+%28hu%29%7C%2CSpiler+TV%7C%2CStory4%7C%2CStory5%7C%2CSuperTV2%7C%2CTV2%7C%2CViasat6%7C%2CZenebutik%7C%2CH%21t+Music+Channel+%28hu%29%7C%2CMTV+%28hu%29%7C%2CMusic+Channel+%28hu%29%7C%2CMuzsika+TV%7C%2CVIVA+%28hu%29%7C%2CDigi+Sport+1+HD%7C%2CDigi+Sport+2+HD%7C%2CM4+Sport%7C%2CSport1+%28hu%29%7C%2CSport2+%28hu%29%7C%2CSportklub%7C%2CSportM+%28hu%29%7C%2CDiscovery+%28Digi+TV%29%7C%2CDiscovery+%28hu%29%7C%2CNational+Geographic+%28hu%29%7C%2CNational+Geographic+Wild+%28hu%29%7C%2CSpektrum+%28hu%29%7C%2CSpektrum+Home+%28hu%29%7C%2CThe+Fishing+and+Hunting+%28hu%29%7C%2CViasat3%7C%2CMinimax+%28hu%29%7C%2CNickelodeon+%28hu%29%7C%2CAXN+Black+%28hu%29%7C%2CCartoon+Network%2BTCM+%28hu%29%7C%2CComedy+Central+%28hu%29%7C%2CDoQ%7C%2CFilm+Caf%E9%7C%2CFilm+M%E1nia%7C%2CFilm%2B+%28hu%29%7C%2CFilm%2B+2%7C%2CMGM+%28hu%29%7C%2CSorozat%2B%7C%2CUniversal+Channel+%28hu%29%7C%2CDuna%7C%2CDuna+World%7C%2CM1%7C%2CM2%7C%2C1TV%7C%2CCCTV+Russkij%7C%2CKHL+TV%7C%2CRTR%7C%2CRussia+24%7C%2CShanson+TV%7C%2CSoyuz%7C%2CTNT-Comedy%7C%2CMuzyka+Pervogo%7C%2CDa+Vinci+Learning%7C%2CRT+Doc%7C%2CRussian+Travel+Guide%7C%2CVremya%7C%2CTV+Nanny%7C%2CDom+Kino%7C%2CAljazeera+%28Arabic%29%7C%2CBrava+HDTV%7C%2CBVN%7C%2CCCTV+Arabic%7C%2CCCTV4+Europe%7C%2CCredo%7C%2CGospel%7C%2CHRT1%7C%2CHRT2%7C%2CIneditTV%7C%2CJurnal+TV+Moldova%7C%2CKazakh+TV%7C%2CNetviet%7C%2CNPO+1%7C%2CNPO+2%7C%2CNPO+3%7C%2CProTV+International%7C%2CPublika%7C%2CRTL+4%7C%2CRTL+5%7C%2CR%DAV%7C%2CSBS6%7C%2CServusTV%7C%2CSlovenija+1%7C%2CSlovenija+2%7C%2CVeronica%7C%2CVTV4%7C%2CXMO%7C%2CBBC+Czech%7C"
#         val = 'STV1%7C%2CSTV2%7C%2CMark%EDza%7C%2CJOJ%7C%2CJOJ+Plus%7C%2CDoma%7C%2CTV+DAJTO%7C%2CWAU%7C%2C%C8T1%7C%2C%C8T2%7C%2CNova%7C%2CNova+Cinema%7C%2CPrima%7C%2CPrima+Cool%7C%2CPrima+LOVE%7C%2CPrima+ZOOM%7C%2CSM%CDCHOV%7C%2CTELKA%7C%2CBarrandov%7C%2C%C8T4+Sport%7C%2C%C8T24%7C%2C%C8T+art%7C%2C%C8T+%3AD%7C%2CCountry+No.+1%7C%2CBBC+World+News%7C%2CFANDA%7C%2CKres%9Dansk%E1+telev%EDzia%7C%2C1TV%7C%2CKinoSv%ECt%7C%2CTA3%7C%2CLux%7C%2CNoe%7C'
        val = 'STV1%7C%2CSTV2%7C%2C'
#         val = "%C8T+art%7C%2CMusic+Box%7C%2CNova+2%7C%2CNova+Gold%7C%2CNova+Action%7C%2C%C8T24%7C%2CDoma%7C%2CJOJ%7C%2CJOJ+Plus%7C%2CMark%EDza%7C%2CSTV1%7C%2CSTV2%7C%2CBarrandov%7C%2C%C8T1%7C%2C%C8T2%7C%2CNova%7C%2CPrima%7C%2CJOJ+Family%7C%2CBarrandov+Plus%7C%2C%C8S+Film%7C%2CJOJ+Cinema%7C%2CKino+Barrandov%7C%2CKino+CS%7C%2CNova+International%7C%2CPrima+Comedy+Central%7C%2CPrima+LOVE%7C%2CPrima+MAX%7C%2CNova+Cinema%7C%2CPrima+Cool%7C%2C%C8T+%3AD%7C%2CKinoSv%ECt%7C%2CPrima+ZOOM%7C%2Cregionalnitelevize.cz%7C%2CSlov%E1cko%7C%2C%C8T4+Sport%7C%2CNova+Sport+1%7C%2CNova+Sport+2%7C%2CO2+Sport%7C%2CO2TV+Fotbal%7C%2CO2TV+Tenis%7C%2CSport+5%7C%2CSport+M%7C%2CSport1%7C%2CSport2%7C%2CBarrandov+Family%7C%2CMTV%7C%2C%D3%E8ko%7C%2C%D3%E8ko+Expres%7C%2C%D3%E8ko+Gold%7C%2CNoe%7C%2CMark%EDza+International%7C%2CPrima+Plus%7C%2CTV+DAJTO%7C%2CWAU%7C%2CTA3%7C%2CLux%7C%2CTV+Na%9Aa%7C%2CVIVA%7C"
        self.cookies = dict(P_cookies_televize_stanice=val)

        self.root_path = "//div[@id='program_obsah_tabulka']"
        self.tv_titles_path = "./*/table[@id='porady_prouzek_scroll_zakladna']//img[@class='logotv']/@title"
        self.table_first_level_path = "./table"
        self.table_all_levels_path = ".//table"
        self.tv_tds_path = ".//td[contains(@class, 'porady_prouzek')]"
        self.time = ".//span[@class='ntvp_cas']"
        self.td_nazov = './/td[@class="nazev"]'
        self.info = './/td[contains(@class,"info")]'
        self.now = datetime.now().replace(second=0, microsecond=0)
        

class TvInfoScrapy(scrapy.Spider):
    name = 'tv_info'
    __tv_list = None
    __epg_info = None

    def start_requests(self):
        self.urls = WebTvInfo()

        for info in self.urls.start_urls:
            yield scrapy.Request(info, cookies=self.urls.cookies, encoding='cp1250')
    

    def parse(self, response):
        # vyberie dany div
        program = response.xpath(self.urls.root_path)
        if len(program) == 0:
            return False
        program = program[0]
        #zobrazi nazvy stanic
        tab_tv_id = program.xpath(self.urls.tv_titles_path) 
        if self.__tv_list == None:
            self.__tv_list = tab_tv_id
             
        # print(tab_tv_id)
        # ziskam vsetky tabulky
        tables = program.xpath(self.urls.table_first_level_path)

        self.__epg_info = {}
        tabs_tds = []
        for table in tables:
            # ziskam stlpce danej tabulky
            tds = table.xpath(self.urls.tv_tds_path)
            name = table.xpath('@name')
            if len(name) > 0:
                name = name[0].extract()
#                 print(name)
#                 print(name[0][1:])
#                 print(tds)
                tabs_tds.append((int(name[1:]), tds))
         
        #prechadzam jednotlive stanice
        for indx, _tv_id in enumerate(tab_tv_id):
            if _tv_id in self.__tv_list:
                _tv_id = _tv_id.extract()
#                 print("TV_ID::", _tv_id)
                tv_id = _tv_id.lower().replace(" ", "_")
                tv_id = unidecode(tv_id)
                # print(tv_id,'=',_tv_id)
                # prechadzam jednotlive tabulky
                info_list = []
                for part, tds in tabs_tds:
                    # ziskam stlpce danej tabulky pre danu stanicu
#                     print("************ {0} *****************".format(part))
                    td = tds[indx]
                    tabs_program = td.xpath('./div/table[@class="porad"]')
                    for tab in tabs_program:
                        yield self.__parse_table(tab, part)

#                         info_list.append(obj.__dict__)
                        
#                 self.__epg_info[tv_id] = info_list
#                  
#         return self.__epg_info

    def __parse_anchor(self, span):
        
        anchs = span.xpath(".//a")
        txt = []
        if anchs:
            for anch in anchs:
                txt.append(anch.xpath('text()').extract() if anch != None else "")
        return txt
                
    def __convert_to_date(self, cas, part):
        cas = cas.xpath('text()').extract()[0]
        cas = cas.split('.')
        cas = self.urls.now.replace(hour=int(cas[0]), minute=int(cas[1]))
        if part == 24:
            cas += timedelta(days=1)
#         cas = pu.time_str(cas)
        return cas
        
    def __convert_end(self, start, end):
        if start > end:
            tmp = start.replace(hour=end.hour, minute=end.minute)
            end = tmp + timedelta(days=1)
        return end
        
        
    def __parse_table(self, table, part):
        obj = PytvinfoItem()
        _time = table.xpath(self.urls.time)[0]
        cas = self.__convert_to_date(_time, part)
        _time = table.xpath('@data-k')[0]
        end = pu.str_time(_time.extract(),"%Y%m%d %H%M")
        end = self.__convert_end(cas, end)
        obj['cas'] = pu.time_str(cas)
        obj['end'] = pu.time_str(end)
        # print(obj.cas + "   " + obj.end)
        spans = table.xpath(self.urls.td_nazov)[0].xpath(".//span")
        info = table.xpath(self.urls.info)
    
        for span in spans:
            clz = span.xpath("@class")
            if clz and 'novy_typprg' in clz[0].extract() :
#                 obj.relacia = span.text.encode('utf-8') if span.text else ""
#                 print(span)
                str = span.xpath('text()').extract()
#                 print("1::", str)
                str = str[0] if len(str) > 0 else ""
#                 print("2::", str)
#                 print(re.match('\>(.*)\<', str))
                rel = str
                obj['relacia'] =  rel if rel else ""
            obj.set_nazov(self.__parse_anchor(span))
        # vypise info o relacii
        obj['popis'] = ""
        if len(info) > 0:
            for inf in info:
                for txt in inf.xpath("descendant::*/text()"): 
                    obj['popis'] += txt.extract().replace("...", "")
#             obj.popis = obj.popis.encode("utf-8")
        return obj
        
        
        
        
        
#         for quote in response.xpath('//div[@class="quote"]'):
#             yield {
#                 'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
#                 'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
#                 'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
#             }
# 
#         next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))

