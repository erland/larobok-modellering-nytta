# Kapitel 13: Att börja dra nytta av modeller

## Varför detta kapitel finns

Efter tolv kapitel är det lätt att förstå modellering som något man gör för att skapa bättre arkitekturbeskrivningar. Men den verkliga nyttan uppstår först när modellerna börjar användas i arbetet: i prioriteringar, konsekvensanalyser, vägval, styrning, dialoger och uppföljning.

Det här kapitlet handlar därför om övergången från att skapa modeller till att dra nytta av dem.

För många arkitekter är detta den svåraste delen. Det går att lära sig symboler, lager, relationer och vyer. Det går också att skapa en snygg modell i ett verktyg. Men om modellen inte används i riktiga samtal och beslut blir den snabbt ännu en arkitekturbild, fast med mer notation.

Tullmyndigheten Atlantis har nu börjat förstå skillnaden mellan bild och modell. Arkitekterna har identifierat ett begränsat utsnitt av importflödet, beskrivit centrala förmågor, kopplat dem till applikationstjänster och visat några viktiga förändringsinitiativ. Frågan är inte längre om de kan modellera. Frågan är hur de ska börja få nytta av modellen i myndighetens vardag.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva vad det innebär att en modell används, inte bara finns,
- välja ett första användningsfall där modellering kan ge tydlig nytta,
- planera en liten men användbar start för modellering i en större myndighet,
- etablera enkla kvalitetskriterier för modellnytta,
- använda modeller i möten, analyser och beslut utan att göra arbetssättet tungt.

## Innan vi börjar

Tidigare kapitel har visat hur man kan välja syfte, avgränsa modellen, använda ArchiMate som språk, välja lager, bygga relationer och skapa vyer för olika målgrupper. Kapitel 12 betonade att man ofta ska börja med en minsta användbar modell.

Nu vänder vi på perspektivet.

I stället för att fråga “hur modellerar vi detta?” frågar vi:

- Var i arbetet kan modellen göra skillnad?
- Vem behöver använda modellen?
- Vilket beslut, vilken analys eller vilket samtal blir bättre av modellen?
- Hur märker vi att modellen faktiskt skapar nytta?

En modell börjar skapa värde när den påverkar hur människor förstår, prioriterar eller agerar.

## Huvudförklaring

### Börja inte med modellbiblioteket

Ett vanligt misstag är att börja ett modelleringsarbete med att försöka bygga ett komplett modellbibliotek. Organisationen skapar mappar, namngivningsregler, lagerstrukturer, modellvyer och kanske även en stor ambition om att “modellera verksamheten”.

Det kan kännas professionellt, men det är ofta en tung start.

För Atlantis skulle ett sådant upplägg kunna innebära att arkitekterna försöker modellera alla förmågor, alla processer, alla applikationer och alla informationsflöden innan någon verksamhetsnytta uppstår. Resultatet blir lätt att modelleringen uppfattas som ett internt arkitekturarbete, inte som ett stöd för myndighetens beslut.

En bättre start är att välja ett konkret användningsfall.

Exempel på första användningsfall kan vara:

- förstå vilka förmågor som påverkas av modernisering av importflödet,
- visa vilka applikationer som stödjer en kritisk verksamhetstjänst,
- jämföra två förändringsinitiativ som påverkar samma applikationslandskap,
- visa beroenden inför migrering från ett äldre system,
- skapa en gemensam bild inför portföljprioritering,
- följa spårbarhet från strategiskt mål till pågående initiativ.

Det viktiga är att användningsfallet är tillräckligt avgränsat för att kunna ge nytta snabbt, men tillräckligt viktigt för att någon ska bry sig om resultatet.

### Formulera nyttan innan modellen byggs

Innan Atlantis börjar modellera bör arkitekterna skriva ned nyttan i enkel form:

> Vi modellerar detta för att hjälpa [målgrupp] att [beslut eller analys] genom att visa [det viktigaste sambandet].

Det kan till exempel bli:

> Vi modellerar importflödets centrala förmågor och applikationsstöd för att hjälpa portföljledningen att prioritera moderniseringsinitiativ genom att visa vilka förändringar som påverkar samma verksamhetsförmågor och system.

Denna mening gör flera saker samtidigt. Den anger målgrupp, användning, avgränsning och förväntad nytta. Den hjälper också arkitekterna att välja bort sådant som inte behövs.

Om modellen inte hjälper portföljledningen att prioritera, har den inte lyckats med sitt syfte, även om den är korrekt ritad.

### Välj en första modellfråga

En modellfråga är den fråga modellen ska hjälpa till att besvara. Den ska vara mer konkret än “hur ser arkitekturen ut?”.

För Atlantis kan en första modellfråga vara:

> Vilka verksamhetsförmågor, applikationstjänster och initiativ behöver förstås tillsammans för att prioritera modernisering av importflödet?

Den frågan pekar på en rimlig startmängd:

- verksamhetsförmågor inom importflödet,
- applikationstjänster som stödjer dessa förmågor,
- centrala applikationer bakom tjänsterna,
- pågående eller planerade initiativ,
- relationer som visar stöd, påverkan och realisering.

Frågan pekar också på vad som inte behöver modelleras från början:

- fullständig organisationsstruktur,
- alla processdetaljer,
- teknisk infrastruktur på låg nivå,
- alla externa parter,
- samtliga databaser och integrationer,
- historiska lösningar som inte påverkar beslutet.

### Gör modellen användbar i ett riktigt möte

Modellen ska inte vänta på att bli färdig innan den används. Den bör tidigt prövas i ett riktigt sammanhang.

För Atlantis kan det vara ett arbetsmöte med arkitekter, portföljansvariga och representanter från importverksamheten. Syftet är inte att godkänna en färdig modell. Syftet är att se om modellen hjälper gruppen att tänka bättre.

Ett sådant möte kan läggas upp så här:

1. Visa först frågan modellen ska hjälpa till att besvara.
2. Visa en enkel vy, inte hela modellen.
3. Be deltagarna kontrollera om de centrala förmågorna verkar rätt.
4. Gå igenom vilka applikationstjänster som stödjer förmågorna.
5. Markera vilka initiativ som påverkar samma delar.
6. Fråga vilka samband som saknas för att kunna fatta bättre beslut.
7. Avsluta med vilka modelländringar som behövs och vilket beslut modellen ska stödja nästa gång.

Det är viktigt att mötet inte blir en notationsexamen. Deltagarna ska inte behöva förstå alla ArchiMate-detaljer. De ska kunna använda vyn för att resonera om verksamhet, IT och förändring.

### Skilj mellan arbetsmodell och beslutsvy

När modellen börjar användas behövs ofta två nivåer:

- arbetsmodellen där arkitekterna håller struktur, element, relationer och spårbarhet,
- beslutsvyn där en målgrupp ser det utsnitt som behövs för ett visst samtal.

Arbetsmodellen kan innehålla mer ArchiMate-semantik. Den kan visa relationer och elementtyper som är viktiga för kvalitet och återanvändning. Beslutsvyn ska däremot vara begriplig för sin målgrupp.

För Atlantis kan arbetsmodellen innehålla förmågor, applikationstjänster, applikationer, initiativ och realiseringsrelationer. En vy för portföljledningen kan visa samma innehåll mer förenklat:

- vilka förmågor som påverkas,
- vilka applikationer som är centrala,
- vilka initiativ som överlappar,
- vilka beroenden som bör hanteras innan beslut.

Detta är en av de viktigaste poängerna med modellering: olika vyer kan bygga på samma modell. När något ändras i modellen kan flera vyer hållas samman.

### Bygg modellvana genom upprepning

En organisation börjar inte dra nytta av modeller genom ett stort införandeprogram. Den börjar ofta dra nytta genom återkommande användning i små men viktiga situationer.

Atlantis kan till exempel använda modellen i tre återkommande sammanhang:

- vid portföljberedning,
- vid konsekvensanalys av förändringsförslag,
- vid arkitekturdialoger mellan verksamhet och IT.

Varje gång modellen används lär sig organisationen något:

- vilka begrepp som behöver vara tydligare,
- vilka relationer som saknas,
- vilka vyer som fungerar,
- vilken detaljnivå som är lagom,
- vilka frågor modellen faktiskt hjälper till att besvara.

Modellering blir då inte en separat aktivitet. Den blir ett stöd i arbetet.

### Gör nyttan synlig

Om modellering ska överleva i en större organisation måste nyttan kunna beskrivas. Annars riskerar den att uppfattas som extra dokumentation.

Nyttan behöver inte alltid mätas med hårda siffror. I början kan den beskrivas genom konkreta observationer:

- Ett beroende upptäcktes innan beslut fattades.
- Två initiativ visade sig påverka samma applikation.
- En verksamhetsförmåga saknade tydligt applikationsstöd.
- En ledningsgrupp kunde diskutera mål, förmågor och initiativ i samma vy.
- En konsekvensanalys gick snabbare eftersom modellen redan innehöll centrala samband.
- En projektbild kunde ersättas med en vy från en återanvändbar modell.

För Atlantis kan en första nyttoberättelse vara:

> När importflödet modellerades upptäcktes att två separata moderniseringsinitiativ påverkade samma applikationstjänst för riskbedömning. Genom modellen kunde portföljledningen samordna initiativen innan de skapade motstridiga förändringsplaner.

Det är en konkret nytta. Den visar varför modellen var mer värd än en fristående bild.

### Sätt enkla kvalitetskriterier

För att börja dra nytta av modeller behövs inte ett stort regelverk. Däremot behövs några enkla kvalitetskriterier.

En startuppsättning för Atlantis kan vara:

- Varje modell ska ha ett uttalat syfte.
- Varje vy ska ha en tydlig målgrupp.
- Centrala element ska ha stabila namn.
- Relationer ska bara användas när de betyder något.
- Modellen ska kunna förklaras utan att börja med verktyget.
- Modellen ska stödja minst ett verkligt samtal, beslut eller analys.
- Det ska vara tydligt vad som är medvetet utelämnat.

Det sista kriteriet är särskilt viktigt. En modell behöver inte vara komplett, men användaren ska förstå dess avgränsning.

### Inför modellering som ett arbetssätt, inte som ett projekt

Om Atlantis behandlar modellering som ett tidsbegränsat projekt finns risken att modellerna blir föråldrade direkt efter leverans. För att nyttan ska fortsätta behöver modellering bli en del av arbetssättet.

Det betyder inte att alla ska modellera allt. Det betyder att vissa återkommande frågor hanteras med stöd av modeller.

Exempel:

- När ett nytt initiativ föreslås: vilka förmågor, applikationer och beroenden påverkas?
- När en applikation ska avvecklas: vilka verksamhetstjänster och processer påverkas?
- När ett strategiskt mål beslutas: vilka förändringar krävs i förmågor och applikationsstöd?
- När två projekt överlappar: vilken del av modellen visar överlappet?
- När en målarkitektur presenteras: vilka delar av nuläget och övergången kan spåras?

På så sätt blir modellen en arbetsyta för arkitekturtänkande, inte ett arkiv.

## Exempel: Atlantis börjar använda modellen

Atlantis har under flera år haft många bilder över importflödet. Några visar processer. Andra visar system. Några visar målbilden för digitalisering. De används i olika presentationer, men de hänger inte ihop.

Arkitekturfunktionen väljer därför ett första användningsfall:

> Stödja portföljledningen inför beslut om vilka moderniseringsinitiativ inom importflödet som ska prioriteras kommande år.

De väljer att börja med en minsta användbar modell. Den innehåller:

- fem verksamhetsförmågor inom importflödet,
- tre centrala verksamhetstjänster,
- sex applikationstjänster,
- fyra centrala applikationer,
- tre förändringsinitiativ,
- relationer som visar stöd, realisering och påverkan.

De skapar tre vyer:

- en verksamhetsvy för att diskutera vilka förmågor som påverkas,
- en applikationsvy för att visa vilka applikationer som stödjer importflödet,
- en portföljvy för att visa hur initiativen överlappar.

Vid första mötet märker de att modellen inte är komplett. Men den gör något viktigt: den visar att initiativet för automatiserad riskbedömning och initiativet för moderniserad ärendehantering båda är beroende av samma applikationstjänst för importdata.

Det leder till en konkret diskussion om samordning, ansvar och tidsplan. Modellen har börjat göra nytta.

Efter mötet uppdaterar arkitekterna modellen. De lägger inte till allt som efterfrågades. De lägger bara till de samband som krävs för nästa portföljbeslut. Därmed växer modellen genom användning, inte genom ambitionen att bli komplett.

## Vanliga misstag

- **Misstag: Att vänta tills modellen är färdig innan den används.**
  - Varför det händer: Arkitekter vill ofta visa något korrekt och komplett.
  - Hur du undviker det: Använd modellen tidigt i ett avgränsat möte och var tydlig med vad som är utkast.

- **Misstag: Att börja med verktyg, mappar och modellregler.**
  - Varför det händer: Det känns ordnat och professionellt.
  - Hur du undviker det: Börja med ett konkret användningsfall och skapa bara de regler som behövs för att stödja det.

- **Misstag: Att visa arbetsmodellen för fel målgrupp.**
  - Varför det händer: Arbetsmodellen är det arkitekterna själva ser.
  - Hur du undviker det: Skapa målgruppsanpassade vyer som bygger på modellen men inte visar allt.

- **Misstag: Att mäta modellering i antal skapade modeller.**
  - Varför det händer: Det är lättare att räkna artefakter än nytta.
  - Hur du undviker det: Följ upp vilka samtal, analyser eller beslut modellen faktiskt har stött.

- **Misstag: Att göra modellering till en separat arkitekturrutin.**
  - Varför det händer: Modellering införs ofta av arkitekturfunktionen.
  - Hur du undviker det: Koppla modellen till befintliga forum som portföljberedning, förändringsanalys och arkitekturdialoger.

## Övningar

### Övning 1: Formulera första nyttan

Välj ett område i din egen organisation där arkitekturbilder ofta används. Skriv en mening enligt mallen:

> Vi modellerar detta för att hjälpa [målgrupp] att [beslut eller analys] genom att visa [det viktigaste sambandet].

Kontrollera sedan om meningen gör det möjligt att välja bort något.

### Övning 2: Välj ett första användningsfall

Välj ett möjligt första användningsfall för modellering:

- portföljprioritering,
- konsekvensanalys,
- systemavveckling,
- målarkitektur,
- förändringsplanering,
- samverkan mellan verksamhet och IT.

Beskriv vilka tre till fem elementtyper som sannolikt räcker för en första minsta användbar modell.

### Övning 3: Planera ett modellmöte

Planera ett möte där en modell ska användas, inte bara visas. Besvara:

1. Vilken fråga ska mötet besvara?
2. Vilken vy ska visas först?
3. Vilka deltagare behöver kunna förstå vyn?
4. Vilka beslut eller insikter ska mötet kunna leda till?
5. Vad ska uppdateras i modellen efter mötet?

### Fördjupning

Ta en befintlig arkitekturbild från ett projekt eller en presentation. Bedöm om den skulle kunna bli en vy från en modell.

Fråga:

- Vilka saker i bilden skulle behöva bli återanvändbara element?
- Vilka samband skulle behöva bli relationer?
- Vilka namn skulle behöva standardiseras?
- Vilka delar är bara presentation och behöver inte in i modellen?
- Vilken nytta skulle modellen ge jämfört med bilden?

## En 30-60-90-dagarsplan för Atlantis

Ett införande behöver vara tillräckligt litet för att gå att genomföra, men tillräckligt verkligt för att skapa nytta. Här är en möjlig startplan.

### Första 30 dagarna: välj fråga och minsta modell

Under den första månaden väljer Atlantis ett konkret beslutsområde, till exempel modernisering av importflödet. Arkitektgruppen formulerar tre frågor som modellen ska kunna hjälpa till att besvara:

- Vilka förmågor och processer påverkas?
- Vilka applikationer och informationsobjekt är centrala?
- Vilka pågående initiativ påverkar samma område?

Gruppen väljer också ett litet gemensamt begreppsset: förmåga, process, verksamhetstjänst, applikationskomponent, applikationstjänst, informationsobjekt, mål, krav och arbetspaket.

### Dag 31-60: skapa återanvändbara vyer

Under nästa period skapas två till fyra vyer ur samma modell. En vy riktas till ledning, en till verksamhet, en till IT-arkitekter och en till portföljstyrning. Varje vy ska ha en namngiven målgrupp och en tydlig fråga.

Målet är inte att modellen ska vara komplett. Målet är att visa att samma modell kan ge flera begripliga utsnitt utan att informationen behöver ritas om från början.

### Dag 61-90: använd modellen i riktiga beslut

Under den tredje perioden används modellen i minst två faktiska möten: ett prioriteringsmöte och ett arkitektur- eller förändringsmöte. Efter varje möte dokumenteras vad modellen hjälpte till med och vad som saknades.

Exempel på utvärderingsfrågor:

- Vilka frågor kunde besvaras snabbare än tidigare?
- Vilka oklarheter blev synliga?
- Vilka begrepp användes inkonsekvent?
- Vilka delar av modellen ska förvaltas vidare?
- Vilka delar kan tas bort?

Efter 90 dagar bör Atlantis inte ha en komplett myndighetsmodell. Däremot bör myndigheten ha ett bevis på att modellering kan skapa bättre samtal, tydligare beroenden och mer återanvändbara beslutsunderlag.

## Snabb sammanfattning

- Modeller skapar nytta först när de används i verkliga samtal, analyser och beslut.
- Börja med ett konkret användningsfall, inte med ett komplett modellbibliotek.
- Formulera modellnyttan innan modellen byggs.
- Använd en modellfråga för att styra avgränsning, element, relationer och vyer.
- Skilj mellan arbetsmodell och beslutsvy.
- Låt modellen växa genom användning, inte genom ambitionen att täcka allt.
- Gör nyttan synlig genom konkreta exempel på bättre beslut, upptäckta beroenden eller snabbare analys.
- En liten modell som används är mer värdefull än en stor modell som ingen litar på eller återkommer till.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan att ha en modell och att använda en modell?
2. Varför är ett konkret användningsfall ofta en bättre start än ett komplett modellbibliotek?
3. Hur kan en modellfråga hjälpa dig att välja bort detaljer?
4. Varför behöver man skilja mellan arbetsmodell och beslutsvy?
5. Vilka tecken visar att en modell börjar skapa nytta?
6. Hur kan modellering kopplas till befintliga forum i stället för att bli en separat aktivitet?

## Nästa steg

Nästa kapitel avslutar boken genom att behandla modellering som arbetssätt. Där flyttas fokus från det första nyttoskapande användningsfallet till långsiktig förvaltning, ansvar, governance, kultur och balans mellan frihet och disciplin.
