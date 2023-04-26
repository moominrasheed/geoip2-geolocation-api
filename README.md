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

## API Endpoint

### `/geolocation` [GET]

- Query Parameter:
  - `ip`: The IP address for which geolocation information is requested.

- Response:
  - The API returns a JSON response with the following fields:
    - `as`: The autonomous system organization (ASO) associated with the IP address.
    - `city`: The city name associated with the IP address.
    - `country`: The country name associated with the IP address.
    - `countryCode`: The ISO code of the country associated with the IP address.
    - `lat`: The latitude associated with the IP address.
    - `lon`: The longitude associated with the IP address.
    - `org`: The organization name associated with the IP address.
    - `query`: The IP address for which geolocation information is requested.
    - `province`: The province name associated with the IP address.
    - `status`: The status of the geolocation lookup (e.g., "success").
    - `timezone`: The timezone associated with the IP address.
    - `zip`: The postal code associated with the IP address.

```python
# Example response
{
  "as": "Example ASO",
  "city": "Example City",
  "country": "Example Country",
  "countryCode": "EX",
  "lat": 12.3456,
  "lon": -78.9012,
  "org": "Example Organization",
  "query": "192.168.1.1",
  "province": "Example Province",
  "status": "success",
  "timezone": "America/New_York",
  "zip": "12345"
}
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
