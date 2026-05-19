# Kapitel 6: Applikationslagret: från systemkarta till begriplig modell

## Varför detta kapitel finns

Många arkitekturbilder börjar som systemkartor. De visar rutor med systemnamn, några pilar, kanske några integrationsplattformar och ibland färger som betyder ägarskap, teknik, status eller risk. En sådan bild kan vara användbar i ett möte, men den blir snabbt svår att återanvända. Den blandar ofta flera frågor samtidigt: vilka system finns, vilka informationsflöden går mellan dem, vilka verksamhetsförmågor de stödjer, vilka tekniska beroenden de har och vilka förändringar som planeras.

Applikationslagret i ArchiMate hjälper oss att skilja på dessa frågor. Det gör det möjligt att gå från en systemkarta som visar “vad vi har” till en modell som också kan visa “vad systemen gör”, “vad de stödjer”, “vilka beroenden som finns” och “vad som påverkas om vi ändrar något”.

Det här kapitlet handlar inte om att modellera alla applikationer i en organisation. Det handlar om att välja den minsta användbara strukturen för att förstå applikationslandskapet i relation till verksamhetens behov.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara skillnaden mellan en systemkarta och en applikationsmodell,
- avgöra när applikationslagret är rätt startpunkt,
- skilja mellan applikation, applikationstjänst, gränssnitt och informationsflöde,
- koppla applikationer till verksamhetsförmågor och processer utan att modellen blir för stor,
- välja bort tekniska och organisatoriska detaljer som inte behövs för modellens syfte,
- formulera en första användbar applikationsvy för Tullmyndigheten Atlantis.

## Innan vi börjar

I kapitel 5 använde vi verksamhetslagret för att förstå importflödet i Atlantis. Vi skilde på förmågor, processer, verksamhetstjänster, roller och aktörer. Det gav en stabil bild av vad myndigheten behöver kunna göra, utan att börja med systemnamn.

Nu vänder vi blicken mot applikationslandskapet. Frågan är inte längre bara vad Atlantis behöver kunna göra, utan också vilka applikationer som stödjer detta, vilka tjänster de erbjuder och vilka beroenden som finns mellan verksamhet och IT.

Det är här många organisationer fastnar. De har ofta gott om systemlistor och integrationsbilder, men svårt att svara på frågor som:

- Vilka applikationer stödjer förmågan att riskbedöma importärenden?
- Vilka applikationer används i flera verksamhetsflöden?
- Vilka systemberoenden gör ett moderniseringsinitiativ större än det först verkar?
- Vilka applikationer exponerar tjänster som andra delar av myndigheten är beroende av?
- Vilka informationsutbyten är kritiska för rättssäker och effektiv handläggning?

En applikationsmodell ska hjälpa till att besvara sådana frågor.

## Huvudförklaring

### Systemkartan är ofta en bra början

En systemkarta är inte fel. Den är ofta ett nödvändigt första steg. När arkitekter i Atlantis samlar deltagare från importhandläggning, riskanalys, IT-förvaltning och utvecklingsprojekt behöver de ofta börja med att få upp det kända landskapet på väggen.

En enkel systemkarta kan till exempel visa:

- Importportalen
- Ärendehanteringssystemet
- Riskanalysplattformen
- Kontrollplaneringssystemet
- Integrationsplattformen
- Dokument- och arkivlösningen
- Externa gränssnitt mot andra myndigheter och EU-system

Detta skapar gemensam orientering. Problemet uppstår när systemkartan börjar användas som om den vore en modell. Då blir varje ruta laddad med otydlig betydelse. En ruta kan ibland betyda ett system, ibland en applikation, ibland en teknisk plattform, ibland en produkt, ibland en förvaltning och ibland ett projekt.

När betydelsen varierar blir modellen svår att analysera. Det går fortfarande att prata om bilden, men det går inte att pålitligt följa samband.

### Applikationslagret ger struktur åt systemkartan

Applikationslagret hjälper oss att ge systemkartan tydligare begrepp. I en praktisk startmängd räcker det ofta att börja med fyra frågor:

1. Vilka applikationskomponenter finns i den del av landskapet vi behöver förstå?
2. Vilka applikationstjänster erbjuder de till verksamheten eller andra applikationer?
3. Vilka applikationsgränssnitt används för att nå tjänsterna?
4. Vilka informationsobjekt eller dataflöden är viktiga för den fråga vi försöker besvara?

Det viktiga är inte att snabbt använda många symboler. Det viktiga är att sluta använda samma ruta för flera olika saker.

En applikationskomponent beskriver en logisk applikationsdel som har ett ansvar i landskapet. En applikationstjänst beskriver vad applikationen erbjuder. Ett applikationsgränssnitt beskriver var eller hur andra använder applikationens funktionalitet. Ett informationsflöde beskriver att information rör sig mellan delar av modellen.

I praktiken innebär det att Atlantis inte bara modellerar “Riskanalysplattformen” som en ruta. Arkitekterna kan också visa att den erbjuder en riskbedömningstjänst, att importflödet använder denna tjänst och att tjänsten behöver information om deklarationer, tidigare avvikelser och kontrollresultat.

### Börja inte med alla applikationer

Ett vanligt misstag är att börja med ambitionen att modellera hela applikationsportföljen. I en större myndighet leder det snabbt till ett stort inventeringsarbete. Resultatet kan bli en katalog, men inte nödvändigtvis en modell som används.

En bättre start är att knyta applikationslagret till en konkret modelleringsfråga.

För Atlantis kan frågan vara:

> Vilka applikationer och applikationstjänster är kritiska för att modernisera importflödet utan att försämra riskanalys, kontroll och rättssäker handläggning?

Den frågan ger en naturlig avgränsning. Modellen behöver inte innehålla alla applikationer i myndigheten. Den behöver börja med de applikationer som stödjer importflödet, riskanalysen, kontrollplaneringen, ärendehanteringen och informationsutbytet.

När modellen sedan används i verkliga diskussioner kan den växa. Men den växer utifrån nytta, inte utifrån inventeringsiver.

### Applikationstjänster är ofta viktigare än systemnamn

Systemnamn är nödvändiga i vardagen. Människor säger “Importportalen”, “Ärendesystemet” eller “Riskmotorn”. Men systemnamn säger sällan tillräckligt om vad applikationen faktiskt erbjuder.

En applikationstjänst beskriver en förmåga hos applikationen ur användarens eller konsumentens perspektiv. Det kan vara:

- ta emot importdeklaration,
- validera ärendedata,
- beräkna riskindikator,
- tillgängliggöra ärendestatus,
- hämta tidigare kontrollutfall,
- arkivera beslutsunderlag.

När tjänsterna synliggörs kan arkitekterna föra en mer användbar diskussion. Frågan blir inte bara “vilket system används?”, utan “vilken tjänst behöver verksamheten, vem tillhandahåller den och vilka andra delar är beroende av den?”.

Detta är särskilt viktigt i en myndighet där system ofta har vuxit fram över lång tid. Ett äldre system kan innehålla flera tjänster som verksamheten fortfarande är starkt beroende av. Ett nytt system kan ersätta en del av funktionaliteten men inte allt. Om modellen bara visar systemrutor kan sådana skillnader döljas.

### Koppla applikationer till verksamhet utan att övermodellera

Applikationslagret blir mest användbart när det kopplas till verksamhetslagret. Men kopplingen måste göras med måtta.

Det är sällan klokt att koppla varje liten processaktivitet till varje applikation. Det skapar många relationer och liten nytta. I stället bör man fråga vilken nivå som passar beslutet.

För Atlantis kan tre kopplingsnivåer vara användbara:

- förmåga till applikationstjänst,
- process till applikationstjänst,
- verksamhetstjänst till applikationstjänst.

Om ledningen vill förstå vilka delar av importförmågan som påverkas av ett systembyte kan förmåga till applikationstjänst räcka. Om ett utvecklingsteam behöver förstå ett konkret flöde kan process till applikationstjänst vara mer relevant. Om fokus ligger på vad en extern aktör får ut av myndigheten kan verksamhetstjänst till applikationstjänst vara bättre.

Det viktiga är att inte modellera alla nivåer bara för att de finns. Välj den koppling som gör frågan begriplig.

### Informationsflöden kräver tydlig avgränsning

Applikationsbilder fylls ofta med pilar. Pilarna kan betyda nästan vad som helst: integration, beroende, filöverföring, användning, databasåtkomst, verksamhetsflöde, ägarskap eller tidsordning.

I en modell behöver pilarna betyda något mer bestämt. Annars kan man inte analysera dem.

För Atlantis kan ett informationsflöde beskriva att importdeklarationsdata skickas från Importportalen till Ärendehanteringssystemet. Ett annat flöde kan visa att riskindikatorer skickas från Riskanalysplattformen till Kontrollplaneringssystemet. Men modellen behöver inte samtidigt beskriva varje teknisk protokollnivå, varje meddelandetyp och varje fält i informationsmodellen.

En praktisk regel är:

> Modellera informationsflöden när flödet är viktigt för beslutet, risken, förändringen eller förståelsen.

Om frågan handlar om vilka system som påverkas av ett nytt informationsutbyte med en annan myndighet kan flöden vara centrala. Om frågan handlar om verksamhetsförmågor på hög nivå kan detaljerade flöden vara onödiga.

### Gränssnitt visar var beroenden uppstår

Ett applikationsgränssnitt kan användas för att visa hur andra applikationer eller aktörer får tillgång till en applikationstjänst. I praktiken hjälper gränssnittet till att göra beroenden tydligare.

I Atlantis kan Riskanalysplattformen erbjuda en riskbedömningstjänst via ett maskinellt gränssnitt. Importportalen eller Ärendehanteringssystemet kan använda detta gränssnitt för att få en riskklassning av ett ärende. Om gränssnittet ändras påverkas fler än den applikation som äger tjänsten.

Men även här gäller minimal användbar modellering. Om modellen används för ledningsdialog kan gränssnittet ofta döljas i vyn. Om modellen används för integrationsplanering kan gränssnittet vara avgörande.

Vyn ska visa det som målgruppen behöver se. Modellen kan innehålla mer struktur än vyn visar.

## Exempel: Atlantis går från systemkarta till applikationsmodell

Atlantis har ett moderniseringsprogram för importflödet. I programmets första workshop visar en arkitekt en systemkarta. Den innehåller ett tjugotal rutor och många pilar. Alla känner igen delar av bilden, men samtalet blir snabbt otydligt.

Verksamhetsarkitekten frågar:

> Vilka av dessa system är faktiskt kritiska för att fatta beslut i importärenden?

IT-arkitekten svarar:

> Det beror på vad vi menar med kritiska. Är det system som handläggaren använder, system som tillhandahåller data, system som gör riskberäkning eller system som måste vara tillgängliga för att ärendet ska gå vidare?

Den frågan visar att systemkartan behöver bli en modell.

Arkitektgruppen väljer en avgränsad startmängd:

- applikationskomponent,
- applikationstjänst,
- applikationsgränssnitt,
- informationsflöde,
- relationen mellan verksamhetsförmåga och applikationstjänst.

De börjar med tre verksamhetsförmågor från kapitel 5:

- ta emot importuppgifter,
- riskbedöma importärenden,
- besluta om kontroll eller klarering.

Sedan identifierar de några applikationstjänster:

- mottagning av importdeklaration,
- ärendevalidering,
- riskklassning,
- kontrollurval,
- ärendestatus,
- arkivering av beslutsunderlag.

Först därefter kopplar de tjänsterna till applikationskomponenter:

- Importportalen erbjuder mottagning av importdeklaration.
- Ärendehanteringssystemet erbjuder ärendevalidering och ärendestatus.
- Riskanalysplattformen erbjuder riskklassning.
- Kontrollplaneringssystemet erbjuder kontrollurval.
- Arkivlösningen erbjuder arkivering av beslutsunderlag.

Den nya modellen ger inte fler rutor för sakens skull. Den ger tydligare betydelse. Nu kan gruppen diskutera vad som händer om Ärendehanteringssystemet byts ut, om Riskanalysplattformen får ett nytt gränssnitt eller om importflödet ska öppnas för mer automatiserad handläggning.

## När applikationslagret är rätt startpunkt

Applikationslagret är ofta rätt startpunkt när huvudfrågan handlar om IT-landskapets stöd till verksamheten.

Det kan vara rätt startpunkt när:

- organisationen har många systembilder men dålig förståelse för beroenden,
- ett moderniseringsinitiativ påverkar flera applikationer,
- samma applikation stödjer flera verksamhetsområden,
- äldre system innehåller kritisk funktionalitet som är svår att ersätta,
- integrationsberoenden påverkar planering och risk,
- verksamheten pratar om problem i systemtermer men egentligen behöver förstå tjänster och förmågor.

För Atlantis är applikationslagret särskilt relevant när modernisering av importflödet ska planeras. Det räcker inte att veta att “Importportalen ska ersättas”. Man behöver förstå vilka tjänster portalen erbjuder, vilka andra applikationer som använder information från den och vilka verksamhetsförmågor som påverkas.

## När applikationslagret inte bör vara startpunkt

Applikationslagret är inte alltid bäst först.

Det kan vara fel startpunkt när:

- organisationen ännu inte vet vilken verksamhetsförändring den vill uppnå,
- diskussionen egentligen handlar om mål, krav eller principer,
- systemnamnen riskerar att låsa samtalet vid dagens lösning,
- huvudproblemet är ansvar, arbetssätt eller process,
- målgruppen är ledning som behöver förstå verksamhetseffekt snarare än applikationsstruktur.

I Atlantis kan ett program för “framtidens importhantering” lätt börja med systemlandskapet. Men om ledningen ännu inte har en gemensam bild av vilka förmågor som ska utvecklas, kan applikationslagret skapa för tidig lösningslåsning. Då bör verksamhetslagret eller motivationslagret komma först.

## Vad man kan välja bort

Applikationslagret kan snabbt bli för detaljerat. Det är därför viktigt att medvetet välja bort.

Du kan ofta välja bort:

- fullständig systeminventering,
- alla tekniska integrationer,
- alla databaser,
- alla interna moduler,
- alla batchflöden,
- alla ägarskapsdetaljer,
- alla livscykelstatusar,
- alla informationsfält,
- alla beroenden som inte påverkar aktuell fråga.

Det betyder inte att dessa saker är oviktiga. Det betyder bara att de inte alltid hör hemma i den modellvy du arbetar med.

En modell som ska hjälpa ledningen prioritera mellan moderniseringsinitiativ behöver ofta visa färre tekniska detaljer. En modell som ska stödja integrationsplanering behöver visa fler. Samma underliggande modell kan ge båda vyerna, men man ska inte försöka lösa båda samtalen med samma bild.

## Vanliga misstag

- **Misstag: Att kalla allt för system.**
  - Varför det händer: Systemnamn är vardagliga och lätta att känna igen.
  - Hur du undviker det: Skilj mellan applikationskomponent, applikationstjänst och teknisk plattform när skillnaden påverkar frågan.

- **Misstag: Att modellera hela applikationsportföljen direkt.**
  - Varför det händer: Det känns ordentligt att börja med komplett inventering.
  - Hur du undviker det: Börja med en modelleringsfråga och ett avgränsat verksamhetsområde.

- **Misstag: Att låta pilar betyda flera olika saker.**
  - Varför det händer: I bilder används pilar ofta fritt.
  - Hur du undviker det: Bestäm vad relationerna betyder i den aktuella modellen och använd dem konsekvent.

- **Misstag: Att visa tekniska detaljer för fel målgrupp.**
  - Varför det händer: Arkitekter vill ofta vara exakta.
  - Hur du undviker det: Skapa olika vyer för ledning, verksamhet, IT och utveckling.

- **Misstag: Att koppla varje processsteg till varje applikation.**
  - Varför det händer: Man vill visa hur allt hänger ihop.
  - Hur du undviker det: Välj kopplingsnivå efter beslutet: förmåga, process eller tjänst.

## Praktiska beslutsregler

Använd applikationslagret när du behöver förstå hur IT-landskapet stödjer, begränsar eller möjliggör verksamheten.

Börja med applikationstjänster när systemnamnen skymmer vad applikationerna faktiskt gör.

Visa gränssnitt när beroenden, integrationsplanering eller förändringsrisk kräver det.

Visa informationsflöden när informationens väg är central för beslutet.

Välj bort tekniska detaljer när de inte påverkar den fråga modellen ska besvara.

## Övningar

### Övning 1: Gör om en systemkarta till en första modell

Välj en befintlig systembild från din organisation, eller använd Atlantis-exemplet.

Gör följande:

1. Markera vilka rutor som är applikationskomponenter.
2. Skriv minst en applikationstjänst för tre av komponenterna.
3. Identifiera en verksamhetsförmåga som använder varje tjänst.
4. Ta bort eller dölj detaljer som inte behövs för att förstå sambandet.

Reflektera över vad som blev tydligare när systemnamnen kompletterades med tjänster.

### Övning 2: Hitta pilar med oklar betydelse

Titta på en applikations- eller integrationsbild.

Besvara frågorna:

1. Betyder alla pilar samma sak?
2. Visar pilarna informationsflöde, användning, beroende, integration eller tidsordning?
3. Vilka pilar behöver tydligare semantik för att modellen ska kunna användas i analys?
4. Vilka pilar kan tas bort i en ledningsvy?

### Övning 3: Välj rätt detaljeringsnivå

Anta att Atlantis ska ersätta Importportalen.

Skapa två olika vyer:

1. En vy för ledningen som visar vilka verksamhetsförmågor och applikationstjänster som påverkas.
2. En vy för integrationsplanering som visar centrala applikationer, gränssnitt och informationsflöden.

Jämför vyerna. Vilka delar finns i båda? Vilka detaljer bör bara finnas i den ena?

### Fördjupning

Formulera en regel för när din organisation ska modellera applikationstjänster. Regeln ska vara enkel nog att användas i vardagen.

Exempel:

> Vi modellerar applikationstjänster när en applikation används av flera verksamhetsområden, när den ingår i ett förändringsinitiativ eller när systemnamnet inte räcker för att förstå beroendet.

## Små modellpåståenden i applikationslagret

En systemkarta visar ofta vilka system som finns. En applikationsmodell bör dessutom visa vad systemen gör för verksamheten och hur de är beroende av varandra.

Exempel från Atlantis:

- Applikationskomponenten **Ärendehanteringssystemet** tillhandahåller applikationstjänsten **Hantera importärende**.
- Applikationstjänsten **Riskbedöm importdeklaration** stödjer verksamhetsprocessen **Prioritera kontrollinsats**.
- Applikationsgränssnittet **Deklarations-API** används av externa ombud för att lämna importuppgifter.
- Informationsobjektet **Importdeklaration** används av både **Ärendehanteringssystemet** och **Riskanalysplattformen**.

Dessa påståenden gör att system inte bara blir rutor på en karta. De blir delar av en modell där det går att fråga vad som stödjer vad, var information används och vilka applikationer som påverkas av en förändring.

## Snabb sammanfattning

- En systemkarta kan vara användbar, men blir begränsad om rutorna och pilarna saknar tydlig betydelse.
- Applikationslagret hjälper till att skilja mellan applikationer, tjänster, gränssnitt och informationsflöden.
- Applikationstjänster gör det tydligare vad ett system faktiskt erbjuder.
- Kopplingen mellan verksamhetsförmågor och applikationstjänster ger ofta mer nytta än enbart systemnamn.
- Informationsflöden och gränssnitt ska modelleras när de behövs för beslut, analys eller förändringsplanering.
- Modellera inte hela applikationsportföljen direkt. Börja med en fråga, ett område och en användbar startmängd.
- Samma modell kan ge olika vyer för ledning, verksamhet, IT och utveckling.

## Quiz/reflektionsfrågor

1. Vad är den viktigaste skillnaden mellan en systemkarta och en applikationsmodell?
2. Varför kan applikationstjänster vara mer användbara än systemnamn?
3. När är applikationslagret en bra startpunkt?
4. När bör man börja i verksamhetslagret eller motivationslagret i stället?
5. Vilka detaljer kan du ofta välja bort i en första applikationsmodell?
6. Hur kan samma modell ge olika vyer för olika målgrupper?

## Nästa steg

I nästa kapitel går vi vidare till tekniklagret. Där undersöker vi när infrastruktur, plattformar, noder, säkerhetszoner och tekniska beroenden faktiskt behöver modelleras, och när de mest skapar brus. Målet är inte att göra arkitekturmodellen tekniktung, utan att förstå när teknik påverkar verksamhetsbeslut, risk och genomförbarhet.
