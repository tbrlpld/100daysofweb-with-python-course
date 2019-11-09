import quart
from services import weather_service, sun_service, location_service

blueprint = quart.blueprints.Blueprint(__name__, __name__)


@blueprint.route('/api/events/<city>/<state>/<country>', methods=['GET'])
def events(city: str, state: str, country: str):
    player = {
        "name": "Jeff the player",
        "city": city,
        "state": state,
        "country": country,
    }
    if not player:
        quart.abort(404)
    return quart.jsonify(player)


@blueprint.route('/api/weather/<zip_code>/<country>', methods=['GET'])
async def weather(zip_code: str, country: str):
    weather_data = await weather_service.get_current(zip_code, country)
    if not weather_data:
        quart.abort(404)
    return quart.jsonify(weather_data)


@blueprint.route('/api/sun/<zip_code>/<country>', methods=['GET'])
def sun(zip_code: str, country: str):
    lat, long = location_service.get_lat_long(zip_code, country)
    sun_data = sun_service.for_today(lat, long)
    if not sun_data:
        quart.abort(404)
    return quart.jsonify(sun_data)
