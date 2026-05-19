# Kapitel 7: Tekniklagret: när infrastrukturen faktiskt spelar roll

## Varför detta kapitel finns

Tekniklagret är lätt att antingen överanvända eller undvika helt. I vissa arkitekturbilder blir tekniken centrum för allt: servrar, nät, databaser, molnplattformar, säkerhetszoner, brandväggar och driftmiljöer. I andra bilder saknas tekniken helt, även när infrastrukturen är den begränsning som avgör om en förändring är möjlig, dyr, riskabel eller beroende av andra initiativ.

ArchiMate hjälper oss att modellera teknik på ett sätt som kan kopplas till applikationer, verksamhetsbehov och förändringsinitiativ. Poängen är inte att ersätta teknisk dokumentation, konfigurationsdatabaser eller nätverksritningar. Poängen är att visa när tekniska förutsättningar påverkar arkitekturbeslut.

I en större myndighet som Tullmyndigheten Atlantis kan tekniklagret bli viktigt när gamla system ska moderniseras, när informationsutbyte med andra myndigheter ska säkras, när driftmiljöer ska konsolideras eller när nya lösningar behöver uppfylla krav på tillgänglighet, informationssäkerhet och spårbarhet.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara när tekniklagret tillför nytta i en arkitekturmodell,
- skilja mellan teknik som är relevant för beslut och teknik som hör hemma i detaljerad teknisk dokumentation,
- använda tekniklagret för att visa plattformar, noder, teknikberoenden och säkerhetsmässiga förutsättningar,
- koppla tekniska element till applikationer och verksamhetskritiska behov,
- avgöra när tekniklagret kan väljas bort,
- formulera en enkel teknikvy för Tullmyndigheten Atlantis.

## Innan vi börjar

I kapitel 6 arbetade vi med applikationslagret. Där skiljde vi mellan applikationer, applikationstjänster, gränssnitt och informationsflöden. Vi såg att en systemkarta blir mer användbar när den visar vad systemen gör och vilka verksamhetsbehov de stödjer.

Tekniklagret ligger under detta. Det handlar om de tekniska miljöer, plattformar och infrastrukturella förmågor som gör att applikationerna kan köras, kommunicera, lagra data och uppfylla krav.

Men tekniklagret ska inte användas bara för att det finns teknik. Nästan alla IT-miljöer har servrar, nät, databaser, integrationer, övervakning och säkerhetskomponenter. Det betyder inte att allt ska in i arkitekturmodellen.

Den viktiga frågan är:

> Påverkar den tekniska förutsättningen ett arkitekturbeslut, en risk, en kostnad, en förändringsplan eller en verksamhetskritisk egenskap?

Om svaret är ja kan tekniklagret vara värdefullt. Om svaret är nej räcker det ofta att låta detaljerna finnas i andra källor.

## Huvudförklaring

### Tekniklagret är inte en driftkarta

En vanlig missuppfattning är att tekniklagret ska vara en komplett karta över driftmiljön. Då blir modellen snabbt för detaljerad. Den fylls med komponenter som är viktiga för tekniker, men som inte hjälper arkitekter, verksamhet eller ledning att fatta beslut.

En driftkarta kan behöva visa exakt vilka servrar, kluster, portar, brandväggsregler, certifikat, databasscheman och övervakningspunkter som finns. En arkitekturmodell behöver normalt visa något annat: vilka tekniska förutsättningar som påverkar applikationer, tjänster, informationsflöden och förändringar.

Skillnaden kan beskrivas så här:

| Fråga | Drift- eller teknisk dokumentation | Arkitekturmodell |
|---|---|---|
| Vad körs exakt var? | Ofta relevant | Bara ibland relevant |
| Vilka tekniska miljöer finns? | Relevant | Relevant när miljöerna påverkar beslut |
| Vilka applikationer är beroende av en plattform? | Ibland relevant | Ofta relevant |
| Vilka säkerhetszoner påverkar informationsutbyte? | Relevant | Relevant om zonerna påverkar arkitekturval |
| Vilka komponenter behöver bytas vid modernisering? | Relevant | Relevant på lagom abstraktionsnivå |

Tekniklagret blir alltså mest användbart när det visar tekniska beroenden på en nivå som kan diskuteras i arkitekturarbetet.

### När tekniklagret är rätt startpunkt

I många fall bör man börja med verksamhets- eller applikationslagret. Men ibland är tekniklagret den bästa startpunkten.

Det gäller till exempel när:

- en teknisk plattform är på väg att avvecklas,
- en säkerhetszon begränsar hur information får flöda,
- en integrationsplattform är flaskhals eller strategiskt vägval,
- en applikation inte kan förändras på grund av driftmiljö eller teknikskuld,
- ett nytt krav handlar om tillgänglighet, redundans, loggning eller spårbarhet,
- ett moln-, container- eller plattformsinitiativ påverkar flera applikationer,
- en myndighet behöver förstå konsekvensen av att flytta drift mellan miljöer.

För Atlantis kan ett exempel vara att den gamla applikationen för importkontroll körs i en äldre driftmiljö som inte längre är strategisk. Om moderniseringsprogrammet bara ser applikationen som en ruta på en systemkarta missar man kanske att flera andra applikationer delar samma plattform, samma databasprodukt, samma integrationsmönster eller samma säkerhetszon.

Då kan tekniklagret hjälpa till att visa varför en till synes liten applikationsförändring egentligen är en större teknisk förändring.

### Vad man kan modellera i tekniklagret

På grundnivå räcker det ofta med ett fåtal typer av tekniska element. Man behöver inte använda allt som språket erbjuder.

För en praktisk arkitekturmodell kan följande vara en rimlig start:

| Teknikbegrepp | Praktisk betydelse | Exempel i Atlantis |
|---|---|---|
| Nod | En teknisk miljö eller körningsplats | Myndighetens interna driftplattform |
| Teknikkomponent | En teknisk komponent som stödjer applikationer | Integrationsplattform, meddelandekö, databastjänst |
| Tekniktjänst | En teknisk tjänst som andra delar använder | Autentisering, loggning, filöverföring |
| Artefakt | En teknisk leverans eller fysisk representation | Driftsatt applikationspaket, konfigurationspaket |
| Kommunikationsnät | Förbindelse eller nätstruktur | Säker förbindelse till annan myndighet |
| Systemprogramvara | Programvara som applikationer körs på | Databasplattform, applikationsserver |

I praktiken ska man välja de element som behövs för att svara på modellens fråga. Om frågan handlar om modernisering av importflödet behöver modellen kanske visa driftplattformar, integrationsteknik och säkerhetszoner. Om frågan handlar om verksamhetsansvar behövs tekniklagret kanske inte alls.

### Teknikberoenden som arkitekturfråga

Teknikberoenden är ofta osynliga tills de blir problem. En applikation kan se enkel ut i en systemkarta, men vara beroende av en databasversion, en äldre integrationslösning, ett nätsegment, ett autentiseringssätt eller en särskild driftmiljö.

När dessa beroenden modelleras på rätt nivå kan de stödja frågor som:

- Vilka applikationer påverkas om en plattform avvecklas?
- Vilka verksamhetsförmågor påverkas om en teknikkomponent fallerar?
- Vilka informationsflöden passerar en viss säkerhetszon?
- Vilka förändringar måste samordnas i samma release eller program?
- Var finns teknikskuld som begränsar verksamhetsutveckling?

I Atlantis kan importflödet vara beroende av en integrationsplattform som används av flera delar av myndigheten. Om plattformen har begränsad kapacitet eller är svår att förändra är den inte bara en teknisk detalj. Den är en arkitekturfaktor.

### Säkerhetszoner och tekniska gränser

I en statlig myndighet är tekniska gränser ofta nära kopplade till informationssäkerhet. Det kan handla om interna och externa zoner, skyddsvärd information, åtkomstkontroll, loggning, integration med andra myndigheter och krav på robusthet.

Det betyder inte att arkitekturmodellen ska ersätta säkerhetsarkitektur eller informationsklassning. Men den kan visa var tekniska gränser påverkar designen.

Exempel:

- Ett riskanalysflöde behöver data från externa aktörer.
- Informationen får inte flöda direkt in i den interna handläggningsmiljön.
- En mottagningszon, valideringstjänst och integrationsplattform behövs innan informationen kan användas.
- Flera applikationer blir beroende av samma tekniska säkerhetsmönster.

En enkel teknikvy kan då visa varför en lösning behöver fler steg än verksamheten först trodde. Det blir inte en bild över alla brandväggar. Det blir en modell över tekniska gränser som påverkar lösningsval.

### Tekniklagret ska kopplas uppåt

Ett tekniklager som bara visar teknik blir ofta isolerat. För att skapa arkitekturnytta behöver det kopplas till applikations- och verksamhetslager.

En användbar kedja kan se ut så här i modellen:

- Teknikkomponenten “Integrationsplattform för myndighetssamverkan” stödjer applikationstjänsten “Ta emot deklarationsunderlag”.
- Applikationstjänsten används av verksamhetsprocessen “Förbereda importkontroll”.
- Processen realiserar delar av förmågan “Genomföra riskbaserad varukontroll”.
- Förmågan är kritisk för målet “Kortare ledtid utan sämre kontrollkvalitet”.

När kedjan finns kan tekniken diskuteras som mer än infrastruktur. Den blir en del av konsekvensanalysen.

Om integrationsplattformen är instabil påverkar det inte bara IT. Det påverkar importkontroll, riskbedömning, handläggningstid och myndighetens mål.

### Lagom teknisk detaljnivå

En praktisk regel är att tekniklagret ska visa tekniska saker som har arkitektureffekt. Detaljnivån ska vara tillräcklig för beslut, men inte så hög att modellen blir en sämre kopia av driftverktygen.

För låg detaljnivå:

- “Teknisk plattform” som enda ruta.
- Alla beroenden blir osynliga.
- Det går inte att se varför en förändring är svår.

För hög detaljnivå:

- Varje server, brandväggsregel och teknisk instans ritas in.
- Modellen blir svår att läsa.
- Den kräver ständig uppdatering.
- Den används inte av andra än teknikspecialister.

Lagom detaljnivå:

- Strategiskt viktiga plattformar visas.
- Kritiska tekniska tjänster visas.
- Säkerhetszoner visas när de påverkar flöden.
- Beroenden till applikationer och förmågor visas.
- Detaljer hänvisas till teknisk dokumentation.

## Exempel: Atlantis moderniserar importkontrollen

Tullmyndigheten Atlantis planerar att modernisera importkontrollen. I den första diskussionen beskrivs förändringen som ett applikationsbyte: det gamla importkontrollsystemet ska ersättas av en ny lösning.

En arkitekt börjar med en enkel applikationsvy och ser att flera applikationer är inblandade:

- Importkontrollsystemet,
- Ärendehanteringssystemet,
- Riskanalysplattformen,
- Dokumentmottagning,
- Integrationsplattformen,
- Rapporteringslösningen.

Detta är användbart, men fortfarande otillräckligt. När arkitekten kopplar in tekniklagret syns fler beroenden:

- Importkontrollsystemet körs i en äldre intern driftmiljö.
- Riskanalysplattformen använder en separat analysmiljö.
- Dokumentmottagning ligger i en mottagningszon för externa filer.
- Integrationsplattformen är gemensam för flera myndighetssamverkansflöden.
- Vissa informationsflöden måste passera validering och loggning innan de når handläggningsmiljön.
- Den äldre databastjänsten används även av andra applikationer som inte ingår i moderniseringsprogrammet.

Modellen visar att moderniseringen inte bara är ett applikationsbyte. Den påverkar driftmiljö, integration, säkerhetszoner och gemensamma tekniska tjänster.

Det leder till tre bättre beslut:

- Programmet behöver samordnas med plattformsförvaltningen.
- Migreringen måste planeras tillsammans med andra beroende applikationer.
- Målarkitekturen behöver visa både applikationsförändring och teknisk förändring.

Utan tekniklagret hade detta kanske upptäckts sent, när lösningen redan var designad eller upphandlad.

## När du ska använda tekniklagret

Använd tekniklagret när det hjälper dig att visa en teknisk förutsättning som påverkar beslut.

Typiska situationer:

- Du behöver förstå konsekvenser av teknisk skuld.
- Du ska visa beroenden till en plattform som ska avvecklas.
- Du behöver förklara varför en förändring kräver samordning med drift eller säkerhet.
- Du ska analysera robusthet, tillgänglighet eller återställningsförmåga på arkitekturnivå.
- Du behöver visa hur applikationer använder gemensamma tekniska tjänster.
- Du vill koppla teknikinitiativ till verksamhetsnytta.

I dessa situationer gör tekniklagret modellen mer användbar.

## När du kan låta bli

Låt bli tekniklagret när tekniken inte behövs för frågan.

Det gäller till exempel när:

- modellen ska förklara verksamhetsansvar,
- syftet är att beskriva en process på konceptuell nivå,
- applikationernas tekniska miljö inte påverkar beslutet,
- detaljerna redan finns i teknisk dokumentation och inte behöver lyftas in,
- målgruppen inte behöver teknisk information för att förstå budskapet,
- risken är att tekniska detaljer skymmer den verksamhetsmässiga poängen.

Det är inte ett misslyckande att välja bort tekniklagret. Tvärtom kan det vara ett tecken på god modelleringsdisciplin.

## Vanliga misstag

- **Misstag: Att göra tekniklagret till en komplett infrastrukturkarta.**
  - Varför det händer: Det finns mycket teknisk information tillgänglig och det känns tryggt att rita in allt.
  - Hur du undviker det: Modellera bara tekniska element som påverkar modellens fråga eller beslut.

- **Misstag: Att hoppa direkt till teknik när problemet egentligen är verksamhetsmässigt.**
  - Varför det händer: IT-organisationer är ofta vana att beskriva problem genom system och plattformar.
  - Hur du undviker det: Börja med frågan. Om frågan handlar om ansvar, process eller förmåga ska du börja högre upp.

- **Misstag: Att modellera tekniska detaljer utan koppling till applikationer eller verksamhet.**
  - Varför det händer: Teknikvyn skapas isolerat av teknikspecialister.
  - Hur du undviker det: Koppla tekniska tjänster och plattformar till applikationstjänster, applikationer eller förmågor.

- **Misstag: Att använda tekniklagret för att dölja osäkerhet.**
  - Varför det händer: Detaljerade tekniska bilder kan se imponerande ut även när beslutsfrågan är oklar.
  - Hur du undviker det: Skriv modellens fråga högst upp i arbetet och kontrollera att varje tekniskt element bidrar till svaret.

- **Misstag: Att glömma att tekniska modeller åldras snabbt.**
  - Varför det händer: Infrastruktur och plattformar förändras ofta genom drift, säkerhetsarbete och livscykelhantering.
  - Hur du undviker det: Modellera stabila arkitekturaspekter och hänvisa till operativa källor för detaljer som ändras ofta.

## Övningar

### Övning 1: Hitta teknikfrågan

Välj en arkitekturbild från din egen organisation som innehåller tekniska komponenter.

Besvara följande frågor:

1. Vilken fråga ska bilden hjälpa till att besvara?
2. Vilka tekniska detaljer är nödvändiga för att besvara frågan?
3. Vilka tekniska detaljer finns med mest av vana?
4. Vilka detaljer borde ligga i teknisk dokumentation i stället för i arkitekturmodellen?

Skriv sedan om bildens syfte i en mening.

### Övning 2: Skapa en enkel teknikvy för Atlantis

Utgå från scenariot där Atlantis moderniserar importkontrollen.

Skapa en enkel teknikvy som visar:

- en äldre intern driftmiljö,
- en mottagningszon för externa uppgifter,
- en integrationsplattform,
- en analysmiljö,
- minst två applikationer som är beroende av dessa tekniska miljöer,
- ett informationsflöde som påverkas av en teknisk eller säkerhetsmässig gräns.

Håll modellen enkel. Syftet är inte att visa all teknik, utan att visa varför moderniseringen påverkar mer än en applikation.

### Övning 3: Välj bort tekniklagret

Tänk dig att Atlantis ska förklara för ledningen vilka verksamhetsförmågor som påverkas av ett nytt EU-regelverk.

Besvara:

1. Behövs tekniklagret i den första modellen?
2. Vilken modellvy skulle vara mer användbar?
3. När skulle tekniklagret eventuellt behöva läggas till senare?

Syftet är att träna på att inte använda tekniklagret när det inte behövs.

### Fördjupning

Välj ett verkligt tekniskt beroende i din organisation, till exempel en integrationsplattform, autentiseringstjänst, databasplattform eller driftmiljö.

Beskriv beroendet på tre nivåer:

1. Teknisk nivå: vad är det?
2. Applikationsnivå: vilka applikationer använder det?
3. Verksamhetsnivå: vilka förmågor, processer eller tjänster påverkas om det förändras?

Reflektera sedan över vilken nivå som är mest relevant för olika målgrupper.

## Små modellpåståenden i tekniklagret

Tekniklagret blir användbart när tekniska beroenden påverkar beslut, risk eller genomförbarhet. Då räcker det inte att säga att ett system finns i en miljö. Modellen behöver visa vilka tekniska förutsättningar som faktiskt spelar roll.

Exempel från Atlantis:

- Noden **Integrationsplattform** exekverar applikationskomponenten **Meddelandeförmedling**.
- Teknikkomponenten **Databasplattform** stödjer applikationskomponenten **Ärendehanteringssystemet**.
- Tekniknätverket **Säker myndighetszon** används för informationsutbyte mellan kontrollsystem och interna beslutsstöd.
- Teknikberoendet till en äldre plattform begränsar möjligheten att införa realtidsanalys.

Poängen är inte att modellera all infrastruktur. Poängen är att synliggöra de tekniska beroenden som förändrar bedömningen av tid, risk, kostnad eller säkerhet.

## Snabb sammanfattning

- Tekniklagret ska inte ersätta driftkartor eller teknisk dokumentation.
- Använd tekniklagret när tekniska förutsättningar påverkar arkitekturbeslut, risker, kostnader eller förändringsplaner.
- Modellera teknik på lagom nivå: plattformar, tekniska tjänster, säkerhetszoner och kritiska beroenden.
- Koppla teknik uppåt till applikationer, verksamhetsförmågor och mål.
- Välj bort tekniklagret när tekniken inte hjälper till att besvara modellens fråga.
- I en myndighetsmiljö kan tekniklagret vara särskilt viktigt för säkerhet, robusthet, samverkan och modernisering av äldre miljöer.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan en teknisk driftkarta och en arkitekturmodell med tekniklager?
2. När är tekniklagret en bra startpunkt?
3. Varför bör tekniska element kopplas till applikationer eller verksamhetsförmågor?
4. Vilken risk uppstår om tekniklagret blir för detaljerat?
5. Ge ett exempel på en teknisk förutsättning som kan påverka ett verksamhetsbeslut.
6. När bör tekniklagret väljas bort?

## Nästa steg

Nu har vi gått igenom verksamhetslagret, applikationslagret och tekniklagret. Tillsammans hjälper de oss att beskriva vad organisationen gör, vilka applikationer som stödjer detta och vilka tekniska förutsättningar som påverkar möjligheten att förändra.

Men arkitektur handlar inte bara om nuläge och struktur. Den behöver också kopplas till varför en förändring behövs. I nästa kapitel går vi därför vidare till motivation och strategi: mål, drivkrafter, krav och principer.
