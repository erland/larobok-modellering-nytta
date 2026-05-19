# Kapitel 8: Motivation och strategi: att koppla modeller till varför

## Varför detta kapitel finns

Hittills har boken visat hur modeller kan beskriva verksamhet, applikationer och teknik. Det är nödvändigt, men inte tillräckligt. En arkitekturmodell som bara visar vad som finns riskerar att bli en avancerad inventering. För att modellen ska göra nytta i styrning, prioritering och förändringsarbete behöver den också kunna visa varför något behöver förändras.

Det är här motivation och strategi blir viktiga. De hjälper oss att koppla arkitekturmodellen till mål, drivkrafter, principer, krav och strategiska vägval. I en större myndighet är detta särskilt viktigt eftersom förändring sällan motiveras av teknik i sig. Förändring motiveras av uppdrag, lagkrav, politiska prioriteringar, effektivitet, säkerhet, rättssäkerhet, service, riskhantering eller behovet av bättre samverkan.

I Tullmyndigheten Atlantis finns många bilder över system, processer och informationsflöden. Men när ledningen frågar varför ett visst moderniseringsinitiativ är viktigt blir svaren ofta blandade:

- “Systemet är gammalt.”
- “Processen är manuell.”
- “Verksamheten vill ha bättre stöd.”
- “Det finns nya krav på informationsutbyte.”
- “Vi behöver öka automatiseringen.”
- “Riskanalysen behöver bli träffsäkrare.”

Alla påståenden kan vara sanna, men de betyder olika saker. Några är problem, några är mål, några är drivkrafter, några är krav och några är möjliga lösningar. Om modellen inte skiljer på dem blir det svårt att förstå vad som faktiskt motiverar förändringen.

Det här kapitlet visar hur motivation och strategi kan användas för att göra arkitekturmodellen mer beslutsnära. Målet är inte att modellera varje styrdokument eller varje formulering i en verksamhetsplan. Målet är att kunna koppla förändringar i verksamhet, applikationer och teknik till de skäl som gör förändringen viktig.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara varför en arkitekturmodell behöver kunna visa varför något förändras,
- skilja mellan drivkraft, mål, krav, princip och begränsning,
- använda motivationselement för att koppla modellering till styrning och beslut,
- avgöra när strategi- och motivationselement tillför nytta och när de skapar onödig tyngd,
- formulera enkla modelleringsfrågor som binder ihop mål, förmågor, initiativ och lösningar,
- undvika vanliga misstag där mål, krav, lösningar och önskelistor blandas ihop.

## Innan vi börjar

Du behöver inte kunna alla ArchiMate-begrepp för motivation och strategi för att få nytta av det här kapitlet. Det viktiga är att förstå rollen dessa delar spelar i modellen.

I tidigare kapitel har vi arbetat med:

- verksamhetsförmågor,
- processer,
- verksamhetstjänster,
- applikationer,
- applikationstjänster,
- teknikberoenden,
- relationer mellan olika delar av modellen.

Nu lägger vi till ett lager av frågor som ligger före eller ovanför dessa delar:

- Varför behöver något förändras?
- Vilket mål stöder förändringen?
- Vilken drivkraft gör frågan aktuell?
- Vilka principer ska styra vägvalet?
- Vilka krav måste lösningen uppfylla?
- Vilka förmågor behöver stärkas?
- Vilka initiativ bidrar faktiskt till målet?

Det är lätt att hoppa direkt från problem till lösning. Motivation och strategi hjälper oss att stanna upp och modellera sambanden däremellan.

## Huvudförklaring

### Varför räcker det inte att modellera nuläget?

En nulägesmodell kan vara mycket värdefull. Den kan visa vad som finns, hur det hänger ihop och vilka beroenden som redan är kända. Men när organisationen ska prioritera förändring behöver nuläget kopplas till skälen för förändring.

Anta att Atlantis har en modell som visar att Importportalen, Ärendehanteringssystemet och Riskanalysplattformen är centrala i importflödet. Det är användbart. Men det svarar inte automatiskt på frågor som:

- Varför ska importflödet moderniseras nu?
- Vilken nytta är viktigast: snabbare handläggning, bättre riskanalys, ökad spårbarhet eller minskad manuell hantering?
- Vilka krav är tvingande och vilka är önskemål?
- Vilka tekniska begränsningar får inte styra mer än de borde?
- Vilket initiativ bidrar mest till myndighetens mål?

Utan koppling till motivation riskerar modellen att beskriva en komplex värld utan att visa vad som är viktigt. Den kan då bli korrekt men svår att använda i beslut.

En beslutsnära modell behöver därför kunna visa både struktur och avsikt:

- struktur: vad som finns och hur det hänger ihop,
- avsikt: varför något behöver förändras och vilken effekt förändringen ska ge.

### Motivation handlar om skälen bakom förändring

Motivationselement används för att beskriva det som driver, begränsar eller rättfärdigar förändring. I praktiken kan de hjälpa arkitekter att skilja mellan flera olika typer av påståenden.

En drivkraft beskriver något som gör frågan relevant. Det kan vara en ny lag, ett förändrat hotläge, ökade volymer, politiska uppdrag, ekonomisk press eller krav på bättre service.

Ett mål beskriver ett önskat tillstånd eller en önskad effekt. Det kan vara att öka automatiseringsgraden i importflödet, minska ledtider eller förbättra träffsäkerheten i riskurvalet.

Ett krav beskriver något som måste uppfyllas. Det kan komma från lagstiftning, säkerhet, verksamhetsbehov, arkitekturprinciper eller tekniska förutsättningar.

En princip uttrycker en regel eller riktning som ska vägleda beslut. Det kan till exempel vara att gemensamma tjänster ska återanvändas före lokala lösningar, eller att information ska registreras en gång och användas flera gånger.

En begränsning beskriver något som inskränker handlingsutrymmet. Det kan vara budget, tid, tekniskt arv, säkerhetsklassning eller beroenden till externa parter.

Dessa begrepp låter teoretiska, men de löser ett praktiskt problem: de gör det möjligt att föra mer precisa samtal om varför en förändring behövs.

### Strategi handlar om riktning och förmåga

Strategi i modellering handlar inte om att skriva en strategiplan i modellen. Det handlar om att visa hur organisationens riktning påverkar arkitekturen.

I Atlantis kan en strategisk riktning vara att öka digital självbetjäning för näringslivet. Den riktningen påverkar flera delar av arkitekturen:

- verksamhetsförmågan att ta emot digitala deklarationer,
- applikationstjänster för ärendeinlämning och statusåterkoppling,
- informationsutbyte med andra myndigheter,
- tekniska tjänster för säker åtkomst och spårbarhet,
- initiativ för att avveckla manuella moment.

När strategin bara finns i dokument och presentationer är det ofta svårt att se vilka delar av arkitekturen som faktiskt påverkas. När strategiska riktningar kopplas till förmågor, tjänster, applikationer och initiativ blir det lättare att se om förändringsportföljen hänger ihop.

Det betyder inte att varje strategiformulering ska modelleras. Det betyder att de strategiska begrepp som styr arkitekturval bör få en plats i modellen när de behövs.

### En praktisk kedja från varför till vad

Ett användbart sätt att börja är att tänka i en enkel kedja:

- Drivkraft: Varför är frågan aktuell?
- Mål: Vilken effekt vill vi uppnå?
- Förmåga: Vad behöver myndigheten kunna göra bättre?
- Förändring: Vilka initiativ eller arbetspaket bidrar?
- Lösning: Vilka verksamhets-, applikations- och teknikdelar påverkas?
- Mått eller kontrollfråga: Hur vet vi om det blev bättre?

Kedjan är inte en fullständig metod, men den hjälper till att undvika två vanliga problem.

Det första problemet är att börja med lösningen. Då blir modellen ett försvar för ett redan valt system eller projekt.

Det andra problemet är att stanna vid målformuleringar. Då blir modellen en snygg strategibild utan koppling till faktisk förändring.

En nyttig modell binder ihop båda ändarna.

### Vad som ofta blandas ihop

I organisationer som är vana att rita bilder blandas flera saker ofta i samma ruta:

- mål,
- problem,
- krav,
- lösningar,
- projekt,
- organisatoriska önskemål,
- tekniska begränsningar,
- arkitekturprinciper.

Det gör bilden snabb att skapa men svår att använda. När någon säger “vi behöver en ny importplattform” kan det betyda minst fem olika saker:

- ett mål: importhanteringen ska bli snabbare,
- ett krav: nya informationsutbyten måste stödjas,
- en lösning: en ny plattform ska införas,
- ett problem: nuvarande lösning är svår att förvalta,
- en princip: gemensamma plattformar ska användas före lokala system.

Modellering hjälper genom att tvinga fram frågan: vilken typ av påstående är detta?

Det kan kännas långsamt i början, men det sparar tid senare. När påståendena skiljs åt blir det lättare att se om lösningen verkligen möter målet, om kravet är tvingande eller förhandlingsbart, och om begränsningen är faktisk eller bara historisk.

## Atlantis-exempel: varför ska importflödet moderniseras?

Atlantis har ett program för att modernisera importflödet. Programmet har vuxit fram under flera år. Olika delar av organisationen beskriver syftet på olika sätt.

Verksamheten säger att manuell handläggning tar för lång tid. IT-förvaltningen säger att flera centrala system har teknisk skuld. Ledningen säger att myndigheten behöver bättre riskbaserad kontroll. Juridikfunktionen säger att nya krav på spårbarhet och informationshantering måste mötas. Samverkansansvariga säger att informationsutbytet med andra myndigheter behöver bli mer robust.

Alla perspektiv är relevanta, men utan modell blir de lätt en lista av argument. En arkitekt kan börja göra detta modellerbart genom att skapa en enkel motivationsstruktur.

Drivkrafter:

- ökade importvolymer,
- krav på snabbare och mer rättssäker handläggning,
- behov av bättre riskurval,
- ökade krav på spårbar informationshantering,
- teknisk skuld i centrala importapplikationer.

Mål:

- minska manuell hantering i importflödet,
- förbättra träffsäkerheten i riskanalysen,
- öka spårbarheten från deklaration till beslut,
- göra informationsutbyte med andra myndigheter mer robust,
- minska beroendet av svårförvaltade äldre komponenter.

Principer:

- gemensamma applikationstjänster ska återanvändas där det är möjligt,
- information ska registreras en gång och återanvändas med tydligt ansvar,
- lösningar som påverkar rättssäkerhet ska kunna granskas och följas upp,
- nya integrationer ska gå via etablerad integrationsförmåga om inget starkt skäl talar emot.

Krav:

- beslut ska kunna spåras till underlag och regler,
- relevanta händelser i importflödet ska loggas,
- informationsutbyte ska följa fastställda säkerhetskrav,
- handläggare ska kunna se aktuell ärendestatus,
- externa aktörer ska få tydlig återkoppling om mottagna underlag.

Förmågor som påverkas:

- ta emot importunderlag,
- bedöma risk,
- fatta tullbeslut,
- genomföra kontroll,
- utbyta information med andra myndigheter,
- följa upp och granska ärenden.

Nu börjar modellen kunna svara på bättre frågor. Den visar inte bara att Importportalen och Riskanalysplattformen finns. Den visar varför de är viktiga i förändringen och vilka mål de förväntas bidra till.

## När motivation och strategi ger nytta

Motivation och strategi är särskilt användbart när modellen ska stödja prioritering, styrning eller förändringsportfölj.

Använd motivation och strategi när:

- flera initiativ konkurrerar om samma budget,
- det är oklart varför en förändring behövs,
- tekniska argument dominerar trots att frågan egentligen är verksamhetsstyrd,
- ledningen vill förstå hur initiativ bidrar till myndighetsmål,
- krav, mål och lösningar blandas ihop,
- arkitekturen behöver visa spårbarhet från uppdrag till lösning,
- förändringar måste motiveras över flera år eller budgetcykler.

I Atlantis är detta relevant när importmoderniseringen konkurrerar med andra initiativ, till exempel modernisering av exportflödet, ny kontrollplanering eller förbättrat informationsutbyte med brottsbekämpande myndigheter. Om alla initiativ presenteras som “viktiga” blir prioriteringen svår. Om de kopplas till mål, drivkrafter och förmågor blir diskussionen mer saklig.

## När du kan välja bort det

Motivation och strategi ska inte användas i varje liten modell. Ibland räcker det med en enkel verksamhets- eller applikationsvy.

Du kan ofta välja bort motivationselement när:

- syftet bara är att förklara ett lokalt nuläge,
- mål och krav redan är välkända och inte ifrågasatta,
- modellen används som tillfällig samtalsskiss,
- målgruppen inte behöver se varför utan bara vad som påverkas,
- detaljerna skulle göra vyn svårare att förstå.

Det viktiga är att skilja mellan modellen och vyn. Det kan vara klokt att ha motivationselement i modellen men inte visa dem i varje vy. En ledningsvy kan visa mål och förmågor. En teknisk arbetsvy kan dölja dem och fokusera på applikations- och teknikberoenden.

Frågan är inte om motivation alltid ska synas. Frågan är om modellen behöver koppla förändringen till varför.

## En liten startmängd

För en organisation som Atlantis är det sällan klokt att börja med hela motivations- och strategipaletten. En liten startmängd räcker långt.

En praktisk startmängd kan vara:

- drivkraft,
- mål,
- krav,
- princip,
- förmåga,
- initiativ eller arbetspaket,
- relationer som visar påverkan, realisering eller bidrag.

Med denna startmängd kan arkitekterna skapa enkla men användbara samband:

- en drivkraft påverkar ett mål,
- ett mål kräver att en förmåga stärks,
- ett initiativ bidrar till ett mål,
- ett krav styr en lösning,
- en princip begränsar eller vägleder val,
- en applikationstjänst stödjer en förmåga.

Det är bättre att använda få begrepp konsekvent än att använda många begrepp osäkert.

## Från strategibild till modell

Många organisationer har strategibilder. De kan vara användbara för kommunikation, men de har ofta tre begränsningar.

För det första är de ofta fristående. De går inte att koppla till konkreta förmågor, system eller initiativ.

För det andra är de ofta tvetydiga. En ruta kan representera ett mål, ett program, en princip eller en lösning beroende på vem som läser bilden.

För det tredje blir de snabbt gamla. När initiativ ändras uppdateras ofta inte sambanden till strategi och mål.

En modellbaserad strategi-vy behöver inte vara mer komplicerad än en vanlig bild. Skillnaden är att den bygger på typade element och relationer. Det gör att samma mål kan återanvändas i flera vyer, samma förmåga kan kopplas till flera initiativ och samma krav kan följas till flera lösningsdelar.

Det betyder att strategivyn inte bara är en presentationsbild. Den är ett fönster mot en modell.

## Praktiskt arbetssätt

När du ska modellera motivation och strategi i ett pågående arbete kan du använda sex steg.

1. Börja med beslutssituationen. Fråga vilket beslut modellen ska stödja.
2. Samla påståenden från styrdokument, intervjuer och befintliga bilder.
3. Sortera påståendena i drivkrafter, mål, krav, principer, begränsningar och lösningar.
4. Välj bara de påståenden som påverkar arkitekturvalen.
5. Koppla dem till förmågor, initiativ, applikationstjänster eller teknikberoenden.
6. Skapa en vy för målgruppen och dölj resten.

Steg 3 är ofta viktigast. Det är där arkitekturarbetet går från ordlista till analys. När gruppen tvingas sortera påståenden blir det tydligt vad man egentligen menar.

Exempel:

- “Vi behöver ökad automatisering” är troligen ett mål.
- “Deklarationsbeslut måste kunna följas upp” är troligen ett krav.
- “Vi ska återanvända gemensam integrationsplattform” är troligen en princip.
- “Nuvarande riskanalysplattform är svår att skala” är troligen en begränsning eller ett problem.
- “Inför ny analysmotor” är troligen en lösning eller ett initiativ.

Det spelar inte alltid någon roll att klassificeringen är perfekt från början. Det viktiga är att gruppen blir tydligare med vad som är vad.

## Vanliga misstag

- **Misstag: Att modellera alla mål i organisationen.**
  - Varför det händer: Strategidokument innehåller många formuleringar som verkar viktiga.
  - Hur du undviker det: Modellera bara mål som påverkar arkitekturval, prioriteringar eller spårbarhet.

- **Misstag: Att blanda mål och lösning.**
  - Varför det händer: Organisationer uttrycker ofta önskad effekt som ett redan valt system eller projekt.
  - Hur du undviker det: Fråga vilken effekt lösningen ska skapa innan du modellerar lösningen som svaret.

- **Misstag: Att låta motivation bli en separat modell.**
  - Varför det händer: Strategi och mål hanteras ofta av andra roller än de som modellerar system och processer.
  - Hur du undviker det: Koppla alltid mål, krav och principer till förmågor, initiativ eller lösningsdelar.

- **Misstag: Att visa all motivation i varje vy.**
  - Varför det händer: När något väl är modellerat vill man gärna visa att arbetet är gjort.
  - Hur du undviker det: Skapa målgruppsanpassade vyer. Ledningen behöver andra samband än en teknisk plattformsgrupp.

- **Misstag: Att behandla principer som dekoration.**
  - Varför det händer: Arkitekturprinciper skrivs ibland som allmänna ambitioner utan tydlig påverkan.
  - Hur du undviker det: Modellera principer bara när de faktiskt styr eller begränsar ett val.

- **Misstag: Att göra kravlistan till en kopia av kravhanteringsverktyget.**
  - Varför det händer: Det är frestande att samla allt på ett ställe.
  - Hur du undviker det: Modellera arkitekturrelevanta krav och länka vid behov till detaljerad kravhantering.

## Övningar

### Övning 1: Sortera påståenden

Utgå från följande påståenden från Atlantis:

1. Importflödet ska få kortare ledtider.
2. Nuvarande ärendehanteringssystem är svårt att förändra.
3. Beslut ska kunna spåras till underlag och regler.
4. Gemensam integrationsplattform ska användas där det är möjligt.
5. Myndigheten vill öka automatiseringsgraden.
6. En ny importportal ska införas.
7. Informationsutbyte med andra myndigheter behöver bli mer robust.
8. Riskurvalet ska bli mer träffsäkert.

Sortera varje påstående som drivkraft, mål, krav, princip, begränsning eller lösning. Det finns inte alltid ett enda rätt svar. Det viktiga är att motivera klassificeringen.

### Övning 2: Koppla mål till förmågor

Välj två av målen från övning 1. Koppla varje mål till minst två verksamhetsförmågor i Atlantis.

Exempel:

- Målet “öka automatiseringsgraden” kan kopplas till förmågorna ta emot importunderlag, bedöma risk och fatta tullbeslut.

Fundera sedan på vilka applikationstjänster som behöver stödja förmågorna.

### Övning 3: Skapa en enkel ledningsvy

Skissa en vy för en ledningsgrupp som ska förstå varför importmoderniseringen är viktig. Vyn får bara innehålla:

- högst tre drivkrafter,
- högst tre mål,
- högst fem förmågor,
- högst tre initiativ.

Skriv bredvid vyn vilka detaljer du valde bort och varför.

### Fördjupning

Välj ett verkligt eller fiktivt arkitekturinitiativ. Skriv först initiativet som en lösning, till exempel “inför ny plattform”. Skriv sedan om det till:

- en drivkraft,
- ett mål,
- ett krav,
- en princip,
- en berörd förmåga.

Jämför versionerna. Vilken formulering hjälper bäst i ett beslutssamtal?

## Små modellpåståenden för motivation och strategi

Motivationsmodeller blir starka när de binder samman ambition, krav och faktisk förändring. De bör därför inte stanna vid allmänna målformuleringar.

Exempel från Atlantis:

- Drivkraften **Ökad internationell handel** påverkar målet **Snabbare importklarering**.
- Målet **Bättre träffsäkerhet i riskurval** realiseras delvis genom kravet **Automatiserad riskbedömning före manuell granskning**.
- Principen **Information ska registreras en gång och återanvändas** styr utformningen av applikationstjänsten **Tillhandahåll deklarationsdata**.
- Kravet **Spårbar beslutsmotivering** påverkar både verksamhetsprocessen **Besluta i importärende** och applikationskomponenten **Beslutsstödsystem**.

När sådana samband finns i modellen kan diskussionen flyttas från lösa önskemål till spårbara avvägningar: vilket mål stöder detta krav, och vilka delar av arkitekturen påverkas?

## Snabb sammanfattning

- Motivation och strategi kopplar modellen till varför något behöver förändras.
- Nulägesmodeller visar vad som finns, men inte alltid vad som är viktigt.
- Drivkrafter, mål, krav, principer och begränsningar bör skiljas åt.
- Strategiska riktningar blir mer användbara när de kopplas till förmågor, initiativ och lösningsdelar.
- Modellera inte alla mål och krav. Modellera det som påverkar arkitekturval och beslut.
- En liten konsekvent startmängd ger ofta mer nytta än en komplett men osäker begreppspalett.
- Vyer ska anpassas till målgruppen. All motivation behöver inte synas överallt.
- Det viktigaste är att modellen gör sambandet mellan uppdrag, mål, förändring och lösning begripligt.

## Quiz/reflektionsfrågor

1. Varför räcker det ofta inte med en modell över nuläge när organisationen ska prioritera förändring?
2. Vad är skillnaden mellan en drivkraft och ett mål?
3. Ge ett exempel på hur ett krav skiljer sig från en princip.
4. När bör motivationselement visas i en vy, och när bör de döljas?
5. Varför är det riskabelt att modellera en lösning innan man har förstått vilket mål den ska bidra till?
6. Hur kan en modell hjälpa en ledningsgrupp att jämföra två olika initiativ?
7. Vilka motivationsbegrepp skulle du börja med i en organisation som är ny på modellering?
8. Hur kan en arkitekt avgöra om ett mål är relevant att modellera?

## Nästa steg

Nu har vi kopplat arkitekturmodellen till varför förändring behövs. Nästa kapitel går vidare till implementation och migration: hur vi kan modellera själva förändringsresan från nuläge till målarkitektur.

Där blir frågan inte bara varför Atlantis behöver modernisera importflödet, utan hur förändringen kan delas upp, planeras, följas och kopplas till både mål och berörda arkitekturdelar.
