# Kapitel 12: Vad man kan välja bort

## Varför detta kapitel finns

En vanlig invändning mot ArchiMate-modellering är att det verkar stort, tungt och svårt att komma igång med. Invändningen är ofta rimlig. Om en organisation försöker använda hela språket, alla lager, många relationstyper och detaljerade modellregler från första dagen blir modelleringen lätt mer belastning än nytta.

Det här kapitlet handlar därför om en av de viktigaste praktiska färdigheterna i arkitekturmodellering: att välja bort medvetet.

Att välja bort betyder inte att modellera slarvigt. Det betyder att låta modellens syfte styra hur mycket struktur som behövs. En modell som ska stödja en strategisk diskussion behöver inte innehålla samma detaljer som en modell som ska användas för teknisk konsekvensanalys. En modell som ska skapa samsyn i ett tidigt skede behöver inte vara lika komplett som en modell som ska ligga till grund för portföljprioritering eller migreringsplanering.

För Tullmyndigheten Atlantis är detta avgörande. Myndigheten har många system, förmågor, processer, regelverk, samarbeten och förändringsinitiativ. Om arkitekterna försöker modellera allt blir arbetet långsamt och svårt att förankra. Om de däremot väljer en tydlig fråga och modellerar minsta användbara utsnitt kan modellen börja skapa nytta tidigt.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför avgränsning är en del av god modellering,
- välja bort lager, element, relationer och detaljer som inte stödjer modellens syfte,
- skilja mellan tillfälligt förenklad modellering och permanent låg kvalitet,
- använda principen minsta användbara modell,
- resonera om när modellen behöver växa och när den bör hållas liten.

## Innan vi börjar

Tidigare kapitel har visat hur verksamhetslager, applikationslager, tekniklager, motivation, implementation, relationer och vyer kan användas. Det kan ge intrycket att en bra modell måste innehålla allt detta.

Så är det inte.

En bra modell är inte den modell som använder flest ArchiMate-element. En bra modell är den modell som på ett tillräckligt korrekt och begripligt sätt hjälper rätt personer att besvara rätt fråga.

Det betyder att modellering alltid behöver tre typer av beslut:

- Vad behöver vi visa?
- Vad behöver vi koppla ihop?
- Vad kan vi låta bli att modellera just nu?

Den tredje frågan är ofta den svåraste, men också den som gör modellering praktiskt användbar.

## Huvudförklaring

### Minsta användbara modell

Minsta användbara modell är den minsta modell som ger mer nytta än en fristående bild.

Den behöver inte vara komplett. Den behöver inte täcka hela myndigheten. Den behöver inte använda alla lager. Den behöver däremot ha tillräcklig struktur för att kunna återanvändas, diskuteras, kvalitetssäkras och kopplas till beslut.

För Atlantis kan en minsta användbar modell till exempel vara:

- tre verksamhetsförmågor som påverkas av ett förändringsinitiativ,
- fem applikationer som stödjer dessa förmågor,
- två centrala informationsflöden,
- några viktiga relationer mellan förmågor, applikationstjänster och initiativ.

Det är inte en fullständig arkitekturmodell för myndigheten. Men den kan vara tillräcklig för att förstå varför modernisering av importflödet påverkar både riskanalys, ärendehantering och samverkan med andra myndigheter.

### Välj bort det som inte påverkar frågan

Det första som kan väljas bort är sådant som inte påverkar den fråga modellen ska besvara.

Om frågan är vilka verksamhetsförmågor som påverkas av ett strategiskt mål, behöver modellen kanske inte visa servrar, nätverkszoner eller databasscheman. Om frågan är vilka tekniska beroenden som påverkar en migrering, räcker det däremot inte med en verksamhetsvy.

En enkel beslutsregel är:

> Modellera det som kan förändra slutsatsen. Utelämna det som inte påverkar slutsatsen.

Om en detalj inte ändrar beslutet, prioriteringen, risken eller samtalet kan den ofta vänta.

### Välj bort lager som inte behövs

ArchiMate ger möjlighet att modellera flera lager, men varje modell behöver inte använda alla lager.

Verksamhetslagret kan räcka när syftet är att förstå ansvar, förmågor, processer eller tjänster på verksamhetsnivå. Applikationslagret kan räcka när syftet är att förstå systemstöd, applikationstjänster och beroenden mellan system. Tekniklagret behövs när infrastruktur, plattformar, drift, säkerhetszoner eller tekniska beroenden påverkar analysen.

För Atlantis kan en tidig modell av ett nytt kontrollflöde börja med verksamhetsförmågor och applikationstjänster. Tekniklagret kan vänta tills frågan blir hur lösningen ska driftsättas, säkras eller migreras.

Det viktiga är att inte se utelämnade lager som ett fel. Det är ett medvetet val, så länge valet är dokumenterat och modellen inte påstår mer än den visar.

### Välj bort relationstyper som inte tillför precision

Relationer skapar mycket av modellens värde, men för många relationstyper kan göra modellen svår att läsa och svår att kvalitetssäkra.

I början kan det vara klokt att använda få relationstyper och vara konsekvent. Det är ofta bättre att ha ett litet antal välförstådda relationer än många relationer som olika arkitekter tolkar olika.

För Atlantis kan arkitektgruppen till exempel börja med att tydligt modellera:

- vilka förmågor som stöds av vilka applikationstjänster,
- vilka applikationer som realiserar dessa tjänster,
- vilka initiativ som påverkar vilka förmågor eller applikationer,
- vilka centrala informationsflöden som är beroende av vissa applikationer.

Mer precisa relationstyper kan införas senare när gruppen har ett gemensamt arbetssätt och när precisionen faktiskt behövs.

### Välj bort fullständig täckning

En annan fallgrop är ambitionen att modellen ska täcka hela organisationen innan den används. Det leder ofta till långa insamlingsfaser och låg upplevd nytta.

Bättre är att börja med ett område där modellen behövs i ett verkligt beslut. Det kan vara ett förändringsprogram, ett systemmoderniseringsinitiativ, ett regelverkskrav eller en återkommande prioriteringsfråga.

För Atlantis kan det vara mer värdefullt att modellera importflödet tillräckligt bra för en pågående modernisering än att försöka skapa en komplett modell över all tullverksamhet. När modellen används i riktiga möten uppstår också bättre återkoppling på vad som saknas.

### Välj bort detaljer som hör hemma i andra artefakter

ArchiMate-modellen ska inte bära all information. Vissa detaljer hör bättre hemma i kravhanteringssystem, informationsmodeller, integrationsdokumentation, säkerhetsklassningar, ärendehanteringssystem eller tekniska designbeskrivningar.

Modellen kan peka på sådant, sammanfatta det eller visa relationer till det. Men om modellen försöker ersätta alla andra artefakter blir den snabbt överlastad.

En praktisk fråga är:

> Behöver denna detalj finnas i modellen, eller räcker det att modellen visar var detaljen hör hemma?

Om svaret är det senare bör detaljen ofta lämnas utanför modellen.

### Välj bort modellering som bara bekräftar det alla redan vet

Ibland skapas modeller över sådant som redan är självklart för målgruppen. Det kan vara användbart som introduktion eller dokumentation, men det skapar sällan stark modellnytta.

Modellering gör mest nytta där det finns oklarhet, beroenden, risk, förändring eller behov av gemensamma beslut. Om alla redan är överens om hur ett litet lokalt system fungerar kanske modellen inte behöver prioriteras. Om däremot samma system visar sig vara kritiskt för flera verksamhetsförmågor blir det relevant att modellera.

För Atlantis är det alltså inte nödvändigt att modellera varje intern stödapplikation bara för att den finns. Men om en sådan applikation visar sig vara avgörande för kontrollflöden, rapportering eller rättssäker handläggning kan den behöva tas in.

## Exempel: Atlantis väljer bort för att komma igång

Atlantis arkitektgrupp får i uppdrag att stödja ett initiativ för mer automatiserad riskanalys i importflödet. Den första impulsen är att skapa en stor modell över hela importverksamheten, alla inblandade system, alla informationsobjekt och alla tekniska integrationer.

Gruppen väljer i stället att börja med en mindre modell. Syftet är att besvara frågan:

> Vilka verksamhetsförmågor, applikationstjänster och centrala informationsflöden påverkas om riskanalysen automatiseras mer?

De väljer in:

- berörda verksamhetsförmågor,
- de viktigaste applikationstjänsterna,
- centrala informationsflöden,
- pågående initiativ som påverkar samma område,
- relationer mellan förmågor, tjänster och initiativ.

De väljer bort:

- detaljerade tekniska komponenter,
- alla integrationsdetaljer,
- fullständig processmodellering,
- detaljerade datamodeller,
- system som inte påverkar riskanalysfrågan.

Resultatet blir inte komplett, men det går att använda i ett styrgruppsmöte. Ledningen kan se att initiativet inte bara påverkar ett IT-system, utan flera förmågor och informationsflöden. Verksamheten kan se vilka delar av importflödet som behöver involveras. IT kan se vilka applikationstjänster som behöver undersökas närmare.

Efter mötet växer modellen, men bara i de delar där nya frågor uppstår.

## När du ska använda detta

Medveten avgränsning är särskilt viktig när:

- organisationen är ny i modellering,
- målgruppen är skeptisk till modeller,
- det finns ont om tid,
- modellens syfte är ett konkret beslut,
- området är stort och komplext,
- modellen riskerar att bli mer dokumentation än beslutsstöd.

Då är det bättre att skapa en liten modell som används än en stor modell som ingen litar på eller orkar underhålla.

## När du inte ska förenkla för mycket

Det finns också situationer där förenkling blir farlig.

Du bör vara försiktig med att välja bort detaljer när modellen används för säkerhetsbedömning, regulatorisk efterlevnad, kritiska beroenden, migreringsplanering eller avveckling av system. I sådana lägen kan detaljer som först verkar oviktiga visa sig vara avgörande.

Det betyder inte att allt måste modelleras. Det betyder att avgränsningen måste göras tydligt och att osäkerheter behöver markeras.

En bra formulering kan vara:

> Denna vy visar verksamhets- och applikationsberoenden för prioriteringsbeslut. Den visar inte tekniska driftberoenden eller detaljerad integrationsdesign.

Då vet läsaren vad modellen kan och inte kan användas till.

## Vanliga misstag

- **Misstag: Att tro att allt måste modelleras innan modellen får användas.**
  - Varför det händer: Arkitekter vill ofta vara noggranna och undvika luckor.
  - Hur du undviker det: Börja med en tydlig fråga och modellera ett avgränsat utsnitt.

- **Misstag: Att välja bort utan att säga det.**
  - Varför det händer: Diagrammet ser rent och tydligt ut, men avgränsningen är osynlig.
  - Hur du undviker det: Skriv alltid vad vyn visar och vad den inte visar.

- **Misstag: Att använda för många elementtyper för tidigt.**
  - Varför det händer: ArchiMate erbjuder många möjligheter och verktyget gör dem lättillgängliga.
  - Hur du undviker det: Starta med få elementtyper och inför fler när det finns ett tydligt behov.

- **Misstag: Att förenkla bort relationerna.**
  - Varför det händer: Element är lättare att rita än relationer.
  - Hur du undviker det: Behåll de relationer som behövs för att modellen ska kunna svara på frågan.

- **Misstag: Att låta varje arkitekt välja bort på sitt eget sätt.**
  - Varför det händer: Organisationen saknar gemensamma modellprinciper.
  - Hur du undviker det: Enas om enkla regler för minsta användbara modell, namngivning och relationer.

## Övningar

### Övning 1: Välj bort i ett konkret scenario

Tänk dig att Atlantis ska besluta om ett initiativ för att modernisera ett äldre ärendehanteringssystem.

Svara på följande frågor:

1. Vilken är den viktigaste beslutssituationen?
2. Vilka tre till fem elementtyper behöver modellen innehålla?
3. Vilka detaljer kan väljas bort i första versionen?
4. Vilken risk uppstår om ni väljer bort för mycket?

### Övning 2: Skriv en avgränsningstext

Formulera två meningar som skulle kunna stå bredvid en vy.

Den första meningen ska beskriva vad vyn visar. Den andra ska beskriva vad vyn inte visar.

Exempel:

> Denna vy visar vilka verksamhetsförmågor och applikationstjänster som påverkas av initiativet Automatiserad riskanalys. Den visar inte tekniska driftberoenden eller detaljerad integrationsdesign.

### Fördjupning

Välj en arkitekturbild från din egen organisation. Fundera på vad som skulle behöva läggas till för att bilden skulle bli en minsta användbar modell.

Fråga särskilt:

- Vilka element behöver ha tydliga typer?
- Vilka relationer behöver bli explicita?
- Vilka delar kan fortfarande lämnas som enkel visualisering?
- Vilken fråga skulle modellen kunna hjälpa till att besvara?

## Fler praktiska avgränsningsfall

Att välja bort är inte ett tecken på låg ambitionsnivå. Det är ofta ett tecken på att modellen har ett tydligt syfte.

### När verksamhetsdetaljer kan väljas bort

Om frågan är vilka applikationer som påverkas av ett nytt lagkrav behöver modellen kanske visa berörda förmågor, processer och informationsobjekt. Den behöver däremot inte visa varje handläggningssteg i detalj. För mycket processdetalj kan göra det svårare att se den egentliga påverkan.

### När tekniklagret kan väljas bort

Om frågan är hur en ny digital tjänst påverkar deklaranter, handläggare och verksamhetsförmågor behöver tekniklagret ofta inte vara med i första vyn. Tekniklagret kan läggas till senare om beslutet påverkas av säkerhetszoner, plattformar, driftmiljöer eller tekniska livscykler.

### När relationstyper kan förenklas

I en tidig arbetsmodell kan Atlantis börja med få relationstyper: stödjer, använder, realiserar och påverkar. När modellen mognar kan relationerna göras mer precisa där precisionen skapar nytta. All precision behöver inte införas dag ett.

### När fullständig täckning bör undvikas

Det är lockande att säga att modellen ska omfatta hela myndigheten. Första nyttan uppstår oftare när modellen täcker ett viktigt beslutsområde tillräckligt bra. För Atlantis kan det vara importflödet, riskanalys eller digital självservice. När modellen har visat nytta där kan den växa.

### Beslutsregel

Välj bort det som inte hjälper den aktuella målgruppen att förstå påverkan, ansvar, beroende eller vägval. Dokumentera bortvalet så att det kan omprövas senare.

## Snabb sammanfattning

- En bra modell behöver inte vara komplett.
- Modellera det som kan påverka slutsatsen.
- Välj bort lager, relationer och detaljer som inte stödjer syftet.
- Dokumentera alltid vad modellen visar och inte visar.
- Börja med minsta användbara modell och låt den växa när riktiga frågor kräver det.
- Förenkling är bra när den är medveten, men farlig när den döljer viktiga beroenden.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan att välja bort medvetet och att modellera slarvigt?
2. När kan tekniklagret väljas bort i en första modell?
3. Varför kan fullständig täckning vara ett hinder för modellnytta?
4. Vilka detaljer hör ofta bättre hemma utanför ArchiMate-modellen?
5. Hur kan en vy visa sin egen avgränsning?

## Nästa steg

Nu har vi sett hur man kan hålla modellen liten nog för att bli användbar. Nästa kapitel handlar om hur man börjar dra nytta av modeller i praktiken: hur Atlantis kan gå från enstaka modelleringsförsök till ett arbetssätt där modeller används i riktiga beslut, möten och förändringsinitiativ.
