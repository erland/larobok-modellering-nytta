# Kapitel 4: Modellnytta i en myndighetskontext

## Varför detta kapitel finns

De tidigare kapitlen har etablerat tre grundidéer. En modell är mer än en bild. En modell ska börja med en fråga. ArchiMate är ett språk som kan hjälpa oss att uttrycka modellen konsekvent.

Nu behöver vi placera detta i den miljö där boken utspelar sig: en större statlig myndighet. Det är en miljö där arkitektur sällan handlar om ett enskilt system eller ett enskilt projekt. Den handlar ofta om ansvar, regelverk, informationsflöden, långlivade system, budgetramar, säkerhetskrav, verksamhetsmål, samverkan och förändringar som måste ske utan att den dagliga verksamheten stannar.

I en sådan miljö räcker det sällan med en vacker bild över nuläget. Bilden kan hjälpa i ett möte, men den kan snabbt tappa värde när någon vill veta vad som påverkas, vilka beroenden som finns, vilka beslut som redan är fattade eller vilka delar av verksamheten som behöver prioriteras.

Tullmyndigheten Atlantis har många typiska myndighetsutmaningar. Myndigheten behöver hantera import och export, stödja kontrollverksamhet, dela information med andra myndigheter, följa lagar och förordningar, skydda känsliga uppgifter och samtidigt modernisera ett applikationslandskap som vuxit fram under lång tid. Flera av frågorna är inte rena IT-frågor. De är verksamhetsfrågor, styrningsfrågor och förändringsfrågor.

Det här kapitlet handlar därför om modellnytta: på vilka sätt en arkitekturmodell kan hjälpa en myndighet att förstå, prioritera, samordna och fatta beslut.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför modellnytta i en myndighet ofta handlar om mer än systemdokumentation,
- beskriva hur modeller kan stödja styrning, konsekvensanalys, portföljprioritering och samverkan,
- skilja mellan lokal projektbild och gemensam myndighetsmodell,
- identifiera situationer där modellering ger tydligare nytta än fristående bilder,
- resonera om när en modell behöver vara spårbar, återanvändbar och förvaltad,
- se hur Tullmyndigheten Atlantis kan använda modeller som beslutsunderlag.

## Innan vi börjar

När någon säger att “vi behöver en arkitekturbild” kan det betyda många olika saker. Det kan betyda att ledningen vill förstå ett förändringsinitiativ. Det kan betyda att en projektgrupp vill visa ett systemflöde. Det kan betyda att säkerhetsfunktionen vill förstå informationsutbyte. Det kan också betyda att förvaltningen vill veta vilka applikationer som är beroende av en viss integrationslösning.

Alla dessa behov kan resultera i bilder, men de kräver inte samma typ av modellering. En enklare bild kan räcka när syftet är att skapa en gemensam ögonblicksbild i ett enskilt möte. En modell blir mer värdefull när informationen behöver återanvändas, jämföras, kvalitetssäkras, förvaltas eller kopplas till andra frågor.

En praktisk tumregel är:

> Modellering blir särskilt värdefull när samma arkitekturinformation behöver användas mer än en gång, av mer än en målgrupp eller i mer än ett beslut.

I en större myndighet inträffar detta ofta. Frågor återkommer. Beslut påverkar varandra. System är långlivade. Regelverk förändras. Projekt avslutas, men deras konsekvenser lever kvar.

## Myndigheten som arkitekturmiljö

En större statlig myndighet skiljer sig från ett litet produktteam på flera sätt. Den har ofta ett bredare uppdrag, fler intressenter och längre livscykler. Den behöver inte bara leverera nya lösningar, utan också säkerställa rättssäkerhet, kontinuitet, informationssäkerhet, spårbarhet och förmåga att följa regelverk.

För Tullmyndigheten Atlantis innebär detta att arkitekturen inte bara ska stödja digitalisering i största allmänhet. Den ska stödja ett myndighetsuppdrag. När Atlantis moderniserar importflödet påverkas till exempel:

- handläggare som ska fatta korrekta beslut,
- kontrollverksamhet som behöver riskinformation,
- externa aktörer som lämnar uppgifter,
- andra myndigheter som tar emot eller delar information,
- applikationer som hanterar ärenden, beslut och meddelanden,
- regelverk som styr vad som får göras och dokumenteras,
- säkerhetskrav som styr åtkomst, loggning och informationsutbyte.

Om varje projekt ritar sin egen bild blir det svårt att se helheten. En projektbild kan vara korrekt för projektets syfte men ändå sakna koppling till myndighetens förmågor, processer, informationsobjekt, mål och beroenden.

En gemensam modell behöver inte innehålla allt. Den behöver däremot innehålla de delar som myndigheten återkommande behöver förstå och styra.

## Fem typer av modellnytta

Modellnytta är inte en enda sak. Olika målgrupper har olika nytta av samma modell, och ibland behöver modellen presenteras genom olika vyer. I en myndighetskontext är fem nyttor särskilt viktiga.

### Gemensamt språk

Den första nyttan är ett gemensamt språk. När verksamhet, IT, säkerhet och ledning använder olika ord för samma sak blir arkitekturdiskussioner snabbt otydliga.

I Atlantis kan en grupp tala om “importsystemet”, en annan om “ärendehanteringen”, en tredje om “klareringsplattformen” och en fjärde om “den nya digitala kanalen”. I praktiken kan dessa ord överlappa, men de betyder inte alltid samma sak.

En modell kan hjälpa genom att skilja på exempelvis verksamhetsförmåga, process, applikation, applikationstjänst och informationsobjekt. Det betyder inte att alla behöver använda ArchiMate-termer i varje möte. Det betyder att arkitekterna har en konsekvent struktur bakom kommunikationen.

### Konsekvensanalys

Den andra nyttan är konsekvensanalys. En myndighet behöver ofta förstå vad som påverkas om något ändras.

Om Atlantis vill ersätta en äldre integrationsplattform räcker det inte att veta vilka tekniska komponenter som finns. Myndigheten behöver veta vilka applikationer som använder plattformen, vilka informationsflöden som passerar genom den, vilka verksamhetsprocesser som berörs och vilka externa parter som påverkas.

En fristående bild kan visa ett utsnitt. En modell kan göra det möjligt att följa relationer mellan flera utsnitt. Det är här relationerna börjar skapa konkret värde.

### Prioritering och portföljstyrning

Den tredje nyttan är prioritering. Större myndigheter har nästan alltid fler förändringsbehov än de kan genomföra samtidigt. Då behövs underlag för att prioritera.

En modell kan hjälpa till att visa vilka initiativ som stödjer viktiga verksamhetsförmågor, vilka applikationer som är särskilt kritiska, vilka beroenden som gör vissa förändringar svåra och var flera initiativ påverkar samma område.

I Atlantis kan flera initiativ samtidigt vilja förändra importflödet: ett initiativ för automatiserad riskanalys, ett för ny digital inlämning, ett för modernare integrationsmönster och ett för förbättrad kontrolluppföljning. Utan modell blir det lätt fyra separata berättelser. Med modell kan man börja se överlapp, beroenden och möjliga sekvenser.

### Spårbarhet från mål till lösning

Den fjärde nyttan är spårbarhet. Myndigheter behöver ofta kunna visa varför en förändring görs och hur den hänger ihop med uppdrag, mål, krav och lösningar.

Det räcker inte alltid att säga att ett system ska moderniseras. Frågan är varför moderniseringen är viktig. Är syftet kortare handläggningstid, bättre datakvalitet, högre informationssäkerhet, bättre kontrollförmåga eller minskad teknisk risk?

En modell kan koppla mål och drivkrafter till förmågor, processer, applikationer och förändringsinitiativ. Den kopplingen gör det lättare att se om ett initiativ verkligen stödjer det man säger att det ska stödja.

### Samverkan över organisatoriska gränser

Den femte nyttan är samverkan. En myndighet arbetar sällan helt ensam. Den behöver samverka med andra myndigheter, departement, leverantörer, internationella aktörer, företag och medborgare.

I Atlantis kan informationsutbyte med andra myndigheter vara avgörande för riskanalys och kontroll. Om varje part bara har sin egen bild av informationsflödet blir diskussionen känslig för missförstånd. En modell kan ge ett mer stabilt sätt att beskriva aktörer, tjänster, informationsobjekt och ansvar.

Det betyder inte att alla externa parter måste dela samma modelleringsverktyg. Men Atlantis kan använda sin egen modell för att skapa tydligare vyer, bättre frågor och mer konsekventa beslutsunderlag.

## Lokal projektbild eller gemensam modell

En vanlig fallgrop i större organisationer är att varje projekt skapar sin egen arkitekturbild. Det är förståeligt. Projektet behöver snabbt förklara sitt omfång, sina beroenden och sin målbild.

Problemet uppstår när projektbilden blir den enda arkitekturrepresentationen. När projektet avslutas försvinner ofta sammanhanget. Bilden kanske sparas i en presentation, men den blir inte en levande del av myndighetens arkitekturkunskap.

Skillnaden kan beskrivas så här:

| Fråga | Lokal projektbild | Gemensam myndighetsmodell |
|---|---|---|
| Primärt syfte | Förklara ett projekt | Bygga återanvändbar arkitekturkunskap |
| Livslängd | Ofta begränsad till projektet | Behöver förvaltas över tid |
| Struktur | Anpassad till presentationen | Bygger på gemensamma begrepp och relationer |
| Återanvändning | Begränsad | Möjlig i flera vyer och analyser |
| Risk | Blir snabbt inaktuell | Kräver ansvar och kvalitet men ger större nytta |

Det betyder inte att projektbilder är fel. Projektbilder kan vara mycket värdefulla. Men om de bygger på en gemensam modell kan de bli både tydligare och mer hållbara. Bilden blir då en vy av modellen, inte en isolerad ritning.

## Atlantis: modernisering av importflödet

Låt oss återvända till Atlantis. Myndigheten vill modernisera importflödet. I början finns flera bilder:

- en processbild över nuvarande importhantering,
- en systemkarta över berörda applikationer,
- en målbild från ett digitaliseringsprogram,
- en integrationsbild från en teknisk förstudie,
- en ledningsbild som visar förväntade effekter.

Varje bild fyller ett syfte. Men de är svåra att jämföra. De använder olika namn, olika detaljeringsnivå och olika avgränsningar. En applikation som är central i systemkartan finns bara som en liten ruta i målbilden. Ett informationsflöde som är viktigt i den tekniska förstudien syns inte i processbilden. Ledningsbilden talar om “snabbare klarering”, men kopplingen till processer och applikationer är otydlig.

Ett modelleringsarbete behöver inte börja med att ersätta alla bilder. Ett bättre första steg är att identifiera vilka frågor Atlantis faktiskt behöver svara på.

Exempel:

- Vilka verksamhetsförmågor påverkas av importmoderniseringen?
- Vilka processer och applikationer stödjer dessa förmågor idag?
- Vilka informationsflöden är kritiska för riskanalys och beslut?
- Vilka initiativ påverkar samma applikationer eller informationsobjekt?
- Vilka beroenden behöver ledningen förstå innan prioritering?

När frågorna är tydliga kan arkitekterna börja skapa en minimal användbar modell. Den kan innehålla ett urval av förmågor, processer, applikationer, applikationstjänster, informationsobjekt och förändringsinitiativ. Den behöver inte vara komplett för hela myndigheten. Den behöver vara tillräckligt strukturerad för att stödja de beslut Atlantis står inför.

## När modellering ger mer nytta än bilder

Det finns situationer där en bild är fullt tillräcklig. Om syftet är att förklara en idé snabbt, skapa diskussion eller visa en grov riktning kan en enkel bild vara rätt verktyg.

Modellering ger däremot mer nytta när något av följande gäller:

- samma information behöver användas i flera sammanhang,
- flera målgrupper behöver olika vyer av samma verklighet,
- beroenden behöver följas över flera lager,
- beslut kräver spårbarhet från mål till lösning,
- förändringar behöver jämföras eller prioriteras,
- arkitekturinformation behöver leva vidare efter ett projekt,
- man behöver kunna se vad som saknas eller motsäger annat i modellen.

I Atlantis är moderniseringen av importflödet ett tydligt exempel. Det är inte en engångspresentation. Det är ett förändringsområde där beslut kommer att fattas under lång tid. Då blir modellen en arbetsyta för kunskap, inte bara ett presentationsmaterial.

## När modellering inte bör överdrivas

Samtidigt ska en större myndighet vara försiktig med att göra modellering tyngre än nyttan motiverar. Om modellering uppfattas som extra administration kommer den att väljas bort eller göras mekaniskt.

Modellering bör inte överdrivas när:

- frågan är tillfällig och enkel,
- målgruppen inte behöver spårbarhet eller återanvändning,
- detaljerna förändras snabbare än modellen hinner förvaltas,
- ingen äger modellens kvalitet efter att den skapats,
- modellen mest skapas för att uppfylla en mall,
- symbolvalet tar mer energi än frågan modellen ska besvara.

Det praktiska målet är inte maximal modellering. Målet är lagom modellering med tydlig nytta.

En bra fråga att ställa är:

> Vad blir möjligt att förstå, besluta eller återanvända tack vare att vi modellerar detta?

Om svaret är otydligt bör modellen förenklas, avgränsas eller vänta.

## Modellnytta kräver arbetssätt

En modell skapar inte nytta bara för att den finns. Den behöver användas i riktiga arbetssituationer.

För Atlantis kan det innebära att modellen används i:

- portföljmöten där initiativ prioriteras,
- arkitekturforum där lösningsförslag granskas,
- verksamhetsdialoger om förmågor och processer,
- säkerhetsdialoger om informationsflöden och beroenden,
- förvaltningsplanering där teknisk skuld och förändringsbehov diskuteras,
- programstyrning där flera initiativ påverkar samma målbild.

Det är först när modellen används i sådana sammanhang som den blir mer än dokumentation. Den blir ett stöd för gemensam förståelse och bättre beslut.

Det innebär också att modellen måste ha en rimlig kvalitetsnivå. Den behöver inte vara perfekt, men den behöver vara tillräckligt korrekt för det den används till. Om modellen används för ledningsprioritering måste centrala beroenden vara trovärdiga. Om den används för teknisk konsekvensanalys måste relationerna vara mer detaljerade. Kvalitetskravet följer användningen.

## Vanliga misstag

- **Misstag: Att beskriva modellnytta som “bättre bilder”.**
  - Varför det händer: Bilder är det synliga resultatet av modelleringsarbetet.
  - Hur du undviker det: Beskriv nyttan i termer av återanvändning, analys, spårbarhet och beslut.

- **Misstag: Att börja med hela myndigheten.**
  - Varför det händer: Arkitektur känns ofta som något som borde täcka allt.
  - Hur du undviker det: Börja med ett viktigt förändringsområde, till exempel importmoderniseringen i Atlantis.

- **Misstag: Att modellera för arkitekterna men inte för besluten.**
  - Varför det händer: Arkitekter kan bli engagerade i struktur och notation.
  - Hur du undviker det: Koppla varje modellutsnitt till en fråga, målgrupp och beslutssituation.

- **Misstag: Att skapa projektmodeller som inte lever vidare.**
  - Varför det händer: Projekt har kortare tidshorisont än myndighetens arkitektur.
  - Hur du undviker det: Låt projektvyer bygga på eller bidra till en gemensam modell där det finns återanvändbar information.

- **Misstag: Att kräva för hög modellmognad för tidigt.**
  - Varför det händer: Organisationen vill snabbt skapa ordning.
  - Hur du undviker det: Inför en liten startmängd, enkla kvalitetsregler och tydliga användningsfall.

## Övningar

### Övning 1: Hitta modellnyttan

Välj en aktuell eller tänkt förändring i din organisation. Skriv ned tre skäl till att en vanlig arkitekturbild kan vara otillräcklig.

Formulera sedan en mening enligt mallen:

> Vi behöver en modell, inte bara en bild, eftersom ...

### Övning 2: Identifiera återanvändbar information

Tänk dig att Atlantis ska modernisera importflödet. Vilken information skulle sannolikt behöva återanvändas i flera sammanhang?

Välj fem saker från listan nedan och motivera varför:

- verksamhetsförmågor,
- processer,
- applikationer,
- informationsobjekt,
- integrationsflöden,
- mål,
- krav,
- initiativ,
- externa aktörer,
- tekniska plattformar.

### Övning 3: Från projektbild till modell

Ta en befintlig arkitekturbild från ett projekt, eller föreställ dig en sådan bild. Markera vilka delar som bara är presentationsstöd och vilka delar som borde finnas som strukturerade modellelement.

Reflektera över:

1. Vilka delar behöver återanvändas efter projektet?
2. Vilka relationer behöver vara tydliga?
3. Vilka målgrupper skulle behöva andra vyer av samma information?

### Fördjupning

Beskriv ett arkitekturforum i Tullmyndigheten Atlantis. Vilka tre modelleringsfrågor skulle forumet kunna använda för att prioritera förändringar i importflödet?

Undvik att börja med symboler. Börja med de beslut forumet behöver fatta.

## Snabb sammanfattning

- Modellnytta i en myndighet handlar ofta om styrning, konsekvensanalys, prioritering, spårbarhet och samverkan.
- En lokal projektbild kan vara användbar, men den blir ofta svår att återanvända över tid.
- En gemensam modell behöver inte täcka allt, men den bör innehålla den arkitekturinformation som återkommer i flera frågor och beslut.
- Modellering ger mest nytta när flera målgrupper behöver olika vyer av samma underliggande verklighet.
- Modellering bör inte överdrivas. Den ska vara lagom omfattande och tydligt kopplad till användning.
- En modell skapar verklig nytta först när den används i möten, analyser, prioriteringar och beslut.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan en lokal projektbild och en gemensam myndighetsmodell?
2. Varför är konsekvensanalys ofta en viktig modellnytta i en större myndighet?
3. När kan en enkel bild vara ett bättre val än en modell?
4. Vad innebär spårbarhet från mål till lösning?
5. Hur kan en modell hjälpa flera initiativ att undvika överlappande eller motstridiga förändringar?
6. Vilka risker uppstår om modellering införs som en tung mall snarare än som ett stöd för beslut?

## Nästa steg

I nästa kapitel går vi in i verksamhetslagret. Där börjar vi titta närmare på när det är klokt att starta modelleringen med förmågor, processer, aktörer och verksamhetstjänster.

Det blir ett viktigt steg för Atlantis, eftersom många arkitekturfrågor i en myndighet inte börjar med teknik. De börjar med vad myndigheten behöver kunna göra, vilka uppgifter den har och vilka verksamhetsförmågor som behöver utvecklas.
