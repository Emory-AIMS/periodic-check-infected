# Step 1 - Requirements
The machine must have access to doctor-infected queue

The following packages should be installed:
```
apt-get update && apt-get -y install python3-pip
pip3 install -r requirements.txt
```

# Step 2 - Configuring 
Copy the config file and fill the values.
```bash
cp config.template.py config.py
```
To test, run:
```bash
python3 main.py
```

# Step 3 - Setup service
Configuring to run every 5 minutes with user `ubuntu`:
```bash
echo "*/5 * * * * ubuntu python3 ~/infected-logger/main.py &>> ~/infected-logger/infected-logger.log" |  sudo tee   /etc/cron.d/infected-logger
```
