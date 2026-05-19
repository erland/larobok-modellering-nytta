# Kapitel 10: Relationer: där modellens värde uppstår

## Varför detta kapitel finns

Det är lätt att tro att ArchiMate handlar om symboler. En aktör ser ut på ett sätt, en applikationskomponent på ett annat och en tekniknod på ett tredje. Men i praktisk modellering är det ofta inte symbolerna som skapar mest värde. Värdet uppstår i relationerna.

En bild kan visa att Tullmyndigheten Atlantis har en verksamhetsprocess, ett ärendehanteringssystem och en integrationsplattform. Men bilden säger inte alltid vad sakerna betyder för varandra. Stödjer systemet processen? Används systemet direkt av en roll? Realiserar applikationen en tjänst? Flödar information mellan två applikationer? Finns ett beroende som gör att ett förändringsinitiativ påverkar flera delar av organisationen?

När relationer saknas blir modellen en samling namngivna rutor. Då kan den fortfarande vara begriplig i ett möte, men den blir svår att återanvända. Den kan inte besvara följdfrågor på ett tillförlitligt sätt. Den kan inte användas för konsekvensanalys, spårbarhet eller kvalitetsgranskning. Den kan inte heller hjälpa organisationen att se skillnaden mellan saker som bara råkar stå bredvid varandra och saker som faktiskt hänger ihop.

I Atlantis vill arkitekterna förstå vad som påverkas när importflödet moderniseras. De har redan identifierat förmågor, processer, applikationer, informationsobjekt, teknikplattformar, mål och arbetspaket. Men så länge dessa delar inte är kopplade med tydliga relationer är modellen ofullständig. Det är relationerna som gör att man kan följa kedjan från ett strategiskt mål till en förändrad förmåga, vidare till en process, en applikationstjänst, en applikationskomponent och ett tekniskt beroende.

Det här kapitlet handlar därför om hur relationer gör modellen användbar. Målet är inte att lära ut varje möjlig relationstyp i ArchiMate. Målet är att hjälpa dig välja relationer som är tillräckligt precisa för att skapa nytta, men inte så detaljerade att modellen blir tung, svårbegriplig eller omöjlig att förvalta.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara varför relationer ofta är viktigare än enskilda element,
- skilja mellan visuell närhet och faktisk modellrelation,
- välja enkla relationer som stödjer analys och spårbarhet,
- undvika övermodellering av relationer,
- se när en relation behöver vara exakt och när en enklare koppling räcker,
- använda relationer för att förstå påverkan i Tullmyndigheten Atlantis.

## Innan vi börjar

Du har redan mött flera byggstenar i modellen:

- verksamhetsförmågor, processer, roller och tjänster,
- applikationskomponenter, applikationstjänster och informationsutbyten,
- teknikplattformar och tekniska beroenden,
- mål, drivkrafter, krav och principer,
- arbetspaket, leveranser och övergångar.

Alla dessa kan ritas var för sig. Men en arkitekturmodell blir först riktigt användbar när byggstenarna kopplas ihop.

En relation är inte bara en linje. Den är ett påstående. När du ritar en relation säger du något om verkligheten eller den planerade förändringen. Därför ska relationer behandlas med samma omsorg som element.

En dålig relation säger:

> Något har nog med något annat att göra.

En bättre relation säger:

> Den här applikationstjänsten stödjer den här verksamhetsprocessen.

En ännu mer användbar relation säger:

> Den här applikationstjänsten realiseras av den här applikationskomponenten och används av den här verksamhetsprocessen i importflödet.

Skillnaden är viktig. Det är den som avgör om modellen bara fungerar som samtalsbild eller om den också kan stödja analys.

## Huvudförklaring

### Relationer som påståenden

När du lägger in en relation i modellen skapar du ett strukturerat påstående. Det påståendet kan senare användas av någon annan, i en annan vy eller i en annan analys.

Tänk på relationer som meningar:

- Importhandläggare använder Importportalen.
- Importportalen erbjuder en digital ansökningstjänst.
- Riskanalysförmågan stödjs av riskbedömningstjänsten.
- Riskbedömningstjänsten realiseras av Riskanalysplattformen.
- Modernisering av importflödet påverkar Ärendehanteringssystemet.

Varje mening kan översättas till en modellrelation. Om relationen är tydlig kan modellen svara på frågor som:

- Vilka processer använder den här applikationstjänsten?
- Vilka applikationer stödjer en viss förmåga?
- Vilka tekniska plattformar blir indirekt berörda av ett förändringsinitiativ?
- Vilka mål saknar koppling till konkreta leveranser?
- Vilka system verkar kritiska eftersom många processer är beroende av dem?

Om relationerna däremot bara är lösa linjer blir modellen svag. Den kan se sammanhängande ut, men den bär inte mycket mening.

### Visuell närhet är inte en relation

I en ritad bild kan man antyda samband genom placering. Två rutor står nära varandra. En pil går ungefär mellan två områden. En färg antyder tillhörighet. För ett enskilt möte kan det räcka.

I en modell räcker det inte.

Om Importportalen står bredvid Importprocessen vet vi inte om portalen:

- används av processen,
- stödjer processen indirekt,
- realiserar en tjänst som processen använder,
- är tänkt att ersätta något i processen,
- bara nämns i samma sammanhang.

När modellen ska återanvändas behöver relationen uttryckas. Annars kan nästa person läsa in en annan betydelse än den du avsåg.

Det betyder inte att varje samband måste modelleras med maximal precision. Men det betyder att viktiga samband inte bör lämnas åt placering, färg eller muntlig förklaring.

### Den minsta användbara relationen

En vanlig fallgrop är att tro att man måste välja den mest exakta relationstypen varje gång. Det leder ofta till osäkerhet. Arkitekter fastnar i frågor som:

- Är detta serving, realization, access eller association?
- Ska relationen gå från verksamhet till applikation eller tvärtom?
- Behöver vi modellera informationsobjektet också?
- Måste vi skilja på användning, stöd och realisering?

Ibland är precision viktig. Men ibland är det viktigare att fånga ett stabilt och begripligt samband. Frågan bör vara:

> Vilken relation behöver vi för att modellen ska kunna besvara den fråga vi arbetar med?

Om syftet är att förstå vilka applikationer som påverkas av en förändrad process kan en enkel koppling mellan process och applikationstjänst räcka i ett första steg. Om syftet är att analysera ansvar, realisering och tekniska beroenden behöver relationerna vara mer precisa.

En minimal användbar relation är en relation som:

- går mellan två tydligt definierade element,
- uttrycker ett samband som målgruppen behöver förstå,
- kan återanvändas i fler än en vy,
- är tillräckligt precis för den aktuella frågan,
- går att förvalta utan orimlig arbetsinsats.

### Vanliga relationstyper i praktiken

I en praktisk myndighetsmodell behöver man ofta återkomma till några grundmönster. Namnen på relationstyperna kan variera beroende på verktyg och ArchiMate-version, men tänkesättet är viktigare än memoreringen.

| Praktisk fråga | Typiskt relationsmönster | Exempel i Atlantis |
|---|---|---|
| Vad stödjer vad? | En tjänst eller komponent stödjer en process eller förmåga | Riskbedömningstjänsten stödjer Importkontroll |
| Vad realiserar vad? | En mer konkret del realiserar en mer abstrakt tjänst eller funktion | Riskanalysplattformen realiserar Riskbedömningstjänsten |
| Vem använder vad? | En roll, process eller tjänst använder en annan tjänst | Importhandläggare använder Digital importtjänst |
| Vilken information berörs? | En process eller applikation läser, skapar eller förändrar information | Importprocessen använder Tulldeklaration |
| Vad påverkas av förändring? | Ett arbetspaket eller en förändring påverkar element i nuläge eller målbild | Programmet Moderniserat importflöde påverkar Ärendehanteringssystemet |
| Vad består något av? | Ett större element delas upp i delar | Importflödet består av registrering, riskbedömning och beslut |

Tabellen är inte en fullständig relationslära. Den är en startpunkt för användbar modellering. I praktiken räcker det ofta långt att organisationen blir konsekvent med några få relationsmönster innan den försöker använda hela språket.

### Relationer över lager

En stor del av nyttan med ArchiMate är att kunna koppla ihop verksamhet, applikation, teknik, motivation och förändring. Det är ofta här modeller blir mer värdefulla än fristående bilder.

I Atlantis kan en kedja se ut så här:

1. Målet är att korta ledtiden för importärenden.
2. Målet påverkar förmågan att hantera importflöden.
3. Förmågan stöds av processen för importklarering.
4. Processen använder en digital importtjänst.
5. Tjänsten realiseras av Importportalen.
6. Importportalen är beroende av integrationsplattformen.
7. Integrationsplattformen driftas på en teknisk plattform.
8. Ett arbetspaket ska modernisera delar av integrationsplattformen.

Varje steg i kedjan är en relation. Kedjan gör det möjligt att diskutera påverkan. Om integrationsplattformen har kapacitetsproblem kan det påverka Importportalen. Om Importportalen påverkas kan den digitala importtjänsten påverkas. Om tjänsten påverkas kan importklareringen påverkas. Då är det inte längre en teknisk detalj. Det blir en verksamhetsfråga.

Det är just den typen av resonemang som gör modellering värdefull i en större myndighet.

### Relationer och spårbarhet

Spårbarhet betyder att man kan följa kopplingar mellan beslut, krav, verksamhetsbehov, lösningar och förändringar. Utan relationer blir spårbarhet manuell. Någon måste minnas varför en applikation finns, vilket mål ett projekt stödjer eller vilka processer som påverkas av ett systembyte.

Med relationer kan modellen hjälpa till.

Exempel:

- Ett mål kan kopplas till ett krav.
- Kravet kan kopplas till en applikationstjänst.
- Applikationstjänsten kan kopplas till en applikationskomponent.
- Applikationskomponenten kan kopplas till ett arbetspaket.
- Arbetspaketet kan kopplas till en leverans.

Då kan Atlantis ställa frågor som:

- Vilka arbetspaket bidrar till målet om snabbare importklarering?
- Vilka krav saknar realisering?
- Vilka applikationer saknar tydlig koppling till verksamhetsnytta?
- Vilka projekt förändrar kritiska verksamhetsförmågor?
- Vilka mål saknar praktisk genomförandeplan?

Det här kräver inte att hela myndigheten modelleras på en gång. Det kräver att relationerna i det valda området är tillräckligt konsekventa.

### Relationer och modellkvalitet

Relationer är också ett sätt att upptäcka kvalitetsproblem.

Om en applikationskomponent inte realiserar någon tjänst kan den fortfarande vara viktig, men modellen väcker en fråga: varför finns den med? Om ett strategiskt mål inte har någon koppling till krav, förmågor eller initiativ kan det vara ett tecken på att målbilden inte omsatts i förändring. Om en process använder många applikationer kan det visa fragmentering. Om ett arbetspaket påverkar många kritiska delar kan det behöva mer styrning och riskhantering.

Modellen ska inte automatiskt ersätta mänsklig bedömning. Men den kan göra svaga eller oklara samband synliga.

Relationer hjälper alltså till att kvalitetssäkra modellen genom att visa:

- saknade kopplingar,
- oväntade beroenden,
- för många eller för få relationer,
- element som bara finns som dekoration,
- förändringar som inte är kopplade till nytta,
- mål som inte är kopplade till genomförande.

### När relationer ska vara exakta

I vissa situationer bör relationer vara mer exakta. Det gäller särskilt när modellen används för analys, styrning eller beslut där feltolkningar kan få konsekvenser.

Var mer noggrann när relationen används för att:

- analysera påverkan inför beslut,
- förstå ansvar eller ägarskap,
- bedöma säkerhet eller regelefterlevnad,
- planera avveckling av system,
- prioritera investeringar,
- följa upp om initiativ realiserar mål,
- kommunicera mellan flera team eller leverantörer.

Om Atlantis ska fatta beslut om att avveckla ett äldre ärendehanteringssystem räcker det inte med en grov pil till “importverksamheten”. Då behöver modellen visa vilka processer, tjänster, informationsobjekt, integrationer och beroenden som faktiskt påverkas.

### När relationer kan vara enklare

I andra situationer är en enklare relation tillräcklig. Det gäller särskilt tidigt i arbetet, när syftet är att skapa gemensam orientering.

En enklare relation kan räcka när:

- modellen används för att starta en diskussion,
- området fortfarande är oklart,
- målgruppen behöver en översikt,
- detaljerna inte påverkar beslutet,
- relationen ska förfinas senare,
- för mycket precision skulle bromsa arbetet.

Det viktiga är att vara tydlig med modellens mognad. En översiktsmodell får gärna vara enkel, men den ska inte presenteras som om den vore en fullständig beroendeanalys.

## Exempel: Atlantis moderniserar riskbedömningen

Tullmyndigheten Atlantis vill förbättra sin riskbedömning av importärenden. I ett första möte finns en bild med fem rutor:

- Importprocessen
- Importportalen
- Riskanalysplattformen
- Tulldeklaration
- Moderniseringsprogrammet

Bilden är begriplig, men den säger inte tillräckligt. Arkitekterna gör därför om den till en enkel modell med relationer:

- Importprocessen använder Digital importtjänst.
- Digital importtjänst realiseras av Importportalen.
- Importportalen använder Riskbedömningstjänst.
- Riskbedömningstjänst realiseras av Riskanalysplattformen.
- Riskanalysplattformen använder informationsobjektet Tulldeklaration.
- Moderniseringsprogrammet påverkar Importportalen och Riskanalysplattformen.
- Målet Kortare ledtid för importärenden motiverar Moderniseringsprogrammet.

Nu kan modellen börja besvara frågor.

Om Riskanalysplattformen försenas påverkas Riskbedömningstjänsten. Om Riskbedömningstjänsten påverkas kan Digital importtjänst få sämre funktion. Om Digital importtjänst påverkas kan Importprocessen behöva fortsätta med manuella steg. Då blir en teknisk försening synlig som verksamhetsrisk.

Det är inte linjerna i sig som skapar nyttan. Det är att relationerna har betydelse.

## När du ska använda detta

Lägg särskild omsorg på relationer när du vill att modellen ska användas för något av följande:

- konsekvensanalys,
- prioritering,
- målspårning,
- avvecklingsbeslut,
- portföljstyrning,
- säkerhets- eller regelefterlevnadsanalys,
- samverkan mellan verksamhet och IT,
- återanvändbara vyer för flera målgrupper.

En modell utan relationer kan vara en bra skiss. En modell med genomtänkta relationer kan bli ett beslutsunderlag.

## När du kan låta bli

Du behöver inte modellera alla relationer i alla lägen.

Du kan vänta med relationer eller hålla dem mycket enkla när:

- du gör en tidig workshopskiss,
- du ännu inte vet vilka element som ska vara kvar,
- målgruppen bara behöver förstå huvuddelarna,
- modellen inte ska återanvändas,
- relationerna skulle ge falsk precision,
- detaljerna riskerar att flytta fokus från huvudfrågan.

Det är bättre att ha få tydliga relationer än många oklara. En modell med tjugo genomtänkta relationer kan vara mer användbar än en modell med tvåhundra linjer som ingen vågar lita på.

## Vanliga misstag

- **Misstag: Att använda linjer som dekoration.**
  - Varför det händer: Man vill visa att saker hör ihop, men har inte bestämt hur.
  - Hur du undviker det: Skriv relationen som en mening innan du modellerar den.

- **Misstag: Att blanda olika betydelser i samma relationstyp.**
  - Varför det händer: Det går snabbt att använda samma pil för allt.
  - Hur du undviker det: Bestäm några grundmönster och dokumentera vad de betyder i er modell.

- **Misstag: Att övermodellera relationer för tidigt.**
  - Varför det händer: Man vill göra modellen korrekt från början.
  - Hur du undviker det: Börja med den relation som behövs för den aktuella frågan och förfina senare.

- **Misstag: Att lita på placering i stället för relationer.**
  - Varför det händer: I bilder fungerar närhet, färg och gruppering ofta bra.
  - Hur du undviker det: Lägg modellrelationer för samband som ska kunna återanvändas eller analyseras.

- **Misstag: Att skapa relationer som ingen förvaltar.**
  - Varför det händer: Det är lätt att lägga till linjer, men svårare att hålla dem aktuella.
  - Hur du undviker det: Modellera bara relationer som har ett tydligt syfte eller ägarskap.

- **Misstag: Att tro att varje relation måste vara perfekt.**
  - Varför det händer: ArchiMate upplevs som ett exakt språk där varje val kan bli fel.
  - Hur du undviker det: Skilj mellan översiktsmodell, arbetsmodell och beslutsmodell. Kräv inte samma precision överallt.

## Övningar

### Övning 1: Skriv relationerna som meningar

Välj en befintlig arkitekturbild från din organisation. Identifiera fem linjer eller visuella samband.

Skriv varje samband som en enkel mening:

1. Vad är källan?
2. Vad är målet?
3. Vad betyder sambandet?
4. Behöver sambandet vara exakt?
5. Ska det finnas i modellen eller bara i vyn?

Exempel:

> Importportalen använder Riskbedömningstjänsten.

Jämför sedan meningarna med bilden. Blir vissa samband tydligare än de var visuellt?

### Övning 2: Hitta den minsta användbara relationen

Utgå från frågan:

> Vilka applikationer påverkas om importprocessen förändras?

Skapa en enkel modellkedja med minst fyra element:

- en verksamhetsprocess,
- en applikationstjänst,
- en applikationskomponent,
- ett arbetspaket.

Lägg bara till de relationer som behövs för att kunna besvara frågan. Lägg inte till teknik, informationsobjekt eller mål om de inte behövs.

Reflektera sedan:

- Vad kunde du välja bort?
- Vilken relation var viktigast?
- Vilken relation blev osäker?
- Vad skulle behöva förfinas om modellen skulle användas som beslutsunderlag?

### Fördjupning

Ta samma modell och lägg till ett mål samt ett tekniskt beroende. Koppla dem med relationer så att du kan följa kedjan från mål till teknik.

Besvara sedan:

- Vilka nya frågor kan modellen svara på?
- Vilka nya kvalitetskrav uppstår?
- Blir modellen mer användbar eller bara mer komplicerad?

## Exempel på relationsval

Relationer ska väljas utifrån vad man vill kunna säga sant om modellen. En relation som är för vag skapar liten nytta. En relation som är för detaljerad kan skapa falsk precision.

Exempel från Atlantis:

- **Verksamhetsprocessen Granska importärende använder applikationstjänsten Visa ärendedata.** Detta säger något om stöd i arbetet.
- **Applikationstjänsten Riskbedöm importdeklaration realiseras av Riskanalysplattformen.** Detta säger något om ansvar i applikationslagret.
- **Kravet Spårbar beslutsmotivering påverkar Ärendehanteringssystemet.** Detta säger något om förändringspåverkan.
- **Arbetspaketet Inför digital importkanal levererar Ny självservicetjänst.** Detta säger något om genomförandet.

En bra kontrollfråga är: om relationen tas bort, förlorar modellen då ett samband som någon behöver för att fatta beslut? Om svaret är nej kan relationen ofta vänta.

## Snabb sammanfattning

- Relationer är strukturerade påståenden, inte bara linjer.
- Modellens analysvärde uppstår ofta i relationerna mellan element.
- Visuell närhet, färg och placering räcker inte när modellen ska återanvändas.
- Börja med den minsta relation som behövs för att besvara den aktuella frågan.
- Var mer exakt när modellen används för beslut, påverkan, ansvar, säkerhet eller uppföljning.
- Håll relationer enklare när modellen är en tidig översikt.
- Få tydliga relationer är bättre än många oklara.
- I en myndighetskontext gör relationer det möjligt att koppla strategiska mål till verksamhet, applikationer, teknik och förändringsinitiativ.

## Quiz/reflektionsfrågor

1. Varför är en relation mer än en linje i en modell?
2. Vad är skillnaden mellan visuell närhet och en faktisk modellrelation?
3. När bör en relation vara mer exakt?
4. När kan en enklare relation räcka?
5. Hur kan relationer hjälpa Tullmyndigheten Atlantis att förstå påverkan av ett moderniseringsprogram?
6. Vilka risker uppstår om en modell har många relationer som ingen litar på?
7. Vilken relation i en befintlig modell i din organisation skulle skapa mest nytta om den förtydligades?

## Nästa steg

Nu har vi gått igenom flera centrala delar av modellering: syfte, språk, myndighetsnytta, verksamhet, applikation, teknik, motivation, förändring och relationer. Nästa kapitel handlar om vyer för olika målgrupper.

Det är ett naturligt nästa steg. När modellen har tydliga element och relationer kan den presenteras på olika sätt för olika behov. Ledningen behöver inte se samma vy som en lösningsarkitekt. En verksamhetsexpert behöver inte se samma detaljer som en teknisk plattformsansvarig. Men om vyerna bygger på samma modell kan de ändå hänga ihop.
