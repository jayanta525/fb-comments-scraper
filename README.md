# Scrape Facebook Posts comments without API

*Updated as on 23 March 2023*

- Docker Image: [docker/jayanta525/fb-comments-scraper](https://hub.docker.com/r/jayanta525/fb-comments-scraper/)
- Depends on: [docker/jayanta525/python3-chromedriver](https://hub.docker.com/r/jayanta525/python3-chromedriver/)

Uses 
* Docker
* BeautifulSoap
* Selenium
* ChromeDriver

# Usage

```
usage: main.py [-h] credentials_file input_file out_dir

Facebook Post Comments Scrapper

positional arguments:
  credentials_file  A txt file with username and password
  input_file        A input file with list of urls
  out_dir           Output directory to store the comments

options:
  -h, --help        show this help message and exit
```

## Run the docker container directly

### Prerequisites
* credentials file
* posts url file
* output directory

### Sample Files


- credentials.txt
    ```
    email = "abc@gmail.com"
    password = "MySuperSecretPassword"
    ```

- posts_url.txt
    ```
    http://facebook.com/****
    http://facebook.com/1212
    http://m.facebook.com       <----Mobile links not supported
    #http://facebook.com        <----Comment URLs with #, ignore
    ```

### Start the container

- Get the live output and to delete the container after each run
    ```
    docker run -v `pwd`:/app -it --rm jayanta525/fb-comments-scraper:v1 credentails.txt posts_url.txt out/
    ```
- To run as daemon(background) - use at your own risk, error logs are not recorded
    ```
    docker run -v `pwd`:/app -d jayanta525/fb-comments-scraper:v1 credentails.txt posts_url.txt out/
    ```


### Use with Github Actions - CI/CD

> TODO