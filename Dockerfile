FROM python:3.10-slim-buster

# Updating apt to see and install Google Chrome
RUN apt-get -y update
RUN apt install -y unzip wget
RUN apt install -y libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 
RUN apt install -y chromium


# adiciona o diretório raiz no container
WORKDIR /app

# instala dependências
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copia projeto para a imagem
COPY . .

# Download the Chrome Driver
#RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
# Unzip the downloaded ChromeDriver binary
#RUN unzip chromedriver_linux64.zip
#RUN mkdir -p /root/.cache/selenium/chromedriver/linux64/124.0.6367.201/
#RUN mv chromedriver /root/.cache/selenium/chromedriver/linux64/124.0.6367.201/

# run
CMD [ "python3", "-m" , "flask", "--app", "server", "run", "--host=0.0.0.0", "--debug"]