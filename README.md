# Automation

A catch all repository for some useful scripts I've put together along the way.

## Best Buy Bot

A bot for buying things on <http://www.bestbuy.com>. It comes pre-configured for buying a [Nintendo Switch](https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255 "Neon Red Neon Blue Nintendo Switch").

Built on top of the Selenium and Twilio APIs.

Runs in a loop and attempts to add an item to your cart. On the first run, the bot will log you in and persist your session. Subsequent attempts will therefore not require the initial login step, making runs faster and more likely to succeed.

Once an item is added to your cart, the bot will send you a text, at which point you can go onto the best buy website and complete the purchase.

### Setup

#### Best Buy Website

I recommend doing the following on best buy's website before proceeding:

1. create an account.
2. add a payment method.
3. add your billing and shipping information.

#### Twilio

1. Create a free [Twilio](https://twilio.com) account.

#### Environment

- Python: 3+
- Chrome Driver: 81.0.4044.69 ([Download](https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.69/))

#### Dependencies

Run the following command to install python dependencies:

```bash
pip3 install -r requirements.txt

```

For best results, I recommended using both venv and pyenv.

### Configuration

Must add a `config.yml` to the root of this project in the following format:

```yaml
best_buy:
  user: "best buy user name"
  password: "best buy password"
twilio:
  sender: "phone number"
  account_sid: "twilio account sid"
  auth_token: "twilio auth token"
```

The twilio account_sid and auth_token should be copied from the [twilio console](https://www.twilio.com/console).

### Run

```bash
python3 best_buy.py [target product] [recipient phone number]
```

| argument                    | description                        | example                                      |
| --------------------------- |------------------------------------| ---------------------------------------------|
| target product              | product page url or macro.         | `neon` or `https://www.bestbuy.com/site/xxx` |
| recipient phone number      | phone number for recieving texts.  | +11234567890                                 |

### Macro Map

- `grey`: <https://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253>
- `neon`: <https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255>
- `ac`: <https://www.bestbuy.com/site/nintendo-switch-animal-crossing-new-horizons-edition-32gb-console-multi/6401728.p?skuId=6401728>,
- `test`: <https://www.bestbuy.com/site/animal-crossing-new-horizons-nintendo-switch/5723316.p?skuId=5723316>

### Extensibility

This bot has been constructed in such a way that it should be trivial to replace the underlying components for (1) interacting with the best buy website and (2) alerting when an "Add to Cart" action has succeeded.