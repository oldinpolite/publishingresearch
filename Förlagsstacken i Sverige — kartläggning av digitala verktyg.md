# Förlagsstacken i Sverige — kartläggning av digitala verktyg

Sammanställd 2026-08-31. Underlag inför användarintervjuer.
Interaktiv version: https://claude.ai/code/artifact/f27a77e4-2287-4b5d-83e6-7d0be385e2c8

## Sammanfattning

1. **Metadatalagret är löst och icke-vinstdrivande.** Bokinfo (2003, tidigare Bokrondellen) ägs av Bonnierförlagen, Norstedts, Natur & Kultur och Förlagssystem. Drivs utan vinstsyfte, är branschens enda databas. Integrera mot den, konkurrera inte.
2. **Toppen av marknaden är stängd.** Mockingbird — byggt av Bonnierförlagen från 2015, eget bolag 2022 med Storytel Books — licensieras av Norstedts (2020) och Natur & Kultur (2024).
3. **Mellansegmentet ägs av Bokdata** (svensk SaaS: produktionssystem, metadata, royalty & rights, försäljningsimport, Insights, Fortnox). Majoritetsägare i Förlagsekonomi sedan 2022. Kunder: Pirat, WAPI, Tukan, Mondial.
4. **Internationella förlags-ERP:er (Klopotek, knk, Virtusales BiblioSuite) saknar svenska referenser.**
5. **Het punkt just nu: försäljningsdata + författarutbetalningar.** Edda Pay (2024, Trollhättan, tre Storytel-alumner, 5,75 Mkr med Almi Invest). Pilot Storytel + Lind & Co; maj 2026 samarbeten med Förlagssystem och The Book Affair.
6. **Digital distribution konsolideras nordiskt:** Elib → Axiell Media → Publizon (2023) → WeDoBooks (köpte Libreka 2025). Parallellt Bokinfo digital och Publit.
7. **Långsvansen är stor och illa försörjd:** 19 000+ titlar 2025, ~1 000 förlag hos Förlagssystem, men bara 63 förlag rapporterar till förlagsstatistiken.
8. **Två regulatoriska klockor:** tillgänglighetslagen (2023:254) för e-böcker sedan 28 juni 2025 utan utpekad teknisk standard; DSM-direktivets transparenskrav.

## Marknaden i siffror

| Mått | Värde | Källa |
|---|---|---|
| Bokförsäljning till slutkonsument 2024 | 5,15 mdr kr | Bokförsäljningsstatistiken |
| Tillväxt 2025 | +6,3 % (fysisk bokhandel +7,3 %) | Bokförsäljningsstatistiken 2025 |
| Andel digitala abonnemangstjänster 2024 | 32,7 % | " |
| Kanaler 2024 | internetbokhandel/bokklubbar 40,2 %, abonnemang 32,7 %, fysisk bokhandel 23,2 %, dagligvaru 3,9 % | " |
| SvF-medlemsförlagens omsättning 2024 | 2 178,6 Mkr, 63 rapporterande förlag | Förlagsstatistik 2024 |
| Format hos medlemsförlagen 2024 | inbundet 50,9 %, ljudbok 35,2 %, pocket 9,0 %, e-bok 4,9 % | " |
| Utgivna titlar 2025 | 19 000+ (+16 %) | KB Utgivningspuls |

OBS: Bokförsäljningsstatistiken (slutkonsument) och Förlagsstatistiken (förlagens nettointäkter) är inte jämförbara.

## Värdekedjan

1. **Förvärv & avtal** — Mockingbird, Bokdata; annars Word/Excel. FRAGMENTERAT
2. **Redaktion & manus** — Word, Google Docs, InDesign, PDF-korrektur. Inget svenskt branschverktyg. FRAGMENTERAT
3. **Produktion** — InDesign, EPUB3, ljudboksstudior, AI-röster, tryckeriportaler. DELVIS
4. **Metadata** — Bokinfo (ONIX, Thema) obligatorisk nod. UPPTAGET
5. **Distribution** — Förlagssystem, Speed/Stardist, Publit, Bokinfo digital, Publizon/WeDoBooks. UPPTAGET
6. **Försäljning & marknad** — Bokinfo order, kundportaler, statistiken. DELVIS
7. **Royalty & avräkning** — Bokdata, Förlagsekonomi, Edda Pay, Fortnox — och mycket Excel. FRAGMENTERAT

## Branschinfrastruktur

**Bokinfo** (6 anställda, icke vinstdrivande): Bokinfo metadata (ONIX/Thema, EDItEUR), Bokinfo order (splittar order till distributörer), Bokinfo digital (e-bok/ljudbok metadata+filer till streaming och bibliotek), Bokinfo VCD (varucertifikat till ICA), Bokförsäljningsstatistiken (sedan 2014, ISBN-nivå). ONIX- och Thema-grupp möts två gånger per år och är öppen för nya deltagare. Titelavgiften har höjts flera gånger (2024, feb 2025) — kännbart för småförlag.

**KB**: ISBN, nationalbibliografi, e-plikt, Utgivningspuls.

**Nordisk jämförelse**: Norges Bokbasen är kommersiell (Meta, DDS, Bokskya, Søk 199 NOK/mån/användare) — strukturell kontrast mot Bokinfos icke-vinstmodell. Finland: Kirjavälitys. Danmark: Publizon.

## Förlagens kärnsystem

| System | Ursprung | Täcker | Svenska användare |
|---|---|---|---|
| Mockingbird | Bonnierförlagen 2015; eget bolag 2022 med Storytel Books | Hela produktlivscykeln | Bonnierförlagen, Storytel Books, Norstedts, Natur & Kultur |
| Bokdata | Svenskt fristående | Produktion, metadata, royalty, försäljningsimport, Insights, Fortnox | Pirat, WAPI, Tukan, Mondial |
| Klopotek | Tyskland | Full publishing-ERP | Inga funna |
| knk | Tyskland (Dynamics 365) | ERP, rights & royalties | Inga funna |
| Virtusales BiblioSuite | UK | Title mgmt, ONIX, royalty, licensiering | Inga funna |
| Excel/egenbyggt | — | Allt | Merparten av små förlag |

Mockingbird Publishing Software AB: 11 anställda, 15,4 Mkr omsättning 2025 (+58,5 %), -1,4 Mkr resultat, dotterbolag till Bonnier Books Group Holding. Uttalad ambition att sälja externt.

## Distribution

**Fysisk:** Förlagssystem (60 000+ titlar, ~1 000 förlag, kundportal + FS-Butiken, delägare i Bokinfo); Speed Group/Speed Logistics (köpte Samdistribution från Bonnier 2018, samarbetar med Publit); Stardist (fd StjärnDistribution, ordnar Bokinfo-anslutning åt småförlag); tryckerier Scandbook, Livonia, ScandinavianBook.

**Digital:** Elib → Axiell Media → Publizon (2023) → WeDoBooks (Biblio, Bookbites, Libreka 2025; kontor Sthlm/Kbh/Aarhus/Jyväskylä; förlagen jobbar i Elib Admin). Bokinfo digital. Publit: POD, lager via Speed, webbshop, distribution till Storytel/BookBeat/Nextory/OverDrive. Publit prismodell: 10 % av nettointäkt via återförsäljare, 20 % egen webbshop, 249 kr utgivningsavgift. Publit Sweden AB: 53,2 Mkr omsättning 2025, 11 anställda, litet minus.

**Streamingtjänsternas portaler:** Storytel Publisher Portal med leveranskrav för ljudfiler, e-böcker, metadata, ISBN, omslag, AI-genererat innehåll och EAA. BookBeat och Nextory har motsvarande. Flera parallella leveransgränssnitt = konkret friktion.

## Produktion

Ingen svensk branschstandard. Word/Google Docs → InDesign → EPUB3 (ur InDesign eller köpt konvertering). Ljudbok: Storytel köpte Earselect 2020, driver Storyside; Voice Switcher med AI-röster på svenska 2024; Natur & Kultur släppte "första" svenska AI-röst-ljudboken 2024. DAM: Mediaflow, QBank (generella, ej förlagsspecifika). Bokinfo har egen bildbank för omslag.

**Tillgänglighetslagen (2023:254)** + förordning 2023:676 + MTM:s föreskrifter KRFS 2025:1, gäller e-böcker och läsprogramvara från 28 juni 2025. Funktionella krav, ingen harmoniserad teknisk standard utpekad. Tillgänglighetsmetadata ska med i ONIX.

## Rättigheter, royalty och ekonomi

Problembild: författare väntar upp till 18 månader på ersättning; förlag saknar samlad kanalöverblick; avräkningsfiler i olika format och valutor; manuell redovisning. DSM-direktivets transparenskrav skärper.

- **Bokdata Royalty & Rights** — avtal till redovisning, royaltystegar, garantihonorar, vinstdelning, attestflöden, Fortnox.
- **Förlagsekonomi** — redovisningsbyrå specialiserad på förlag sedan 2006, författarportal, flervaluta. Majoritetsägd av Bokdata.
- **Edda Pay** — realtidsdata över kanaler (fas 1) + flexibla författarutbetalningar (fas 2).
- **Mockingbird** — inbyggt för sina förlag.
- **Fortnox/Visma** — bokföringsgrund utan förlagslogik.

Tre svenska aktörer arbetar på samma problem från olika håll. Inget svenskt systemstöd hittat för rights/licensiering hos agenturer (Bonnier Rights, Salomonsson, Ahlander syns inte som referenskunder).

## Angränsande segment

**Tidskrifter/dagspress**
- Prenumeration/CRM: Flowy, Nätverkstan, Piano, Pliro, Preno, Sesamy, Tulo PayWay, Unseald
- E-tidning: Prenly (~90 % av dagstidningarna), Issuu, e-magin (Adeprimo), PageSuite, Visiolink
- Redaktionella system: Naviga (fd Infomaker, Umeå) — Naviga Content, Newspilot; Stibo DX
- Aggregatorer: Readly, ARCY (Bonnier News), Pling (Aller), Flipp (Story House Egmont)
- Sveriges Tidskrifter: ~330 medlemmar

**Läromedel**: egna plattformar hos Gleerups, Liber, NE, Studentlitteratur (digital studieplattform 2022), Natur & Kultur. Skolon är aggregator/distributionslager mot skolorna, med kontrakt i Addas ramavtal.

## Segmentering (hypotes — verifiera)

| Segment | Antal | Kärnsystem | Distribution | Royalty | Betalningsvilja |
|---|---|---|---|---|---|
| Förlagsgrupper | 4–6 | Mockingbird | Egen/Förlagssystem | Mockingbird | Hög men låst |
| Etablerade medelstora | ~50–60 | Bokdata, egenbyggt, Excel | Förlagssystem, Speed | Bokdata/Förlagsekonomi | Rimlig — köparna finns här |
| Små förlag | Hundratals | Excel + Bokinfo | Stardist, Publit, Speed | Excel/byrå | Låg per enhet |
| Mikro/egenutgivare | Tusentals | Inget | Publit, Bookea, BoD, Whip Media | Ingen | Bara transaktionsbaserad |

## Vita fläckar — hypoteser med intervjutest

- **H1 Kanalavstämning.** Avräkningar från Storytel/BookBeat/Nextory/Publit/bibliotek/utland i olika format och valutor. *Test: hur många timmar per kvartal, och vem gör det?*
- **H2 Tillgänglighet som tjänst.** Lagkrav sedan juni 2025 utan teknisk standard. *Test: vad gjorde ni inför 28 juni 2025, vem kontrollerar era EPUB-filer?*
- **H3 Rättighetsregister för agenturer.** Inget svenskt systemstöd funnet. *Test: var ligger info om sålda rättigheter, territorier, löptider?*
- **H4 Redaktionellt arbetsflöde.** Steg 1–2 saknar branschverktyg. *Test: beskriv vägen från antagning till tryckfärdig fil — var tappas tid?*
- **H5 Ljudboksproduktionens verktygskedja.** En tredjedel av intäkterna, obefintligt verktygsstöd hos små förlag. *Test: hur beställer och kvalitetssäkrar ni en produktion?*
- **H6 Långsvansens administration.** Låg betalningsvilja per förlag → bara transaktions-/självbetjäningsmodell fungerar. *Test: vad betalar ni idag, vid vilket pris byter ni?*

## Strategiska randvillkor

- Bygg mot Bokinfo, inte bredvid. ONIX/Thema-gruppen är en billig väg in i branschsamtalet.
- Sverige ensamt räcker inte — tänk nordiskt från början (Bokbasen, Publizon/WeDoBooks, Kirjavälitys).
- Domänkunskap är inträdesbiljetten. Mockingbird och Edda Pay kommer båda inifrån branschen.

## Osäkerheter

- Boktugg och Svensk Bokhandel är delvis betalvägg — teckna prenumeration före intervjuerna.
- Kartläggningen av försäljningsprocessen på forlaggare.se (uppladdad 2022) beskriver 2000-talets andra hälft (Bokia, Megadisc, Nielsen BookScan) — historik, inte nuläge.
- Marknadsstorlek förväxlas lätt: en automatisk sammanfattning angav 55,2 mdr; korrekt är 5,15 mdr (2024) resp. ca 5,5 mdr (2025).
- Mockingbirds försäljning utanför Bonnier/Storytel-sfären ej verifierad.
- Segmentsantalen är uppskattningar — ersätt med tal ur KB:s ISBN-register.
- Bokinfos och Publizons aktuella prislistor ej lästa.

## Nästa steg

1. Läs *Det digitala genombrottet* (SvF 2024) i sin helhet.
2. Hämta antal aktiva utgivare ur KB:s ISBN-register.
3. Boka demo hos Bokdata och Publit.
4. Kontakta Bokinfo om ONIX/Thema-gruppen.
5. Bokmässan — Edda Pay och Whip Media finns i utställarlistan.
