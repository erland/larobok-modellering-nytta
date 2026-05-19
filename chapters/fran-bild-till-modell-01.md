# Kapitel 1: Från bild till modell

## Varför detta kapitel finns

Många arkitekter börjar sitt arbete i en bild. Det är naturligt. En bild kan snabbt samla en diskussion, visa ett problem och hjälpa människor att se samma sak framför sig. I en större myndighet kan en bra bild ibland vara skillnaden mellan ett otydligt möte och ett möte där deltagarna faktiskt börjar förstå varandra.

Men en bild är inte alltid en modell.

En bild kan vara en tillfällig kommunikationsyta. En modell är en strukturerad representation av något vi vill förstå, analysera, återanvända eller förändra. Skillnaden är inte att modellen måste vara mer komplicerad. Skillnaden är att modellen har en inre struktur som gör att den kan fortsätta skapa nytta efter att mötet är slut.

I Tullmyndigheten Atlantis finns många arkitekturbilder. Det finns systemkartor, processbilder, PowerPoint-bilder, målarkitekturer, färgkodade beroendekartor och ritningar över integrationsflöden. En del är mycket användbara. Andra är svåra att tolka redan några månader efter att de skapades. Några visar samma system med olika namn. Några blandar verksamhetsförmågor, organisation, applikationer och tekniska komponenter i samma ruta. Nästan alla har skapats för ett särskilt möte, ett särskilt initiativ eller en särskild fråga.

Det här kapitlet hjälper dig att se när en bild räcker och när du behöver ta steget till modellering.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara skillnaden mellan en fristående bild, en vy och en modell
- beskriva varför modellering kan ge mer nytta än diagramritande
- känna igen när en arkitekturbild behöver en tydligare modellstruktur
- avgöra när en enkel bild fortfarande är ett bättre val
- formulera den första praktiska regeln för att gå från bild till modell

## Innan vi börjar

Du behöver inte kunna ArchiMate för att förstå detta kapitel. Vi börjar före notation, symboler och detaljerade regler.

Det viktiga i början är att skilja mellan tre saker:

- **Bild:** det som visas för en människa.
- **Vy:** ett urval av modellinnehåll för en viss målgrupp eller fråga.
- **Modell:** den strukturerade representation som ligger bakom en eller flera vyer.

En vanlig fälla är att tro att ArchiMate främst handlar om hur symboler ser ut. Det gör det inte. Symbolerna är bara ytan. Den verkliga poängen är att skapa ett språk där saker betyder något på ett konsekvent sätt och där samband mellan saker kan återanvändas.

## Bilden som mötesverktyg

En bild är ofta det snabbaste sättet att få igång ett samtal. Om en grupp arkitekter, verksamhetsspecialister och chefer ska diskutera ett förändringsinitiativ kan en enkel skiss räcka långt.

Tänk dig att Atlantis planerar att förbättra hanteringen av importdeklarationer. En arkitekt ritar en bild med följande delar:

- företag som lämnar in deklarationer
- ett digitalt inlämningsgränssnitt
- ett ärendehanteringssystem
- en riskanalysfunktion
- handläggare som gör manuell kontroll
- ett beslutsstöd för klarering

Bilden fungerar bra i mötet. Deltagarna pekar på rutorna, upptäcker oklarheter och diskuterar var flaskhalsar uppstår.

Det är inget fel med detta. Tvärtom är det ofta en utmärkt start. Problemet uppstår först när bilden börjar användas som om den vore mer än den är.

Efter mötet kanske någon frågar:

- Vilka verksamhetsförmågor påverkas av ändringen?
- Vilka applikationer stödjer riskanalysen?
- Vilka informationsobjekt används i flera flöden?
- Vilka beroenden finns mellan importflödet och kontrollverksamheten?
- Vilka delar av målarkitekturen påverkar pågående projekt?

Om bilden bara är en fristående ritning måste någon tolka den manuellt. Rutorna kanske inte har entydiga typer. Linjerna kanske betyder olika saker på olika ställen. Samma applikation kanske finns i flera bilder, men med olika namn. Då är bilden fortfarande användbar som minnesstöd, men den är svag som analysunderlag.

## Modellen som gemensam struktur

En modell gör inte automatiskt arbetet bättre. En dålig modell kan vara lika förvirrande som en dålig bild. Men en bra modell ger något som en lös bild sällan ger: gemensam struktur.

I en modell behöver vi ta ställning till vad saker är. Är rutan “Importkontroll” en process, en förmåga, en organisatorisk enhet, en tjänst eller ett system? Svaret spelar roll eftersom olika typer av saker används för olika frågor.

Om “Importkontroll” är en verksamhetsförmåga kan den hjälpa oss att resonera om vad myndigheten behöver kunna göra. Om den är en process kan den hjälpa oss att förstå arbetsflöde och ansvar. Om den är en applikation har vi sannolikt blandat ihop verksamhetens behov med ett tekniskt stöd.

Modellering tvingar oss inte att beskriva allt. Däremot tvingar den oss att vara tydliga med det vi faktiskt beskriver.

Det är här nyttan börjar. När element och relationer har en konsekvent betydelse kan modellen användas på flera sätt:

- som grund för olika vyer
- som gemensamt språk mellan verksamhet och IT
- som stöd för konsekvensanalys
- som underlag för prioritering
- som minne över beslut och antaganden
- som bro mellan nuläge, målbild och förändringsplan

## Vy är inte samma sak som modell

En viktig distinktion är skillnaden mellan vy och modell.

En vy är det någon ser. En modell är det som vyn bygger på.

I ett modelleringsverktyg kan samma modellinnehåll visas på flera sätt. Ledningen kan få en vy som visar förmågor, strategiska mål och större förändringsinitiativ. En lösningsarkitekt kan få en vy som visar applikationstjänster, integrationer och beroenden. En informationssäkerhetsspecialist kan få en vy som visar informationsflöden, zoner och kritiska beroenden.

Om varje vy ritas fristående finns risken att de långsamt glider isär. Om vyerna bygger på samma modell kan de däremot vara olika utan att bli motsägelsefulla.

I Atlantis kan samma applikation, exempelvis ett ärendehanteringssystem för tullklarering, förekomma i flera vyer:

- i en verksamhetsvy som stöd för processen “Handlägga importdeklaration”
- i en applikationsvy som en applikationskomponent med tjänster
- i en förändringsvy som något som påverkas av ett moderniseringsinitiativ
- i en riskvy som beroende för samhällsviktig verksamhet

Poängen är inte att visa allt på en gång. Poängen är att flera vyer kan peka tillbaka på samma modellerade sak.

## Exempel: två bilder som ser lika ut men betyder olika saker

Föreställ dig två arkitekturbilder i Atlantis.

Den första bilden har rubriken “Importflödet”. Den visar företag, deklaration, riskanalys, kontroll och beslut. Linjerna visar ungefärlig ordning i processen.

Den andra bilden har också rubriken “Importflödet”. Den visar företag, e-tjänst, integrationsplattform, ärendehanteringssystem och beslutsstöd. Linjerna visar informationsutbyte mellan applikationer.

Båda bilderna kan vara bra. Men om de saknar tydliga typer kan de lätt blandas ihop. Någon tror att “riskanalys” är en verksamhetsaktivitet. Någon annan tror att det är ett system. En tredje tror att det är en organisatorisk funktion. Diskussionen handlar då inte längre om arkitekturfrågan utan om vad bilden egentligen betyder.

I en modell skulle vi kunna skilja på exempelvis:

- verksamhetsförmågan att bedöma risk
- processen där riskbedömning görs
- informationen som används för riskbedömning
- applikationstjänsten som tillhandahåller riskanalys
- applikationskomponenten som realiserar tjänsten

Vi behöver inte alltid modellera alla dessa saker. Men när begreppen blandas ihop i viktiga beslut är det ett tecken på att en vanlig bild inte längre räcker.

## När bilden räcker

Det vore ett misstag att alltid kräva modellering. Ibland är en bild bättre.

En enkel bild kan räcka när syftet är att:

- utforska en idé i ett tidigt samtal
- förklara något snabbt för en engångspublik
- skapa en workshopskiss som inte ska förvaltas
- visa en förenklad berättelse utan krav på analys
- fånga ett resonemang innan man vet vad som är viktigt

I sådana lägen kan modellering bli för tungt. Om allt måste struktureras direkt kan samtalet tappa fart. En skiss kan vara rätt nivå.

Men det bör vara ett medvetet val. Frågan är inte om bilder är dåliga. Frågan är om bilden förväntas bära mer ansvar än den klarar.

## När modellen behövs

En modell blir mer motiverad när innehållet ska leva längre, återanvändas eller kopplas till beslut.

Du bör överväga modellering när:

- samma företeelser återkommer i flera bilder
- flera målgrupper behöver olika vyer av samma verklighet
- samband och beroenden är viktigare än layouten
- modellen ska användas för konsekvensanalys
- namn, typer och relationer behöver vara konsekventa
- arkitekturunderlaget ska förvaltas över tid
- flera initiativ påverkar samma förmågor, processer eller system
- du behöver kunna svara på frågor som inte syns direkt i en enskild bild

I Atlantis blir detta tydligt när modernisering av importflödet påverkar både verksamhetsprocesser, digitala tjänster, ärendehantering, riskanalys, integrationer, datakällor, säkerhetskrav och samverkan med andra myndigheter. En fristående bild kan visa en berättelse. En modell kan hjälpa till att se hur berättelsen hänger ihop med andra delar av myndigheten.

## Minimal användbar modell

Ett viktigt begrepp i den här boken är **minimal användbar modell**.

En minimal användbar modell är den minsta modell som hjälper oss att besvara en faktisk fråga eller fatta ett bättre beslut. Den är inte minimal för att den är slarvig. Den är minimal för att den avstår från detaljer som inte behövs just nu.

För Atlantis skulle en första minimal modell kunna fokusera på frågan:

> Vilka verksamhetsförmågor och applikationer påverkas av förändringar i importflödet?

Då behöver modellen kanske bara innehålla:

- ett litet antal centrala verksamhetsförmågor
- några viktiga verksamhetsprocesser
- de applikationer som stödjer processerna
- relationer som visar stöd, beroende eller realisering
- en vy för verksamhetsdialog och en vy för IT-dialog

Den behöver inte börja med all teknik, alla integrationer, alla informationsobjekt eller alla möjliga ArchiMate-relationer. Det kan komma senare om nyttan kräver det.

## Från ritvana till modellvana

För arkitekter som är vana att rita bilder kan modellering först kännas långsammare. Det beror ofta på att modellen kräver beslut som bilden tidigare dolde.

När du ritar en ruta kan du låta den betyda lite av varje. När du modellerar behöver du bestämma vad rutan representerar. Det kan kännas som friktion, men friktionen är ofta värdefull. Den visar att organisationen saknar ett gemensamt språk.

Ett bra sätt att börja är inte att införa alla regler på en gång. Börja i stället med tre enkla vanor:

1. Sätt typ på de viktigaste sakerna.
2. Namnge saker konsekvent.
3. Gör relationerna begripliga.

Det räcker långt. Om ni kan skilja mellan förmåga, process, applikation och tjänst har ni redan tagit ett stort steg från bild till modell.

## Vanliga misstag

- **Misstag: Att tro att modellen måste vara komplett från början.**
  - Varför det händer: Man förväxlar modellering med inventering av allt.
  - Hur du undviker det: Börja med en fråga och skapa bara den modell som behövs för att besvara den.

- **Misstag: Att rita ArchiMate-symboler utan modellstruktur.**
  - Varför det händer: Man byter notation men behåller gammal ritlogik.
  - Hur du undviker det: Säkerställ att element, relationer och namn kan återanvändas i flera vyer.

- **Misstag: Att lägga för mycket betydelse i layouten.**
  - Varför det händer: I bilder bär placering, färg och pilar ofta stora delar av budskapet.
  - Hur du undviker det: Låt relationerna bära betydelsen och låt layouten stödja läsbarhet.

- **Misstag: Att använda samma ruta för flera olika saker.**
  - Varför det händer: Vardagsspråk är ofta mer otydligt än modelleringsspråk.
  - Hur du undviker det: Fråga om rutan beskriver en förmåga, process, organisation, applikation, tjänst, information eller teknik.

- **Misstag: Att göra modellen till ett självändamål.**
  - Varför det händer: Modellering kan uppfattas som metodkrav snarare än beslutsstöd.
  - Hur du undviker det: Koppla varje modellinsats till en målgrupp, en fråga och en användning.

## Övningar

### Övning 1: Granska en befintlig arkitekturbild

Välj en arkitekturbild som används i din organisation. Svara på frågorna:

1. Vad är bildens huvudsakliga syfte?
2. Vilka rutor beskriver verksamhet?
3. Vilka rutor beskriver IT-system eller applikationer?
4. Vilka rutor beskriver information, teknik eller organisation?
5. Vad betyder linjerna?
6. Skulle en annan arkitekt tolka bilden på samma sätt?

Avsluta med att markera tre saker i bilden som skulle vinna på att få tydligare typ eller relation.

### Övning 2: Hitta modellfrågan

Utgå från samma bild och formulera en fråga som bilden försöker hjälpa till att besvara.

Exempel:

- Vilka applikationer stödjer importflödet?
- Vilka förmågor påverkas av ett nytt regelkrav?
- Vilka system behöver förändras för att korta handläggningstiden?
- Vilka informationsflöden går mellan Atlantis och andra myndigheter?

Bedöm sedan om bilden räcker för frågan eller om en modell skulle ge mer nytta.

### Övning 3: Skapa en minimal användbar modellidé

Skriv en kort modellidé med fyra delar:

1. Fråga: Vad ska modellen hjälpa oss att förstå?
2. Målgrupp: Vem ska använda vyn?
3. Innehåll: Vilka 3–5 typer av saker behöver modelleras?
4. Avgränsning: Vad ska inte modelleras ännu?

Målet är inte att skapa en färdig ArchiMate-modell. Målet är att träna på att tänka modell före notation.

### Fördjupning

Diskutera i en arkitektgrupp:

- När har en bild i er organisation fungerat riktigt bra?
- När har en bild skapat missförstånd?
- Vilka återkommande begrepp används olika av olika personer?
- Vilken typ av fråga skulle motivera en gemensam modell?

## Snabb sammanfattning

- En bild kan vara ett utmärkt kommunikationsverktyg.
- En modell är en strukturerad representation som kan återanvändas, analyseras och förvaltas.
- En vy är ett urval av modellen för en viss målgrupp eller fråga.
- Modellering behövs när samband, konsekvensanalys, återanvändning och gemensam betydelse är viktigare än en enskild presentation.
- Börja inte med alla ArchiMate-detaljer. Börja med frågan modellen ska hjälpa till att besvara.
- Den första nyttiga modellen är ofta liten, avgränsad och kopplad till ett verkligt beslut.

## Quiz/reflektionsfrågor

1. Vad är den viktigaste skillnaden mellan en bild och en modell?
2. Varför kan två korrekta bilder ändå skapa problem om de inte bygger på samma modell?
3. Vad innebär det att en vy inte är samma sak som modellen?
4. När är det bättre att bara rita en enkel bild?
5. Vilken fråga i din egen organisation skulle kunna motivera en minimal användbar modell?

## Nästa steg

I nästa kapitel går vi från skillnaden mellan bild och modell till den viktigaste startfrågan i all praktisk modellering: vad ska modellen hjälpa oss att förstå?

Där börjar vi formulera modellens syfte innan vi väljer ArchiMate-element, detaljeringsnivå och vyer.
