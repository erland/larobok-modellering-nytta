# Kapitel 3: ArchiMate som språk, inte som mål i sig

## Varför detta kapitel finns

De två första kapitlen har handlat om varför modellering behövs och hur man börjar med en tydlig fråga. Nu är det dags att introducera ArchiMate, men med en viktig varning: ArchiMate är inte poängen med arbetet.

Poängen är inte att skapa en modell som innehåller så många ArchiMate-element som möjligt. Poängen är att använda ett gemensamt språk så att arkitekter, verksamhetsrepresentanter, ledning, utveckling, säkerhet och förvaltning kan prata om samma verklighet utan att varje bild behöver tolkas från början.

I Tullmyndigheten Atlantis finns många arkitekturbilder redan. Det finns systemkartor, processbilder, målarkitekturer, flödesbilder och PowerPoint-bilder från olika projekt. Vissa är användbara i enskilda möten, men de är svåra att koppla ihop. När någon frågar vilka applikationer som stödjer importflödets viktigaste förmågor, eller vilka verksamhetsmål som påverkas av ett visst förändringsinitiativ, räcker bilderna ofta inte till.

ArchiMate kan hjälpa till här, men bara om språket används med omdöme. Ett språk hjälper oss att skilja på saker som annars blandas ihop. Det hjälper oss också att skapa relationer mellan sakerna. Men ett språk kan också bli tungt, främmande och överdrivet om man försöker använda allt på en gång.

Det här kapitlet visar därför ArchiMate som ett praktiskt modelleringsspråk: tillräckligt strukturerat för att ge nytta, men inte som ett självändamål.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför ArchiMate bör ses som ett språk snarare än som ett ritbibliotek,
- skilja mellan element, relationer, lager och vyer,
- förstå hur ArchiMate kan ge mer nytta än fristående bilder,
- välja en liten och användbar startmängd av ArchiMate-begrepp,
- beskriva när ArchiMate bör förenklas för målgruppen,
- undvika vanliga misstag där språket blir viktigare än modellnyttan.

## Innan vi börjar

I kapitel 1 skilde vi mellan bild och modell. En bild kan vara användbar för ett samtal, men den bär inte alltid en tydlig underliggande struktur. I kapitel 2 började vi med modelleringsfrågan: vad ska modellen hjälpa oss att förstå?

ArchiMate kommer in först efter dessa två steg. Det är ett svar på frågan: vilket gemensamt språk behöver vi för att uttrycka modellen på ett konsekvent sätt?

Det betyder att en bra ArchiMate-modell inte börjar med en stencil eller en symbolpalett. Den börjar med ett behov:

- Vilka saker behöver vi skilja på?
- Vilka samband behöver vi följa?
- Vilka vyer behöver olika målgrupper?
- Vilka beslut eller analyser ska modellen stödja?
- Vilken detaljeringsnivå räcker?

När dessa frågor är tydliga blir ArchiMate ett hjälpmedel. När de är otydliga riskerar ArchiMate att bli ännu ett sätt att producera svårtolkade bilder.

## ArchiMate i en mening

ArchiMate är ett standardiserat modelleringsspråk för enterprise architecture. Det ger begrepp och relationer för att beskriva arkitektur över flera delar av en organisation, till exempel verksamhet, applikationer, teknik, mål, krav och förändring.

Det viktigaste i den meningen är inte “standardiserat”. Det viktigaste är “språk”.

Ett språk gör tre saker:

1. Det ger namn åt saker.
2. Det ger regler för hur saker kan kopplas ihop.
3. Det gör det möjligt för flera personer att förstå och återanvända samma uttryck.

När en arkitekt ritar en ruta med texten “Importsystemet” kan rutan betyda flera olika saker. Den kan betyda ett system, en applikation, ett verksamhetsområde, ett projekt, ett användargränssnitt eller en teknisk plattform. I ett vanligt möte kan deltagarna kanske reda ut detta muntligt. I en modell som ska återanvändas senare räcker det inte.

I ArchiMate behöver vi bestämma vad rutan är. Är det en applikationskomponent? Är det en applikationstjänst? Är det en verksamhetstjänst? Är det en tekniktjänst? Är det ett arbetspaket? Valet avgör hur elementet kan relateras till andra element och vilken analys modellen kan stödja.

## Språk, notation och modell

Det är lätt att blanda ihop tre saker:

- **Språket**: begreppen och reglerna.
- **Notationen**: hur begreppen visas visuellt.
- **Modellen**: den strukturerade representationen av det vi beskriver.

ArchiMate innehåller både språk och notation. Men när vi arbetar praktiskt är modellen viktigare än hur symbolerna råkar se ut i ett visst verktyg.

Tänk på Tullmyndigheten Atlantis. En arkitekt kan rita en bild där “Riskanalys” är en blå ruta, “Ärendehantering” en grön ruta och “Kontrollbeslut” en orange ruta. Bilden kan se tydlig ut. Men om färgerna bara betyder något i arkitektens huvud går betydelsen förlorad när någon annan ska använda bilden.

I en ArchiMate-modell kan vi i stället bestämma att:

- “Riskanalys” är en verksamhetsförmåga.
- “Ärendehantering” är en applikationskomponent.
- “Kontrollbeslut” är ett verksamhetsobjekt eller ett resultat av en verksamhetsprocess, beroende på vad vi behöver analysera.

Det betyder inte att varje samtal måste innehålla ArchiMate-termer. Det betyder att modellen bakom samtalet har en tydligare struktur.

## Element: modellens byggstenar

Ett element är en modellerad sak. Det kan vara något verksamhetsnära, något tekniskt, något strategiskt eller något förändringsrelaterat.

Exempel på element i Atlantis kan vara:

- verksamhetsförmågan “Hantera importdeklaration”,
- verksamhetsprocessen “Genomföra dokumentkontroll”,
- applikationskomponenten “Deklarationssystemet”,
- applikationstjänsten “Ta emot importdeklaration”,
- målet “Minska manuell handläggningstid”,
- kravet “Beslut ska kunna motiveras i efterhand”,
- arbetspaketet “Modernisera importflödet”.

Det viktiga är att varje element representerar något som modellen behöver hålla reda på. Ett element ska inte finnas med bara för att det finns i verkligheten. Det ska finnas med för att det behövs för modellens fråga.

Om frågan är vilka applikationer som påverkas av en förändring i importflödet, behöver vi kanske modellera applikationskomponenter och deras koppling till verksamhetsprocesser. Om frågan är hur en strategisk målsättning bryts ner i förändringsinitiativ, behöver vi modellera mål, krav, principer och arbetspaket.

Ett vanligt misstag är att försöka skapa en komplett katalog över allt. Det låter ambitiöst, men leder ofta till en modell som är för stor för att förvalta och för oklar för att användas. Börja i stället med de element som behövs för en faktisk fråga.

## Relationer: där betydelsen uppstår

Element utan relationer är mest en lista. Relationerna visar varför elementen hör ihop.

I en vanlig bild kan en linje betyda nästan vad som helst. Den kan betyda beroende, informationsflöde, ansvar, ägarskap, teknisk integration, användning eller påverkan. I mötet kanske det går att förklara muntligt. I en modell behöver relationen bära mer betydelse.

ArchiMate har olika relationstyper för olika slags samband. I en praktisk start behöver läsaren inte kunna alla. Det viktiga är att förstå att relationens betydelse påverkar modellens användbarhet.

I Atlantis kan vi behöva uttrycka att:

- en verksamhetsprocess använder en applikationstjänst,
- en applikationskomponent realiserar en applikationstjänst,
- ett krav påverkar utformningen av en lösning,
- ett arbetspaket realiserar en del av en målarkitektur,
- en förmåga betjänar ett verksamhetsbehov,
- en informationsmängd flödar mellan två delar av organisationen.

Skillnaden mellan dessa samband är inte akademisk. Den avgör vilka frågor modellen kan besvara.

Om vi bara ritar en pil mellan “Importprocess” och “Deklarationssystemet” vet vi inte om pilen betyder att processen använder systemet, att systemet stödjer processen, att data flödar från processen, att processen ska ersätta systemet eller att systemet orsakar problem i processen.

När relationer modelleras mer konsekvent kan modellen användas för analys:

- Vad påverkas om applikationen tas bort?
- Vilka processer saknar tydligt applikationsstöd?
- Vilka krav realiseras inte av något initiativ?
- Vilka mål saknar koppling till pågående förändring?
- Var finns beroenden mellan verksamhet, applikation och teknik?

Därför är relationer ofta viktigare än symboler. Symbolen säger vad något är. Relationen säger varför det spelar roll.

## Lager och domäner: ett sätt att minska sammanblandning

ArchiMate organiserar arkitekturbeskrivningar i olika områden. I praktiskt arbete talar många fortfarande om lager, till exempel verksamhet, applikation och teknik. I nyare ArchiMate-sammanhang förekommer också begrepp som domäner. Oavsett terminologi är den pedagogiska poängen densamma: vi behöver skilja mellan olika slags verklighet.

För en myndighet som Atlantis är detta särskilt viktigt eftersom samma ord ofta används på flera nivåer.

Ordet “tjänst” kan till exempel betyda:

- en tjänst som myndigheten erbjuder en extern aktör,
- en funktion som en applikation tillhandahåller,
- en teknisk tjänst i infrastrukturen,
- en intern organisatorisk service.

Om allt kallas “tjänst” utan precisering blir samtalet snabbt otydligt. ArchiMate hjälper oss att fråga: vilken typ av tjänst menar vi?

Ett praktiskt sätt att tänka är:

- **Verksamhetsområdet** beskriver aktörer, roller, förmågor, processer, tjänster och verksamhetsobjekt.
- **Applikationsområdet** beskriver applikationer, applikationstjänster, gränssnitt och applikationsdata.
- **Teknikområdet** beskriver tekniska plattformar, noder, systemprogramvara, nätverk och tekniktjänster.
- **Motivationsområdet** beskriver mål, drivkrafter, krav, principer och intressenter.
- **Implementations- och migrationsområdet** beskriver förändring över tid, till exempel arbetspaket, leveranser och platåer.

Den här boken använder dessa områden som praktiska orienteringspunkter. Vi kommer inte att försöka använda allt på en gång. I stället kommer vi att välja det område som bäst svarar mot modelleringsfrågan.

## Vyer: modellen möter målgruppen

En modell kan innehålla mer än vad någon enskild målgrupp behöver se. Därför behövs vyer.

En vy är en målgruppsanpassad presentation av delar av modellen. Den kan vara enkel, pedagogisk och visuellt ren, men den bör fortfarande bygga på en underliggande modell.

I Atlantis kan samma modell ge olika vyer:

- Ledningen behöver se vilka strategiska mål och risker som påverkas av moderniseringen.
- Verksamhetsansvariga behöver se vilka förmågor och processer som förändras.
- IT-arkitekter behöver se applikationsberoenden.
- Säkerhetsansvariga behöver se informationsflöden och zoner.
- Programledningen behöver se arbetspaket, beroenden och övergångar.

Om varje målgrupp får en separat fristående bild uppstår snart problem. Begrepp får olika namn. System ritas på olika sätt. Samband saknas i en vy men finns i en annan. När något ändras måste flera bilder uppdateras manuellt.

Med en modellbaserad ansats kan flera vyer bygga på samma underliggande element och relationer. Det betyder inte att verktyget löser allt automatiskt. Det betyder att arkitekterna kan arbeta mer konsekvent och minska dubbelarbete.

En bra vy ska inte visa allt modellen vet. Den ska visa det målgruppen behöver för sin fråga.

## ArchiMate betyder inte att alla måste prata ArchiMate

En vanlig invändning är att verksamhetsrepresentanter inte vill lära sig ArchiMate. Det är en rimlig invändning. De ska oftast inte behöva göra det.

ArchiMate är i första hand ett språk för den underliggande arkitekturbeskrivningen. Vyerna kan däremot anpassas. I en ledningsvy kan elementnamn, layout, färger och förklaringar göras begripliga utan att målgruppen behöver kunna alla symboler.

Det betyder att arkitekten har två ansvar:

1. Modellen ska vara tillräckligt korrekt för att vara återanvändbar.
2. Vyn ska vara tillräckligt begriplig för målgruppen.

Om arkitekten visar en fullständig ArchiMate-vy för en målgrupp som bara behöver förstå konsekvenserna av ett beslut, har arkitekten kanske använt språket korrekt men kommunikationen fel.

I praktiken kan man därför behöva två nivåer:

- en arbetsvy för arkitekter, där ArchiMate-semantiken är tydlig,
- en kommunikationsvy för beslutsfattare eller verksamhet, där samma modell presenteras enklare.

Det är inte fusk. Det är god modellering.

## Atlantis-exempel: från rörig systembild till enkel modellstruktur

Anta att Atlantis har en befintlig bild över importflödet. Bilden visar:

- importdeklaration,
- riskanalys,
- ärendehandläggning,
- dokumentkontroll,
- deklarationssystem,
- kontrollsystem,
- integrationsplattform,
- extern informationskälla,
- beslutsmeddelande till företag.

Allt ligger på samma bild. Pilarna betyder lite olika saker. Några rutor är processer, några är system, några är informationsobjekt och några är externa aktörer. Bilden fungerar i ett projektmöte eftersom deltagarna redan känner sammanhanget. Men den är svår att återanvända.

En första modellering behöver inte göra allt. Den kan börja med fyra frågor:

1. Vilka delar är verksamhetsprocesser eller förmågor?
2. Vilka delar är applikationer eller applikationstjänster?
3. Vilka delar är information eller verksamhetsobjekt?
4. Vilka samband behöver vi kunna följa?

Då kan arkitekten börja strukturera bilden:

- “Genomföra riskanalys” modelleras som verksamhetsprocess eller förmåga, beroende på frågan.
- “Deklarationssystemet” modelleras som applikationskomponent.
- “Riskanalystjänst” modelleras som applikationstjänst om den är något applikationen tillhandahåller.
- “Importdeklaration” modelleras som verksamhetsobjekt eller dataobjekt beroende på nivå.
- “Företag” modelleras som extern verksamhetsaktör.
- “Beslutsmeddelande” modelleras som informationsobjekt eller flöde, beroende på analysbehov.

Redan denna enkla struktur ger nytta. Vi kan se vad som är verksamhet, vad som är applikation och vad som är information. Vi kan också börja skapa tydligare relationer: processen använder en applikationstjänst, applikationskomponenten realiserar tjänsten, information flödar mellan aktörer och system.

Det här är fortfarande inte en komplett modell. Men den är mer användbar än en bild där allt betyder allt.

## En liten startmängd räcker långt

För en organisation som börjar modellera är det klokt att begränsa språket. Ett vanligt införandemisstag är att ge arkitekterna hela ArchiMate-paletten och hoppas att allt blir konsekvent. Resultatet blir ofta motsatsen: olika arkitekter väljer olika element för samma sak.

En bättre start är en överenskommen startmängd.

För Atlantis kan en första startmängd vara:

| Område | Startbegrepp | Typisk användning |
|---|---|---|
| Verksamhet | Aktör, roll, förmåga, process, verksamhetstjänst, verksamhetsobjekt | För att beskriva vad myndigheten gör och för vem |
| Applikation | Applikationskomponent, applikationstjänst, applikationsgränssnitt, dataobjekt | För att beskriva applikationsstöd och informationshantering |
| Motivation | Mål, krav, princip, intressent | För att koppla modellen till varför förändring behövs |
| Förändring | Arbetspaket, leverans, platå | För att beskriva förändring över tid |
| Relationer | Använder, realiserar, flödar, består av, påverkar | För att skapa spårbarhet och analysbarhet |

Den exakta startmängden kan variera. Poängen är att den ska vara liten nog att användas konsekvent och bred nog att svara på de första viktiga frågorna.

Startmängden bör dokumenteras i organisationens modellprinciper. Där bör det också framgå vad man ännu inte använder och varför.

## När ArchiMate ska förenklas

ArchiMate ska förenklas när full precision inte ger motsvarande nytta.

Det kan gälla när:

- målgruppen behöver förstå beslutet snarare än modellen,
- frågan är tidig och utforskande,
- detaljerna är osäkra,
- modellen används för workshop och gemensam förståelse,
- organisationen ännu saknar vana att läsa modeller,
- precisionen skulle skapa mer diskussion om notation än om sakfrågan.

Förenkling betyder inte att man slutar modellera. Det betyder att man gör medvetna val.

Exempel:

- Använd få elementtyper i en första vy.
- Dölj relationstyper i en kommunikationsvy men behåll dem i modellen.
- Visa bara de viktigaste beroendena.
- Använd begriplig namngivning även om den inte är perfekt.
- Separera arbetsvyer från beslutsvyer.
- Lägg detaljer i modellen men visa dem inte för alla.

Det avgörande är att förenklingen är avsiktlig. Om man förenklar utan att veta vad man förenklar bort blir modellen svagare. Om man förenklar medvetet blir modellen mer användbar.

## När ArchiMate inte behövs

ArchiMate är inte alltid rätt verktyg.

Det kan räcka med en enkel bild när:

- syftet är att snabbt tänka tillsammans,
- bilden inte ska återanvändas,
- inga samband behöver följas över tid,
- målgruppen bara behöver en tillfällig lägesbild,
- det inte finns någon förväntan på analys eller spårbarhet.

Det är viktigt att säga detta tydligt. En organisation som tror att alla bilder måste bli ArchiMate-modeller riskerar att göra modellering till en börda.

Frågan är inte: “Kan detta ritas i ArchiMate?”

Frågan är: “Behöver detta vara en modell?”

Om svaret är nej kan en skiss vara bättre. Om svaret är ja bör man använda ett språk och ett arbetssätt som gör modellen hållbar.

## När ArchiMate verkligen hjälper

ArchiMate hjälper särskilt när en organisation behöver hantera samband över gränser.

I Atlantis blir språket användbart när frågor spänner över flera områden:

- Hur hänger strategin om ökad automatisering ihop med faktiska applikationsförändringar?
- Vilka processer påverkas om riskanalysplattformen byts ut?
- Vilka informationsflöden korsar organisatoriska gränser?
- Vilka applikationstjänster är kritiska för rättssäker handläggning?
- Vilka krav saknar tydlig realisering i pågående initiativ?
- Vilka beroenden behöver portföljstyrningen förstå innan finansiering beslutas?

Dessa frågor är svåra att besvara med enstaka bilder. De kräver att element och relationer kan återanvändas i flera vyer. De kräver också att arkitekter menar samma sak med samma begrepp.

Det är här ArchiMate kan skapa nytta: inte genom att göra bilderna mer avancerade, utan genom att göra arkitekturbeskrivningen mer sammanhängande.

## Praktisk beslutsregel

En användbar regel är:

> Använd ArchiMate när du behöver att flera personer, över tid, ska kunna förstå, återanvända eller analysera samma arkitekturbeskrivning.

En annan regel är:

> Välj inte ett ArchiMate-element för att det finns i paletten. Välj det för att det hjälper dig skilja på något som annars skulle blandas ihop.

Dessa två regler skyddar mot två motsatta misstag. Det första misstaget är att fortsätta rita otydliga bilder trots att organisationen behöver modellnytta. Det andra misstaget är att använda ArchiMate så tungt att arbetet tappar fart och förtroende.

## Vanliga misstag

- **Misstag: Att börja med hela ArchiMate-språket.**
  - Varför det händer: Det känns seriöst att visa alla möjligheter från början.
  - Hur du undviker det: Börja med en liten startmängd som svarar mot de första modelleringsfrågorna.

- **Misstag: Att tro att korrekt notation automatiskt ger nytta.**
  - Varför det händer: Det är lättare att kontrollera symboler än att kontrollera om modellen används i beslut.
  - Hur du undviker det: Koppla varje modell till en fråga, målgrupp och användningssituation.

- **Misstag: Att visa för mycket ArchiMate för fel målgrupp.**
  - Varför det händer: Arkitekten vill vara transparent med hela modellen.
  - Hur du undviker det: Skapa målgruppsanpassade vyer som bygger på modellen men inte visar allt.

- **Misstag: Att använda linjer utan betydelse.**
  - Varför det händer: I vanliga bilder används pilar ofta som allmänna samband.
  - Hur du undviker det: Bestäm vilken relationstyp som behövs, eller skriv tydligt att sambandet ännu är oklassificerat.

- **Misstag: Att modellera allt som finns.**
  - Varför det händer: Organisationen vill skapa en komplett arkitekturbas.
  - Hur du undviker det: Modellera först det som behövs för en konkret analys, förändring eller beslutssituation.

- **Misstag: Att göra ArchiMate till en expertklubb.**
  - Varför det händer: Språket kan uppfattas som tekniskt och internt.
  - Hur du undviker det: Håll modellen strukturerad men gör vyer och förklaringar begripliga för målgruppen.

## Övningar

### Övning 1: Sortera en bild

Ta en befintlig arkitekturbild från din organisation, eller föreställ dig en bild över Atlantis importflöde. Lista rutorna i bilden och markera vad varje ruta egentligen verkar vara:

- verksamhetsförmåga,
- verksamhetsprocess,
- applikation,
- applikationstjänst,
- information,
- teknisk komponent,
- mål eller krav,
- förändringsinitiativ,
- oklart.

Reflektera sedan över vilka rutor som blandar flera betydelser.

### Övning 2: Hitta relationernas betydelse

Välj tre pilar eller linjer i samma bild. Skriv vad varje pil betyder.

Exempel:

- använder,
- realiserar,
- skickar information till,
- består av,
- påverkar,
- ansvarar för,
- är beroende av.

Markera vilka pilar som inte går att tolka utan muntlig förklaring.

### Övning 3: Skapa en startmängd

Föreslå en första ArchiMate-startmängd för Atlantis om målet är att förstå moderniseringen av importflödet. Begränsa dig till högst tio elementtyper och fem relationstyper.

Förklara varför du valde just dessa.

### Fördjupning

Jämför två möjliga sätt att modellera “riskanalys” i Atlantis:

1. Som verksamhetsförmåga.
2. Som verksamhetsprocess.
3. Som applikationstjänst.

När är respektive val rimligt? Vilka frågor kan modellen besvara med varje val? Vilka risker uppstår om man väljer fel nivå?

## Praktisk versionshållning

I boken behandlas ArchiMate 4 som huvudversion, men Atlantis behöver inte börja sitt arbete med att diskutera varje skillnad mellan versioner. För en myndighet som redan har modeller, verktyg eller mallar från ArchiMate 3.x är den praktiska frågan snarare:

- Vilka modellbegrepp använder vi redan på ett konsekvent sätt?
- Vilka begrepp behöver vi lägga till för att få bättre spårbarhet?
- Vilka vyer och relationer ska vara gemensamma i myndigheten?
- När behöver vi kontrollera en detalj mot den officiella specifikationen?

Det viktiga i början är inte att varje arkitekt kan hela specifikationen. Det viktiga är att organisationen väljer ett litet antal begrepp och relationer som används likadant i flera sammanhang.

## Snabb sammanfattning

- ArchiMate ska ses som ett modelleringsspråk, inte som ett mål i sig.
- Ett språk hjälper oss att ge namn åt saker, skapa tydliga relationer och återanvända modellen.
- Element beskriver vad modellen håller reda på.
- Relationer beskriver varför elementen hör ihop.
- Vyer gör modellen begriplig för olika målgrupper.
- En liten och gemensam startmängd är ofta bättre än att använda hela språket från början.
- ArchiMate behövs inte för alla bilder, men är värdefullt när samband behöver förstås, återanvändas och analyseras över tid.
- God modellering innebär att vara tillräckligt precis i modellen och tillräckligt begriplig i vyn.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan ArchiMate som språk och ArchiMate som notation?
2. Varför är relationer ofta viktigare än symboler i en arkitekturmodell?
3. När kan en enkel skiss vara bättre än en ArchiMate-modell?
4. Vad är risken med att införa hela ArchiMate-paletten från början?
5. Hur kan samma modell användas för både arkitekter och beslutsfattare?
6. Vilka ArchiMate-begrepp skulle du välja först för att modellera ett myndighetsövergripande förändringsinitiativ?

## Nästa steg

Nu har vi placerat ArchiMate i rätt roll: ett språk som hjälper oss att skapa tydligare och mer återanvändbara modeller. Nästa kapitel går vidare till modellnytta i en myndighetskontext.

Där kommer vi att titta närmare på varför större myndigheter har särskilda behov av gemensamma modeller: många intressenter, stark regelstyrning, långa livscykler, komplexa beroenden, samverkan med andra organisationer och höga krav på spårbarhet.
