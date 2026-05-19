# Kapitel 14: Modellering som arbetssätt

## Varför detta kapitel finns

När en organisation börjar använda ArchiMate uppstår ofta en tydlig första fas. Några arkitekter lär sig notation, bygger några modeller, tar fram några vyer och visar att modellerna kan ge bättre samtal än fristående bilder. Det är ett viktigt steg, men det räcker inte för att modellering ska bli en varaktig förmåga.

Det här kapitlet handlar om nästa steg: modellering som arbetssätt.

Med arbetssätt menas inte att alla måste modellera allt på samma sätt, i samma verktyg och med samma detaljnivå. Det betyder att organisationen har tillräckligt gemensamma principer för att modeller ska kunna återanvändas, förstås, förbättras och användas i riktiga beslut. Det betyder också att modellering blir en del av arkitekturarbetet, inte en separat aktivitet som görs vid sidan av.

För Tullmyndigheten Atlantis har de första modellerna börjat skapa nytta. Arkitekterna har använt dem för att diskutera importflödet, förstå beroenden mellan förmågor och applikationer, och visa varför vissa förändringsinitiativ behöver samordnas. Nu uppstår en ny fråga: hur undviker myndigheten att modelleringen blir personberoende, ojämn eller alltför tung?

Det är här arbetssättet blir avgörande. En modell kan vara bra i ett enskilt projekt. Ett modelleringsarbetssätt gör att modellerna fortsätter vara användbara när projektet är slut, när nya initiativ startar och när fler arkitekter behöver bidra.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva vad det innebär att göra modellering till ett arbetssätt,
- skilja mellan nyttig modellstyrning och onödig modellbyråkrati,
- formulera enkla modellprinciper för en större myndighet,
- förklara roller och ansvar kring modellkvalitet och modellförvaltning,
- känna igen risker som gör att modellering tappar nytta över tid,
- föreslå en realistisk fortsättning efter de första lyckade modellerna.

## Innan vi börjar

Tidigare kapitel har visat hur man kan börja med syfte, välja relevanta delar av ArchiMate, bygga vyer för olika målgrupper, välja bort sådant som inte behövs och börja använda modeller i riktiga sammanhang.

Det här kapitlet samlar ihop trådarna. Fokus ligger inte på fler ArchiMate-element, utan på de organisatoriska förutsättningarna för att modellering ska fortsätta ge nytta.

Tre begrepp är särskilt viktiga:

- **Modellprinciper**: enkla regler som hjälper arkitekter att modellera tillräckligt konsekvent.
- **Modellförvaltning**: arbetet med att hålla modeller relevanta, begripliga och användbara över tid.
- **Governance**: de beslut, ansvar och forum som styr hur modeller skapas, ändras och används.

I den här boken används governance i praktisk mening. Det handlar inte i första hand om formella styrdokument, utan om hur organisationen säkerställer att modellering stödjer verkliga behov.

## Från aktivitet till vana

I många organisationer börjar modellering som en aktivitet:

- någon skapar en modell inför ett projektmöte,
- någon gör en vy till ett beslutsunderlag,
- någon dokumenterar ett applikationslandskap,
- någon modellerar målarkitektur för ett initiativ.

Detta kan ge nytta. Men om varje modell skapas isolerat blir nyttan kortlivad. När mötet är över, projektet avslutat eller arkitekten bytt uppdrag tappar modellen ofta betydelse.

Modellering som arbetssätt innebär att modellerna får en plats i det återkommande arkitekturarbetet. De används inte bara när någon särskilt efterfrågar en bild, utan när organisationen behöver förstå, analysera och besluta.

Skillnaden kan beskrivas så här:

| Modellering som aktivitet | Modellering som arbetssätt |
|---|---|
| Görs inför en viss presentation | Används löpande i arkitekturarbetet |
| Resultatet är ofta en vy eller bild | Resultatet är en modell som kan ge flera vyer |
| Ansvar ligger hos enskild arkitekt | Ansvar är fördelat och tydligt |
| Kvalitet bedöms visuellt | Kvalitet bedöms utifrån användbarhet och spårbarhet |
| Modellen blir snabbt inaktuell | Modellen har en förvaltad livscykel |

För Atlantis betyder detta att modellen över importflödet inte ska vara “arkitektens modell”. Den ska vara en gemensam kunskapsresurs som kan användas av flera arkitekter och förbättras när ny kunskap uppstår.

## Modellering behöver ett tydligt syfte även som arbetssätt

När modellering skalas upp finns en risk att organisationen börjar modellera för modelleringens skull. Det kan låta så här:

- “Alla projekt måste leverera ArchiMate-modeller.”
- “Alla system ska beskrivas på samma detaljnivå.”
- “Alla relationer måste vara fullständiga innan modellen får användas.”
- “Vi behöver först modellera hela myndigheten.”

Sådana ambitioner kan verka ordningsamma, men de riskerar att skapa tröghet. Om kraven blir för stora kommer arkitekter och projektledare att se modellering som administration snarare än som stöd.

Därför behöver även ett gemensamt arbetssätt utgå från samma princip som tidigare i boken:

> Modellera det som behövs för att skapa nytta i en faktisk fråga.

Det betyder att Atlantis inte bör börja med ett krav på heltäckande myndighetsmodell. En bättre start är att definiera några återkommande användningsfall där modellerna ska användas.

Exempel:

- konsekvensanalys vid förändring av centrala applikationer,
- portföljdialog kring överlappande initiativ,
- målarkitekturdialog för modernisering av importflödet,
- förmågebaserad prioritering,
- risk- och beroendeanalys inför större upphandlingar,
- dialog med verksamheten om vad en förändring faktiskt påverkar.

Dessa användningsfall ger riktning för modelleringen. De hjälper också organisationen att avgöra vilken kvalitet som krävs.

## En liten uppsättning modellprinciper

Ett modelleringsarbetssätt behöver principer. Men principerna bör vara få, begripliga och användbara. Om principerna blir för många kommer de inte att följas. Om de blir för abstrakta hjälper de inte i vardagen.

För Atlantis kan en första uppsättning modellprinciper se ut så här:

1. **Modellen ska ha ett uttalat syfte.** Varje modellutsnitt ska kunna kopplas till en fråga, målgrupp eller beslutssituation.
2. **Vyer ska bygga på modellen.** En vy får förenkla, men den ska inte hitta på en annan verklighet än modellen.
3. **Element ska namnges så att verksamhet och IT kan förstå dem.** Namn ska inte vara interna förkortningar om målgruppen inte delar dem.
4. **Relationer ska bara läggas till när de betyder något.** En relation ska hjälpa någon att förstå beroende, ansvar, användning, realisering eller påverkan.
5. **Detaljnivån ska följa nyttan.** Allt behöver inte modelleras lika djupt.
6. **Modellen ska kunna förklaras muntligt.** Om arkitekten inte kan förklara modellen utan att peka på varje symbol är modellen troligen för krånglig.
7. **Modellen ska ägas och förvaltas.** Någon ska veta varför modellen finns, när den senast användes och när den behöver ses över.

Dessa principer är inte perfekta eller fullständiga. De är medvetet enkla. Syftet är att skapa en gemensam lägstanivå utan att kväva lärande och anpassning.

## Roller och ansvar

När modeller skapas av enskilda personer kan arbetet fungera så länge organisationen är liten eller modellen är begränsad. I en större myndighet behövs tydligare ansvar.

Det betyder inte att man måste införa en stor modellorganisation. Men några roller behöver vara begripliga.

### Modellägare

En modellägare ansvarar för att ett modellområde har ett syfte och fortsätter vara relevant. Det kan vara en chefsarkitekt, domänarkitekt, verksamhetsarkitekt eller annan person med ansvar för ett arkitekturområde.

Modellägaren behöver inte själv modellera allt. Däremot behöver modellägaren kunna svara på frågor som:

- Varför finns detta modellområde?
- Vilka beslut eller analyser ska det stödja?
- Vem använder modellen?
- När är modellen tillräckligt bra?
- När behöver modellen uppdateras?

I Atlantis kan modellen över importflödet ha en modellägare inom den arkitekturfunktion som ansvarar för verksamhets- och applikationsarkitektur kopplat till kärnflöden.

### Modellförfattare

Modellförfattaren skapar och ändrar modellen. Det är ofta en arkitekt, men kan också vara någon annan med modellkompetens och sakområdeskunskap.

Modellförfattaren behöver förstå både ArchiMate och sammanhanget. En modell som är språkligt korrekt men sakligt missvisande ger liten nytta. En modell som är sakligt rik men notationsmässigt otydlig blir svår att återanvända.

### Modellgranskare

Modellgranskaren hjälper till att bedöma kvalitet. Det kan handla om sakgranskning, arkitekturgranskning eller modellgranskning.

Granskningen bör inte bara fråga: “Är ArchiMate korrekt använt?” Den bör också fråga:

- Svarar modellen på sin fråga?
- Är vyn begriplig för målgruppen?
- Är viktiga relationer uttryckta?
- Har modellen onödiga detaljer?
- Går det att återanvända modellen i nästa steg?

### Modellanvändare

Modellanvändaren är den som drar nytta av modellen. Det kan vara en beslutsfattare, verksamhetsutvecklare, projektledare, säkerhetsspecialist, produktägare, utvecklingsteam eller annan arkitekt.

Det är lätt att glömma modell-användaren. Men utan användare finns ingen modellnytta. Därför bör varje viktig modell ha en tydlig målgrupp, även om målgruppen bara är “arkitekter som ska göra konsekvensanalys”.

## Modellkvalitet är mer än snygga vyer

En snygg vy kan vara värdefull. Den kan skapa intresse, göra ett svårt samband begripligt och ge en bra startpunkt för dialog. Men modellkvalitet är mer än visuell kvalitet.

En användbar modell behöver flera typer av kvalitet.

### Begreppskvalitet

Begreppskvalitet handlar om att elementen betyder rätt saker. Om “Importkontroll” ibland betyder en process, ibland en förmåga och ibland en organisatorisk funktion blir modellen svår att lita på.

Atlantis behöver därför vara noga med centrala begrepp. Om “Riskanalys” modelleras som förmåga i ett sammanhang och som applikationstjänst i ett annat måste det finnas en tydlig anledning. Annars skapas förvirring.

### Relationskvalitet

Relationskvalitet handlar om att sambanden uttrycker något meningsfullt. En modell med många element men få relationer blir ofta en lista i bildform. En modell med för många relationer blir svår att läsa och underhålla.

God relationskvalitet kräver frågor som:

- Vilka samband behöver vi kunna följa?
- Vilka beroenden är viktiga för beslut?
- Vilka relationer är bara visuella närhetsmarkörer?
- Vilka relationer behöver vara korrekta för analys?

### Vy-kvalitet

Vy-kvalitet handlar om att presentationen hjälper målgruppen. En vy kan vara korrekt men ändå misslyckad om den visar för mycket, använder fel begrepp eller saknar berättelse.

En ledningsvy för Atlantis behöver kanske visa hur tre moderniseringsinitiativ påverkar samma verksamhetsförmågor. Den behöver inte visa varje applikationskomponent. En arbetsvy för arkitekter kan däremot behöva mer detaljer.

### Förvaltningskvalitet

Förvaltningskvalitet handlar om att modellen går att leva med över tid. Det innebär att det finns rimliga svar på frågor som:

- Vem får ändra modellen?
- Hur vet vi vad som är aktuellt?
- Hur hanteras osäker information?
- När arkiveras eller ersätts en modell?
- Hur skiljer vi mellan nuläge, målbild och hypotes?

För Atlantis är detta särskilt viktigt eftersom myndigheten har långlivade system, regelstyrda processer och många parallella förändringsinitiativ. En modell som blandar nuläge, önskat läge och osäkra antaganden utan markering kan snabbt bli farlig som beslutsunderlag.

## Hantera nuläge, målbild och övergång

Ett vanligt problem i arkitekturmodeller är att olika tidslägen blandas ihop. En vy kan visa något som finns idag, något som är beslutat, något som är önskat och något som bara är en idé. Om detta inte syns tydligt kan modellen misstolkas.

Ett arbetssätt behöver därför ange hur Atlantis skiljer mellan:

- **nuläge**: det som faktiskt finns eller gäller,
- **beslutat framtida läge**: förändringar som är beslutade och finansierade,
- **målbild**: ett önskat tillstånd som styr riktning,
- **hypotes eller alternativ**: möjliga lösningar som ännu inte är beslutade,
- **övergångsläge**: tillfälliga lösningar under migration.

Detta behöver inte alltid uttryckas med avancerad notation. Ibland räcker det med namngivning, vyindelning, modellpaket eller tydlig metadata. Det viktiga är att användaren förstår vilken sorts information modellen visar.

Exempel från Atlantis:

- En nulägesvy visar att äldre ärendehanteringssystem fortfarande stödjer importhandläggning.
- En målbild visar att en ny applikationstjänst ska stödja automatiserad riskklassning.
- En migrationsvy visar att båda lösningarna måste existera parallellt under en övergångsperiod.
- En beslutsvy visar vilka beroenden som måste hanteras innan äldre funktionalitet kan avvecklas.

Om dessa blandas i en enda bild utan tydlig markering kan ledningen tro att målbilden redan är beslutad eller att nuläget är mer modernt än det faktiskt är.

## Verktygsdisciplin utan verktygsdyrkan

ArchiMate-modellering görs ofta i särskilda modelleringsverktyg. Verktygen kan ge stor nytta: återanvändning av element, relationer mellan vyer, rapporter, spårbarhet och analys. Men verktyg löser inte grundproblemet om arbetssättet saknas.

Det finns två vanliga ytterligheter.

Den första är verktygslöshet. Då ritar arkitekterna bilder i presentationsverktyg och tappar modellens struktur. Det kan vara snabbt, men gör det svårt att återanvända informationen.

Den andra är verktygsdyrkan. Då tror organisationen att modellnytta uppstår bara för att ett avancerat verktyg används. Resultatet blir ofta modeller som är tekniskt lagrade men inte används.

Atlantis behöver en mellanväg: tillräcklig verktygsdisciplin för att modellerna ska gå att återanvända, men inte så mycket verktygsfokus att arkitekterna glömmer användningen.

Praktiska regler kan vara:

- skapa centrala element en gång och återanvänd dem,
- undvik dubbletter med nästan samma namn,
- skilj mellan arbetsvyer och presentationsvyer,
- lägg inte in detaljer som ingen ansvarar för att hålla aktuella,
- använd modellpaket eller motsvarande struktur för domäner och tidslägen,
- dokumentera osäkerhet där modellen innehåller antaganden,
- exportera vyer till presentationer när det behövs, men behåll modellen som källa.

En användbar tumregel är:

> Presentationsverktyg kan vara mottagare av en vy, men bör inte vara källan till arkitekturmodellen.

## Governance som skydd mot två misslyckanden

Modellering kan misslyckas på två motsatta sätt.

Det första misslyckandet är anarki. Alla modellerar på sitt sätt. Samma sak får olika namn. Olika symboler används för samma begrepp. Relationer betyder olika saker i olika modeller. Det går snabbt i början, men nyttan minskar när modellerna ska kopplas ihop.

Det andra misslyckandet är byråkrati. Alla måste följa omfattande regler. Modeller granskas mer för form än för användbarhet. Arkitekter lägger mer tid på korrekthet än på insikt. Då slutar verksamheten att efterfråga modellerna.

Bra governance skyddar mot båda.

För Atlantis kan governance börja enkelt:

- en liten modellprinciplista,
- ett gemensamt begreppsregister för centrala förmågor, applikationer och tjänster,
- en överenskommen metod för att namnge nuläge och målbild,
- lättviktig granskning av modeller som ska användas i beslut,
- tydlig ansvarsfördelning för centrala modellområden,
- återkommande forum där arkitekter visar modeller och lär av varandra.

Detta är inte tung styrning. Det är ett sätt att skapa tillit. När användare litar på modellerna vågar de använda dem.

## Modellering i möten

Ett av de bästa sätten att göra modellering till arbetssätt är att använda modellen i möten. Inte som bilaga. Inte som sista slide. Utan som arbetsyta.

Det kan göras på flera sätt.

### Förberedande analys

Arkitekten använder modellen före mötet för att identifiera frågor:

- Vilka förmågor påverkas?
- Vilka applikationer återkommer i flera initiativ?
- Vilka beroenden är oklara?
- Vilka relationer saknas för att analysen ska bli trovärdig?

Mötet handlar då inte om att beundra modellen, utan om att pröva analysen.

### Gemensam rättning

Modellen visas för sakkunniga som får reagera:

- “Det där är inte en process, det är en regelstyrd kontrollpunkt.”
- “Den applikationen används inte längre i det flödet.”
- “Det saknas ett informationsutbyte med en annan myndighet.”
- “Det där är målbild, inte nuläge.”

Sådana reaktioner är värdefulla. De visar att modellen används för att skapa gemensam kunskap.

### Beslutsstöd

Modellen används för att synliggöra konsekvenser:

- Om vi avvecklar denna applikation, vilka tjänster påverkas?
- Om vi prioriterar detta initiativ, vilka andra initiativ måste samordnas?
- Om vi inför ny riskklassning, vilka processer och informationsobjekt berörs?
- Om vi skjuter upp en migration, vilka beroenden kvarstår?

När modellen används så blir den ett verktyg för styrning, inte bara dokumentation.

## Kultur: från “min bild” till “vår modell”

En underskattad del av modellering är kultur. Arkitekter är ofta vana vid att skapa egna bilder för egna uppdrag. Det kan vara effektivt och kreativt. Men det gör också att kunskap blir personbunden.

Modellering som arbetssätt kräver ett skifte:

- från min bild till vår modell,
- från presentation till kunskapsbas,
- från engångsleverans till återanvändbar struktur,
- från personlig stil till gemensam begriplighet.

Detta kan kännas ovant. En arkitekt kan uppleva att den egna uttrycksfriheten minskar. En projektledare kan uppleva att modellering tar längre tid än att rita en snabb bild. En chef kan undra varför organisationen behöver investera i modellkvalitet.

Därför behöver nyttan visas konkret. Inte genom att säga att ArchiMate är bra, utan genom att visa att modellerna hjälper Atlantis att fatta bättre beslut, undvika dubbelarbete och förstå konsekvenser tidigare.

## Vanliga misstag

- **Misstag: Att införa modellering som regel innan nyttan är visad.**
  - Varför det händer: Organisationen vill standardisera snabbt.
  - Hur du undviker det: Börja med några användningsfall där modellerna faktiskt används och låt principerna växa därifrån.

- **Misstag: Att göra governance till en granskningsmur.**
  - Varför det händer: Man vill säkerställa kvalitet.
  - Hur du undviker det: Granska i första hand modellens användbarhet, begriplighet och relevans för beslutet.

- **Misstag: Att förväxla verktygsinförande med modelleringsförmåga.**
  - Varför det händer: Verktyg är konkreta och går att upphandla.
  - Hur du undviker det: Definiera arbetssätt, roller och modellprinciper innan verktyget blir huvudfrågan.

- **Misstag: Att låta varje arkitekt skapa egna varianter av centrala begrepp.**
  - Varför det händer: Det är snabbt i början.
  - Hur du undviker det: Etablera ett litet gemensamt begreppsregister och återanvänd centrala element.

- **Misstag: Att kräva fullständig modell innan den får användas.**
  - Varför det händer: Man vill inte visa något ofärdigt.
  - Hur du undviker det: Markera osäkerhet tydligt och använd modellen för att upptäcka vad som behöver förbättras.

- **Misstag: Att glömma förvaltning efter projektet.**
  - Varför det händer: Projektet ser modellen som leverans, inte som långsiktig kunskapsresurs.
  - Hur du undviker det: Bestäm redan från början vem som äger modellen och när den ska ses över.

## Övningar

### Övning 1: Formulera tre modellprinciper

Välj ett arkitekturområde i din organisation, till exempel ett verksamhetsflöde, ett applikationsområde eller ett förändringsprogram.

Formulera tre enkla modellprinciper som skulle hjälpa arkitekter att modellera mer konsekvent utan att skapa onödig byråkrati.

Exempel:

1. Alla vyer ska ange om de visar nuläge, målbild eller övergångsläge.
2. Centrala applikationer ska återanvändas som gemensamma element.
3. Relationer ska bara användas när de hjälper analys eller kommunikation.

Diskutera sedan:

- Vilken princip ger mest nytta direkt?
- Vilken princip riskerar att bli för tung?
- Vilken princip behöver förklaras med exempel?

### Övning 2: Identifiera modellroller

Utgå från Tullmyndigheten Atlantis eller din egen organisation.

Välj ett modellområde, till exempel importflöde, kundmöte, ärendehantering, dataplattform eller digital kanal.

Besvara:

1. Vem borde vara modellägare?
2. Vem eller vilka borde vara modellförfattare?
3. Vilka sakkunniga behöver granska modellen?
4. Vilka är modellens viktigaste användare?
5. Vad händer om ingen tar ansvar för modellen efter första leveransen?

### Övning 3: Skilj mellan nuläge och målbild

Tänk dig att Atlantis visar en vy över framtida automatiserad riskklassning i importflödet.

Markera vilka delar som är:

- nuläge,
- beslutat framtida läge,
- målbild,
- hypotes,
- övergångsläge.

Reflektera sedan över vad som kan gå fel om dessa blandas i samma vy utan tydlig markering.

### Fördjupning: Designa ett lättviktigt modellforum

Skissa ett enkelt modellforum för en större myndighet.

Beskriv:

- syftet med forumet,
- vilka roller som bör delta,
- vilka modeller som ska tas upp,
- vilka beslut forumet får fatta,
- hur man undviker att forumet blir en flaskhals,
- hur forumet kan sprida lärande snarare än bara kontrollera.

## Avslutande handlingsplan

När boken är slut bör nästa steg inte vara att skapa ett stort modelleringsprogram. Ett bättre första steg är att välja en verklig arkitekturfråga och använda modellen för att förbättra ett beslut.

För Atlantis kan en enkel handlingsplan vara:

1. Välj ett prioriterat område där dagens bilder inte räcker.
2. Formulera tre frågor som modellen ska besvara.
3. Välj minsta gemensamma ArchiMate-begreppsset.
4. Skapa en modell som kan ge minst två olika vyer.
5. Använd vyerna i ett riktigt beslutsmöte.
6. Dokumentera vilken nytta modellen gav.
7. Ta bort det som inte användes.
8. Förvalta bara de delar av modellen som någon faktiskt återkommer till.

Det är så modellering blir ett arbetssätt: inte genom att alla modellerar allt, utan genom att organisationen lär sig vilka modeller som gör skillnad.

## Snabb sammanfattning

- Modellering som arbetssätt betyder att modeller används, förbättras och förvaltas som en del av arkitekturarbetet.
- Ett arbetssätt behöver gemensamma principer, men principerna ska vara få och nyttiga.
- Roller som modellägare, modellförfattare, modellgranskare och modellanvändare gör ansvaret tydligare.
- Modellkvalitet handlar om begrepp, relationer, vyer och förvaltning, inte bara om snygg layout.
- Nuläge, målbild, beslutade förändringar och hypoteser behöver skiljas åt.
- Verktyg är viktiga, men de ersätter inte syfte, arbetssätt och ansvar.
- Governance ska skapa tillit och återanvändbarhet, inte onödig modellbyråkrati.
- En stark modelleringskultur går från “min bild” till “vår modell”.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan modellering som aktivitet och modellering som arbetssätt?
2. Varför bör ett modelleringsarbetssätt fortfarande utgå från konkreta användningsfall?
3. Vilka risker finns med för mycket respektive för lite governance?
4. Vad gör en modellägare?
5. Varför räcker det inte att en vy är visuellt snygg?
6. Hur kan en organisation skilja mellan nuläge, målbild och hypotes i sina modeller?
7. Varför bör presentationsbilder inte vara den primära källan till arkitekturmodellen?
8. Vad betyder skiftet från “min bild” till “vår modell” i praktiken?

## Nästa steg

Det här kapitlet avslutar bokens huvudsakliga progression. Vi har gått från den grundläggande skillnaden mellan bild och modell till frågan om hur modellering blir ett arbetssätt som skapar nytta över tid.

För en läsare som vill gå vidare är nästa praktiska steg inte att modellera allt. Det är att välja en verklig fråga där modellen kan göra skillnad.

Börja där:

1. Välj ett prioriterat område.
2. Formulera frågan modellen ska hjälpa till att besvara.
3. Välj minsta användbara modellutsnitt.
4. Skapa en eller två vyer för verkliga målgrupper.
5. Använd modellen i ett faktiskt möte.
6. Fånga vad som blev tydligare.
7. Förbättra modellen och arbetssättet stegvis.

När modellering görs på det sättet blir ArchiMate inte bara ett språk för arkitekter. Det blir ett sätt för organisationen att tänka klarare om förändring.
