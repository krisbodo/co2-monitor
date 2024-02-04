# co2-monitor

Monitoring indoors carbon dioxide concentration with a raspberry pi

## Setup

### Physical setup
The project is set up using a raspberry pi zero W and a SGP30 eCO2 monitor, with a headless setup.

### Installation
Clone the repository and install the requirements (on the raspberry pi):

```bash
git clone https://github.com/krisbodo/co2-monitor
cd co2-monitor
pip install -r requirements.txt
```

### Push notifications
It's currently set up to send push notifications using the [Pushover](https://pushover.net/) free trial. You will need to create a `.env` file at the root of the project folder and store the user key and the application token on it like this:

```python
PUSHOVER_USER_KEY="<PASTE YOUR USER KEY>"
PUSHOVER_APP_TOKEN="<PASTE YOUR APP TOKEN>"
```