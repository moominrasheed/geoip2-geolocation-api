# GeoIP2 Geolocation API

This is a Flask web application that provides geolocation information for a given IP address using MaxMind's GeoIP2 databases.

## Setup

1. Install dependencies using `pip`:

```bash
pip install flask maxminddb
```

2. Download the GeoIP2 databases from MaxMind's website:

- [GeoLite2-City.mmdb](https://dev.maxmind.com/geoip/geoip2/geolite2/)
- [GeoLite2-Country.mmdb](https://dev.maxmind.com/geoip/geoip2/geolite2/)
- [GeoLite2-ASN.mmdb](https://dev.maxmind.com/geoip/geoip2/geolite2/)

3. Update the paths to the downloaded databases in the `city_db_path`, `country_db_path`, and `asn_db_path` variables in the `app.py` file:

```python
city_db_path = 'GeoLite2-City.mmdb'
country_db_path = 'GeoLite2-Country.mmdb'
asn_db_path = 'GeoLite2-ASN.mmdb'
```

4. Start the Flask application:

```bash
python app.py
```

## Deployment

The GeoIP2 Geolocation API can be deployed in various ways, depending on your requirements and preferences. Here are a few options:

### Local Development

For local development, you can simply run the Flask application on your local machine using the `python app.py` command as mentioned in the setup section.

### Virtual Environment

You can create a virtual environment for the Flask application and deploy it in a virtual environment. Here's an example:

1. Create and activate a virtual environment:

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

2. Install dependencies inside the virtual environment:

```bash
pip install flask maxminddb
```

3. Update the paths to the downloaded databases in the `city_db_path`, `country_db_path`, and `asn_db_path` variables in the `app.py` file.

4. Start the Flask application:

```bash
python app.py
```

### Docker

You can also deploy the GeoIP2 Geolocation API in a Docker container. Here's an example:

1. Install Docker on your machine following the [official Docker documentation](https://docs.docker.com/get-docker/).

2. Build a Docker image from the provided Dockerfile:

```bash
docker build -t geoip2-api .
```

3. Run a Docker container from the built image:

```bash
docker run -p 5000:5000 -d geoip2-api
```

This will run the Flask application inside a Docker container, and you can access it at `http://localhost:5000` in your web browser.

## API Endpoint

[API endpoint details here]

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
