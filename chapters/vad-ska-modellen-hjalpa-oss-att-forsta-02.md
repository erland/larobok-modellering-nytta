# Kapitel 2: Vad ska modellen hjälpa oss att förstå?

## Varför detta kapitel finns

Många arkitekturbilder börjar med att någon öppnar ett ritverktyg och frågar: “Vad ska vi rita?” Det låter praktiskt, men leder ofta fel. Den viktigare frågan är: “Vad behöver vi förstå bättre än vi gör idag?”

En arkitekturmodell blir nyttig först när den hjälper någon att besvara en verklig fråga. Det kan vara en fråga om ansvar, beroenden, risk, kostnad, förändringspåverkan, informationsflöden, förmågor eller prioriteringar. Utan en sådan fråga riskerar modellen att bli en välritad karta utan tydlig användning.

I det här kapitlet lär du dig att börja modellering med syfte, beslut och användning. Det gör det lättare att välja rätt delar av ArchiMate, välja bort onödig detaljering och avgöra när en enkel bild faktiskt räcker.

## Lärandemål

Efter kapitlet ska du kunna:

- formulera en modelleringsfråga innan du börjar modellera,
- skilja mellan kommunikationssyfte, analysfråga och beslutsfråga,
- välja en rimlig första avgränsning för en modell,
- bedöma när ArchiMate-modellering ger mer nytta än en fristående bild,
- använda Tullmyndigheten Atlantis som exempel för att koppla modellering till faktisk verksamhetsnytta.

## Innan vi börjar

I förra kapitlet skilde vi mellan bild, vy och modell. En bild kan hjälpa ett samtal här och nu. En modell kan återanvändas, kopplas till andra delar, kvalitetssäkras och användas för analys. Skillnaden blir viktig först när någon vill göra något mer än att bara förstå en presentation.

Det är därför modellering inte bör börja med notation. Den bör börja med en användningssituation.

En bra startfråga är:

> Vilken fråga ska modellen hjälpa oss att besvara, och för vem?

Den frågan låter enkel, men förändrar arbetssättet. I stället för att fråga vilka symboler som ska finnas med, börjar du fråga vilken osäkerhet som behöver minska.

## Från ritbehov till förståelsebehov

När någon beställer en arkitekturbild är beställningen ofta formulerad som ett ritbehov:

- “Vi behöver en nulägesbild.”
- “Kan du rita upp systemlandskapet?”
- “Vi behöver visa hur processen hänger ihop.”
- “Gör en målarkitekturbild till styrgruppen.”
- “Kan du ta fram en bild över beroenden?”

Detta är inte fel, men det är ofullständigt. Bakom varje sådan beställning finns nästan alltid ett förståelsebehov.

| Ritbehov | Möjligt förståelsebehov |
|---|---|
| Nulägesbild | Vad består nuläget av, och var finns de viktigaste beroendena? |
| Systemlandskap | Vilka applikationer stödjer vilka verksamhetsförmågor? |
| Processbild | Vilka steg, roller och informationsobjekt är viktiga för förändringen? |
| Målarkitekturbild | Vilka förändringar behöver göras, i vilken ordning och varför? |
| Beroendebild | Vad påverkas om en komponent, förmåga eller tjänst ändras? |

En fristående bild kan räcka när syftet är att förklara något snabbt. En modell blir mer relevant när förståelsebehovet återkommer, när flera målgrupper behöver olika vyer, eller när informationen behöver analyseras och hållas ihop över tid.

## Tre sorters modelleringsfrågor

Ett praktiskt sätt att börja är att skilja mellan tre sorters frågor: kommunikationsfrågor, analysfrågor och beslutsfrågor.

### Kommunikationsfrågor

En kommunikationsfråga handlar om att skapa gemensam förståelse. Den kan låta så här:

- “Hur hänger importflödet ihop på en övergripande nivå?”
- “Vilka verksamhetsområden berörs av den nya digitala tjänsten?”
- “Vilka applikationer behöver verksamheten känna till i den här förändringen?”

Här kan en enkel vy vara tillräcklig. ArchiMate kan ändå vara användbart eftersom språket gör det tydligt vad som är en aktör, en process, en tjänst, en applikation eller ett informationsobjekt. Men modellen behöver inte vara komplett. Den behöver vara begriplig och tillräckligt konsekvent.

### Analysfrågor

En analysfråga handlar om att förstå samband, mönster eller konsekvenser. Den kan låta så här:

- “Vilka förmågor är beroende av samma äldre applikation?”
- “Var uppstår dubbelregistrering av uppgifter?”
- “Vilka delar av målarkitekturen påverkas om integrationsplattformen försenas?”
- “Vilka verksamhetstjänster använder information som klassas som känslig?”

Här börjar modellens struktur bli viktigare. Om relationerna inte är konsekventa går det inte att lita på analysen. En bild kan visa ett exempel, men en modell kan göra det möjligt att följa samband.

### Beslutsfrågor

En beslutsfråga handlar om att stödja ett val. Den kan låta så här:

- “Vilket moderniseringsalternativ bör vi prioritera först?”
- “Kan vi avveckla det gamla kontrollsystemet utan att störa kritiska flöden?”
- “Vilka beroenden måste lösas innan vi inför den nya importtjänsten?”
- “Vilka delar av verksamheten får störst nytta av gemensam ärendeinformation?”

Här måste modellen vara tillräckligt trovärdig för att påverka beslut. Det betyder inte att den måste vara fullständig. Det betyder att avgränsning, begrepp, relationer och antaganden måste vara tydliga.

## Atlantis-exempel: modernisering av importflödet

Tullmyndigheten Atlantis har ett pågående initiativ för att modernisera importflödet. Målet är att företag ska kunna lämna bättre digitala uppgifter tidigare, att riskanalysen ska bli mer träffsäker och att handläggningen ska bli mer rättssäker och effektiv.

I början ber programledningen arkitekturgruppen om “en bild över importflödet”. Det går att tolka på många sätt:

- en processbild över hur ett importärende hanteras,
- en systemkarta över applikationer som används,
- en informationsmodell över tulldeklarationer, riskdata och beslut,
- en målbild över framtida digitala tjänster,
- en beroendekarta över förändringar som måste samordnas.

Alla kan vara relevanta. Ingen är automatiskt rätt.

Arkitekturgruppen väljer därför att formulera tre modelleringsfrågor:

1. Vilka verksamhetsförmågor behövs för att hantera importflödet från föranmälan till beslut?
2. Vilka applikationer stödjer dessa förmågor idag?
3. Vilka beroenden behöver ledningen förstå innan den prioriterar moderniseringsinitiativ?

Med de frågorna blir första modellen smalare men mer användbar. Den behöver inte beskriva varje processteg, varje integration eller varje teknisk komponent. Den behöver först visa samband mellan förmågor, applikationer och förändringsbehov.

Det gör också valet av ArchiMate-delar enklare. Arkitekterna kan börja med förmågor, applikationer, applikationstjänster och några centrala relationer. Tekniklagret kan vänta. Detaljerade processflöden kan vänta. Fullständig informationsmodell kan vänta.

## Frågan styr vad du tar med

En modell blir ofta svår att använda när den försöker svara på för många frågor samtidigt. Den vill visa nuläge, målbild, process, system, teknik, informationsflöden, projekt, risker och ansvar i samma vy. Resultatet blir en bild som kanske innehåller mycket information, men som inte hjälper någon särskilt bra.

Ett bättre arbetssätt är att låta frågan styra vad som ska vara med.

| Modelleringsfråga | Trolig startpunkt | Ofta onödigt i första versionen |
|---|---|---|
| Vilka förmågor påverkas av en förändring? | Verksamhetsförmågor och förändringsinitiativ | Tekniska noder och detaljerade integrationer |
| Vilka applikationer stödjer ett verksamhetsområde? | Applikationer, applikationstjänster och verksamhetsförmågor | Fullständiga processflöden |
| Var finns risk för dubbelarbete? | Processer, roller, information och applikationer | Infrastrukturdetaljer |
| Vad krävs för att nå målarkitekturen? | Nuläge, målbild, gap och arbetspaket | Alla relationstyper i ArchiMate |
| Vilka beroenden påverkar prioritering? | Förmågor, applikationer, initiativ och relationer | Dekorativa symboler och teknisk implementation |

Poängen är inte att de bortvalda delarna aldrig behövs. Poängen är att de inte behövs först.

## Att formulera en bra modelleringsfråga

En bra modelleringsfråga är konkret nog för att styra arbetet, men öppen nog för att skapa insikt. Den bör helst innehålla fyra delar:

- vad som ska förstås,
- vilket område som avses,
- vem som ska använda svaret,
- vilket beslut eller vilken handling svaret ska stödja.

En svag fråga är:

> Hur ser importflödet ut?

En bättre fråga är:

> Vilka verksamhetsförmågor och applikationer är mest kritiska för att modernisera importflödet, så att programledningen kan prioritera första etappen?

Den bättre frågan ger vägledning. Den pekar ut förmågor, applikationer, modernisering, importflöde, programledning och prioritering. Den säger också något om vad som kan lämnas utanför.

## Modellens första avgränsning

När frågan är formulerad behöver modellen avgränsas. Avgränsning är inte ett misslyckande. Det är en förutsättning för att modellen ska bli användbar.

En första avgränsning kan göras med fem frågor:

1. Vilken verksamhetsförändring, förmåga eller beslutsfråga gäller modellen?
2. Vilka målgrupper ska använda modellen?
3. Vilka ArchiMate-lager behövs i första versionen?
4. Vilken detaljeringsnivå är tillräcklig för syftet?
5. Vilka delar ska uttryckligen lämnas utanför tills vidare?

För Atlantis modernisering av importflödet kan första avgränsningen vara:

- Område: importflödet från föranmälan till beslut.
- Målgrupp: programledning, verksamhetsarkitekter, IT-arkitekter och portföljstyrning.
- Lager: verksamhetslager, applikationslager och ett fåtal motivationsbegrepp.
- Detaljnivå: förmågor och centrala applikationstjänster, inte alla processteg.
- Utanför: teknisk infrastruktur, detaljerade informationsattribut och integrationsprotokoll.

Denna avgränsning gör modellen möjlig att skapa, diskutera och förbättra.

## När räcker en bild?

Det är viktigt att inte göra modellering till ett självändamål. Ibland är en bild rätt verktyg.

En bild kan räcka när:

- syftet är en engångspresentation,
- innehållet inte behöver återanvändas,
- det inte finns behov av analys eller spårbarhet,
- målgruppen bara behöver en förenklad förklaring,
- osäkerheten är hög och arbetet fortfarande är utforskande.

Exempel: Om generaldirektören behöver en enkel illustration av varför modernisering av importflödet är viktigt, kan en välgjord kommunikationsbild vara bättre än en ArchiMate-vy.

Men en modell är ofta bättre när:

- samma information ska användas i flera vyer,
- flera arkitekter behöver arbeta konsekvent,
- samband ska analyseras,
- förändringar ska följas över tid,
- beslut behöver spårbarhet,
- modellen ska överleva presentationen.

Exempel: Om Atlantis behöver se vilka applikationer som stödjer vilka förmågor, vilka initiativ som påverkar dem och vilka beroenden som finns mellan etapper, blir en modell mer värdefull än en enskild bild.

## Från första fråga till första vy

När modelleringsfrågan är tydlig kan du skapa en första vy. Vyn är inte hela modellen. Den är ett sätt att visa den del av modellen som behövs för ett visst samtal.

Ett enkelt arbetsflöde är:

1. Skriv modelleringsfrågan högst upp i arbetsmaterialet.
2. Identifiera målgruppen.
3. Lista 5–15 begrepp som sannolikt behöver vara med.
4. Välj vilka begrepp som ska bli ArchiMate-element.
5. Rita bara de relationer som behövs för frågan.
6. Testa vyn i ett samtal.
7. Justera modellen efter vad samtalet visar.

Detta arbetssätt gör modellen levande. Den börjar inte som en slutprodukt, utan som ett verktyg för bättre förståelse.

## Vanliga misstag

- **Misstag: Att börja med verktyget i stället för frågan.**
  - Varför det händer: Ritverktyg och modelleringsverktyg gör det lätt att börja producera symboler direkt.
  - Hur du undviker det: Skriv först modelleringsfrågan och målgruppen innan du skapar första elementet.

- **Misstag: Att försöka skapa en komplett modell från början.**
  - Varför det händer: Arkitekter vill ofta vara korrekta och heltäckande.
  - Hur du undviker det: Skapa en minimal användbar modell som svarar på en tydlig fråga och bygg ut den först när ny nytta kräver det.

- **Misstag: Att blanda flera frågor i samma vy.**
  - Varför det händer: Många intressenter vill få in sina perspektiv i samma bild.
  - Hur du undviker det: Skapa flera vyer från samma modell i stället för en överlastad vy.

- **Misstag: Att modellera för arkitekter men säga att modellen är för beslutsfattare.**
  - Varför det händer: Arkitekter kan omedvetet skapa vyer som passar deras egen förståelse.
  - Hur du undviker det: Testa vyn med den faktiska målgruppen och ta bort sådant som inte hjälper deras fråga.

- **Misstag: Att välja detaljeringsnivå efter vad som går att modellera.**
  - Varför det händer: ArchiMate och verktyg kan representera många typer av samband.
  - Hur du undviker det: Välj detaljeringsnivå efter vad som behövs för beslut, analys eller gemensam förståelse.

## Övningar

### Övning 1: Hitta frågan bakom bilden

Välj en arkitekturbild du nyligen har sett eller ritat. Svara på följande frågor:

1. Vilken fråga verkar bilden försöka besvara?
2. Vem är bilden egentligen till för?
3. Vilket beslut eller vilken handling ska bilden stödja?
4. Skulle samma innehåll behöva återanvändas i andra sammanhang?
5. Är detta främst en bild, en vy eller början på en modell?

### Övning 2: Formulera en bättre modelleringsfråga

Utgå från beställningen: “Vi behöver en bild över våra system.”

Skriv om den till tre bättre modelleringsfrågor:

1. En kommunikationsfråga.
2. En analysfråga.
3. En beslutsfråga.

Försök få med målgrupp och användning i varje fråga.

### Övning 3: Avgränsa Atlantis-modellen

Anta att Tullmyndigheten Atlantis ska modernisera importflödet. Gör en första avgränsning:

1. Vilket område ska modellen täcka?
2. Vilka två målgrupper är viktigast?
3. Vilka två ArchiMate-lager behövs först?
4. Vilka tre saker ska lämnas utanför första versionen?
5. Vilken vy skulle du skapa först?

### Fördjupning

Fundera på en modell i din egen organisation. Vilken återkommande fråga skulle göra den mer värdefull?

Exempel:

- “Vilka applikationer stödjer våra mest kritiska förmågor?”
- “Vilka förändringsinitiativ påverkar samma verksamhetsområde?”
- “Var är vi beroende av information som ägs av någon annan?”
- “Vilka tekniska beroenden hindrar oss från att avveckla ett system?”

Välj en fråga och beskriv vilken modellinformation som behövs för att besvara den.

## Snabb sammanfattning

- Modellering bör börja med en fråga, inte med symboler.
- En bra modelleringsfråga kopplar samman område, målgrupp och användning.
- Kommunikationsfrågor, analysfrågor och beslutsfrågor kräver olika nivå av modellstruktur.
- En bild kan räcka för engångskommunikation, men en modell behövs när information ska återanvändas, analyseras och följas över tid.
- Avgränsning är en styrka. Den hjälper dig skapa en minimal användbar modell.
- I Tullmyndigheten Atlantis blir importflödet ett exempel på hur modellering kan gå från “rita en bild” till “stöd ett beslut”.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan ett ritbehov och ett förståelsebehov?
2. Varför är det riskabelt att börja modellering med verktyget?
3. När kan en enkel bild vara bättre än en modell?
4. Vad kännetecknar en bra modelleringsfråga?
5. Hur kan samma modell ge olika vyer till olika målgrupper?

## Nästa steg

Nu har vi sett hur frågan styr modellen. I nästa kapitel går vi vidare till ArchiMate som språk. Där tittar vi på hur element, relationer, lager och vyer hjälper oss att uttrycka modelleringsfrågor på ett mer konsekvent sätt, utan att ArchiMate blir ett mål i sig.
