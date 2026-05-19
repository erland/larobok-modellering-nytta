# Kapitel 11: Vyer för olika målgrupper

## Varför detta kapitel finns

En arkitekturmodell blir sällan användbar genom att alla får se allt. Tvärtom blir modellen ofta svår att använda när varje målgrupp möts av samma kompletta vy över verksamhet, applikationer, teknik, mål, initiativ och relationer.

Det är här vyer blir viktiga. En vy är inte bara en bild. En vy är ett urval ur modellen, anpassat för en viss fråga, en viss målgrupp och ett visst sammanhang. Den kan vara enkel, men den bör bygga på modellens gemensamma struktur. Då kan samma underliggande modell ge olika presentationer utan att arkitekterna behöver rita om allt från början.

För Tullmyndigheten Atlantis kan samma modell behöva stödja flera samtal. Ledningen vill förstå vilka förmågor som påverkas av en ny strategi. Verksamheten vill förstå hur importflödet hänger ihop med roller, regler och information. IT vill förstå vilka applikationer som stödjer vilka tjänster. Säkerhetsfunktionen vill förstå kritiska beroenden, integrationspunkter och informationsflöden. Portföljstyrningen vill förstå vilka initiativ som bidrar till vilka mål.

Om alla dessa grupper får samma diagram blir resultatet ofta antingen för detaljerat eller för förenklat. Poängen med vyer är att kunna visa rätt del av modellen vid rätt tillfälle.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara skillnaden mellan modell, vy och diagram,
- välja vy utifrån målgrupp, fråga och beslutssituation,
- skapa enklare vyer för ledning, verksamhet, IT, säkerhet och portföljstyrning,
- avgöra när en vy bör vara kommunikativ, analyserande eller styrande,
- undvika vanliga misstag där vyer blir fristående bilder utan koppling till modellen.

## Innan vi börjar

Tidigare kapitel har byggt upp skillnaden mellan bild och modell, mellan syfte och notation samt mellan element och relationer. Det här kapitlet binder ihop detta i den praktiska situation där arkitekten ska kommunicera med andra.

En modell kan innehålla många element och relationer. En vy visar ett urval. Ett diagram är den konkreta visuella presentationen av vyn. I vardagligt tal blandas orden ofta ihop, men för modellnytta är skillnaden viktig.

- **Modellen** är den underliggande strukturen.
- **Vyn** är ett medvetet urval ur modellen.
- **Diagrammet** är hur vyn visas för människor.

En arkitekt som bara ritar diagram kan behöva skapa nya bilder för varje möte. En arkitekt som bygger modeller kan återanvända samma modellinnehåll i flera vyer.

## Huvudförklaring

### Börja med målgruppen

En bra vy börjar inte med frågan: “Vilka ArchiMate-element ska jag visa?” Den börjar med frågan: “Vem ska använda vyn, och till vad?”

Målgruppen avgör vad som ska lyftas fram, vad som ska döljas och vilken detaljnivå som är rimlig. En ledningsgrupp behöver sällan se varje applikationsgränssnitt. En integrationsarkitekt behöver däremot ofta förstå just gränssnitt, informationsflöden och beroenden. En verksamhetschef kan behöva se vilka processer och förmågor som påverkas, men inte vilka tekniknoder som används i driftmiljön.

Det betyder inte att varje målgrupp ska få en egen sanning. Tvärtom. Poängen är att olika målgrupper ska kunna se olika delar av samma sammanhängande modell.

För Atlantis kan en modell över modernisering av importflödet ge flera vyer:

- en ledningsvy över mål, förmågor och större förändringsinitiativ,
- en verksamhetsvy över importprocessen, roller och verksamhetstjänster,
- en applikationsvy över system, applikationstjänster och informationsutbyte,
- en säkerhetsvy över känslig information, beroenden och zoner,
- en portföljvy över initiativ, leveranser och målarkitektur.

Samma modellinnehåll kan alltså användas i olika samtal.

### Börja med frågan

En vy bör kunna kopplas till en fråga. Om vyn inte hjälper någon att svara på en fråga finns risken att den bara blir dekorativ.

Exempel på frågor:

- Vilka verksamhetsförmågor påverkas av ett visst initiativ?
- Vilka applikationer stödjer en viss verksamhetstjänst?
- Var uppstår kritiska beroenden i importflödet?
- Vilka mål bidrar ett förändringsinitiativ till?
- Vilka informationsflöden behöver särskild säkerhetsbedömning?
- Vad behöver förändras för att nå målarkitekturen?

När frågan är tydlig blir det lättare att välja innehåll. Om frågan gäller verksamhetsförmågor bör vyn inte domineras av tekniska komponenter. Om frågan gäller integrationsrisker bör den inte främst visa strategiska mål.

En enkel regel är:

> En vy är bra när den gör en fråga lättare att diskutera utan att skapa nya missförstånd.

### Kommunikativa, analyserande och styrande vyer

Alla vyer har inte samma syfte. Det är bra att skilja mellan tre typer.

En **kommunikativ vy** hjälper människor att förstå. Den används ofta i möten, presentationer och workshops. Den ska vara tydlig, lagom detaljerad och gärna ha en berättande ordning. Den behöver inte visa allt, men den får inte förenkla så mycket att den blir missvisande.

En **analyserande vy** hjälper arkitekter eller specialister att undersöka samband. Den kan vara mer detaljerad och visa fler relationer. Den används för konsekvensanalys, beroendeanalys, gap-analys eller riskbedömning.

En **styrande vy** hjälper organisationen att fatta beslut, följa upp eller styra förändring. Den kan visa mål, principer, förmågor, initiativ, leveranser och ansvar. Den behöver vara tillräckligt stabil för att kunna återkomma i flera beslutssituationer.

I Atlantis kan en kommunikativ vy visa hur importflödet hänger ihop från deklaration till beslut. En analyserande vy kan visa vilka applikationer och informationsflöden som påverkas om riskanalystjänsten ändras. En styrande vy kan visa hur moderniseringsinitiativet bidrar till mål som snabbare klarering, ökad träffsäkerhet i kontroller och bättre rättssäkerhet.

### Ledningsvy

En ledningsvy bör svara på frågor om riktning, prioritering och konsekvens. Den ska sällan visa teknisk detalj. Den bör i stället visa samband mellan mål, drivkrafter, förmågor, större förändringsinitiativ och önskade effekter.

För Atlantis kan ledningsvyn visa:

- strategiska mål, till exempel snabbare och mer träffsäker tullhantering,
- berörda förmågor, till exempel riskanalys, varuklassificering och ärendehandläggning,
- större initiativ, till exempel modernisering av importflödet,
- huvudsakliga effekter och risker,
- beroenden till andra myndigheter eller externa aktörer.

Det som kan väljas bort är detaljerade systemintegrationer, databasstrukturer, tekniska noder och fullständiga processflöden. De kan finnas i modellen, men de behöver inte vara med i ledningsvyn om de inte påverkar beslutet.

### Verksamhetsvy

En verksamhetsvy bör hjälpa verksamhetsrepresentanter att se hur arbetet hänger ihop. Den kan visa aktörer, roller, processer, verksamhetstjänster, informationsobjekt och förmågor.

För Atlantis kan en verksamhetsvy över importflödet visa:

- aktörer som importör, tullhandläggare och riskanalytiker,
- verksamhetsprocesser som ta emot deklaration, genomföra riskbedömning och fatta beslut,
- verksamhetstjänster som importklarering och kontrollbeslut,
- centrala informationsobjekt som tulldeklaration, varupost och kontrollunderlag,
- kopplingar till förmågor som riskbaserad kontroll och rättssäker handläggning.

Det som ofta kan väljas bort är teknisk infrastruktur och detaljerade applikationskomponenter. Om verksamheten behöver förstå systemstöd kan applikationstjänster visas, men inte hela applikationslandskapet.

### IT- och applikationsvy

En IT- eller applikationsvy bör hjälpa arkitekter, systemägare och utvecklingsteam att förstå systemstöd, applikationstjänster, informationsutbyte och beroenden.

För Atlantis kan en applikationsvy visa:

- applikationskomponenter som ärendehanteringssystem, riskanalysplattform och integrationsplattform,
- applikationstjänster som hämta deklarationsdata, beräkna riskindikator och skapa kontrollärende,
- informationsflöden mellan applikationer,
- vilka verksamhetstjänster eller processer som applikationerna stödjer,
- beroenden som påverkar förändringsplanering.

Det som ofta kan väljas bort är fullständiga strategikartor, alla verksamhetsroller och detaljer på tekniknivå. Men vissa kopplingar till verksamhet och mål bör finnas kvar, annars riskerar vyn att bli en isolerad systemkarta.

### Säkerhetsvy

En säkerhetsvy bör hjälpa organisationen att förstå risk, skyddsvärde, beroenden och konsekvenser. Den behöver ofta kombinera verksamhet, information, applikation och teknik.

För Atlantis kan en säkerhetsvy visa:

- känsliga informationsobjekt,
- applikationer som behandlar informationen,
- externa parter eller myndigheter som utbyter information,
- teknikzoner eller plattformar där det är relevant,
- kritiska beroenden i import- och kontrollflöden,
- relationer till krav, principer eller säkerhetsmål.

Här är det särskilt viktigt att inte visa allt. En säkerhetsvy som innehåller hela myndighetens tekniklandskap blir snabbt oläsbar. Vyn bör avgränsas till en fråga, till exempel: “Vilka delar påverkas om kontrollunderlag klassas som särskilt skyddsvärt?”

### Portfölj- och förändringsvy

En portfölj- och förändringsvy bör visa hur initiativ, arbetspaket, leveranser och mål hänger ihop. Den hjälper organisationen att se om förändringar faktiskt bidrar till önskad utveckling.

För Atlantis kan en sådan vy visa:

- strategiska mål,
- berörda förmågor,
- förändringsinitiativ,
- arbetspaket,
- förväntade leveranser,
- beroenden mellan initiativ,
- övergångar från nuläge till målarkitektur.

Det som kan väljas bort är detaljer i processflöden och systemgränssnitt, om de inte är avgörande för prioriteringen. Däremot bör vyn visa tillräckligt med samband för att beslutsfattare ska se konsekvenser av att flytta, stoppa eller finansiera initiativ.

## Exempel: samma modell, fem vyer

Atlantis arbetar med ett initiativ som ska modernisera importflödet. Arkitekturgruppen har modellerat ett begränsat område: importdeklaration, riskbedömning, kontrollbeslut, berörda applikationer, centrala informationsobjekt och planerade förändringsinitiativ.

I stället för att skapa en stor bild väljer arkitekturgruppen fem vyer.

**Vy 1: Ledningsöversikt**  
Visar mål, förmågor och initiativ. Den används för att diskutera prioritering och förväntad effekt.

**Vy 2: Verksamhetsflöde**  
Visar roller, processer och verksamhetstjänster. Den används i workshop med verksamhetsrepresentanter.

**Vy 3: Applikationsberoenden**  
Visar applikationer, applikationstjänster och informationsflöden. Den används med systemägare och lösningsarkitekter.

**Vy 4: Säkerhetsberoenden**  
Visar skyddsvärd information, system som behandlar informationen och externa informationsutbyten. Den används i säkerhetsdialog.

**Vy 5: Förändringskarta**  
Visar nuläge, målbild, arbetspaket och beroenden. Den används i portföljstyrning.

Det viktiga är att vyerna inte är fem fristående bilder. De bygger på samma modell. Om en applikation byter namn, om en förmåga delas upp eller om ett initiativ ändras ska detta kunna slå igenom i flera vyer.

## När du ska använda detta

Använd målgruppsanpassade vyer när:

- samma modell behöver användas i flera olika samtal,
- en målgrupp drunknar i detaljer som är viktiga för en annan målgrupp,
- du behöver visa både helhet och detalj utan att blanda ihop dem,
- du vill undvika att PowerPoint-bilder blir separata sanningar,
- du vill återanvända modellinnehåll över tid.

Vyer är särskilt värdefulla när en myndighet arbetar med tvärgående förändring. I sådana situationer behöver många parter förstå samma förändring ur olika perspektiv.

## När du kan låta bli

Du behöver inte skapa många vyer om modellen bara används för ett mycket begränsat samtal. Om syftet är att snabbt förklara ett isolerat systemberoende kan en enkel vy räcka.

Du kan också vänta med avancerad vyhantering om organisationen ännu inte har modellvana. I början är det ofta bättre att skapa några få tydliga vyer än att införa en stor vykatalog.

Det viktiga är att inte skapa vyer bara för att det går. Varje vy bör ha en användare, en fråga och ett sammanhang.

## Vanliga misstag

- **Misstag: Att visa hela modellen för alla.**
  - Varför det händer: Arkitekten vill vara transparent och visa allt arbete som lagts ner.
  - Hur du undviker det: Börja med målgruppens fråga och välj bort det som inte hjälper samtalet.

- **Misstag: Att göra varje vy till en fristående bild.**
  - Varför det händer: Det går snabbt att kopiera en gammal bild och anpassa den för nästa möte.
  - Hur du undviker det: Återanvänd element och relationer från modellen, även när presentationen förenklas.

- **Misstag: Att blanda flera beslutssituationer i samma vy.**
  - Varför det händer: Man vill att en bild ska fungera för ledning, verksamhet och IT samtidigt.
  - Hur du undviker det: Skapa hellre två eller tre enklare vyer med tydlig målgrupp.

- **Misstag: Att tro att en vy måste vara komplett.**
  - Varför det händer: Modellering förväxlas med dokumentation av allt som finns.
  - Hur du undviker det: Skriv ner vilken fråga vyn ska besvara och avgränsa därefter.

- **Misstag: Att välja ArchiMate-element efter symbolernas utseende.**
  - Varför det händer: Vyn skapas som en bild och inte som ett modellurval.
  - Hur du undviker det: Välj element efter betydelse, relation och analysbehov.

## Övningar

### Övning 1: Identifiera målgrupp och fråga

Välj en arkitekturbild som används i din organisation i dag. Svara på följande frågor:

1. Vem är målgruppen?
2. Vilken fråga ska bilden hjälpa målgruppen att besvara?
3. Vilka delar i bilden stödjer frågan?
4. Vilka delar skapar mest brus?
5. Skulle bilden kunna delas upp i två vyer?

### Övning 2: Skapa tre vyer från samma modellområde

Utgå från Atlantis-scenariot eller ett eget område. Välj ett förändringsinitiativ, till exempel modernisering av importflödet.

Skapa en kort beskrivning av tre vyer:

1. En ledningsvy.
2. En verksamhetsvy.
3. En applikationsvy.

För varje vy, skriv:

- målgrupp,
- huvudfråga,
- vilka elementtyper som bör visas,
- vilka detaljer som bör väljas bort,
- vilket beslut eller samtal vyn ska stödja.

### Fördjupning

Fundera över vilka vyer som borde vara återkommande i en större myndighet. Exempel kan vara förmågekarta, systemstödsöversikt, informationsflödesvy, initiativkarta och säkerhetsberoendevy.

Välj tre återkommande vyer och beskriv vilka kvalitetskriterier de bör ha. Ska de uppdateras inför varje beslut, varje kvartal eller bara när större förändringar sker?

## Exempel på vyer från samma modell

Samma underliggande modell kan ge flera olika vyer. Det är en av de stora skillnaderna mellan modellering och fristående bilder.

Exempel från Atlantis:

- Ledningen får en vy över mål, förmågor och större förändringsinitiativ.
- Verksamhetsansvariga får en vy över processer, roller, information och verksamhetstjänster.
- IT-arkitekter får en vy över applikationstjänster, applikationskomponenter och integrationer.
- Säkerhetsfunktionen får en vy över informationsobjekt, skyddsvärden, zoner och kritiska beroenden.
- Portföljstyrningen får en vy över arbetspaket, leveranser, platåer och påverkade förmågor.

Det viktiga är att vyerna inte blir fem separata sanningar. De ska vara olika utsnitt ur samma modell, anpassade till olika frågor.

## Snabb sammanfattning

- En vy är ett målgruppsanpassat urval ur modellen.
- Samma modell kan ge flera vyer utan att skapa flera separata sanningar.
- Bra vyer börjar med målgrupp, fråga och beslutssituation.
- Ledningsvyer bör visa riktning, påverkan och prioritering.
- Verksamhetsvyer bör visa arbete, roller, tjänster och förmågor.
- Applikationsvyer bör visa systemstöd, tjänster, informationsflöden och beroenden.
- Säkerhetsvyer bör vara avgränsade till risk, skyddsvärde och kritiska samband.
- Portföljvyer bör visa hur initiativ bidrar till mål och målarkitektur.
- Det är bättre med några få användbara vyer än många diagram utan tydlig användning.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan modell, vy och diagram?
2. Varför bör inte alla målgrupper få se samma kompletta modellvy?
3. Vilken typ av vy passar bäst för en ledningsgrupp som ska prioritera ett initiativ?
4. Vilken information bör ofta finnas i en applikationsvy?
5. När kan en säkerhetsvy behöva kombinera verksamhets-, informations-, applikations- och teknikperspektiv?
6. Vad är risken med att skapa fristående vyer som inte bygger på samma modell?
7. Vilka tre vyer skulle skapa mest nytta i din egen organisation just nu?

## Nästa steg

Nu har vi sett hur modeller kan presenteras för olika målgrupper utan att förlora sammanhanget. Nästa kapitel går vidare till en fråga som är minst lika viktig: vad man kan välja bort. Där handlar det om att modellera tillräckligt mycket för att skapa nytta, men inte så mycket att modellen blir tung, dyr och svår att använda.
