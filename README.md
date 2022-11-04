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

| Jméno                                           | ID                                                     |
| ----------------------------------------------- | ------------------------------------------------------ |
| `Current kWh price in CZK`                      | `sensor.current_kwh_price_in_czk`                      |
| `Is currently cheapest electricity hour in day` | `sensor.is_currently_cheapest_electricity_hour_in_day` |
| `Base cheapest hour`                            | `sensor.base_cheapest_hour`                            |
| `Base second cheapest hour`                     | `sensor.base_second_cheapest_hour`                     |
| `Offpeak cheapest hour`                         | `sensor.offpeak_cheapest_hour`                         |
| `Offpeak second cheapest hour`                  | `sensor.offpeak_second_cheapest_hour`                  |
| `Peak cheapest hour`                            | `sensor.peak_cheapest_hour`                            |
| `Peak second cheapest hour`                     | `sensor.peak_second_cheapest_hour`                     |

Vysvětlení:

PEAK LOAD (8:00 - 20:00)

OFFPEAK LOAD (0:00 - 8:00, 20:00 - 24:00)

## Grafy

### Cena elektřiny

![Graf ceny elektřiny](docs/examples/graf.png)

- Po nainstalování [ApexCharts](https://github.com/RomRider/apexcharts-card) přes HACS de návodu, přidejte custom komponentu a vložte do ní níže uvedený kód.

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
        const date = new Date().setHours(index)
        return [date, price];
      });
graph_span: 24h
span:
  start: day
```
