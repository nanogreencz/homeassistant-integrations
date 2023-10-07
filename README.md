# Home Assistent Nanogreen Integrace

## Instalace

1. Nainstalujte HACS pomocí [oficiálního návodu](https://hacs.xyz/docs/setup/prerequisites).
2. Zrestartujte Home Assistenta.
3. Přidejte Nano Green repozitář.

Klikněte na "HACS" v levém menu.

Klikněte na "Integrations".

![přidání repozitáře krok 1](docs/installation/pridani_repozitare_1.png)

Klikněte na tři tečky v pravém horním rohu obrazovky.

Klikněte na "Custom repositories".

![přidání repozitáře krok 2](docs/installation/pridani_repozitare_2.png)

Do pole "Repository" přidat `https://github.com/nanogreencz/homeassistant-integrations`.

Ve výběru "Category" vybrat `Integration`.

Klikněte na "Add".

![přidání repozitáře krok 3](docs/installation/pridani_repozitare_3.png)

Repozitář by se vám měl zobrazit mezi ostatními repozitáři.

![přidání repozitáře krok 3](docs/installation/pridani_repozitare_4.png)

4. Stáhněte Nano Green integraci.

![stáhnutí integrace krok 1](docs/installation/stahnuti_integrace_1.png)

![stáhnutí integrace krok 2](docs/installation/stahnuti_integrace_2.png)

![stáhnutí integrace krok 3](docs/installation/stahnuti_integrace_3.png)

5. Zrestartujte Home Assistenta.

6. Nainstalujte Nano Green integraci pomocí Home Assistent settings menu.

![instalace integrace krok 1](docs/installation/instalace_integrace_1.png)

![instalace integrace krok 2](docs/installation/instalace_integrace_2.png)

## Sensory

| ID                                      | Popis                                                                                                                                   |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `current_market_price`                  | Současná tržní cena silové elektřiny.                                                                                                   |
| `current_consumption_price`             | Spotřební cena silové el. po odečtení poplatků podle aktuálního ceníku, bez DPH.                                                        |
| `current_consumption_price_incl_vat`    | Spotřební cena silové el. po odečtení poplatků podle aktuálního ceníku, včetně DPH.                                                     |
| `current_production_price_with_nano`    | Výkupní cena silové el. při současném odběru elektřiny od Nano Green po odečtení poplatku za služby obchodu ve výši 600 Kč/MWh bez DPH. |
| `current_production_price_without_nano` | Výkupní cena silové el. při odběru elektřiny od jiného dodavatele po odečtení poplatku za služby obchodu ve výši 900 Kč/MWh bez DPH.    |
| `today_base_cheapest_hour`              | Dnešní nejlevnější hodina za celý den.                                                                                                  |
| `today_peak_cheapest_hour`              | Dnešní nejlevnější hodina v energetické špičce.                                                                                         |
| `today_offpeak_cheapest_hour`           | Dnešní nejlevnější hodina mimo energetickou špičku.                                                                                     |
| `today_base_second_cheapest_hour`       | Dnešní druhá nejlevnější hodina za celý den.                                                                                            |
| `today_peak_second_cheapest_hour`       | Dnešní druhá nejlevnější hodina v energetické špičce.                                                                                   |
| `today_offpeak_second_cheapest_hour`    | Dnešní druhá nejlevnější hodina mimo energetickou špičku.                                                                               |
| `is_currently_cheapest_hour`            | Binární sensor. Zapnutý, pokud je nejlevnější hodina elektřiny z celého dne.                                                            |
| `is_currently_second_cheapest_hour`     | Binární sensor. Zapnutý, pokud je druhá nejlevnější hodina elektřiny z celého dne.                                                      |
| `is_currently_third_cheapest_hour`      | Binární sensor. Zapnutý, pokud je třetí nejlevnější hodina elektřiny z celého dne.                                                      |
| `is_currently_fourth_cheapest_hour`     | Binární sensor. Zapnutý, pokud je čtvrtá nejlevnější hodina elektřiny z celého dne.                                                     |
| `is_currently_fifth_cheapest_hour`      | Binární sensor. Zapnutý, pokud je pátá nejlevnější hodina elektřiny z celého dne.                                                       |
| `is_currently_sixth_cheapest_hour`      | Binární sensor. Zapnutý, pokud je šestá nejlevnější hodina elektřiny z celého dne.                                                      |
| `is_currently_in_two_cheapest_hours`    | Binární sensor. Zapnutý, pokud je jedna ze dvou nejlevnějších hodin elektřiny z celého dne.                                             |
| `is_currently_in_three_cheapest_hours`  | Binární sensor. Zapnutý, pokud je jedna ze tří nejlevnějších hodin elektřiny z celého dne.                                              |
| `is_currently_in_four_cheapest_hours`   | Binární sensor. Zapnutý, pokud je jedna ze čtyř nejlevnějších hodin elektřiny z celého dne.                                             |
| `is_currently_in_five_cheapest_hours`   | Binární sensor. Zapnutý, pokud je jedna z pěti nejlevnějších hodin elektřiny z celého dne.                                              |
| `is_currently_in_six_cheapest_hours`    | Binární sensor. Zapnutý, pokud je jedna z šesti nejlevnějších hodin elektřiny z celého dne.                                             |

Vysvětlení:

Kromě silové elektřiny ještě platíte za distribuci podle vašeho distribučního území ČEZ, PRE nebo EG.d a distribučního tarifu. Některé tarify mají dvě ceny NT/VT (nesouvisí s časy Peak/OffPeak spotu).
Distribuce se platí pro nákup i prodej. V ČR, jako jediné zemi na světě, je měření po fázích zvlášť. Pokud máte na jedné fázi prodej a na druhé nákup, za prodej platíte. Za distribuci platíte pro oba směry.

PEAK LOAD (8:00 - 20:00)

OFFPEAK LOAD (0:00 - 8:00, 20:00 - 24:00)

## Grafy

### Cena elektřiny

![Graf ceny elektřiny](docs/examples/graf.png)

- Po nainstalování [ApexCharts](https://github.com/RomRider/apexcharts-card) přes HACS dle návodu, přidejte vlastní komponentu a vložte do ní níže uvedený kód.

```yaml
type: custom:apexcharts-card
header:
  show: true
  title: Cena elektriny dnes
  show_states: true
  colorize_states: true
series:
  - entity: sensor.current_market_price_czk_kwh
    data_generator: |
      return entity.attributes.today_hourly_prices.map((price, index) => {
        const date = new Date()
        date.setHours(index)
        date.setMinutes(0)
        date.setSeconds(0)
        return [date, price];
      });
    show:
      in_header: before_now
graph_span: 24h
span:
  start: day
```

- také si můžete do grafu dát cenu spotřeby včetně všech poplatků a DPH a i na další den dopředu

```yaml
type: custom:apexcharts-card
header:
  show: true
  title: Cena elektriny s DPH a poplatky
  show_states: true
  colorize_states: true
series:
  - entity: sensor.current_market_price_czk_kwh
    data_generator: >
      return
      [...entity.attributes.today_hourly_consumption_prices_incl_vat.map((price,
      index) => {
        const date = new Date()
        date.setHours(index)
        date.setMinutes(0)
        date.setSeconds(0)
        return [date, price];
      }), ...entity.attributes.tomorrow_hourly_prices_incl_vat.map((price,
      index) => {
        const date2 = new Date()
        date2.setDate(date2.getDate()+1)
        date2.setHours(index)
        date2.setMinutes(0)
        date2.setSeconds(0)
        return [date2, price];
      })];
    show:
      in_header: before_now
now:
  show: true
graph_span: 48h
span:
  start: day
```
