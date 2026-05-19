# Kapitel 5: Verksamhetslagret: när det är rätt startpunkt

## Varför detta kapitel finns

Många arkitekturbilder börjar med system. Det är förståeligt. Systemen är synliga i projekt, budgetar, driftmiljöer och incidenter. Men i en större myndighet leder en systemstart ofta till att samtalet fastnar i lösningar innan man har förstått vad myndigheten faktiskt behöver kunna göra.

Verksamhetslagret i ArchiMate hjälper oss att beskriva verksamheten innan vi låser diskussionen vid applikationer, tekniska lösningar eller organisationsrutor. Det betyder inte att allt alltid ska börja i verksamhetslagret. Det betyder att verksamhetslagret ofta är rätt startpunkt när frågan handlar om uppdrag, förmågor, processer, tjänster, ansvar eller förändringens nytta.

I Tullmyndigheten Atlantis har flera moderniseringsinitiativ börjat som systemfrågor:

- “Vi behöver ersätta importsystemet.”
- “Vi behöver ett nytt gränssnitt mot transportörer.”
- “Vi behöver bättre analysstöd.”
- “Vi behöver effektivare handläggning.”

Alla dessa påståenden kan vara rimliga. Men de är ännu inte tillräckligt tydliga som arkitekturfrågor. Innan Atlantis kan avgöra vad som ska förändras behöver myndigheten förstå vilka verksamhetsförmågor, processer, roller och tjänster som påverkas.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara när verksamhetslagret är en bra startpunkt för modellering,
- skilja mellan förmåga, process, verksamhetstjänst, roll och aktör på en praktisk nivå,
- välja en liten användbar startmängd för verksamhetsmodellering,
- avgöra när verksamhetslagret blir för detaljerat,
- formulera enkla verksamhetsvyer som kan kopplas vidare till applikationer och förändringsinitiativ.

## Innan vi börjar

I tidigare kapitel har vi skiljt mellan bild, vy och modell. Vi har också betonat att modellering bör börja med en fråga. Verksamhetslagret är inte ett självändamål. Det är ett sätt att strukturera vissa typer av frågor.

En enkel tumregel är:

> Börja i verksamhetslagret när diskussionen handlar om vad myndigheten behöver kunna göra, inte vilket system som råkar göra det idag.

Det är särskilt viktigt i en myndighet där uppdrag, rättssäkerhet, lagkrav, samverkan och långlivade verksamhetsförmågor ofta är mer stabila än enskilda IT-system.

## Vad verksamhetslagret hjälper oss med

Verksamhetslagret hjälper oss att beskriva verksamheten som verksamhet. Det kan låta självklart, men i praktiken blandas ofta flera saker ihop i samma bild:

- organisatoriska enheter,
- arbetsuppgifter,
- processflöden,
- system,
- informationsobjekt,
- projekt,
- mål,
- tekniska integrationer.

När allt detta visas samtidigt kan bilden bli kommunikativ i ett möte, men svår att återanvända som modell. Verksamhetslagret hjälper oss att börja sortera.

För Tullmyndigheten Atlantis kan verksamhetslagret till exempel hjälpa till att svara på frågor som:

- Vilka förmågor behövs för att hantera import från föranmälan till beslut?
- Vilka verksamhetstjänster erbjuder Atlantis till företag, privatpersoner och andra myndigheter?
- Vilka roller deltar i riskbedömning, kontrollurval och beslut?
- Vilka processer är centrala för rättssäker och effektiv tullklarering?
- Var finns beroenden mellan importflödet och andra delar av myndighetens uppdrag?

Det viktiga är inte att alla dessa frågor måste modelleras samtidigt. Det viktiga är att ArchiMate ger oss begrepp som gör det möjligt att skilja dem åt.

## Centrala begrepp i verksamhetslagret

I det här kapitlet behöver vi inte hela verksamhetslagret. Vi börjar med en liten startmängd.

### Förmåga

En förmåga beskriver vad en organisation behöver kunna göra för att uppfylla sitt uppdrag. En förmåga är inte samma sak som en process, en avdelning eller ett system.

Exempel i Atlantis:

- ta emot importuppgifter,
- bedöma risk,
- fatta tullbeslut,
- genomföra kontroll,
- kommunicera beslut,
- följa upp regelefterlevnad.

Förmågor är ofta användbara i dialog med ledning och portföljstyrning eftersom de är relativt stabila. Ett system kan bytas ut, en process kan förbättras och en organisatorisk enhet kan förändras, men behovet av att bedöma risk finns kvar.

### Verksamhetsprocess

En verksamhetsprocess beskriver ett flöde av arbete eller beteende. Där förmågan säger vad myndigheten behöver kunna göra, beskriver processen hur arbete utförs i ett visst sammanhang.

Exempel i Atlantis:

- hantera föranmälan,
- genomföra riskurval,
- handlägga importdeklaration,
- besluta om kontroll,
- avsluta ärende.

Processer är användbara när frågan handlar om flöde, ansvar, väntetider, överlämningar eller förbättringar i arbetssättet.

### Verksamhetstjänst

En verksamhetstjänst beskriver vad verksamheten tillhandahåller till en mottagare. Den kan vara riktad till externa aktörer, andra myndigheter, interna delar av organisationen eller samverkansparter.

Exempel i Atlantis:

- importklarering,
- tullinformation till företag,
- riskbaserat kontrollurval,
- utlämning av tullstatus till samverkande myndighet.

Verksamhetstjänster är användbara när man vill beskriva myndighetens erbjudande, gränssnitt mot omvärlden eller vad en mottagare faktiskt får nytta av.

### Roll och aktör

En aktör är en person, organisation eller organisatorisk enhet som utför något. En roll beskriver vilket ansvar eller vilken funktion aktören har i ett visst sammanhang.

Exempel i Atlantis:

- aktör: Importavdelningen,
- roll: tullhandläggare,
- roll: kontrollsamordnare,
- extern aktör: transportör,
- extern aktör: importör,
- samverkansaktör: annan myndighet.

Skillnaden mellan aktör och roll är praktiskt viktig. Samma organisatoriska enhet kan bära flera roller, och samma roll kan ibland utföras av olika enheter eller typer av användare.

## När verksamhetslagret är rätt startpunkt

Verksamhetslagret är ofta rätt startpunkt när modellen ska stödja en fråga där systemnamn riskerar att skymma verksamhetsbehovet.

### När initiativet drivs av verksamhetsnytta

Om Atlantis vill minska handläggningstid i importflödet räcker det inte att börja med systemkartan. Frågan handlar först om vilka delar av verksamhetsflödet som skapar väntan, dubbelarbete eller otydligt ansvar.

En första modell kan då visa:

- berörda förmågor,
- centrala processer,
- roller som deltar,
- verksamhetstjänster som påverkas.

Först därefter blir det meningsfullt att koppla på applikationer.

### När flera system stödjer samma verksamhetsområde

I större myndigheter är det vanligt att samma verksamhetsförmåga stöds av flera applikationer. Om Atlantis har ett äldre ärendehanteringssystem, ett separat riskanalysstöd och flera lokala rapporteringslösningar kan en ren systembild visa många rutor men ändå inte svara på vad de tillsammans stödjer.

Genom att börja med förmågor och processer kan modellen visa varför systemen finns och var överlapp, luckor eller beroenden uppstår.

### När ansvar och målgrupper är oklara

Verksamhetslagret är också användbart när diskussionen handlar om vem som gör vad. Men här behöver man vara försiktig. Syftet är inte att rita en organisationskarta om frågan egentligen handlar om ansvar i ett flöde.

I Atlantis kan frågan vara:

> Vem ansvarar för att riskbedömningen är tillräcklig innan en importdeklaration går vidare till beslut?

Då kan roller och processer vara viktigare än organisationsenheter.

### När man behöver prata med verksamheten

En modell som börjar med tekniska komponenter kan vara svår att använda i samtal med verksamhetens experter. En verksamhetsvy med förmågor, processer och tjänster kan däremot skapa ett gemensamt samtal utan att modellen reduceras till en enkel presentation.

Det betyder inte att verksamheten behöver lära sig all ArchiMate-notation. En kommunikationsvy kan vara förenklad men ändå bygga på en strukturerad modell.

## När verksamhetslagret inte är rätt startpunkt

Verksamhetslagret är kraftfullt, men det är inte alltid rätt första steg.

### När frågan är tydligt teknisk

Om Atlantis behöver förstå kapacitetsrisker i en integrationsplattform, redundans i driftmiljön eller tekniska beroenden vid en migrering kan teknik- eller applikationslagret vara en bättre start. Verksamhetslagret kan fortfarande behövas senare för att visa konsekvenser, men det behöver inte vara första modellen.

### När verksamhetsbilden redan är tillräckligt stabil

Ibland finns redan en välförankrad beskrivning av verksamheten. Då kan det vara mer effektivt att börja där osäkerheten finns. Om alla är överens om importprocessens huvudsteg men oense om applikationsberoenden, är det rimligt att börja med applikationslagret och koppla tillbaka till verksamheten när det behövs.

### När modellen riskerar att bli en processkartläggning utan arkitekturfråga

Det är lätt att verksamhetsmodellering glider över i mycket detaljerad processdokumentation. Det kan vara värdefullt i rätt sammanhang, men det är inte alltid arkitekturmodellering.

En varningssignal är när modellen börjar beskriva varje handläggningssteg, varje undantag och varje lokal rutin utan att detta kopplas till en arkitekturfråga. Då bör man gå tillbaka till modelleringsfrågan:

> Vilket beslut eller vilken förståelse ska modellen stödja?

## En minimal startmängd för verksamhetsmodellering

För Atlantis räcker det ofta att börja med fem typer av saker:

- förmåga,
- verksamhetsprocess,
- verksamhetstjänst,
- verksamhetsroll,
- aktör.

Till detta behövs ett fåtal relationer, till exempel att en roll deltar i en process, att en process realiserar en tjänst, eller att en förmåga stöds av processer och senare av applikationer.

Startmängden ska vara liten nog att användas konsekvent. Den ska också vara tydlig nog för att skilja mellan frågor som annars blandas ihop.

En enkel arbetsordning kan vara:

1. Formulera modelleringsfrågan.
2. Identifiera de viktigaste förmågorna.
3. Välj en eller två processer som visar hur förmågorna används.
4. Lägg till roller och aktörer bara där ansvar eller samverkan är relevant.
5. Beskriv verksamhetstjänster om frågan handlar om vad som levereras till en mottagare.
6. Vänta med applikationer tills verksamhetsstrukturen är tillräckligt tydlig.

Det här är inte en regel för alla modeller. Det är en trygg startpunkt när verksamhetslagret är nytt för organisationen.

## Atlantis-exempel: importflödet

Atlantis ska modernisera delar av importflödet. Flera projektförslag finns redan:

- ersätta ett äldre importsystem,
- införa bättre digital kommunikation med transportörer,
- förbättra riskanalys,
- automatisera delar av handläggningen,
- skapa bättre uppföljning av beslut och kontroller.

Om arkitekterna börjar med en systembild riskerar diskussionen att handla om vilka system som ska ersättas. Men ledningen behöver först förstå vilka verksamhetsförmågor som påverkas.

En första verksamhetsmodell kan därför börja så här:

| Modellfråga | Verksamhetsdel att börja med | Varför |
|---|---|---|
| Vad behöver Atlantis kunna göra bättre? | Förmågor | Ger stabil struktur för prioritering. |
| Var uppstår väntan och överlämningar? | Processer | Visar flöde och ansvar. |
| Vad får importören eller transportören från myndigheten? | Verksamhetstjänster | Gör nyttan begriplig utifrån mottagaren. |
| Vilka deltar i arbetet? | Roller och aktörer | Synliggör ansvar och samverkan. |
| Vilka system behöver senare kopplas in? | Applikationer, men först efter verksamhetsstrukturen | Hindrar att systemkartan styr frågan för tidigt. |

En möjlig första vy kan visa att förmågan “bedöma risk” används i flera processer: föranmälan, riskurval, kontrollbeslut och uppföljning. Den kan också visa att riskbedömningen inte bara är ett analysverktyg utan en verksamhetsförmåga som kräver information, regelverk, kompetens, processer och applikationsstöd.

Det är här modellnyttan börjar synas. Atlantis kan diskutera modernisering utifrån förmågor och verksamhetsnytta, inte bara utifrån systemlivscykel.

## Vad man kan välja bort

När man börjar med verksamhetslagret är det vanligt att vilja modellera för mycket. Det kan snabbt göra modellen svår att använda.

### Välj bort fullständig processdetalj

Om syftet är arkitekturanalys behöver du sällan alla steg i en process. Börja med huvudsteg och de överlämningar som spelar roll för frågan.

För Atlantis kan det räcka att visa:

- ta emot uppgifter,
- bedöma risk,
- fatta beslut,
- genomföra kontroll,
- avsluta ärende.

Lokala variationer och undantag kan dokumenteras senare om de påverkar arkitekturbeslutet.

### Välj bort organisationsdetalj om ansvar inte är frågan

Det kan vara frestande att modellera varje avdelning, enhet och grupp. Gör det bara när organisationsstrukturen påverkar frågan.

Om modellen handlar om förmågor är det ofta bättre att börja med vad myndigheten behöver kunna göra. Organisationen kan kopplas på när ansvar, bemanning eller governance blir relevant.

### Välj bort alla relationstyper som inte behövs

ArchiMate erbjuder många sätt att uttrycka samband. En erfaren modellerare kan använda dem nyanserat, men en organisation som börjar modellera behöver konsekvens mer än full uttryckskraft.

Börja med ett fåtal relationstyper och använd dem stabilt. Lägg till fler när behovet uppstår.

### Välj bort absolut täckning

En modell över Atlantis importflöde behöver inte beskriva hela myndigheten. Den behöver beskriva det som krävs för att svara på den aktuella frågan. Att modellera hela verksamheten innan någon nytta uppstår är ett vanligt sätt att tappa energi och förtroende.

## Vanliga misstag

- **Misstag: Att börja med organisationskartan.**
  - Varför det händer: Organisationen är synlig och politiskt viktig.
  - Hur du undviker det: Börja med förmågor eller processer om frågan handlar om vad myndigheten behöver kunna göra.

- **Misstag: Att beskriva processer på för låg nivå.**
  - Varför det händer: Verksamhetsexperter känner till många detaljer och undantag.
  - Hur du undviker det: Modellera bara detaljer som påverkar analysen, beslutet eller kommunikationen.

- **Misstag: Att blanda förmåga, process och system i samma ruta.**
  - Varför det händer: I vardagligt språk används systemnamn ofta som namn på arbete.
  - Hur du undviker det: Fråga om rutan beskriver vad myndigheten kan göra, hur arbetet går till eller vilket applikationsstöd som används.

- **Misstag: Att tro att verksamhetslagret bara är för verksamhetsarkitekter.**
  - Varför det händer: Lagret uppfattas som mindre tekniskt.
  - Hur du undviker det: Använd verksamhetslagret som brygga mellan uppdrag, processer, applikationer och förändringsinitiativ.

- **Misstag: Att modellera verksamheten utan mottagare.**
  - Varför det händer: Modellen blir intern och speglar organisationens eget språk.
  - Hur du undviker det: Lägg till verksamhetstjänster när frågan handlar om vad myndigheten levererar till företag, medborgare eller andra myndigheter.

## Övningar

### Övning 1: Hitta rätt startpunkt

Välj ett aktuellt eller fiktivt initiativ i din organisation. Skriv en mening som beskriver initiativet som en systemfråga. Skriv sedan om den som en verksamhetsfråga.

Exempel:

- Systemfråga: “Vi behöver ersätta importsystemet.”
- Verksamhetsfråga: “Vilka förmågor i importflödet behöver förbättras, och vilka applikationer stödjer dem idag?”

Reflektera över hur samtalet förändras när frågan formuleras om.

### Övning 2: Skapa en liten förmågekarta

Utgå från Atlantis importflöde eller ett eget verksamhetsområde. Lista fem till sju förmågor. Kontrollera sedan varje förmåga med frågan:

> Är detta något organisationen behöver kunna göra, eller är det egentligen en process, en organisatorisk enhet eller ett system?

Justera listan tills den känns stabil.

### Övning 3: Välj vad som ska lämnas utanför

Ta en verksamhetsprocess som du känner till. Skriv tre saker som du medvetet inte skulle modellera i en första arkitekturmodell.

Exempel:

- lokala undantagsrutiner,
- detaljerade handläggningssteg,
- interna gruppnamn,
- tekniska integrationer,
- historiska varianter.

Motivera varför de kan vänta.

### Fördjupning

Skapa två vyer utifrån samma tänkta modell:

1. En kommunikationsvy för en verksamhetschef.
2. En arbetsvy för arkitekter.

Båda vyerna ska bygga på samma verksamhetsbegrepp, men de behöver inte visa samma detaljer. Jämför vad du väljer att visa och dölja.

## Små modellpåståenden i verksamhetslagret

Ett praktiskt sätt att börja är att skriva modellens innehåll som korta påståenden innan man ritar vyer. Då blir det tydligare om man verkligen modellerar samband eller bara placerar symboler bredvid varandra.

Exempel från Atlantis:

- Förmågan **Hantera importdeklaration** stödjer målet **Snabbare och mer rättssäker importklarering**.
- Processen **Granska importärende** realiserar delar av förmågan **Kontrollera varuflöden**.
- Rollen **Tullhandläggare** utför processen **Besluta i importärende**.
- Verksamhetstjänsten **Importklarering** används av externa aktörer som deklaranter, ombud och transportörer.

Sådana påståenden hjälper arkitekten att se om modellen svarar på rätt fråga. Om frågan handlar om ansvar, bör roller och aktörer finnas med. Om frågan handlar om vad myndigheten måste kunna göra, är förmågor viktigare än detaljerade processsteg.

## Snabb sammanfattning

- Verksamhetslagret är ofta rätt startpunkt när frågan handlar om uppdrag, nytta, förmågor, processer, tjänster eller ansvar.
- Börja inte med alla ArchiMate-element. Använd en liten startmängd som går att använda konsekvent.
- Förmågor beskriver vad myndigheten behöver kunna göra.
- Processer beskriver hur arbete utförs i ett visst sammanhang.
- Verksamhetstjänster beskriver vad verksamheten tillhandahåller till en mottagare.
- Roller och aktörer hjälper till att beskriva ansvar och deltagande.
- Välj bort detaljer som inte stödjer modelleringsfrågan.
- Modellera verksamheten för att skapa nytta, inte för att dokumentera allt.

## Quiz/reflektionsfrågor

1. När är verksamhetslagret en bättre startpunkt än applikationslagret?
2. Vad är skillnaden mellan en förmåga och en process?
3. Varför kan det vara skadligt att börja med systemnamn när man diskuterar verksamhetsförändring?
4. När bör man lägga till verksamhetstjänster i modellen?
5. Vilka verksamhetsdetaljer kan du ofta välja bort i en första modell?
6. Hur kan verksamhetslagret hjälpa till att skapa bättre beslutsunderlag i en myndighet?

## Nästa steg

När verksamhetslagret ger en begriplig bild av vad myndigheten behöver kunna göra blir nästa fråga vilket applikationsstöd som möjliggör, begränsar eller försvårar detta. Nästa kapitel handlar därför om applikationslagret: hur man går från en systemkarta till en modell som visar tjänster, ansvar, beroenden och förändringspåverkan.
