# Modellering som gör nytta

**Praktisk ArchiMate-modellering för arkitekter i större myndigheter**

Författare: Erland Lindmark

Detta är ett bokprojekt för en kombinerad lärobok och praktisk handbok om ArchiMate-modellering i större myndigheter.

## Projektets huvudidé

Boken hjälper IT-arkitekter och verksamhetsarkitekter att gå från fristående arkitekturbilder till modeller som kan skapa nytta genom gemensamt språk, spårbarhet, analys, återanvändning och bättre beslutsunderlag.

## Scenario

Boken använder den fiktiva myndigheten **Tullmyndigheten Atlantis** som återkommande scenario.

## Lokal export

Projektet innehåller en lokal exportpipeline.

```bash
./scripts/export-book.sh --format epub
./scripts/export-book.sh --format pdf
./scripts/export-book.sh --format all
```

Exporten förutsätter att Pandoc finns installerat. PDF-export kräver även en Pandoc-kompatibel PDF-motor, exempelvis xelatex.
