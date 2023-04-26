from flask import Flask, request, jsonify
from maxminddb import open_database

app = Flask(__name__)

# Load GeoIP2 City database
city_db_path = 'GeoLite2-City.mmdb'  # Path to your downloaded GeoLite2-City database
city_geoip_db = open_database(city_db_path)

# Load GeoIP2 Country database
country_db_path = 'GeoLite2-Country.mmdb'  # Path to your downloaded GeoLite2-Country database
country_geoip_db = open_database(country_db_path)

# Load GeoIP2 ASN database
asn_db_path = 'GeoLite2-ASN.mmdb'  # Path to your downloaded GeoLite2-ASN database
asn_geoip_db = open_database(asn_db_path)

@app.route('/geolocation', methods=['GET'])
def get_geolocation():
    ip_address = request.args.get('ip')  # Get IP address from query parameter

    # Perform GeoIP City lookup
    city_result = city_geoip_db.get(ip_address)
    city = city_result.get('city', {}).get('names', {}).get('en')

    # Perform GeoIP Country lookup
    country_result = country_geoip_db.get(ip_address)
    country = country_result.get('country', {}).get('names', {}).get('en')
    iso_code = country_result.get('country', {}).get('iso_code')
    subdivisions = country_result.get('subdivisions', {})
    timezone = city_result.get('location', {}).get('time_zone')

    # Perform GeoIP ASN lookup
    asn_result = asn_geoip_db.get(ip_address)
    aso = asn_result.get('autonomous_system_organization')

    # Get province value from subdivisions field
    province = subdivisions[0].get('names', {}).get('en') if subdivisions else None

    # Construct response with desired fields
    response = {
        'as': aso or None,
        'city': city,
        'country': country,
        'countryCode': iso_code,
        'lat': city_result.get('location', {}).get('latitude'),
        'lon': city_result.get('location', {}).get('longitude'),
        'org': aso or None,
        'query': ip_address,
        'province': province.get('en') if province else None,  # Extract 'en' value from province
        'status': 'success',
        'timezone': timezone,
        'zip': city_result.get('postal', {}).get('code')
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
