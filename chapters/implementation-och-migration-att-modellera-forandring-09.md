# Kapitel 9: Implementation och migration: att modellera förändring

## Varför detta kapitel finns

De tidigare kapitlen har visat hur modeller kan beskriva nuläge, mål, förmågor, applikationer, teknik och varför en förändring behövs. Men i en större myndighet räcker det sällan att förstå nuläge och målbild. Den svåra delen är ofta resan mellan dem.

Många arkitekturbilder visar ett önskat framtida läge. De kan vara tydliga i ett styrgruppsmöte, men de svarar inte alltid på frågor som:

- Vad behöver förändras först?
- Vilka delar kan förändras oberoende av varandra?
- Vilka leveranser behöver komma före andra?
- Vilka gamla lösningar måste leva kvar under en övergångsperiod?
- Vad händer om ett projekt försenas?
- Hur vet vi att ett initiativ faktiskt bidrar till målarkitekturen?

När förändring bara beskrivs som en pil från nuläge till målbild blir arkitekturarbetet lätt för grovt. Det kan se ut som om organisationen bara behöver fatta beslut och sedan gå direkt till framtiden. I praktiken sker förändring genom arbetspaket, delleveranser, övergångslägen, beroenden, kompromisser och successiva beslut.

I Tullmyndigheten Atlantis finns ett program för att modernisera importflödet. Programmet vill gå från manuell hantering och flera äldre system till mer automatiserade riskbedömningar, bättre informationsutbyte och tydligare digitala tjänster. Ledningen vill se målbilden. Projektledningen vill se leveranser. Verksamheten vill veta när arbetssätt påverkas. IT-förvaltningen vill veta när gamla system kan avvecklas. Säkerhetsfunktionen vill veta när nya integrations- och åtkomstmönster införs.

Alla dessa frågor hör ihop. Implementation och migration handlar om att modellera förändringen så att den går att förstå, diskutera, prioritera och följa upp. Målet är inte att ersätta projektplaner, portföljstyrning eller detaljerad releaseplanering. Målet är att koppla förändringsarbetet till arkitekturens innehåll: vilka förmågor, processer, applikationer, tjänster, informationsobjekt och teknikdelar som påverkas.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara varför nuläge och målbild inte räcker för att styra förändring,
- beskriva hur implementation och migration kan användas för att modellera förändringsresan,
- skilja mellan initiativ, arbetspaket, leverans, övergångsläge och målarkitektur,
- visa hur en förändring kan kopplas till berörda verksamhets-, applikations- och teknikdelar,
- avgöra när migrationsmodellering skapar nytta och när den blir för detaljerad,
- använda Atlantis-scenariot för att resonera om stegvis modernisering,
- formulera praktiska frågor som gör en förändringsmodell användbar i portfölj- och beslutsarbete.

## Innan vi börjar

I kapitel 8 kopplade vi modellen till varför förändring behövs. Där såg vi att mål, drivkrafter, krav och principer hjälper oss att förstå varför ett initiativ är viktigt. Nu går vi ett steg vidare och frågar hur förändringen kan genomföras.

Det är frestande att tänka att en målarkitektur är slutpunkten och att allt däremellan är projektledning. Men för arkitekter är mellanlägena ofta avgörande. En organisation kan behöva leva i ett övergångsläge under flera år. Gamla och nya applikationer kan behöva samexistera. En verksamhetsförmåga kan förstärkas innan bakomliggande teknik är helt moderniserad. En ny digital tjänst kan införas innan alla gamla informationsflöden är avvecklade.

Migrationsmodellering blir därför särskilt viktig när:

- förändringen sträcker sig över flera projekt eller program,
- flera verksamhetsdelar påverkas samtidigt,
- gamla och nya lösningar behöver samexistera,
- det finns många beroenden mellan leveranser,
- ledningen behöver förstå konsekvenser av prioritering eller försening,
- arkitekturen behöver följas upp över tid.

Det betyder inte att varje projektplan ska ritas i ArchiMate. Det betyder att de arkitekturellt viktiga delarna av förändringen bör kopplas till modellen.

## Från målbild till förändringsresa

En målbild kan vara mycket värdefull. Den visar riktning. Den hjälper olika aktörer att förstå vart organisationen vill. Men en målbild kan också vara vilseledande om den ser mer färdig och enkel ut än förändringen faktiskt är.

I Atlantis kan målbilden för importflödet exempelvis säga:

- Importunderlag ska kunna tas emot digitalt.
- Riskbedömning ska kunna ske mer automatiserat.
- Handläggare ska få ett sammanhållet stöd för beslut.
- Informationsutbyte med andra myndigheter ska bli mer robust.
- Äldre integrationslösningar ska fasas ut.

Detta är en bra riktning, men den säger inte hur vägen dit ser ut. För att modellen ska göra nytta behöver den visa förändringsresan på en nivå som passar besluten.

En enkel förändringsresa kan beskrivas i tre steg:

1. Nuläge: hur Atlantis arbetar och vilka lösningar som används idag.
2. Övergångsläge: ett tillfälligt men planerat läge där vissa nya delar finns och vissa gamla delar lever kvar.
3. Målarkitektur: det läge som organisationen strävar mot inom en viss planeringshorisont.

Denna indelning låter enkel, men den kan göra stor skillnad. Den gör det möjligt att se att målarkitekturen inte uppstår på en gång. Den gör också övergångsläget legitimt. I många organisationer finns övergångslägen ändå, men de hanteras som avvikelser eller tillfälliga kompromisser. När de modelleras blir de något man kan planera, analysera och förvalta.

## Atlantis-exempel: modernisering av importflödet

Tullmyndigheten Atlantis har ett äldre importflöde där flera delar har vuxit fram över tid. Verksamheten har hög kompetens, men mycket kunskap sitter i rutiner, specialfall och personberoende arbetssätt. IT-landskapet innehåller ett äldre ärendehanteringssystem, separata kontrollstöd, manuella filöverföringar och flera integrationer som är svåra att överblicka.

Ett nytt program, Import 2030, ska förbättra flödet. Programmet har fyra övergripande ambitioner:

- öka automatiseringen av lågriskärenden,
- förbättra riskanalysen,
- ge handläggare bättre beslutsstöd,
- minska beroendet av äldre integrationer.

Om detta bara ritas som en målbild blir det svårt att förstå vad programmet faktiskt ska leverera. En mer användbar modell kan dela upp förändringen i arkitekturellt meningsfulla delar.

Exempel på arbetspaket kan vara:

- etablera gemensam importinformationsmodell,
- införa ny riskbedömningstjänst,
- införa handläggarstöd för digital import,
- modernisera integrationsmönster för externa parter,
- avveckla äldre filöverföringar,
- flytta prioriterade informationsutbyten till ny integrationsplattform.

Exempel på leveranser kan vara:

- godkänd begreppsmodell för importärenden,
- driftsatt riskbedömningstjänst för en första ärendetyp,
- nytt användargränssnitt för handläggare i pilotflöde,
- integrationsgränssnitt för utvald extern part,
- avvecklingsbeslut för ett äldre delsystem.

Exempel på övergångslägen kan vara:

- ett pilotläge där nya riskbedömningen används för en begränsad ärendemängd,
- ett samexistensläge där gammalt ärendehanteringssystem och nytt handläggarstöd används parallellt,
- ett stabiliseringsläge där externa integrationer successivt flyttas över.

Poängen är inte att kalla allt för rätt ArchiMate-ord från början. Poängen är att skapa en modell där förändringen blir begriplig och går att koppla till arkitekturens övriga delar.

## Grundbegrepp för att modellera förändring

När du modellerar implementation och migration behöver du inte börja med många begrepp. En praktisk startmängd räcker långt.

### Arbetspaket

Ett arbetspaket beskriver en avgränsad insats som ska genomföras. Det kan motsvara ett projekt, ett delprojekt, en etapp eller en större aktivitet. I modelleringen är arbetspaketet användbart när du vill visa att en viss förändring inte bara är ett önskat tillstånd utan något som kräver planerat arbete.

I Atlantis kan “införa ny riskbedömningstjänst” vara ett arbetspaket. Det är inte samma sak som själva tjänsten. Tjänsten är en del av arkitekturen. Arbetspaketet är insatsen som ska skapa, införa eller förändra den.

Denna skillnad är viktig. Om organisationen blandar ihop lösningen med arbetet som inför lösningen blir det svårt att följa upp vad som faktiskt har levererats.

### Leverans

En leverans är ett tydligt resultat av ett arbetspaket. Den kan vara en modell, en beslutad princip, en tjänst, ett gränssnitt, en migrerad datamängd, en avvecklad integration eller ett annat resultat som organisationen kan ta emot och använda.

I Atlantis kan arbetspaketet “etablera gemensam importinformationsmodell” ha leveransen “godkänd begrepps- och informationsmodell för importärenden”. Arbetspaketet “införa handläggarstöd för digital import” kan ha leveransen “pilotdriftsatt handläggarstöd för importflöde A”.

Leveranser är viktiga eftersom de gör förändringen mer konkret. De hjälper också modellen att kopplas till portföljstyrning och uppföljning.

### Övergångsläge

Ett övergångsläge beskriver ett relativt stabilt tillstånd under förändringsresan. Det är inte slutmålet, men det är inte heller bara ett kaos mellan två lägen. Det är ett läge som organisationen kan behöva leva med under en tid.

För Atlantis kan ett övergångsläge vara att ny riskbedömning används för vissa importärenden medan gamla handläggarstöd fortfarande används för andra. Detta kan vara helt rimligt, men bara om organisationen förstår vilka beroenden, kostnader och risker som följer med samexistensen.

Övergångslägen är särskilt viktiga i myndigheter eftersom förändring ofta måste ske utan att uppdraget stannar. Tullflöden, beslut, kontroller och informationsutbyten måste fortsätta fungera även när arkitekturen förändras.

### Gap eller skillnad mellan lägen

Många modelleringspraktiker använder begreppet gap för att beskriva skillnaden mellan två lägen, till exempel mellan nuläge och målarkitektur. I versionsmedveten modellering bör du vara uppmärksam på exakt hur ditt verktyg och din ArchiMate-version hanterar detta, men tankesättet är fortfarande användbart: vad saknas, vad ändras, vad tillkommer och vad ska tas bort?

För praktisk modellnytta kan du formulera skillnaden som frågor:

- Vilka förmågor behöver stärkas?
- Vilka applikationstjänster saknas?
- Vilka integrationer behöver ersättas?
- Vilka informationsobjekt behöver standardiseras?
- Vilka tekniska beroenden behöver avvecklas?
- Vilka risker finns under samexistensperioden?

När gapet formuleras så blir det ett arbetsunderlag, inte bara en ruta i en modell.

## Koppla förändring till arkitekturdelar

En migrationsmodell blir användbar först när förändringsdelarna kopplas till det som faktiskt påverkas. Annars blir den bara en projektlista.

Ett arbetspaket bör därför kunna kopplas till exempelvis:

- berörda verksamhetsförmågor,
- berörda processer eller arbetssätt,
- applikationer och applikationstjänster som införs, ändras eller avvecklas,
- informationsobjekt eller dataflöden som förändras,
- teknikplattformar och integrationsmönster som påverkas,
- mål, krav och principer som arbetet bidrar till.

I Atlantis kan arbetspaketet “införa ny riskbedömningstjänst” kopplas till:

- förmågan bedöma risk,
- applikationstjänsten riskbedömning,
- informationsobjekten importdeklaration, aktörsuppgift och riskindikator,
- målet öka träffsäkerheten i riskurval,
- principen återanvänd gemensamma informationsbegrepp,
- övergångsläget pilot för automatiserad riskbedömning.

När dessa kopplingar finns kan modellen svara på frågor som en vanlig projektlista inte klarar lika väl:

- Vilka mål påverkas om arbetspaketet försenas?
- Vilka applikationer måste finnas innan pilotläget kan fungera?
- Vilka verksamhetsförmågor får nytta av första leveransen?
- Vilka gamla delar kan inte avvecklas förrän en viss leverans är klar?
- Vilka beroenden bör synas i portföljstyrningen?

Detta är ett exempel på modellnytta. Modellen hjälper inte bara till att visa en plan. Den hjälper organisationen att resonera om konsekvenser.

## Vad ska modelleras och vad ska lämnas i projektplanen?

En vanlig fallgrop är att försöka modellera hela projektplanen i arkitekturverktyget. Det skapar snabbt onödig detaljering. Arkitekturmodellen ska inte ersätta planeringsverktyg, backloggar, tidplaner, ekonomisystem eller uppföljningsrapporter.

En bra tumregel är att modellera det som har arkitekturell betydelse.

Modellera gärna:

- arbetspaket som förändrar förmågor, processer, tjänster, applikationer, information eller teknik,
- leveranser som skapar eller förändrar arkitekturdelar,
- övergångslägen som organisationen behöver förstå och leva med,
- beroenden som påverkar prioritering eller sekvensering,
- avvecklingar som minskar risk, kostnad eller komplexitet,
- kopplingar mellan mål och förändringsinsatser.

Lämna normalt utanför modellen:

- detaljerade aktivitetslistor,
- personallokering,
- veckovisa statusmarkeringar,
- intern mötesplanering,
- detaljerade sprintar,
- uppgifter som bara är relevanta för projektgruppen och inte för arkitekturförståelsen.

Det betyder inte att dessa saker är oviktiga. De hör bara hemma i andra styrnings- och planeringsartefakter. Arkitekturmodellen ska länka till dem när det behövs, inte kopiera dem.

## När implementation och migration skapar störst nytta

Migrationsmodellering är särskilt värdefull när förändringen är komplex nog att enkla bilder inte räcker, men inte så detaljerad att modellen blir projektadministration.

Den skapar ofta stor nytta i följande situationer:

- när flera initiativ påverkar samma förmåga,
- när en målarkitektur kräver flera övergångslägen,
- när gamla applikationer behöver avvecklas stegvis,
- när verksamheten måste förstå hur arbetssätt förändras över tid,
- när portföljen behöver se beroenden mellan initiativ,
- när säkerhet, juridik eller informationsförvaltning påverkar ordningsföljden,
- när ledningen behöver förstå varför en viss etapp måste göras före en annan.

I Atlantis blir detta tydligt när importmoderniseringen konkurrerar med andra initiativ. Om ledningen bara ser tre projekt med kostnad och tidplan kan det vara svårt att avgöra vad som bör prioriteras. Om modellen visar att två projekt bygger på samma informationsmodell, eller att en avveckling inte kan ske förrän en ny integrationsförmåga finns, blir prioriteringen mer informerad.

## När du kan låta bli

Du behöver inte alltid modellera implementation och migration. Ibland räcker en enkel målbild, ett beslutunderlag eller en kort lista över nästa steg.

Du kan ofta låta bli när:

- förändringen är liten och påverkar få arkitekturdelar,
- det bara finns ett arbetspaket och få beroenden,
- målbilden kan införas direkt utan viktiga övergångslägen,
- förändringen redan är väl förstådd av alla berörda,
- modellen inte kommer att användas i beslut, uppföljning eller kommunikation.

Det är också klokt att låta bli om organisationen saknar grundläggande modellstruktur. Om verksamhetsförmågor, applikationstjänster och centrala relationer inte finns alls kan det vara bättre att först modellera de delar som förändringen ska kopplas till.

En migrationsmodell utan koppling till arkitekturens innehåll blir lätt en snyggare projektplan. Den gör inte nödvändigtvis mer nytta.

## Praktisk arbetsgång

När Atlantis ska börja modellera implementation och migration kan arkitekterna använda en enkel arbetsgång.

### Steg 1: Formulera förändringsfrågan

Börja med en fråga som modellen ska hjälpa till att besvara.

Exempel:

- Hur tar vi oss från dagens importflöde till en mer automatiserad målarkitektur?
- Vilka övergångslägen behöver ledningen förstå?
- Vilka initiativ måste samordnas för att riskbedömningen ska fungera?
- Vilka äldre system kan avvecklas när?

Frågan avgör vad som behöver modelleras.

### Steg 2: Välj lägen

Identifiera nuläge, ett eller flera övergångslägen och målarkitektur. Beskriv dem kort i ord innan du börjar modellera.

Exempel:

- Nuläge: äldre importflöde med manuella kontroller och flera separata integrationslösningar.
- Övergångsläge 1: ny riskbedömning i pilot för utvalda ärendetyper.
- Övergångsläge 2: nytt handläggarstöd och gammalt ärendehanteringssystem i samexistens.
- Målarkitektur: sammanhållet digitalt importflöde med modern integration och automatiserat stöd för lågriskärenden.

### Steg 3: Identifiera arkitekturellt viktiga arbetspaket

Välj bara arbetspaket som förändrar arkitekturen på ett sätt som behöver förstås utanför projektgruppen.

Exempel:

- etablera importinformationsmodell,
- införa riskbedömningstjänst,
- införa handläggarstöd,
- modernisera externa integrationer,
- avveckla äldre filöverföringar.

### Steg 4: Koppla arbetspaket till leveranser

För varje arbetspaket: vad blir resultatet?

Skriv leveranserna konkret. Undvik formuleringar som “förbättrad förmåga” om det inte framgår vad som faktiskt finns efteråt.

### Steg 5: Koppla leveranser till arkitekturdelar

Koppla leveranserna till förmågor, processer, applikationstjänster, information och teknik. Det är här modellen börjar ge mer nytta än en vanlig plan.

### Steg 6: Skapa målgruppsanpassade vyer

Alla behöver inte se allt. Ledningen kan behöva se etapper, mål och risker. Portföljstyrningen kan behöva se beroenden. Verksamheten kan behöva se när arbetssätt påverkas. IT-förvaltningen kan behöva se avveckling och samexistens.

## Vanliga misstag

- **Misstag: Att modellera projektplanen i stället för förändringsarkitekturen.**
  - Varför det händer: Det är lätt att börja med aktiviteter, datum och ansvar eftersom det redan finns i projektmaterialet.
  - Hur du undviker det: Modellera bara det som påverkar arkitekturdelar, beroenden, övergångslägen eller beslut.

- **Misstag: Att visa målbilden utan övergångslägen.**
  - Varför det händer: Målbilder är enklare att kommunicera och ser mer strategiska ut.
  - Hur du undviker det: Identifiera minst ett realistiskt övergångsläge när förändringen tar längre tid eller kräver samexistens.

- **Misstag: Att kalla allt för initiativ.**
  - Varför det händer: Organisationer använder ofta initiativ, projekt, leverans och förmåga blandat.
  - Hur du undviker det: Skilj på arbetet som genomförs, resultatet som levereras och arkitekturdelarna som förändras.

- **Misstag: Att modellera för många leveranser.**
  - Varför det händer: När modellen kopplas till portföljstyrning vill många lägga in allt.
  - Hur du undviker det: Ta bara med leveranser som påverkar arkitekturbeslut, beroenden eller uppföljning.

- **Misstag: Att glömma avveckling.**
  - Varför det händer: Nya lösningar får mer uppmärksamhet än gamla lösningar som ska bort.
  - Hur du undviker det: Modellera avveckling som en aktiv del av förändringsresan, inte som något som “bara händer sen”.

- **Misstag: Att inte koppla arbetspaket till mål.**
  - Varför det händer: Projekt kan leva vidare på egen logik efter att de startats.
  - Hur du undviker det: Koppla varje arkitekturellt viktigt arbetspaket till minst ett mål, krav eller princip.

## Övningar

### Övning 1: Gör en förändringsresa

Utgå från Atlantis importmodernisering. Skriv tre korta beskrivningar:

1. Nuläge.
2. Övergångsläge.
3. Målarkitektur.

Håll varje beskrivning till högst fem meningar. Markera sedan vilka verksamhetsförmågor som påverkas i varje läge.

### Övning 2: Skilj på arbete, leverans och arkitekturdel

Sortera följande påståenden i tre grupper: arbetspaket, leverans eller arkitekturdel.

1. Införa riskbedömningstjänst.
2. Riskbedömningstjänst.
3. Pilotdriftsatt riskbedömning för importflöde A.
4. Modernisera externa integrationer.
5. Integrationsplattform.
6. Godkänd importinformationsmodell.
7. Importinformationsmodell.
8. Avveckla äldre filöverföringar.

Diskutera vilka formuleringar som kan behöva förtydligas.

### Övning 3: Hitta beroenden

Välj tre arbetspaket från kapitlet. Skriv för varje arbetspaket:

- vad det behöver från andra arbetspaket,
- vilken leverans det skapar,
- vilka förmågor eller applikationstjänster det påverkar,
- vad som händer om det blir försenat.

### Fördjupning

Välj ett verkligt eller fiktivt förändringsinitiativ i din egen organisation. Skapa en enkel tabell med fyra kolumner:

| Arbetspaket | Leverans | Berörd arkitekturdel | Bidrar till mål |
|---|---|---|---|
| | | | |

Fyll i högst fem rader. Granska sedan om tabellen visar arkitekturella samband eller om den mest är en projektlista. Ta bort det som inte hjälper till att förstå förändringen.

## Små modellpåståenden för förändring

Implementation och migration handlar om att visa hur arkitekturen förändras över tid. Då behöver modellen skilja mellan nuläge, målbild och det arbete som tar organisationen däremellan.

Exempel från Atlantis:

- Arbetspaketet **Inför nytt digitalt importflöde** realiserar leveransen **Första version av digital självservice för deklaranter**.
- Leveransen **Riskbedömning före handläggning** påverkar applikationstjänsten **Riskbedöm importdeklaration**.
- Platån **Målarkitektur 2028** innehåller förmågan **Automatiserad riskprioritering**.
- Gapet mellan nuläge och målbild omfattar både avveckling av manuell dubbelregistrering och införande av en gemensam deklarationsdatakälla.

Med den typen av påståenden kan Atlantis se om ett initiativ faktiskt leder mot målarkitekturen eller bara skapar ännu en lokal lösning.

## Snabb sammanfattning

- Nuläge och målbild räcker ofta inte för att styra komplex förändring.
- Implementation och migration hjälper modellen att visa förändringsresan.
- Övergångslägen gör samexistens, beroenden och temporära kompromisser synliga.
- Arbetspaket beskriver insatser; leveranser beskriver resultat; arkitekturdelar beskriver det som förändras.
- Modellera inte hela projektplanen. Modellera det som har arkitekturell betydelse.
- Koppla förändringsdelar till mål, förmågor, applikationer, information och teknik.
- Avveckling är en del av förändringsarkitekturen och bör inte glömmas bort.
- Den bästa migrationsmodellen hjälper organisationen att prioritera, samordna och följa upp förändring.

## Quiz/reflektionsfrågor

1. Varför är det ofta otillräckligt att bara visa nuläge och målarkitektur?
2. Vad är skillnaden mellan ett arbetspaket och en leverans?
3. Varför kan ett övergångsläge vara viktigt att modellera?
4. När bör en projektaktivitet inte tas med i arkitekturmodellen?
5. Hur kan en migrationsmodell hjälpa portföljstyrning?
6. Vad kan hända om avveckling inte modelleras?
7. Ge ett exempel på hur ett arbetspaket kan kopplas till ett verksamhetsmål.
8. Vilka målgrupper kan behöva olika vyer av samma förändringsresa?

## Nästa steg

Nu har vi modellerat förändringsresan från nuläge till målarkitektur. Nästa kapitel går djupare in i relationerna mellan modellens delar.

Där blir huvudfrågan: vilka samband behöver modellen visa för att ge verklig nytta? Vi kommer att se att relationer ofta är den del av modellen där analysvärdet uppstår, men också den del där många modeller blir antingen för lösa eller för komplicerade.
